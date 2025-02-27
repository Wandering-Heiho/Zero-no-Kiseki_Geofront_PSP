from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1440.bin",                # FileName
        "c1440",                    # MapName
        "c1440",                    # Location
        0x0031,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 49, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1440",                  # 0
        "Ashleigh",               # 1
        "Jingo",                  # 2
        "Sister Hatina",          # 3
        "Bracer Lynn",            # 4
        "Bracer Aeolia",          # 5
        "Garcia",                 # 6
    ))

    AddCharChip((
        "chr/ch09200.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch25500.itc",                   # 02
        "chr/ch32000.itc",                   # 03
        "chr/ch32100.itc",                   # 04
    ))

    DeclNpc(-2859,   0,       13750,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(5670,    29,      8649,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2930,    0,       7659,    315,  389,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-2170,   19,      5400,    180,  389,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-2170,   29,      4110,    0,    389,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 17,  9.899999618530273,     14.0,                  -0.5,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.4749999046325684,   -7.0,                  0.10000000149011612,   1.0])

    DeclActor(4590,    0,       7540,    1000,    5670,    1500,    8650,    0x007E, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_21C",          # 00, 0
        "Function_1_2D4",          # 01, 1
        "Function_2_3FE",          # 02, 2
        "Function_3_451",          # 03, 3
        "Function_4_317E",         # 04, 4
        "Function_5_3753",         # 05, 5
        "Function_6_39AF",         # 06, 6
        "Function_7_3C9C",         # 07, 7
        "Function_8_3FD7",         # 08, 8
        "Function_9_4839",         # 09, 9
        "Function_10_483D",        # 0A, 10
        "Function_11_65E6",        # 0B, 11
        "Function_12_6A8D",        # 0C, 12
        "Function_13_70C3",        # 0D, 13
        "Function_14_71E7",        # 0E, 14
        "Function_15_7371",        # 0F, 15
        "Function_16_7613",        # 10, 16
        "Function_17_7E8C",        # 11, 17
    ))


    def Function_0_21C(): pass

    label("Function_0_21C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_25C"),
        (1, "loc_268"),
        (2, "loc_274"),
        (3, "loc_280"),
        (4, "loc_28C"),
        (5, "loc_298"),
        (6, "loc_2A4"),
        (SWITCH_DEFAULT, "loc_2B0"),
    )


    label("loc_25C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_268")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_274")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_280")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_28C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_298")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2D3")

    Return()

    # Function_0_21C end

    def Function_1_2D4(): pass

    label("Function_1_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA")
    Event(0, 16)

    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2F8")
    Jump("loc_3FD")

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_310")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3FD")

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_3FD")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_351")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 1850, 0, 8750, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C")
    SetChrFlags(0x8, 0x10)

    label("loc_34C")

    Jump("loc_3FD")

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_364")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3FD")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_372")
    Jump("loc_3FD")

    label("loc_372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_391")
    SetChrPos(0x8, 1810, 0, 10210, 135)
    Jump("loc_3FD")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_39F")
    Jump("loc_3FD")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3B2")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3FD")

    label("loc_3B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3C0")
    Jump("loc_3FD")

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3EE")
    SetChrPos(0x8, -1940, 30, 10250, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9")
    SetChrFlags(0x8, 0x10)

    label("loc_3E9")

    Jump("loc_3FD")

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD")
    SetChrFlags(0x8, 0x10)

    label("loc_3FD")

    Return()

    # Function_1_2D4 end

    def Function_2_3FE(): pass

    label("Function_2_3FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_417")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_41D")

    label("loc_417")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_439")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_450")

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_450")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_450")

    label("loc_450")

    Return()

    # Function_2_3FE end

    def Function_3_451(): pass

    label("Function_3_451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_674")
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_491")
    Call(0, 7)
    SetScenarioFlags(0x6B, 3)
    Jump("loc_66C")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4A2")
    Call(0, 4)
    Jump("loc_66C")

    label("loc_4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4B6")
    Call(0, 7)
    SetScenarioFlags(0x6B, 3)
    Jump("loc_66C")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_563")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_55B")

    ChrTalk(
        0x8,
        (
            "This sister from the cathedral has been\x01",
            "constantly pestering us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Good grief, what an annoying woman.\x01",
            "I ought to cut her tongue off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E")

    label("loc_55B")

    Call(0, 5)

    label("loc_55E")

    Jump("loc_66C")

    label("loc_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_571")
    Jump("loc_66C")

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_585")
    Call(0, 7)
    SetScenarioFlags(0x6B, 3)
    Jump("loc_66C")

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5F1")

    ChrTalk(
        0x8,
        (
            "I'm going to take inventory and figure out how\x01",
            "badly this theft has hurt my bottom line.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C")

    label("loc_5F1")


    ChrTalk(
        0x8,
        "Oh, for the love of...! New goods again?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, Aidios. It's going to take even longer\x01",
            "to keep track of inventory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66C")

    TalkEnd(0xFE)
    Jump("loc_317D")

    label("loc_674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_68F")
    Call(0, 7)
    Jump("loc_781")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6A0")
    Call(0, 4)
    Jump("loc_781")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6B1")
    Call(0, 7)
    Jump("loc_781")

    label("loc_6B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_75F")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_754")

    ChrTalk(
        0x8,
        (
            "This sister from the cathedral has been\x01",
            "constantly pestering us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What a goddamn annoying woman.\x01",
            "I ought to cut her tongue off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_757")

    label("loc_754")

    Call(0, 5)

    label("loc_757")

    TalkEnd(0xFE)
    Jump("loc_781")

    label("loc_75F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_76D")
    Jump("loc_781")

    label("loc_76D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_77E")
    Call(0, 7)
    Jump("loc_781")

    label("loc_77E")

    Call(0, 8)

    label("loc_781")

    Jump("loc_317D")

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A8")
    Call(0, 6)
    Jump("loc_317D")

    label("loc_7A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_849")

    ChrTalk(
        0x8,
        "You're telling me there was a bomb threat at the airport?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know who was responsible, but\x01",
            "they've sure got some balls.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE")

    label("loc_849")


    ChrTalk(
        0x8,
        "You're telling me there was a bomb threat at the airport?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It'd be a pain in my ass if the airport\x01",
            "went and exploded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I suppose I'll just have to look forward to the VALIANT\x01",
            "efforts of Crossbell's finest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305F(Where does a black market broker\x01",
            "get off saying somethin' like that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(That seemed like obvious sarcasm to me.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_9AE")

    Jump("loc_317A")

    label("loc_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9C4")
    Call(0, 4)
    Jump("loc_317A")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_E84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0B")

    ChrTalk(
        0xFE,
        (
            "My daughter's been longing for one\x01",
            "of those what's-it-called dolls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you guys free right now?\x01",
            "Could you keep her company for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been too busy with work,\x01",
            "so she's been really bored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FM-Maybe some other time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Guess business must be\x01",
            "going pretty well, eh?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 5)
    Jump("loc_E7F")

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BEB")

    ChrTalk(
        0x8,
        (
            "Oh, yeah. I figured Dudley was going to\x01",
            "stop by because of that incident earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Weird. He's usually the first one to start\x01",
            "digging up dirt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(Dudley's restrained at the moment,\x01",
            "isn't he?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7F")

    label("loc_BEB")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005FOh, yeah. That reminds me...\x02\x03",
            "#0001FA-Are you, by any chance, selling\x01",
            "hard drugs through your shop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hard drugs?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, you're probably referring to that blue drug\x01",
            "that releases your inner bliss. Word about that\x01",
            "thing has been spreading all over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Unfortunately, I don't have any in stock.\x01",
            "After all, that stuff's nowhere near my\x01",
            "distribution route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FIs that right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FThat does lend credibility to all of these\x01",
            "rumors we've heard, though, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FY'know what they say. Where there's smoke,\x01",
            "there's fire.\x02\x03",
            "I figure it's probably bein' sold on the\x01",
            "black market by some other dealer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E7F")

    Jump("loc_317A")

    label("loc_E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_11EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F20")

    ChrTalk(
        0x8,
        (
            "Still, though. Poor Garcia must be having\x01",
            "a hard time these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He has a lot more gray hairs ever\x01",
            "since joining Revache.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11EA")

    label("loc_F20")


    ChrTalk(
        0x8,
        "Damn it. Now they've gone and done it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If that Cao guy pulls something crazy,\x01",
            "there'll be riots in the streets.\x02",
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
            "#0003FAre you trying to scare us with a\x01",
            "dramatization?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FKinda nuts you can keep a straight face\x01",
            "while spoutin' a line like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FExcuse me, ma'am. Are you in possession of\x01",
            "any information that may assist us in our\x01",
            "investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well. All I can tell you is that Revache's goons\x01",
            "were behind that raid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm not an information broker, so I don't really give a\x01",
            "flying rat's ass about all that stuff. If you want to\x01",
            "get some info, go talk to them yourselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11EA")

    Jump("loc_317A")

    label("loc_11EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1297")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_128F")

    ChrTalk(
        0x8,
        (
            "This sister from the cathedral has been\x01",
            "constantly pestering us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What a goddamn annoying woman.\x01",
            "I ought to cut her tongue off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1292")

    label("loc_128F")

    Call(0, 5)

    label("loc_1292")

    Jump("loc_317A")

    label("loc_1297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1560")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1344")

    ChrTalk(
        0x8,
        (
            "You guys had better watch your back while you're\x01",
            "out on the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lot of suspicious people claiming to be here\x01",
            "to 'see the festival' today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155B")

    label("loc_1344")


    ChrTalk(
        0x8,
        (
            "I don't like it one bit. My gut's telling me that there's\x01",
            "something real shady going down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Likely 'cause of that whole shindig\x01",
            "Revache has been hyping up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FWhat is this 'shindig' you're referring to?\x01",
            "Are you talking about the Schwarze Auction?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "The heck? You guys know about it, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Think Marconi started hosting that thing\x01",
            "seven or eight years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A bunch more creeps pop out of the woodwork when\x01",
            "it comes around, and it's all thanks to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I don't like it one bit.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_155B")

    Jump("loc_317A")

    label("loc_1560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_167F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15D7")

    ChrTalk(
        0x8,
        (
            "Anyway, I'll have Jingo tend to the store\x01",
            "while I go and grab some drinks over\x01",
            "at Trinity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167A")

    label("loc_15D7")


    ChrTalk(
        0x8,
        "Phew... I'm finally done taking inventory.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*sigh* Work, work, and more work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "These Anniversary Festivals make\x01",
            "taking inventory such a damn pain.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_167A")

    Jump("loc_317A")

    label("loc_167F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_194F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_179B")

    ChrTalk(
        0x8,
        (
            "It's not exactly rare to hear of a bomb threat\x01",
            "in Crossbell, quite frankly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FSeriously? This is the first time I've ever\x01",
            "heard of something like that happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those guys over in the First Division do a\x01",
            "bang-up job suppressing information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_194A")

    label("loc_179B")


    ChrTalk(
        0x8,
        "Today's the parade, yeah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heheh... Come to think of it, it's been,\x01",
            "what, ten years since that incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Some terrorists managed to plant a bomb\x01",
            "in one of the parade floats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Heh. Sure hope nothing bad happens this year.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FAnybody ever tell you how scary you are?\x01",
            "You tryin' to make us piss ourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, the First Division is keeping watch.\x01",
            "I wouldn't worry your pretty little heads over it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_194A")

    Jump("loc_317A")

    label("loc_194F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1BD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19F2")

    ChrTalk(
        0x8,
        (
            "*puff*...\x01",
            "Looks to me like Garcia's having himself\x01",
            "one hell of a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's all because he went and joined\x01",
            "Revache like an idiot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD2")

    label("loc_19F2")

    OP_93(0x8, 0xB4, 0x0)

    ChrTalk(
        0x8,
        (
            "*puff*...\x01",
            "Why's Garcia in such a rush?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I bet he started crying like a little girl when\x01",
            "he found out his routes were shutting down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FYeah, uh...I don't think that'd ever happen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FC'mon, are you seriously doin'\x01",
            "business with that jackass?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I made more than a few deals with him\x01",
            "before he went and joined Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Eh. He's just a longtime customer, is all.\x01",
            "These days, he's been acting a little more\x01",
            "stuck-up than I'd prefer, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BD2")

    Jump("loc_317A")

    label("loc_1BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C57")

    ChrTalk(
        0x8,
        (
            "We've got ourselves one hell of a haul today.\x01",
            "Heheh. Let Jingo know if anything strikes your fancy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7F")

    label("loc_1C57")


    ChrTalk(
        0x8,
        (
            "We got ourselves one hell of a haul today.\x01",
            "We're selling them at a discount, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Business usually gets more lively around the time of\x01",
            "the Anniversary Festival. Not that I'm complaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FConsidering we're officers of the law,\x01",
            "that's not exactly the most thrilling news...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D7F")

    Jump("loc_317A")

    label("loc_1D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_20B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E3A")

    ChrTalk(
        0x8,
        (
            "The guys over in the First Division have their\x01",
            "noses buried deep in some kind of investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Not like it's any of my business,\x01",
            "so what do I care?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20AE")

    label("loc_1E3A")


    ChrTalk(
        0x8,
        "An investigator from the First Division just came by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Sounded like he was sniffing out something big.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FAnd on that note...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FDo you sell any information on\x01",
            "Crossbell's underworld?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Listen up, chump.\x01",
            "I strictly deal in stolen goods. You got that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That being said, I do overhear sensitive info\x01",
            "every once in a while...if you catch my drift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rumors about Revache, Heiyue, any lowlife making\x01",
            "a splash in Crossbell's underworld. You name it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sometimes during negotiations,\x01",
            "a slip of the tongue can betray\x01",
            "a person's secrets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(She must be the First Division's informant.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20AE")

    Jump("loc_317A")

    label("loc_20B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_269B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 7)), scpexpr(EXPR_END)), "loc_230A")

    ChrTalk(
        0x8,
        "Heiyue's Cao is one smooth operator.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh. While his standard operating procedure isn't\x01",
            "exactly the prettiest, I can't argue with the results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If I'm being honest, I'm actually a little interested, too.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2305")

    ChrTalk(
        0x102,
        (
            "#0101FE-Excuse me. Could we humbly request you to\x01",
            "stop arming both parties involved?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heheh... Now, I definitely can't promise you that,\x01",
            "but they no longer need my services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Let's face it, both groups are already\x01",
            "armed to the teeth.\x02",
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
    SetScenarioFlags(0x0, 0)

    label("loc_2305")

    Jump("loc_2696")

    label("loc_230A")


    ChrTalk(
        0x8,
        "Cao's fascinating advance has just begun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's already doing a marvelous job of\x01",
            "destroying his opponents, right?\x02",
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
            "#0005FCao? That name sounds like it's...\x02\x03",
            "Oh, is that the name of Heiyue's boss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, it is. I haven't really met him, either,\x01",
            "just so you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's the branch manager of Heiyue's Crossbell outfit.\x01",
            "He's supposedly cunning enough to handle any problem\x01",
            "on his own. Be it internally or externally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I imagine they're planning their attack, now that\x01",
            "they've gained a foothold in Crossbell.\x01",
            "A method fit for the mafia, I'd say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FIs that related to the uptick in crimes\x01",
            "being reported around the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FY'know, I kinda had the feelin' that this month's\x01",
            "been especially heavy on the crimes...\x02\x03",
            "#0301FFigures that somethin' behind the scenes\x01",
            "is pullin' all the strings, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 7)

    label("loc_2696")

    Jump("loc_317A")

    label("loc_269B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2AB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2899")

    ChrTalk(
        0x8,
        (
            "A brand new heavy machine gun has been in\x01",
            "circulation since last week. You can bet your\x01",
            "asses I stocked up on them right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Revache went and got themselves a ton of\x01",
            "them, so you best watch your backs.\x02",
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
            "#0003FYeah. I'd definitely appreciate not being\x01",
            "gunned down by a weapon like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FFirepower like that will make mincemeat\x01",
            "out of you in a matter of seconds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB2")

    label("loc_2899")


    ChrTalk(
        0x104,
        (
            "#0305FSay, isn't that a Reinford-brand\x01",
            "heavy machine gun?\x02\x03",
            "Looks like a new model, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yeah, they started circulating last week.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh. Not only do they fire at a higher rate,\x01",
            "but the power on these bad boys has been\x01",
            "boosted by 20 percent as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Itching to try one out, Red?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0305FNah. I'm gonna give that a hard pass.\x02\x03",
            "#0306FY'know, probably not the brightest idea to flaunt\x01",
            "your smuggled merch in front of the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F*sigh* You said it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2AB2")

    Jump("loc_317A")

    label("loc_2AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B3B")

    ChrTalk(
        0x8,
        "Business is business...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm leaving the store to Jingo for a bit.\x01",
            "I've got somewhere I need to be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7E")

    label("loc_2B3B")


    ChrTalk(
        0x8,
        (
            "There's a meeting in the Empire\x01",
            "that I can't afford to miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Goddamn it. I have low blood pressure, people.\x01",
            "I told them not to call for me so early in the\x01",
            "damn morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(A meeting? It might be her weapons supplier.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F(Might be right on the money. Lotta big\x01",
            "manufacturers out in Erebonia.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2C7E")

    Jump("loc_317A")

    label("loc_2C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2F4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D68")

    ChrTalk(
        0x8,
        (
            "Looks like even the CGF has begun to fully\x01",
            "embrace newer model orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Not only that, but they're starting to utilize\x01",
            "state-of-the-art quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "They're still slowly being phased in, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F49")

    label("loc_2D68")

    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#0205FAh...\x02\x03",
            "These must be the new type\x01",
            "of quartz for the Enigma unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yeah, those are the ones.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Got a new stock of merchandise from the CGF.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Damn. These new orbments aren't popular\x01",
            "with customers. A steady supply isn't\x01",
            "enough to make money off of 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FWait... You're in cahoots with the CGF?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYeah, you'll find that crap anywhere ya look.\x01",
            "A whole lot more corruption in their ranks\x01",
            "than you'd like to believe.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_2F49")

    Jump("loc_317A")

    label("loc_2F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3027")

    ChrTalk(
        0x8,
        (
            "Well, whatever's plaguing the CGF\x01",
            "isn't my problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The only thing I care about is whether\x01",
            "they're buying my merchandise or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Heh. Sounds 'bout right for a\x01",
            "black market broker.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_317A")

    label("loc_3027")


    ChrTalk(
        0x8,
        (
            "Anyway, this shipment's for Heiyue.\x01",
            "It's about time I go deliver it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FHeiyue?\x01",
            "The mobsters from the East?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        "Oh. You know about them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They buy a little something every time\x01",
            "I stock some new wares.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heheh. Probably checking out their capabilities before\x01",
            "Revache gets their hands on them, I'd guess.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_317A")

    TalkEnd(0xFE)

    label("loc_317D")

    Return()

    # Function_3_451 end

    def Function_4_317E(): pass

    label("Function_4_317E")

    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    TurnDirection(0x8, 0x10A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 1)), scpexpr(EXPR_END)), "loc_3301")

    ChrTalk(
        0x8,
        (
            "Whenever you need some info on the\x01",
            "underground, you know who to call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. I like to throw my most valued clients\x01",
            "a bone or two at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205F(Do you come here regularly, Dudley?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603F(She's a valuable informant, so we engage in a\x01",
            "bit of give-and-take. You'll soon come to realize\x01",
            "that it's a vital asset for an investigation.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_373A")

    label("loc_3301")


    ChrTalk(
        0x8,
        "Yo. Good to see you again, Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In need of some maintenance today?\x01",
            "Or, have you come for more info?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603FAshleigh. I understand that this may be\x01",
            "a difficult question for you to answer, but...\x02\x03",
            "#0600F...you wouldn't happen to be dealing a\x01",
            "certain...illegal drug, would you?\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0001F(Leave it to Dudley to cut to the chase.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha... 'The blue drug that releases your inner bliss.'\x01",
            "I was wondering when you were going to question me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hate to break it to you, but I haven't laid a finger on\x01",
            "that stuff. I've heard plenty of rumors about it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Been about two or three weeks now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603FAh, is that so?\x02\x03",
            "#0600FMy apologies. Please disregard\x01",
            "everything I just said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Will do.\x01",
            "In return, be a doll and buy something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've got a new type of armor-piercing ammo\x01",
            "in stock that's compatible with your gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#0603FI owe you one, Ashleigh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0101F(These two... Could they be?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301F(Have they always been this friendly?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 1)

    label("loc_373A")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_4_317E end

    def Function_5_3753(): pass

    label("Function_5_3753")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "Goddess Almighty, lady! How many times do I\x01",
            "have to say it before you get it through your head?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "She's already got her basic arithmetic down!\x01",
            "Show her, Jingo. Answer me this question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "One rifle from the Reinford Company\x01",
            "sells for 15,000 mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Last week, we sold 40 rifles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "What were our total sales?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "600,000 mira!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)

    ChrTalk(
        0x8,
        "Perfect, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I am inclined to completely disagree.\x01",
            "How is this in any way appropriate?\x02",
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
    ClearChrFlags(0x8, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_5_3753 end

    def Function_6_39AF(): pass

    label("Function_6_39AF")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    TurnDirection(0x8, 0x104, 500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A17")

    ChrTalk(
        0x8,
        (
            "Hey, redhead. You look like you\x01",
            "know your way around a gun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A5D")

    label("loc_3A17")


    ChrTalk(
        0x8,
        (
            "Hey, you. Redhead. You look like you\x01",
            "know your way around a gun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5D")


    ChrTalk(
        0x8,
        "You ever been in the military?\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0305FHuh?\x02\x03",
            "#0300FWell, I did spend some time in the CGF.\x02\x03",
            "But the Guardian Force isn't officially classified\x01",
            "as the military, so I wouldn't call myself a soldier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A tall redhead...that looks like he's\x01",
            "fought some real battles...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "Hmmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#0305FUh, can I help you, lady?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "No, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sorry to bother you. Just give me a\x01",
            "heads-up if you need anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FSure...\x01",
            "(What was that all about?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 2)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFE)
    Return()

    # Function_6_39AF end

    def Function_7_3C9C(): pass

    label("Function_7_3C9C")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    TurnDirection(0x8, 0x0, 0)

    ChrTalk(
        0x8,
        (
            "Well, if it isn't the CPD's whatchamacallit section.\x01",
            "Heh. Seems like you guys aren't doing half bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You looking for something in particular?\x01",
            "We just stocked up on some nice merch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FNo, um... Should a black market broker\x01",
            "really be as open about this as you are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FThis place is as shady as ever.\x01",
            "Everything in here is smuggled, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, I'm just a simple seller of alcohol\x01",
            "and groceries...on the surface.\x01",
            "Hahaha. Got a problem with that, bub?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FWell, I have heard they are primarily\x01",
            "contracted by foreign militaries and\x01",
            "various jaeger corps.\x02\x03",
            "Since they do not appear to be receiving\x01",
            "threats from Revache, they must have\x01",
            "their tacit consent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FThe fact that a store like this can operate\x01",
            "around here so shamelessly is insane...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 1)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_7_3C9C end

    def Function_8_3FD7(): pass

    label("Function_8_3FD7")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x8,
        (
            "We have sixty .60-caliber\x01",
            "Reinfords, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(Hey, Lloyd...)\x02\x03",
            "(I can make out handguns in\x01",
            "that wooden box.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0201F(The other box over there appears\x01",
            "filled to the brim with ammunition.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F(Explosives and hand grenades...\x01",
            "I think I spy a bulletproof vest and\x01",
            "some other gadgets over there.)\x02\x03",
            "#0306F(Wait a damn minute. Is that drum\x01",
            "can over there filled with the liquid\x01",
            "fuel the CGF uses?)\x02",
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
            "#0001FU-Um... Excuse us.\x02\x03",
            "Pardon us, but we'd like some information\x01",
            "regarding the type of business you're running.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        "Hmm? Oh. Customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "We're brokers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We deal with smuggled goods coming\x01",
            "in from all over Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys new to the CPD? Never seen\x01",
            "you guys around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FB-Brokers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FPeople who like to operate in the dark.\x02\x03",
            "#0301FI'd heard rumors of a black market with\x01",
            "a long reach operating out of Crossbell\x01",
            "somewhere. Take it that's you, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FSmuggled goods and weapons...\x01",
            "Are you connected to Revache, by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, of course not.\x01",
            "Even the thought of being lumped in with\x01",
            "those numbskulls makes me sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm a respectable broker, thank you very much.\x01",
            "I trade with ten-odd countries, including\x01",
            "their militaries and the jaeger corps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't associate with small-time thugs that fire\x01",
            "their guns at the drop of a hat. You're cops, right?\x01",
            "If you want to take them down, be my guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, a detective from the First Division\x01",
            "usually stops by here every so often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well. Half the reason is to buy supplies, and\x01",
            "the other half is to loosen my tongue about\x01",
            "current smuggling trends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIt is surprising to see the CPD\x01",
            "openly associating with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FShe's still suspicious, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. Are you guys going to buy something,\x01",
            "or what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you must know, I don't sell weapons to\x01",
            "anybody I don't trust. It's one of our creeds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That being said, if anything ever catches\x01",
            "your eye, don't hesitate to ask my daughter\x01",
            "over at the counter about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 1)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_8_3FD7 end

    def Function_9_4839(): pass

    label("Function_9_4839")

    Call(0, 10)
    Return()

    # Function_9_4839 end

    def Function_10_483D(): pass

    label("Function_10_483D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_485C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4857")
    Call(0, 11)
    SetScenarioFlags(0x6B, 3)
    Return()

    label("loc_4857")

    Jump("loc_486A")

    label("loc_485C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_486A")
    Call(0, 12)
    Return()

    label("loc_486A")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4877")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65E2")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Trade (Equipment)\x01",      # 1
            "Trade (Quartz)\x01",         # 2
            "Trade (Other)\x01",          # 3
            "Leave\x01",                  # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48FC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_48FC")

    RunExpression(0x4, (scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D3, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4966")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4925")
    OP_AF(0x90)
    Jump("loc_4957")

    label("loc_4925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4935")
    OP_AF(0x8F)
    Jump("loc_4957")

    label("loc_4935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4945")
    OP_AF(0x8E)
    Jump("loc_4957")

    label("loc_4945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4955")
    OP_AF(0x8D)
    Jump("loc_4957")

    label("loc_4955")

    OP_AF(0x8C)

    label("loc_4957")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65DD")

    label("loc_4966")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4985")
    OP_AF(0x9A)
    Jump("loc_49B7")

    label("loc_4985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4995")
    OP_AF(0x99)
    Jump("loc_49B7")

    label("loc_4995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_49A5")
    OP_AF(0x98)
    Jump("loc_49B7")

    label("loc_49A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_49B5")
    OP_AF(0x97)
    Jump("loc_49B7")

    label("loc_49B5")

    OP_AF(0x96)

    label("loc_49B7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65DD")

    label("loc_49C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_49E5")
    OP_AF(0xA4)
    Jump("loc_4A27")

    label("loc_49E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_49F5")
    OP_AF(0xA5)
    Jump("loc_4A27")

    label("loc_49F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4A05")
    OP_AF(0xA3)
    Jump("loc_4A27")

    label("loc_4A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4A15")
    OP_AF(0xA2)
    Jump("loc_4A27")

    label("loc_4A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4A25")
    OP_AF(0xA1)
    Jump("loc_4A27")

    label("loc_4A25")

    OP_AF(0xA0)

    label("loc_4A27")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D3, 0x0)"), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A43")
    SetScenarioFlags(0x9D, 5)

    label("loc_4A43")

    Jump("loc_65DD")

    label("loc_4A48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A5C")
    Jump("loc_65DD")

    label("loc_4A5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65DD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4AE3")

    ChrTalk(
        0x9,
        "'Scuse me, customers. We're about to close.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Move yer rears if ya wanna buy somethin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_4AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 5)), scpexpr(EXPR_END)), "loc_4C75")

    ChrTalk(
        0x9,
        (
            "One Mishy...\x01",
            "Two Mishy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "'Colonel, it's time we began\x01",
            "marching through the snow!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ahhh! Playing make-believe with\x01",
            "Mishy is so much fun!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C6D")
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
            "#0006F(What kind of strange version of\x01",
            "house is she playing?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(Will all those Mishy be happy now?)\x02",
    )

    CloseMessageWindow()

    label("loc_4C6D")

    SetScenarioFlags(0x0, 1)
    Jump("loc_4E24")

    label("loc_4C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDB")

    ChrTalk(
        0x9,
        "Hey. Wanna buy somethin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Might even throw in some free goodies\x01",
            "if yer a regular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Here ya go. One free bullet for you.\x02",
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
            "#0106F(I'm not convinced that it's okay for a child to be\x01",
            "playing with all of these dangerous goods.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E24")

    label("loc_4DDB")


    ChrTalk(
        0x9,
        "Aw, maaaan. I'm so bored today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Mama's been super busy lately.\x02",
    )

    CloseMessageWindow()

    label("loc_4E24")

    Jump("loc_65DD")

    label("loc_4E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5016")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4EDF")

    ChrTalk(
        0x9,
        (
            "Y'know, Mama ran a store in a conflict\x01",
            "zone before I was even born!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She'd always tell me about these crazy firefights\x01",
            "she'd have with her customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5011")

    label("loc_4EDF")


    ChrTalk(
        0x9,
        "Y'know what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I know that I'm in safe hands if we're ever attacked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mama's already used to that sorta thing.\x01",
            "She'd beat anybody at their own game.\x02",
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
        0x104,
        "#0306F(The hell kinda store is this?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5011")

    Jump("loc_65DD")

    label("loc_5016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_50A3")

    ChrTalk(
        0x9,
        (
            "Ignore that nosy-ass sister\x01",
            "and buy somethin', will ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Arithmetic's a total piece of cake for\x01",
            "a smarty like myself!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_50A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_559D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_END)), "loc_51B6")

    ChrTalk(
        0x9,
        "Y'know, we don't serve random kids here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If ya wanna play, then gimme a heads-up\x01",
            "so I know that's why you're comin', 'kay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FYeah, got it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FKeA...before that, we need to have\x01",
            "a little bit of a talk about something.\x01",
            "Please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5598")

    label("loc_51B6")


    ChrTalk(
        0x153,
        (
            "#1110FHey, Lloyd! What do they even sell here?\x01",
            "This place gives me the creeps!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    ChrTalk(
        0x9,
        "H-Huh? You supposed to be a customer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "We don't sell to kids here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1105FAwww, really?!\x02\x03",
            "#1108FOh, but think of all the fun you could\x01",
            "have with some of this stuff...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "You got a good pair of eyes on ya.\x01",
            "I'm starting to see some promise\x01",
            "in you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Will you play with me sometime?\x01",
            "If you do, you can stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FReally? Yay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Pay attention, now. This one's .45-caliber,\x01",
            "and this one's .60-caliber. See the difference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FOh, yeah! Totally! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FStop. Please, just stop...\x02\x03",
            "These aren't toys, KeA. They're very dangerous.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54CD")

    ChrTalk(
        0x102,
        (
            "#0103FI wonder what made her take such\x01",
            "a liking to a place like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5595")

    label("loc_54CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_553E")

    ChrTalk(
        0x103,
        (
            "#0206FI am shocked to think that KeA would\x01",
            "enjoy playing in such a suspicious place...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5595")

    label("loc_553E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5595")

    ChrTalk(
        0x104,
        (
            "#0306FHow the hell'd she take a fancy\x01",
            "to a shady place like this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5595")

    SetScenarioFlags(0xB0, 3)

    label("loc_5598")

    Jump("loc_65DD")

    label("loc_559D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5699")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5613")

    ChrTalk(
        0x9,
        (
            "I hope Mama's gonna take me to\x01",
            "the festival later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Seems kinda pissy, so I doubt it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5694")

    label("loc_5613")


    ChrTalk(
        0x9,
        (
            "Ah. It's the festival... Man, I wanted to\x01",
            "play, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Store's still open, so I don't got much\x01",
            "of a choice, now do I?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5694")

    Jump("loc_65DD")

    label("loc_5699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_571B")

    ChrTalk(
        0x9,
        "You customers tired?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "If you are, then buy somethin'!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Buyin' stuff will totally make you feel better!\x02",
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_571B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5929")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5790")

    ChrTalk(
        0x9,
        (
            "This orbal camera can take pictures just like\x01",
            "any other. It's a sweet bargain right now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5924")

    label("loc_5790")


    ChrTalk(
        0x9,
        (
            "Some tourist came by and asked me\x01",
            "to sell him an orbal camera...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When I recommended one with a small gun\x01",
            "inside of it, the coward got scared and ran!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, sucks for him. Doesn't it seem super\x01",
            "useful to you guys?\x02",
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
            "#0006FDoes this store carry a single item that\x01",
            "WON'T take your life?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5924")

    Jump("loc_65DD")

    label("loc_5929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5A20")

    ChrTalk(
        0x9,
        "Hahaha! Serves that old jaeger right!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A1B")

    ChrTalk(
        0x104,
        (
            "#0306FAin't that pretty ballsy of her to do?\x01",
            "Girl's givin' me the chills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FI am in complete agreement.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FIs their parent-child dynamic\x01",
            "always like this?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5A1B")

    Jump("loc_65DD")

    label("loc_5A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5AA1")

    ChrTalk(
        0x9,
        "You wanna see the expensive stuff, customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Sure, it might eat your wallet, but deal with it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B68")

    label("loc_5AA1")


    ChrTalk(
        0x9,
        "We just got some new goods in, customers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It's all pretty expensive. Ya wanna see it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't mind the price. Of course it's going to be\x01",
            "expensive. You just gotta deal with it, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5B68")

    Jump("loc_65DD")

    label("loc_5B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5C7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5BDD")

    ChrTalk(
        0x9,
        "Come on and buy somethin', customers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Our store closes in the evening, y'know!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C7A")

    label("loc_5BDD")


    ChrTalk(
        0x9,
        (
            "Mama's gonna be restocking the\x01",
            "inventory today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's why we gotta close in the evening.\x01",
            "So if you're buyin' something, ya better hurry it up!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5C7A")

    Jump("loc_65DD")

    label("loc_5C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5F8E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5D20")

    ChrTalk(
        0x9,
        "Mama's still not back yet.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x9,
        (
            "Man, she sure is late today...\x01",
            "The hell's takin' her so long?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E96")

    label("loc_5D20")


    ChrTalk(
        0x9,
        (
            "...'Scuse me, customers! Keep it the hell down\x01",
            "next time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4SYou were bein' way too loud out there!\x02",
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
        "#0006FSorry, Jingo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You'll scare away all the business, dumbasses!\x01",
            "Ain't that right?! Huh?! HUH?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "If yer plannin' to goof off, then do it QUIETLY!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5E96")

    Jump("loc_5F89")

    label("loc_5E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5F27")

    ChrTalk(
        0x9,
        "Mama's still not back yet.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x9,
        (
            "Man, she sure is late today...\x01",
            "The hell's takin' her so long?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F89")

    label("loc_5F27")


    ChrTalk(
        0x9,
        "Those street kids can get so annoying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'm gonna strangle y'all one day! Y'hear me?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5F89")

    Jump("loc_65DD")

    label("loc_5F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_60B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5FFD")

    ChrTalk(
        0x9,
        "Today's one of Mama's drinkin' days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Better hurry up if ya wanna talk to her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_60AE")

    label("loc_5FFD")


    ChrTalk(
        0x9,
        "Hmm? Ya need somethin' from Mama?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Better hurry up if ya wanna talk to her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mama told me that she was going to go drinkin'\x01",
            "after she was done takin' inventory.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_60AE")

    Jump("loc_65DD")

    label("loc_60B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_623A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_613C")

    ChrTalk(
        0x9,
        (
            "Mama hasn't been takin' me to\x01",
            "any of her dealings lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Aww, tendin' the store everyday is so boring!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6235")

    label("loc_613C")


    ChrTalk(
        0x9,
        "Y'think her deals have gotten nastier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mama told me that last time she tried to deal\x01",
            "with Revache, she got attacked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mama told me it's been pretty dangerous for\x01",
            "her, so she hasn't been takin' me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Maaan... It's so boring here!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_6235")

    Jump("loc_65DD")

    label("loc_623A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_64EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_62CB")

    ChrTalk(
        0x9,
        (
            "This .60-caliber bullet hasn't been too\x01",
            "popular with customers lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm. Might be time to put it up on sale.\x02",
    )

    CloseMessageWindow()
    Jump("loc_64E7")

    label("loc_62CB")


    ChrTalk(
        0x9,
        (
            "So we'll put normal bullets over here\x01",
            "and explosives over there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm... Maybe I should put 'em all in\x01",
            "that big case. Make 'em all a lil' easier\x01",
            "to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Whaddaya think, customers?\x02",
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
        "#0006FHow do you think I'm going to respond?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FTh-They're extremely dangerous, Jingo.\x01",
            "Maybe you should leave them alone?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "How are the customers going to know what\x01",
            "to buy if it isn't up on display?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_64E7")

    Jump("loc_65DD")

    label("loc_64EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6575")

    ChrTalk(
        0x9,
        "Mama's even got a jaeger for an acquaintance!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That old dude's super tough-lookin'.\x01",
            "I've seen him in here before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_6575")


    ChrTalk(
        0x9,
        "Ya guys buyin' anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mira can be traced, so we only exchange\x01",
            "with other goods. Ya got it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65DD")

    Jump("loc_4877")

    label("loc_65E2")

    TalkEnd(0x9)
    Return()

    # Function_10_483D end

    def Function_11_65E6(): pass

    label("Function_11_65E6")

    TalkBegin(0x9)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "Ah, customers. What'cha guys after today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll tell ya what. We recently stocked up on\x01",
            "some super-duper strong grenades!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "One of these babies can take down an entire\x01",
            "platoon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FThis place gets shadier with each visit...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67AC")

    ChrTalk(
        0x102,
        (
            "#0103FIt's outward appearance suggests a\x01",
            "simple exchange shop.\x02\x03",
            "The legal gray area they choose to operate in\x01",
            "is always dangerously treading on black, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68FE")

    label("loc_67AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_685A")

    ChrTalk(
        0x103,
        (
            "#0203FThe shop's outside appearance merely presents\x01",
            "itself as a normal exchange shop...\x02\x03",
            "Their legality, however, constantly treads\x01",
            "back and forth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68FE")

    label("loc_685A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68FE")

    ChrTalk(
        0x104,
        (
            "#0303FDespite this place lookin' like your\x01",
            "run-of-the-mill exchange shop...\x02\x03",
            "Place seems to always be teeterin'\x01",
            "between legal and illegal, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68FE")

    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Speak to Jingo and choose 'Exchange' for a catalog\x01",
            "of tradable goods. If you have the necessary items,\x01",
            "you can perform an exchange.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Equipment and quartz found at this shop are rare\x01",
            "and cannot be obtained by other means.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Be aware that since items are used instead of mira,\x01",
            "you should think carefully about the trades you\x01",
            "choose to perform.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetScenarioFlags(0xB3, 4)
    TalkEnd(0x9)
    Return()

    # Function_11_65E6 end

    def Function_12_6A8D(): pass

    label("Function_12_6A8D")

    TalkBegin(0x9)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "Oh, customers!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        "#4SMama! We have new customers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4SCan I sell 'em some weapons?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BA7")
    Sleep(1500)

    ChrTalk(
        0x9,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "Oh, sorry 'bout that. Mama's not\x01",
            "here right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, whatever. Here to buy somethin'?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C31")

    label("loc_6BA7")


    ChrTalk(
        0x8,
        "#4PHuh? New customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4PSell 'em the untraceable stuff!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        "Ya heard her, folks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "So, you buying somethin' today?\x02",
    )

    CloseMessageWindow()

    label("loc_6C31")

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
        "#0005FWe, uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FActually, what kind of store is this\x01",
            "supposed to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, we sell smuggled goods. We got\x01",
            "everything you'd ever need here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ignorin' the fact that we've only got meds and\x01",
            "quartz available right now. Oh, but we have\x01",
            "that, and also this thing here...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "Oh, yeah. Don't count on usin' any mira.\x01",
            "That stuff leaves a trail. Pay with goods only.\x02",
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
            "#0203FThis continues to sound more\x01",
            "suspicious by the minute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FSo, what the lil' miss is trying to say...is that\x01",
            "this is some kinda exchange shop, yeah?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Speak to Jingo and choose 'Exchange' for a catalog\x01",
            "of tradable goods. If you have the necessary items,\x01",
            "you can perform an exchange.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Equipment and quartz found at this shop are rare\x01",
            "and cannot be obtained by other means.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Be aware that since items are used instead of mira,\x01",
            "you should think carefully about the trades you\x01",
            "choose to perform.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetScenarioFlags(0x6B, 3)
    SetScenarioFlags(0xB3, 4)
    TalkEnd(0x9)
    Return()

    # Function_12_6A8D end

    def Function_13_70C3(): pass

    label("Function_13_70C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_713A")

    ChrTalk(
        0xA,
        (
            "*sigh* Teaching the children of the\x01",
            "Downtown District is never as\x01",
            "straightforward as you'd hope.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71E3")

    label("loc_713A")


    ChrTalk(
        0xA,
        (
            "I'd like for Jingo to participate in Sunday School\x01",
            "like all the other kids, but I'm always turned away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I pray that I'm able to make Ashleigh\x01",
            "understand...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_71E3")

    TalkEnd(0xFE)
    Return()

    # Function_13_70C3 end

    def Function_14_71E7(): pass

    label("Function_14_71E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_736D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72E0")

    ChrTalk(
        0xFE,
        (
            "I came to get information about\x01",
            "yesterday's raid on Heiyue, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...the shopkeeper here has never\x01",
            "been an easy lady to work with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She seems on edge around me. Probably\x01",
            "because I'm not a regular client.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_736D")

    label("loc_72E0")


    ChrTalk(
        0xFE,
        (
            "If I had to guess, she's the type of woman\x01",
            "that relies on herself to get things done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess I'm not going to have any luck here.\x02",
    )

    CloseMessageWindow()

    label("loc_736D")

    TalkEnd(0xFE)
    Return()

    # Function_14_71E7 end

    def Function_15_7371(): pass

    label("Function_15_7371")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_760F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7567")

    ChrTalk(
        0xFE,
        (
            "Scott and Wenzel went to\x01",
            "check on Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's supposedly been an eyewitness report\x01",
            "claiming that the mafia had gone there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhy would the mafia go to a CGF post?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's actually been quite a few eyewitness\x01",
            "reports leading up to this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been hearing a ton of rumors that the CGF\x01",
            "commander is in cahoots with the mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FYeah, word on the street is he's bein' bribed.\x02\x03",
            "#0306FMan, I never really liked that guy anyway.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_760F")

    label("loc_7567")


    ChrTalk(
        0xFE,
        (
            "Well, an investigation of Bellguard Gate\x01",
            "shouldn't be a big deal, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since that big raid just went down, we gotta\x01",
            "track down some evidence, just in case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_760F")

    TalkEnd(0xFE)
    Return()

    # Function_15_7371 end

    def Function_16_7613(): pass

    label("Function_16_7613")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    LoadChrToIndex("chr/ch02200.itc", 0x1E)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    OP_68(2670, 1200, 7100, 0)
    MoveCamera(63, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -270, 0, 1360, 45)
    SetChrPos(0x102, 860, 0, 1510, 0)
    SetChrPos(0x103, -810, 0, 500, 45)
    SetChrPos(0x104, 1130, 0, 760, 0)
    SetChrPos(0xD, 2330, 0, 6050, 0)
    SetChrPos(0x8, 2920, 0, 7720, 180)
    SetChrPos(0x9, 4380, -1920, 14500, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetCameraDistance(17000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0xD,
        (
            "#3104FI'm giving you this offer out of the\x01",
            "goodness of my heart, okay?\x02\x03",
            "#3100FThis is for your own good, Ashleigh.\x01",
            "Accept Revache's protection.\x02\x03",
            "We'll make sure to have\x01",
            "your business' back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How many times have I turned\x01",
            "down this offer now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3104FYou don't seem to understand, Ashleigh.\x02\x03",
            "#3101FI know exactly what you're capable of, so I'd\x01",
            "like to settle this without having to take you down.\x01",
            "Don't think we'll let you off so easy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*cough*... Interesting offer, my friend.\x01",
            "Hit me with your best shot, Garcia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My business extends all the way from\x01",
            "Crossbell to Eastern Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Get over yourself. My routes are too much for\x01",
            "some hotheaded, petty criminals to handle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once you get that through your thick skull,\x01",
            "you can get over yourself, Mr. Mafia Boss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3107FWho do you think you're talking to?\x01",
            "Don't get too cocky, you fool!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3790, 1200, 8640, 3000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_95(0x9, 9740, 0, 14440, 2000, 0x0)
    OP_95(0x9, 9740, 0, 12440, 2000, 0x0)
    TurnDirection(0x9, 0xD, 500)

    ChrTalk(
        0x9,
        "Hey, customer. Yeah, you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "SHUT UP!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3103FUgh...\x01",
            "You and that little brat of yours\x01",
            "haven't changed one bit.\x02\x03",
            "#3100FWell, whatever. Think it over.\x01",
            "If you want to keep your little operation\x01",
            "in Crossbell up and running, that is.\x02",
        )
    )

    CloseMessageWindow()
    Fade(300)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_93(0x8, 0xE1, 0x0)
    OP_68(1500, 500, 4580, 0)
    OP_68(40, 1200, 2580, 2000)
    MoveCamera(41, 17, 0, 0)
    SetCameraDistance(17000, 0)
    OP_95(0xD, 730, 20, 3170, 2000, 0x0)

    ChrTalk(
        0xD,
        "#3101FYou're in the way. Move.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_7CAC():
        OP_96(0x101, 0xFFFFFD6C, 0x0, 0x6E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7CAC)

    def lambda_7CC6():
        OP_96(0x102, 0x532, 0x0, 0x6E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7CC6)

    def lambda_7CE0():
        OP_96(0x103, 0xFFFFF9E8, 0x0, 0x460, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7CE0)
    OP_95(0xD, -110, 0, 70, 2000, 0x0)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)

    def lambda_7D17():
        TurnDirection(0x101, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D17)

    def lambda_7D24():
        TurnDirection(0x102, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D24)

    def lambda_7D31():
        TurnDirection(0x103, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7D31)

    def lambda_7D3E():
        TurnDirection(0x104, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7D3E)

    def lambda_7D4B():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7D4B)
    OP_95(0xD, -320, 0, -2350, 2000, 0x0)

    ChrTalk(
        0x104,
        (
            "#0301FSo even Garcia Rossi\x01",
            "comes down here, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FIt sounded like an intense argument...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    Sleep(1000)
    OP_D5(0x1E)
    OP_68(130, 1200, 1760, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 130, 0, 1760, 45)
    SetChrPos(0x1, 130, 0, 1760, 45)
    SetChrPos(0x2, 130, 0, 1760, 45)
    SetChrPos(0x3, 130, 0, 1760, 45)
    SetChrPos(0x9, 5670, 30, 8650, 225)
    SetScenarioFlags(0xB5, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_16_7613 end

    def Function_17_7E8C(): pass

    label("Function_17_7E8C")

    EventBegin(0x1)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F65")

    ChrTalk(
        0x9,
        (
            "Oh?\x01",
            "Customers, please hold on a minute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That leads to the basement storeroom, and you're\x01",
            "definitely not allowed in there. So keep your asses\x01",
            "right up here if you wanna buy somethin'!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8001")

    label("loc_7F65")


    ChrTalk(
        0x9,
        "Didja not hear me the first time, customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thought I told you to never set foot\x01",
            "near the basement! If yer itchin' to\x01",
            "buy somethin', DO IT HERE!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8001")

    Sleep(50)
    SetChrPos(0x0, 9940, 0, 11910, 180)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_17_7E8C end

    SaveToFile()

Try(main)
