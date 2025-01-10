from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3510.bin",                # FileName
        "t3510",                    # MapName
        "t3510",                    # Location
        0x005C,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 92, 0, 4, 0, 5],
    )

    BuildStringList((
        "t3510",                  # 0
        "Receptionist Marcana",   # 1
        "Receptionist Thomas",    # 2
        "Ricardo",                # 3
        "Lonnie",                 # 4
        "Rosco",                  # 5
        "Arios",                  # 6
        "Passenger",              # 7
        "Passenger",              # 8
        "Boy",                    # 9
        "Passenger",              # 10
        "Passenger",              # 11
        "Boy",                    # 12
        "Inspector Donovan",      # 13
        "Detective Raymond",      # 14
        "Detective Emma",         # 15
        "Anton",                  # 16
        "Ricky",                  # 17
        "Receptionist Michel",    # 18
        "Shizuku",                # 19
        "Renne",                  # 20
        "Arios",                  # 21
        "Bracer Scott",           # 22
        "Bracer Wenzel",          # 23
        "Bracer Lynn",            # 24
        "Bracer Aeolia",          # 25
        "Zeit",                   # 26
        "KeA",                    # 27
        "カード",                 # 28
        "Marsha",                 # 29
    ))

    AddCharChip((
        "chr/ch28200.itc",                   # 00
        "chr/ch28100.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "chr/ch10500.itc",                   # 03
        "chr/ch22100.itc",                   # 04
        "chr/ch24200.itc",                   # 05
        "chr/ch23800.itc",                   # 06
        "chr/ch20000.itc",                   # 07
        "chr/ch23500.itc",                   # 08
        "chr/ch30300.itc",                   # 09
        "chr/ch30200.itc",                   # 0A
        "chr/ch30500.itc",                   # 0B
        "chr/ch02402.itc",                   # 0C
        "chr/ch37300.itc",                   # 0D
        "chr/ch37400.itc",                   # 0E
    ))

    DeclNpc(-10220,  150,     2849,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-8350,   150,     6730,    135,  261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6679,    0,       5530,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6630,    0,       -3460,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(6110,    0,       -4760,   45,   389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-4750,   5179,    12399,   75,   469,  0x0, 0,   12,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(6500,    0,       -10180,  345,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-10500,  5000,    7010,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-10970,  5000,    6079,    270,  389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1120,   5000,    13970,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-2160,   0,       -2170,   165,  389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(29,      0,       -8789,   135,  389,  0x0, 0,   6,   0,   0,   2,   0,   18,  255,  0)
    DeclNpc(8850,    0,       -7480,   225,  389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(7630,    0,       -8699,   45,   389,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-7539,   5000,    11000,   315,  405,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(8329,    0,       -319,    45,   385,  0x0, 0,   13,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(6500,    0,       -330,    45,   385,  0x0, 0,   14,  0,   0,   0,   0,   24,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 37,  0.25999999046325684,   7.989999771118164,     0.0,                   36.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -0.04333333298563957,  -3.994999885559082,    -0.0,                  1.0])

    DeclActor(-8690,   0,       2530,    1000,    -10220,  1600,    2850,    0x007E, 0,  6,  0x0000)
    DeclActor(-7210,   0,       5680,    1000,    -8350,   1600,    6730,    0x007E, 0,  8,  0x0000)
    DeclActor(-7590,   0,       -2440,   1200,    -7590,   1500,    -2440,   0x007C, 0,  38, 0x0000)

    ScpFunction((
        "Function_0_564",          # 00, 0
        "Function_1_61C",          # 01, 1
        "Function_2_647",          # 02, 2
        "Function_3_672",          # 03, 3
        "Function_4_673",          # 04, 4
        "Function_5_73E",          # 05, 5
        "Function_6_7F0",          # 06, 6
        "Function_7_7F4",          # 07, 7
        "Function_8_E41",          # 08, 8
        "Function_9_E45",          # 09, 9
        "Function_10_139C",        # 0A, 10
        "Function_11_1A6F",        # 0B, 11
        "Function_12_1B95",        # 0C, 12
        "Function_13_1CB3",        # 0D, 13
        "Function_14_1D73",        # 0E, 14
        "Function_15_1E06",        # 0F, 15
        "Function_16_1E56",        # 10, 16
        "Function_17_1F17",        # 11, 17
        "Function_18_1F6A",        # 12, 18
        "Function_19_1FBD",        # 13, 19
        "Function_20_217A",        # 14, 20
        "Function_21_21D9",        # 15, 21
        "Function_22_2288",        # 16, 22
        "Function_23_246A",        # 17, 23
        "Function_24_2EAD",        # 18, 24
        "Function_25_2F7C",        # 19, 25
        "Function_26_368C",        # 1A, 26
        "Function_27_39F1",        # 1B, 27
        "Function_28_3D94",        # 1C, 28
        "Function_29_4150",        # 1D, 29
        "Function_30_43A4",        # 1E, 30
        "Function_31_4C23",        # 1F, 31
        "Function_32_4C60",        # 20, 32
        "Function_33_58BE",        # 21, 33
        "Function_34_58D3",        # 22, 34
        "Function_35_58E8",        # 23, 35
        "Function_36_5911",        # 24, 36
        "Function_37_593A",        # 25, 37
        "Function_38_5A01",        # 26, 38
    ))


    def Function_0_564(): pass

    label("Function_0_564")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5A4"),
        (1, "loc_5B0"),
        (2, "loc_5BC"),
        (3, "loc_5C8"),
        (4, "loc_5D4"),
        (5, "loc_5E0"),
        (6, "loc_5EC"),
        (SWITCH_DEFAULT, "loc_5F8"),
    )


    label("loc_5A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_61B")

    Return()

    # Function_0_564 end

    def Function_1_61C(): pass

    label("Function_1_61C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_646")
    OP_94(0xFE, 0xFFFFF704, 0xFFFFF876, 0xDB6, 0xFFFFE1C4, 0x3E8)
    Sleep(300)
    Jump("Function_1_61C")

    label("loc_646")

    Return()

    # Function_1_61C end

    def Function_2_647(): pass

    label("Function_2_647")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_671")
    OP_94(0xFE, 0x406, 0xFFFFE192, 0xFFFFFBFA, 0xFFFFD9C2, 0x3E8)
    Sleep(100)
    Jump("Function_2_647")

    label("loc_671")

    Return()

    # Function_2_647 end

    def Function_3_672(): pass

    label("Function_3_672")

    Return()

    # Function_3_672 end

    def Function_4_673(): pass

    label("Function_4_673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_682")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_69F")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_707")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6CB")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_707")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_707")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0xF, 0x10)
    BeginChrThread(0x13, 0, 0, 2)

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_71F")
    Jump("loc_73D")

    label("loc_71F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_735")
    SetMapFlags(0x10000000)
    Event(0, 29)
    Jump("loc_73D")

    label("loc_735")

    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_73D")

    Return()

    # Function_4_673 end

    def Function_5_73E(): pass

    label("Function_5_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_750")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_750")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_782")
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_7AB")

    label("loc_782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_79C")
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    Jump("loc_7AB")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7AB")
    ClearMapObjFlags(0x0, 0x4)

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7C2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7C2")

    label("loc_7C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_END)), "loc_7D3")
    OP_24(0x86)
    Jump("loc_7EF")

    label("loc_7D3")

    SoundDistance(0x86, 0x16D0, 0x0, 0x259E, 0x1388, 0x30D40, 0x64, 0x0)

    label("loc_7EF")

    Return()

    # Function_5_73E end

    def Function_6_7F0(): pass

    label("Function_6_7F0")

    Call(0, 7)
    Return()

    # Function_6_7F0 end

    def Function_7_7F4(): pass

    label("Function_7_7F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_816")
    Call(0, 32)
    Return()

    label("loc_816")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_944")

    ChrTalk(
        0x8,
        (
            "The police conducted a thorough\x01",
            "search of the airport earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those detectives mentioned something\x01",
            "about a false bomb threat, I think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, well. I shouldn't fret about it. We\x01",
            "need to hurry and resume airport services\x01",
            "if we want to stick to our schedule.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A2D")

    label("loc_944")


    ChrTalk(
        0x8,
        (
            "I'm afraid that neither I nor the CPD have\x01",
            "any idea what the motive behind the bomb\x01",
            "threat was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, well. I shouldn't fret about it. We still\x01",
            "need to hurry and resume airport services\x01",
            "if we want to stick to our schedule.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2D")

    Jump("loc_E3D")

    label("loc_A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BB2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AFC")

    ChrTalk(
        0x8,
        (
            "Our regularly scheduled flight to Liberl via\x01",
            "the Calabria will be departing soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Passengers who have their tickets, please\x01",
            "hurry and head through the boarding gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAD")

    label("loc_AFC")


    ChrTalk(
        0x8,
        (
            "I don't quite understand the situation...\x01",
            "but this Carla definitely isn't in any of\x01",
            "our records.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, we look forward to serving you\x01",
            "next time you're looking to fly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAD")

    Jump("loc_E3D")

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D26")

    ChrTalk(
        0x8,
        (
            "Our airship routes primarily consist of ones\x01",
            "going north, to the Principality of Remiferia,\x01",
            "and ones going south, to the Liberl Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We do have routes that fly to Erebonia and\x01",
            "Calvard, but the amount of people who take\x01",
            "those is considerably less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Or, I should say, your average person is\x01",
            "much more likely to take the railway.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E3D")

    label("loc_D26")


    ChrTalk(
        0x8,
        (
            "Our airship routes primarily consist of ones\x01",
            "going north, to the Principality of Remiferia,\x01",
            "and ones going south, to the Liberl Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We do have routes that fly to Erebonia and\x01",
            "Calvard, but most people tend to take the\x01",
            "railway when traveling to those two countries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3D")

    TalkEnd(0x8)
    Return()

    # Function_7_7F4 end

    def Function_8_E41(): pass

    label("Function_8_E41")

    Call(0, 9)
    Return()

    # Function_8_E41 end

    def Function_9_E45(): pass

    label("Function_9_E45")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_101B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F66")

    ChrTalk(
        0x9,
        (
            "The second I heard about the bomb\x01",
            "threat, a chill ran down my spine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Things ended up being fine, but this\x01",
            "disaster forced us to freeze our entire\x01",
            "flight schedule for today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We feel horrible that it's inconvenienced\x01",
            "so many of our passengers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1016")

    label("loc_F66")


    ChrTalk(
        0x9,
        (
            "Because of our mandatory halting of airport\x01",
            "services, many of our passengers' travel\x01",
            "plans have been delayed significantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Whoever did this, I'll never forgive you.\x02",
    )

    CloseMessageWindow()

    label("loc_1016")

    Jump("loc_1398")

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_11D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1106")

    ChrTalk(
        0x9,
        (
            "Here at the ticket counter, we handle ticket sales,\x01",
            "immigration registration, and baggage claim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We are in charge of transporting your\x01",
            "baggage to your destination. I assure\x01",
            "you, it is safe with us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11D2")

    label("loc_1106")


    ChrTalk(
        0x9,
        (
            "On top of handling ticket sales, we are also\x01",
            "in charge of loading the passengers' baggage\x01",
            "onto the airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Feel free to ask for our help when you're\x01",
            "transporting heavy baggage on your flight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D2")

    Jump("loc_1398")

    label("loc_11D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F5")

    ChrTalk(
        0x9,
        (
            "With this many tourists, the entry process\x01",
            "becomes a lot more hectic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At times like this, I almost want to throw\x01",
            "everything away and go enjoy all of the\x01",
            "festivities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But I can't neglect my job. I have a\x01",
            "responsibility to the airport to uphold.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1398")

    label("loc_12F5")


    ChrTalk(
        0x9,
        (
            "Whenever work gets wild like this, I\x01",
            "can't help but want to escape...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No, I shouldn't think like that. I have\x01",
            "a responsibility to the airport to uphold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1398")

    TalkEnd(0x9)
    Return()

    # Function_9_E45 end

    def Function_10_139C(): pass

    label("Function_10_139C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BE")
    Call(0, 30)
    Return()

    label("loc_13BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1492")

    ChrTalk(
        0xFE,
        (
            "Geez, I still can't believe it! How the\x01",
            "heck did that card get in there?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm positive that it wasn't there when\x01",
            "that courier came to drop off the package...\x01",
            "At least, I'm pretty sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6B")

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_163A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159C")

    ChrTalk(
        0xFE,
        (
            "I sort of feel bad for the police, too. They\x01",
            "must have put aside a lot of important stuff\x01",
            "to come here and investigate the threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They must think this was a big waste\x01",
            "of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, at least we know the airport's safe now.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1635")

    label("loc_159C")


    ChrTalk(
        0xFE,
        (
            "You know, I ended up searching the entire\x01",
            "airport with the police. Boy, did that wear\x01",
            "me out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, at least we know the airport's safe now.\x02",
    )

    CloseMessageWindow()

    label("loc_1635")

    Jump("loc_1A6B")

    label("loc_163A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1835")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178E")

    ChrTalk(
        0xFE,
        (
            "Oftentimes, wealthier passengers like to\x01",
            "take their pets with them on their flights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They have to be placed in special cages, due to\x01",
            "our baggage rules. All the barking and crying can\x01",
            "be a bit of handful when that happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't bother me too much, but it'd be\x01",
            "nice if they could keep it down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1830")

    label("loc_178E")


    ChrTalk(
        0xFE,
        (
            "I know the owner and his or her pet haven't\x01",
            "done anything wrong, but still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personally, I'd rather not handle someone\x01",
            "else's pet. But that's just me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1830")

    Jump("loc_1A6B")

    label("loc_1835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1981")

    ChrTalk(
        0xFE,
        (
            "If my watch is right, someone from the\x01",
            "up-and-coming Capua Delivery Service\x01",
            "should be arriving any minute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumor says that they were originally\x01",
            "involved with some shady business\x01",
            "before becoming a shipping company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their boss might look scary as a\x01",
            "monster, but they're good people,\x01",
            "overall.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A6B")

    label("loc_1981")


    ChrTalk(
        0xFE,
        (
            "Fun fact: I heard that their airship,\x01",
            "the Bobcat, is top-of-the-line and\x01",
            "used as their base of operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to them, it can even give\x01",
            "the Arseille a run for its money...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm not sure if I believe that, though.\x02",
    )

    CloseMessageWindow()

    label("loc_1A6B")

    TalkEnd(0xFE)
    Return()

    # Function_10_139C end

    def Function_11_1A6F(): pass

    label("Function_11_1A6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B33")

    ChrTalk(
        0xFE,
        "Hurry and take care of that one, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right outside the airport, there's a local\x01",
            "shipping company named Rhimes Deliveries.\x01",
            "Run it over there and come back, y'hear?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1B91")

    label("loc_1B33")


    ChrTalk(
        0xFE,
        "C'mon, move your ass!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we're late, Her Ladyship is going\x01",
            "to chew us out big-time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B91")

    TalkEnd(0xFE)
    Return()

    # Function_11_1A6F end

    def Function_12_1B95(): pass

    label("Function_12_1B95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C02")

    ChrTalk(
        0xFE,
        "Yeah, yeah, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, they love to throw the long\x01",
            "jobs at me, huh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1CAF")

    label("loc_1C02")


    ChrTalk(
        0xFE,
        (
            "Wait, didn't the bosses' friends come\x01",
            "to Crossbell, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If she wasn't so loaded with work, I bet\x01",
            "Her Ladyship would have come with me\x01",
            "to hang out with those two.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAF")

    TalkEnd(0xFE)
    Return()

    # Function_12_1B95 end

    def Function_13_1CB3(): pass

    label("Function_13_1CB3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I think those guys are from a shipping\x01",
            "company, but something about those\x01",
            "wild uniforms doesn't really look the part...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it does make them look pretty\x01",
            "cool, so whatever.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1CB3 end

    def Function_14_1D73(): pass

    label("Function_14_1D73")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Haha, look over there! That airship\x01",
            "is going to take off any second now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Whoa! That's so freaking cool!\x01",
            "How does that even work?!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1D73 end

    def Function_15_1E06(): pass

    label("Function_15_1E06")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I get to fly on a big airship! This is\x01",
            "the greatest day of my LIFE!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1E06 end

    def Function_16_1E56(): pass

    label("Function_16_1E56")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Air travel has become quite pleasant over\x01",
            "the past few years, hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Goddess dwells in the sky, you know.\x01",
            "Perhaps we have received Her blessings\x01",
            "through our endeavors.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1E56 end

    def Function_17_1F17(): pass

    label("Function_17_1F17")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Hurry up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we don't board soon, we're\x01",
            "going to miss our flight!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1F17 end

    def Function_18_1F6A(): pass

    label("Function_18_1F6A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Dang it, I was wanting to stay in\x01",
            "Crossbell for a little while longer.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1F6A end

    def Function_19_1FBD(): pass

    label("Function_19_1FBD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2100")

    ChrTalk(
        0xFE,
        "Hey there, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything's fine at the airport now,\x01",
            "if you were wondering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know who caused that mess,\x01",
            "but boy, was it a nuisance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWell, just keep up the good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll try, but I'm running out of gas.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We weren't even able to find out who\x01",
            "our perp was...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2176")

    label("loc_2100")


    ChrTalk(
        0xFE,
        (
            "Well, I'll withdraw for now and leave\x01",
            "that bit to the First Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've still got to write up my report.\x02",
    )

    CloseMessageWindow()

    label("loc_2176")

    TalkEnd(0xFE)
    Return()

    # Function_19_1FBD end

    def Function_20_217A(): pass

    label("Function_20_217A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I still have to write up my report for the\x01",
            "brass... Can't they give a man a break?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_217A end

    def Function_21_21D9(): pass

    label("Function_21_21D9")

    TalkBegin(0xFE)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "Right... Is that right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Understood. I'll make investigating\x01",
            "the source of that letter my top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You be careful, too, Dudley.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Return()

    # Function_21_21D9 end

    def Function_22_2288(): pass

    label("Function_22_2288")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_231C")
    Jump("loc_2366")

    label("loc_231C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_233C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2366")

    label("loc_233C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_235C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2366")

    label("loc_235C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2366")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2462")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A6")
    Call(0, 26)
    Jump("loc_2462")

    label("loc_23A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23BC")
    Call(0, 27)
    Jump("loc_2462")

    label("loc_23BC")


    ChrTalk(
        0xFE,
        (
            "#1403FYou might not think it, but the final day of\x01",
            "the Anniversary Festival tends to bring\x01",
            "the most disturbances.\x02\x03",
            "#1400FDon't lose focus until the day is done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2462")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_2288 end

    def Function_23_246A(): pass

    label("Function_23_246A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2520")

    ChrTalk(
        0xFE,
        (
            "A brutal rejection in Liberl, and a\x01",
            "gentle one in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, Ricky. What's there to live\x01",
            "for now? What am I supposed\x01",
            "to do...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CE")

    label("loc_2520")


    ChrTalk(
        0x101,
        "#0000FOh, Anton?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, it's you guys. You know, I waited\x01",
            "a really long time for you yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(We completely forgot about him.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FAbout that... We're really sorry, Anton.\x02\x03",
            "You see, we were in the middle of a\x01",
            "really important investigation yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, well, in the end, I had to go\x01",
            "meet Fran all by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to ask her out on a lunch\x01",
            "date, but...things didn't work out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fran said...she already had a special\x01",
            "someone that she's taking care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FR-Really...? I'm sorry to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Somethin' about a sweet girl like Fran\x01",
            "sayin' she has a 'special somebody'\x01",
            "rubs me the wrong way.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, don't worry about me. I'm used to\x01",
            "this sort of thing...ha ha ha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing that pure smile form on her lips as\x01",
            "she talked about the person she loves...\x01",
            "It basically killed me inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, my game plan is to head back to\x01",
            "Liberl and reinvent myself! Stronger,\x01",
            "better, and smarter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Giving up on him in the middle of his\x01",
            "support request wasn't our wisest\x01",
            "call, was it?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(I think you might be right.)\x02\x03",
            "(Well, we can't do any more for him.\x01",
            "Let's leave him be and hope he finds\x01",
            "some peace someday.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_29CE")

    Jump("loc_2EA9")

    label("loc_29D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2A7D")

    ChrTalk(
        0xFE,
        (
            "A brutal rejection in Liberl, and a\x01",
            "gentle one in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, Ricky. What's there to live\x01",
            "for now? What am I supposed\x01",
            "to do...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3F")

    label("loc_2A7D")


    ChrTalk(
        0xFE,
        (
            "Oh, hey. Thanks again for all\x01",
            "your help yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FAnton, are you returning home?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sadly so. There's nothing left for me\x01",
            "here, since Fran rejected me and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FTruly unfortunate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, don't worry about me. I'm used to\x01",
            "this sort of thing...ha ha ha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing that pure smile form on her lips as\x01",
            "she talked about the person she loves...\x01",
            "It basically killed me inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(The person she loves...? Should we tell\x01",
            "him that she meant the sergeant major?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Eh, quit while you're ahead. That talk\x01",
            "would probably get a lil' more confusing\x01",
            "than what we wanna deal with.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Agreed. I feel horrible for him, but\x01",
            "I feel like it's for the best...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_2D3F")

    Jump("loc_2EA9")

    label("loc_2D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2DE2")

    ChrTalk(
        0xFE,
        (
            "A brutal rejection in Liberl, and a\x01",
            "gentle one in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, Ricky. What's there to live\x01",
            "for now? What am I supposed\x01",
            "to do...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA9")

    label("loc_2DE2")


    ChrTalk(
        0xFE,
        (
            "Even though I finally found my dream\x01",
            "girl, the one who returned my wallet to\x01",
            "me, it still ended in disaster...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She already has a special someone...?\x01",
            "Fate, what did I do to deserve this?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_2EA9")

    TalkEnd(0xFE)
    Return()

    # Function_23_246A end

    def Function_24_2EAD(): pass

    label("Function_24_2EAD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hey, it's up to Anton whether he wants to\x01",
            "stay depressed forever or actually learn\x01",
            "from his rejection this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess I'll keep watching after the poor guy.\x01",
            "I'm his only friend, after all.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_2EAD end

    def Function_25_2F7C(): pass

    label("Function_25_2F7C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    LoadChrToIndex("chr/ch09100.itc", 0x20)
    LoadChrToIndex("chr/ch02400.itc", 0x21)
    LoadChrToIndex("chr/ch08200.itc", 0x22)
    LoadChrToIndex("chr/ch02702.itc", 0x23)
    LoadChrToIndex("chr/ch27200.itc", 0x24)
    LoadChrToIndex("chr/ch27300.itc", 0x25)
    LoadChrToIndex("chr/ch32100.itc", 0x26)
    LoadChrToIndex("chr/ch32000.itc", 0x27)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_68(0, 900, 1000, 0)
    MoveCamera(310, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 600, 0, -400, 0)
    SetChrPos(0x102, 1900, 0, -600, 0)
    SetChrPos(0x104, 200, 0, -1500, 0)
    SetChrPos(0x103, 1500, 0, -1700, 0)
    SetChrPos(0x107, -800, 0, 2700, 180)
    SetChrPos(0x108, 800, 0, 2700, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 0, 0, 3000, 180)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -2200, 0, -1100, 45)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrPos(0x19, -1100, 0, 300, 45)
    SetChrChipByIndex(0x1C, 0x21)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -2300, 0, 0, 45)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrPos(0x22, -200, 0, -400, 0)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, 2700, 0, 600, 315)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -300, 0, -2800, 0)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 1000, 0, -3100, 0)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -3200, 0, -2200, 45)
    SetChrChipByIndex(0x20, 0x26)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -2200, 0, -2200, 45)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#5301115V",
            scpstr(0x18),
            "#30WEstelle and Joshua decided to\x01",
            "return to Liberl with Renne.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(320, 27, 0, 4000)
    SetCameraDistance(19000, 4000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    FadeToDark(300, 0, 100)
    OP_0D()

    AnonymousTalk(
        0xFF,
        (
            "#5301116V",
            scpstr(0x18),
            "#30WThough the Bracer Guild's manpower was\x01",
            "cut, the CPD more than made up for it\x01",
            "through political reform.\x02\x03",
            "#5301117VHopefully, we can reduce their burden and\x01",
            "continue to strengthen our partnership in\x01",
            "the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 700, 3000, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_C9(0x0, 0x3, 0xFF9B9B9B, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    Sleep(500)
    SetMessageWindowPos(50, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#5301118V",
            scpstr(0x18),
            "#30WBefore leaving, Renne reminded us of some\x01",
            "difficult questions.\x02\x03",
            "#5301119VThe truth behind what happened 500 years\x01",
            "ago, why KeA was at the Schwarze Auction...\x02\x03",
            "#5301120V...and who the true killer of my brother,\x01",
            "Guy Bannings, really is.\x02\x03",
            "#5301121VUnfortunately, the girl who seemed to know\x01",
            "everything, didn't hold the answers.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#5301122V",
            scpstr(0x18),
            "#30WHowever, finding the truth behind these\x01",
            "questions is my--no, OUR duty.\x02\x03",
            "#5301123VPromising to reunite again someday,\x01",
            "we gave our farewells and parted.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    RemoveParty(0x6, 0x0)
    RemoveParty(0x7, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5E, 0)
    NewScene("e3500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_2F7C end

    def Function_26_368C(): pass

    label("Function_26_368C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4490, 6400, 11460, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27290, 0)
    SetChrPos(0x101, -4250, 5000, 10550, 0)
    SetChrPos(0x102, -5000, 5000, 10200, 0)
    SetChrPos(0x103, -3100, 5000, 10300, 315)
    SetChrPos(0x104, -4500, 5000, 8900, 0)
    SetChrSubChip(0xD, 0x2)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#11P#1405FOh, isn't this rare? I wasn't expecting\x01",
            "to run into the SSS here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0105FArios...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FH-Hello. Thanks again for helping us\x01",
            "out at the Ancient Battlefield yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0300FSo, goin' on another business trip?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#1403FIndeed. To Remiferia this time.\x02\x03",
            "#1405FFrom the looks of things, you aren't\x01",
            "intending to board an airship, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0012FNo, we aren't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0206FWe are in the middle of solving a nasty\x01",
            "mystery, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#1404FIs that so? Very well, then.\x02\x03",
            "#1402FRemember, today's the last day of the\x01",
            "festival. Don't lose focus just yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0012FY-Yes, sir. (We definitely can't\x01",
            "let him know about our plan to\x01",
            "infiltrate the auction...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 5000, 10550, 0)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0xB3, 6)
    EventEnd(0x5)
    Return()

    # Function_26_368C end

    def Function_27_39F1(): pass

    label("Function_27_39F1")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4490, 6400, 11460, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27290, 0)
    SetChrPos(0x101, -4250, 5000, 10550, 0)
    SetChrPos(0x102, -5000, 5000, 10200, 0)
    SetChrPos(0x103, -3100, 5000, 10300, 315)
    SetChrPos(0x104, -4500, 5000, 8900, 0)
    SetChrSubChip(0xD, 0x2)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#6P#0108FExcuse me, Arios...\x02\x03",
            "#0101FAre you sure it's okay to leave\x01",
            "without going to see Shizuku?\x02\x03",
            "It sounds like you haven't been\x01",
            "able to spend much time with\x01",
            "her during the festival, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#1403FBelieve me, it pains me to go so long\x01",
            "away from Shizuku's side.\x02\x03",
            "#1402FI had hoped that I'd be able to see her at\x01",
            "least one time this week, but unfortunately,\x01",
            "that didn't happen.\x02\x03",
            "#1404FI'm sure that Estelle and Joshua have been\x01",
            "spending plenty of time with her, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106FI'm sorry. I didn't mean to intrude\x01",
            "on your family affairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#1402FNo, I should be the one apologizing.\x01",
            "If not for me, you wouldn't have to\x01",
            "worry about Shizuku's well-being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001F(I wonder if Elie was reminded of her\x01",
            "and her parents...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 5000, 10550, 0)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0xB4, 2)
    EventEnd(0x5)
    Return()

    # Function_27_39F1 end

    def Function_28_3D94(): pass

    label("Function_28_3D94")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-21960, 1250, 24660, 0)
    MoveCamera(321, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(42870, 0)
    SetChrPos(0x101, -600, 0, -18300, 0)
    SetChrPos(0x102, 750, 0, -20000, 0)
    SetChrPos(0x103, 750, 0, -18300, 0)
    SetChrPos(0x104, -600, 0, -20000, 0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetCameraDistance(49570, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(500)
    OP_68(-5130, 1250, 17490, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(60830, 0)
    OP_68(830, 1250, -11780, 8000)
    MoveCamera(315, 27, 0, 8000)
    OP_6E(300, 8000)
    SetCameraDistance(51170, 8000)
    PlaceName2(340, 200, "c_plac32", 0x0, 1500)
    Sleep(3800)

    def lambda_3EAB():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3EAB)
    Sleep(50)

    def lambda_3EC3():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3EC3)
    Sleep(50)

    def lambda_3EDB():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3EDB)
    Sleep(50)

    def lambda_3EF3():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3EF3)
    WaitChrThread(0x3, 1)
    Sleep(300)
    Fade(500)
    OP_68(10, 650, -13380, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32259, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#0001FAll right, let's try checking out the airport.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FPhantom Thief B's clue mentioned the 'white\x01",
            "falcon,' which is Liberl's national bird.\x02\x03",
            "#0202FBy 'the entrance to the white falcon,' he must\x01",
            "have been referring to Crossbell Airport, where\x01",
            "there are daily flights to Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0305FAll that's left is 'a place where time is carried\x01",
            "away'...ain't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0104FLet's keep that detail in our minds while\x01",
            "we investigate.\x02\x03",
            "#0100FShall we begin?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -110, 0, -15030, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xD2, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_3D94 end

    def Function_29_4150(): pass

    label("Function_29_4150")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-21960, 1250, 24660, 0)
    MoveCamera(321, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(42870, 0)
    SetChrPos(0x101, -600, 0, -18300, 0)
    SetChrPos(0x102, 750, 0, -20000, 0)
    SetChrPos(0x103, 750, 0, -18300, 0)
    SetChrPos(0x104, -600, 0, -20000, 0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetCameraDistance(59570, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(500)
    OP_68(-5130, 1250, 17490, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(60830, 0)
    OP_0D()
    OP_68(830, 1250, -11780, 8000)
    MoveCamera(315, 27, 0, 8000)
    OP_6E(300, 8000)
    SetCameraDistance(51170, 8000)
    PlaceName2(340, 200, "c_plac32", 0x0, 1500)
    Sleep(3800)

    def lambda_4268():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4268)

    def lambda_427D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_427D)

    def lambda_4292():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4292)

    def lambda_42A7():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_42A7)
    WaitChrThread(0x3, 1)
    Sleep(300)
    Fade(500)
    OP_68(10, 850, -13380, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32259, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0003FHere we are. Crossbell Airport.\x01",
            "Let's hurry over to the reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101FWe have to ask about Carla\x01",
            "before it's too late!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -110, 0, -15030, 0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xD2, 2)
    EventEnd(0x5)
    Return()

    # Function_29_4150 end

    def Function_30_43A4(): pass

    label("Function_30_43A4")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50091.itc", 0x1E)
    OP_4B(0xA, 0xFF)
    OP_68(6620, 860, 4440, 0)
    MoveCamera(319, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32830, 0)
    SetChrPos(0x101, 6000, 10, 3800, 0)
    SetChrPos(0x102, 7200, 10, 2400, 0)
    SetChrPos(0x103, 7200, 10, 3800, 0)
    SetChrPos(0x104, 6000, 10, 2400, 0)
    SetChrPos(0xA, 6680, 0, 5530, 180)
    SetChrPos(0x23, 8580, 600, 8610, 0)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x1E)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#11PHi there. Are you here to pick up\x01",
            "your things, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PPlease just flash me your claim check\x01",
            "when you see your luggage, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003F(This is the airport's baggage claim.\x01",
            "Maybe he'll be able to help us...)\x02\x03",
            "#0000FUm, excuse me. Have you seen a\x01",
            "card around here? It'd probably be\x01",
            "pretty out of place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PA card...? Like, not a claim check?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PI'm sorry, but I can't think of anything\x01",
            "like that off the top of my head. Why\x01",
            "don't you try asking the receptionist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0300FWill do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0204FWe appreciate your assistance.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x23, 0, 0, 31)
    Sleep(2000)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5P#0011F#12AUh... Is that what I think it is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0111F#12AUnbelievable.\x02",
    )

    CloseMessageWindow()
    OP_68(7130, 1260, 2560, 2000)

    def lambda_47AE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47AE)

    def lambda_47BB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_47BB)

    def lambda_47C8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_47C8)
    OP_95(0x102, 8090, 10, 440, 1200, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Sleep(300)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Obtained a white envelope.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
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
        0x104,
        (
            "#5P#0306FSo many questions, so few answers.\x02\x03",
            "#0301FB sure is one tough customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0108FLet's see what the next message is...\x02",
    )

    CloseMessageWindow()
    OP_95(0x102, 7200, 10, 2400, 1200, 0x0)

    def lambda_4950():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4950)

    def lambda_495D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_495D)
    Sleep(200)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, 90, -1, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　Find the mark of a splendid correspondent!\x01",
            "　11/1192\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#11P#0006FAnother riddle. Great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FI don't know why I even\x01",
            "got my hopes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200F'The mark of a splendid correspondent'...\x01",
            "What exactly could that mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0103FCorrespondent... So someone who\x01",
            "communicates through letters?\x02\x03",
            "#0100FPerhaps we should ask someone whose\x01",
            "job revolves around writing letters?\x02\x03",
            "#0106FThat's just a wild guess, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FWell, there's nothing to do but\x01",
            "start searching for new clues.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 6780, 10, 3210, 0)
    OP_4C(0xA, 0xFF)
    OP_D5(0x1E)
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x22, 0x1, 0x5)
    SetScenarioFlags(0x0, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_30_43A4 end

    def Function_31_4C23(): pass

    label("Function_31_4C23")

    OP_96(0x23, 0x212A, 0x258, 0x866, 0x2DA, 0x0)
    OP_96(0x23, 0x2300, 0x258, 0x532, 0x2DA, 0x0)
    OP_96(0x23, 0x260C, 0x258, 0x456, 0x2DA, 0x0)
    Return()

    # Function_31_4C23 end

    def Function_32_4C60(): pass

    label("Function_32_4C60")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch34500.itc", 0x1E)
    OP_68(-7940, 850, 2230, 0)
    MoveCamera(314, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32180, 0)
    SetChrPos(0x101, -6570, 0, 2270, 266)
    SetChrPos(0x102, -6260, 0, 970, 266)
    SetChrPos(0x103, -4860, 0, 910, 266)
    SetChrPos(0x104, -5170, 0, 2290, 266)
    SetChrPos(0x24, -3120, 0, -6240, 0)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse me, do you have a moment?\x01",
            "We have a bit of an emergency...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POh, dear. What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FYou see, an individual by the name of\x01",
            "Carla Campbell should have boarded\x01",
            "an outgoing flight to Liberl.\x02\x03",
            "We were wondering, has that airship\x01",
            "finished boarding yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou said Carla Campbell? If you'll\x01",
            "give me a moment, please...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x8)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PI'm terribly sorry, but Carla Campbell\x01",
            "wasn't listed as a passenger.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        "#6P#0105FA-Are you positive?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FThat's strange. I could have sworn that\x01",
            "she planned on taking this flight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FMe, too. There's only one flight scheduled\x01",
            "today that's headin' for Liberl, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FCorrect, and it has not departed yet...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x24,
        "Voice",
        "#2PP-Pardon me...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_50C8():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50C8)

    def lambda_50D5():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50D5)

    def lambda_50E2():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_50E2)

    def lambda_50EF():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50EF)

    def lambda_50FC():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_50FC)
    OP_68(-3470, 1250, -3500, 2000)
    Sleep(2000)

    NpcTalk(
        0x24,
        "Maid",
        "#6PI knew it...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x24,
        "Maid",
        "#6PYou're the police, aren't you?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-6070, 1250, -470, 0)
    MoveCamera(299, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30600, 0)
    SetChrPos(0x24, -3960, 0, -3890, 355)
    OP_96(0x24, 0xFFFFECD2, 0x0, 0xFFFFF556, 0x3E8, 0x0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#11P#0105FWait, aren't you Marsha? One of the maids\x01",
            "at Representative Campbell's mansion?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0200FAre you the maid that ran away with Carla?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "#6PY-Yes, that's right...\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1700)

    ChrTalk(
        0x24,
        (
            "#6PYou see, Lady Carla...never intended\x01",
            "to go to Liberl in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#6PThat was merely a rumor she spread to\x01",
            "throw her father off her tracks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#6PIn actuality, she plans to live in the home\x01",
            "of an acquaintance in the Republic.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#11P#0005FShe's going to Calvard...?! Crap, she\x01",
            "must have gone to the station, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "#6PIf you hurry, you might make it in time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#6PI-I-I'm sorry. My lady has caused so\x01",
            "much trouble for everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#6PBut, if at all possible...please bring\x01",
            "Lady Carla back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#6PDespite what she says, she doesn't\x01",
            "really want to leave Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0303FSo she's still got some regrets, huh?\x02\x03",
            "#0300FWell, time to roll. We'll bring her back\x01",
            "for ya, don't you worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0203FIf she's Republic-bound... The train will be\x01",
            "departing in a matter of minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0001FThere's no time to waste, then!\x02",
    )

    CloseMessageWindow()

    def lambda_5656():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5656)

    def lambda_5663():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5663)

    def lambda_5670():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5670)

    def lambda_567D():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_567D)
    Sleep(200)

    def lambda_568D():

        label("loc_568D")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_568D")

    QueueWorkItem2(0x24, 1, lambda_568D)
    OP_68(-3070, 1250, -2850, 3000)
    MoveCamera(314, 28, 0, 3000)
    OP_6E(300, 3000)
    SetCameraDistance(30680, 3000)
    BeginChrThread(0x103, 1, 0, 36)
    BeginChrThread(0x104, 1, 0, 35)
    BeginChrThread(0x101, 1, 0, 33)
    BeginChrThread(0x102, 1, 0, 34)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_56ED():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56ED)

    def lambda_56FA():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_56FA)
    Sleep(400)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#0000FThanks, Marsha! You were a big help!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FMarsha, could you go inform the\x01",
            "representative of what's happened?\x02\x03",
            "You can leave bringing Carla back\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#5PO-Okay. Please, I'm leaving Lady\x01",
            "Carla in your hands!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_57F9():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57F9)

    def lambda_5806():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5806)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_581B():
        OP_95(0xFE, 1190, 0, -16350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_581B)

    def lambda_5835():
        OP_95(0xFE, -670, 0, -16360, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5835)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x24, 0x1)
    SetChrPos(0x0, 30, 0, -15120, 180)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x5A, 0x0)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    OP_49()
    OP_D5(0x1E)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_29(0x2D, 0x1, 0x9)
    Sleep(1000)
    EventEnd(0x5)
    NewScene("r1500", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_32_4C60 end

    def Function_33_58BE(): pass

    label("Function_33_58BE")

    OP_95(0xFE, -2100, 0, -2600, 4000, 0x0)
    Return()

    # Function_33_58BE end

    def Function_34_58D3(): pass

    label("Function_34_58D3")

    OP_95(0xFE, -2700, 0, -3900, 4000, 0x0)
    Return()

    # Function_34_58D3 end

    def Function_35_58E8(): pass

    label("Function_35_58E8")

    OP_95(0xFE, 670, 0, -4290, 5000, 0x0)
    OP_95(0xFE, -400, 0, -16000, 5000, 0x0)
    Return()

    # Function_35_58E8 end

    def Function_36_5911(): pass

    label("Function_36_5911")

    OP_95(0xFE, 670, 0, -5760, 5000, 0x0)
    OP_95(0xFE, -400, 0, -12500, 5000, 0x0)
    Return()

    # Function_36_5911 end

    def Function_37_593A(): pass

    label("Function_37_593A")

    EventBegin(0x1)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0x0, 500)

    ChrTalk(
        0xA,
        (
            "Hold up... The boarding platform\x01",
            "is over that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You can't enter if you don't have\x01",
            "a boarding pass, so be careful\x01",
            "not to wander too far in.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 960, 0, 5140, 180)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_37_593A end

    def Function_38_5A01(): pass

    label("Function_38_5A01")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Welcome to Crossbell State!\x01",
            "Are you looking for a place to\x01",
            "stay? Try Hotel Millennium!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_5A01 end

    SaveToFile()

Try(main)
