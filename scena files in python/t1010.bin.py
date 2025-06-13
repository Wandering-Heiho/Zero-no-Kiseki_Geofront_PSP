from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1010.bin",                # FileName
        "t1010",                    # MapName
        "t1010",                    # Location
        0x0042,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1010",                  # 0
        "Emmy",                   # 1
        "Zell",                   # 2
        "Gabrion",                # 3
        "Lughman",                # 4
        "Man",                    # 5
        "To Speaker's Mansion",   # 6
        "To Hotel Delphinia",     # 7
    ))

    AddCharChip((
        "chr/ch27700.itc",                   # 00
        "chr/ch22302.itc",                   # 01
        "chr/ch22202.itc",                   # 02
        "chr/ch33100.itc",                   # 03
        "chr/ch33000.itc",                   # 04
    ))

    DeclNpc(2279,    -3700,   -12430,  180,  341,  0x0, 0,   1,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(3660,    -3700,   -12430,  180,  341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(26860,   -2000,   2200,    270,  257,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1970,   -2000,   34720,   180,  257,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2400,    -1799,   55840,   0,    385,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)

    DeclEvent(0x0000, 0, 13,  -6.460000038146973,    -16.520000457763672,   -3.799999952316284,    156.25,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.2920000553131104,    3.30400013923645,      0.7599999904632568,    1.0])

    DeclActor(-6460,   -3800,   -16520,  1200,    -6210,   -5800,   -21830,  0x007C, 0,  12, 0x0000)

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "To Speaker's Mansion")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ScpFunction((
        "Function_0_21C",          # 00, 0
        "Function_1_2D4",          # 01, 1
        "Function_2_335",          # 02, 2
        "Function_3_396",          # 03, 3
        "Function_4_3C1",          # 04, 4
        "Function_5_43E",          # 05, 5
        "Function_6_531",          # 06, 6
        "Function_7_7E4",          # 07, 7
        "Function_8_A6A",          # 08, 8
        "Function_9_119F",         # 09, 9
        "Function_10_144F",        # 0A, 10
        "Function_11_1741",        # 0B, 11
        "Function_12_1821",        # 0C, 12
        "Function_13_192C",        # 0D, 13
        "Function_14_1ABF",        # 0E, 14
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_334")
    OP_95(0xFE, 26860, -2000, 2200, 2000, 0x0)
    OP_95(0xFE, -4019, -1800, 2200, 2000, 0x0)
    OP_95(0xFE, -3510, -1800, -1500, 2000, 0x0)
    OP_95(0xFE, 26860, -2000, -2060, 2000, 0x0)
    Jump("Function_1_2D4")

    label("loc_334")

    Return()

    # Function_1_2D4 end

    def Function_2_335(): pass

    label("Function_2_335")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_395")
    OP_95(0xFE, -1970, -2000, 34720, 2000, 0x0)
    OP_95(0xFE, -1970, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 34720, 2000, 0x0)
    Jump("Function_2_335")

    label("loc_395")

    Return()

    # Function_2_335 end

    def Function_3_396(): pass

    label("Function_3_396")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C0")
    OP_94(0xFE, 0xFFFFEB1A, 0xB9D2, 0xF8C, 0xD67E, 0x3E8)
    Sleep(300)
    Jump("Function_3_396")

    label("loc_3C0")

    Return()

    # Function_3_396 end

    def Function_4_3C1(): pass

    label("Function_4_3C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_3CF")
    Jump("loc_431")

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_431")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_3EB")
    Jump("loc_431")

    label("loc_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3F9")
    Jump("loc_431")

    label("loc_3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_407")
    Jump("loc_431")

    label("loc_407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_415")
    Jump("loc_431")

    label("loc_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_428")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_431")

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_431")

    label("loc_431")

    BeginChrThread(0xA, 0, 0, 1)
    BeginChrThread(0xB, 0, 0, 2)
    Return()

    # Function_4_3C1 end

    def Function_5_43E(): pass

    label("Function_5_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47E")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "t1010_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1010_sky_y", 0x1, 0x1)
    Jump("loc_4A2")

    label("loc_47E")

    SetMapObjFrame(0xFF, "t1010_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1010_sky_y", 0x0, 0x1)

    label("loc_4A2")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C2")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4C2")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A")
    OP_66(0x0, 0x1)
    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -6210, -5800, -21830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_52A")

    Sound(126, 1, 80, 0)
    Return()

    # Function_5_43E end

    def Function_6_531(): pass

    label("Function_6_531")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C5")
    Jump("loc_60F")

    label("loc_5C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60F")

    label("loc_5E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_605")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60F")

    label("loc_605")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_642")
    Jump("loc_7DC")

    label("loc_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_650")
    Jump("loc_7DC")

    label("loc_650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_65E")
    Jump("loc_7DC")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_66C")
    Jump("loc_7DC")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_7DC")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_735")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_695")
    Call(0, 8)
    Jump("loc_730")

    label("loc_695")


    ChrTalk(
        0xFE,
        (
            "Zell is such a good-for-nothing.\x01",
            "Truly hopeless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Zell becomes a doctor, I'll just be stuck\x01",
            "at home with nothing to do but be lonely,\x01",
            "won't I?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_730")

    Jump("loc_7DC")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_7D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_750")
    Call(0, 8)
    Jump("loc_7CE")

    label("loc_750")


    ChrTalk(
        0xFE,
        (
            "Zell is such a good-for-nothing.\x01",
            "Truly hopeless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Does he really think taking a career\x01",
            "like that will make me happy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CE")

    Jump("loc_7DC")

    label("loc_7D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7DC")

    label("loc_7DC")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_531 end

    def Function_7_7E4(): pass

    label("Function_7_7E4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_878")
    Jump("loc_8C2")

    label("loc_878")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_898")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C2")

    label("loc_898")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C2")

    label("loc_8B8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_8F5")
    Jump("loc_A62")

    label("loc_8F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_903")
    Jump("loc_A62")

    label("loc_903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_911")
    Jump("loc_A62")

    label("loc_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_91F")
    Jump("loc_A62")

    label("loc_91F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_92D")
    Jump("loc_A62")

    label("loc_92D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_998")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_948")
    Call(0, 8)
    Jump("loc_993")

    label("loc_948")


    ChrTalk(
        0xFE,
        (
            "Emmy is being really selfish. What's so\x01",
            "wrong with chasing my dreams?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_993")

    Jump("loc_A62")

    label("loc_998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B3")
    Call(0, 8)
    Jump("loc_A54")

    label("loc_9B3")


    ChrTalk(
        0xFE,
        (
            "I can't really understand what Emmy's\x01",
            "trying to say at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not like I'd even care about being her fiance,\x01",
            "but our parents already decided on it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A54")

    Jump("loc_A62")

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A62")

    label("loc_A62")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_7E4 end

    def Function_8_A6A(): pass

    label("Function_8_A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_A78")
    Jump("loc_1193")

    label("loc_A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_A86")
    Jump("loc_1193")

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_A94")
    Jump("loc_1193")

    label("loc_A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_AA2")
    Jump("loc_1193")

    label("loc_AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_AB0")
    Jump("loc_1193")

    label("loc_AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_E77")
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x9, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B4D")
    Jump("loc_B97")

    label("loc_B4D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B6D")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B97")

    label("loc_B6D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B8D")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B97")

    label("loc_B8D")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B97")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C50")
    Jump("loc_C9A")

    label("loc_C50")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C70")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C9A")

    label("loc_C70")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C90")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C9A")

    label("loc_C90")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C9A")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(
        0x8,
        (
            "Listen up, Zell. You're my fiance,\x01",
            "and that means you need to properly\x01",
            "plan your future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Do you have a future career planned?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh, yeah... I actually want to become\x01",
            "a doctor at St. Ursula Hospital.\x01",
            "At least, that's my plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Absolutely not. I've heard that once you\x01",
            "become a doctor, you rarely have time\x01",
            "to visit home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I won't allow you to become a husband\x01",
            "that disregards his family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "A-Are you serious...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1193")

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_118A")
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x9, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F14")
    Jump("loc_F5E")

    label("loc_F14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F34")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F5E")

    label("loc_F34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F54")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F5E")

    label("loc_F54")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F5E")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1017")
    Jump("loc_1061")

    label("loc_1017")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1037")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1061")

    label("loc_1037")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1057")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1061")

    label("loc_1057")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1061")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(
        0x8,
        (
            "Hey, Zell. Since you're my fiance now,\x01",
            "you have to work to become a proper\x01",
            "man, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Umm...so what should I do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's not for me to decide. But\x01",
            "whatever you choose, make sure\x01",
            "it's something respectable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "A-And a doctor isn't...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1193")

    label("loc_118A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1193")

    label("loc_1193")

    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_8_A6A end

    def Function_9_119F(): pass

    label("Function_9_119F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_11B0")
    Jump("loc_144B")

    label("loc_11B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_11BE")
    Jump("loc_144B")

    label("loc_11BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_11CC")
    Jump("loc_144B")

    label("loc_11CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_11DA")
    Jump("loc_144B")

    label("loc_11DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_11E8")
    Jump("loc_144B")

    label("loc_11E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_12FE")

    ChrTalk(
        0xFE,
        (
            "What do you think you are doing?\x01",
            "You can't visit the residential area\x01",
            "dressed like THAT.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People of your ilk have a place where\x01",
            "they belong. And that is not here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you must come this way, at least change\x01",
            "into more suitable clothes at the boutique.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144B")

    label("loc_12FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_1442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(
        0xFE,
        "My, oh, my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What business do commoners have\x01",
            "in the pristine residential area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you came to sightsee, I advise\x01",
            "you stick to the theme park.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_143D")

    label("loc_13B7")


    ChrTalk(
        0xFE,
        (
            "If you came to sightsee, I advise\x01",
            "you stick to the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you see my mansion? I can't\x01",
            "fault you for being jealous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143D")

    Jump("loc_144B")

    label("loc_1442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_144B")

    label("loc_144B")

    TalkEnd(0xFE)
    Return()

    # Function_9_119F end

    def Function_10_144F(): pass

    label("Function_10_144F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_1460")
    Jump("loc_173D")

    label("loc_1460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_146E")
    Jump("loc_173D")

    label("loc_146E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_147C")
    Jump("loc_173D")

    label("loc_147C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_148A")
    Jump("loc_173D")

    label("loc_148A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_1498")
    Jump("loc_173D")

    label("loc_1498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1564")

    ChrTalk(
        0xFE,
        (
            "Talk of the street is that there's going to\x01",
            "be an Anniversary Festival party over at\x01",
            "Speaker Hartmann's mansion tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, he's even invited friends from\x01",
            "abroad as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173D")

    label("loc_1564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_1734")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1676")

    ChrTalk(
        0xFE,
        (
            "If you walk down this street, you'll run\x01",
            "straight into the speaker's mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I imagine you'll go into shock just by gazing\x01",
            "upon its architectural genius and splendor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, if only there'd be a day where\x01",
            "I could share in his wealth.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_172F")

    label("loc_1676")


    ChrTalk(
        0xFE,
        "Speaker Hartmann's mansion is straight ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maintaining such a huge mansion must cost quite\x01",
            "a bit of mira... Oh, if only there'd be a day\x01",
            "where I could share in his wealth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172F")

    Jump("loc_173D")

    label("loc_1734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_173D")

    label("loc_173D")

    TalkEnd(0xFE)
    Return()

    # Function_10_144F end

    def Function_11_1741(): pass

    label("Function_11_1741")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If my memory serves me right, Speaker Hartmann's\x01",
            "mansion should be somewhere this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps I will go have a slight rest there\x01",
            "before tonight. I imagine my guest room\x01",
            "is already prepped and ready for me.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1741 end

    def Function_12_1821(): pass

    label("Function_12_1821")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FAuction, smocktion. It's time for fishin'!\x02",
    )

    CloseMessageWindow()
    OP_68(-3780, -2000, -21590, 1500)
    MoveCamera(315, 25, 0, 1500)
    OP_6E(320, 1500)
    SetCameraDistance(39000, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190D")
    OP_E0(0x2)
    ClearScenarioFlags(0x0, 3)
    MiniGame(0x6, 0x4, 0xFFFFE6D8, 0xFFFFF128, 0xFFFFC36A, 0xB4, 0xFFFFE7BE, 0xFFFFE958, 0xFFFFAABA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190D")
    SetScenarioFlags(0x0, 3)

    label("loc_190D")

    OP_E0(0x2)
    EventEnd(0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_192B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192B")
    Call(0, 14)

    label("loc_192B")

    Return()

    # Function_12_1821 end

    def Function_13_192C(): pass

    label("Function_13_192C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4510, -2000, -17230, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24740, 0)
    SetChrPos(0x101, -7200, -3800, -15000, 180)
    SetChrPos(0x102, -6000, -3800, -15000, 180)
    SetChrPos(0x103, -7200, -3800, -13800, 180)
    SetChrPos(0x104, -6000, -3800, -13800, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_19BF")
    SetChrPos(0x151, -4800, -3800, -14400, 180)

    label("loc_19BF")

    StopEffect(0x1, 0x2)
    OP_0D()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1A26")
    OP_63(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1A26")

    Sleep(1000)
    OP_68(-2980, -2000, -24760, 3000)
    SetCameraDistance(21000, 3000)
    OP_6F(0x79)
    LoadEffect(0x0, "event\\eva00_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -6210, -5800, -21830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(860, 0, 100, 0)
    Sleep(3000)
    StopEffect(0x0, 0x2)
    Sleep(2000)
    OP_29(0x24, 0x1, 0x8)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, -7200, -3800, -15000, 180)
    EventEnd(0x5)
    Return()

    # Function_13_192C end

    def Function_14_1ABF(): pass

    label("Function_14_1ABF")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4510, -2000, -17230, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24740, 0)
    SetChrPos(0x101, -7200, -3800, -15000, 180)
    SetChrPos(0x102, -6000, -3800, -15000, 180)
    SetChrPos(0x103, -7200, -3800, -13800, 180)
    SetChrPos(0x104, -6000, -3800, -13800, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1B52")
    SetChrPos(0x151, -4800, -3800, -14400, 180)

    label("loc_1B52")

    StopEffect(0x1, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0005FI could tell that fish was a beaut, but\x01",
            "is this Toma's engagement ring, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0205FSo a fish mistook it for food after it fell\x01",
            "into the lake?\x02\x03",
            "#0206FThe odds of that being the case are so\x01",
            "astronomically low that I am a little\x01",
            "hesitant to believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FY-Yeah. I certainly wasn't expecting anything\x01",
            "like this...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1D0E")

    ChrTalk(
        0x151,
        (
            "#11P#5709FHahaha! Almost seems impossible, right?\x01",
            "Yet here it is, all the same.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0E")


    ChrTalk(
        0x104,
        (
            "#11P#0306FNot sure if all that walkin' was worth the effort,\x01",
            "honestly...\x02\x03",
            "#0300FOh, well. We found the sucker, so everything's\x01",
            "cool in my book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FAgreed... Might as well go and have Toma\x01",
            "confirm whether or not this is his ring,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x9)
    OP_65(0x0, 0x1)
    SetChrPos(0x0, -7200, -3800, -15000, 180)
    StopEffect(0x8, 0x2)
    EventEnd(0x5)
    Return()

    # Function_14_1ABF end

    SaveToFile()

Try(main)
