from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1050.bin",                # FileName
        "t1050",                    # MapName
        "t1050",                    # Location
        0x0043,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1050",                  # 0
        "Manager Haggar",         # 1
        "Lottie",                 # 2
        "Citrus",                 # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Wazy",                   # 6
        "Toma",                   # 7
        "Alvina",                 # 8
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25600.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch20400.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch20200.itc",                   # 05
        "chr/ch20300.itc",                   # 06
        "chr/ch08000.itc",                   # 07
    ))

    DeclNpc(-479,    0,       10050,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-100709, 0,       8859,    270,  257,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-101819, 0,       8859,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(8970,    0,       6630,    225,  385,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(8250,    0,       5920,    45,   385,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   7,   0,   0,   3,   255, 255, 255,  0)
    DeclNpc(96220,   0,       121949,  270,  261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(103230,  0,       124330,  0,    261,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(-20,     0,       8270,    1500,    -480,    1500,    10050,   0x007E, 0,  7,  0x0000)
    DeclActor(5500,    0,       13500,   1200,    5500,    1500,    13500,   0x007C, 0,  28, 0x0000)
    DeclActor(-99830,  0,       13590,   1200,    -99830,  1500,    13590,   0x007C, 0,  29, 0x0000)
    DeclActor(-96600,  0,       120560,  1500,    -96600,  1000,    120560,  0x007C, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_29C",          # 00, 0
        "Function_1_354",          # 01, 1
        "Function_2_3B5",          # 02, 2
        "Function_3_416",          # 03, 3
        "Function_4_495",          # 04, 4
        "Function_5_549",          # 05, 5
        "Function_6_583",          # 06, 6
        "Function_7_617",          # 07, 7
        "Function_8_61B",          # 08, 8
        "Function_9_A4D",          # 09, 9
        "Function_10_CE8",         # 0A, 10
        "Function_11_EA4",         # 0B, 11
        "Function_12_FC7",         # 0C, 12
        "Function_13_1647",        # 0D, 13
        "Function_14_19FB",        # 0E, 14
        "Function_15_1AD9",        # 0F, 15
        "Function_16_1B4C",        # 10, 16
        "Function_17_25F5",        # 11, 17
        "Function_18_260A",        # 12, 18
        "Function_19_268D",        # 13, 19
        "Function_20_48D6",        # 14, 20
        "Function_21_491B",        # 15, 21
        "Function_22_497E",        # 16, 22
        "Function_23_49E1",        # 17, 23
        "Function_24_4A26",        # 18, 24
        "Function_25_4A6B",        # 19, 25
        "Function_26_56AD",        # 1A, 26
        "Function_27_6A36",        # 1B, 27
        "Function_28_71AD",        # 1C, 28
        "Function_29_7253",        # 1D, 29
    ))


    def Function_0_29C(): pass

    label("Function_0_29C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2DC"),
        (1, "loc_2E8"),
        (2, "loc_2F4"),
        (3, "loc_300"),
        (4, "loc_30C"),
        (5, "loc_318"),
        (6, "loc_324"),
        (SWITCH_DEFAULT, "loc_330"),
    )


    label("loc_2DC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_2E8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_2F4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_300")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_30C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_318")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_324")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_330")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_33C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_353")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_353")

    Return()

    # Function_0_29C end

    def Function_1_354(): pass

    label("Function_1_354")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B4")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_354")

    label("loc_3B4")

    Return()

    # Function_1_354 end

    def Function_2_3B5(): pass

    label("Function_2_3B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_415")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_2_3B5")

    label("loc_415")

    Return()

    # Function_2_3B5 end

    def Function_3_416(): pass

    label("Function_3_416")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_494")
    SetScenarioFlags(0xAA, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0xA)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -100040, 0, 13630, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)

    label("loc_494")

    Return()

    # Function_3_416 end

    def Function_4_495(): pass

    label("Function_4_495")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AF")
    Event(0, 19)

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4BD")
    Jump("loc_548")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_548")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4D9")
    Jump("loc_548")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4E7")
    Jump("loc_548")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_548")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_531")
    SetChrPos(0x9, -93960, 0, 8260, 0)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 94190, 0, 11580, 0)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_548")

    label("loc_531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_53F")
    Jump("loc_548")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_548")

    label("loc_548")

    Return()

    # Function_4_495 end

    def Function_5_549(): pass

    label("Function_5_549")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_582")
    EndChrThread(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    label("loc_582")

    Return()

    # Function_5_549 end

    def Function_6_583(): pass

    label("Function_6_583")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FA")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_5FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_616")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_616")

    Return()

    # Function_6_583 end

    def Function_7_617(): pass

    label("Function_7_617")

    Call(0, 8)
    Return()

    # Function_7_617 end

    def Function_8_61B(): pass

    label("Function_8_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_631")
    Call(0, 16)
    Jump("loc_A4C")

    label("loc_631")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_642")
    Jump("loc_A49")

    label("loc_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_650")
    Jump("loc_A49")

    label("loc_650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_65E")
    Jump("loc_A49")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_66C")
    Jump("loc_A49")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_A49")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_7D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_777")
    TurnDirection(0x8, 0x151, 0)

    ChrTalk(
        0x8,
        "Mr. Hemisphere, are you heading out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If so, we'd be more than happy to prepare\x01",
            "your room for your return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#5700FI might be out for a bit, so I would greatly\x01",
            "appreciate that, Haggar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Understood, sir.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7D3")

    label("loc_777")


    ChrTalk(
        0x8,
        (
            "Allow us to tidy up your room while\x01",
            "you're out, Mr. Hemisphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Have a great day.\x02",
    )

    CloseMessageWindow()

    label("loc_7D3")

    Jump("loc_A49")

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_867")

    ChrTalk(
        0x8,
        "Are you acquaintances of Mr. Hemisphere's?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you go through the door on the left,\x01",
            "his room is the first on the right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A49")

    label("loc_867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_A40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_974")

    ChrTalk(
        0x8,
        "Good day. Welcome to Hotel Delphinia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We had a major influx of guests today.\x01",
            "As always, it's our pleasure to host them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I assume the guests not currently here\x01",
            "are enjoying themselves, visiting\x01",
            "everything Mishelam has to offer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A3B")

    label("loc_974")


    ChrTalk(
        0x8,
        (
            "We had a major influx of guests today.\x01",
            "As always, it's our pleasure to host them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I assume the guests not currently here\x01",
            "are enjoying themselves, visiting\x01",
            "everything Mishelam has to offer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3B")

    Jump("loc_A49")

    label("loc_A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A49")

    label("loc_A49")

    TalkEnd(0x8)

    label("loc_A4C")

    Return()

    # Function_8_61B end

    def Function_9_A4D(): pass

    label("Function_9_A4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_A5E")
    Jump("loc_CE4")

    label("loc_A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_A6C")
    Jump("loc_CE4")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_A7A")
    Jump("loc_CE4")

    label("loc_A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_A88")
    Jump("loc_CE4")

    label("loc_A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_A96")
    Jump("loc_CE4")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_BD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6D")
    TurnDirection(0xFE, 0x151, 0)

    ChrTalk(
        0xFE,
        "P-Pardon me, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        "#5705FHmm? Did you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Oh, dear... He really is as handsome\x01",
            "as the others were saying.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        "#5702FHaha, aren't you the silly goose?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BCB")

    label("loc_B6D")


    ChrTalk(
        0xFE,
        "Are you going out, by chance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, have a pleasant and safe evening!\x01",
            "Hahahaha...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCB")

    Jump("loc_CE4")

    label("loc_BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_C2F")
    TurnDirection(0xFE, 0xA, 0)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        "Ah! I locked eyes with him!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Calm down, dear. It's okay.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_CE4")

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_CDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4A")
    Call(0, 11)
    Jump("loc_CD6")

    label("loc_C4A")


    ChrTalk(
        0xFE,
        "I only saw him when he checked in, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That guest was pretty cute... I'd love to\x01",
            "strike up a conversation with him, all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD6")

    Jump("loc_CE4")

    label("loc_CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_CE4")

    label("loc_CE4")

    TalkEnd(0xFE)
    Return()

    # Function_9_A4D end

    def Function_10_CE8(): pass

    label("Function_10_CE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_CF9")
    Jump("loc_EA0")

    label("loc_CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_D07")
    Jump("loc_EA0")

    label("loc_D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_D15")
    Jump("loc_EA0")

    label("loc_D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_D23")
    Jump("loc_EA0")

    label("loc_D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_D31")
    Jump("loc_EA0")

    label("loc_D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_DB3")

    ChrTalk(
        0xFE,
        (
            "Please, feel free to inform us of any\x01",
            "complaints you may have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This establishment always aims to improve.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA0")

    label("loc_DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_E0F")

    ChrTalk(
        0xFE,
        (
            "When will this girl learn? You can't act\x01",
            "like that in front of guests...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA0")

    label("loc_E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2A")
    Call(0, 11)
    Jump("loc_E92")

    label("loc_E2A")


    ChrTalk(
        0xFE,
        (
            "If she has enough free time to talk about\x01",
            "boys, she can use that time to sweep the\x01",
            "floors instead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E92")

    Jump("loc_EA0")

    label("loc_E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_EA0")

    label("loc_EA0")

    TalkEnd(0xFE)
    Return()

    # Function_10_CE8 end

    def Function_11_EA4(): pass

    label("Function_11_EA4")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    ChrTalk(
        0x9,
        (
            "Hey, did you see that looker just now?\x01",
            "I'd looove to clean his room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "He WAS a boy, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Again with the boys...\x01",
            "Instead of focusing on that, use that\x01",
            "energy of yours to finish sweeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Aw, come on. Aren't you the least bit curious...?\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_EA4 end

    def Function_12_FC7(): pass

    label("Function_12_FC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10AF")

    ChrTalk(
        0xFE,
        (
            "My plan to propose during the fireworks\x01",
            "show can still work now, luckily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll never be able to thank you enough, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's time for me to start mentally\x01",
            "preparing for tonight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1400")

    label("loc_10AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_130F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125B")

    ChrTalk(
        0xFE,
        (
            "I-I guess I'll make my way to Mishelam\x01",
            "Wonderland now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't get over my nerves... I've planned\x01",
            "out the entire proposal, but will I actually\x01",
            "be able to follow through?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know it took you a lot of pain and effort\x01",
            "to find my ring. With that as my courage,\x01",
            "I won't give up now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With that being said, I'm still going to\x01",
            "keep running through the proposal\x01",
            "in my head for practice...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_130A")

    label("loc_125B")


    ChrTalk(
        0xFE,
        (
            "'Please, my dear. Marry me!'\x01",
            "Maybe that one...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "'Let's get married!' ...That's not bad, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'Woman, just take the ring already\x01",
            "and marry me!' ...Maybe not.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130A")

    Jump("loc_1400")

    label("loc_130F")


    ChrTalk(
        0xFE,
        (
            "Well, it's time for me to start mentally\x01",
            "preparing for tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just wish I knew whether Alvina will say\x01",
            "yes or no already... This is a life or death\x01",
            "situation here, okay?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FCome on, you're exaggerating a little bit...\x02",
    )

    CloseMessageWindow()

    label("loc_1400")

    Jump("loc_1643")

    label("loc_1405")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_141A")
    Call(0, 27)
    Jump("loc_1643")

    label("loc_141A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_14CD")

    ChrTalk(
        0xFE,
        (
            "O-Okay, forget about that for now!\x01",
            "Could you go check around the\x01",
            "residential area for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might have dropped the ring\x01",
            "around that bench I sat at...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_14CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14EB")
    Call(0, 26)
    Jump("loc_1643")

    label("loc_14EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1509")
    Call(0, 26)
    Jump("loc_1643")

    label("loc_1509")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1527")
    Call(0, 26)
    Jump("loc_1643")

    label("loc_1527")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1640")

    ChrTalk(
        0xFE,
        (
            "I don't have any idea where I\x01",
            "dropped the ring...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The only lead I have is that Alvina\x01",
            "and I checked out a bunch of places\x01",
            "when we first arrived here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Anyway, if you find anything that\x01",
            "even resembles an engagement ring,\x01",
            "please come bring it to me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_1640")

    Call(0, 25)

    label("loc_1643")

    TalkEnd(0xFE)
    Return()

    # Function_12_FC7 end

    def Function_13_1647(): pass

    label("Function_13_1647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_16D2")

    ChrTalk(
        0xFE,
        "Toma can't hide his enthusiasm at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did something exciting happen to him\x01",
            "while I wasn't looking?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_16D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1789")

    ChrTalk(
        0xFE,
        (
            "Toma seems to be planning something\x01",
            "at Mishelam Wonderland for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not like it was hard to figure out. He couldn't\x01",
            "keep a secret hidden to save his life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_1789")


    ChrTalk(
        0xFE,
        (
            "I get asked why I'm dating Toma\x01",
            "too many times to keep up with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I look at Toma, see how he acts, how\x01",
            "he carries himself, I can't help but laugh.\x01",
            "And I think that's where his charm lies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1854")

    Jump("loc_19F7")

    label("loc_1859")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_191E")

    ChrTalk(
        0xFE,
        (
            "Toma, what's the matter with you?\x01",
            "All it's been is depressed looks\x01",
            "and panic attacks the entire day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Toma keeps telling me that it's\x01",
            "nothing, so I guess I'll let it go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F7")

    label("loc_191E")


    ChrTalk(
        0xFE,
        (
            "Toma and I have made plans to walk\x01",
            "around the theme park tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He told me that since there's going to be\x01",
            "a giant fireworks show, tonight will be full of\x01",
            "romance and excitement!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Heehee. I can't wait.\x02",
    )

    CloseMessageWindow()

    label("loc_19F7")

    TalkEnd(0xFE)
    Return()

    # Function_13_1647 end

    def Function_14_19FB(): pass

    label("Function_14_19FB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, is the sun already setting? I wish this\x01",
            "relaxing day with my wife could last forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Granted, I'm sure cheese and wine while\x01",
            "watching the fireworks show from our\x01",
            "room's window will be lovely as well.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_19FB end

    def Function_15_1AD9(): pass

    label("Function_15_1AD9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I sure am glad we decided to book\x01",
            "a hotel room in advance. I doubt we\x01",
            "would have got one if we didn't.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1AD9 end

    def Function_16_1B4C(): pass

    label("Function_16_1B4C")

    EventBegin(0x0)
    Fade(1000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -16950, 0, 11920, 45)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xD, 0x8000)
    OP_68(-240, 1100, 7180, 0)
    MoveCamera(327, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16470, 0)
    SetChrPos(0x101, -500, 0, 6400, 0)
    SetChrPos(0x102, 500, 0, 6400, 0)
    SetChrPos(0x103, 500, 0, 5000, 0)
    SetChrPos(0x104, -500, 0, 5000, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05700.itp")
    OP_0D()

    ChrTalk(
        0x8,
        "#3500440V#11PGood day. Welcome to Hotel Delphinia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500441V#11PAre you looking to stay with us tonight?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500442V#0100F#6PYes. Do you happen to have\x01",
            "any open rooms?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500443V#11PI'm terribly sorry, ladies and gentlemen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500444V#11PThe truth is, we had one cancellation\x01",
            "earlier today, but someone booked it\x01",
            "almost immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500445V#0106F#6PI was afraid of that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500446V#0206F#6PA shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500447V#0306F#6PThat's the way it goes, I guess. Might\x01",
            "as well walk on over to the restaurant.\x02\x03",
            "#3500448V#0300FWe can mull over everything there, eh?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E77():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E77)
    Sleep(50)

    def lambda_1E87():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E87)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3500449V#0006F#11PThat's about our only choice, yeah...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1437, 255, 100, 0)
    Sleep(700)

    NpcTalk(
        0xD,
        "Cool Voice",
        "#3500450V#4P#24AQuite the dilemma you're in, isn't it?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-1880, 1100, 6720, 5100)
    MoveCamera(307, 16, 0, 5100)

    def lambda_1F8F():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F8F)

    def lambda_1F9C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F9C)
    Sleep(50)

    def lambda_1FAC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FAC)

    def lambda_1FB9():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1FB9)
    Sleep(50)

    def lambda_1FC9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FC9)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0xA)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0xD, 3, 0, 17)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 1)
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
        "#3500451V#0005F#12PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500452V#0105F#12PW-Wazy? What are you doing here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500453V#2POh, Mr. Hemisphere...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(1435, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(700)

    AnonymousTalk(
        0xD,
        (
            "#3500454VSaid dilemma seems to be about getting\x01",
            "a room here, but...\x02\x03",
            "#3500455VAll you're looking for is a place to have a\x01",
            "nice, relaxing chat, right?\x02",
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

    ChrTalk(
        0x101,
        "#3500456V#0000F#12PBasically. But Wazy, what are you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500457V#5704F#5P#NAllow me to make things easier, then.\x02\x03",
            "#3500458VWould you like to use my room?\x02",
        )
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

    ChrTalk(
        0x101,
        "#3500459V#0011F#12PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500460V#0305F#6PWhoa, that came outta left field.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3500461V#5702F#5P#NCome on, this way.\x02",
    )

    CloseMessageWindow()
    OP_68(-3940, 1200, 6960, 5000)
    BeginChrThread(0xD, 3, 0, 18)
    WaitChrThread(0xD, 3)
    OP_6F(0x1)
    OP_68(-1350, 1100, 6510, 1200)

    def lambda_23DB():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23DB)

    def lambda_23E8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23E8)
    Sleep(100)

    def lambda_23F8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23F8)

    def lambda_2405():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2405)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#3500462V#0101F#12PShould we take him up on that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500463V#0211F#6PI don't like the way he is dressed.\x01",
            "It is too suspicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500464V#0301F#6PHis getup? I think the real suspicious\x01",
            "thing is that a freakin' gang leader is\x01",
            "hangin' out in Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500465V#0006F#5PWell, it's not like we haven't worked\x01",
            "with him before...\x02\x03",
            "#3500466V#0000FFor now, let's find his room.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 40, 0, 6580, 270)
    SetChrPos(0x8, -480, 0, 10050, 180)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 0, 0, 0, 0)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0xA4, 5)
    OP_29(0x47, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_16_1B4C end

    def Function_17_25F5(): pass

    label("Function_17_25F5")

    OP_95(0xFE, -4000, 0, 8400, 3000, 0x0)
    Return()

    # Function_17_25F5 end

    def Function_18_260A(): pass

    label("Function_18_260A")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_96(0xFE, 0xFFFFC037, 0x0, 0x2EEA, 0x9C4, 0x0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_79(0x5)

    def lambda_2645():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2645)
    Sleep(200)

    def lambda_265D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_265D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    Return()

    # Function_18_260A end

    def Function_19_268D(): pass

    label("Function_19_268D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50353.itc", 0x1E)
    OP_68(-99800, 1100, 124250, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xD, -102200, 150, 124000, 90)
    SetChrPos(0x101, -101400, 0, 121700, 0)
    SetChrPos(0x102, -100300, 0, 121700, 315)
    SetChrPos(0x103, -100300, 0, 120400, 315)
    SetChrPos(0x104, -101400, 0, 120400, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis063.itp")
    FadeToBright(1000, 0)
    OP_68(-101070, 1100, 122980, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#3500467V#5709F#11PTruth be told, I didn't expect the SSS\x01",
            "to have such refined tastes.\x02\x03",
            "#3500468V#5702FGetting a vacation day on the last day\x01",
            "of the Anniversary Festival and spending\x01",
            "it at a place like Mishelam? Bravo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500469V#0012F#6PUh... Yeah, we just decided to take\x01",
            "a short break from work.\x02\x03",
            "#3500470V#0001FMore importantly, what's with\x01",
            "that outfit, Wazy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500471V#5704F#11PPretty stylish, isn't it?\x02\x03",
            "#3500472V#5700FLet's just call it my side job's uniform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500473V#0005F#6PYou have a side job...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500474V#0101F#6PWhat kind of job would require\x01",
            "an outfit like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500475V#5703F#11PIn the cold, cold world of high society, many\x01",
            "beautiful, lonely ladies search for that spark\x01",
            "of love they've lost...\x02\x03",
            "#3500476V#5702FMy job is to simply ignite that and give them\x01",
            "the time they desperately dream about.\x02",
        )
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

    ChrTalk(
        0x101,
        "#3500477V#0011F#6PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500478V#0105F#6PYou can't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500479V#0211F#6PYou work as a host, Wazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500480V#0307F#6PI work my ass off for the CPD while you get\x01",
            "to have a good time chillin' with bab--er,\x01",
            "I mean... You're too young to be hostin'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500481V#5702F#11PHaha. If you think I'm doing it for the\x01",
            "money, you are sadly mistaken.\x02\x03",
            "#3500482VIt'd be rude for me to deny women my\x01",
            "company when they constantly ask for it.\x02\x03",
            "#3500483V#5709FI suppose we could call it charity work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500484V#0006F#6PYou're unbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500485V#0306F#6PHe's frank, I'll give him that. The fact that\x01",
            "it wins over ladies blows my mind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500486V#0103F#6P*sigh* I can't say I approve of this 'job,'\x01",
            "but who am I to judge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500487V#0200F#6PWazy, do you work as a host\x01",
            "for Mishelam specifically?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500488V#5702F#11PYes. I'm a part of Mishelam's very\x01",
            "own escort service.\x02\x03",
            "#3500489VTonight, I'm to accompany a lady\x01",
            "to a funny little party. I'm sure it will\x01",
            "end up being quite the adventure.\x02",
        )
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

    ChrTalk(
        0x101,
        "#3500490V#0005F#6PParty...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500491V#0101F#6PYou don't mean...\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1436, 255, 90, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#3500492V#5704F#11PAh. That explains that.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x101,
        (
            "#3500493V#0012F#6PExplains what? What are you\x01",
            "talking about, Wazy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500494V#5702F#11PThe Schwarze Auction...\x02\x03",
            "#3500495V#5702FYou came to check it out, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500496V#0001F#6PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500497V#0306F#6PDamn, caught before we even got\x01",
            "to the front door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500498V#0101F#6PThat must mean that the 'funny little\x01",
            "party' you're attending is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500499V#5700F#11PThe very same.\x02\x03",
            "#3500500V#5704FThis will be my second go-around,\x01",
            "just with a different lady this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500501V#0006F#6PYou're full of surprises, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500502V#0206F#6PThe real surprise is that someone with auction\x01",
            "knowledge was hiding under our noses the\x01",
            "entire time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500503V#5705F#11PHumor me for a second. Are you guys\x01",
            "planning to expose the auction to the public?\x02\x03",
            "#3500504VThat won't amount to much, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500505V#0006F#6PFrom the very beginning, we never had any\x01",
            "intention to take down the auction.\x02\x03",
            "#3500506V#0008FWe just have to see something there...\x02\x03",
            "#3500507VThis auction, a luxurious, underground party,\x01",
            "essentially represents the corruption of\x01",
            "Crossbell itself.\x02\x03",
            "#3500508V#0013FAnd we have to see for ourselves how high\x01",
            "this barrier we want to overcome really is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500509V#0105F#6PLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500510V#5702F#11PHaha... Is that so?\x02\x03",
            "#3500511V#5704FI don't doubt your enthusiasm for a second,\x01",
            "but you can't attend the auction that easily.\x01",
            "With no invitation, you'll be kicked to the curb.\x02\x03",
            "#3500512VEach year, they change the rose motif slightly,\x01",
            "so forging won't get you very far.\x02\x03",
            "#3500513V#5702FYou might be out of luck, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500514V#0000F#6PActually, we already have an invitation.\x02",
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0xD,
        (
            "#3500515V#5705FWow. You're serious, aren't you?\x02\x03",
            "#3500516V#5709FI assume it's pointless asking how\x01",
            "you got your hands on one.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#3500517V#0004FLet's just say it was an odd situation.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    ChrTalk(
        0x102,
        (
            "#3500518V#0108F#6PWe have the invitation, but is it really\x01",
            "all we need?\x02\x03",
            "#3500519V#0101FI wouldn't be surprised if they used\x01",
            "some sort of RSVP system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500520V#5705F#11PNo, I think you're overthinking things.\x02\x03",
            "#3500521V#5704FDue to the underground nature of the whole\x01",
            "thing, they're always open to potential clients.\x02\x03",
            "#3500522V#5702FSince smuggled goods are a big aspect of the\x01",
            "auction, many more famous individuals prefer\x01",
            "to mask their identities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500523V#0300F#6PSounds like we'll be able to survive, then.\x02\x03",
            "#3500524V#0305FHey, wait. How many people can get in with\x01",
            "one invite?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500525V#5703F#11PI don't believe there's a rule set in stone,\x01",
            "but most people go in pairs.\x02\x03",
            "#3500526V#5700FI'd recommend that. Four people is a\x01",
            "crowd, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500527V#0201F#6PSo only two of us can go...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500528V#0106F#6PUnfortunately so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500529V#5704F#11PAlso, since it IS a high-class party,\x01",
            "you should wear something more formal.\x02\x03",
            "#3500530V#5702FOf course, if you dress as well as me,\x01",
            "you'd be the center of attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500531V#0006F#6PI think I'd rather avoid that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3500532V#0001F#5PHey, Elie.\x02\x03",
            "#3500533VDo you know where we can get some\x01",
            "new clothes for the auction?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#3500534V#0102F#12PThe boutique downstairs should be\x01",
            "perfect for what we need.\x02\x03",
            "#3500535VI've been there before, so there's no\x01",
            "need to worry. I can pay, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500536V#0011F#5PAre you sure...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500537V#0104F#12POf course. Leave it to me.\x02\x03",
            "#3500538V#0100FA more crucial question is, who among us\x01",
            "will pair up and infiltrate the auction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500539V#0006F#5PI'm not sure yet.\x02\x03",
            "#3500540V#0008FRock-paper-scissors probably isn't the\x01",
            "best way to go about deciding...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500541V#0306F#6PWhat are you on about?\x02\x03",
            "#3500542V#0300FYou only gotta pick one, dude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500543V#0005F#5PHuh...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#3500544V#0204F#6PYou are the one most invested in\x01",
            "the Schwarze Auction, Lloyd...\x02\x03",
            "#3500545V#0202FAnd given that you are our leader,\x01",
            "it is only natural that you go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500546V#0005F#5PGuys, are you sure about this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500547V#0103F#12PThis decision would be a lot simpler if you\x01",
            "just accepted your responsibilities already.\x02\x03",
            "#3500548V#0102FYou want to see the corruption of Crossbell\x01",
            "firsthand, don't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3500549V#0004F#5PYou're right. I'll lead the charge into the\x01",
            "Schwarze Auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3500550V#5704F#11PThen all you have to do is pick your date.\x02\x03",
            "#3500551V#5702FYou would stand out a tad too much if\x01",
            "you went solo, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500552V#0006F#5PThat's a good point. Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500553V#0103F#12PYou can pick me, Tio, or Randy.\x02\x03",
            "#3500554V#0100FRemember that you'll be surrounded by the\x01",
            "mafia when making your decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500555V#0204F#6PThe remaining two can be on standby\x01",
            "outside the venue while the other two\x01",
            "are inside.\x02\x03",
            "#3500556V#0202FIs that acceptable?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500557V#0302F#6PWell, no matter how we divvy up roles,\x01",
            "it'd be best to move along to the boutique.\x02\x03",
            "#3500558VPlenty of time to choose before we have\x01",
            "to find some new digs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500559V#0000F#5PRight. We'll do that.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetChrChipByIndex(0xD, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    AddParty(0x50, 0xFF, 0xFF)
    OP_68(-100000, 1250, 12500, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18600, 0)
    SetChrPos(0x101, -100030, 0, 14990, 180)
    SetChrPos(0x102, -100030, 0, 14990, 180)
    SetChrPos(0x103, -100030, 0, 14990, 180)
    SetChrPos(0x104, -100030, 0, 14990, 180)
    SetChrPos(0x151, -100030, 0, 14990, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(17600, 2500)
    OP_6F(0x10)
    OP_0D()
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)
    OP_68(-100000, 1250, 10500, 4000)
    BeginChrThread(0x101, 3, 0, 20)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 22)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 23)
    Sleep(1000)
    BeginChrThread(0x151, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x151, 3)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sleep(100)
    Sound(890, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    OP_6F(0x1)
    TurnDirection(0x101, 0x151, 400)

    ChrTalk(
        0x101,
        (
            "#3500560V#0011F#6PWait a second...\x02\x03",
            "#3500561V#0001FWazy, is there some reason why\x01",
            "you're following us?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4634():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4634)
    Sleep(100)

    def lambda_4644():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4644)

    def lambda_4651():
        TurnDirection(0xFE, 0x151, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4651)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x151,
        (
            "#3500562V#5709F#11PSince the opportunity has arisen,\x01",
            "I figure I'll offer a lesson in style.\x02\x03",
            "#3500563V#5702FI'll throw in a way to trick the people\x01",
            "running the security checkpoint, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500564V#0006F#6PWell, I guess we don't have any\x01",
            "reason to refuse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500565V#0211F#6PIt's obvious that he is compelled by curiosity\x01",
            "rather than a genuine desire to assist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500566V#0302F#5POh, hell. Let's hear the guy out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500567V#0100F#5PIf we're all ready, let's head downstairs\x01",
            "to the boutique.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -99720, 0, 10000, 90)
    SetScenarioFlags(0xA4, 6)
    OP_29(0x47, 0x1, 0x5)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -93960, 0, 8260, 0)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 94190, 0, 11580, 0)
    BeginChrThread(0xA, 0, 0, 2)
    EventEnd(0x5)
    Return()

    # Function_19_268D end

    def Function_20_48D6(): pass

    label("Function_20_48D6")


    def lambda_48DB():
        OP_95(0xFE, -100000, 0, 9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48DB)

    def lambda_48F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48F5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_490E():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_490E)
    WaitChrThread(0x101, 1)
    Return()

    # Function_20_48D6 end

    def Function_21_491B(): pass

    label("Function_21_491B")


    def lambda_4920():
        OP_95(0xFE, -100000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4920)

    def lambda_493A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_493A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_4953():
        OP_95(0xFE, -101200, 0, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4953)
    WaitChrThread(0xFE, 1)

    def lambda_4971():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4971)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_491B end

    def Function_22_497E(): pass

    label("Function_22_497E")


    def lambda_4983():
        OP_95(0xFE, -100000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4983)

    def lambda_499D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_499D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_49B6():
        OP_95(0xFE, -98800, 0, 10200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49B6)
    WaitChrThread(0xFE, 1)

    def lambda_49D4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49D4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_497E end

    def Function_23_49E1(): pass

    label("Function_23_49E1")


    def lambda_49E6():
        OP_95(0xFE, -100000, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49E6)

    def lambda_4A00():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A00)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_4A19():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A19)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_49E1 end

    def Function_24_4A26(): pass

    label("Function_24_4A26")


    def lambda_4A2B():
        OP_95(0xFE, -98610, 0, 11590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A2B)

    def lambda_4A45():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A45)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_4A5E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A5E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_4A26 end

    def Function_25_4A6B(): pass

    label("Function_25_4A6B")

    EventBegin(0x0)
    Fade(500)
    OP_68(97820, 900, 122220, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20810, 0)
    SetChrPos(0x101, 98200, 0, 121000, 270)
    SetChrPos(0x102, 98200, 0, 122200, 270)
    SetChrPos(0x103, 99400, 0, 121000, 270)
    SetChrPos(0x104, 99400, 0, 122200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4AFE")
    SetChrPos(0x151, 100600, 0, 121600, 270)

    label("loc_4AFE")

    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x10E, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#5PI don't get it... What did I do\x01",
            "to deserve this?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x5A, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#5PHey, you all! Did you happen to\x01",
            "find something while walking\x01",
            "around the resort?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PUm, that something being an...\x01",
            "(...engagement ring?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FI don't think so...\x02\x03",
            "#0001FYou dropped an engagement ring?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P#5SPlease, keep your voice down!\x02",
    )

    CloseMessageWindow()
    OP_68(99540, 1200, 123070, 2000)
    OP_6F(0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0x10E, 0x1F4)

    ChrTalk(
        0xF,
        "#12PToma? What are you shouting about?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#5POh! Um, hahaha... Don't worry about\x01",
            "it, Alvina. Everything's perfect. More\x01",
            "than perfect, actually!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PIs that right? Heehee, you're such\x01",
            "an oddball sometimes, Toma.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x1F4)
    OP_68(97820, 900, 122220, 2000)
    OP_6F(0x1)

    ChrTalk(
        0xE,
        (
            "#5PSh-She almost noticed, didn't she?\x01",
            "Aidios, help me out here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FO-Oh. Sorry. (I think I almost ruined\x01",
            "this guy's day...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PIn exchange for nearly spilling the\x01",
            "beans, help me search for the ring!\x01",
            "That'll be enough of an apology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FWhat in the world do we have to\x01",
            "apologize for...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FWe have no such obligation. Lloyd,\x01",
            "I recommend we ignore him and focus\x01",
            "on more pressing issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PS-Sorry! That was a little rude of me.\x01",
            "I'm begging you, man... Please help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYou know about the fireworks show\x01",
            "tonight, right? At the theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAll I want is to be able to propose\x01",
            "under the glowing night sky...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_50DC")

    ChrTalk(
        0x151,
        "#5700F#12PQuite the romantic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0102FIndeed.\x02\x03",
            "#0100FWe don't have much free time,\x01",
            "but we'll keep an eye out for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_514F")

    label("loc_50DC")


    ChrTalk(
        0x102,
        (
            "#12P#0102FWhat a wonderful proposal...\x02\x03",
            "#0100FWe don't have much free time, but we'll\x01",
            "keep an eye out for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_514F")


    ChrTalk(
        0xE,
        "#5PHuh...? You will?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0011FElie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0104FIt's not a big deal, is it?\x02\x03",
            "After all, he's only this desperate\x01",
            "because he's thinking of his girlfriend.\x01",
            "I think it's quite admirable.\x02\x03",
            "#0100FAnd besides, if he isn't able to propose,\x01",
            "I'm sure she will be let down as well.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5360")

    ChrTalk(
        0x101,
        (
            "#12P#006FThat may be, but it's not like we should\x01",
            "string along a citizen like Wazy on a\x01",
            "request...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#5704F#12POh, don't mind me.\x02\x03",
            "#5700FAs long as you don't forget the real\x01",
            "reason why you're here, I don't see\x01",
            "an issue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53E3")

    label("loc_5360")


    ChrTalk(
        0x101,
        (
            "#12P#0003FWell...I guess I do feel bad for this guy.\x01",
            "It would be a shame to come out all this\x01",
            "way and not be able to propose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E3")


    ChrTalk(
        0x102,
        (
            "#12P#0100FIt's decided, then!\x02\x03",
            "#0105FSo, do you have any idea as to\x01",
            "where you might have lost it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PNot a clue!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAll I can say is that Alvina and I\x01",
            "went on a quick tour of the resort\x01",
            "when we first arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PThey kicked us out of the jewelry store, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203FThat narrows it down...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI tried, okay? If you find anything\x01",
            "remotely resembling an engagement\x01",
            "ring, come show it to me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAfter the sun sets, we'll set off\x01",
            "to Mishelam Wonderland. I need\x01",
            "that ring before then, please!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PYou guys are my only hope!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Where Is the Engagement Ring?]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0xE, 0x10E, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 97960, 0, 122140, 270)
    OP_29(0x24, 0x4, 0x2)
    OP_29(0x24, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_4A6B end

    def Function_26_56AD(): pass

    label("Function_26_56AD")

    EventBegin(0x0)
    Fade(500)
    OP_68(97820, 900, 122220, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20810, 0)
    SetChrPos(0x101, 98200, 0, 121000, 270)
    SetChrPos(0x102, 98200, 0, 122200, 270)
    SetChrPos(0x103, 99400, 0, 121000, 270)
    SetChrPos(0x104, 99400, 0, 122200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5740")
    SetChrPos(0x151, 100600, 0, 121600, 270)

    label("loc_5740")

    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x5A, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_0D()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#5PDid you guys come across my\x01",
            "engagement ring?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FHopefully. We found this inside the resort.\x02\x03",
            "Toma, do you mind giving this a look?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5856")
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x34C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5856")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_588E")
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x34D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_588E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58C6")
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x34E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_58C6")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0xE,
        "#5PHmm, let's see here...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59B4")

    ChrTalk(
        0xE,
        "#5PA gold ring...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PSorry, guys. This isn't my ring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThe shape is pretty close, but the\x01",
            "color is nothing like mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x2)

    label("loc_59B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A69")

    ChrTalk(
        0xE,
        "#5PA pearl ring...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PSorry, guys. This isn't my ring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PIt's beautiful, I'll give it that.\x01",
            "But it looks nothing like the\x01",
            "one I bought.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x4)

    label("loc_5A69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B2D")

    ChrTalk(
        0xE,
        "#5PA platinum ring...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PSorry, guys. This isn't my ring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PDo you really think I could propose with\x01",
            "something as ugly as this? Who do you\x01",
            "think I am?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x6)

    label("loc_5B2D")

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
        0x101,
        "#12P#0006FMy mistake...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYou can have this back. Do whatever\x01",
            "you want with it. I don't care.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Toma returned the ring.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6958")
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#5PI can't believe you've brought me\x01",
            "so many rings and NONE of them\x01",
            "were mine. What are the odds...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P*sigh* Where in the world could\x01",
            "I have dropped that stupid thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FUmm... Don't lose heart just yet.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5EFD")

    ChrTalk(
        0x151,
        (
            "#5706F#12PNow all we have to do is think of where\x01",
            "to search next. But we seem to be\x01",
            "avoiding a certain scenario...\x02\x03",
            "#5702FSomeone could have swiped it, right?\x01",
            "After all, it was an expensive ring lying\x01",
            "on the ground, all alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0011FW-Wazy...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PO-Oh, Goddess... This is the end...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0x104,
        "#12P#0306FPull yourself together, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        "#5709F#12PHaha, just a bit of teasing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6054")

    label("loc_5EFD")


    ChrTalk(
        0x104,
        (
            "#12P#0306FThough, we still haven't found the damn thing.\x01",
            "Kinda makes me think that someone actually\x01",
            "did pick it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0011FR-Randy! Stop...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PKick me while I'm down...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0x103,
        (
            "#12P#0203FYou can see him slowly become\x01",
            "more and more depressed. All\x01",
            "thanks to Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0306FSo it's all my fault, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_6054")

    OP_68(99540, 1200, 123070, 2000)
    OP_6F(0x1)
    OP_93(0xF, 0x10E, 0x1F4)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(99270, 1200, 122850, 2000)
    OP_95(0xF, 102010, 0, 123530, 2000, 0x0)
    TurnDirection(0xF, 0xE, 500)
    OP_6F(0x1)

    ChrTalk(
        0xF,
        (
            "#12PToma, are you feeling okay?\x01",
            "You're looking sort of sick...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_60FA():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_60FA)
    Sleep(100)

    def lambda_610A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_610A)
    Sleep(50)

    def lambda_611A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_611A)
    Sleep(100)

    def lambda_612A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_612A)
    Sleep(50)

    def lambda_613A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_613A)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_615B")

    def lambda_6153():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_6153)

    label("loc_615B")


    ChrTalk(
        0xE,
        (
            "#5PAh! Um, do I...? Well, y'see, there's\x01",
            "a perfectly good explanation for that.\x01",
            "It's, uh...nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12PIt doesn't look like nothing to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PIf you're feeling blue, how about we\x01",
            "cheer ourselves up by checking out\x01",
            "the residential area again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PSitting together on that bench near the\x01",
            "lakeshore was the highlight of my\x01",
            "morning. Want to do it again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PYeah, that was a good time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#5P#5SWait...! WAIT JUST A SECOND!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_63C4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63C4)
    Sleep(100)

    def lambda_63D4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63D4)
    Sleep(50)

    def lambda_63E4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_63E4)
    Sleep(100)

    def lambda_63F4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_63F4)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_6415")

    def lambda_640D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_640D)

    label("loc_6415")


    ChrTalk(
        0x101,
        "#12P#0005FT-Toma?\x02",
    )

    CloseMessageWindow()

    def lambda_6431():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6431)

    ChrTalk(
        0xE,
        (
            "#5PI remember! It was definitely back\x01",
            "there where it happened!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI was sitting on a bench, having a\x01",
            "fun conversation with Alvina when...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI reached into my pocket to double\x01",
            "check that the ring was still there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PLater, when we returned to the hotel,\x01",
            "I checked my pocket again, and it\x01",
            "was gone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PIf I dropped it, it had to have been somewhere\x01",
            "near that bench! I've never been more sure of\x01",
            "anything in my life!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FYou're positive...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FThis clue came out of nowhere...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PHey, Toma. What have you been freaking\x01",
            "out about?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6684():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6684)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#5PU-Uh! Nothing at all! Just talking to\x01",
            "some buddies of mine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PCome on, Alvina! Let's go take in\x01",
            "the beauty of Mishelam, the finest\x01",
            "place in all of Crossbell! Ahaha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PYou sure? Toma, you're really acting\x01",
            "strange. Even stranger than usual.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(97670, 1200, 121980, 2000)
    OP_95(0xF, 103230, 0, 124330, 2000, 0x0)
    OP_93(0xF, 0x0, 0x1F4)
    OP_6F(0x1)

    ChrTalk(
        0xE,
        "#5PTh-That was a close one...\x02",
    )

    CloseMessageWindow()

    def lambda_6800():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6800)

    ChrTalk(
        0xE,
        (
            "#5PGuys! I need you to check out that\x01",
            "fancy residential area for me, okay?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PMy ring might still be somewhere\x01",
            "near that bench we sat at...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FWe can do that. Lloyd, shall we\x01",
            "head on over there now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FLet's do it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_694D")

    ChrTalk(
        0x151,
        (
            "#5709F#12PHaha! It's never a dull time with\x01",
            "the SSS, is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_694D")

    OP_29(0x24, 0x1, 0x7)
    Jump("loc_6A13")

    label("loc_6958")


    ChrTalk(
        0xE,
        (
            "#5P*sigh* Why can't I remember\x01",
            "where I dropped it? That would\x01",
            "make this whole mess go away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAnyway, if you find something that\x01",
            "looks like my ring, please come\x01",
            "show it to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A13")

    OP_93(0xE, 0x10E, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 97960, 0, 122140, 270)
    EventEnd(0x5)
    Return()

    # Function_26_56AD end

    def Function_27_6A36(): pass

    label("Function_27_6A36")

    EventBegin(0x0)
    Fade(500)
    OP_68(97820, 900, 122220, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20810, 0)
    SetChrPos(0x101, 98200, 0, 121000, 270)
    SetChrPos(0x102, 98200, 0, 122200, 270)
    SetChrPos(0x103, 99400, 0, 121000, 270)
    SetChrPos(0x104, 99400, 0, 122200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_6AC9")
    SetChrPos(0x151, 100600, 0, 121600, 270)

    label("loc_6AC9")

    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x5A, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_0D()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#5PHey, guys...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PDid you...did you finally find my ring?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FWell, we hope so. Mind taking\x01",
            "a look at it?\x02",
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
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x34F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x34F, 1)

    ChrTalk(
        0xE,
        "#5PHmm, let's see here...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        "#5PTh-This is it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PThis is the one!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAn argem ring engraved with\x01",
            "mine and Alvina's names...\x01",
            "This is definitely my ring!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0012FReally? Good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FDude, I would have lost my mind\x01",
            "if you told us we got the wrong\x01",
            "one again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_6DAE")

    ChrTalk(
        0x151,
        (
            "#5702F#12PMore like you would have lost your\x01",
            "mind if you kept looking for that ring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0206FI hope that was not intended to be funny.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DD5")

    label("loc_6DAE")


    ChrTalk(
        0x103,
        "#12P#0206FI am glad this is over.\x02",
    )

    CloseMessageWindow()

    label("loc_6DD5")


    ChrTalk(
        0x102,
        (
            "#12P#0100FI'm just happy that we were\x01",
            "able to find it for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PThank you, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI don't know what I would have done if\x01",
            "we went into the park without it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PNow it looks like I can finally put\x01",
            "my proposal-under-the-fireworks\x01",
            "plan into motion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI would have never been able to\x01",
            "do this without you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PHere. Take this as a token of my\x01",
            "appreciation.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x9A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x9A, 1)

    ChrTalk(
        0x101,
        (
            "#12P#0005FAre you sure about this...? This looks\x01",
            "like a REALLY expensive quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI wouldn't ever use it, so don't let\x01",
            "that bother you. It's just a small\x01",
            "way of showing my thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PWell, it's time to start mentally preparing\x01",
            "for the big moment tonight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PIf we ever meet again, I'll know that I\x01",
            "can rely on you guys, no matter what.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Where Is the Engagement Ring?]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0xE, 0x10E, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 97960, 0, 122140, 270)
    OP_29(0x24, 0x1, 0xA)
    OP_29(0x24, 0x4, 0x10)
    SetScenarioFlags(0x0, 3)
    EventEnd(0x5)
    Return()

    # Function_27_6A36 end

    def Function_28_71AD(): pass

    label("Function_28_71AD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "                   ~Staircase~\x01",
            "The third floor is currently reserved for\x01",
            "VIPs. Please refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_71AD end

    def Function_29_7253(): pass

    label("Function_29_7253")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears to be locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_29_7253 end

    SaveToFile()

Try(main)
