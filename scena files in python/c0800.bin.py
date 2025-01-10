from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0800.bin",                # FileName
        "c0800",                    # MapName
        "c0800",                    # Location
        0x0003,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 3, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0800",                  # 0
        "Guardsman Romeo",        # 1
        "Passenger",              # 2
        "Passenger",              # 3
        "Passenger",              # 4
        "Inspection Officer Quattro",# 5
        "Old Man",                # 6
        "Old Lady",               # 7
        "Passenger",              # 8
        "Passenger",              # 9
        "Passenger",              # 10
        "Passenger",              # 11
        "Passenger",              # 12
        "Passenger",              # 13
        "Passenger",              # 14
        "Attendant",              # 15
        "Attendant",              # 16
        "Passenger",              # 17
        "列車",                   # 18
        "Representative Campbell",# 19
        "Carla",                  # 20
        "Marsha",                 # 21
        "SE制御",                 # 22
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch20302.itc",                   # 01
        "chr/ch24400.itc",                   # 02
        "chr/ch20802.itc",                   # 03
        "chr/ch28500.itc",                   # 04
    ))

    DeclNpc(-1500,   0,       -18530,  0,    385,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(43000,   100,     -17200,  180,  453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(49700,   0,       -14050,  0,    385,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(15000,   100,     -17200,  180,  453,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(7500,    0,       -12500,  270,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 33,  58.0,                  -16.0,                 0.0,                   17.015625,             [0.3333333134651184,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3636363446712494,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -19.333332061767578,   5.81818151473999,      -0.0,                  1.0])

    DeclActor(24500,   0,       0,       2000,    24500,   1500,    0,       0x007C, 0,  34, 0x0000)
    DeclActor(24500,   0,       -16000,  2000,    24500,   1500,    -16000,  0x007C, 0,  34, 0x0000)
    DeclActor(18000,   0,       0,       2000,    17500,   1500,    0,       0x007C, 0,  35, 0x0000)
    DeclActor(18000,   0,       -16000,  2000,    17500,   1500,    -16000,  0x007C, 0,  35, 0x0000)

    ScpFunction((
        "Function_0_498",          # 00, 0
        "Function_1_550",          # 01, 1
        "Function_2_623",          # 02, 2
        "Function_3_6E3",          # 03, 3
        "Function_4_9F5",          # 04, 4
        "Function_5_CEC",          # 05, 5
        "Function_6_E11",          # 06, 6
        "Function_7_105E",         # 07, 7
        "Function_8_109B",         # 08, 8
        "Function_9_11BC",         # 09, 9
        "Function_10_1A0A",        # 0A, 10
        "Function_11_1C03",        # 0B, 11
        "Function_12_1D50",        # 0C, 12
        "Function_13_20AE",        # 0D, 13
        "Function_14_20D7",        # 0E, 14
        "Function_15_214C",        # 0F, 15
        "Function_16_2F67",        # 10, 16
        "Function_17_2FBC",        # 11, 17
        "Function_18_34F9",        # 12, 18
        "Function_19_353D",        # 13, 19
        "Function_20_3611",        # 14, 20
        "Function_21_3670",        # 15, 21
        "Function_22_36CF",        # 16, 22
        "Function_23_372E",        # 17, 23
        "Function_24_378D",        # 18, 24
        "Function_25_3C92",        # 19, 25
        "Function_26_3CD4",        # 1A, 26
        "Function_27_3D31",        # 1B, 27
        "Function_28_3D48",        # 1C, 28
        "Function_29_41EC",        # 1D, 29
        "Function_30_520C",        # 1E, 30
        "Function_31_5235",        # 1F, 31
        "Function_32_5256",        # 20, 32
        "Function_33_5E26",        # 21, 33
        "Function_34_5FB5",        # 22, 34
        "Function_35_5FF7",        # 23, 35
        "Function_36_6039",        # 24, 36
        "Function_37_6084",        # 25, 37
    ))


    def Function_0_498(): pass

    label("Function_0_498")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4D8"),
        (1, "loc_4E4"),
        (2, "loc_4F0"),
        (3, "loc_4FC"),
        (4, "loc_508"),
        (5, "loc_514"),
        (6, "loc_520"),
        (SWITCH_DEFAULT, "loc_52C"),
    )


    label("loc_4D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_4E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_4F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_4FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_508")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_514")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_520")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_52C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_538")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_538")

    label("loc_54F")

    Return()

    # Function_0_498 end

    def Function_1_550(): pass

    label("Function_1_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_564")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 17)
    Jump("loc_5C6")

    label("loc_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_578")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 8)
    Jump("loc_5C6")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_58C")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 15)
    Jump("loc_5C6")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_5A6")
    ClearScenarioFlags(0x5C, 3)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Event(0, 28)
    Jump("loc_5C6")

    label("loc_5A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C6")
    Event(0, 24)

    label("loc_5C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1")
    Jump("loc_5E6")

    label("loc_5E1")

    ClearChrFlags(0x8, 0x80)

    label("loc_5E6")

    Jump("loc_622")

    label("loc_5EB")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_610")
    Jump("loc_622")

    label("loc_610")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_622")
    ClearChrFlags(0xC, 0x80)

    label("loc_622")

    Return()

    # Function_1_550 end

    def Function_2_623(): pass

    label("Function_2_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_635")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_635")

    SetMapObjFlags(0x1, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_680")
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)

    label("loc_680")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CB")
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6DC")
    OP_24(0x323)
    Jump("loc_6E2")

    label("loc_6DC")

    Sound(803, 1, 100, 0)

    label("loc_6E2")

    Return()

    # Function_2_623 end

    def Function_3_6E3(): pass

    label("Function_3_6E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_701")
    Jump("loc_7B8")

    label("loc_701")


    ChrTalk(
        0xFE,
        (
            "Hey there. Did you just get back\x01",
            "from Calvard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd also really like to take a trip\x01",
            "out there some day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(I wasn't exactly out there having\x01",
            "the time of my life...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B8")

    Jump("loc_9F1")

    label("loc_7BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_967")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CA")

    ChrTalk(
        0xFE,
        (
            "Freight transports with supplies for the\x01",
            "CGF depart from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our latest departure is headed towards\x01",
            "Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because us folks in the CGF can't just\x01",
            "provide security and call it a day,\x01",
            "our lives aren't the easiest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_962")

    label("loc_8CA")


    ChrTalk(
        0xFE,
        (
            "The train headed towards the gate is\x01",
            "transporting supplies for the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Platform 3 is exclusively for freight trains,\x01",
            "so entry is prohibited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_962")

    Jump("loc_9F1")

    label("loc_967")


    ChrTalk(
        0xFE,
        (
            "Looks like the inspection of the train\x01",
            "departing for Erebonia is complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Think it's about time I head back\x01",
            "to Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F1")

    TalkEnd(0xFE)
    Return()

    # Function_3_6E3 end

    def Function_4_9F5(): pass

    label("Function_4_9F5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A89")
    Jump("loc_AD3")

    label("loc_A89")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD3")

    label("loc_AA9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD3")

    label("loc_AC9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1C")

    ChrTalk(
        0xFE,
        (
            "They typically don't inspect any passengers\x01",
            "inbound to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're more concerned with anybody headed\x01",
            "out to Erebonia or Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a consequence, smugglers and\x01",
            "illegal immigrants are especially fond\x01",
            "of traveling into Crossbell by train.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CA0")

    label("loc_C1C")


    ChrTalk(
        0xFE,
        (
            "Trains are unsurprisingly popular with\x01",
            "smugglers and illegal immigrants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But hey, it's not my problem, so what do I care?\x02",
    )

    CloseMessageWindow()

    label("loc_CA0")

    Jump("loc_CE4")

    label("loc_CA5")


    ChrTalk(
        0xFE,
        (
            "Anyway, break's just about over.\x01",
            "Better get back to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_9F5 end

    def Function_5_CEC(): pass

    label("Function_5_CEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D77")

    ChrTalk(
        0xFE,
        (
            "A friend of mine is going to Erebonia,\x01",
            "so I came to see him off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What time is his train supposed to depart?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E0D")

    label("loc_D77")


    ChrTalk(
        0xFE,
        "Hmm... Why hasn't it left?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanted to see him off properly, but\x01",
            "from the looks of it, I'll have to throw\x01",
            "him a welcome-back party instead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0D")

    TalkEnd(0xFE)
    Return()

    # Function_5_CEC end

    def Function_6_E11(): pass

    label("Function_6_E11")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EA5")
    Jump("loc_EEF")

    label("loc_EA5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EC5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EEF")

    label("loc_EC5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EE5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EEF")

    label("loc_EE5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EEF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F99")

    ChrTalk(
        0xFE,
        (
            "A good friend of mine is coming in\x01",
            "on the next train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's been what, 10 years? I'm getting nostalgic...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1056")

    label("loc_F99")


    ChrTalk(
        0xFE,
        (
            "The inspection team showed up, so here's\x01",
            "to hoping the train leaves soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because in case you weren't aware,\x01",
            "the outbound train has to depart before\x01",
            "the inbound train can arrive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1056")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_E11 end

    def Function_7_105E(): pass

    label("Function_7_105E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1072")
    Jump("loc_1097")

    label("loc_1072")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1087")
    Call(0, 10)
    Jump("loc_1097")

    label("loc_1087")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_1097")
    Call(0, 9)

    label("loc_1097")

    TalkEnd(0xFE)
    Return()

    # Function_7_105E end

    def Function_8_109B(): pass

    label("Function_8_109B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(452)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 7000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(61500, 2500, -10500, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(16000, 0)
    OP_EE(0x0, 0x1)
    OP_68(58500, 2500, -11500, 5000)
    MoveCamera(45, 20, 0, 5000)
    SetCameraDistance(24000, 5000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x19, 3, 0, 18)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(5500, 3300, -8000, 0)
    MoveCamera(48, -15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(14000, 0)
    OP_68(5500, 2300, -8000, 4000)
    OP_0D()
    WaitChrThread(0x19, 3)
    OP_6F(0x1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_109B end

    def Function_9_11BC(): pass

    label("Function_9_11BC")

    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(5270, 1500, -12980, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17840, 0)
    SetChrPos(0x101, 5500, 0, -13000, 90)
    SetChrPos(0x102, 5250, 0, -12000, 90)
    SetChrPos(0x103, 4000, 0, -13000, 90)
    SetChrPos(0x104, 3700, 0, -12000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()

    ChrTalk(
        0xFE,
        (
            "#11PAllow me to briefly explain the\x01",
            "specifics of the task at hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FPlease do. We're all ears.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#11PI will be assigning each of you a car\x01",
            "to inspect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#11PYou will speak to every passenger,\x01",
            "inspect their luggage, and verify\x01",
            "the validity of their entry application.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#11PAny passengers found carrying an invalid\x01",
            "entry application or dangerous goods are\x01",
            "to be apprehended immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0003FOkay. Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FI'm cool with conductin' an inspection...\x02\x03",
            "#0301F...but what do we do when passengers\x01",
            "ain't in their seats during the check?\x02\x03",
            "#0306FI dunno, but I feel like a bunch of amateurs\x01",
            "like ourselves might not be able to\x01",
            "cover everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#11PRight. Please exercise caution in that regard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#11PPassengers will be notified that they are to\x01",
            "remain in their seats for the duration of\x01",
            "the inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#11PThe occasional trickster may try to cause a ruckus\x01",
            "in the hopes that we overlook small details during\x01",
            "the inspection, so don't get caught off guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FYou are certainly strict.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FAll right, I think I've got the idea now.\x02\x03",
            "#0003FAlthough... I'm a little bothered that each\x01",
            "person has to inspect their own car.\x02\x03",
            "#0000FRandy and I will definitely be fine on our own,\x01",
            "but what about Elie and Tio?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_177B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_177B)

    def lambda_1788():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1788)

    def lambda_1795():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1795)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        (
            "#5P#0105FReally? This is the moment you decide\x01",
            "to start worrying about us?\x02\x03",
            "#0104FI'm also an officer, so I'm familiar\x01",
            "with the basics of martial arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FLikewise.\x02\x03",
            "#0200FI will not allow anybody throwing a fit\x01",
            "to overpower me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0309FWay to patronize 'em, Lloyd. They ain't\x01",
            "a bunch of weaklings.\x02\x03",
            "Hopefully, this is a lesson learned.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#12P#0003FY-Yeah, I guess that was uncalled for.\x02",
    )

    CloseMessageWindow()

    def lambda_1952():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1952)

    def lambda_195F():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_195F)

    def lambda_196C():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_196C)

    def lambda_1979():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1979)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0xC,
        (
            "With that said... Are you all ready\x01",
            "to commence the inspection?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0x2)
    Call(0, 11)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F6")
    Call(0, 12)
    Jump("loc_1A09")

    label("loc_19F6")

    SetChrPos(0x0, 5000, 0, -13500, 90)
    EventEnd(0x5)

    label("loc_1A09")

    Return()

    # Function_9_11BC end

    def Function_10_1A0A(): pass

    label("Function_10_1A0A")

    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(5270, 1500, -12980, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17840, 0)
    SetChrPos(0x101, 5500, 0, -13000, 90)
    SetChrPos(0x102, 5250, 0, -12000, 90)
    SetChrPos(0x103, 4000, 0, -13000, 90)
    SetChrPos(0x104, 3700, 0, -12000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#11PYou will now split up and begin\x01",
            "inspecting your respective cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI would like you to confirm the validity\x01",
            "of the entry application for every\x01",
            "passenger and inspect their luggage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWith that said... Are you all ready\x01",
            "to commence the inspection?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BEF")
    Call(0, 12)
    Jump("loc_1C02")

    label("loc_1BEF")

    SetChrPos(0x0, 5000, 0, -13500, 90)
    EventEnd(0x5)

    label("loc_1C02")

    Return()

    # Function_10_1A0A end

    def Function_11_1C03(): pass

    label("Function_11_1C03")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D4F")

    ChrTalk(
        0x101,
        "#6P#0006FI still need some time to mentally prepare myself...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI suppose it's only natural. There is no\x01",
            "room for error in this task, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHowever, note that the train cannot wait\x01",
            "much longer for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PPlease return as soon as possible.\x02",
    )

    CloseMessageWindow()

    label("loc_1D4F")

    Return()

    # Function_11_1C03 end

    def Function_12_1D50(): pass

    label("Function_12_1D50")


    ChrTalk(
        0x101,
        "#6P#0000FYes. Understood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAhem!\x01",
            "Good. You are ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PVery well. Without further ado,\x01",
            "let's begin the inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI'll inspect the first car, so please\x01",
            "divide the remaining cars among\x01",
            "yourselves.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E38():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E38)
    Sleep(300)

    def lambda_1E48():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E48)

    def lambda_1E55():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E55)

    def lambda_1E62():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E62)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#12P#0000FIn that case... I'll take the second car.\x02\x03",
            "Elie, Tio, and Randy, take the following\x01",
            "three cars in that exact order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0300FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0100FSee you later, then.\x02",
    )

    CloseMessageWindow()

    def lambda_1F54():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F54)

    def lambda_1F61():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F61)

    def lambda_1F6E():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F6E)

    def lambda_1F7B():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F7B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0xC,
        (
            "#11PLet me remind you that this task\x01",
            "will require your full attention.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 1, 0, 13)
    Sleep(500)
    BeginChrThread(0x101, 1, 0, 14)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#6P#0001FAll right. I've got a train to inspect!\x02",
    )

    CloseMessageWindow()
    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)

    def lambda_2046():
        OP_97(0x101, 0x12C, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2046)
    BeginChrThread(0x1D, 0, 0, 36)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    StopBGM(0x7D0)
    WaitBGM()
    EndChrThread(0x1D, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1D50 end

    def Function_13_20AE(): pass

    label("Function_13_20AE")

    OP_97(0xC, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_97(0xC, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_20AE end

    def Function_14_20D7(): pass

    label("Function_14_20D7")


    def lambda_20DC():
        OP_97(0x102, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20DC)
    Sleep(300)
    OP_97(0x103, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_210D():
        OP_97(0x103, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_210D)
    Sleep(400)

    def lambda_212A():
        OP_97(0x104, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_212A)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Return()

    # Function_14_20D7 end

    def Function_15_214C(): pass

    label("Function_15_214C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(5270, 1500, -12980, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17840, 0)
    SetChrPos(0x101, 5500, 0, -13000, 90)
    SetChrPos(0x102, 5250, 0, -12000, 90)
    SetChrPos(0x103, 4000, 0, -13000, 90)
    SetChrPos(0x104, 3700, 0, -12000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_299D")
    OP_2C(0x9, 0x2)

    ChrTalk(
        0xC,
        "#11PThis man has falsified his immigration papers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FF-Falsified? How so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FHas he fabricated his entire work history?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PCorrect. He's a former swindler from Calvard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThis guy likes to bounce around. I've had a\x01",
            "run-in with him before, when he tried to conceal\x01",
            "his criminal record on this same application.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThis marks the second time I've caught him.\x01",
            "Man, this moron will never learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0301FA former swindler, eh? Wonder what\x01",
            "brings him to good ol' Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PNow that his prison sentence in Calvard is up,\x01",
            "it looks like he's trying to lead an honest life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThe scale of his fraudulent behavior was fairly\x01",
            "small, so he apparently wasn't given a heavy\x01",
            "sentence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0103FIt's unfortunate, though. A criminal record\x01",
            "will follow someone for the rest of their lives...\x02\x03",
            "#0108FIf your immigration papers show you have\x01",
            "a criminal record, your ability to travel is\x01",
            "heavily restricted. I can't imagine he likes it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P'If only I hadn't gone and committed fraud...'\x01",
            "I'm sure he regrets his crimes, but\x01",
            "he chose this life by breaking the law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PCommitting crimes will burden you for the rest of\x01",
            "your life, and the world would be a better place if\x01",
            "more people understood that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001FSo what's going to happen to this man?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PI've detained him in my office for the time being.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI'll give him a stern warning, and then ship him\x01",
            "back off to Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PIt's nothing out of the ordinary for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0003FYeah, I guess there's no other choice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAt any rate, we've successfully completed\x01",
            "our inspection without incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWe're a bit behind schedule, so we\x01",
            "shouldn't delay this train any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI believe I owe the Special Support Section\x01",
            "a proper thank you, don't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PI'll be sure to give you a ring next time I need help.\x02",
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0xC)
    Jump("loc_2A95")

    label("loc_299D")


    ChrTalk(
        0xC,
        (
            "#11PWe've successfully completed the inspection\x01",
            "without incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThanks to you, it looks like we'll be able to\x01",
            "send this train on its way on schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI believe I owe the Special Support Section\x01",
            "a proper thank you, don't I?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A95")


    ChrTalk(
        0x101,
        (
            "#6P#0000FWe appreciate it. You've taught us a lot\x01",
            "during this request.\x02\x03",
            "Feel free to give us a call if you ever\x01",
            "need our help again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PI think I'll take you up on that offer.\x02",
    )

    CloseMessageWindow()
    OP_68(5080, 1000, -12450, 5000)
    MoveCamera(26, 13, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(17840, 5000)
    BeginChrThread(0xC, 1, 0, 13)
    BeginChrThread(0x101, 1, 0, 16)
    WaitChrThread(0xC, 1)
    EndChrThread(0x101, 0x1)

    def lambda_2B97():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B97)

    def lambda_2BA4():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BA4)

    def lambda_2BB1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BB1)

    def lambda_2BBE():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BBE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#12P#0006FPhew... That was a lot harder than\x01",
            "I was anticipating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FYou can say that again...\x02\x03",
            "#0106FThough Tio is probably the most\x01",
            "exhausted among us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0005FWhy do you say that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0309FPeople thought she was some kinda\x01",
            "station mascot and kept smothering her.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#12P#0005FS-Station mascot?\x01",
            "Are you all right, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FD-Don't tell me you're so traumatized\x01",
            "that you can no longer speak!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0206FN-No, not quite. I am experiencing\x01",
            "some mental fatigue. I should recover\x01",
            "in a bit...\x02\x03",
            "#0200FCan we leave, please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FY-Yeah, sure. I hope you aren't\x01",
            "straining yourself too hard, Tio.\x02",
        )
    )

    CloseMessageWindow()
    Sound(9, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Inspection Assistance Wanted]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 5000, 0, -13500, 90)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_29(0x9, 0x1, 0xD)
    OP_29(0x9, 0x4, 0x10)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_15_214C end

    def Function_16_2F67(): pass

    label("Function_16_2F67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FBB")

    def lambda_2F77():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F77)

    def lambda_2F84():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F84)

    def lambda_2F91():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2F91)

    def lambda_2F9E():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2F9E)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    Jump("Function_16_2F67")

    label("loc_2FBB")

    Return()

    # Function_16_2F67 end

    def Function_17_2FBC(): pass

    label("Function_17_2FBC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(452)
    LoadChrToIndex("chr/ch20800.itc", 0x1E)
    LoadChrToIndex("chr/ch20900.itc", 0x1F)
    LoadChrToIndex("chr/ch20000.itc", 0x20)
    LoadChrToIndex("chr/ch20400.itc", 0x21)
    LoadChrToIndex("chr/ch20700.itc", 0x22)
    LoadChrToIndex("chr/ch28300.itc", 0x23)
    LoadChrToIndex("chr/ch20200.itc", 0x24)
    LoadChrToIndex("chr/ch20500.itc", 0x25)
    LoadChrToIndex("chr/ch28400.itc", 0x26)
    LoadChrToIndex("chr/ch21802.itc", 0x27)
    LoadChrToIndex("apl/ch50003.itc", 0x28)
    OP_68(17500, 3800, -200, 0)
    MoveCamera(58, 1, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(17000, 0)
    OP_EE(0x0, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 15700, 0, -9700, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 15700, 0, -9700, 180)
    SetChrPos(0xE, 15700, 0, -9700, 180)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 3000, 0, -2600, 90)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 20000, 0, 2200, 270)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x2)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 19500, 100, -1300, 180)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3000, 0, 3300, 90)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 20000, 0, -30000, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 52500, 0, -13300, 45)
    SetChrChipByIndex(0x18, 0x27)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 32800, 100, -14600, 0)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 7000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_E5()
    ClearChrFlags(0xF, 0x80)

    def lambda_320D():
        OP_95(0xFE, 40000, 0, -2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_320D)
    ClearChrFlags(0x10, 0x80)

    def lambda_322C():
        OP_95(0xFE, 8000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_322C)
    ClearChrFlags(0x13, 0x80)
    OP_68(17500, 1800, -200, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    ClearChrFlags(0x14, 0x80)

    def lambda_326B():
        OP_95(0xFE, 34000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_326B)
    OP_6F(0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(1000)
    OP_68(27000, 1500, -15000, 0)
    MoveCamera(54, 5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(28000, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)

    def lambda_32DC():
        OP_95(0xFE, 12000, 0, -30000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_32DC)
    MoveCamera(60, 5, 0, 8000)
    SetCameraDistance(38000, 8000)
    WaitChrThread(0x16, 1)
    PlaceName2(340, 200, "c_plac00", 0x0, 0)
    Sleep(2000)

    def lambda_3322():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3322)
    WaitChrThread(0x16, 2)
    Sleep(500)

    def lambda_3336():
        OP_95(0xFE, 22000, 0, -30000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3336)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(1000)
    Fade(500)
    OP_68(57000, 1500, -8500, 0)
    OP_6E(780, 0)
    SetCameraDistance(21000, 0)
    MoveCamera(53, 2, 0, 0)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_68(10000, 500, -8500, 10000)
    MoveCamera(57, 12, 0, 10000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x19, 3, 0, 18)
    WaitChrThread(0x19, 3)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_68(18400, -900, -4400, 0)
    MoveCamera(54, 10, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(30500, 0)
    SetCameraDistance(33500, 20000)
    Sleep(1000)
    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x11, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xF, 3, 0, 22)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 20)
    Sleep(2200)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 23)
    BeginChrThread(0xD, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0xE, 3, 0, 21)
    Sleep(8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    OP_EE(0x0, 0xA)
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2FBC end

    def Function_18_34F9(): pass

    label("Function_18_34F9")

    Sound(452, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x168, 0x0, 0x0)
    Sleep(2000)

    def lambda_3517():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3517)
    OP_79(0x1)
    Sound(143, 0, 100, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_18_34F9 end

    def Function_19_353D(): pass

    label("Function_19_353D")


    def lambda_3542():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x2260, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3542)
    Sleep(2000)

    def lambda_355F():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_355F)
    Sleep(1000)

    def lambda_356F():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x1E78, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_356F)
    Sleep(2000)

    def lambda_358C():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x1A90, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_358C)
    Sleep(2000)

    def lambda_35A9():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x16A8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_35A9)
    Sleep(2000)

    def lambda_35C6():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0x12C0, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_35C6)
    Sleep(1500)

    def lambda_35E3():
        OP_96(0xFE, 0x1B58, 0xFFFFF9F2, 0xFFFFE05C, 0xED8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_35E3)
    WaitChrThread(0x19, 1)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_19_353D end

    def Function_20_3611(): pass

    label("Function_20_3611")

    SetChrPos(0xFE, 6000, 0, -9700, 180)

    def lambda_3627():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3627)

    def lambda_3638():
        OP_95(0xFE, 6000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3638)
    WaitChrThread(0xFE, 1)

    def lambda_3656():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3656)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_3611 end

    def Function_21_3670(): pass

    label("Function_21_3670")

    SetChrPos(0xFE, 15700, 0, -9700, 180)

    def lambda_3686():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3686)

    def lambda_3697():
        OP_95(0xFE, 15700, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3697)
    WaitChrThread(0xFE, 1)

    def lambda_36B5():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36B5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_3670 end

    def Function_22_36CF(): pass

    label("Function_22_36CF")

    SetChrPos(0xFE, 18700, 0, -9700, 180)

    def lambda_36E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36E5)

    def lambda_36F6():
        OP_95(0xFE, 18700, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36F6)
    WaitChrThread(0xFE, 1)

    def lambda_3714():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3714)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_36CF end

    def Function_23_372E(): pass

    label("Function_23_372E")

    SetChrPos(0xFE, 28400, 0, -9700, 180)

    def lambda_3744():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3744)

    def lambda_3755():
        OP_95(0xFE, 28400, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3755)
    WaitChrThread(0xFE, 1)

    def lambda_3773():
        OP_95(0xFE, -5000, 0, -12800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3773)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_372E end

    def Function_24_378D(): pass

    label("Function_24_378D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(453)
    SoundLoad(805)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x0, 0x19)
    OP_49()
    SetChrPos(0x19, 55000, -1550, 8000, 0)
    OP_D3(0x19, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_70(0x0, 0x1E)
    OP_68(-22350, 3240, -810, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -21570, 600, 190, 90)
    SetChrPos(0x102, -21570, 600, -1220, 90)
    SetChrPos(0x103, -22700, 600, -1220, 90)
    SetChrPos(0x104, -22700, 600, 190, 90)
    OP_68(-14120, 2100, 690, 2000)

    def lambda_3865():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3865)

    def lambda_387A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_387A)

    def lambda_388F():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_388F)

    def lambda_38A4():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_38A4)
    StopBGM(0x1388)
    Sound(805, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x3, 1)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Attendant's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Platform 1: The train bound for the\x01",
            "Republic is now departing.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you are not boarding the train, then please\x01",
            "step back to the center of the platform.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_39EA():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_39EA)

    def lambda_39F7():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_39F7)

    def lambda_3A04():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3A04)

    def lambda_3A11():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3A11)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5P#0305FYo, hold up... Isn't that the train the\x01",
            "representative's daughter is ridin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FIt looks like we still have a bit of time,\x01",
            "so let's board!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3B0E():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3B0E)

    def lambda_3B1B():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3B1B)

    def lambda_3B28():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3B28)

    def lambda_3B35():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3B35)
    WaitChrThread(0x3, 1)
    BeginChrThread(0x19, 3, 0, 25)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(150)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(250)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(150)
    BeginChrThread(0x103, 3, 0, 26)
    Sleep(2000)
    BeginChrThread(0x1D, 0, 0, 37)
    Sleep(3000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x104, 3)
    EndChrThread(0x1D, 0x0)
    Sound(454, 0, 100, 0)
    OP_71(0x0, 0x14, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sound(143, 0, 100, 0)
    OP_82(0x64, 0x32, 0xBB8, 0x1F4)
    Sleep(800)
    Fade(500)
    OP_68(5700, 1500, 4200, 0)
    MoveCamera(58, 1, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(17000, 0)
    OP_EE(0x0, 0x1)
    OP_0D()
    BeginChrThread(0x19, 1, 0, 27)
    OP_68(61700, 1500, 4200, 9000)
    Sleep(8000)
    BeginChrThread(0x1D, 0, 0, 36)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x1D, 0x0)
    OP_EE(0x0, 0xA)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x325)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0040", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_378D end

    def Function_25_3C92(): pass

    label("Function_25_3C92")

    OP_68(-9530, 2100, -200, 2000)
    OP_6F(0x1)
    OP_68(700, 1500, 4200, 1500)
    MoveCamera(44, 13, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(18000, 1500)
    Return()

    # Function_25_3C92 end

    def Function_26_3CD4(): pass

    label("Function_26_3CD4")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x1)
    OP_95(0xFE, -1000, 0, 3000, 5000, 0x1)

    def lambda_3CFC():
        OP_95(0xFE, -1000, 0, 7000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CFC)
    Sleep(400)

    def lambda_3D19():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D19)
    OP_64(0xFE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_3CD4 end

    def Function_27_3D31(): pass

    label("Function_27_3D31")

    Sound(453, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x169, 0x294, 0x0, 0x0)
    Return()

    # Function_27_3D31 end

    def Function_28_3D48(): pass

    label("Function_28_3D48")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(452)
    LoadChrToIndex("chr/ch20800.itc", 0x1E)
    LoadChrToIndex("chr/ch20900.itc", 0x1F)
    LoadChrToIndex("chr/ch20000.itc", 0x20)
    LoadChrToIndex("chr/ch20400.itc", 0x21)
    LoadChrToIndex("chr/ch20700.itc", 0x22)
    LoadChrToIndex("chr/ch28300.itc", 0x23)
    LoadChrToIndex("chr/ch20200.itc", 0x24)
    LoadChrToIndex("chr/ch20500.itc", 0x25)
    LoadChrToIndex("chr/ch28400.itc", 0x26)
    LoadChrToIndex("chr/ch21802.itc", 0x27)
    LoadChrToIndex("chr/ch27700.itc", 0x28)
    LoadChrToIndex("chr/ch33200.itc", 0x29)
    LoadChrToIndex("chr/ch34500.itc", 0x2A)
    LoadChrToIndex("apl/ch50111.itc", 0x2B)
    SoundLoad(803)
    OP_68(17500, 3800, -200, 0)
    MoveCamera(58, 1, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(17000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x0, 15700, 0, -9700, 180)
    SetChrPos(0x1, 15700, 0, -9700, 180)
    SetChrPos(0x2, 15700, 0, -9700, 180)
    SetChrPos(0x3, 15700, 0, -9700, 180)
    SetChrPos(0x1B, 15700, 0, -9700, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x29)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x12, 0x2)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3000, 0, 3300, 90)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 3000, 0, -2600, 90)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 20000, 0, 2200, 270)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrChipByIndex(0x13, 0x1)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 19500, 100, -1300, 180)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 20000, 0, -30000, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 52500, 0, -13300, 45)
    SetChrChipByIndex(0x18, 0x27)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 32800, 100, -14600, 0)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 7000, -1550, -8100, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others transferred\x01",
            "in Altair for the return trip.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Then, 30 minutes later...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7103", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 2)
    Sound(803, 2, 100, 0)
    ClearScenarioFlags(0x0, 3)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Sleep(2500)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_68(61500, 2500, -10500, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(16000, 0)
    OP_EE(0x0, 0x1)
    OP_68(58500, 2500, -11500, 5000)
    MoveCamera(45, 20, 0, 5000)
    SetCameraDistance(24000, 5000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x19, 3, 0, 18)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(5500, 3300, -8000, 0)
    MoveCamera(48, -15, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(14000, 0)
    OP_68(5500, 2300, -8000, 4000)
    OP_0D()
    WaitChrThread(0x19, 3)
    OP_6F(0x1)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -2000, -1550, -8100, 0)
    OP_68(18400, -900, -4400, 0)
    MoveCamera(54, 10, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(30500, 0)
    SetCameraDistance(33500, 20000)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_41E8")
    Call(0, 29)
    Jump("loc_41EB")

    label("loc_41E8")

    Call(0, 32)

    label("loc_41EB")

    Return()

    # Function_28_3D48 end

    def Function_29_41EC(): pass

    label("Function_29_41EC")

    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    BeginChrThread(0x11, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xF, 3, 0, 22)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 20)
    Sleep(2200)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 23)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x1B, 3, 0, 21)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x0, 0x2)
    EndChrThread(0x0, 0x3)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1, 0x2)
    EndChrThread(0x1, 0x3)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x2, 0x2)
    EndChrThread(0x2, 0x3)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x3, 0x2)
    EndChrThread(0x3, 0x3)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1B, 0x2)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0xF, 0x1)
    EndChrThread(0xF, 0x2)
    EndChrThread(0xF, 0x3)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x1B, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x101, 4059, 0, -15180, 45)
    SetChrPos(0x102, 4920, 0, -15560, 0)
    SetChrPos(0x103, 3910, 0, -13780, 135)
    SetChrPos(0x104, 4810, 0, -12940, 180)
    SetChrPos(0x1B, 5870, 0, -14030, 270)
    SetChrPos(0xF, 5500, 0, -14560, 270)
    SetChrPos(0x1A, -7130, 600, -15750, 90)
    SetChrPos(0x1C, -9130, 600, -16740, 90)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_68(4760, 1500, -14530, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(12050, 0)
    OP_EE(0x0, 0xA)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#5P#0306FPhew... We're finally back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FWell, various factors delayed our return.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#11PUmm... Sorry for the trouble I've caused.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PI truly thank you for listening to what I\x01",
            "had to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FPlease don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FWho's to say we can't handle consultations?\x01",
            "You can count on the SSS to lend you an\x01",
            "ear whenever you need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#11PTh-Thank you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(200)
    TurnDirection(0x1B, 0x1A, 400)
    Sleep(400)

    ChrTalk(
        0x1B,
        "#11PAh...\x02",
    )

    CloseMessageWindow()
    OP_68(1960, 1500, -15420, 3000)
    MoveCamera(320, 30, 0, 3000)

    def lambda_45F1():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45F1)

    def lambda_45FE():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_45FE)

    def lambda_460B():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_460B)

    def lambda_4618():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4618)

    def lambda_4625():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4625)

    def lambda_463A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_463A)
    Sleep(2500)
    Sleep(800)

    ChrTalk(
        0x1A,
        (
            "#5PHmph. How dare you worry me at\x01",
            "a time like this, you daft girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#12PS-Speak for yourself, Father!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#12PYou couldn't even bother to find me yourself,\x01",
            "so you sent the police in your stead!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 1, 0, 30)
    OP_96(0x1C, 0xFFFFFCD6, 0x0, 0xFFFFBEB0, 0x3E8, 0x0)
    TurnDirection(0x1C, 0x1B, 400)
    Sleep(300)

    ChrTalk(
        0x1C,
        "#5PExcuse me, Lady Carla...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PM-My apologies. I was just so\x01",
            "terribly worried.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xE1, 0x190)
    Sleep(300)

    ChrTalk(
        0x1B,
        "#12PHmph! So you were in on it, too, Marsha?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PF-F-Forgive me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#12PI'm still mad at you, but...thank you, Marsha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#12PWill you return to my side?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PO-Of course. I'd be happy to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#12POh, thank heavens. I think I've\x01",
            "finally made up my mind.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1A, 400)
    Sleep(300)

    ChrTalk(
        0x1B,
        "#12PI have a request, Father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#12PYou must knock every time you wish\x01",
            "to enter my room! Every time, okay?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#12PIn addition, you may no longer intrude\x01",
            "upon my private life!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#12PAnd if you refuse, I'll be hopping back on\x01",
            "the train, and I won't look back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5PHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PFine. You have to stay home and\x01",
            "behave yourself for a while, first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#12PSo, are you honoring my request,\x01",
            "or are you refusing it?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x101, 0)

    ChrTalk(
        0x1A,
        (
            "#5PWell, I don't want to be worried or have\x01",
            "another falling out! I'll accept your terms.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(2670, 1500, -15870, 2000)

    def lambda_4AE8():

        label("loc_4AE8")

        TurnDirection(0xFE, 0x1A, 400)
        Yield()
        Jump("loc_4AE8")

    QueueWorkItem2(0x1B, 1, lambda_4AE8)

    def lambda_4AFA():

        label("loc_4AFA")

        TurnDirection(0xFE, 0x1A, 400)
        Yield()
        Jump("loc_4AFA")

    QueueWorkItem2(0x1C, 1, lambda_4AFA)

    def lambda_4B0C():
        OP_95(0xFE, 2040, 0, -14970, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4B0C)
    Sleep(300)
    OP_96(0x1B, 0x244, 0x0, 0xFFFFC180, 0x3E8, 0x0)
    Sleep(400)

    ChrTalk(
        0x1A,
        (
            "#5PSo THIS is the power of the Something-Or-\x01",
            "Other Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PFor the time being, allow me to thank you\x01",
            "for safely bringing my daughter home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PHowever! Not a word of this incident\x01",
            "is to escape your lips to anyone.\x01",
            "Am I understood?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0300FYes, Your Majesty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FOur lips are sealed, so you can rest easy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#5PFine, then.\x02",
    )

    CloseMessageWindow()
    OP_95(0x1A, -630, 0, -14820, 2000, 0x0)

    ChrTalk(
        0x1A,
        "#5PWe're leaving, Carla!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#12PYou don't need to command me!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1A, 0, 0, 31)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)

    def lambda_4D11():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4D11)

    def lambda_4D1E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_4D1E)
    Sleep(300)

    ChrTalk(
        0x1B,
        (
            "#5PElie, everyone...\x01",
            "Until we meet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PI can't thank you all enough\x01",
            "for all that you've done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PUmm... Please feel free to drop by\x01",
            "our house whenever you'd like.\x01",
            "We'll welcome you with open arms.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The two of them bowed deeply.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    BeginChrThread(0x1B, 1, 0, 31)

    def lambda_4E4B():

        label("loc_4E4B")

        TurnDirection(0xFE, 0x1B, 400)
        Yield()
        Jump("loc_4E4B")

    QueueWorkItem2(0x1C, 1, lambda_4E4B)
    Sleep(1200)
    BeginChrThread(0x1C, 1, 0, 31)
    OP_63(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(2400)

    ChrTalk(
        0x101,
        "#12P#0004FI guess that settles that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300FEven though that took FOREVER,\x01",
            "I'm glad we helped 'em out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FJudging by their conversation, I think\x01",
            "they will work things out. What a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0104FI hope you're right. I pray they'll be able\x01",
            "to work out their differences.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(4580, 1500, -14920, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12550, 0)
    SetChrPos(0x102, 5380, 0, -15280, 270)
    OP_0D()

    def lambda_4FEF():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FEF)

    def lambda_4FFC():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FFC)

    def lambda_5009():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5009)

    def lambda_5016():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5016)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#0100FAnyway, Lloyd. We should get going now.\x02\x03",
            "There's still some requests we can\x01",
            "finish up today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FYeah, good point.\x02\x03",
            "#0000FShall we get to it, guys?\x02",
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
            "[Search for an Important Person]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x1C)
    SetChrPos(0x0, 4780, 0, -14570, 275)
    ClearChrFlags(0x8, 0x80)
    OP_70(0x1, 0x0)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
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
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_29(0x2D, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_41EC end

    def Function_30_520C(): pass

    label("Function_30_520C")

    OP_96(0xFE, 0xDC0, 0x0, 0xFFFFC89C, 0x7D0, 0x0)
    OP_96(0xFE, 0x244, 0x0, 0xFFFFC39C, 0x7D0, 0x0)
    Return()

    # Function_30_520C end

    def Function_31_5235(): pass

    label("Function_31_5235")

    OP_93(0xFE, 0x10E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_31_5235 end

    def Function_32_5256(): pass

    label("Function_32_5256")

    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    BeginChrThread(0x11, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xF, 3, 0, 22)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 20)
    Sleep(2200)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 23)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 21)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x0, 0x2)
    EndChrThread(0x0, 0x3)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1, 0x2)
    EndChrThread(0x1, 0x3)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x2, 0x2)
    EndChrThread(0x2, 0x3)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x3, 0x2)
    EndChrThread(0x3, 0x3)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x101, 3910, 0, -14550, 90)
    SetChrPos(0x102, 4920, 0, -15560, 0)
    SetChrPos(0x103, 5870, 0, -14030, 270)
    SetChrPos(0x104, 4810, 0, -12940, 180)
    SetChrPos(0x1C, -8130, 600, -16740, 90)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_68(4760, 1500, -14530, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(12050, 0)
    OP_EE(0x0, 0xA)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#5P#0306FPhew... We're finally back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0203FWell, various factors delayed our return.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1C,
        "Voice",
        "Ah, you're all back.\x02",
    )

    CloseMessageWindow()
    OP_68(2670, 1500, -15870, 3000)
    MoveCamera(320, 30, 0, 3000)

    def lambda_54BA():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54BA)

    def lambda_54C7():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54C7)

    def lambda_54D4():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_54D4)

    def lambda_54E1():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_54E1)
    OP_95(0x1C, 130, 0, -15210, 2000, 0x0)
    Sleep(300)

    ChrTalk(
        0x1C,
        "#5PWh-Where is she? Where's Lady Carla?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FSorry to be the bearer of bad news, but we\x01",
            "weren't able to convince her to come home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106FWe parted with Carla once we reached\x01",
            "the Republic.\x02\x03",
            "#0108FI'm deeply sorry. We listened to your story,\x01",
            "and yet we still managed to fail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PN-No, it's okay. Please don't blame yourselves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PThis is my fault. I failed to prevent her\x01",
            "from leaving.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x1C,
        (
            "#5POh, but... How will I ever break this\x01",
            "to the master?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PI may very well be relieved of my duties...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0103FLeave contacting Representative Campbell\x01",
            "to me. Don't worry.\x02\x03",
            "#0100FI'll try to smooth things over, so you\x01",
            "should just return for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PYou'd do that for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5POkay, then. I'll be taking my leave.\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PU-Um... Thank you for all that\x01",
            "you've done today.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Marsha bowed deeply.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    BeginChrThread(0x1C, 1, 0, 31)
    Sleep(2400)

    ChrTalk(
        0x104,
        (
            "#12P#0306FMan... Did we really do our best\x01",
            "this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI have his contact information. Telling the\x01",
            "representative the truth is the least we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FYeah, you're right. Thankfully, we were able\x01",
            "to confirm her safety.\x02\x03",
            "I'm sure the representative will be relieved\x01",
            "to hear as much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0103FI'll take care of that. I'll have to debrief\x01",
            "him before Marsha returns home.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_68(4580, 1500, -14920, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12550, 0)
    OP_0D()

    def lambda_5A65():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A65)
    Sleep(20)

    def lambda_5A75():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A75)
    Sleep(12)

    def lambda_5A85():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A85)
    Sleep(80)
    OP_93(0x102, 0xB4, 0x190)
    Sleep(300)
    Fade(300)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    Sleep(600)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2800)
    OP_64(0x102)
    Sleep(300)
    SetChrName("")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie called the representative and explained\x01",
            "the events that took place.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    OP_93(0x102, 0x0, 0x190)
    Sleep(200)

    ChrTalk(
        0x101,
        "#6P#0005FHow'd Representative Campbell take it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0103F'You've done enough,' was all he said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0306FWell, damn. That about sums up his feelings.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0203FAnyway, we have fulfilled our obligations.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#11P#0200FShall we head back, Lloyd? We still have\x01",
            "other matters to address for the day.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#0005FGood call, Tio.\x02\x03",
            "#0000FShall we get to it, guys?\x02",
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
            "[Search for an Important Person]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 4780, 0, -14570, 275)
    OP_70(0x1, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
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
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_29(0x2D, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_5256 end

    def Function_33_5E26(): pass

    label("Function_33_5E26")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_5EB9")

    ChrTalk(
        0x101,
        (
            "#0003FThis path connects to another platform.\x02\x03",
            "#0000FOur work here is done, so let's get out\x01",
            "of the way and head outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9E")

    label("loc_5EB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5F33")

    ChrTalk(
        0x101,
        (
            "#0000FWe've wrapped up the investigation.\x01",
            "We don't have any business on the\x01",
            "Calvard-bound platform.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9E")

    label("loc_5F33")


    ChrTalk(
        0x101,
        (
            "#0003FThis path connects to another platform.\x02\x03",
            "#0001FWe need to get started before the\x01",
            "train departs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F9E")

    Sleep(50)
    SetChrPos(0x0, 54500, 0, -16000, 270)
    EventEnd(0x4)
    Return()

    # Function_33_5E26 end

    def Function_34_5FB5(): pass

    label("Function_34_5FB5")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a timetable for the Crossbell State area.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_34_5FB5 end

    def Function_35_5FF7(): pass

    label("Function_35_5FF7")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a route map for the Crossbell State area.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_35_5FF7 end

    def Function_36_6039(): pass

    label("Function_36_6039")

    OP_25(0x323, 0x64)
    Sleep(200)
    OP_25(0x323, 0x5A)
    Sleep(200)
    OP_25(0x323, 0x50)
    Sleep(200)
    OP_25(0x323, 0x46)
    Sleep(200)
    OP_25(0x323, 0x3C)
    Sleep(200)
    OP_25(0x323, 0x32)
    Sleep(200)
    OP_25(0x323, 0x28)
    Sleep(200)
    OP_25(0x323, 0x1E)
    Sleep(200)
    OP_25(0x323, 0x14)
    Sleep(200)
    OP_25(0x323, 0xA)
    Sleep(200)
    OP_25(0x323, 0x0)
    Return()

    # Function_36_6039 end

    def Function_37_6084(): pass

    label("Function_37_6084")

    OP_25(0x325, 0x64)
    Sleep(80)
    OP_25(0x325, 0x5A)
    Sleep(80)
    OP_25(0x325, 0x50)
    Sleep(80)
    OP_25(0x325, 0x46)
    Sleep(80)
    OP_25(0x325, 0x3C)
    Sleep(80)
    OP_25(0x325, 0x32)
    Sleep(80)
    OP_25(0x325, 0x28)
    Sleep(80)
    OP_25(0x325, 0x1E)
    Sleep(80)
    OP_25(0x325, 0x14)
    Sleep(80)
    OP_25(0x325, 0xA)
    Sleep(80)
    OP_25(0x325, 0x0)
    Return()

    # Function_37_6084 end

    SaveToFile()

Try(main)
