from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1310.bin",                # FileName
        "c1310",                    # MapName
        "c1310",                    # Location
        0x001C,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 300, 5000, 0, 0, 1, 28, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1310",                  # 0
        "Security Guard Wang",    # 1
        "Security Guard Paul",    # 2
        "Receptionist Lanfei",    # 3
        "Receptionist Corinna",   # 4
        "Trader Rizero",          # 5
        "Researcher",             # 6
        "Chief Roberts",          # 7
        "Citizen",                # 8
        "Citizen",                # 9
        "Bracer Scott",           # 10
        "Bracer Wenzel",          # 11
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch27900.itc",                   # 01
        "chr/ch30500.itc",                   # 02
        "chr/ch27702.itc",                   # 03
        "chr/ch32800.itc",                   # 04
        "chr/ch29300.itc",                   # 05
        "chr/ch20900.itc",                   # 06
        "chr/ch20902.itc",                   # 07
        "chr/ch27200.itc",                   # 08
        "chr/ch27300.itc",                   # 09
    ))

    DeclNpc(8500,    0,       13310,   270,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-5730,   300,     29909,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       300,     31700,   180,  257,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7110,    300,     32759,   90,   257,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-4840,   0,       18180,   90,   341,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(5000,    0,       17850,   90,   257,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(6500,    0,       17850,   270,  257,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(6570,    300,     29760,   0,    257,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8210,    300,     28309,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(1820,    300,     25760,   315,  389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(3220,    300,     25959,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)

    DeclEvent(0x0000, 0, 25,  9.5,                   16.0,                  -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.75,                 -5.333333492279053,    0.10000000894069672,   1.0])

    DeclActor(0,       300,     30300,   1500,    0,       1800,    31700,   0x007E, 0,  6,  0x0000)
    DeclActor(6650,    300,     31080,   1500,    7110,    1800,    32759,   0x007E, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_300",          # 00, 0
        "Function_1_3B8",          # 01, 1
        "Function_2_5E3",          # 02, 2
        "Function_3_5EA",          # 03, 3
        "Function_4_684",          # 04, 4
        "Function_5_191B",         # 05, 5
        "Function_6_2DDF",         # 06, 6
        "Function_7_2DE3",         # 07, 7
        "Function_8_35A7",         # 08, 8
        "Function_9_58C3",         # 09, 9
        "Function_10_58C7",        # 0A, 10
        "Function_11_6F42",        # 0B, 11
        "Function_12_83F8",        # 0C, 12
        "Function_13_8D24",        # 0D, 13
        "Function_14_9024",        # 0E, 14
        "Function_15_90FC",        # 0F, 15
        "Function_16_99F5",        # 10, 16
        "Function_17_9A80",        # 11, 17
        "Function_18_9BEE",        # 12, 18
        "Function_19_9D55",        # 13, 19
        "Function_20_9F8B",        # 14, 20
        "Function_21_B187",        # 15, 21
        "Function_22_C21C",        # 16, 22
        "Function_23_CAE3",        # 17, 23
        "Function_24_CDA2",        # 18, 24
        "Function_25_D1E0",        # 19, 25
    ))


    def Function_0_300(): pass

    label("Function_0_300")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_340"),
        (1, "loc_34C"),
        (2, "loc_358"),
        (3, "loc_364"),
        (4, "loc_370"),
        (5, "loc_37C"),
        (6, "loc_388"),
        (SWITCH_DEFAULT, "loc_394"),
    )


    label("loc_340")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_34C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_358")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_364")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_370")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_37C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_388")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_394")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_3A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_3B7")

    Return()

    # Function_0_300 end

    def Function_1_3B8(): pass

    label("Function_1_3B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D0")
    ClearScenarioFlags(0x5F, 1)
    Event(0, 2)

    label("loc_3D0")

    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_41E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_414")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1080, 300, 29510, 0)
    SetChrFlags(0xE, 0x10)

    label("loc_414")

    SetChrFlags(0xC, 0x80)
    Jump("loc_5C1")

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_42C")
    Jump("loc_5C1")

    label("loc_42C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_43A")
    Jump("loc_5C1")

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_448")
    Jump("loc_5C1")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_45B")
    SetChrFlags(0xC, 0x10)
    Jump("loc_5C1")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_46E")
    SetChrFlags(0xC, 0x10)
    Jump("loc_5C1")

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_486")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_5C1")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_494")
    Jump("loc_5C1")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4B8")
    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5C1")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4C6")
    Jump("loc_5C1")

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5C1")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4F8")
    Jump("loc_5C1")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_53E")
    SetChrPos(0xB, 7110, 300, 32759, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_END)), "loc_539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_539")

    Jump("loc_5C1")

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_END)), "loc_564")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_564")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5C1")

    label("loc_584")

    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_END)), "loc_5A1")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_5A1")

    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_5C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E2")
    Event(0, 23)

    label("loc_5E2")

    Return()

    # Function_1_3B8 end

    def Function_2_5E3(): pass

    label("Function_2_5E3")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_5E3 end

    def Function_3_5EA(): pass

    label("Function_3_5EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_603")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_609")

    label("loc_603")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)

    label("loc_609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_620")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63C")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_653")

    label("loc_63C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_653")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_653")

    label("loc_653")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_683")
    OP_1B(0x0, 0x0, 0xD)

    label("loc_683")

    Return()

    # Function_3_5EA end

    def Function_4_684(): pass

    label("Function_4_684")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_711")

    ChrTalk(
        0xFE,
        (
            "Hmm... I feel like we're not getting as many\x01",
            "customers as we usually do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It might just be my imagination, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1917")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_87E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7C5")

    ChrTalk(
        0xFE,
        (
            "It's our job as guards to help make our\x01",
            "patrons feel safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There may have been a shooting recently,\x01",
            "but I assure you, the IBC is perfectly secure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_879")

    label("loc_7C5")


    ChrTalk(
        0xFE,
        (
            "We've increased the number of guards on\x01",
            "duty by about twenty percent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just precautionary measures, considering\x01",
            "the shooting that just happened in the\x01",
            "Harbor District.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_879")

    Jump("loc_1917")

    label("loc_87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_95B")

    ChrTalk(
        0xFE,
        (
            "Our security department grades the level of\x01",
            "safety for major cities across the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a necessary metric to keep track of,\x01",
            "to ensure Mr. Crois' safety whenever he\x01",
            "travels abroad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A41")

    label("loc_95B")


    ChrTalk(
        0xFE,
        (
            "Crossbell's safety rating has rapidly deteriorated\x01",
            "over the last couple of weeks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to our analysis, it's fallen down\x01",
            "to a C-.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Citizens should be careful of dark alleyways.\x01",
            "They can get pretty dangerous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A41")

    Jump("loc_1917")

    label("loc_A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AB4")

    ChrTalk(
        0xFE,
        (
            "Guards like us have to stay alert at all times.\x01",
            "You never know what might happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43")

    label("loc_AB4")


    ChrTalk(
        0xFE,
        "We've made it to the last day of the festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now's the time to look alive. There's always\x01",
            "trouble brewing in moments like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B43")

    Jump("loc_1917")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_BAC")

    ChrTalk(
        0xFE,
        (
            "The IBC's directors have been in\x01",
            "meetings all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Heh. I feel bad for 'em.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1917")

    label("loc_BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C7A")

    ChrTalk(
        0xFE,
        (
            "Most people will forget because of the festival,\x01",
            "but Crossbell isn't exactly safe right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here's to hoping a wandering tourist doesn't\x01",
            "get lost and caught up in trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D73")

    label("loc_C7A")


    ChrTalk(
        0xFE,
        (
            "According to a recent report by our security\x01",
            "department, Crossbell's safety rating\x01",
            "has dramatically decreased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What the hell are the police doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the situation continues to get any worse,\x01",
            "we'll have to strengthen our security.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D73")

    Jump("loc_1917")

    label("loc_D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DDE")

    ChrTalk(
        0xFE,
        (
            "Either way, you won't be able to operate\x01",
            "the elevator without a key card.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8B")

    label("loc_DDE")


    ChrTalk(
        0xFE,
        (
            "Some person tried to operate the elevator\x01",
            "without a key card moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Damned tourists. Read the sign!\x01",
            "It says it right there, 'Entry is prohibited!'\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E8B")

    Jump("loc_1917")

    label("loc_E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F27")

    ChrTalk(
        0xFE,
        (
            "The Harbor District's experiencing some\x01",
            "heavy congestion right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all these extra customers, we'd\x01",
            "better stay vigilant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1917")

    label("loc_F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_FC5")

    ChrTalk(
        0xFE,
        (
            "The building's security system is off of\x01",
            "the grid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doesn't matter what kind of hacking\x01",
            "thingy you try. You won't be able to\x01",
            "break in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1917")

    label("loc_FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_10E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_END)), "loc_103F")

    ChrTalk(
        0xFE,
        "Do you have business on the top floor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please board the elevator and scan your\x01",
            "key card.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DF")

    label("loc_103F")


    ChrTalk(
        0xFE,
        (
            "The upper floors are off limits,\x01",
            "except to authorized personnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have any business up there, then\x01",
            "please request access from the receptionist.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10DF")

    Jump("loc_1917")

    label("loc_10E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F5")

    ChrTalk(
        0xFE,
        (
            "Crossbell's public order continues\x01",
            "to deteriorate as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't look like it's connected to any\x01",
            "sort of huge incident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You never know what could happen.\x01",
            "The state doesn't have any laws to\x01",
            "crack down on mercenaries.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1281")

    label("loc_11F5")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0xFE,
        "Crossbell's in a complex situation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It isn't accurate to call it safe, so we\x01",
            "need to keep our wits about us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1281")

    Jump("loc_1917")

    label("loc_1286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1316")

    ChrTalk(
        0xFE,
        (
            "If the company continues to grow, then we'll\x01",
            "have to expand our security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Some businesses are having problems.\x02",
    )

    CloseMessageWindow()
    Jump("loc_143D")

    label("loc_1316")


    ChrTalk(
        0xFE,
        (
            "Our security department has been getting\x01",
            "a lot more questions from foreign\x01",
            "businesses lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "VIPs are constantly asking for bodyguards,\x01",
            "so we've been getting requests to train\x01",
            "their security guards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doesn't matter what company it is, security\x01",
            "will always be a difficult task.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_143D")

    Jump("loc_1917")

    label("loc_1442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_15EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14D7")

    ChrTalk(
        0xFE,
        (
            "Hey. Did you guys know there's a\x01",
            "huge cafeteria on the floor above us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahem! Never mind.\x01",
            "It's still business hours.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E7")

    label("loc_14D7")


    ChrTalk(
        0xFE,
        (
            "I like to run 100 selge every morning to\x01",
            "maintain my stamina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm always training my body. You never know\x01",
            "when something's going to happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thing is, my morning runs always leave\x01",
            "me with an empty stomach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ahem! Forget it. It's still business hours.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_15E7")

    Jump("loc_1917")

    label("loc_15EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_181B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1691")

    ChrTalk(
        0xFE,
        (
            "There's no place on the continent more\x01",
            "secure than this building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can rest easy and focus on handling\x01",
            "your business deals here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_1691")


    ChrTalk(
        0xFE,
        (
            "We like to boast about how this building\x01",
            "is the safest place on the entire continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Modern buildings require modern security.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our security system utilizes the latest\x01",
            "in orbal engineering advances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not to mention, our security department\x01",
            "is full of trained professionals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't matter what kind of criminal they are.\x01",
            "This establishment won't get invaded.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1816")

    Jump("loc_1917")

    label("loc_181B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1874")

    ChrTalk(
        0xFE,
        (
            "Leave the IBC's security concerns to us.\x01",
            "We're trained professionals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1917")

    label("loc_1874")


    ChrTalk(
        0xFE,
        (
            "Oh, that jacket of yours...\x01",
            "Are you guys a part of the CPD?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We work in the IBC's security department.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let us handle the IBC's security concerns.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1917")

    TalkEnd(0xFE)
    Return()

    # Function_4_684 end

    def Function_5_191B(): pass

    label("Function_5_191B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19A6")

    ChrTalk(
        0xFE,
        (
            "Mr. Crois and his daughter are\x01",
            "out on a business trip right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It feels a little lonely around here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A54")

    label("loc_19A6")


    ChrTalk(
        0xFE,
        (
            "Miss Crois is out on a business trip\x01",
            "at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like she goes on more trips\x01",
            "with each passing year...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's become an awful lot like her father.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1A54")

    Jump("loc_2DDB")

    label("loc_1A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B19")

    ChrTalk(
        0xFE,
        (
            "Doesn't seem like there are as many\x01",
            "customers as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Must be because of the shooting.\x01",
            "Sadly, we don't have enough manpower\x01",
            "to station guards outside the IBC.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DDB")

    label("loc_1B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1BC7")

    ChrTalk(
        0xFE,
        (
            "Not sure if it's because of the Anniversary\x01",
            "Festival or what, but there's been talk of\x01",
            "expanding the business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm a bit concerned about it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D1D")

    label("loc_1BC7")


    ChrTalk(
        0xFE,
        (
            "Actually, the Reinford Company\x01",
            "operates a division of their sales\x01",
            "department inside of this building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've been getting requests from their\x01",
            "competitors, the Verne Company, to\x01",
            "open up a branch here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I'd heard they butt heads at every\x01",
            "possible opportunity, so I figure they're\x01",
            "pretty competitive with each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1D1D")

    Jump("loc_2DDB")

    label("loc_1D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1DEC")

    ChrTalk(
        0xFE,
        (
            "Though not well documented, Crossbell\x01",
            "has had its fair share of terroristic\x01",
            "incidents in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More importantly, the festival appears to have\x01",
            "ended without a hitch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E7E")

    label("loc_1DEC")


    ChrTalk(
        0xFE,
        "The Anniversary Festival is ending today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's too bad I didn't get a chance to enjoy it.\x01",
            "Still, I'm glad it ended without incident.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1E7E")

    Jump("loc_2DDB")

    label("loc_1E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1F04")

    ChrTalk(
        0xFE,
        (
            "Miss Crois popped in here a little\x01",
            "while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She made me happy by thanking us\x01",
            "for all of our hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DDB")

    label("loc_1F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_208A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F97")

    ChrTalk(
        0xFE,
        "Hey, have you guys heard of Mishelam Wonderland?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've got a cute feline mascot that goes\x01",
            "by the name of Mishy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2085")

    label("loc_1F97")


    ChrTalk(
        0xFE,
        (
            "There's a theme park on the other\x01",
            "side of Lake Elm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a real hit with families. Thank\x01",
            "the IBC and their generous investment\x01",
            "for making it all possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure it's been packed during the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2085")

    Jump("loc_2DDB")

    label("loc_208A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_20DA")

    ChrTalk(
        0xFE,
        (
            "Though, it's still calmer in here than\x01",
            "in the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_20DA")


    ChrTalk(
        0xFE,
        (
            "There's tourists from all across the continent\x01",
            "here to check out the festivities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A few of them came in to ask for\x01",
            "directions earlier.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "I'm not used to dealing with those kinds\x01",
            "of people. It was a pain.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_21D1")

    Jump("loc_2DDB")

    label("loc_21D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2329")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_225D")

    ChrTalk(
        0xFE,
        "Chief Roberts looked happier than usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something good must have happened\x01",
            "to him during work, I bet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2324")

    label("loc_225D")


    ChrTalk(
        0xFE,
        (
            "Chief Roberts from the Epstein Foundation\x01",
            "came to greet me a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He had a bright smile across his face\x01",
            "as he walked away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm guessing something good happened to him.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2324")

    Jump("loc_2DDB")

    label("loc_2329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_24FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2404")

    ChrTalk(
        0xFE,
        (
            "I'm impressed at how put together Miss Crois is\x01",
            "for her age. Don't know anyone else that can\x01",
            "manage multiple businesses like she can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wouldn't expect any less from the\x01",
            "CEO's daughter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FA")

    label("loc_2404")


    ChrTalk(
        0xFE,
        "Miss Crois is on the IBC's board of directors.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, she's not directly involved with\x01",
            "managing the company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's successfully managing several\x01",
            "businesses at her age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We feel honored to serve as her personal\x01",
            "bodyguards.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_24FA")

    Jump("loc_2DDB")

    label("loc_24FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_259C")

    ChrTalk(
        0xFE,
        "Nothing unusual to report today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's because the IBC's main headquarters\x01",
            "has the perfect security system in place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260C")

    label("loc_259C")


    ChrTalk(
        0xFE,
        "Nothing unusual to report today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The IBC's main offices haven't had any\x01",
            "issues ever since opening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_260C")

    Jump("loc_2DDB")

    label("loc_2611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_26B3")

    ChrTalk(
        0xFE,
        (
            "The IBC's board of directors will be meeting\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've gotta pay extra attention to security\x01",
            "today. Can't have anything bad happening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DDB")

    label("loc_26B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2838")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2788")

    ChrTalk(
        0xFE,
        (
            "Our security department grades the level of\x01",
            "safety for major cities across the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Crois often goes abroad on business trips,\x01",
            "so we have to monitor that for his safety.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2833")

    label("loc_2788")


    ChrTalk(
        0xFE,
        (
            "Crossbell's safety rating has rapidly deteriorated\x01",
            "over the last couple of weeks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We gotta stay vigilant. Don't know what\x01",
            "kinda nutjob might come and attack.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2833")

    Jump("loc_2DDB")

    label("loc_2838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2912")

    ChrTalk(
        0xFE,
        (
            "The receptionist can help you withdraw\x01",
            "mira from bank accounts stationed in\x01",
            "other countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, uh... I don't plan on walking you guys\x01",
            "to the receptionist. Figure it out on your own.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4E")

    label("loc_2912")


    ChrTalk(
        0xFE,
        (
            "The IBC has a ton of branches stationed\x01",
            "throughout the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only that, but we're affiliated with many\x01",
            "different banks, too. It's safe to say we own the\x01",
            "largest network of banks on the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The receptionist can help you withdraw\x01",
            "mira from bank accounts stationed in\x01",
            "other countries.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2A4E")

    Jump("loc_2DDB")

    label("loc_2A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B45")

    ChrTalk(
        0xFE,
        (
            "Even though Crossbell's made some crazy\x01",
            "technological advancements, we still suffer\x01",
            "damage from the occasional monster attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As employees of a security firm, it's our duty\x01",
            "to make sure we help prevent them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C35")

    label("loc_2B45")


    ChrTalk(
        0xFE,
        (
            "There have apparently been monsters popping\x01",
            "up everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our department managed to receive some\x01",
            "of the reports, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that an intern at St. Ursula\x01",
            "was attacked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's some scary stuff, man. I feel\x01",
            "for them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C35")

    Jump("loc_2DDB")

    label("loc_2C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2CED")

    ChrTalk(
        0xFE,
        (
            "I get asked a lot of questions just 'cause\x01",
            "I stand near the receptionist's counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhh... If you'd like to check your account,\x01",
            "then ask the receptionist.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DDB")

    label("loc_2CED")


    ChrTalk(
        0xFE,
        "Welcome to the International Bank of Crossbell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been employed here for two years,\x01",
            "and yet here I am still guiding customers\x01",
            "to the teller's window.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it's because I stand so close to the\x01",
            "receptionist's counter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2DDB")

    TalkEnd(0xFE)
    Return()

    # Function_5_191B end

    def Function_6_2DDF(): pass

    label("Function_6_2DDF")

    Call(0, 7)
    Return()

    # Function_6_2DDF end

    def Function_7_2DE3(): pass

    label("Function_7_2DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DF5")
    Call(0, 20)
    Return()

    label("loc_2DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E1F")
    Call(0, 24)
    Return()

    label("loc_2E1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E40")
    Call(0, 21)
    Return()

    label("loc_2E40")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32CB")

    ChrTalk(
        0xA,
        (
            "Hello, and welcome to the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xA, 0x102, 500)

    ChrTalk(
        0xA,
        "Oh, now this is a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's been quite a while, hasn't it,\x01",
            "Miss MacDowell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(Huh?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205F(Are you acquainted, Elie?)\x02",
    )

    CloseMessageWindow()

    def lambda_2F46():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F46)

    def lambda_2F53():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2F53)

    def lambda_2F60():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2F60)
    Sleep(300)

    ChrTalk(
        0x102,
        "#0100FHello, Lanfei. Indeed, it has been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This is our first time seeing each other since\x01",
            "you returned from your studies abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, yes. That reminds me. Would you like\x01",
            "me to inform the miss of your arrival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She's currently overseeing Mishelam's\x01",
            "operations, but I'm sure she'd rush back\x01",
            "if I told her you were visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FI'm glad to hear that Bell's still keeping\x01",
            "herself busy.\x02\x03",
            "#0100FThat's okay, though. I'm not here to discuss\x01",
            "anything important with her today.\x02\x03",
            "I'll visit her another day when I have the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Is that so? I'll send her your regards, then.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#0305F(Didn't know you had connections within\x01",
            "the IBC, Mademois-Elie.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Yeah, you seemed pretty close to\x01",
            "each other, too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#203F(She continues to uphold her\x01",
            "image of a noble lady.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#0113FI can hear you, you know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 4)
    Jump("loc_35A3")

    label("loc_32CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34B9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Exchange\x01",               # 1
            "Ask About Request\x01",      # 2
            "Leave\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3359")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3359")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_338C")
    OP_AF(0xB5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 2)), scpexpr(EXPR_END)), "loc_3387")
    Sleep(100)
    Call(0, 22)
    TalkEnd(0xA)
    Return()

    label("loc_3387")

    Jump("loc_34AF")

    label("loc_338C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347F")

    ChrTalk(
        0xA,
        (
            "I'd like you to participate in a test exchange\x01",
            "to verify that our services are operational.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please bring thirty of each\x01",
            "type of sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That should be enough to adequately\x01",
            "demonstrate our services.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34AF")

    label("loc_347F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3493")
    Jump("loc_34AF")

    label("loc_3493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34AF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)

    label("loc_34AF")

    Jump("loc_32F2")

    label("loc_34B4")

    Jump("loc_35A3")

    label("loc_34B9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_34C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A3")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3518")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3518")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_356E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_354A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3543")
    OP_AF(0xB7)
    Jump("loc_3545")

    label("loc_3543")

    OP_AF(0xB6)

    label("loc_3545")

    Jump("loc_355F")

    label("loc_354A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_355D")
    OP_AF(0xB5)
    Jump("loc_355F")

    label("loc_355D")

    OP_AF(0xB4)

    label("loc_355F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_359E")

    label("loc_356E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3582")
    Jump("loc_359E")

    label("loc_3582")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_359E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)

    label("loc_359E")

    Jump("loc_34C3")

    label("loc_35A3")

    TalkEnd(0xA)
    Return()

    # Function_7_2DE3 end

    def Function_8_35A7(): pass

    label("Function_8_35A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3778")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_36C7")

    ChrTalk(
        0xA,
        (
            "Carla bosses around her poor maid with\x01",
            "unreasonable requests far too often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I watched her try to order her maid to make\x01",
            "a reservation at a hotel in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I only know this because Carla was yelling\x01",
            "at her maid in our lobby.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3773")

    label("loc_36C7")


    ChrTalk(
        0xA,
        "The meeting ended a few moments ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I believe Miss Crois is currently\x01",
            "in the CEO's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You may proceed to the 16th floor\x01",
            "using the elevator over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3773")

    Jump("loc_58C2")

    label("loc_3778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_38D2")

    ChrTalk(
        0xA,
        "Thank you for your swift cooperation today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We may finally launch our new services\x01",
            "thanks to your efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The key card I've given you will remain\x01",
            "active, so you may continue to freely\x01",
            "use the service as you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, that sounds handy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FLeave it to the IBC to flex at any\x01",
            "chance they can get.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C2")

    label("loc_38D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_39D1")

    ChrTalk(
        0xA,
        (
            "I just asked City Hall about the situation\x01",
            "at the airport. Apparently it's temporarily\x01",
            "closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't think the sudden closure will affect\x01",
            "our business too badly. Still, though.\x01",
            "I've never experienced anything like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A85")

    label("loc_39D1")


    ChrTalk(
        0xA,
        (
            "Crossbell Airport appears to be closed\x01",
            "for inspection today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The CEO and Miss Crois are out on\x01",
            "a business trip in the Republic, but I\x01",
            "don't think it should affect us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3A85")

    Jump("loc_58C2")

    label("loc_3A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3D01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3B37")

    ChrTalk(
        0xA,
        (
            "Miss Crois has been in discussions with the\x01",
            "board of directors about how to handle this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm hoping this doesn't affect our\x01",
            "stock prices...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFC")

    label("loc_3B37")


    ChrTalk(
        0xA,
        (
            "What should we do? It doesn't help\x01",
            "that Mr. Crois is away, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHmm? Are you referring to the incident\x01",
            "that took place in the Harbor District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FIs everything okay here, Lanfei?\x01",
            "Were any of you affected?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "No, we're all fortunately safe and sound.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm more worried about our stocks.\x01",
            "Their value is volatile, so they\x01",
            "may end up being affected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our board of directors are trying to\x01",
            "work out how to handle this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3CFC")

    Jump("loc_58C2")

    label("loc_3D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D8F")

    ChrTalk(
        0xA,
        (
            "I wonder how Mr. Crois\x01",
            "will handle this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He told us that he'll be having a\x01",
            "discussion about it this evening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F09")

    label("loc_3D8F")


    ChrTalk(
        0xA,
        (
            "Oh, Miss MacDowell! Good thing\x01",
            "you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mr. Crois will be returning from\x01",
            "his lengthy business trip today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It should almost be time for his\x01",
            "return, actually...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_END)), "loc_3F06")

    ChrTalk(
        0x102,
        (
            "#0100FHahaha... I actually ran into\x01",
            "Uncle at the entrance.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder what's keeping him, then. Is he\x01",
            "taking care of some important business?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F06")

    SetScenarioFlags(0x0, 2)

    label("loc_3F09")

    Jump("loc_58C2")

    label("loc_3F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3F8E")

    ChrTalk(
        0xA,
        "The CEO is off on another business trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "My apologies. I believe he'll return within\x01",
            "the next few days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C2")

    label("loc_3F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_415F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4041")

    ChrTalk(
        0xA,
        (
            "Mr. Crois is currently busy with a celebration\x01",
            "and planning another business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may be some time before you will\x01",
            "be able to meet him again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_415A")

    label("loc_4041")


    ChrTalk(
        0xA,
        (
            "I saw Miss Crois here earlier, so I believe\x01",
            "her meeting with the board of directors\x01",
            "should be finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, Mr. Crois is spending his\x01",
            "evening at a celebration and planning\x01",
            "another business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may be some time before you will\x01",
            "be able to meet him again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_415A")

    Jump("loc_58C2")

    label("loc_415F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4215")

    ChrTalk(
        0xA,
        (
            "Oh, that reminds me... There's an important\x01",
            "all-day-long meeting today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The CEO is far too busy to show any\x01",
            "excitement for the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_434E")

    label("loc_4215")


    ChrTalk(
        0xA,
        (
            "We have more customers than usual today,\x01",
            "so I can appreciate how quickly Corinna\x01",
            "works in situations like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "My only problem with her is...she vanishes\x01",
            "into thin air the moment her break starts,\x01",
            "even when we're still busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh* She'll be gone before you can\x01",
            "say, 'Your break is starting.'\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_434E")

    Jump("loc_58C2")

    label("loc_4353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_441B")

    ChrTalk(
        0xA,
        (
            "Both the CEO and Miss Crois\x01",
            "are absent today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You may be able to find them at St. Ursula\x01",
            "Medical College if you have any important\x01",
            "matters to discuss, Miss MacDowell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4514")

    label("loc_441B")


    ChrTalk(
        0xA,
        (
            "Hello, and welcome to the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The CEO and Miss Crois\x01",
            "are absent today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you'd like to speak with them, then they're\x01",
            "on their way to St. Ursula Medical College.\x01",
            "They should be arriving any minute now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4514")

    Jump("loc_58C2")

    label("loc_4519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 2)), scpexpr(EXPR_END)), "loc_45B6")

    ChrTalk(
        0xA,
        (
            "Ah, yes. Miss Crois should be in her office,\x01",
            "if you'd like to speak to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I think she is free to meet with you right now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_487D")

    label("loc_45B6")


    ChrTalk(
        0xA,
        (
            "Hello, and welcome to the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It's good to see you all again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope you're enjoying celebrating\x01",
            "Crossbell State's 70th birthday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThank you, Lanfei. We are.\x02\x03",
            "Work must be far more hectic for you, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes. Crossbell's birthday isn't an internationally\x01",
            "observed holiday, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And, seeing as how we're an international\x01",
            "bank, business continues to operate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Today's just another normal day for us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FTh-That's unfortunate. I feel bad for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't worry about me. We'll be compensated\x01",
            "with time off after the Anniversary Festival\x01",
            "has ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please don't hesitate to ask if you need\x01",
            "to use any of our services.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 2)

    label("loc_487D")

    Jump("loc_58C2")

    label("loc_4882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_491B")

    ChrTalk(
        0xA,
        "The CEO left for another business trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I believe Miss Crois is currently in her room,\x01",
            "if you'd like to speak with her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB0")

    label("loc_491B")


    ChrTalk(
        0xA,
        "The CEO left for another business trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I believe he'll return in about two weeks,\x01",
            "so please remain patient until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FUncle never takes a moment of rest, does he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He can't. Not when he's aggressively trying to\x01",
            "expand our influence by forming partnerships\x01",
            "with foreign banks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "His current lifestyle doesn't allow for him to be\x01",
            "in town for more than a few days at a time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4AB0")

    Jump("loc_58C2")

    label("loc_4AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_4CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4B41")

    ChrTalk(
        0xA,
        (
            "I look forward to seeing you again,\x01",
            "Miss MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sure Miss Crois would be delighted\x01",
            "if you visited.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CDD")

    label("loc_4B41")


    ChrTalk(
        0xA,
        (
            "It sounds like you were able to meet\x01",
            "with Miss Crois. I'm happy for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, Miss MacDowell. Please hold\x01",
            "on to your key card, as it will remain\x01",
            "perfectly valid for use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sure Miss Crois would be delighted\x01",
            "if you visited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FI get the impression that all of our future\x01",
            "meetings are going to be that messy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FY-Yeah, probably.\x01",
            "(Bell can get overbearing at times...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4CDD")

    Jump("loc_58C2")

    label("loc_4CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4D83")

    ChrTalk(
        0xA,
        (
            "Mr. Crois is ready to meet you, so please\x01",
            "take the elevator to the top floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The elevator can be found on the\x01",
            "right side of this floor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C2")

    label("loc_4D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4F4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4E45")

    ChrTalk(
        0xA,
        (
            "Corinna vanishes into thin air the moment\x01",
            "her break starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She does excellent work, but I find\x01",
            "she can be a little too overbearing\x01",
            "with the customers at times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F4A")

    label("loc_4E45")


    ChrTalk(
        0xA,
        (
            "Corinna's been a fantastic worker\x01",
            "ever since she joined us last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However...she vanishes into thin air the\x01",
            "moment her break starts, and it's a bit\x01",
            "of a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She does excellent work, but I find\x01",
            "her to be a bit too overbearing\x01",
            "at times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4F4A")

    Jump("loc_58C2")

    label("loc_4F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_53EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_506B")

    ChrTalk(
        0xA,
        (
            "Stock market speculation has grown\x01",
            "considerably as a field since you\x01",
            "went abroad, Miss MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "New investments are made daily,\x01",
            "and brokers regularly plan how to\x01",
            "compete with one another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can explain the details to you\x01",
            "next time you're here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53EA")

    label("loc_506B")


    ChrTalk(
        0xA,
        (
            "More customers have been showing an\x01",
            "interest in investment banking lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We've been receiving more inquiries\x01",
            "about the IBC's bond policy.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5183")

    ChrTalk(
        0xA,
        (
            "The service you helped implement has been\x01",
            "popular thus far. I imagine that's been\x01",
            "influencing the recent change.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5183")


    ChrTalk(
        0xA,
        (
            "Oh, by the way... How are things going\x01",
            "with you lately, Miss MacDowell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The account you opened up a long\x01",
            "time ago is still open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh. I didn't know you were into\x01",
            "investing, Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FWhoa, look at Mademois-Elie go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FI opened it because it made for useful study\x01",
            "material. Political movements are often\x01",
            "reflected in investment patterns.\x02\x03",
            "#0100FSadly, I can't come here as often as I could\x01",
            "when I was a student. My job keeps me\x01",
            "too busy, so I apologize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, no. It's okay! You can always come\x01",
            "back when it's convenient for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'll get you back into the swing of it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_53EA")

    Jump("loc_58C2")

    label("loc_53EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_55AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5466")

    ChrTalk(
        0xA,
        "Miss Crois was terribly worried about you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please don't push yourself too hard, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_55A6")

    label("loc_5466")


    ChrTalk(
        0xA,
        (
            "I read about your recent achievements,\x01",
            "Miss MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FO-Oh... I'm guessing you read the\x01",
            "Crossbell Times, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, I saw that you were in\x01",
            "yesterday's issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Miss Crois was terribly worried about you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I know you're just trying to do your job,\x01",
            "but please don't push yourself too hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_55A6")

    Jump("loc_58C2")

    label("loc_55AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5753")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_565B")

    ChrTalk(
        0xA,
        (
            "You'll be able to find all kinds of information about\x01",
            "the different operations that take place in here.\x01",
            "Please ask me if you need to know anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_574E")

    label("loc_565B")


    ChrTalk(
        0xA,
        (
            "You'll be able to find all kinds of information about\x01",
            "the different operations that take place in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our building is actually home to twenty\x01",
            "different companies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please refer to this desk if any of them\x01",
            "are expecting you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_574E")

    Jump("loc_58C2")

    label("loc_5753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_57ED")

    ChrTalk(
        0xA,
        (
            "I will absolutely tell Miss Crois.\x01",
            "I'm sure she'll be delighted\x01",
            "to hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please come back whenever you'd\x01",
            "like, Miss MacDowell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C2")

    label("loc_57ED")


    ChrTalk(
        0xA,
        (
            "Hello, and welcome to the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Miss Crois left this morning to conduct\x01",
            "some inspections, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I sincerely apologize.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I will let her know you were here.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_58C2")

    Return()

    # Function_8_35A7 end

    def Function_9_58C3(): pass

    label("Function_9_58C3")

    Call(0, 10)
    Return()

    # Function_9_58C3 end

    def Function_10_58C7(): pass

    label("Function_10_58C7")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_59C0")

    ChrTalk(
        0xB,
        "Huh, I don't see Rizero around today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He's usually here every day, so it's\x01",
            "pretty strange not to see him around.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_59BB")

    ChrTalk(
        0x101,
        "#0001F(One of the missing people...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(It sounds like he regularly visited\x01",
            "the IBC.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59BB")

    Jump("loc_6F3E")

    label("loc_59C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5B2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5A6E")

    ChrTalk(
        0xB,
        (
            "I'm confident the inside of the building is\x01",
            "secure at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "On the other hand, I couldn't tell you if\x01",
            "our stock prices are secure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B2A")

    label("loc_5A6E")


    ChrTalk(
        0xB,
        (
            "I heard there was some sort of raid.\x01",
            "That's never good news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thankfully, our security department does a\x01",
            "flawless job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "There's nothing to worry about inside the building.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5B2A")

    Jump("loc_6F3E")

    label("loc_5B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5CDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5BED")

    ChrTalk(
        0xB,
        (
            "Rizero's been having an incredible lucky\x01",
            "streak with his investments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I was him, I'd quit while I'm still ahead.\x01",
            "You never know when things might go bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD5")

    label("loc_5BED")


    ChrTalk(
        0xB,
        (
            "Rizero's been having an incredible lucky\x01",
            "streak with his investments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He even managed to score big on some of\x01",
            "them this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's honestly really impressive. I think it's been\x01",
            "going on for two whole weeks now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5CD5")

    Jump("loc_6F3E")

    label("loc_5CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5D6A")

    ChrTalk(
        0xB,
        "The IBC is closed for the holiday tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Just one more day to get through and\x01",
            "then it's vacation time. I can't wait!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F3E")

    label("loc_5D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5DA7")

    ChrTalk(
        0xB,
        "Miss Crois is such a sweetheart.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E65")

    label("loc_5DA7")


    ChrTalk(
        0xB,
        (
            "Miss Crois handsomely rewarded all of\x01",
            "the employees that worked through the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I get super motivated when I have a\x01",
            "boss that cares about me the way\x01",
            "she does!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5E65")

    Jump("loc_6F3E")

    label("loc_5E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6026")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5F1B")

    ChrTalk(
        0xB,
        (
            "The Anniversary Festival attracts\x01",
            "too many annoying people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't believe he managed to tear through\x01",
            "that application form in thirty seconds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6021")

    label("loc_5F1B")


    ChrTalk(
        0xB,
        (
            "We had a customer come in and try to\x01",
            "open a bank account to commemorate\x01",
            "the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He was in a hurry for the parade and wanted\x01",
            "to open it right away. To no one's surprise, he\x01",
            "rushed through it and messed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Sheesh, how annoying can you be?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_6021")

    Jump("loc_6F3E")

    label("loc_6026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_61A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_60B0")

    ChrTalk(
        0xB,
        (
            "The Anniversary Festival attracts too\x01",
            "many annoying people. They're clueless,\x01",
            "so I hate having to guide them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61A1")

    label("loc_60B0")


    ChrTalk(
        0xB,
        (
            "One of our customers yesterday caused\x01",
            "me nothing but problems!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He didn't really understand the concept\x01",
            "of a savings account, let alone a bank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He kept saying stuff like 'Give me money!'\x01",
            "or 'What the heck's a bank account?'\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_61A1")

    Jump("loc_6F3E")

    label("loc_61A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_62C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_622D")

    ChrTalk(
        0xB,
        (
            "The IBC is an international bank, so we\x01",
            "generally don't observe holidays.\x01",
            "It's kinda tragic, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62C4")

    label("loc_622D")


    ChrTalk(
        0xB,
        (
            "Most businesses in Crossbell State are\x01",
            "closed for the duration of the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd be lying if I said I wasn't a little\x01",
            "jealous of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_62C4")

    Jump("loc_6F3E")

    label("loc_62C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_641D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6355")

    ChrTalk(
        0xB,
        (
            "We shut down all of the terminals in the\x01",
            "building, just to be on the safe side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Ugh, how annoying is that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6418")

    label("loc_6355")


    ChrTalk(
        0xB,
        (
            "The security department contacted us to\x01",
            "tell us the back door had been removed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Oh, finally! We can use the terminals again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "How annoying. I wish they'd cut\x01",
            "me some slack.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)

    label("loc_6418")

    Jump("loc_6F3E")

    label("loc_641D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_64A4")

    ChrTalk(
        0xB,
        (
            "Lanfei supposedly used to hold\x01",
            "a secretarial role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It shows, too. I admire her beautifully\x01",
            "written signatures.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F3E")

    label("loc_64A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_668F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6537")

    ChrTalk(
        0xB,
        (
            "I've been enjoying working as a\x01",
            "receptionist for the IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The hours are tough, but I've been\x01",
            "having a lot of fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668A")

    label("loc_6537")


    ChrTalk(
        0xB,
        "*click* *clack*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 300)

    ChrTalk(
        0xB,
        (
            "I used to work with a smaller company,\x01",
            "but it was soooooooo boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I found out that I can handle the heck\x01",
            "out of a terminal, which helped land\x01",
            "me a job here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The hours may be strict, but the work\x01",
            "is fulfilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I feel fortunate enough to have a job\x01",
            "that's fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    ClearChrFlags(0xB, 0x10)

    label("loc_668A")

    Jump("loc_6F3E")

    label("loc_668F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_673C")

    ChrTalk(
        0xB,
        (
            "Hey there! Welcome to the IBC's\x01",
            "main reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We offer all sorts of nifty information\x01",
            "here. Feel free to ask me anything\x01",
            "you'd like!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6941")

    label("loc_673C")


    ChrTalk(
        0xB,
        (
            "Hey there! Welcome to the IBC's\x01",
            "main reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Would you like to open an account\x01",
            "or perhaps make a transaction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We also offer introductions to investments,\x01",
            "loans, and assets. We can even teach you a\x01",
            "thing or two about managing real estate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Go ahead and use any of our services!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Wow, it really feels like you can do\x01",
            "just about anything at the IBC.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(You technically can... As long as it's\x01",
            "mira-related. Their services cover just\x01",
            "about anything you could ever want.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_6941")

    Jump("loc_6F3E")

    label("loc_6946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6BA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6A11")

    ChrTalk(
        0xB,
        (
            "The orbal network is still in its infancy,\x01",
            "so any banking documents are still\x01",
            "handled by paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Our efficiency is bound to skyrocket\x01",
            "once that bad boy is up and running!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BA2")

    label("loc_6A11")


    ChrTalk(
        0xB,
        (
            "This building fully converted to orbal\x01",
            "technology a few years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Only problem is, our terminals can only\x01",
            "communicate with other terminals\x01",
            "within this building for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Our general affairs department just\x01",
            "recently started using them, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because the terminals are only used for\x01",
            "work done inside the building, any backend\x01",
            "banking is still done with paper documents.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_6BA2")

    Jump("loc_6F3E")

    label("loc_6BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6DC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6C50")

    ChrTalk(
        0xB,
        (
            "You can use your IBC accounts to withdraw mira\x01",
            "at any of our branches across the continent.\x01",
            "Pretty nifty, right? You should try it sometime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DBC")

    label("loc_6C50")


    ChrTalk(
        0xB,
        "*click* *clack* *clack* *click*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 300)

    ChrTalk(
        0xB,
        (
            "Hello, my dear customers.\x01",
            "Are you here to open an account?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You can use your IBC accounts to withdraw mira\x01",
            "at any of our branches across the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You can also use your accounts at\x01",
            "any of our partnered banks. It is\x01",
            "rather convenient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I highly recommend this service.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    ClearChrFlags(0xB, 0x10)

    label("loc_6DBC")

    Jump("loc_6F3E")

    label("loc_6DC1")

    OP_4B(0xF, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6EA8")
    TurnDirection(0xF, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xF,
        (
            "Oh, I'm sorry. I'm still going through\x01",
            "the process.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm terribly sorry about this, but could you\x01",
            "wait over by that sofa to your right? Thanks!\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    OP_9E(0xF, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_6F36")

    label("loc_6EA8")


    ChrTalk(
        0xB,
        (
            "Wait just a second, please.\x01",
            "*click* *click* *clack*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Okay, great! I can verify your account\x01",
            "for you now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Oh, yes. Please do.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_6F36")

    OP_4C(0xF, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_6F3E")

    TalkEnd(0xB)
    Return()

    # Function_10_58C7 end

    def Function_11_6F42(): pass

    label("Function_11_6F42")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6FD6")
    Jump("loc_7020")

    label("loc_6FD6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6FF6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7020")

    label("loc_6FF6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7016")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7020")

    label("loc_7016")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7020")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_70BC")

    ChrTalk(
        0xFE,
        (
            "I don't believe this!\x01",
            "I've never heard of such a thing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you trying to insult me?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7180")

    label("loc_70BC")


    ChrTalk(
        0xFE,
        (
            "What the hell?! A temporary suspension\x01",
            "of the Crossbell Times?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Unbelievable! I am outraged!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I look forward to reading through the column\x01",
            "in the economics section in every issue!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7180")

    Jump("loc_83F0")

    label("loc_7185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_72ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_723F")

    ChrTalk(
        0xFE,
        (
            "If it's investments you've come to talk about,\x01",
            "then leave it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been successfully predicting the market\x01",
            "non-stop ever since the festival ended!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72E8")

    label("loc_723F")


    ChrTalk(
        0xFE,
        "Hahaha! MORE PROFITS!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've wiped out all of the losses I accumulated\x01",
            "during the Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahahahahaha!\x01",
            "I love investments! They're great!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_72E8")

    Jump("loc_83F0")

    label("loc_72ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_747B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7386")

    ChrTalk(
        0xFE,
        (
            "This is most regrettable. I'm stuck working\x01",
            "during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The heavy losses I've suffered have\x01",
            "been catastrophic!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7476")

    label("loc_7386")

    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "That's it! I've finally figured out why\x01",
            "all my investments keep bombing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It must be because I've neglected going out\x01",
            "and enjoying the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, where would be a good place\x01",
            "to have some fun?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7476")

    Jump("loc_83F0")

    label("loc_747B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_75AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7524")

    ChrTalk(
        0xFE,
        (
            "How the hell are there already three\x01",
            "less zeroes?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There HAS to be a mistake! Was there\x01",
            "an error in my judgment?\x01",
            "*angrily rubbing head*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75A8")

    label("loc_7524")


    ChrTalk(
        0xFE,
        (
            "Absolutely preposterous. This shouldn't\x01",
            "be happening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*angrily rubbing head*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Was there an error in my judgment?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_75A8")

    Jump("loc_83F0")

    label("loc_75AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_762D")

    ChrTalk(
        0xFE,
        "I absolutely need to earn a profit today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What am I supposed to do?\x01",
            "Only a third of my assets remain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83F0")

    label("loc_762D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_77A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_769C")

    ChrTalk(
        0xFE,
        (
            "Argh... The prices are fluctuating too violently\x01",
            "to predict. What a predicament...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77A2")

    label("loc_769C")


    ChrTalk(
        0xFE,
        (
            "Stock prices may have skyrocketed\x01",
            "during the Anniversary Festival...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it has become much more complicated\x01",
            "to find the right stock to invest in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahem! Essentially, what I'm trying to say is...\x01",
            "There's nothing I could have done about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_77A2")

    Jump("loc_83F0")

    label("loc_77A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_78C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_77EB")

    ChrTalk(
        0xFE,
        "These damn tourists get on my nerves...\x02",
    )

    CloseMessageWindow()
    Jump("loc_78BF")

    label("loc_77EB")


    ChrTalk(
        0xFE,
        (
            "Oh, for crying out... Are the lot of you also\x01",
            "tourists here to withdraw more mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're all failures! Learn how to manage\x01",
            "your assets and equip yourselves with\x01",
            "the proper amount of spending money!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_78BF")

    Jump("loc_83F0")

    label("loc_78C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_796A")

    ChrTalk(
        0xFE,
        (
            "Can somebody PLEASE tell me why the\x01",
            "terminals aren't working?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What am I going to do if I end up losing\x01",
            "more money because of this?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A29")

    label("loc_796A")


    ChrTalk(
        0xFE,
        (
            "The receptionist told me that my financial\x01",
            "summary will be delayed due to the\x01",
            "terminal breakdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have a bad feeling about this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Who is responsible for this tomfoolery?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7A29")

    Jump("loc_83F0")

    label("loc_7A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7B05")

    ChrTalk(
        0xFE,
        (
            "The most important part of investing is to cultivate\x01",
            "your senses at a young age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe that investing and financial analysis\x01",
            "should be adopted into the Sunday School\x01",
            "curriculum.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB3")

    label("loc_7B05")


    ChrTalk(
        0xFE,
        (
            "Oh, do you lot have business to\x01",
            "attend to here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You are quite admirable for your age.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That being said, have you considered honing\x01",
            "your financial intuition?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7BB3")

    Jump("loc_83F0")

    label("loc_7BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7C25")

    ChrTalk(
        0xFE,
        "It's not that surprising, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've always been a pro at managing\x01",
            "assets!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CFE")

    label("loc_7C25")


    ChrTalk(
        0xFE,
        (
            "I'm the owner of a trading company that\x01",
            "sells goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Investing is something I just do in my\x01",
            "spare time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It definitely helps bring in some extra\x01",
            "mira. I earned an extra cool million\x01",
            "last month alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7CFE")

    Jump("loc_83F0")

    label("loc_7D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7ED7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7DE6")

    ChrTalk(
        0xFE,
        (
            "There is no festival greater than the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My investment senses are tingling... The insane\x01",
            "amounts of foreign mira that enters our economy\x01",
            "thanks to tourists cannot be ignored.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7ED2")

    label("loc_7DE6")


    ChrTalk(
        0xFE,
        "All right, let's check out today's economics section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hah. I anticipated that the stock market would\x01",
            "be more volatile during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the most opportune time for solo\x01",
            "investors like myself to take part.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7ED2")

    Jump("loc_83F0")

    label("loc_7ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_80E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7FC1")

    ChrTalk(
        0xFE,
        (
            "The IBC has always acted as an international\x01",
            "bank, even dating back to its rise to power\x01",
            "towards the end of the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've had the occasional setback, but\x01",
            "they continue to thrive these days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80E2")

    label("loc_7FC1")


    ChrTalk(
        0xFE,
        (
            "The IBC has been accumulating the\x01",
            "latest and greatest orbal technology\x01",
            "for many years now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The truth is, the IBC has been around for ages.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Supposedly it was founded about 300 years\x01",
            "ago--towards the end of the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They certainly have a long-running history.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_80E2")

    Jump("loc_83F0")

    label("loc_80E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_828E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_815D")

    ChrTalk(
        0xFE,
        (
            "Far too many people in Crossbell refuse\x01",
            "to open their minds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It truly is a shame.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8289")

    label("loc_815D")


    ChrTalk(
        0xFE,
        (
            "Crossbell has managed to remain prosperous\x01",
            "through its entire history by engaging in trade\x01",
            "and exchanging septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, their older methods are no longer\x01",
            "valid with the rise of orbal technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The age of financial investments has begun!\x01",
            "Don't waste my time with any small deals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8289")

    Jump("loc_83F0")

    label("loc_828E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8310")

    ChrTalk(
        0xFE,
        "Oh, do you have business with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please keep it down if you don't.\x01",
            "You're bothering the other customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83F0")

    label("loc_8310")


    ChrTalk(
        0xFE,
        "Let's see what the economics section has to say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, interesting. The IBC is offering a new\x01",
            "service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm willing to wager that their stocks will rise\x01",
            "because of this. I'd better check on it, pronto!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)

    label("loc_83F0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_6F42 end

    def Function_12_83F8(): pass

    label("Function_12_83F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 3)), scpexpr(EXPR_END)), "loc_8559")

    ChrTalk(
        0xFE,
        (
            "With that settled, we'll continue to\x01",
            "wire your foundation stipend via\x01",
            "the IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I understand where you're\x01",
            "coming from, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll someday have to decide how you'll\x01",
            "use it. Will you keep it, or will you return\x01",
            "all of it back to the foundation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FI understand. I will continue to think about it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_896B")

    label("loc_8559")


    ChrTalk(
        0xFE,
        "Whoa!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "H-Hello there, Tio. Do you have business\x01",
            "at the IBC?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FNo, not particularly.\x02\x03",
            "#0205FWhat might you be engaged in, Chief?\x01",
            "(His behavior is oddly suspicious...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "I-I'm just making a payment. Don't mind me!\x02",
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
        0xFE,
        (
            "The Epstein Foundation has been handling\x01",
            "your living expenses for now, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You've never bothered to spend any of it, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI receive a more than adequate salary from\x01",
            "the CPD.\x02\x03",
            "#0208FFurthermore, I wish to live by my own means\x01",
            "with the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FTio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "R-Right. That makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How very much like you, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, I understand. I'll cease my\x01",
            "meddling for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, uh, Tio... Are you upset with me right\x01",
            "now by any chance?\x02",
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
        0x103,
        (
            "#0211FYou have a penchant to make me\x01",
            "irrationally upset, Chief.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 3)
    ClearChrFlags(0xE, 0x10)

    label("loc_896B")

    Jump("loc_8D20")

    label("loc_8970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8BA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_898B")
    Call(0, 15)
    Jump("loc_8BA4")

    label("loc_898B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AFE")

    ChrTalk(
        0xFE,
        (
            "Even though it's theoretically possible,\x01",
            "its operational capacity can't keep up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It still suffers from limitations, despite using\x01",
            "the top of the line equipment made by\x01",
            "the Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(They're discussing something far\x01",
            "beyond my comprehension.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(Well, he is the most knowledgeable\x01",
            "specialist in all of Crossbell.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8BA4")

    label("loc_8AFE")


    ChrTalk(
        0xFE,
        (
            "Even though it's theoretically possible,\x01",
            "its operational capacity can't keep up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't discount the possibility that\x01",
            "the algorithm could evolve, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BA4")

    Jump("loc_8D20")

    label("loc_8BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BBB")
    Call(0, 15)
    Jump("loc_8D20")

    label("loc_8BBB")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        "G-Good luck with your work, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, please...show up at the branch\x01",
            "office every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about you. You hardly\x01",
            "ever report in, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FYou need not concern yourself with me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "I-I knew it. She hates me.\x02",
    )

    CloseMessageWindow()

    label("loc_8D20")

    TalkEnd(0xFE)
    Return()

    # Function_12_83F8 end

    def Function_13_8D24(): pass

    label("Function_13_8D24")

    EventBegin(0x1)
    Sound(160, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_8D7C():
        OP_92(0x101, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D7C)
    Sleep(50)

    def lambda_8D92():
        OP_92(0x102, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D92)
    Sleep(50)

    def lambda_8DA8():
        OP_92(0x103, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8DA8)
    Sleep(50)

    def lambda_8DBE():
        OP_92(0x104, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8DBE)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    EventBegin(0x0)
    Fade(500)
    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(9500, 1500, 16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0xE, 11000, 0, 16500, 270)
    SetChrPos(0xD, 11500, 0, 15600, 270)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_68(5750, 1500, 17850, 4000)
    MoveCamera(44, 15, 0, 4000)
    BeginChrThread(0xE, 3, 0, 14)

    NpcTalk(
        0xE,
        "Elderly Man",
        "Yep, it's been doing a good job.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Researcher",
        "Thanks again.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Researcher",
        "You've been a great help, Chief.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Researcher",
        (
            "This kind of algorithm is especially\x01",
            "challenging.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 1900, 9000, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 250, 300, 7750, 45)
    SetChrPos(0x102, 600, 300, 9100, 45)
    SetChrPos(0x104, -350, 300, 8750, 45)
    SetChrPos(0x103, 0, 300, 10150, 45)
    OP_0D()

    ChrTalk(
        0x103,
        "#0205F(Is that...?)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0xE, 3)
    SetChrPos(0x0, 0, 300, 7750, 0)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x6F, 4)
    EventEnd(0x5)
    Return()

    # Function_13_8D24 end

    def Function_14_9024(): pass

    label("Function_14_9024")


    def lambda_9029():
        OP_97(0xE, 0xFFFFEE6C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9029)

    def lambda_9043():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_9043)
    Sleep(50)

    def lambda_9057():
        OP_97(0xD, 0xFFFFE69C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9057)

    def lambda_9071():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_9071)
    Sleep(1250)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0xE, 1)

    def lambda_909E():
        OP_97(0xE, 0x0, 0x0, 0x546, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_909E)
    WaitChrThread(0xE, 1)

    def lambda_90BC():
        OP_93(0xE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_90BC)
    WaitChrThread(0xD, 1)

    def lambda_90CD():
        OP_97(0xD, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_90CD)
    WaitChrThread(0xD, 1)

    def lambda_90EB():
        OP_93(0xD, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_90EB)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xD, 1)
    Return()

    # Function_14_9024 end

    def Function_15_90FC(): pass

    label("Function_15_90FC")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(6500, 1200, 17000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x103, 6500, 0, 16350, 0)
    SetChrPos(0x102, 5900, 0, 15150, 0)
    SetChrPos(0x101, 7100, 0, 15350, 0)
    SetChrPos(0x104, 6500, 0, 14150, 0)
    OP_93(0xE, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0205FI have not seen you in some time, Chief.\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "I recognize that voice...!\x02",
    )

    CloseMessageWindow()

    def lambda_91F3():
        TurnDirection(0xD, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_91F3)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0xE, 0x103, 500)

    ChrTalk(
        0xE,
        "O-Oh, well if it isn't Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "H-How are you doing these days?\x02",
    )

    CloseMessageWindow()
    OP_64(0xE)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#0000F'Chief'? Is this man your boss?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#0203FThat is correct. He is my direct boss and the\x01",
            "chief of the orbal staff's development team.\x02\x03",
            "#0200FHe specializes in orbal networks, and acts as the\x01",
            "head of the Epstein Foundation's Crossbell branch.\x02\x03",
            "I suppose you could call him my supervisor.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_939D():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_939D)
    Sleep(50)
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0xE,
        (
            "Everything appears to be running smoothly\x01",
            "at that new division of the CPD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I'm quite relieved to see you doing well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "But why don't you ever come by to deliver\x01",
            "reports, Tio? I'm really worried about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205FIs that the official explanation behind your\x01",
            "'gracious' delivery of an orbal staff to the\x01",
            "weapons shop for me?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou know, now that I think about it...\x01",
            "Wendy mentioned that somebody from the\x01",
            "foundation drops by pretty frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "*gulp*\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "W-Well, you see. There's a perfectly\x01",
            "reasonable explanation for that...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    ChrTalk(
        0xE,
        (
            "A-Ah, crap. This is bad. Tio is\x01",
            "definitely mad at me now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "B-But, how can she expect me to leave a\x01",
            "child like her to her own devices in a city\x01",
            "like this? *grumble* *mumble*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FYour behavior is suspicious, Chief.\x02",
    )

    CloseMessageWindow()
    OP_9C(0xE, 0x0, 0x0, 0x0, 0x190, 0x2EE0)

    ChrTalk(
        0xE,
        "Wh-What?! What could you possibly mean?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xE, 0x103, 500)

    ChrTalk(
        0x103,
        (
            "#0206F*sigh*...\x02\x03",
            "#0205FPlease refrain from secretly leaving\x01",
            "new equipment for me at different\x01",
            "locations.\x02\x03",
            "I would rather not participate in\x01",
            "a scavenger hunt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "H-Haha... Okay, Tio. I-I understand,\x01",
            "and I'm terribly sorry, okay?\x01",
            "Please, don't be upset with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211FIt is precisely your behavior at times\x01",
            "like this that upsets me, Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*gulp* *sweat* H-Haha...\x01",
            "You're right. I get it now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0106F(Aren't you being too harsh, Tio?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(I am unable to help it. I am irritated\x01",
            "beyond comprehension.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 6500, 0, 16350, 0)
    OP_93(0xD, 0x5A, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x6C, 5)
    EventEnd(0x5)
    Return()

    # Function_15_90FC end

    def Function_16_99F5(): pass

    label("Function_16_99F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9A3C")

    ChrTalk(
        0xFE,
        "I-I see... It requires more research, I take it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A7C")

    label("loc_9A3C")


    ChrTalk(
        0xFE,
        (
            "Hmm, I see. I see. I can always trust\x01",
            "the chief's opinion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A7C")

    TalkEnd(0xFE)
    Return()

    # Function_16_99F5 end

    def Function_17_9A80(): pass

    label("Function_17_9A80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9BEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B97")

    ChrTalk(
        0xFE,
        (
            "We received a request from one of the\x01",
            "companies within the building today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing that can calm me down\x01",
            "in a place filled with all of these\x01",
            "high-tech gadgets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(High-tech...? His mannerisms\x01",
            "remind me of an elderly man.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9BEA")

    label("loc_9B97")


    ChrTalk(
        0xFE,
        "I wonder what floor the client is on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe I'll ask the receptionist.\x02",
    )

    CloseMessageWindow()

    label("loc_9BEA")

    TalkEnd(0xFE)
    Return()

    # Function_17_9A80 end

    def Function_18_9BEE(): pass

    label("Function_18_9BEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CCC")

    ChrTalk(
        0xFE,
        (
            "Supposedly, there are people who make\x01",
            "a living entirely off of trading stocks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can you really feel accomplished\x01",
            "by earning mira like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a world beyond my comprehension.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9D51")

    label("loc_9CCC")


    ChrTalk(
        0xFE,
        (
            "Or maybe...they get their thrills by\x01",
            "gambling on the stock market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless, it's still a world beyond\x01",
            "my comprehension.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D51")

    TalkEnd(0xFE)
    Return()

    # Function_18_9BEE end

    def Function_19_9D55(): pass

    label("Function_19_9D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9F81")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DF2")
    Jump("loc_9E3C")

    label("loc_9DF2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E12")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E3C")

    label("loc_9E12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E32")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E3C")

    label("loc_9E32")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E3C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9EEF")

    ChrTalk(
        0xFE,
        "I'm here to make a deposit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The IBC's investments yield the best interest\x01",
            "rates, so most Crossbellans bank with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F75")

    label("loc_9EEF")


    ChrTalk(
        0xFE,
        (
            "I'm thinking about making a large purchase\x01",
            "for my grandkid's birthday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One, two, three... Yep, I've got the\x01",
            "full amount.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_9F75")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_9F8A")

    label("loc_9F81")

    TalkBegin(0xFE)
    Call(0, 10)
    TalkEnd(0xFE)

    label("loc_9F8A")

    Return()

    # Function_19_9D55 end

    def Function_20_9F8B(): pass

    label("Function_20_9F8B")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(1000)
    OP_68(0, 1300, 30100, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A50D")

    ChrTalk(
        0xA,
        (
            "#2200277V#5PHello, and welcome to the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200294V#5PIt's good to see you again, Miss MacDowell.\x01",
            "I see you've brought your SSS companions, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200279V#5PThank you for helping us test our\x01",
            "new service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200280V#5PIt couldn't have reached its current\x01",
            "popularity without your efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200281V#0002F#12PReally? That's good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200282V#12P#0202FI am glad we were able to assist you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200283V#5PLikewise. We'll be sure to rely on\x01",
            "your help again when the time comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200284V#5PAnyway, how may I help you today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200285V#0001F#12PWell, actually...\x02",
    )

    CloseMessageWindow()

    def lambda_A292():
        OP_96(0xFE, 0xFFFFFDA8, 0x12C, 0x7274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A292)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#2200286V#6P#0104FThere's something I'd like to ask you, Lanfei.\x02\x03",
            "#2200309V#0100FWould it be possible to see Mr. Crois?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#2200300V#5POh? You're not here to see Miss Crois?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200312V#6P#0103FIndeed. I must apologize for our lack of\x01",
            "an appointment, however.\x02\x03",
            "#2200313V#0101FBut even so, I'd still like to meet with him.\x01",
            "Or is he too busy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200314V#5PNo, he should be in his office right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200304V#5PWill your companions be joining you\x01",
            "for the meeting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200305V#6P#0102FThey will be. We'd like to ask him a few\x01",
            "questions regarding a certain incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC63")

    label("loc_A50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_END)), "loc_A8D7")

    ChrTalk(
        0xA,
        (
            "#2200277V#5PHello, and welcome to the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200278V#5PIt's good to see you again, Miss MacDowell.\x01",
            "I see you've brought your SSS companions, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200306V#5PHow may we help you today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200296V#12P#0012FOh, hello. It's good to see you, too.\x02\x03",
            "#2200297V#0001FWell, actually...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A65F():
        OP_96(0xFE, 0xFFFFFDA8, 0x12C, 0x7274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A65F)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#2200298V#6P#0104FGood morning, Lanfei. There's\x01",
            "something I'd like to ask you.\x02\x03",
            "#2200299V#0100FIs Mr. Crois in today?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#2200288V#5POh? You're not here to see Miss Crois?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200301V#6P#0104FIndeed. We haven't scheduled an\x01",
            "appointment, though, so I apologize.\x02\x03",
            "#2200302V#0101FBut even so, I'd still like to meet with him.\x01",
            "Or is he absent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200303V#5PActually, he's in his office right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200292V#5PWill your companions be joining you\x01",
            "for the meeting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200293V#6P#0102FThey will be. We'd like to ask him a few\x01",
            "questions regarding a certain incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC63")

    label("loc_A8D7")


    ChrTalk(
        0xA,
        (
            "#2200277V#5PHello, and welcome to the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200295V#5PHow may we help you today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200307V#0001F#12PUhh...\x02",
    )

    CloseMessageWindow()

    def lambda_A973():
        OP_96(0xFE, 0xFFFFFDA8, 0x12C, 0x7274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A973)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#2200308V#6P#0104FGood morning, Lanfei. There's\x02\x03",
            "#2200287V#0100Fsomething I'd like to ask you.\x01",
            "Is Mr. Crois in today?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#2200310V#5POh, Miss MacDowell! It's good to\x01",
            "see you again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200311V#5POh? You're not here to see Miss Crois?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200289V#6P#0103FIndeed. We haven't scheduled an\x01",
            "appointment, though, so I apologize.\x02\x03",
            "#2200290V#0101FBut even so, I'd still like to meet with him.\x01",
            "Or is he absent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200291V#5PActually, he's in his office right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200315V#5PMy apologies for being rude, but who are\x01",
            "the people accompanying you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200316V#6P#0102FOh, these are my coworkers from the CPD.\x02\x03",
            "#2200317VWe'd like to ask Mr. Crois a few questions\x01",
            "regarding a certain incident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC63")


    ChrTalk(
        0xA,
        "#2200318V#5POh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200319V#5PUnderstood. Please wait while I\x01",
            "notify him of your arrival.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xA, 0x258, 0x7D00, 0x190)

    def lambda_ACDF():
        OP_95(0xFE, 600, 300, 32000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_ACDF)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x190)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#2200320V#12P#0302F(Leave it up to Mademois-Elie to crash\x01",
            "the CEO's party like it's nothin'.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_END)), "loc_ADC6")

    ChrTalk(
        0x101,
        (
            "#2200321V#0002F(Seriously... It's like she's from a totally\x01",
            "different world.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE23")

    label("loc_ADC6")


    ChrTalk(
        0x101,
        (
            "#2200322V#0012F(Yeah, it definitely feels like we're from\x01",
            "a different planet from her.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE23")


    ChrTalk(
        0xA,
        "#2200323V#5PYes... Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200324V#5PUnderstood. I'll send them in.\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x190)

    def lambda_AE7F():
        OP_95(0xFE, 0, 300, 31700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AE7F)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x190)

    ChrTalk(
        0xA,
        (
            "#2200325V#5PMr. Crois will meet with you now,\x01",
            "Miss MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200326V#5PI'll issue you a key card for the elevator.\x01",
            "His office is on the top floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200327V#6P#0109FExcellent. Thank you, Lanfei.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x320),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x320, 1)
    OP_93(0x102, 0xB4, 0x1F4)

    ChrTalk(
        0x102,
        "#2200328V#0100F#5PShall we board the elevator, then?\x02",
    )

    CloseMessageWindow()

    def lambda_B006():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B006)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_END)), "loc_B0E8")

    ChrTalk(
        0x101,
        (
            "#2200329V#0002FSounds like a plan... I have to say, you\x01",
            "really pulled through back there, Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200330V#0300FWell, let's head on up and have a nice\x01",
            "little chat with Mr. CEO himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B15E")

    label("loc_B0E8")


    ChrTalk(
        0x101,
        "#2200331V#0002FY-Yeah, let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200332V#0300FWell, let's head on up there and\x01",
            "chat with Mr. CEO himself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B15E")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 300, 28800, 180)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x82, 2)
    OP_29(0x43, 0x1, 0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_20_9F8B end

    def Function_21_B187(): pass

    label("Function_21_B187")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(1000)
    OP_68(0, 1000, 30100, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8CA")

    ChrTalk(
        0xA,
        (
            "#5PHello, and welcome to the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xA,
        "#5POh, now this is a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt's been quite some time, hasn't\x01",
            "it, Miss MacDowell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0005F(Huh?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0205F(Are you acquainted, Elie?)\x02",
    )

    CloseMessageWindow()

    def lambda_B30F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B30F)

    def lambda_B31C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B31C)

    def lambda_B329():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B329)
    Sleep(300)

    ChrTalk(
        0x102,
        "#12P#0100FHello, Lanfei. Indeed, it has been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThis is our first encounter ever since you\x01",
            "returned from your studies abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POh, yes. That reminds me. Would you like\x01",
            "me to inform the miss of your arrival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PShe's currently overseeing Mishelam's\x01",
            "operations, but I'm sure she'd rush back\x01",
            "if I told her you were visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0104FI'm glad to see that Bell's still keeping\x01",
            "herself busy.\x02\x03",
            "#0100FThat's okay, though. I'm not here to discuss\x01",
            "anything important with her today.\x02\x03",
            "I'll visit her another day when I have the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PIs that so? I'll send her your regards, then.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_B5A3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5A3)

    def lambda_B5B0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B5B0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#0305F(Didn't know you had connections within\x01",
            "the IBC, Mademois-Elie.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0005F(Yeah, you seemed pretty close to\x01",
            "each other, too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#203F(She continues to uphold her\x01",
            "image of a noble lady.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#0113FI can hear you, you know.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#0100FAren't we here to get work done, Lloyd?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#11P#0012FO-Oh, yeah. You're right, we are.\x01",
            "(Whoops, totally forgot about that.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B77D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B77D)

    def lambda_B78A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B78A)

    def lambda_B797():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B797)

    def lambda_B7A4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B7A4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#0000FPlease, allow me to introduce ourselves.\x01",
            "We're members of the CPD's Special\x01",
            "Support Section.\x02\x03",
            "I believe we received a request from\x01",
            "the IBC for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5POh, is that what this is all about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PMy apologies. I'll explain the details\x01",
            "to you immediately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 4)
    Jump("loc_BA7F")

    label("loc_B8CA")


    ChrTalk(
        0xA,
        (
            "#5PHello, and welcome to the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#5PAh, you've brought your SSS friends with you,\x01",
            "Miss MacDowell. It's good to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FWe saw your request and came to\x01",
            "help, Lanfei.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FI think the request mentioned needing\x01",
            "us to do something for the IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5POh, is that what this is all about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PMy apologies, I'll explain the details\x01",
            "to you immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA7F")


    ChrTalk(
        0x102,
        "#12P#0100FGreat, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYou may have read about it in the\x01",
            "finance section already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThe IBC will soon be offering a new service\x01",
            "to exchange sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PEssentially, our service will allow patrons\x01",
            "to exchange sepith at a higher rate than\x01",
            "the average market value.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FSo, you're offerin' to cough up more dough\x01",
            "than your everyday shop? I gotta hand it\x01",
            "to ya, that's pretty nifty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FThe service's purpose is to amass\x01",
            "a large reservoir of sepith, due to\x01",
            "the scarcity of natural septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0204FThe IBC is unparalleled when it comes to\x01",
            "designing simple, yet effective services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PYou flatter us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHowever, to counteract theft and sepith\x01",
            "counterfeiting, we've limited the service\x01",
            "to IBC members for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWe're trying to expand the service to be\x01",
            "able to store sepith in our terminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWe'd like for you to participate in the\x01",
            "beta testing of the service, hence\x01",
            "the request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FSounds good. What exactly do we\x01",
            "need to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PGreat! First things first, please take\x01",
            "this card with you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x35B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x35B, 1)

    ChrTalk(
        0xA,
        (
            "#5PI'll guide you through it, so please follow\x01",
            "my instructions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PJust so you know, you'll need to exchange\x01",
            "a specific amount of sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThirty of each type of sepith\x01",
            "should be sufficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0002FThirty of each type. Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0309FSounds cool. Let's give it a spin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0104FOh, by the way. There's no requirement\x01",
            "to deposit them all at the same time.\x02\x03",
            "#0100FWe can deposit small portions of it while\x01",
            "we take a break from other requests.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Assistance With New Service]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You are now able to utilize the\x01",
            "IBC's exchange service.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Speak with Lanfei and select\x01",
            "'Exchange,' then 'EXCHANGE'\x01",
            "to perform an exchange.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 300, 28800, 0)
    OP_4C(0xA, 0xFF)
    Sleep(500)
    OP_29(0x7, 0x1, 0x0)
    ClearScenarioFlags(0x49, 2)
    EventEnd(0x5)
    Return()

    # Function_21_B187 end

    def Function_22_C21C(): pass

    label("Function_22_C21C")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(1000)
    OP_68(0, 1000, 30100, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()

    ChrTalk(
        0xA,
        "#5POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt appears you've managed to exchange\x01",
            "thirty of each sepith type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PJust one moment, please.\x02",
    )

    CloseMessageWindow()
    OP_92(0xA, 0x258, 0x7D00, 0x190)

    def lambda_C323():
        OP_95(0xFE, 600, 300, 32000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C323)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x190)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#5PHello, this is the reception desk...\x01",
            "I'd like to convert thirty of each\x01",
            "type of sepith into mira, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PRight, right... Okay, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PYes, understood.\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x190)

    def lambda_C402():
        OP_95(0xFE, 0, 300, 31700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C402)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x190)

    ChrTalk(
        0xA,
        (
            "#5PI've confirmed the transaction with our\x01",
            "employees at the exchange terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThere was an incident where an employee\x01",
            "confused earth and space sepith, but the\x01",
            "transaction was reversed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHere's hoping things will run\x01",
            "smoothly from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FHaha. I'm guessin' they've got a bit\x01",
            "of that hands-on experience now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0104FI'm glad we were able to be of\x01",
            "service to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5POh, of course! You've been an immense help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt's not much, but please take this as\x01",
            "a token of our appreciation.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1F5, 3)
    AddItemNumber(0x1FB, 2)
    AddItemNumber(0x1F8, 2)

    ChrTalk(
        0x103,
        "#12P#0205FA rather generous reward.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PBut that's not all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYou can keep using the VIP card\x01",
            "I gave you earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYou're our special guests, so you may\x01",
            "continue to use our exchange service\x01",
            "as you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PPlease consider it as another token of\x01",
            "our appreciation.\x02",
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
        0x101,
        (
            "#11P#0011FAre you sure about this? Isn't this\x01",
            "too much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FAin't this supposed to be a service meant\x01",
            "for IBC members only?\x02\x03",
            "#0309FYou tellin' me we're getting these awesome\x01",
            "perks all thanks to Mademois-Elie here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0109FAhahaha... I highly doubt that's the reason why.\x02\x03",
            "#0105F...Lanfei. You're not giving us special treatment\x01",
            "because of our relationship, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5POf course not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PPlease visit again if there's anything\x01",
            "I can assist you with in the future.\x02",
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
            "[Assistance With New Service]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 300, 28800, 180)
    OP_4C(0xA, 0xFF)
    OP_29(0x7, 0x4, 0x10)
    OP_29(0x7, 0x1, 0x1)
    SetScenarioFlags(0x1, 1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_22_C21C end

    def Function_23_CAE3(): pass

    label("Function_23_CAE3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(220, 5800, 11750, 0)
    MoveCamera(16, 14, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 700, 300, 1650, 0)
    SetChrPos(0x102, -700, 300, 1650, 0)
    SetChrPos(0x103, -700, 300, 0, 0)
    SetChrPos(0x104, 700, 300, 0, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0x9, 0x8000)

    def lambda_CB7A():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_CB7A)

    def lambda_CB8F():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_CB8F)

    def lambda_CBA4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_CBA4)

    def lambda_CBB9():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_CBB9)
    OP_68(220, 1800, 11750, 4000)
    MoveCamera(16, 10, 0, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x3, 1)
    Sleep(300)
    Fade(800)
    OP_68(-90, 1800, 6110, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(16850, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#0000FAll right, we made it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300FAlways feels like they're runnin' a huge-ass\x01",
            "facility when we come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FI presume the representative's runaway\x01",
            "daughter may have stopped here.\x02\x03",
            "Shall we inquire with the receptionist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FYes, let's ask Lanfei to see if she\x01",
            "knows anything about it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 300, 4570, 0)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    OP_29(0x2D, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_23_CAE3 end

    def Function_24_CDA2(): pass

    label("Function_24_CDA2")

    EventBegin(0x0)
    Fade(800)
    OP_4B(0xA, 0xFF)
    OP_68(0, 1200, 30100, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#5PHi again, Miss MacDowell.\x01",
            "Do you need help with anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FHi, Lanfei. I'm just here to ask you\x01",
            "a quick question.\x02\x03",
            "Did a lady by the name of Carla\x01",
            "stop by here today?\x02\x03",
            "#0103FI think she may have been here\x01",
            "with a maid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POh, I do seem to remember Carla\x01",
            "coming by earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PShe told me she had urgent business\x01",
            "to discuss with Miss Crois.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        "#12P#0105FWith Bell...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PMiss Crois consented to it, so I\x01",
            "directed her to the top floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PThis all happened about an hour ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FDo you mind if we go and ask Mariabell\x01",
            "for some details?\x02\x03",
            "#0001FTruth be told, we're conducting an investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POh, yes. I think you should be okay\x01",
            "to talk with her right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI believe she's currently in the\x01",
            "CEO's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FAll right, let's get crackin'.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -370, 300, 28210, 180)
    OP_4C(0xA, 0xFF)
    OP_29(0x2D, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_24_CDA2 end

    def Function_25_D1E0(): pass

    label("Function_25_D1E0")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "Um, excuse me. Only staff members are\x01",
            "permitted to go beyond here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Entry is prohibited to those without\x01",
            "authorization.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_25_D1E0 end

    SaveToFile()

Try(main)
