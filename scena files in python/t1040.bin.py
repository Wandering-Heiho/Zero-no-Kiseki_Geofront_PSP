from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1040.bin",                # FileName
        "t1040",                    # MapName
        "t1040",                    # Location
        0x0044,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 68, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1040",                  # 0
        "Kilika",                 # 1
        "Lyte",                   # 2
        "Mercy",                  # 3
        "Boy",                    # 4
        "Man",                    # 5
        "Man",                    # 6
        "Woman",                  # 7
        "Girl",                   # 8
        "Young Man",              # 9
        "Tourist",                # 10
        "Old Man",                # 11
        "Old Lady",               # 12
        "Winona",                 # 13
        "Drona",                  # 14
        "Girl",                   # 15
        "Young Man",              # 16
    ))

    AddCharChip((
        "chr/ch07302.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34500.itc",                   # 02
        "chr/ch21302.itc",                   # 03
        "chr/ch21202.itc",                   # 04
        "chr/ch24602.itc",                   # 05
        "chr/ch24202.itc",                   # 06
        "chr/ch20202.itc",                   # 07
        "chr/ch20302.itc",                   # 08
        "chr/ch27900.itc",                   # 09
        "chr/ch26600.itc",                   # 0A
        "chr/ch21602.itc",                   # 0B
        "chr/ch33002.itc",                   # 0C
        "chr/ch21702.itc",                   # 0D
        "chr/ch21300.itc",                   # 0E
        "chr/ch21200.itc",                   # 0F
    ))

    DeclNpc(-97889,  0,       18979,   45,   469,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-104069, 0,       2980,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-101099, 0,       5880,    90,   257,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-103029, 0,       10760,   225,  469,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-104839, 0,       8949,    45,   469,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-93879,  0,       11039,   225,  469,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-95839,  0,       9050,    45,   469,  0x0, 0,   8,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-104949, 0,       8989,    45,   469,  0x0, 0,   3,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-102970, 0,       10960,   225,  469,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-93940,  0,       11039,   225,  469,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-97919,  0,       18979,   45,   469,  0x0, 0,   12,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-97930,  0,       20979,   135,  469,  0x0, 0,   13,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-1860,   0,       10640,   180,  257,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-6250,   0,       6099,    180,  257,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-6019,   0,       4829,    90,   385,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-7389,   0,       3789,    45,   385,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)

    DeclActor(-1770,   0,       8810,    1000,    -1860,   1500,    10640,   0x007E, 0,  17, 0x0000)
    DeclActor(-101650, 0,       2470,    1000,    -104070, 1500,    2980,    0x007E, 0,  5,  0x0000)
    DeclActor(-102930, 0,       14990,   1200,    -102930, 800,     14990,   0x007C, 0,  33, 0x0000)

    ScpFunction((
        "Function_0_388",          # 00, 0
        "Function_1_440",          # 01, 1
        "Function_2_4C9",          # 02, 2
        "Function_3_591",          # 03, 3
        "Function_4_656",          # 04, 4
        "Function_5_8DC",          # 05, 5
        "Function_6_8E0",          # 06, 6
        "Function_7_BA6",          # 07, 7
        "Function_8_F3D",          # 08, 8
        "Function_9_FA2",          # 09, 9
        "Function_10_11CF",        # 0A, 10
        "Function_11_139D",        # 0B, 11
        "Function_12_14DA",        # 0C, 12
        "Function_13_16C6",        # 0D, 13
        "Function_14_19BA",        # 0E, 14
        "Function_15_1C01",        # 0F, 15
        "Function_16_1DBD",        # 10, 16
        "Function_17_1FAB",        # 11, 17
        "Function_18_1FAF",        # 12, 18
        "Function_19_211F",        # 13, 19
        "Function_20_2173",        # 14, 20
        "Function_21_21E3",        # 15, 21
        "Function_22_22C1",        # 16, 22
        "Function_23_234B",        # 17, 23
        "Function_24_2398",        # 18, 24
        "Function_25_36ED",        # 19, 25
        "Function_26_3746",        # 1A, 26
        "Function_27_379F",        # 1B, 27
        "Function_28_37F8",        # 1C, 28
        "Function_29_3851",        # 1D, 29
        "Function_30_38AA",        # 1E, 30
        "Function_31_4379",        # 1F, 31
        "Function_32_4F21",        # 20, 32
        "Function_33_5C27",        # 21, 33
    ))


    def Function_0_388(): pass

    label("Function_0_388")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3C8"),
        (1, "loc_3D4"),
        (2, "loc_3E0"),
        (3, "loc_3EC"),
        (4, "loc_3F8"),
        (5, "loc_404"),
        (6, "loc_410"),
        (SWITCH_DEFAULT, "loc_41C"),
    )


    label("loc_3C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_404")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_410")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_41C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_428")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_43F")

    Return()

    # Function_0_388 end

    def Function_1_440(): pass

    label("Function_1_440")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C8")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_440")

    label("loc_4C8")

    Return()

    # Function_1_440 end

    def Function_2_4C9(): pass

    label("Function_2_4C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E3")
    Event(0, 24)

    label("loc_4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4F1")
    Jump("loc_58A")

    label("loc_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4FF")
    Jump("loc_58A")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_50D")
    Jump("loc_58A")

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_51B")
    Jump("loc_58A")

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_529")
    Jump("loc_58A")

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_550")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_58A")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_581")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_58A")

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_58A")

    label("loc_58A")

    BeginChrThread(0xA, 0, 0, 1)
    Return()

    # Function_2_4C9 end

    def Function_3_591(): pass

    label("Function_3_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C8")
    SetMapObjFrame(0xFF, "t1040_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky_y", 0x1, 0x1)
    Jump("loc_5EC")

    label("loc_5C8")

    SetMapObjFrame(0xFF, "t1040_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky_y", 0x0, 0x1)

    label("loc_5EC")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_655")
    LoadEffect(0x0, "event\\eva00_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -102930, 800, 14990, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_655")

    Return()

    # Function_3_591 end

    def Function_4_656(): pass

    label("Function_4_656")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EA")
    Jump("loc_734")

    label("loc_6EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_734")

    label("loc_70A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_734")

    label("loc_72A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_734")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81D")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "#3403FHmm, I suppose this place flaunts its\x01",
            "high-class reputation for a reason.\x02\x03",
            "#3400FStill...\x02\x03",
            "#3404F(I still think I prefer Mrs. Mao's\x01",
            "old-fashioned way of cooking.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8D4")

    label("loc_81D")


    ChrTalk(
        0xFE,
        (
            "#3405FOh, were you planning to have lunch\x01",
            "here as well?\x02\x03",
            "#3400FIt's quite delicious, but it will burn a\x01",
            "hole in your wallet. If you feel up to\x01",
            "it, why don't you order something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_656 end

    def Function_5_8DC(): pass

    label("Function_5_8DC")

    Call(0, 6)
    Return()

    # Function_5_8DC end

    def Function_6_8E0(): pass

    label("Function_6_8E0")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA2")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_93E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95E")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B9D")

    label("loc_95E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_972")
    Jump("loc_B9D")

    label("loc_972")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_999")
    Jump("loc_B9D")

    label("loc_999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_9A7")
    Jump("loc_B9D")

    label("loc_9A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_9B5")
    Jump("loc_B9D")

    label("loc_9B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_9C3")
    Jump("loc_B9D")

    label("loc_9C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_9D1")
    Jump("loc_B9D")

    label("loc_9D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A80")

    ChrTalk(
        0x9,
        (
            "The sun is setting. Won't be long until\x01",
            "all the tourists start making their way\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That gives us a little time to prepare\x01",
            "for the late-night crowd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9D")

    label("loc_A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_B94")

    ChrTalk(
        0x9,
        (
            "Welcome to Fortuna, the best restaurant\x01",
            "this side of Lake Elm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please come try each and every one of\x01",
            "our delicately crafted dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I can assure you that no matter which you\x01",
            "choose, our first-rate ingredients will send\x01",
            "you into a daze of ecstasy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9D")

    label("loc_B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B9D")

    label("loc_B9D")

    Jump("loc_8ED")

    label("loc_BA2")

    TalkEnd(0x9)
    Return()

    # Function_6_8E0 end

    def Function_7_BA6(): pass

    label("Function_7_BA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_BB7")
    Jump("loc_F39")

    label("loc_BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_BC5")
    Jump("loc_F39")

    label("loc_BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_BD3")
    Jump("loc_F39")

    label("loc_BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_BE1")
    Jump("loc_F39")

    label("loc_BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_BEF")
    Jump("loc_F39")

    label("loc_BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_D77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE1")

    ChrTalk(
        0xFE,
        (
            "Occasionally, a really sweaty, middle-aged\x01",
            "man comes to eat lunch here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the look of him, I have him pinned\x01",
            "as a park worker, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wait, don't tell me he's...Mishy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Forget I said anything.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D72")

    label("loc_CE1")


    ChrTalk(
        0xFE,
        (
            "Occasionally, a really sweaty, middle-aged\x01",
            "man comes to eat lunch here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wait, don't tell me he's...Mishy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Forget I said anything.\x02",
    )

    CloseMessageWindow()

    label("loc_D72")

    Jump("loc_F39")

    label("loc_D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6B")

    ChrTalk(
        0xFE,
        (
            "That Eastern woman has been frowning\x01",
            "ever since she stepped inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way... Is she one of our\x01",
            "competitors' spies?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, now that I think about it, we\x01",
            "really don't have any competitors...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F2B")

    label("loc_E6B")


    ChrTalk(
        0xFE,
        (
            "You know, now that I think about it,\x01",
            "we don't really have any competitors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe I mistook a customer for\x01",
            "a spy. My immaturity has gotten the best\x01",
            "of me for the last time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2B")

    Jump("loc_F39")

    label("loc_F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F39")

    label("loc_F39")

    TalkEnd(0xFE)
    Return()

    # Function_7_BA6 end

    def Function_8_F3D(): pass

    label("Function_8_F3D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*munch* *munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dad! Hurry up and eat so we\x01",
            "can get back to the theme park!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_F3D end

    def Function_9_FA2(): pass

    label("Function_9_FA2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1036")
    Jump("loc_1080")

    label("loc_1036")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1056")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1080")

    label("loc_1056")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1076")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1080")

    label("loc_1076")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1080")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116E")

    ChrTalk(
        0xFE,
        (
            "All the food in the park looked unappetizing\x01",
            "to me, so we decided to take a break and\x01",
            "eat here for lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*munch* *munch* *munch*\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "Whoa, remember to chew your food.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_11C7")

    label("loc_116E")

    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "I know you're eager to get back to the\x01",
            "park, but we've still got a lot of time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_FA2 end

    def Function_10_11CF(): pass

    label("Function_10_11CF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1263")
    Jump("loc_12AD")

    label("loc_1263")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1283")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12AD")

    label("loc_1283")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12A3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12AD")

    label("loc_12A3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12AD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "You know how the IBC funds Mishelam\x01",
            "and all of its construction, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From what I've heard, the best chef\x01",
            "at the IBC's Mishelam screenings was\x01",
            "given the mira to open this restaurant.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_11CF end

    def Function_11_139D(): pass

    label("Function_11_139D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1431")
    Jump("loc_147B")

    label("loc_1431")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1451")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_147B")

    label("loc_1451")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1471")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_147B")

    label("loc_1471")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_147B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "This restaurant's chef is out of this world!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_139D end

    def Function_12_14DA(): pass

    label("Function_12_14DA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_156E")
    Jump("loc_15B8")

    label("loc_156E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_158E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15B8")

    label("loc_158E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15AE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15B8")

    label("loc_15AE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15B8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169A")

    ChrTalk(
        0xFE,
        (
            "I bought a really pretty dress at the boutique,\x01",
            "but the jewelry shop said no first-time customers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ugh, what a stupid rule. Nothing to do\x01",
            "but eat my anger away!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_16BE")

    label("loc_169A")


    ChrTalk(
        0xFE,
        "Time to eat all my anger away!\x02",
    )

    CloseMessageWindow()

    label("loc_16BE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_14DA end

    def Function_13_16C6(): pass

    label("Function_13_16C6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_175A")
    Jump("loc_17A4")

    label("loc_175A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_177A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17A4")

    label("loc_177A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_179A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17A4")

    label("loc_179A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17A4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_194E")

    ChrTalk(
        0xFE,
        (
            "To be honest, I'm thanking the Goddess\x01",
            "that she wasn't allowed in the jewelry store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering she already bought a nice dress\x01",
            "at the boutique, I would have been on the verge\x01",
            "of bankruptcy if she bought a ring or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe this restaurant wasn't the greatest idea,\x01",
            "either, now that I'm looking at the prices... My\x01",
            "wallet isn't going to like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_19B2")

    label("loc_194E")


    ChrTalk(
        0xFE,
        (
            "Now that I'm looking at the prices here,\x01",
            "I'm starting to get a little worried for my\x01",
            "wallet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_16C6 end

    def Function_14_19BA(): pass

    label("Function_14_19BA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A4E")
    Jump("loc_1A98")

    label("loc_1A4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A6E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A98")

    label("loc_1A6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A8E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A98")

    label("loc_1A8E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A98")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8F")

    ChrTalk(
        0xFE,
        "What a magnificent taste! How divine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I try out everything, from cheap meals to\x01",
            "delectable 3-star restaurants! And now that\x01",
            "this dish has graced my plate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Bravo! I say bravo!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1BF9")

    label("loc_1B8F")


    ChrTalk(
        0xFE,
        (
            "Mishelam's esteemed restaurant has made\x01",
            "quite the impression on me, I must say!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Bravo, Fortuna!\x02",
    )

    CloseMessageWindow()

    label("loc_1BF9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_19BA end

    def Function_15_1C01(): pass

    label("Function_15_1C01")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C95")
    Jump("loc_1CDF")

    label("loc_1C95")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1CB5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CDF")

    label("loc_1CB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CD5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CDF")

    label("loc_1CD5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CDF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Tonight, I'm finally taking my wife to\x01",
            "Speaker Hartmann's annual party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's quite the wild event. I can't wait\x01",
            "to see how she'll react to the\x01",
            "extravagance of it all.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_1C01 end

    def Function_16_1DBD(): pass

    label("Function_16_1DBD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E51")
    Jump("loc_1E9B")

    label("loc_1E51")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E71")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E9B")

    label("loc_1E71")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E91")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E9B")

    label("loc_1E91")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E9B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Riding the ferris wheel with my husband\x01",
            "was the highlight of my day. It's not often\x01",
            "we get to take it easy like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being able to enjoy myself without forcing\x01",
            "him on the more intense park rides was\x01",
            "quite the treat.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_1DBD end

    def Function_17_1FAB(): pass

    label("Function_17_1FAB")

    Call(0, 18)
    Return()

    # Function_17_1FAB end

    def Function_18_1FAF(): pass

    label("Function_18_1FAF")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_211B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_200D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_200D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202D")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2116")

    label("loc_202D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2041")
    Jump("loc_2116")

    label("loc_2041")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2116")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x14,
        (
            "Here at Boutique Colserica, we have a\x01",
            "vast arrangement of clothes and styles\x01",
            "to choose from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "If you'd like, one of our employees would\x01",
            "love to help you find that perfect outfit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2116")

    Jump("loc_1FBC")

    label("loc_211B")

    TalkEnd(0x14)
    Return()

    # Function_18_1FAF end

    def Function_19_211F(): pass

    label("Function_19_211F")

    TalkBegin(0xFE)
    TurnDirection(0x15, 0x16, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213B")
    Call(0, 21)
    Jump("loc_216F")

    label("loc_213B")


    ChrTalk(
        0xFE,
        "Oh, my, that looks absolutely splendid on you.\x02",
    )

    CloseMessageWindow()

    label("loc_216F")

    TalkEnd(0xFE)
    Return()

    # Function_19_211F end

    def Function_20_2173(): pass

    label("Function_20_2173")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218F")
    OP_93(0xFE, 0x5A, 0x0)
    Call(0, 21)
    Jump("loc_21DF")

    label("loc_218F")


    ChrTalk(
        0x16,
        (
            "Hmm, she's right. I think this dress\x01",
            "might bring out my finer points... ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DF")

    TalkEnd(0xFE)
    Return()

    # Function_20_2173 end

    def Function_21_21E3(): pass

    label("Function_21_21E3")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "Oh, my... That dress fits you\x01",
            "like a glove, dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "You think so? Who am I to argue\x01",
            "with a professional? I'll take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Wonderful. If you don't mind, I'll take\x01",
            "your measurements right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_21_21E3 end

    def Function_22_22C1(): pass

    label("Function_22_22C1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "We've been in here for not even a minute, and\x01",
            "she's already bought an expensive dress...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, Goddess! All my savings...!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_22C1 end

    def Function_23_234B(): pass

    label("Function_23_234B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x32A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32A, 1)
    Return()

    # Function_23_234B end

    def Function_24_2398(): pass

    label("Function_24_2398")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, 0, -3000, 0)
    SetChrPos(0x102, 0, 0, -3000, 0)
    SetChrPos(0x103, 0, 0, -3000, 0)
    SetChrPos(0x104, 0, 0, -3000, 0)
    SetChrPos(0x151, 0, 0, -3000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, 1860, 0, 5910, 90)
    OP_68(-2760, 200, 3570, 0)
    MoveCamera(345, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(21520, 0)
    FadeToBright(1000, 0)
    OP_68(-2760, 200, 5070, 7000)
    BeginChrThread(0x101, 3, 0, 25)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 27)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 28)
    Sleep(1000)
    BeginChrThread(0x151, 3, 0, 29)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x151, 3)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3500568V#0011F#12PI don't think our budget covers a\x01",
            "place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500569V#0304F#6PWell, it is a pretty fancy store.\x02\x03",
            "#3500570V#0300FClassy suits, casual clothes...\x01",
            "They basically got stuff for\x01",
            "every occasion here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        "#3500571V#5704F#6PImpressive prices, too.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#3500572V#0100F#6PWe don't need to worry about prices.\x02\x03",
            "#3500573VLloyd, have you decided who you want\x01",
            "to bring with you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2669():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2669)
    Sleep(100)

    def lambda_2679():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2679)

    def lambda_2686():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2686)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x151, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3500574V#0004F#11PYeah, I think so.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Bring Elie\x01",       # 0
            "Bring Tio\x01",        # 1
            "Bring Randy\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2728"),
        (1, "loc_2A74"),
        (2, "loc_2F1F"),
        (SWITCH_DEFAULT, "loc_36A8"),
    )


    label("loc_2728")

    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 1)
    OP_29(0x47, 0x1, 0x6)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3500575V#0000F#11PElie, would you mind accompanying me?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#3500576V#0104F#6PI'd love to.\x02\x03",
            "#3500577V#0102FThe two of us will probably look the most\x01",
            "inconspicuous trying to enter the venue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500578V#0002F#11PDefinitely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3500579V#5702F#6PHaha, wonderful choice. If I were you,\x01",
            "I'd dress as an ordinary couple.\x02\x03",
            "#3500580V#5703FA wealthy young dame, along with her\x01",
            "commoner boyfriend, attempts to join\x01",
            "in on a much-talked-about party...\x02\x03",
            "#3500581V#5700FA convincing facade, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500582V#0005F#11PI think we could pull that off...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500583V#0106F#6P...You could at least pretend to be\x01",
            "flustered at that idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500584V#0309F#6PHaha, better go get yourself dolled up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500585V#0202F#12PI am curious to see how this transformation\x01",
            "will play out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_2A74")

    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 2)
    OP_29(0x47, 0x1, 0x7)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3500586V#0000F#5PWould you be okay with tagging\x01",
            "along, Tio?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#3500587V#0205F#12PAre you sure?\x02\x03",
            "#3500588V#0206FAllow me to stress: I am NOT a child.\x01",
            "However, I would still probably stand\x01",
            "out compared to the other attendees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500589V#0004F#5PYeah, I agree.\x02\x03",
            "#3500590V#0000FBut on the other hand, I doubt anyone\x01",
            "would peg us for police officers if you\x01",
            "were with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500591V#0205F#12POh, I see...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x151,
        (
            "#3500592V#5702F#6PClever. I saw a girl around the same\x01",
            "age as Tio last year, so that very well\x01",
            "might be the best way in.\x02\x03",
            "#3500593V#5704FI can see it now. A pair of noble siblings, naive\x01",
            "in the ways of this corrupt world, who hail from\x01",
            "a small, insignificant country...\x02\x03",
            "#3500594V#5700FDoes that backstory suit your fancy?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DA5():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DA5)

    def lambda_2DB2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2DB2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3500595V#0005F#11PI-It could work, yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500596V#0205F#11PSo that means Lloyd and I are siblings...?\x02",
    )

    CloseMessageWindow()

    def lambda_2E3D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E3D)
    Sleep(50)

    def lambda_2E4D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2E4D)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#3500597V#0109F#5PDespite looking completely different,\x01",
            "I think you two could pull that off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500598V#0302F#6PSounds like a plan. You two better\x01",
            "go get yourselves lookin' all spiffy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_2F1F")

    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 3)
    OP_29(0x47, 0x1, 0x8)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3500599V#0000F#5PRandy. Would you mind tag-teaming\x01",
            "this with me?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#3500600V#0305F#6PI don't mind, but wouldn't two dudes\x01",
            "goin' together be kinda weird?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500601V#0006F#5PYeah, I'm not a fan of it, either...\x02",
    )

    CloseMessageWindow()

    def lambda_3036():
        OP_93(0xFE, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3036)

    def lambda_3043():
        OP_93(0xFE, 0x10E, 0xC8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3043)

    def lambda_3050():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3050)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3500602V#0008F#5P(But the mafia is running this thing, right?\x01",
            "I'm less a fan of bringing a girl into the\x01",
            "lion's den with me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500603V#0300F#6P(Can't argue with that gentlemanly logic.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500604V#0111F#5PExcuse me. What exactly are you\x01",
            "two whispering about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500605V#0211F#12PUnbelievable... When were you planning\x01",
            "to tell us about your relationship?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        "#3500606V#0012F#5PThat's definitely not the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500607V#0309F#6PHey, if you're into that kinda thing,\x01",
            "I ain't goin' to be the one to judge!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3500608V#5702F#6PHaha, you act like I haven't seen two men\x01",
            "come to the auction together before.\x02\x03",
            "#3500609V#5704F#6PThink of it like this. An honest rich kid, raised\x01",
            "by a loving family, was tricked into attending\x01",
            "a party by his good-for-nothing friend.\x02\x03",
            "#3500610V#5700FHow does that sound?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_33B2():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33B2)
    Sleep(50)

    def lambda_33C2():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33C2)
    Sleep(50)

    def lambda_33D2():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_33D2)
    Sleep(50)

    def lambda_33E2():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_33E2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3500611V#0005F#11PThat might actually work...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500612V#0302F#12PHaha. Hell yeah.\x02",
    )

    CloseMessageWindow()

    def lambda_344F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_344F)
    WaitChrThread(0x103, 1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#3500613V#0105F#5PIf we're going with that, you should try to\x01",
            "find something flashy to wear, Randy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34CC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34CC)
    WaitChrThread(0x102, 1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#3500614V#0109F#5PAnd Lloyd, try to find something more...\x01",
            "traditional-looking to match your role.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3548():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3548)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x103,
        (
            "#3500615V#0202F#12PI think we should take this rare opportunity\x01",
            "to find the optimal outfits for these two.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_35FC():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35FC)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3500616V#0011F#5PHey, let's not go overboard here...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#3500617V#0306F#6PChill, Lloyd. It's time to man up and\x01",
            "be the models they want us to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A8")

    SetCameraDistance(22020, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_36CF")
    Call(0, 30)
    Jump("loc_36EC")

    label("loc_36CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_36E0")
    Call(0, 31)
    Jump("loc_36EC")

    label("loc_36E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_36EC")
    Call(0, 32)

    label("loc_36EC")

    Return()

    # Function_24_2398 end

    def Function_25_36ED(): pass

    label("Function_25_36ED")


    def lambda_36F2():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36F2)

    def lambda_370C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_370C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3725():
        OP_95(0xFE, 0, 0, 2020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3725)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_25_36ED end

    def Function_26_3746(): pass

    label("Function_26_3746")


    def lambda_374B():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_374B)

    def lambda_3765():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3765)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_377E():
        OP_95(0xFE, -790, 0, 650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_377E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_26_3746 end

    def Function_27_379F(): pass

    label("Function_27_379F")


    def lambda_37A4():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37A4)

    def lambda_37BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_37BE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_37D7():
        OP_95(0xFE, 870, 0, 920, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37D7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_27_379F end

    def Function_28_37F8(): pass

    label("Function_28_37F8")


    def lambda_37FD():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37FD)

    def lambda_3817():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3817)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3830():
        OP_95(0xFE, 0, 0, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3830)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_37F8 end

    def Function_29_3851(): pass

    label("Function_29_3851")


    def lambda_3856():
        OP_95(0xFE, -460, 0, -1690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3856)

    def lambda_3870():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3870)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3889():
        OP_95(0xFE, -1630, 0, -530, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3889)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_29_3851 end

    def Function_30_38AA(): pass

    label("Function_30_38AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    SetChrChipPat(0x1, 0x1, 0x4D)
    LoadChrChipPat()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05300.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetChrPos(0x101, -7700, 0, 9950, 180)
    SetChrPos(0x102, -6350, 0, 9950, 180)
    SetChrPos(0x103, -6350, 0, 8150, 0)
    SetChrPos(0x104, -7000, 0, 6850, 0)
    SetChrPos(0x151, -7700, 0, 8150, 0)
    FadeToBright(1000, 0)
    OP_68(-7640, 900, 9240, 0)
    MoveCamera(311, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2500)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x102,
        "#3500618VSorry to keep you waiting!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#3500619VHopefully, these will be okay...\x02",
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
        0x104,
        (
            "#3500620V#0305F#6PHmmm, not too shabby.\x02\x03",
            "#3500621V#0309FDamn! You're workin' that dress!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500622V#0204F#6PYes. Elie looks beautiful...\x02\x03",
            "#3500623V#0202FAnd your outfit suits you quite well, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500624V#5005F#11PYou think so...?\x02\x03",
            "#3500625V#5006FHonestly, I think I pale in comparison to Elie.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#3500626V#5304F#12PHeehee. That's not true!\x02\x03",
            "#3500627V#5302FYou pull off that suit well with your\x01",
            "broad shoulders.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#3500628V#5004F#5PThanks for the vote of confidence, Elie.\x02\x03",
            "#3500629V#5000FHopefully, I'll be able to pull off being your\x01",
            "boyfriend for one night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500630V#5313F#12PW-Well, you certainly look the part.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3500631V#5704F#6PNo need for advice, I see.\x02\x03",
            "#3500632V#5702FWell, I'll do you another favor.\x01",
            "Wear these, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E37():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E37)

    def lambda_3E44():

        label("loc_3E44")

        TurnDirection(0x102, 0x101, 200)
        Yield()
        Jump("loc_3E44")

    QueueWorkItem2(0x102, 1, lambda_3E44)

    def lambda_3E56():

        label("loc_3E56")

        TurnDirection(0x103, 0x101, 200)
        Yield()
        Jump("loc_3E56")

    QueueWorkItem2(0x103, 1, lambda_3E56)

    def lambda_3E68():

        label("loc_3E68")

        TurnDirection(0x104, 0x101, 200)
        Yield()
        Jump("loc_3E68")

    QueueWorkItem2(0x104, 1, lambda_3E68)

    def lambda_3E7A():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3E7A)
    WaitChrThread(0x151, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)

    ChrTalk(
        0x101,
        "#3500633V#5005F#11PGlasses...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3500634V#5703F#6PWhen women get all dressed up, it's as\x01",
            "if they become a whole different person.\x02\x03",
            "#3500675V#5700FHowever, formal attire doesn't do much\x01",
            "to change your look, Lloyd.\x02\x03",
            "#3500676VWhile you're at the auction, it'd be better to\x01",
            "wear something that will add to the disguise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500677V#5000F#11PThat's a good idea. Thanks, Wazy.\x02",
    )

    CloseMessageWindow()

    def lambda_4021():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4021)
    WaitChrThread(0x151, 1)
    Sleep(300)
    Fade(1000)
    Sound(820, 0, 100, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#3500678VHow do I look?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    ChrTalk(
        0x151,
        "#3500679V#5702F#6PHmm, interesting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500680V#5302F#12PWow, I'm surprised. I bet you'll give off a\x01",
            "completely different first impression now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500681V#0202F#6PI was not expecting them to work as well\x01",
            "as they do. I like them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500682V#0309F#6PSounds like they're a hit, Lloyd! Maybe you\x01",
            "should get yourself a pair after this is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500683V#5106F#11PMy eyes are fine as is...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3500684V#5004F#11PAll right. With this, all our preparations\x01",
            "should be complete.\x02\x03",
            "#3500685V#5000FAll that's left is for us to wait until the\x01",
            "auction starts.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_38AA end

    def Function_31_4379(): pass

    label("Function_31_4379")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    SetChrChipPat(0x2, 0x1, 0x4E)
    LoadChrChipPat()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05400.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetChrPos(0x101, -7700, 0, 9950, 180)
    SetChrPos(0x102, -6350, 0, 8150, 0)
    SetChrPos(0x103, -6350, 0, 9950, 180)
    SetChrPos(0x104, -7000, 0, 6850, 0)
    SetChrPos(0x151, -7700, 0, 8150, 0)
    FadeToBright(1000, 0)
    OP_68(-7640, 900, 9240, 0)
    MoveCamera(311, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2500)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#3500635VWell, this is what we decided on.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x103,
        (
            "#3500636VI still think this is a bit too\x01",
            "frilly for my taste...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x102,
        (
            "#3500637V#0109F#6POh, you both look wonderful!\x02\x03",
            "#3500638V#0102FLloyd looks dashing in the suit,\x01",
            "but you look adorable, Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500639V#0304F#6PWell, it's not every day you see Tio Tot\x01",
            "in regular clothes.\x02\x03",
            "#3500640V#0300FThat look is a breath of fresh air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500641V#5405F#11PA-Are you being facetious...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#3500642V#5002F#5PNot at all, Tio. You look great.\x02\x03",
            "#3500643V#5004FThough, I'm not sure if these outfits are\x01",
            "good for the siblings story we had lined up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3500644V#5702F#6PNo big deal. How about we change it to a\x01",
            "butler escorting his young mistress to a\x01",
            "lovely party?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x151, 400)

    ChrTalk(
        0x101,
        "#3500645V#5000F#11PPerfect!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#3500646V#5403F#12PI think I would rather stay siblings.\x02\x03",
            "#3500647V#5402FI doubt I am cut out for being a mistress.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#3500648V#5005F#5PAre you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3500649V#5704F#6POh, I'm sure she has her reasons\x01",
            "for preferring that one.\x02\x03",
            "#3500650V#5702FWell, I'll do you another favor.\x01",
            "Wear these, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49DF():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49DF)

    def lambda_49EC():

        label("loc_49EC")

        TurnDirection(0x102, 0x101, 200)
        Yield()
        Jump("loc_49EC")

    QueueWorkItem2(0x102, 1, lambda_49EC)

    def lambda_49FE():

        label("loc_49FE")

        TurnDirection(0x103, 0x101, 200)
        Yield()
        Jump("loc_49FE")

    QueueWorkItem2(0x103, 1, lambda_49FE)

    def lambda_4A10():

        label("loc_4A10")

        TurnDirection(0x104, 0x101, 200)
        Yield()
        Jump("loc_4A10")

    QueueWorkItem2(0x104, 1, lambda_4A10)

    def lambda_4A22():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4A22)
    WaitChrThread(0x151, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)

    ChrTalk(
        0x101,
        "#3500651V#5005F#11PGlasses...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3500652V#5703F#6PWhen women get all dressed up, it's as\x01",
            "if they become a whole different person.\x02\x03",
            "#3500675V#5700FHowever, formal attire doesn't do much\x01",
            "to change your look, Lloyd.\x02\x03",
            "#3500676VWhile you're at the auction, it'd be better to\x01",
            "wear something that will add to the disguise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500677V#5000F#11PThat's a good idea. Thanks, Wazy.\x02",
    )

    CloseMessageWindow()

    def lambda_4BC9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4BC9)
    WaitChrThread(0x151, 1)
    Sleep(300)
    Fade(1000)
    Sound(820, 0, 100, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#3500678VHow do I look?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    ChrTalk(
        0x151,
        "#3500679V#5702F#6PHmm, interesting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500680V#0102F#6PWow, I'm surprised. I bet you'll give off a\x01",
            "completely different first impression now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500681V#5402F#12PI was not expecting them to work as well\x01",
            "as they do. I like them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500682V#0309F#6PSounds like they're a hit, Lloyd! Maybe you\x01",
            "should get yourself a pair after this is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500683V#5106F#11PMy eyes are fine as is...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3500684V#5004F#11PAll right. With this, all our preparations\x01",
            "should be complete.\x02\x03",
            "#3500685V#5000FAll that's left is for us to wait until the\x01",
            "auction starts.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4379 end

    def Function_32_4F21(): pass

    label("Function_32_4F21")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    SetChrChipPat(0x3, 0x1, 0x4F)
    LoadChrChipPat()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05600.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetChrPos(0x101, -7700, 0, 9950, 180)
    SetChrPos(0x102, -7000, 0, 6850, 0)
    SetChrPos(0x103, -6350, 0, 8150, 0)
    SetChrPos(0x104, -6350, 0, 9950, 180)
    SetChrPos(0x151, -7700, 0, 8150, 0)
    FadeToBright(1000, 0)
    OP_68(-7640, 900, 9240, 0)
    MoveCamera(311, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2500)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#3500653VSorry about the wait, everyone.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 30, 3)
    Sleep(500)

    AnonymousTalk(
        0x104,
        (
            "#3500654VI think we did good, for what\x01",
            "it's worth.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x102,
        "#3500655V#0105F#6POh, wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500656V#0201F#6PHmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#3500657V#5011F#11PCrap. Judging by your faces,\x01",
            "I look silly, don't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500658V#5605F#11PHey, I thought I looked pretty damn\x01",
            "slick in this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500659V#0102F#6PNo, don't worry. You both look fantastic.\x02\x03",
            "#3500660V#0109FI was just surprised by how much the\x01",
            "outfits match Wazy's story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500661V#0204F#6P'An honest rich kid, raised by a loving family,\x01",
            "was tricked into attending a party by his\x01",
            "good-for-nothing friend.'\x02\x03",
            "#3500662V#0202FIt is almost uncanny.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        "#3500663V#5005F#5PIs it really?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(
        0x104,
        (
            "#3500664V#5609F#12PLemme teach you a few of my tricks before we\x01",
            "hit the scene, Lloyd. Can't have you lettin'\x01",
            "down any ladies at the auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500665V#0107F#6PDo NOT do that!\x02\x03",
            "#3500666V#0111FLloyd already has some kind of curse\x01",
            "to begin with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500667V#0211F#6PIf he learns anything else, we will not\x01",
            "be able to keep him on his leash.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500668V#5603F#12PGood point... I forgot how dangerous\x01",
            "this guy can be.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3500669V#5011F#5PWait just a second!\x02\x03",
            "#3500670V#5013FI don't appreciate all these underhanded\x01",
            "and FALSE comments about me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3500671V#5709F#6PHaha, a man loved by many.\x02\x03",
            "#3500672V#5702FWell, I'll do you another favor.\x01",
            "Wear these, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_56ED():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56ED)

    def lambda_56FA():

        label("loc_56FA")

        TurnDirection(0x102, 0x101, 200)
        Yield()
        Jump("loc_56FA")

    QueueWorkItem2(0x102, 1, lambda_56FA)

    def lambda_570C():

        label("loc_570C")

        TurnDirection(0x103, 0x101, 200)
        Yield()
        Jump("loc_570C")

    QueueWorkItem2(0x103, 1, lambda_570C)

    def lambda_571E():

        label("loc_571E")

        TurnDirection(0x104, 0x101, 200)
        Yield()
        Jump("loc_571E")

    QueueWorkItem2(0x104, 1, lambda_571E)

    def lambda_5730():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5730)
    WaitChrThread(0x151, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)

    ChrTalk(
        0x101,
        "#3500673V#5005F#11PGlasses...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3500674V#5703F#6PYou see, Randy makes quite the new, bold\x01",
            "statement with his showy getup.\x02\x03",
            "#3500675V#5700FHowever, formal attire doesn't do much\x01",
            "to change your look, Lloyd.\x02\x03",
            "#3500676VWhile you're at the auction, it'd be better to\x01",
            "wear something that will add to the disguise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500677V#5000F#11PThat's a good idea. Thanks, Wazy.\x02",
    )

    CloseMessageWindow()

    def lambda_58D0():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_58D0)
    WaitChrThread(0x151, 1)
    Sleep(300)
    Fade(1000)
    Sound(820, 0, 100, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#3500678VHow do I look?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    ChrTalk(
        0x151,
        "#3500679V#5702F#6PHmm, interesting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500680V#0102F#6PWow, I'm surprised. I bet you'll give off a\x01",
            "completely different first impression now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500681V#0202F#6PI was not expecting them to work as well\x01",
            "as they do. I like them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500682V#5609F#12PSounds like they're a hit, Lloyd! Maybe you\x01",
            "should get yourself a pair after this is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500683V#5106F#5PMy eyes are fine as is...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3500684V#5004F#11PAll right. With this, all our preparations\x01",
            "should be complete.\x02\x03",
            "#3500685V#5000FAll that's left is for us to wait until the\x01",
            "auction starts.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_4F21 end

    def Function_33_5C27(): pass

    label("Function_33_5C27")

    EventBegin(0x0)
    Fade(500)
    OP_68(-102630, 1400, 14570, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21880, 0)
    SetChrPos(0x101, -101580, 0, 14400, 270)
    SetChrPos(0x102, -101560, 0, 15620, 225)
    SetChrPos(0x103, -101840, 0, 13530, 315)
    SetChrPos(0x104, -100390, 0, 14710, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5CBA")
    SetChrPos(0x151, -100780, 0, 13600, 270)

    label("loc_5CBA")

    StopEffect(0x0, 0x2)
    SetChrFlags(0xA, 0x80)
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
            scpstr(SCPSTR_CODE_ITEM, 0x34E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34E, 1)

    ChrTalk(
        0x101,
        (
            "#11P#0005FI wasn't expecting to find a ring\x01",
            "in a place like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FIt is possible that this could be the engagement\x01",
            "ring Toma had mentioned.\x02\x03",
            "We should make time to confirm this with him\x01",
            "in his hotel room, if possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x5)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, -101580, 0, 14400, 270)
    ClearChrFlags(0xA, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_5C27 end

    SaveToFile()

Try(main)
