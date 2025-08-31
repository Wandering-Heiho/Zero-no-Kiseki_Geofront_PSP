from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0470.bin",                # FileName
        "c0470",                    # MapName
        "c0470",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 37, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0470",                  # 0
        "Proprietor Drake",       # 1
        "Cherry",                 # 2
        "Galetti",                # 3
        "Elinda",                 # 4
        "Raytarossa",             # 5
        "Old Man Rick",           # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Lechter",                # 10
        "Mayor Bickson",          # 11
        "Gantz",                  # 12
        "Lechter",                # 13
    ))

    AddCharChip((
        "chr/ch20002.itc",                   # 00
        "chr/ch21200.itc",                   # 01
        "chr/ch25800.itc",                   # 02
        "chr/ch25900.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch27100.itc",                   # 05
        "chr/ch32300.itc",                   # 06
        "chr/ch32302.itc",                   # 07
        "chr/ch33302.itc",                   # 08
        "chr/ch07402.itc",                   # 09
    ))

    DeclNpc(-899,    4000,    21299,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(6199,    -1000,   8000,    270,  261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       -1000,   13649,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6500,   -1000,   6000,    90,   261,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(1350,    -949,    11500,   0,    341,  0x0, 0,   8,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   0,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(0,       -1000,   5349,    225,  389,  0x0, 0,   1,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(0,       -1000,   5349,    225,  389,  0x0, 0,   6,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(3299,    -949,    12590,   315,  469,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(1820,    4000,    18850,   0,    469,  0x0, 0,   9,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-900,    4000,    20000,   2000,    -900,    5500,    21300,   0x007E, 0,  5,  0x0000)
    DeclActor(5240,    -1000,   8000,    1200,    6200,    500,     8000,    0x007E, 0,  7,  0x0000)
    DeclActor(-920,    -1000,   12050,   1700,    0,       500,     13650,   0x007E, 0,  9,  0x0000)
    DeclActor(-4500,   -1000,   6000,    1500,    -6500,   500,     6000,    0x007E, 0,  11, 0x0000)
    DeclActor(7530,    4000,    17960,   1800,    7530,    5500,    17960,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    15750,   1800,    7530,    5500,    15750,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    13410,   1800,    7530,    5500,    13410,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    10460,   1800,    7530,    5500,    10460,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    8300,    1800,    7530,    5500,    8300,    0x007C, 0,  20, 0x0000)

    ScpFunction((
        "Function_0_3E4",          # 00, 0
        "Function_1_49C",          # 01, 1
        "Function_2_4C7",          # 02, 2
        "Function_3_61B",          # 03, 3
        "Function_4_713",          # 04, 4
        "Function_5_7D0",          # 05, 5
        "Function_6_7D4",          # 06, 6
        "Function_7_2C4F",         # 07, 7
        "Function_8_2C53",         # 08, 8
        "Function_9_44C9",         # 09, 9
        "Function_10_44CD",        # 0A, 10
        "Function_11_5567",        # 0B, 11
        "Function_12_556B",        # 0C, 12
        "Function_13_6560",        # 0D, 13
        "Function_14_7BB5",        # 0E, 14
        "Function_15_9256",        # 0F, 15
        "Function_16_94E3",        # 10, 16
        "Function_17_98FB",        # 11, 17
        "Function_18_9959",        # 12, 18
        "Function_19_A0E6",        # 13, 19
        "Function_20_A497",        # 14, 20
        "Function_21_A524",        # 15, 21
        "Function_22_A88E",        # 16, 22
        "Function_23_B39F",        # 17, 23
        "Function_24_CD99",        # 18, 24
        "Function_25_CDF4",        # 19, 25
        "Function_26_CE4F",        # 1A, 26
        "Function_27_CE75",        # 1B, 27
        "Function_28_CE9B",        # 1C, 28
        "Function_29_D2ED",        # 1D, 29
    ))


    def Function_0_3E4(): pass

    label("Function_0_3E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_424"),
        (1, "loc_430"),
        (2, "loc_43C"),
        (3, "loc_448"),
        (4, "loc_454"),
        (5, "loc_460"),
        (6, "loc_46C"),
        (SWITCH_DEFAULT, "loc_478"),
    )


    label("loc_424")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_430")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_43C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_448")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_454")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_460")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_46C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_478")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_484")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_49B")

    Return()

    # Function_0_3E4 end

    def Function_1_49C(): pass

    label("Function_1_49C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C6")
    OP_94(0xFE, 0x744, 0x1BD0, 0xFFFFF704, 0xB2C, 0x3E8)
    Sleep(300)
    Jump("Function_1_49C")

    label("loc_4C6")

    Return()

    # Function_1_49C end

    def Function_2_4C7(): pass

    label("Function_2_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E2")
    SetMapFlags(0x10000000)
    Event(0, 23)
    Jump("loc_4F4")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F4")
    Event(0, 19)

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_508")
    ClearScenarioFlags(0x5C, 0)
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_527")
    SetChrPos(0xD, 50, 4050, 18950, 0)
    Jump("loc_61A")

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_535")
    Jump("loc_61A")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_55B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_551")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_556")

    label("loc_551")

    SetChrFlags(0x8, 0x80)

    label("loc_556")

    Jump("loc_61A")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_587")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_61A")

    label("loc_587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_595")
    Jump("loc_61A")

    label("loc_595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5C1")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_61A")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D4")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_61A")

    label("loc_5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5EF")
    ClearChrFlags(0x10, 0x80)
    SetChrSubChip(0x10, 0x1)
    SetChrSubChip(0xC, 0x2)
    Jump("loc_61A")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_602")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_61A")

    label("loc_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_615")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_61A")

    label("loc_615")

    ClearChrFlags(0xE, 0x80)

    label("loc_61A")

    Return()

    # Function_2_4C7 end

    def Function_3_61B(): pass

    label("Function_3_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_634")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_63A")

    label("loc_634")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_63A")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -6000, -1000, 16000, 5000, 5000, 0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67B")
    OP_1B(0x0, 0x0, 0x1D)

    label("loc_67B")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_691")
    OP_66(0x5, 0x1)
    Jump("loc_712")

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_69F")
    Jump("loc_712")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_6AD")
    Jump("loc_712")

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_6C4")
    Jump("loc_6C8")

    label("loc_6C4")

    OP_65(0x0, 0x1)

    label("loc_6C8")

    Jump("loc_712")

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_6EB")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jump("loc_712")

    label("loc_6EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6F9")
    Jump("loc_712")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_712")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)

    label("loc_712")

    Return()

    # Function_3_61B end

    def Function_4_713(): pass

    label("Function_4_713")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_724")
    Jump("loc_7CC")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_732")
    Jump("loc_7CC")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_740")
    Jump("loc_7CC")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_7CC")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_75C")
    Jump("loc_7CC")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_76A")
    Jump("loc_7CC")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_778")
    Jump("loc_7CC")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_786")
    Jump("loc_7CC")

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_794")
    Jump("loc_7CC")

    label("loc_794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7A2")
    Jump("loc_7CC")

    label("loc_7A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7B0")
    Jump("loc_7CC")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7BE")
    Jump("loc_7CC")

    label("loc_7BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7CC")
    Jump("loc_7CC")

    label("loc_7CC")

    TalkEnd(0xFE)
    Return()

    # Function_4_713 end

    def Function_5_7D0(): pass

    label("Function_5_7D0")

    Call(0, 6)
    Return()

    # Function_5_7D0 end

    def Function_6_7D4(): pass

    label("Function_6_7D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EA")
    Call(0, 22)
    Jump("loc_2C4E")

    label("loc_7EA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8CB")

    ChrTalk(
        0x8,
        (
            "It's unfortunately as I surmised.\x01",
            "Gantz has yet to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A pity. We've sullied our reputation\x01",
            "in the eyes of one of our patrons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope he forgives our injustice and\x01",
            "returns here once again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_8CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_BC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_981")

    ChrTalk(
        0x8,
        (
            "Do you seek Lechter? He was\x01",
            "whining about having to return to\x01",
            "the Empire last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He sends you his regards and\x01",
            "wishes you all good luck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_981")


    ChrTalk(
        0x8,
        (
            "Lechter will not be here today,\x01",
            "by the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He mentioned that he had to return to the\x01",
            "Empire during last night's conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FOh, what? He's already gone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, he is. I got the impression that he did\x01",
            "not wish to leave, but some trouble\x01",
            "surfaced back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FI...see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FAn unfortunate loss for us. I'm sure he was\x01",
            "holding on to valuable information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206FWhile true, I get the impression that he\x01",
            "rarely speaks truthfully when divulging\x01",
            "things.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB5")

    ChrTalk(
        0x10A,
        "#0605F(Who the heck are you guys talking about?)\x02",
    )

    CloseMessageWindow()

    label("loc_BB5")

    SetScenarioFlags(0xD0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_BBB")

    Jump("loc_DA6")

    label("loc_BC0")


    ChrTalk(
        0x8,
        (
            "If you're looking for Gantz, I regret to inform\x01",
            "you that he is absent today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I suspect that he is struggling to come back\x01",
            "after yesterday's incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FI assure you that isn't the case, sir.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0303FDon't sweat it. He's goin' through some stuff.\x02\x03",
            "#0300FHey, Drake. Do us a solid and give us a ring\x01",
            "if he shows his face around here, will ya?\x02\x03",
            "Got some unfinished business with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Understood. Has he gotten himself into\x01",
            "trouble?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 6)

    label("loc_DA6")

    Jump("loc_2C4B")

    label("loc_DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_1110")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_END)), "loc_E97")

    ChrTalk(
        0x8,
        (
            "I'll notify our staff to remain silent regarding\x01",
            "Gantz's violent outburst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "While I'm sure there'll be rumors, this place is\x01",
            "rife with drama. People will quickly forget and\x01",
            "move on to the next hot topic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110B")

    label("loc_E97")


    ChrTalk(
        0x8,
        (
            "Thank you for helping us before. Allow me\x01",
            "to properly express my gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FWe kinda lucked out. Things coulda been\x01",
            "a lot worse had we not come when we did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYeah, no kidding. Someone could have been\x01",
            "hurt had they tried to fight him while he\x01",
            "had that unnatural strength.\x02\x03",
            "#0001FExcuse me, sir. I know this may be uncouth,\x01",
            "but would you mind keeping quiet about this\x01",
            "for now?\x02\x03",
            "We've yet to uncover all the facts, so we\x01",
            "don't want any misinformation to spread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right. This doesn't bode too well for us,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rumors are bound to spread, but I'll\x01",
            "notify my staff to remain silent about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 5)

    label("loc_110B")

    Jump("loc_2C4B")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1201")

    ChrTalk(
        0x8,
        (
            "There's no mistaking it. Gantz certainly\x01",
            "is a frequent guest to this establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I believe he's staying in a deluxe suite\x01",
            "on the top floor of Hotel Millennium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It might be a wise idea to visit him yourselves.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_1201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_132B")

    ChrTalk(
        0x8,
        (
            "I don't mind if you come around here, Randy.\x01",
            "Just don't get carried away when you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those who gamble are destined to one day\x01",
            "suffer the consequences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FYeah, yeah. Spare me the lecture.\x01",
            "(Damn, Drake's definitely feelin'\x01",
            "a little on edge right now.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1552")

    label("loc_132B")


    ChrTalk(
        0x104,
        (
            "#0300FWhat's up, Drake? I'm back to blow\x01",
            "off some steam!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You again, Randy? Yeesh. Shoo, shoo!\x01",
            "We don't need you around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't appreciate how ruthless you've been.\x01",
            "Our profits have gone down the drain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#0305FSomethin' the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm? No, it's nothing important.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just try to keep it casual, please.\x01",
            "It's all about having fun, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those who gamble are destined to one day\x01",
            "suffer the consequences.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1552")

    Jump("loc_2C4B")

    label("loc_1557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1AEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15D6")

    ChrTalk(
        0x8,
        (
            "I would advise that you don't become\x01",
            "involved with Revache & Co.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please be careful out there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AE9")

    label("loc_15D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_182C")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "I heard you showed up on Revache's\x01",
            "property, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph. Throwing yourself into the face of\x01",
            "danger, are we? I thought they warned you\x01",
            "to not pry into their business anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FWeeeell... That's kinda just how everythin'\x01",
            "unfolded. I didn't go there askin' for a fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hah. Be it the CPD or the CGF, you've got\x01",
            "a knack for picking dangerous careers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hurry up and find a more peaceful\x01",
            "job, Randy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(You two seem pretty close to each other.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Yeah. Used to waste away in this casino\x01",
            "back when I first moved to Crossbell.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE6")

    label("loc_182C")


    ChrTalk(
        0x8,
        (
            "Now that you've all gone and trod\x01",
            "on Revache's property...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please stay safe. Nothing positive will\x01",
            "come from getting involved with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Keep Randy out of trouble while you're at it,\x01",
            "too. That man never fails to throw himself\x01",
            "into the face of danger with his career choices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha. Sorry to have him always worry you, sir.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19D2")

    ChrTalk(
        0x102,
        "#0100FYou seem well acquainted with Randy, sir.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A1C")

    label("loc_19D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A1C")

    ChrTalk(
        0x103,
        (
            "#0200FYou seem well informed about Randy,\x01",
            "Mr. Drake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A1C")


    ChrTalk(
        0x8,
        "It's quite simple, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Randy would often come by when he\x01",
            "first moved to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm not aware of his circumstances, but\x01",
            "something about him makes me want to\x01",
            "help the poor man out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE6")

    SetScenarioFlags(0x0, 0)

    label("loc_1AE9")

    Jump("loc_2C4B")

    label("loc_1AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1CC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B89")

    ChrTalk(
        0x8,
        (
            "There's an information broker that operates\x01",
            "within the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "People these days have gotten clever,\x01",
            "haven't they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBD")

    label("loc_1B89")


    ChrTalk(
        0x8,
        (
            "I've heard an information broker operates\x01",
            "within the orbal network these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They supposedly deal with anything, ranging\x01",
            "from normal information all the way up to\x01",
            "insider info on illegal happenings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh. The mafia used to contract that job out\x01",
            "back in the day. They've sure smartened up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CBD")

    Jump("loc_2C4B")

    label("loc_1CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DB8")

    ChrTalk(
        0x8,
        (
            "Where do I even begin? The mayor has been\x01",
            "living here since the inception of its turbulent\x01",
            "history as a state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's all thanks to that man's sole efforts that\x01",
            "we've been able to live in peace these last\x01",
            "15 years.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F46")

    label("loc_1DB8")


    ChrTalk(
        0x8,
        (
            "Henry MacDowell has been Crossbell's mayor\x01",
            "for the last 15 years. He tends to not have any\x01",
            "strong leaning toward either side of the spectrum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Crossbell has certainly had its fair share of\x01",
            "problems these last 15 years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, we've been able to overcome them\x01",
            "thanks to his leadership and guidance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It might not mean much coming from a puny\x01",
            "old casino, but he is a fine man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F46")

    Jump("loc_2C4B")

    label("loc_1F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_214E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FD0")

    ChrTalk(
        0x8,
        (
            "There's always an open seat for you at our\x01",
            "bar, Randy. Don't be afraid to come by for\x01",
            "a drink some time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_1FD0")


    ChrTalk(
        0x8,
        (
            "You look stressed out, Randy. Is everything\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHaha, really? Thought I was hidin' it well.\x02\x03",
            "#0306FJust a bunch of stuff happenin' at work.\x01",
            "Not really worth listenin' to it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, if you insist.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On that note, I received a bottle of some\x01",
            "great stuff today. Feel free to join me\x01",
            "for a drink later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FSounds like a date to me!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2149")

    Jump("loc_2C4B")

    label("loc_214E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_23CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21C6")

    ChrTalk(
        0x8,
        "Revache is the king of Crossbell's underworld.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I urge you to not do anything reckless.\x02",
    )

    CloseMessageWindow()
    Jump("loc_23C9")

    label("loc_21C6")

    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "I heard you went and stuck your nose into\x01",
            "Revache's business, Randy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#0306FHow the hell'd you find that out?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's not important. Just cut it out, okay?\x01",
            "They're too powerful for rookie officers\x01",
            "like yourselves to take down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everybody in Crossbell, ESPECIALLY\x01",
            "business owners of this district, know\x01",
            "that all too well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They require protection money from me,\x01",
            "lest I suffer the consequences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_23C9")

    Jump("loc_2C4B")

    label("loc_23CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2565")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_246B")

    ChrTalk(
        0x8,
        (
            "Between the festival and Arc en Ciel's new play,\x01",
            "there's a lot to be excited for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I am quite looking forward to next month.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2560")

    label("loc_246B")


    ChrTalk(
        0x8,
        (
            "I welcome you to Barca Casino,\x01",
            "everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Business has been booming. It must be due\x01",
            "to the upcoming Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tickets for Arc en Ciel's new play went\x01",
            "on sale yesterday. I've never seen a\x01",
            "line that large in my life.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2560")

    Jump("loc_2C4B")

    label("loc_2565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_26B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_25F3")

    ChrTalk(
        0x8,
        (
            "I welcome you to Barca Casino,\x01",
            "everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I would be most appreciative if you came\x01",
            "to enjoy yourselves here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B0")

    label("loc_25F3")


    ChrTalk(
        0x8,
        (
            "I welcome you to Barca Casino,\x01",
            "everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our bar is always available to any tired\x01",
            "patrons in need of a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I would be most delighted to offer you\x01",
            "alcoholic beverages.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_26B0")

    Jump("loc_2C4B")

    label("loc_26B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_28FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_273F")

    ChrTalk(
        0x8,
        "The casino is reserved for a VIP tonight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll be entertaining a high-ranking official\x01",
            "and his cronies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F9")

    label("loc_273F")


    ChrTalk(
        0x8,
        "The casino is reserved for a VIP tonight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll be treating a high-ranking official and\x01",
            "his cronies extra special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F*sigh* Again, man? Haven't you been gettin'\x01",
            "way too many of those lately?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Well, we've been seeing more customers,\x01",
            "so I can't complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You would be better off not showing your\x01",
            "face around here, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FYeah, yeah. You know I want nothin'\x01",
            "to do with those jackasses anyway.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_28F9")

    Jump("loc_2C4B")

    label("loc_28FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_END)), "loc_29C0")

    ChrTalk(
        0x8,
        (
            "I welcome you to Barca Casino,\x01",
            "everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everybody except for that idiot Randy\x01",
            "is always welcome here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FThe hell, man. I'm a payin' customer, too,\x01",
            "ya old fox.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_29C0")

    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "I welcome you to Barca Casino,\x01",
            "everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Would you like to try your luck at roulette?\x01",
            "A seat just happened to open up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301FWhy do you keep ignorin' me, ya old fox?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Feel free to make your presence scarce,\x01",
            "Randy. Your ilk is unneeded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Shoo, shoo! Leave something for the other\x01",
            "customers every once in a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FHarsh, dude. You're just salty that I've\x01",
            "been killin' it.\x02\x03",
            "#0300FI'll remember this! I'm gonna show up tonight and\x01",
            "there ain't a damn thing you can do about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Whatever you say, you damned brat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(I-Is Randy a regular here? What an\x01",
            "odd relationship those two have...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 0)

    label("loc_2C4B")

    TalkEnd(0x8)

    label("loc_2C4E")

    Return()

    # Function_6_7D4 end

    def Function_7_2C4F(): pass

    label("Function_7_2C4F")

    Call(0, 8)
    Return()

    # Function_7_2C4F end

    def Function_8_2C53(): pass

    label("Function_8_2C53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C78")
    Call(0, 28)
    Return()

    label("loc_2C78")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",          # 0
            "Exchange\x01",      # 1
            "Leave\x01",         # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CDA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2CDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D40")
    SetScenarioFlags(0x6D, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2CFC")
    OP_AF(0x41)
    Jump("loc_2D31")

    label("loc_2CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2D0C")
    OP_AF(0x40)
    Jump("loc_2D31")

    label("loc_2D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2D1C")
    OP_AF(0x3F)
    Jump("loc_2D31")

    label("loc_2D1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2D2F")
    OP_AF(0x3E)
    Jump("loc_2D31")

    label("loc_2D2F")

    OP_AF(0x3D)

    label("loc_2D31")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44C0")

    label("loc_2D40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D54")
    Jump("loc_44C0")

    label("loc_2D54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2E59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DB0")

    ChrTalk(
        0x9,
        "It's time to make some dough, guys! ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E54")

    label("loc_2DB0")


    ChrTalk(
        0x9,
        "Welcome to Barca Casino!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Teehee. We've become famous after\x01",
            "yesterday's little incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm happy to see all of these wonderful\x01",
            "new customers. ☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E54")

    Jump("loc_44C0")

    label("loc_2E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2F9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2EEC")

    ChrTalk(
        0x9,
        (
            "Lechter seems to be getting along\x01",
            "pretty well with the owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Look at him go! He's totally fitting in already. ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F99")

    label("loc_2EEC")


    ChrTalk(
        0x9,
        "Welcome to Barca Casino!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was here until late last night drinking\x01",
            "with Lechter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's a total weirdo, but he has plenty of\x01",
            "interesting stories to tell! ☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2F99")

    Jump("loc_44C0")

    label("loc_2F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_305A")

    ChrTalk(
        0x9,
        (
            "The guy that beat Gantz is drinking with\x01",
            "the owner right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He managed to draw a five of a kind\x01",
            "in their last big gamble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "He's totally a pro gambler, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_44C0")

    label("loc_305A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_32B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3127")

    ChrTalk(
        0x9,
        (
            "Gantz is currently in the middle of a\x01",
            "heated match with another customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Some man decided to rise to the\x01",
            "occasion after Galetti and Elinda\x01",
            "were no longer able to compete.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32AD")

    label("loc_3127")


    ChrTalk(
        0x9,
        (
            "Hey, Randy! The owner's over in\x01",
            "the special room if you need him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's been watching all of Gantz's\x01",
            "matches all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FOh, you mean that one room reserved\x01",
            "for VIPs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yep! Gantz is in the middle of a match\x01",
            "with some other guy right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's pretty crazy, isn't it? He used to\x01",
            "be some casual amateur, but now he\x01",
            "gets the full VIP treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0201F...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_32AD")

    Jump("loc_44C0")

    label("loc_32B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_342D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_333D")

    ChrTalk(
        0x9,
        (
            "Gantz has been coming here all\x01",
            "the time these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's almost as if he's a different person\x01",
            "altogether.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3428")

    label("loc_333D")


    ChrTalk(
        0x9,
        (
            "Gantz has been acting sorta odd...\x01",
            "Something about him feels...different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Those wins are getting to his head... His ego\x01",
            "must be as big as an inflated Mishy balloon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I feel like he's become a totally different person.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3428")

    Jump("loc_44C0")

    label("loc_342D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_34BE")

    ChrTalk(
        0x9,
        "You wanna know about Gantz?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You should probably talk to the owner\x01",
            "about him. He's usually up for a chat\x01",
            "over at the bar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44C0")

    label("loc_34BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_374D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_356A")

    ChrTalk(
        0x9,
        (
            "That guy has been making a killing.\x01",
            "It's actually downright unbelievable,\x01",
            "if you think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's been raking in the dough\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3748")

    label("loc_356A")


    ChrTalk(
        0x9,
        (
            "We've been getting a customer that hits\x01",
            "up the VIP room pretty often these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "He's been making some real bank.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He managed to clean out Galetti with a\x01",
            "straight flush yesterday. Everybody\x01",
            "was freaking out over it. ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FYou kiddin'?! There's somebody who\x01",
            "showboats as hard as I do?!\x02\x03",
            "#0301FOh, hell no! I'm gonna challenge\x01",
            "him to a duel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FStop making a scene, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0506FIs Randy a professional gambler?\x01",
            "He makes it sound like he is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3748")

    Jump("loc_44C0")

    label("loc_374D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_393A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_37D2")

    ChrTalk(
        0x9,
        (
            "Come to this counter to exchange for\x01",
            "more medals and prizes. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I hope you play your hearts out! ☆\x02",
    )

    CloseMessageWindow()
    Jump("loc_3935")

    label("loc_37D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38C6")

    ChrTalk(
        0x9,
        (
            "Oh. Hi, Randy. I haven't seen you\x01",
            "around here for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's good to see you again. Go\x01",
            "out there and have some fun. ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHaha. Kinda in the middle of somethin'\x01",
            "today, so I'm only gonna play for a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3932")

    label("loc_38C6")


    ChrTalk(
        0x9,
        "Oh? Randy isn't with you guys today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, whatever. Go out there and have\x01",
            "some fun, everyone! ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3932")

    SetScenarioFlags(0x0, 1)

    label("loc_3935")

    Jump("loc_44C0")

    label("loc_393A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3B4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_39A1")

    ChrTalk(
        0x9,
        (
            "Being a police officer seems like a\x01",
            "pretty cool career. I'm kinda jealous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B49")

    label("loc_39A1")


    ChrTalk(
        0x9,
        (
            "Are you gambling in the middle of the\x01",
            "day, Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's not a good idea. I'm going\x01",
            "to report you to your chief if you\x01",
            "don't stop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FChief...prooobably wouldn't give\x01",
            "a damn, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FYeah, he DOES love to be hands-off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FI suspect he may even join you at the tables.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FWhile true, he can at least act serious\x01",
            "when necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I see. You've got a nice boss,\x01",
            "don't you? ☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3B49")

    Jump("loc_44C0")

    label("loc_3B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3BCA")

    ChrTalk(
        0x9,
        (
            "I feel like the owner kinda has an\x01",
            "aura around him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I guess I can see it, now that I know.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D1B")

    label("loc_3BCA")


    ChrTalk(
        0x9,
        (
            "Apparently, the owner was a part of\x01",
            "some mafia back in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "His group was supposedly\x01",
            "eliminated by Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've even heard that he's got a gunshot\x01",
            "wound right on his chest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FYou serious? That old fox had a crazy\x01",
            "past like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Teehee. It's a secret, though! ☆\x01",
            "He doesn't like us talking about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3D1B")

    Jump("loc_44C0")

    label("loc_3D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3D9A")

    ChrTalk(
        0x9,
        "Welcome to Barca Casino!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The night has only just begun! ㈱\x01",
            "I hope you all play until you drop! ☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44C0")

    label("loc_3D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3E5C")

    ChrTalk(
        0x9,
        (
            "Arc en Ciel's new play's coming\x01",
            "next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I bet we're going to get a lot of customers,\x01",
            "seeing as how we're next door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I just can't wait to see these new faces! ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_44C0")

    label("loc_3E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_406C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3EDE")

    ChrTalk(
        0x9,
        (
            "You haven't been winning much these\x01",
            "days, have you, Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'm boooooored! Come play more often!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4067")

    label("loc_3EDE")


    ChrTalk(
        0x9,
        "Welcome to Barca, everyone! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh. Hi, Randy. I haven't seen you\x01",
            "around here much lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FSorry, sweet-cheeks. Been bustin' my\x01",
            "ass off at work. I can only come, like,\x01",
            "three times a week right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Booo! That sounds soooo boring!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FIsn't three times a week kind of a lot already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FFixing Randy's gambling addiction will\x01",
            "be a leviathan of a task.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4067")

    Jump("loc_44C0")

    label("loc_406C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_41BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_40FC")

    ChrTalk(
        0x9,
        (
            "I think something happened just\x01",
            "outside of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm safe inside of here, so...I don't\x01",
            "really care! Teehee! ☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41B9")

    label("loc_40FC")


    ChrTalk(
        0x9,
        "We had a visit by some officers moments ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently, something happened just outside\x01",
            "of here last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm safe inside of here, so...I don't\x01",
            "really care! Teehee! ☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_41B9")

    Jump("loc_44C0")

    label("loc_41BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4347")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4237")

    ChrTalk(
        0x9,
        "I guess the owner doesn't gamble these days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It's kinda disappointing, don't you think?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4342")

    label("loc_4237")


    ChrTalk(
        0x9,
        (
            "Galetti and Elinda are both incredible\x01",
            "gamblers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Let me tell you. If they went at you seriously,\x01",
            "you'd lose all of your money. Easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I actually heard that the owner is\x01",
            "way better than both of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I wanna see that with my own eyes some day.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4342")

    Jump("loc_44C0")

    label("loc_4347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_43C3")

    ChrTalk(
        0x9,
        (
            "Come to this counter to exchange for\x01",
            "more medals and prizes. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I hope you play your hearts out! ☆\x02",
    )

    CloseMessageWindow()
    Jump("loc_44C0")

    label("loc_43C3")


    ChrTalk(
        0x9,
        "Welcome to Barca Casino!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hi, Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hope you have lots of fun, like you\x01",
            "always do! ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FYou know it, Cherry! You can leave it\x01",
            "to me, baby!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F(So he's always coming here to have\x01",
            "fun, eh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(He's hopeless...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_44C0")

    Jump("loc_2C85")

    label("loc_44C5")

    TalkEnd(0x9)
    Return()

    # Function_8_2C53 end

    def Function_9_44C9(): pass

    label("Function_9_44C9")

    Call(0, 10)
    Return()

    # Function_9_44C9 end

    def Function_10_44CD(): pass

    label("Function_10_44CD")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5563")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                # 0
            "Play Poker\x01",          # 1
            "Play Blackjack\x01",      # 2
            "Leave\x01",               # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4540")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4540")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_458B")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_458B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45D6")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_45D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45EA")
    Jump("loc_555E")

    label("loc_45EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_555E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_46C7")

    ChrTalk(
        0xA,
        "Huh. Gantz isn't around today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A little strange, if you ask me. He usually\x01",
            "manages to come by, even if it's late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's probably still reeling from\x01",
            "his loss yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_555E")

    label("loc_46C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4766")

    ChrTalk(
        0xA,
        (
            "Casino's been the talk of the town ever\x01",
            "since yesterday's little incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's been a while since we had a thrilling\x01",
            "match like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_555E")

    label("loc_4766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_483D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_47A8")

    ChrTalk(
        0xA,
        "I just hope that Gantz is doing okay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4838")

    label("loc_47A8")


    ChrTalk(
        0xA,
        "I'm worried about Gantz's health.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We may have the occasional scuffle\x01",
            "during our matches, but he IS a\x01",
            "regular at our establishment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4838")

    Jump("loc_555E")

    label("loc_483D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_48D2")

    ChrTalk(
        0xA,
        (
            "It's looking like Gantz is going to make\x01",
            "a ton of money again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I feel kind of sorry for his opponent, to be honest.\x02",
    )

    CloseMessageWindow()
    Jump("loc_49C5")

    label("loc_48D2")


    ChrTalk(
        0xA,
        (
            "I went to observe the situation over in the VIP\x01",
            "room moments ago, and it's just as disappointing\x01",
            "as I was expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Gantz's opponent is getting totally murdered.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Meh. I guess he did tie Gantz once out\x01",
            "of their five matches.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_49C5")

    Jump("loc_555E")

    label("loc_49CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4A3A")

    ChrTalk(
        0xA,
        (
            "He used to pull off a full house at best,\x01",
            "so how the hell can he be that lucky now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B07")

    label("loc_4A3A")


    ChrTalk(
        0xA,
        (
            "Gantz has been drawing nothing but\x01",
            "incredible hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've watched him play, so I can pretty\x01",
            "confidently say that he isn't cheating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So how the hell is he that lucky?\x01",
            "I just don't get it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4B07")

    Jump("loc_555E")

    label("loc_4B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_4BC3")

    ChrTalk(
        0xA,
        "You'd like to know about Gantz?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah, he's a regular. Used to only come on\x01",
            "weekends, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think you'll be able to get more details\x01",
            "out of the owner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_555E")

    label("loc_4BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4C99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C32")

    ChrTalk(
        0xA,
        "Oh, hell. Have my skills gotten worse?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Pardon me. I'm rambling to myself.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4C94")

    label("loc_4C32")


    ChrTalk(
        0xA,
        (
            "I haven't suffered a loss this great in\x01",
            "a long, long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Have my skills gotten worse?\x02",
    )

    CloseMessageWindow()

    label("loc_4C94")

    Jump("loc_555E")

    label("loc_4C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4D40")

    ChrTalk(
        0xA,
        (
            "The casino saw its highest profit margins\x01",
            "ever during this year's Anniversary\x01",
            "Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm pleased we were able to show\x01",
            "everyone a good time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_555E")

    label("loc_4D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4DFE")

    ChrTalk(
        0xA,
        (
            "The Entertainment District thrives any time\x01",
            "Arc en Ciel performs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "S'pose we'll have to thank our big star,\x01",
            "Ilya Platiere, for all the fortune she\x01",
            "brings us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF7")

    label("loc_4DFE")


    ChrTalk(
        0xA,
        (
            "Actually, now that I think about it...\x01",
            "Isn't the private performance soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Arc en Ciel usually does a private performance\x01",
            "for their investors and affluential people\x01",
            "across the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "As a result, the casino sees more business.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4EF7")

    Jump("loc_555E")

    label("loc_4EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5036")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4F6D")

    ChrTalk(
        0xA,
        "Would anybody like to have a match?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Who knows? It could even be your lucky day.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5031")

    label("loc_4F6D")


    ChrTalk(
        0xA,
        (
            "The whims of fate can be\x01",
            "an unpredictable beast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You'll never be quite sure how\x01",
            "things are going to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This is precisely why men choose\x01",
            "to cling on to fate for their dear life.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5031")

    Jump("loc_555E")

    label("loc_5036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5084")

    ChrTalk(
        0xA,
        "Oh, evening already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It's crunch time for the casino.\x02",
    )

    CloseMessageWindow()
    Jump("loc_555E")

    label("loc_5084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_51E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5103")

    ChrTalk(
        0xA,
        "The VIP room has been reserved for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We'll be having some VIPs in attendance\x01",
            "after dark.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51E3")

    label("loc_5103")


    ChrTalk(
        0xA,
        (
            "Our special back room has already\x01",
            "been reserved today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I would assume it's because the\x01",
            "diet is coming to an end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "All kinds of politicians and business\x01",
            "executives have been coming to\x01",
            "get their kicks lately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_51E3")

    Jump("loc_555E")

    label("loc_51E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_530F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5258")

    ChrTalk(
        0xA,
        "Heh. I'm no stinking cheater.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A loss is a loss. You must graciously\x01",
            "accept it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_530A")

    label("loc_5258")


    ChrTalk(
        0xA,
        (
            "One of our customers yesterday was on\x01",
            "the verge of losing, so they tried to cheat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "*sigh* Utterly disgraceful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A loss is a loss. You must graciously\x01",
            "accept it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_530A")

    Jump("loc_555E")

    label("loc_530F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_547E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_53A0")

    ChrTalk(
        0xA,
        (
            "We have a special room for our VIPs\x01",
            "over in the back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No offense, but common folk are\x01",
            "prohibited from entering.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5479")

    label("loc_53A0")


    ChrTalk(
        0xA,
        (
            "We have a special room for our VIPs\x01",
            "over in the back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Heh. We may call them VIPs, but they're\x01",
            "usually diet members, or nobility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Given their influence, we need a special\x01",
            "room to satisfy their needs.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5479")

    Jump("loc_555E")

    label("loc_547E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_550A")

    ChrTalk(
        0xA,
        (
            "Miss Raytarossa is one of our regulars\x01",
            "that visits from the Republic once a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Heh. She's one hell of a gambler.\x02",
    )

    CloseMessageWindow()
    Jump("loc_555E")

    label("loc_550A")


    ChrTalk(
        0xA,
        "You've found the cards table.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Would you like to play a game of\x01",
            "blackjack?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_555E")

    Jump("loc_44DA")

    label("loc_5563")

    TalkEnd(0xA)
    Return()

    # Function_10_44CD end

    def Function_11_5567(): pass

    label("Function_11_5567")

    Call(0, 12)
    Return()

    # Function_11_5567 end

    def Function_12_556B(): pass

    label("Function_12_556B")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5578")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_655C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",               # 0
            "Play Roulette\x01",      # 1
            "Leave\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55D2")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_55D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_561D")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_561D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5631")
    Jump("loc_6557")

    label("loc_5631")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6557")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5777")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_56B1")

    ChrTalk(
        0xB,
        "Welcome to the Barca Casino.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I hope you all enjoy yourselves tonight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5772")

    label("loc_56B1")


    ChrTalk(
        0xB,
        "Looks like the diet's finally come to a close.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The casino usually doesn't light up until\x01",
            "nighttime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Heh. Everybody knows that's the best\x01",
            "time for a casino to earn some money.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5772")

    Jump("loc_6557")

    label("loc_5777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_58EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5848")

    ChrTalk(
        0xB,
        (
            "Ever since yesterday's high-stakes match,\x01",
            "people are beginning to think of us as a\x01",
            "classy establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not that I mind. All that means is that\x01",
            "there's more money to be made.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_5848")


    ChrTalk(
        0xB,
        (
            "Wow... I get the impression that we've got\x01",
            "way more customers than we normally do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think word about yesterday's high-stakes\x01",
            "match has spread.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_58E5")

    Jump("loc_6557")

    label("loc_58EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_59C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_593B")

    ChrTalk(
        0xB,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "That person's playing kind of...carelessly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_59BF")

    label("loc_593B")


    ChrTalk(
        0xB,
        (
            "That person's strategy is mystifying, to\x01",
            "be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Wh-What if...he's been losing intentionally,\x01",
            "all to put up an act?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_59BF")

    Jump("loc_6557")

    label("loc_59C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5A2A")

    ChrTalk(
        0xB,
        "*sigh* That man plays recklessly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I would quit while I'm ahead\x01",
            "if I were him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6557")

    label("loc_5A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5AB6")

    ChrTalk(
        0xB,
        (
            "Gantz's intuition and insight are beyond\x01",
            "comprehension...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've never experienced so many crushing\x01",
            "defeats in a row.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6557")

    label("loc_5AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_5C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5B56")

    ChrTalk(
        0xB,
        (
            "You'd be correct. Gantz is indeed one\x01",
            "of our regulars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think it'd be better if you heard\x01",
            "the details from the owner, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C2C")

    label("loc_5B56")


    ChrTalk(
        0xB,
        "Oh, Gantz?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yes, he is indeed one of our regulars.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He was a casual gambler with a penchant\x01",
            "for losing...until recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think it'd be better if you heard\x01",
            "the details from the owner, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5C2C")

    Jump("loc_6557")

    label("loc_5C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5D37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5CA5")

    ChrTalk(
        0xB,
        (
            "I like to claim that a gamble is a\x01",
            "matter of luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Even I manage to lose at times.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D32")

    label("loc_5CA5")


    ChrTalk(
        0xB,
        "*sigh* That guy destroyed me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Don't mind me. It's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "So what do you say? Would you like\x01",
            "to try your hand at a match?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5D32")

    Jump("loc_6557")

    label("loc_5D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5DE1")

    ChrTalk(
        0xB,
        (
            "It's my pleasure to welcome you\x01",
            "to our quaint little casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I would be more than happy to take\x01",
            "your challenge any time you visit Barca.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ECE")

    label("loc_5DE1")


    ChrTalk(
        0xB,
        (
            "Haha. Didn't you think the Anniversary\x01",
            "Festival was thrilling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Looks like a bunch of the tourists are\x01",
            "going to stay around for longer, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The good news is, the Entertainment\x01",
            "District will continue to prosper for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5ECE")

    Jump("loc_6557")

    label("loc_5ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5F5C")

    ChrTalk(
        0xB,
        (
            "Do your best to not get carried away,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Heheh. You'll end up drowning in debt\x01",
            "before you even notice it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6557")

    label("loc_5F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5FE7")

    ChrTalk(
        0xB,
        (
            "I may not look it, but I'm a\x01",
            "darn good gambler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You'll be sorely disappointed if you think\x01",
            "you can beat me easily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6557")

    label("loc_5FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_607C")

    ChrTalk(
        0xB,
        "Oh, wow. Look at the time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You can't hear the evening bell inside\x01",
            "of the casino, so I usually have trouble\x01",
            "telling the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6557")

    label("loc_607C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_60EB")

    ChrTalk(
        0xB,
        "Do you need something from the owner?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He's up on the second floor manning\x01",
            "the counter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6557")

    label("loc_60EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6142")

    ChrTalk(
        0xB,
        (
            "How do you think this year's\x01",
            "Anniversary Festival will go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6211")

    label("loc_6142")


    ChrTalk(
        0xB,
        "I personally cannot wait for next month's festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The Entertainment District is about to get\x01",
            "a whole lot busier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's our busiest time of the year, so we're\x01",
            "about to make a ton of money.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_6211")

    Jump("loc_6557")

    label("loc_6216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_63B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_62BB")

    ChrTalk(
        0xB,
        (
            "Those who have proven their worth\x01",
            "may enter the VIP room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you ask me, I think all of our patrons\x01",
            "should strive to make it there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63B0")

    label("loc_62BB")


    ChrTalk(
        0xB,
        (
            "Things got pret-ty crazy in the VIP\x01",
            "room last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Most of the people authorized to enter\x01",
            "the VIP room are gamblers that have\x01",
            "won a lot of money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you ask me, I think all of our patrons\x01",
            "should be striving to make it there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_63B0")

    Jump("loc_6557")

    label("loc_63B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6467")

    ChrTalk(
        0xB,
        (
            "Life's bittersweet trap is when you start to\x01",
            "think you understand how things will go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's when you'll end up having the rug\x01",
            "pulled out from under you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6557")

    label("loc_6467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_64BE")

    ChrTalk(
        0xB,
        (
            "Would you like to spin the roulette?\x01",
            "Today might be your lucky day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6557")

    label("loc_64BE")


    ChrTalk(
        0xB,
        "Welcome to the Barca Casino.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I like the look in your eyes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Would you like to spin the roulette? Who\x01",
            "knows, maybe you'll strike riches.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_6557")

    Jump("loc_5578")

    label("loc_655C")

    TalkEnd(0xB)
    Return()

    # Function_12_556B end

    def Function_13_6560(): pass

    label("Function_13_6560")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_65F4")
    Jump("loc_663E")

    label("loc_65F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6614")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_663E")

    label("loc_6614")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6634")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_663E")

    label("loc_6634")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_663E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_66C2")

    ChrTalk(
        0xC,
        "*sigh* I feel like I've lost my edge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Maybe it's time I returned home.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7BAD")

    label("loc_66C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6759")

    ChrTalk(
        0xC,
        (
            "I tried to press Lechter regarding\x01",
            "yesterday's match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "He dodged my questions, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Quite irritatingly, to be honest...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7BAD")

    label("loc_6759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_6967")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_67F1")

    ChrTalk(
        0xC,
        (
            "That Lechter man's skills are less than\x01",
            "stellar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yet he manages to trap you by giving you\x01",
            "a false sense of security.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6962")

    label("loc_67F1")


    ChrTalk(
        0xC,
        (
            "That Lechter man came yesterday, but his\x01",
            "skills weren't particularly memorable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I managed to utterly crush him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhat about that last hand, though?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FYeah, no kiddin'. Pullin' a five of a kind\x01",
            "off to beat a straight flush ain't somethin'\x01",
            "any regular guy could do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Nothing more than a mere coincidence,\x01",
            "perhaps. I can't be too sure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6962")

    Jump("loc_7BAD")

    label("loc_6967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_69DE")

    ChrTalk(
        0xC,
        (
            "Some moron tried to challenge\x01",
            "Gantz to a match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I gave him a warning, but he failed to listen.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7BAD")

    label("loc_69DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_6AF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6A5D")

    ChrTalk(
        0xC,
        "I, too, have foolishly challenged him before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I didn't sense that he was the least bit\x01",
            "inept.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AF1")

    label("loc_6A5D")


    ChrTalk(
        0xC,
        (
            "I heard that Gantz used to be\x01",
            "a third-rate gambler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Is that really the truth, though? I failed to\x01",
            "get that impression from him at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6AF1")

    Jump("loc_7BAD")

    label("loc_6AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6BB5")

    ChrTalk(
        0xC,
        (
            "This is only what I've heard, but there's\x01",
            "supposedly a person that keeps pulling\x01",
            "off impressive victories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'll admit I'm interested in seeing it for myself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C93")

    label("loc_6BB5")


    ChrTalk(
        0xC,
        (
            "I've just returned to Crossbell for the first time\x01",
            "in a few weeks, and I believe I've stumbled upon\x01",
            "something most interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Is the house not on a losing streak?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Who might this formidable opponent be?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6C93")

    Jump("loc_7BAD")

    label("loc_6C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6DFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6D4D")

    ChrTalk(
        0xC,
        (
            "This sounds like a most favorable opportunity for\x01",
            "me to exit the fray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I believe I've had my fill. Perhaps it is time\x01",
            "I conceded and returned home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DF8")

    label("loc_6D4D")


    ChrTalk(
        0xC,
        (
            "Phew... I had Drake do me the favor of playing\x01",
            "a few games to help pass the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "The owner is truly powerful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It's been some time since my last defeat.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6DF8")

    Jump("loc_7BAD")

    label("loc_6DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6F34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6E65")

    ChrTalk(
        0xC,
        "I managed to beat that man once again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Perhaps I was too harsh on him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F2F")

    label("loc_6E65")

    OP_4B(0xA, 0xFF)
    SetChrSubChip(0xC, 0x0)

    ChrTalk(
        0xA,
        (
            "I would not expect any less of you, considering\x01",
            "your skills, Miss Raytarossa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Allow me to offer you this glass of wine, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, my. Quite the thoughtful one, aren't we?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)

    label("loc_6F2F")

    Jump("loc_7BAD")

    label("loc_6F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_713E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_700C")

    ChrTalk(
        0xC,
        (
            "I've heard the IBC has the most assets\x01",
            "out of any company in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm not particularly surprised the IBC\x01",
            "has outdone the Empire or Republic\x01",
            "when it comes to mira, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7139")

    label("loc_700C")


    ChrTalk(
        0xC,
        (
            "I've heard the IBC has the most assets\x01",
            "out of any company in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Crossbell is known as a confluence of mira.\x01",
            "Given their historical international bank, it's\x01",
            "only natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The true surprise is how they've managed\x01",
            "to strike greater riches than the Reinford\x01",
            "and Verne Companies.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7139")

    Jump("loc_7BAD")

    label("loc_713E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7194")
    SetChrSubChip(0xC, 0x2)

    ChrTalk(
        0xC,
        (
            "Sheesh... I have never met such an\x01",
            "entitled man in all my life.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_7194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_72DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_721C")

    ChrTalk(
        0xC,
        (
            "Supposedly the CGF's commander is\x01",
            "an absolute casanova.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "You have to pity his poor subordinates, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_72D8")

    label("loc_721C")


    ChrTalk(
        0xC,
        "The CGF is an elite corps, is it not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Though, I've heard their commander is\x01",
            "an absolute casanova.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I pity his poor subordinates. He must be\x01",
            "rather difficult to work with.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_72D8")

    Jump("loc_7BAD")

    label("loc_72DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_75A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_734C")

    ChrTalk(
        0xC,
        "Oh, Father... You've prepared far too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "*sigh* I can't enjoy it this way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_759D")

    label("loc_734C")


    ChrTalk(
        0xC,
        (
            "I came by this month with hopes of\x01",
            "purchasing tickets for Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FHeh. Lotta tourists like yourself are here\x01",
            "to buy 'em right now, ma'am.\x02\x03",
            "#0300FNot worth gettin' depressed if you didn't\x01",
            "manage to get your hands on any.\x02\x03",
            "If you wanna wait a couple of months,\x01",
            "this handsome fella would gladly--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've got my own tickets, already.\x01",
            "Father arranged it for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "*sigh* I feel as if I've missed out on an\x01",
            "important experience.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0306FMaaaan... That wasn't how it was\x01",
            "supposed to go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FRecompose yourself, Randy. You will live.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_759D")

    Jump("loc_7BAD")

    label("loc_75A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_76EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7629")

    ChrTalk(
        0xC,
        (
            "It feels as though my mind and body are\x01",
            "enchanted when I visit Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I quite enjoy this feeling.\x02",
    )

    CloseMessageWindow()
    Jump("loc_76E5")

    label("loc_7629")


    ChrTalk(
        0xC,
        (
            "It feels as though my mind and body are\x01",
            "enchanted when I visit Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I feel as if the bustling of the city causes\x01",
            "my head to go numb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It's not a bad feeling at all.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_76E5")

    Jump("loc_7BAD")

    label("loc_76EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7864")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_779A")

    ChrTalk(
        0xC,
        (
            "Have you heard that Drake used to\x01",
            "be a famous gambler?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Not only that, but he was also in a mafia.\x01",
            "I...may be slightly interested to hear more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_785F")

    label("loc_779A")


    ChrTalk(
        0xC,
        "I'm already tired of playing at the cards table.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Perhaps I'll request Drake to do me the\x01",
            "favor of being my opponent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've heard that he was a famous gambler\x01",
            "in his younger years.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_785F")

    Jump("loc_7BAD")

    label("loc_7864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 1)), scpexpr(EXPR_END)), "loc_7933")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7899")

    ChrTalk(
        0xC,
        "I like my men strong. ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_792E")

    label("loc_7899")


    ChrTalk(
        0xC,
        "I like my men strong. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309F(Bless Aidios! I friggin' love the casino!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Aren't you getting a little too excited,\x01",
            "Randy?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_792E")

    Jump("loc_7BAD")

    label("loc_7933")

    SetChrSubChip(0xC, 0x0)
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x104, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_79CB")
    Jump("loc_7A15")

    label("loc_79CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79EB")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A15")

    label("loc_79EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A0B")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A15")

    label("loc_7A0B")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A15")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        "Oh? So you are the famed Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've heard the rumors. You're\x01",
            "quite the gambler, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309F*whistle* It's an honor to be beckoned by\x01",
            "a lovely lady like yourself, ma'am.\x02\x03",
            "#0300FHey, wanna have a gamble with our\x01",
            "lives on the line?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0111FExcuse me. Could you spare us from\x01",
            "your debauchery?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FOr save it for some other time,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 1)

    label("loc_7BAD")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_6560 end

    def Function_14_7BB5(): pass

    label("Function_14_7BB5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7C49")
    Jump("loc_7C93")

    label("loc_7C49")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C69")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C93")

    label("loc_7C69")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C89")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C93")

    label("loc_7C89")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7C93")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7E34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7D45")

    ChrTalk(
        0xD,
        "It's important to be able to shift your focus.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Such is the key to playing at the casino\x01",
            "for longer periods.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E2F")

    label("loc_7D45")


    ChrTalk(
        0xD,
        "Gah... I lost too much mira today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Not much I can do about it, I suppose.\x01",
            "Guess I'll buy the old missus a present\x01",
            "to smooth things over before I go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's important to be able to shift your focus\x01",
            "while gambling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7E2F")

    Jump("loc_924E")

    label("loc_7E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7EE3")

    ChrTalk(
        0xD,
        "Gah... Just thinking about Lechter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I saw that brat withdraw 30,000 medals.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Seeing that made me all cranky. I'm\x01",
            "not going to let him one-up me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_924E")

    label("loc_7EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_7F6E")

    ChrTalk(
        0xD,
        "What's with all the ruckus downstairs?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Lotta scary stories these days. We've\x01",
            "got some turbulent times ahead of us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_924E")

    label("loc_7F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8074")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7FE7")

    ChrTalk(
        0xD,
        (
            "Am I getting old, or has Gantz gotten\x01",
            "freakishly good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Nobody can beat the guy anymore.\x02",
    )

    CloseMessageWindow()
    Jump("loc_806F")

    label("loc_7FE7")


    ChrTalk(
        0xD,
        (
            "I heard Gantz was making a fortune\x01",
            "in the VIP room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "A tourist is playing against Gantz, hmm?\x01",
            "Oh, well. It's their funeral.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_806F")

    Jump("loc_924E")

    label("loc_8074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_8101")

    ChrTalk(
        0xD,
        (
            "It's dark out already? I'm having\x01",
            "such a good time, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I don't want to go home! I'm still on\x01",
            "a gambling high!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_924E")

    label("loc_8101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_827E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_81B1")

    ChrTalk(
        0xD,
        (
            "I've heard a rumor about some dispute\x01",
            "between mafias happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Be careful out there, lads and lasses.\x01",
            "Try not to get caught up in their mess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8279")

    label("loc_81B1")


    ChrTalk(
        0xD,
        (
            "Word on the street is that Revache\x01",
            "has been behaving suspiciously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "You kids better be careful out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Don't get involved with 'em. They won't\x01",
            "let detectives like you off lightly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8279")

    Jump("loc_924E")

    label("loc_827E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_84D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8325")

    ChrTalk(
        0xD,
        (
            "My battle axe of a wife has been nagging\x01",
            "me faaaaaaar too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then again, I suppose it's good that she's\x01",
            "still healthy for her age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84D0")

    label("loc_8325")


    ChrTalk(
        0xD,
        (
            "The ol' battle axe always nags at me for\x01",
            "going to the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We had another argument this morning,\x01",
            "so she stormed off to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Phew... Been sweating bullets all day\x01",
            "because of her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84CD")

    ChrTalk(
        0x104,
        (
            "#0300FHaha. Some things never change, do\x01",
            "they, Gramps?\x02\x03",
            "Ever consider cleanin' up that act and\x01",
            "making your life a little easier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You're one to talk, Randy! Anyway,\x01",
            "I'm not leaving until I win a prize.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84CD")

    SetScenarioFlags(0x0, 5)

    label("loc_84D0")

    Jump("loc_924E")

    label("loc_84D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_86A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8586")

    ChrTalk(
        0xD,
        (
            "The fact that all of us can live in comfort is\x01",
            "thanks to the Geofront's existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Although, I hear the city's management is\x01",
            "in total disarray.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A0")

    label("loc_8586")


    ChrTalk(
        0xD,
        (
            "The Geofront was planned approximately\x01",
            "twenty years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "They built it with urgency, considering our\x01",
            "infrastructure started to rapidly degrade\x01",
            "as our population increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The thing's expanded so much that it\x01",
            "practically encircles the whole city from\x01",
            "underground.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_86A0")

    Jump("loc_924E")

    label("loc_86A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_888E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8751")

    ChrTalk(
        0xD,
        (
            "Grr... That damned wife of mine. She's been\x01",
            "making these visits more complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Too bad it's not enough to get me to\x01",
            "abandon the casino!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8889")

    label("loc_8751")


    ChrTalk(
        0xD,
        (
            "Geez Louise! It is NOT easy to pull the wool\x01",
            "over the eyes of that ol' battle axe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I tried to sneak out of the back exit of\x01",
            "my house this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And then I just about ran into her on\x01",
            "the street corner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*sigh* I ran away in a panic. I HAD to have\x01",
            "been seconds away from getting caught.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8889")

    Jump("loc_924E")

    label("loc_888E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_89A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_890E")

    ChrTalk(
        0xD,
        (
            "I used to be able to soak in the nightlife,\x01",
            "but this old body o' mine can hardly\x01",
            "handle it anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_899E")

    label("loc_890E")


    ChrTalk(
        0xD,
        (
            "Whoops! Better head home, or I'm going to\x01",
            "get an earful from the missus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The nightlife can get pretty harsh when\x01",
            "you reach my age.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_899E")

    Jump("loc_924E")

    label("loc_89A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8B6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8A79")

    ChrTalk(
        0xD,
        (
            "The Entertainment District hasn't changed\x01",
            "one bit after all these years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The crime rate has been getting pretty\x01",
            "bad as of late, too. Strangers to this\x01",
            "district ought to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B6A")

    label("loc_8A79")


    ChrTalk(
        0xD,
        (
            "Regardless of how much Crossbell changes,\x01",
            "the Entertainment District will never die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Bars, casinos, floods of tourists, and\x01",
            "cute girls... ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It may change on the outside a little,\x01",
            "but it'll still be the same underneath it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8B6A")

    Jump("loc_924E")

    label("loc_8B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8BCE")

    ChrTalk(
        0xD,
        (
            "I lost too much money yesterday. I NEED\x01",
            "to make up for it somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CCC")

    label("loc_8BCE")


    ChrTalk(
        0xD,
        "Oooh! I'm in good form today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Time for the money to return to Papa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHaven't been here in a hot minute. Good\x01",
            "knowin' you haven't changed, Gramps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Is that you, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You're damn right. I need to play the\x01",
            "slots every day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8CCC")

    Jump("loc_924E")

    label("loc_8CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8E1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8D3E")

    ChrTalk(
        0xD,
        "The casino's the only thing I live for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Don't take the casino away from me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E17")

    label("loc_8D3E")


    ChrTalk(
        0xD,
        (
            "Damn that ol' battle axe. She ambushed\x01",
            "me as I was leaving this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Boy, did she lay into me this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I thought she was going to drag me\x01",
            "back there by the collar. Phew, that\x01",
            "was a close call.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8E17")

    Jump("loc_924E")

    label("loc_8E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_903B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8EF7")

    ChrTalk(
        0xD,
        (
            "I've been parading around these streets\x01",
            "for 50 years. I've been here since the\x01",
            "day this neighborhood was built.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You're still a baby sucking from his\x01",
            "mother's teat compared to me, Randy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9036")

    label("loc_8EF7")


    ChrTalk(
        0xD,
        (
            "I've been parading around these streets\x01",
            "for 50 years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You're still a baby sucking from his\x01",
            "mother's teat compared to me, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHeh. Ya got me there, Gramps. Only been\x01",
            "around these parts for a year and a half\x01",
            "at most.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIs it truly worth competing over something\x01",
            "this shameless, Randy?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_9036")

    Jump("loc_924E")

    label("loc_903B")

    SetChrSubChip(0xD, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_90B1")

    ChrTalk(
        0xD,
        (
            "Shut up! Don't distract me! I've got\x01",
            "a good rhythm going!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Okay, here we go! HERE! WE! GO!\x02",
    )

    CloseMessageWindow()
    Jump("loc_924E")

    label("loc_90B1")


    ChrTalk(
        0x104,
        "#0300FHow's it goin', Rick?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I know that voice. That you, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Shut up! Don't distract me! I've got\x01",
            "a good rhythm going!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHahaha. Good to see you haven't changed.\x02\x03",
            "Don'tcha think you're playin' a bit too\x01",
            "much, though? You're not gonna hear\x01",
            "the end of it from the missus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "If it happens, it happens!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Why am I not surprised that all of\x01",
            "Randy's friends behave like him?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_924E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_7BB5 end

    def Function_15_9256(): pass

    label("Function_15_9256")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9347")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_92B5")

    ChrTalk(
        0xE,
        (
            "Damn it! That lady running the\x01",
            "roulette table is a total demon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9342")

    label("loc_92B5")


    ChrTalk(
        0xE,
        (
            "Hey, uh... Could I bum some mira\x01",
            "off of you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I accidentally blew everything I had. I don't\x01",
            "have enough for the train fare home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_9342")

    Jump("loc_94DF")

    label("loc_9347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_93C4")

    ChrTalk(
        0xE,
        "Ughhhhh... Damn it all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm definitely...DEFINITELY going to crush\x01",
            "her like a bug next time we play!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94DF")

    label("loc_93C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9433")

    ChrTalk(
        0xE,
        (
            "Women like her always give\x01",
            "me a bad headache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I'm gonna send her home crying to mommy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_94DF")

    label("loc_9433")


    ChrTalk(
        0xE,
        "Sonuvabitch! I lost again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "That chick at the cards table gave me\x01",
            "a total beatdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'll definitely...DEFINITELY crush her\x01",
            "like a bug next time we play!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_94DF")

    TalkEnd(0xFE)
    Return()

    # Function_15_9256 end

    def Function_16_94E3(): pass

    label("Function_16_94E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9603")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9576")

    ChrTalk(
        0xF,
        (
            "I lost six times in seven matches...?\x01",
            "I can't believe this at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "*sigh* I have no pride left as a gambler...\x02",
    )

    CloseMessageWindow()
    Jump("loc_95FE")

    label("loc_9576")


    ChrTalk(
        0xF,
        (
            "I-It's no use... The chick at the cards\x01",
            "table took everything I had...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Guess I'll...head home and start over\x01",
            "from scratch.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_95FE")

    Jump("loc_98F7")

    label("loc_9603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_975D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_96AF")

    ChrTalk(
        0xF,
        (
            "I've gone to casinos all over the continent\x01",
            "and kicked some major ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "And despite that, you Crossbellan gamblers\x01",
            "scare the hell outta me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9758")

    label("loc_96AF")


    ChrTalk(
        0xF,
        (
            "D-Damn it... I tried my luck at the roulette\x01",
            "table after I got my ass kicked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But still! You guys are all freakishly strong!\x01",
            "How's everyone so powerful?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_9758")

    Jump("loc_98F7")

    label("loc_975D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_982A")

    ChrTalk(
        0xF,
        (
            "That chick at the cards table is\x01",
            "pretty skilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm not going to show her mercy just 'cause\x01",
            "she's a lady. I'm a gambler, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I'll come at her with all I got next time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_98F7")

    label("loc_982A")


    ChrTalk(
        0xF,
        (
            "I've been touring casinos all over the\x01",
            "continent to train my skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hmph. I'll have to train exclusively in\x01",
            "Crossbell this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It's the only thing I can do to match up\x01",
            "to these monsters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98F7")

    TalkEnd(0xFE)
    Return()

    # Function_16_94E3 end

    def Function_17_98FB(): pass

    label("Function_17_98FB")

    TalkBegin(0xFE)

    ChrTalk(
        0x10,
        "Wh-What the hell?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "You got a straight flush?! Are you\x01",
            "KIDDING me right now?!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_98FB end

    def Function_18_9959(): pass

    label("Function_18_9959")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99ED")
    Jump("loc_9A37")

    label("loc_99ED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9A0D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A37")

    label("loc_9A0D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A2D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A37")

    label("loc_9A2D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A37")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 3)), scpexpr(EXPR_END)), "loc_9B59")

    ChrTalk(
        0x11,
        (
            "#3504FWell, I'm all finished with my mission.\x01",
            "It'd be kinda boring to just up and\x01",
            "leave like this, though.\x02\x03",
            "#3510FThink I'll have a little bit of 'me' time,\x01",
            "if you know what I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0013F(Did he just say mission? What mission?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_A0DE")

    label("loc_9B59")


    ChrTalk(
        0x11,
        "#3505FYo, guys. How's he holding up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FSorry, Lechter. We can't exactly hand out\x01",
            "classified information like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FBut still, I think things have finally begun\x01",
            "to calm down.\x02\x03",
            "#0100FI believe you'll be able to demand an\x01",
            "apology out of him later, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3509FHahaha! What are you even talking about?!\x02\x03",
            "#3500FIt's not like I MEANT to wait until the very end\x01",
            "to crush all his hopes and dreams and bring\x01",
            "him back down to earth, ya know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0011FHold on... Did you intentionally wait until\x01",
            "the last hand to beat him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FThere's no friggin' way, man. That was just\x01",
            "some lucky coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3509FSure was. A big, beautiful coincidence.\x01",
            "Karma must have noticed all the good\x01",
            "deeds I've done and rewarded me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0008F(Did he actually destroy Gantz like that\x01",
            "on purpose? If so...how?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F(Eh, who knows? I've definitely lost all\x01",
            "confidence in my poker skills, though.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211F(I am under the impression that nothing\x01",
            "is impossible for a man like Lechter.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3504FHey, I only gave you guys a helping hand.\x02\x03",
            "That guy would've ended up like that sooner\x01",
            "or later, anyway. Just so happened to be\x01",
            "the former, I guess.\x02\x03",
            "#3502FHaha. I'll leave the annoying stuff to you guys.\x01",
            "Just make sure you don't take your eyes off\x01",
            "of him, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FWe know that already.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 3)

    label("loc_A0DE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_9959 end

    def Function_19_A0E6(): pass

    label("Function_19_A0E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1200, 500, 10850, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 0, 0, -6250, 0)
    SetChrPos(0x102, -1000, 0, -5500, 0)
    SetChrPos(0x103, 1000, 0, -4500, 0)
    SetChrPos(0x104, 0, 0, -3900, 0)
    OP_68(-1360, 500, 6970, 3000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(500)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_68(6530, 5500, 10270, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20800, 0)
    OP_68(-1050, 5500, 21040, 5000)
    MoveCamera(41, 24, 0, 5000)
    SetCameraDistance(20800, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1500, -5000, 0)
    MoveCamera(49, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xD, 0x8000)

    ChrTalk(
        0x104,
        "#0309FThink I'll go for a couple of rounds today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FI am beginning to think that you have an\x01",
            "addiction, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106FHe should be patrolling, but he always ends\x01",
            "up getting carried away in the casino...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FWe're supposed to be gathering intel, so\x01",
            "I won't tell him to not play at all...\x02\x03",
            "#0000F*sigh* Just try to show some restraint, Randy.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In order to play games at the casino, you\x01",
            "must exchange your mira for medals at\x01",
            "the front desk.\x02\x03",
            "You cannot exchange medals for mira,\x01",
            "but you may exchange them for prizes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToBright(300, 0)
    SetChrPos(0x0, 0, 0, -5000, 0)
    SetScenarioFlags(0x6D, 5)
    EventEnd(0x5)
    Return()

    # Function_19_A0E6 end

    def Function_20_A497(): pass

    label("Function_20_A497")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Play Slots\x01",      # 0
            "Leave\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A520")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_A520")

    TalkEnd(0xFF)
    Return()

    # Function_20_A497 end

    def Function_21_A524(): pass

    label("Function_21_A524")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, -500, 14500, 0)
    MoveCamera(30, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -100, 0, -5300, 0)
    SetChrPos(0x102, 1100, 0, -4900, 330)
    SetChrPos(0x103, -1100, 0, -4900, 30)
    SetChrPos(0x104, 0, 0, -3700, 0)
    OP_68(0, 500, 7500, 6000)
    SetCameraDistance(25000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1000, -2700, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)

    def lambda_A600():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF574, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A600)
    WaitChrThread(0x104, 1)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#4100578V#0302F#11P'Bout time for business at the casino\x01",
            "to really pick up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#4100579V#0309F#5PYou guys ready? Let's find ourselves a\x01",
            "miner and hit the slots, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100580V#12P#0006FWe're only going to be doing one of\x01",
            "those things, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100581V#12P#0211FConsidering we are not undercover, there\x01",
            "is absolutely zero reason for us to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100582V#0103F#12PAgreed. Anyway, let's just stick with\x01",
            "questioning employees and customers.\x02\x03",
            "#4100583V#0100FPerhaps that will lead to some clue about\x01",
            "Gantz's whereabouts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100584V#0306F#5PYeah, yeah. Killjoys.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, -4700, 0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xC1, 5)
    OP_C7(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_21_A524 end

    def Function_22_A88E(): pass

    label("Function_22_A88E")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(-900, 5000, 20000, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -1100, 4000, 17400, 0)
    SetChrPos(0x102, 200, 4000, 17800, 0)
    SetChrPos(0x103, -2000, 4000, 17800, 0)
    SetChrPos(0x104, -900, 4000, 18700, 0)
    SetChrPos(0x8, -900, 4000, 21300, 180)
    OP_0D()

    ChrTalk(
        0x8,
        "#4100585V#5PGood evening, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4100586V#5PHave you all come to play with Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100587V#12P#0001FNo, not today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100588V#0300F#11PWe actually wanna ask you something.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd asked about the missing miner.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#4100589V#5PMissing? That's preposterous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100590V#5PHe came here earlier. The guy managed\x01",
            "to make a killing, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4100591V#12P#0005FWait, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100592V#0105F#12PAnd he was winning, you say...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100593V#0301F#11PC'mon, Drake. You must be thinkin' of\x01",
            "someone else, right?\x02\x03",
            "#4100594VY'see, we're lookin' for a miner from Mainz.\x01",
            "I doubt he has the skill OR intuition needed\x01",
            "to stay afloat here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4100595V#5PI assure you, I know the man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100596V#5PIt all started about two weeks ago... It'd been\x01",
            "a while since I last saw him, but I swear it was\x01",
            "like he was a completely different person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100597V#5PThanks to him, my dealers are in the middle of\x01",
            "a losing streak. We've lost almost...\x01",
            "500,000 mira to him now?\x02",
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
        "#4100598V#12P#0011FFive hundred THOUSAND?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100599V#12P#0205FThat is an exorbitant amount of money...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100600V#0306F#11PThere's no friggin' way, man...\x02\x03",
            "#4100601V#0301FHe's gotta be cheating, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100602V#5PAs I'm sure you know, we are professionals.\x01",
            "If someone was cheating, we would notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100603V#5PBesides, he not only has shown incredible\x01",
            "talent, but miraculously good luck as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100604V#5PEverybody here would like to know how in\x01",
            "the world he turned into a gambling phenom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100605V#0303F#11PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100606V#0106F#12PThis is quite different from the story\x01",
            "Mayor Bickson gave us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100607V#12P#0003FExcuse me, sir.\x02\x03",
            "#4100608V#0001FApparently, Gantz hasn't returned to\x01",
            "Mainz yet...\x02\x03",
            "#4100609VDo you have any idea where he's staying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4100610V#5PAh, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100611V#5PLast I heard, he's staying at the hotel\x01",
            "across the street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4100612V#5PThe deluxe suite on the top floor, no less.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#4100613V#12P#0005FWell, I guess he does have the mira for it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100614V#0306F#11PSeriously, though, that place is crazy\x01",
            "expensive.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        (
            "#4100615V#6P#0202FIn any case, I am surprised we were able to\x01",
            "find him this easily.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        (
            "#4100616V#0100F#11PLikewise. We should go and pay\x01",
            "him a visit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x8, -900, 4000, 21300, 180)
    SetChrPos(0x0, -900, 4000, 17500, 180)
    OP_4C(0x8, 0xFF)
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    SetScenarioFlags(0xC1, 6)
    OP_29(0x4A, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_22_A88E end

    def Function_23_B39F(): pass

    label("Function_23_B39F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    LoadChrToIndex("chr/ch07402.itc", 0x1F)
    LoadChrToIndex("chr/ch37600.itc", 0x20)
    LoadChrToIndex("chr/ch37602.itc", 0x21)
    LoadChrToIndex("chr/ch23200.itc", 0x22)
    OP_68(0, 0, 3000, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -700, 0, -5800, 0)
    SetChrPos(0x102, 700, 0, -5800, 0)
    SetChrPos(0x103, -700, 0, -6900, 0)
    SetChrPos(0x104, 700, 0, -6900, 0)
    SetChrPos(0x13D, 0, 0, -8000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 102200, 100, 5000, 270)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 97800, 100, 5000, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 0, -1000, 3000, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 101300, 0, 1600, 315)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearMapFlags(0x10000000)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis085.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis086.itp")
    SetCameraDistance(26500, 3000)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_B5A7():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5A7)

    def lambda_B5C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5C1)
    Sleep(50)

    def lambda_B5D5():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B5D5)

    def lambda_B5EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B5EF)
    Sleep(50)

    def lambda_B603():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B603)

    def lambda_B61D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B61D)
    Sleep(50)

    def lambda_B631():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B631)

    def lambda_B64B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B64B)
    Sleep(50)

    def lambda_B65F():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_B65F)

    def lambda_B679():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13D, 2, lambda_B679)
    Sleep(1300)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x12, 0xB4, 0x1F4)

    ChrTalk(
        0x12,
        "#4200433VOh, you came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4200434VI think a fight is about to break out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200435V#0013FQuickly take us to where Gantz is\x01",
            "playing, sir!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4200436VSure.\x02",
    )

    CloseMessageWindow()

    def lambda_B758():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_B758)
    OP_68(-3000, 0, 20200, 2500)
    MoveCamera(33, 15, 0, 2500)
    OP_6F(0x41)

    ChrTalk(
        0x12,
        (
            "#4200437VHe's in the middle of a private match\x01",
            "in the back room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4200438VWe don't have time to waste. Gantz\x01",
            "could blow at any second!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200439V#0011FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200440V#0105FWasn't Gantz the one provoking\x01",
            "his opponent?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x9C4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_68(100200, 1000, 2000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 99900, 0, -7000, 0)
    SetChrPos(0x102, 99900, 0, -7000, 0)
    SetChrPos(0x103, 99900, 0, -7000, 0)
    SetChrPos(0x104, 99900, 0, -7000, 0)
    SetChrPos(0x13D, 99900, 0, -7000, 0)
    SetChrPos(0x12, 99900, 0, -7000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(100570, 1000, 5280, 4000)
    Sleep(10)
    PlayBGM("ed7518", 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13,
        "#4200441V#5PEat this, punk!\x02",
    )

    CloseMessageWindow()
    Sound(90, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0x13,
        (
            "#4200442VNine, ten, jack, queen, and king! A\x01",
            "straight flush of diamonds, baby!\x02\x03",
            "#4200443VTry to beat this hand! You can't!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0x14,
        (
            "#4200444V#3507FGah! Are you kidding me?\x02\x03",
            "#4200445V#3506FWasn't expecting you to pull out a\x01",
            "hand that strong on our last round...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#4200446V#5PHah! This is my true talent!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4200447V#5PYou tied one too many games using\x01",
            "those tricky hands of yours, but that's\x01",
            "coming to an end!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13,
        (
            "#4200448V#5P#4SC'mon, show us your hand! Might as\x01",
            "well give up while you're at it, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x14,
        (
            "#4200449V#11P#3505FHuh? Are you feeling okay, man?\x02\x03",
            "#4200450V#3510FWho said anything about losing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#4200451V#5PA-Are you kidding me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4200452V#5PThe only way you'd be able to beat me\x01",
            "is with a royal straight flush!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#4200453V#5PThere's no way you could have--\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#4200454V#11P#3504FAnd that's where you're wrong, pal.\x02",
    )

    CloseMessageWindow()
    Sound(90, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0x13,
        "#4200455VWhat?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0x8,
        (
            "#4200456VA five of a kind? And they're ALL aces?!\x02\x03",
            "#4200457VI can't believe what I've seen today!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0x14,
        (
            "#4200458V#3504FWhat hands beat a royal straight flush\x01",
            "usually depends on the rules, but...\x02\x03",
            "#4200459V#3500F...rules or no rules, it's obvious that this\x01",
            "blows your straight flush outta the water.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    ChrTalk(
        0x13,
        "#4200460V#5P#60WWh-Wh-What...?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)

    def lambda_BF48():
        OP_9D(0xFE, 0x18060, 0x0, 0x1388, 0x64, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BF48)
    WaitChrThread(0x8, 1)
    Sound(819, 0, 100, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)

    ChrTalk(
        0x13,
        "#4200461V#5P#4SDon't screw with me, you damn cheat!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x8, 500)

    ChrTalk(
        0x13,
        (
            "#4200462V#5PDrake! You're his accomplice, aren't you?!\x01",
            "Well, screw you, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200463V#11PI-I assure you, I am nothing of the sort!\x01",
            "I swear upon Aidios Herself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200464V#11PAnd during my careful observation of\x01",
            "the match, I saw nothing that suggests\x01",
            "Mr. Arundel was cheating!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)

    ChrTalk(
        0x13,
        (
            "#4200465V#5PCan it! How the hell am I supposed to\x01",
            "buy that crap?!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(101140, 1000, 4800, 1000)

    def lambda_C14F():

        label("loc_C14F")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_C14F")

    QueueWorkItem2(0x8, 2, lambda_C14F)

    def lambda_C161():
        OP_95(0xFE, 98400, 0, 2100, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C161)
    WaitChrThread(0x13, 1)

    def lambda_C17F():
        OP_95(0xFE, 100800, 0, 1600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C17F)
    Sleep(50)
    SetChrSubChip(0x14, 0x1)
    WaitChrThread(0x13, 1)
    EndChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    Sound(804, 0, 100, 0)

    def lambda_C1B8():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C1B8)

    def lambda_C1D1():
        OP_96(0xFE, 0x18BB4, 0xC8, 0x640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C1D1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    ClearChrFlags(0x8, 0x20)

    ChrTalk(
        0x13,
        (
            "#4200466V#5PI've got luck and intuition on my side!\x01",
            "I'm supposed to be unstoppable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4200467V#5PThere's no way I can lose to\x01",
            "this jackass!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4200468VS-Sir, please calm yourself...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#4200469V#5P#3505FSeriously, dude. Take a chill pill.\x02\x03",
            "#4200470V#3504FPoker's just a game of luck, after all.\x02\x03",
            "#4200471V#3501FAll it means is that your luck has run\x01",
            "out, bud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#4200472V#5P#40W...\x02",
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    def lambda_C3A4():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C3A4)

    def lambda_C3BD():
        OP_9D(0xFE, 0x19960, 0x0, 0x640, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C3BD)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)

    ChrTalk(
        0x8,
        "#4200473V#1P*cough*... *cough* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#4200474V#5P#40WI refuse...to believe this crap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4200475V#5P#40WGambling should be a piece of cake\x01",
            "after using that stuff...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(100200, 1000, -1500, 2000)
    SetCameraDistance(23500, 2000)
    Sound(103, 0, 100, 0)

    def lambda_C4B8():
        OP_96(0xFE, 0x18894, 0x0, 0xFFFFF63C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C4B8)

    def lambda_C4D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C4D2)
    Sleep(200)

    def lambda_C4E6():
        OP_96(0xFE, 0x18380, 0x0, 0xFFFFF510, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C4E6)

    def lambda_C500():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_C500)
    Sleep(450)
    BeginChrThread(0x104, 3, 0, 25)
    Sleep(450)
    BeginChrThread(0x103, 3, 0, 24)
    Sleep(450)

    def lambda_C526():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEFFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C526)

    def lambda_C540():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C540)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(200)

    def lambda_C58A():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEAE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_C58A)

    def lambda_C5A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13D, 2, lambda_C5A4)
    Sleep(800)
    OP_6F(0x11)

    ChrTalk(
        0x12,
        "#4200476V#6PGantz?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200477V#0013F#12PLook out!\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0x0, 0x2BC)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x13,
        "#4200478V#11P#4STHERE'S NO WAY IN HELL I COULD LOSE!\x02",
    )

    CloseMessageWindow()
    OP_68(101350, 1000, 3170, 1500)
    MoveCamera(45, 19, 0, 1500)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 27)
    Sleep(300)

    def lambda_C678():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C678)
    Sleep(50)

    def lambda_C695():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C695)
    Sleep(50)

    def lambda_C6B2():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C6B2)
    Sleep(50)

    def lambda_C6CF():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_C6CF)

    def lambda_C6E9():
        OP_96(0xFE, 0x18A88, 0x0, 0xA28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C6E9)
    WaitChrThread(0x13, 1)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x103, 1)

    def lambda_C719():
        TurnDirection(0xFE, 0x13, 700)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C719)
    OP_6F(0x41)
    Sleep(300)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    def lambda_C742():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C742)

    ChrTalk(
        0x13,
        (
            "#4200479V#4S#11PAAAAAARGH! LET GO OF ME! LET GO OF\x01",
            "ME, DAMN IT!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 2)

    ChrTalk(
        0x101,
        (
            "#4200480V#0007FYou have to calm down, Gantz!\x02\x03",
            "#4200481V#0010F(What's with this insane strength?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4200482V#6PStop this madness, Gantz!\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#4200483V#5P#3505FWell, if it isn't my favorite pals.\x02\x03",
            "#4200484V#3509FHow's it hanging?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#4200485V#12P#0106F*sigh* I don't know what I was expecting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200486V#6P#0211F#NHow can one man be so suspicious?\x01",
            "It is unfathomable.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x13D,
        (
            "#4200487V#12P#2102FQuite the class clown we got here.\x01",
            "An acquaintance of yours, guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200488V#0306FSorta? Not like we know squat about\x01",
            "him, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        (
            "#4200489V#0305FWhoa, hold the phone! A five of a kind\x01",
            "versus a straight flush?!\x02\x03",
            "#4200490V#0307FWhat the hell even happened here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#4200491V#5P#3510FIt was a real nail-biter, Randy.\x02\x03",
            "#4200492V#3504FI was on the verge of losing everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200493V#12P#0111FI can barely keep up with this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200494V#6P#0206FAt least we were able to neutralize\x01",
            "the threat before anyone was hurt.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    def lambda_CC04():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_CC04)

    ChrTalk(
        0x13,
        "#4200495V#11P#5SLET ME GO, DAMN IT! LET ME GO!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13,
        "#4200496V#11P#4SI CAN'T LOSE! I CAN'T LOSE!!!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After further protest and shouting, Gantz became\x01",
            "overwhelmingly exhausted and passed out.\x02\x03",
            "Due to his condition, the Special Support Section\x01",
            "decided to carry him to his hotel room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0450", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_B39F end

    def Function_24_CD99(): pass

    label("Function_24_CD99")


    def lambda_CD9E():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CD9E)

    def lambda_CDB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CDB8)
    WaitChrThread(0x103, 1)

    def lambda_CDCD():
        OP_95(0xFE, 98700, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CDCD)
    WaitChrThread(0x103, 1)

    def lambda_CDEB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CDEB)
    Return()

    # Function_24_CD99 end

    def Function_25_CDF4(): pass

    label("Function_25_CDF4")


    def lambda_CDF9():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CDF9)

    def lambda_CE13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CE13)
    WaitChrThread(0x104, 1)

    def lambda_CE28():
        OP_95(0xFE, 101100, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CE28)
    WaitChrThread(0x104, 1)

    def lambda_CE46():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CE46)
    Return()

    # Function_25_CDF4 end

    def Function_26_CE4F(): pass

    label("Function_26_CE4F")


    def lambda_CE54():
        OP_95(0xFE, 101600, 0, 2600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CE54)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x13, 700)
    Return()

    # Function_26_CE4F end

    def Function_27_CE75(): pass

    label("Function_27_CE75")


    def lambda_CE7A():
        OP_95(0xFE, 100400, 0, 2600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CE7A)
    WaitChrThread(0x12, 1)
    TurnDirection(0x12, 0x13, 700)
    Return()

    # Function_27_CE75 end

    def Function_28_CE9B(): pass

    label("Function_28_CE9B")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(500)
    OP_68(4030, -100, 7770, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21440, 0)
    SetChrPos(0x101, 2140, -1000, 8000, 90)
    SetChrPos(0x102, 3160, -1000, 6510, 90)
    SetChrPos(0x103, 1840, -1000, 6510, 90)
    SetChrPos(0x104, 3560, -1000, 8000, 90)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_0D()

    ChrTalk(
        0x9,
        "#11PWelcome to Barca Casino!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POh! Hiya, Randy. Welcome back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FYo, Cherry. Would you be a doll and\x01",
            "answer a quick question?\x02\x03",
            "You have a Mishy plush you\x01",
            "give out here as a prize, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYep! It's our cheapest prize! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBut since Mishy is so popular, they tend to\x01",
            "disappear pretty quickly... Maybe I should\x01",
            "put everything on display sometime today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWow, though. Never would have expected\x01",
            "YOU to be interested, Randy. Aren't they\x01",
            "just so...cute?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0309FHahaha! I knew it!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    def lambda_D140():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D140)

    def lambda_D14D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D14D)
    Sleep(500)

    ChrTalk(
        0x104,
        "#5P#0300FSee? Told ya guys I wasn't yankin' your chains.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0100FI suppose you're right...this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FLloyd, our client is in a dire situation.\x02\x03",
            "#0201FIt is our duty to retrieve the target.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 300)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0000FYeah, you have a point.\x02\x03",
            "#0003F(Is it just me...or have Tio's eyes been\x01",
            "sparkling ever since Mishy was first\x01",
            "mentioned?)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2820, -1000, 7050, 90)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetScenarioFlags(0x70, 3)
    OP_29(0xC, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_28_CE9B end

    def Function_29_D2ED(): pass

    label("Function_29_D2ED")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#0001FSince we're already here, we should try and\x01",
            "gather some information on Gantz.\x02\x03",
            "I figure some of the employees or other\x01",
            "customers might know a thing or two.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, -5000, 0)
    EventEnd(0x4)
    Return()

    # Function_29_D2ED end

    SaveToFile()

Try(main)
