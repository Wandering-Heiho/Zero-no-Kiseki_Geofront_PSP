from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0150.bin",                # FileName
        "c0150",                    # MapName
        "c0150",                    # Location
        0x0007,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 7, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0150",                  # 0
        "Hoisdorf",               # 1
        "Braun",                  # 2
        "Selteo",                 # 3
        "Nonno",                  # 4
        "Secretary Ernest",       # 5
        "Grace",                  # 6
        "Flotte",                 # 7
        "Kendall",                # 8
        "Businessman",            # 9
        "Businessman",            # 10
        "Tourist",                # 11
        "Citizen",                # 12
        "Citizen",                # 13
        "Citizen",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Tourist",                # 17
        "Tourist",                # 18
        "Mediator",               # 19
        "Young Man",              # 20
        "Woman",                  # 21
        "Tourist",                # 22
        "Tourist",                # 23
        "Tourist",                # 24
        "Gironde",                # 25
        "Inspector Donovan",      # 26
        "Detective Raymond",      # 27
        "Chief Roberts",          # 28
        "Fran",                   # 29
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch21302.itc",                   # 04
        "chr/ch27600.itc",                   # 05
        "chr/ch20402.itc",                   # 06
        "chr/ch32302.itc",                   # 07
        "chr/ch33202.itc",                   # 08
        "chr/ch21002.itc",                   # 09
        "chr/ch22002.itc",                   # 0A
        "chr/ch20502.itc",                   # 0B
        "chr/ch24102.itc",                   # 0C
        "chr/ch21202.itc",                   # 0D
        "chr/ch24502.itc",                   # 0E
        "chr/ch23702.itc",                   # 0F
        "chr/ch21802.itc",                   # 10
        "chr/ch20200.itc",                   # 11
        "chr/ch27602.itc",                   # 12
        "chr/ch02302.itc",                   # 13
        "chr/ch30300.itc",                   # 14
        "chr/ch30200.itc",                   # 15
        "chr/ch06002.itc",                   # 16
        "chr/ch29300.itc",                   # 17
        "chr/ch34302.itc",                   # 18
    ))

    DeclNpc(-509,    0,       12449,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-42889,  0,       5699,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-52029,  0,       3650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-8880,   0,       3240,    45,   261,  0x0, 0,   3,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(-3250,   150,     4570,    180,  469,  0x0, 0,   19,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-3299,   0,       4480,    180,  469,  0x0, 0,   22,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(-7449,   150,     8510,    270,  341,  0x0, 0,   24,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(2450,    5150,    17559,   180,  469,  0x0, 0,   16,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(8739,    5000,    14520,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(2450,    5150,    13479,   0,    469,  0x0, 0,   18,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(4559,    150,     5920,    180,  469,  0x0, 0,   6,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(3259,    150,     -6150,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   21,  255,  0)
    DeclNpc(1009,    0,       -3920,   90,   469,  0x0, 0,   12,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(1009,    0,       -3920,   90,   469,  0x0, 0,   9,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   6,   0,   255, 255, 0,   24,  255,  0)
    DeclNpc(6400,    5150,    13449,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(6400,    5150,    17700,   180,  469,  0x0, 0,   11,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(1009,    0,       -3920,   90,   469,  0x0, 0,   13,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   6,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   4,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(3210,    150,     -1879,   180,  469,  0x0, 0,   15,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(3210,    150,     -6130,   0,    469,  0x0, 0,   14,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-1159,   150,     2180,    270,  469,  0x0, 0,   7,   0,   255, 255, 0,   32,  255,  0)
    DeclNpc(60580,   -1000,   -8600,   270,  261,  0x0, 0,   17,  0,   0,   0,   0,   5,   255,  0)
    DeclNpc(56610,   -1000,   -11899,  270,  405,  0x0, 0,   20,  0,   0,   0,   0,   6,   255,  0)
    DeclNpc(55229,   -1000,   -11899,  90,   405,  0x0, 0,   21,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(57790,   -1000,   -12300,  90,   405,  0x0, 0,   23,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(59140,   -1000,   -8880,   1500,    60580,   500,     -8600,   0x007E, 0,  4,  0x0000)
    DeclActor(-510,    0,       10640,   1000,    -510,    1500,    12450,   0x007E, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_518",          # 00, 0
        "Function_1_5D0",          # 01, 1
        "Function_2_66D",          # 02, 2
        "Function_3_8B5",          # 03, 3
        "Function_4_8E9",          # 04, 4
        "Function_5_8ED",          # 05, 5
        "Function_6_2AC9",         # 06, 6
        "Function_7_32C5",         # 07, 7
        "Function_8_341C",         # 08, 8
        "Function_9_3420",         # 09, 9
        "Function_10_42EB",        # 0A, 10
        "Function_11_56DC",        # 0B, 11
        "Function_12_5A36",        # 0C, 12
        "Function_13_6C91",        # 0D, 13
        "Function_14_798B",        # 0E, 14
        "Function_15_7A69",        # 0F, 15
        "Function_16_7E47",        # 10, 16
        "Function_17_94D3",        # 11, 17
        "Function_18_985B",        # 12, 18
        "Function_19_9A4F",        # 13, 19
        "Function_20_9C66",        # 14, 20
        "Function_21_9EBE",        # 15, 21
        "Function_22_A11F",        # 16, 22
        "Function_23_A2C2",        # 17, 23
        "Function_24_A58F",        # 18, 24
        "Function_25_A843",        # 19, 25
        "Function_26_A9A8",        # 1A, 26
        "Function_27_AD10",        # 1B, 27
        "Function_28_B0D0",        # 1C, 28
        "Function_29_B86B",        # 1D, 29
        "Function_30_BD2C",        # 1E, 30
        "Function_31_BFF5",        # 1F, 31
        "Function_32_C232",        # 20, 32
        "Function_33_C4AF",        # 21, 33
        "Function_34_C4B9",        # 22, 34
        "Function_35_C7C3",        # 23, 35
        "Function_36_CC96",        # 24, 36
        "Function_37_D275",        # 25, 37
        "Function_38_1127C",       # 26, 38
        "Function_39_11D6D",       # 27, 39
        "Function_40_12CBA",       # 28, 40
        "Function_41_12F1D",       # 29, 41
        "Function_42_13462",       # 2A, 42
    ))


    def Function_0_518(): pass

    label("Function_0_518")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_558"),
        (1, "loc_564"),
        (2, "loc_570"),
        (3, "loc_57C"),
        (4, "loc_588"),
        (5, "loc_594"),
        (6, "loc_5A0"),
        (SWITCH_DEFAULT, "loc_5AC"),
    )


    label("loc_558")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_564")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_570")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_57C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_588")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_594")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5CF")

    Return()

    # Function_0_518 end

    def Function_1_5D0(): pass

    label("Function_1_5D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66C")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_5D0")

    label("loc_66C")

    Return()

    # Function_1_5D0 end

    def Function_2_66D(): pass

    label("Function_2_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_67C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 37)

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6A6")
    SetChrPos(0xB, -7600, 0, 6990, 0)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_8B4")

    label("loc_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6B9")
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_8B4")

    label("loc_6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6D1")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_8B4")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_6DF")
    Jump("loc_8B4")

    label("loc_6DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6FC")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_8B4")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_70A")
    Jump("loc_8B4")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_74C")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrSubChip(0xD, 0x1)
    SetChrPos(0xB, -1730, 0, 4050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_8B4")

    label("loc_74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_777")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_772")
    ClearChrFlags(0xC, 0x80)

    label("loc_772")

    Jump("loc_8B4")

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7BC")
    SetChrPos(0xA, 6790, 0, 13090, 180)
    SetChrPos(0xB, 6790, 0, 11430, 0)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_8B4")

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7E3")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_8B4")

    label("loc_7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_800")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_8B4")

    label("loc_800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_82C")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_8B4")

    label("loc_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_84E")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_8B4")

    label("loc_84E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_870")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_8B4")

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_897")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_8B4")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8B4")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    label("loc_8B4")

    Return()

    # Function_2_66D end

    def Function_3_8B5(): pass

    label("Function_3_8B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8E8")

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8E8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8E8")

    label("loc_8E8")

    Return()

    # Function_3_8B5 end

    def Function_4_8E9(): pass

    label("Function_4_8E9")

    Call(0, 5)
    Return()

    # Function_4_8E9 end

    def Function_5_8ED(): pass

    label("Function_5_8ED")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B17")

    ChrTalk(
        0x20,
        (
            "As much as I wanna say come on in and\x01",
            "have a look around, I'm afraid I can't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "You can't buy a weapon in Crossbell\x01",
            "without a license, kids. So, if this is\x01",
            "a prank, then beat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe're actually from the CPD, sir.\x01",
            "Sorry for the confusion.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x20,
        "Y'all are police officers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, you must be those kids Sergei\x01",
            "told me about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Hmm, all right. Feel free to take a look\x01",
            "around the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "When you're ready to check out, show me\x01",
            "your Detective Notebook. That'll substitute\x01",
            "as a license.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 2)

    label("loc_B17")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC5")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B72")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B91")
    OP_AF(0x5)
    Jump("loc_BD3")

    label("loc_B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BA1")
    OP_AF(0x4)
    Jump("loc_BD3")

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BB1")
    OP_AF(0x3)
    Jump("loc_BD3")

    label("loc_BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BC1")
    OP_AF(0x2)
    Jump("loc_BD3")

    label("loc_BC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_BD1")
    OP_AF(0x1)
    Jump("loc_BD3")

    label("loc_BD1")

    OP_AF(0x0)

    label("loc_BD3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AC0")

    label("loc_BE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF6")
    Jump("loc_2AC0")

    label("loc_BF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C35")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 36)
    Jump("loc_2AC0")

    label("loc_C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_E62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC8")

    ChrTalk(
        0x20,
        (
            "'Fraid you can't stay here long this time\x01",
            "around, folks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "I'm about to close shop, so make it quick.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FGlad to see you still don't care about\x01",
            "sellin' anything, Gironde.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Doubt I ever will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "By the way, it sounds like something big\x01",
            "happened over at the airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Wonder if this has anything to do with the\x01",
            "sense of dread I've been feeling lately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E5D")

    label("loc_DC8")


    ChrTalk(
        0x20,
        (
            "Seems like something big happened over\x01",
            "at the airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Wonder if this has anything to do with the\x01",
            "sense of dread I've been feeling lately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5D")

    Jump("loc_2AC0")

    label("loc_E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_108D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1016")

    ChrTalk(
        0x20,
        "Well, if it isn't Alex Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Don't think I've ever seen you cooperate\x01",
            "with the Special Support Section before.\x01",
            "You finally burned out, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603FDon't think for a second that I'll let that\x01",
            "comment slide.\x02\x03",
            "#0600FAnd I'm hardly cooperating. I'm in charge\x01",
            "of this investigation, for your information!\x02\x03",
            "Though, I would appreciate it if you kept\x01",
            "your mouth shut about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "You got it, pal.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1088")

    label("loc_1016")


    ChrTalk(
        0x20,
        (
            "I still can't believe that you're working\x01",
            "with the Special Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "What a weird combination.\x02",
    )

    CloseMessageWindow()

    label("loc_1088")

    Jump("loc_2AC0")

    label("loc_108D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1281")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F3")

    ChrTalk(
        0x20,
        (
            "You seriously came to buy weapons this\x01",
            "early in the morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Learn to lighten up, kids.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "If you're looking for an upgrade, why not\x01",
            "save it for the afternoon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FCorrect me if I am wrong, sir, but it sounds\x01",
            "like you would rather laze about than see\x01",
            "to your patrons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "That's the long and short of it, yeah.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_127C")

    label("loc_11F3")


    ChrTalk(
        0x20,
        (
            "Relaxing and catching up on magazines\x01",
            "sounds much nicer than dealing with you\x01",
            "kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "So try not to stick around too long, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_127C")

    Jump("loc_2AC0")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_13F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137C")

    ChrTalk(
        0x20,
        (
            "Oh, come on... Before you start bothering\x01",
            "me, do you really need to buy anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "'Cause I'm not in the mood. You can take\x01",
            "a look around, but then you gotta scram.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FStill indifferent to potential buyers.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13F1")

    label("loc_137C")


    ChrTalk(
        0x20,
        (
            "Yeah, well, what's new? If you're really that\x01",
            "interested in what I've got, look around and\x01",
            "then leave me alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F1")

    Jump("loc_2AC0")

    label("loc_13F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_14AD")

    ChrTalk(
        0x20,
        (
            "Ohoh. If it isn't the Special Support\x01",
            "Section kids. You make a habit out\x01",
            "of working this late?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I've already closed up shop. Get on\x01",
            "back to that base of yours!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC0")

    label("loc_14AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_16D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163D")

    ChrTalk(
        0x20,
        (
            "Those Revache guys have been causing\x01",
            "more and more problems lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "'Cause of that, the bracers are always\x01",
            "complaining about how busy they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Wouldn't hurt for the CPD to try a little\x01",
            "harder, too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHahaha, maybe so. Sorry, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FY'know, it's the First Division who's\x01",
            "in charge of mafia stuff. Make sure\x01",
            "to chew their ears off next.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16CB")

    label("loc_163D")


    ChrTalk(
        0x20,
        (
            "Those Revache guys have been causing\x01",
            "more and more problems lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Can't say I'm jealous of how busy the\x01",
            "Bracer Guild must be now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CB")

    Jump("loc_2AC0")

    label("loc_16D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1A7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187F")

    ChrTalk(
        0x20,
        "You guys, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Haven't seen you for quite some\x01",
            "time. How's life been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, a bit of this, a bit of that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FWhoa, this place is cool! What the\x01",
            "heck is all this stuff, Lloyd?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x20,
        (
            "Hands off the merchandise, kid. It's\x01",
            "dangerous stuff. Way too dangerous\x01",
            "for someone like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Get outta here already!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "I don't sell any kids' toys here. Got it?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 7)
    Jump("loc_1A79")

    label("loc_187F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A10")

    ChrTalk(
        0x20,
        "Now get outta here already!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "You aren't going to find any toys in here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F(...He keeps saying that, but I'm sure\x01",
            "he'd find us something if we asked.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1976")

    ChrTalk(
        0x102,
        (
            "#0100F(Of course. He's a nice person, deep\x01",
            "down.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A08")

    label("loc_1976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_19CD")

    ChrTalk(
        0x103,
        (
            "#0200F(I agree. Despite his rough exterior,\x01",
            "he is a very kind man.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A08")

    label("loc_19CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1A08")

    ChrTalk(
        0x104,
        "#0300F(Well, yeah. He ain't such a bad guy.)\x02",
    )

    CloseMessageWindow()

    label("loc_1A08")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1A79")

    label("loc_1A10")


    ChrTalk(
        0x20,
        "C'mon, now! Get outta here already!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "You aren't going to find anything here\x01",
            "for that kid, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A79")

    Jump("loc_2AC0")

    label("loc_1A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1C12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7C")

    ChrTalk(
        0x20,
        (
            "Customers keep telling me about all the\x01",
            "messes the mafia keeps making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "One of the bracer guys wouldn't stop running\x01",
            "his mouth about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "What was it again...? Revache's having a\x01",
            "spat with some foreign mafia, too?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C0D")

    label("loc_1B7C")


    ChrTalk(
        0x20,
        "Tsk, tsk. Crossbell's as dangerous as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Boy, I feel bad for the tourists. They have no\x01",
            "idea what's going on beneath the surface.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0D")

    Jump("loc_2AC0")

    label("loc_1C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1D2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D00")

    ChrTalk(
        0x20,
        "Customers? This early?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I'm not trying to brag, but this is easily the\x01",
            "gloomiest store in all of Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "So, can't you let me enjoy my mornings a\x01",
            "bit before having to deal with customers?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D27")

    label("loc_1D00")


    ChrTalk(
        0x20,
        "...*sigh* Fine. Have it your way.\x02",
    )

    CloseMessageWindow()

    label("loc_1D27")

    Jump("loc_2AC0")

    label("loc_1D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1DAE")

    ChrTalk(
        0x20,
        "Huh...? Really? This late?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Fine, fine. Pick out what you want and\x01",
            "let me know. I was just about to close.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC0")

    label("loc_1DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1E3F")

    ChrTalk(
        0x20,
        (
            "Ugh, there's too many customers today...\x01",
            "I can't even read my magazines in peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "C'mon! Finish up shopping and go home!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AC0")

    label("loc_1E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F41")

    ChrTalk(
        0x20,
        (
            "Looks like those Revache guys who were\x01",
            "arrested have already been released.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I mean, damn. Why can't the CPD be a bit\x01",
            "more stubborn when it comes to them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Isn't this just setting a bad example for\x01",
            "the citizenry, too?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FDE")

    label("loc_1F41")


    ChrTalk(
        0x20,
        (
            "Well, whatever. It's got nothing to do with\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "With stuff like this always happening, it's\x01",
            "no wonder the public doesn't have faith\x01",
            "in the police.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FDE")

    Jump("loc_2AC0")

    label("loc_1FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_220F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2168")

    ChrTalk(
        0x20,
        "You know Speaker Hartmann?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "He's the leader of the Imperial Faction\x01",
            "and the most influential politician in all\x01",
            "of Crossbellan politics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Anyway, rumor has it that he's going to\x01",
            "run for mayor in the next election cycle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "And 'cause of that, he's been tryin' to make\x01",
            "connections in every circle you can think of.\x01",
            "I couldn't care less, personally.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_220A")

    label("loc_2168")


    ChrTalk(
        0x20,
        (
            "Rumor has it that Hartmann is looking to throw\x01",
            "his name in the ring for mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "If a man like him ends up winning, who\x01",
            "knows what'd happen to Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220A")

    Jump("loc_2AC0")

    label("loc_220F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_25E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C5")

    ChrTalk(
        0x20,
        (
            "Another customer? Damn, right when I\x01",
            "thought things were starting to slow down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FAre you okay, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Am I okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I'd say not. I've been working like hell all day.\x01",
            "Is it too much to ask for a short break? I have\x01",
            "magazines I'm wanting to read, y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Honestly, it'd be a lot better if I didn't have any\x01",
            "customers show up. That goes double for you\x01",
            "guys. Get what you want and scram.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 1)
    Jump("loc_25E2")

    label("loc_23C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2534")

    ChrTalk(
        0x20,
        (
            "There aren't too many weapons shops operating\x01",
            "in Crossbell, surprisingly enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Most of my regulars consist of CPD officers\x01",
            "and bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well... Technically, that's only scratching the\x01",
            "surface of the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I hear that there's a famous black-market shop\x01",
            "in the Downtown District. I wouldn't get involved\x01",
            "with it, if I were you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25E2")

    label("loc_2534")


    ChrTalk(
        0x20,
        (
            "I hear that there's a famous black-market shop\x01",
            "in the Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Of course, they aren't the type to deal in your\x01",
            "average weapons. Stay clear of them, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E2")

    Jump("loc_2AC0")

    label("loc_25E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_28F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2825")
    SetScenarioFlags(0x4C, 4)

    ChrTalk(
        0x20,
        (
            "Hey, miss. That guy stopped by the shop\x01",
            "again, if you were wondering.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#0205FThat guy? You mean Chief Roberts?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Yeah, that's him. He left another orbal\x01",
            "staff with me like he did last time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "If you want it, fork over the cash.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FVery well, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FTio's boss sure likes to work in roundabout\x01",
            "ways, doesn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FIsn't that the truth? I don't understand why\x01",
            "he doesn't just give it to you directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0201F(Chief... Pushing matters like this will\x01",
            "only serve to annoy me further.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F0")

    label("loc_2825")


    ChrTalk(
        0x20,
        (
            "Oh, yeah. Dudley came by the shop this\x01",
            "morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Sounds like he has a lot on his plate nowadays.\x01",
            "Geez. He's always been too serious and a rigid\x01",
            "fool, but I'm worried he's overworking himself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F0")

    Jump("loc_2AC0")

    label("loc_28F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_29B0")

    ChrTalk(
        0x20,
        (
            "State law now requires people to possess\x01",
            "a license to purchase and carry weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "But considering how many fakes are out in the\x01",
            "wild, it's not like it's enforced.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC0")

    label("loc_29B0")


    ChrTalk(
        0x20,
        (
            "Don't worry, though. I don't intend to sell these\x01",
            "orbal staves to anyone but you, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Y'know, isn't selling them to me, only to sell to\x01",
            "you, sort of strange? I mean, I feel like there're\x01",
            "better ways to go about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F(Chief, what are you up to...?)\x02",
    )

    CloseMessageWindow()

    label("loc_2AC0")

    Jump("loc_B21")

    label("loc_2AC5")

    TalkEnd(0x20)
    Return()

    # Function_5_8ED end

    def Function_6_2AC9(): pass

    label("Function_6_2AC9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315B")
    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)
    TurnDirection(0x21, 0x0, 0)
    TurnDirection(0x22, 0x0, 0)

    ChrTalk(
        0x101,
        (
            "#0000FInspector Donovan and Detective Raymond...?\x02\x03",
            "Are you in the middle of an investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "We are, indeed. Happen to be collecting evidence\x01",
            "for that warehouse district shooting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I'd bet anything that the culprit is related\x01",
            "to Revache somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Those guys have been causing nothing but\x01",
            "trouble recently, like that thing with the truck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FTruck?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FMind fillin' us in?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0201FPlease do. My interest is piqued.\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "Raymond, what have I said about reining\x01",
            "in that loose tongue of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Aw, crap. I did it again, didn't I?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "Well, I suppose we have no choice but to\x01",
            "tell them now. It all started with a rumor\x01",
            "that was sent to the Second Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Last weekend, there was an incident that\x01",
            "happened in Calvard involving a truck...\x01",
            "One of Revache's trucks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Supposedly, it was attacked by an unknown\x01",
            "party and went up in flames.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FSomeone blew it up?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "It seems so. And while those on top may try\x01",
            "to cover it up, stories like this are becoming\x01",
            "more and more common.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Fortunately, citizens have yet to be involved,\x01",
            "but word is that the Bracer Guild has been\x01",
            "investigating the incident as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FThat certainly sounds suspicious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FDo you think the attackers might have been\x01",
            "Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FI bet it was. Who else would have the balls\x01",
            "to do something like that to Revache?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FIt's not our business, but it would do us good\x01",
            "to keep a close eye on how this unfolds.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x21, 0xFF)
    OP_4C(0x22, 0xFF)
    OP_93(0x21, 0x10E, 0x0)
    OP_93(0x22, 0x5A, 0x0)
    SetScenarioFlags(0x94, 7)
    Jump("loc_32C1")

    label("loc_315B")

    TurnDirection(0x21, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "It looks like the First Division's in charge of\x01",
            "investigating that series of truck accidents.\x01",
            "We hardly know any details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, there's been a lot of incidents like that\x01",
            "happening lately. No reason why we need\x01",
            "to hear about every little thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Listen, you four. Make sure to pay attention\x01",
            "to things as you patrol the city, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x10E, 0x0)

    label("loc_32C1")

    TalkEnd(0xFE)
    Return()

    # Function_6_2AC9 end

    def Function_7_32C5(): pass

    label("Function_7_32C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32DA")
    Call(0, 6)
    Jump("loc_3418")

    label("loc_32DA")

    OP_4B(0x21, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Donovaaan, let's go home already. I'm not\x01",
            "sure I can handle another all-nighter... Not\x01",
            "after last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Enough griping, Raymond. We still have to\x01",
            "check out that other lead! Let's move out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Seriously? You're a monster, Donovan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(I think it'd be best to leave them to their\x01",
            "business.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x21, 0xFF)

    label("loc_3418")

    TalkEnd(0xFE)
    Return()

    # Function_7_32C5 end

    def Function_8_341C(): pass

    label("Function_8_341C")

    Call(0, 9)
    Return()

    # Function_8_341C end

    def Function_9_3420(): pass

    label("Function_9_3420")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_342D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E7")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_347E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_347E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_349E")
    OP_AF(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_42E2")

    label("loc_349E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34B2")
    Jump("loc_42E2")

    label("loc_34B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_352E")

    ChrTalk(
        0x8,
        (
            "I should've known it was too early to let\x01",
            "Selteo handle the kitchen on his own.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_352E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_363C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F0")

    ChrTalk(
        0x8,
        (
            "We've gotten a lot of complaints about\x01",
            "Selteo sending out really strange dishes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ahem. I apologize on the behalf of our\x01",
            "chef. He's prone to cause trouble.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3637")

    label("loc_35F0")


    ChrTalk(
        0x8,
        (
            "Now, if only Selteo would take his job a\x01",
            "little more seriously...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3637")

    Jump("loc_42E2")

    label("loc_363C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3728")

    ChrTalk(
        0x8,
        (
            "Selteo likes to leave the kitchen occasionally\x01",
            "during his shifts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Most of the time, it's to present the dishes he\x01",
            "makes directly to the customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Does he not understand that we\x01",
            "have a waitress for that...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_3728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3883")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384F")

    ChrTalk(
        0x8,
        (
            "Our chef, Braun, and I have been close friends\x01",
            "for about forty years now. Even did our training\x01",
            "together, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "We're worried about the next generation, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Selteo has potential, but he doesn't make the\x01",
            "effort to practice seriously and cultivate it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_387E")

    label("loc_384F")


    ChrTalk(
        0x8,
        "Is there ANY way to motivate that boy...?\x02",
    )

    CloseMessageWindow()

    label("loc_387E")

    Jump("loc_42E2")

    label("loc_3883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3911")

    ChrTalk(
        0x8,
        (
            "This year's festival brought in the highest\x01",
            "profits we've seen in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Unfortunately, all good things must end...\x02",
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_3911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ABC")

    ChrTalk(
        0x8,
        (
            "Nonno's words must have actually gotten\x01",
            "to Selteo. He's full of energy today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Just what in the world did she tell him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Was it something along the lines of 'There's\x01",
            "going to be a bunch of girls stopping by the\x01",
            "restaurant during the Anniversary Festival'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Either way, it might have been a little TOO\x01",
            "effective. I'm happy that he's working hard,\x01",
            "but just look at him. He's crazed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B68")

    label("loc_3ABC")


    ChrTalk(
        0x8,
        (
            "Nonno's words must have actually gotten\x01",
            "to Selteo. He's full of energy today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since he's usually so lackadaisical about\x01",
            "everything, I'm a little uncomfortable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B68")

    Jump("loc_42E2")

    label("loc_3B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3C51")

    ChrTalk(
        0x8,
        (
            "From the looks of it, people eager to take part\x01",
            "in the Anniversary Festival have been arriving\x01",
            "here ahead of schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure they probably just want to take in the\x01",
            "sights before the festivities start.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_3C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3CED")

    ChrTalk(
        0x8,
        "I'm very sorry about the noise, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Things would be so much easier around here\x01",
            "if Selteo took work a little more seriously...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_3CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3DED")

    ChrTalk(
        0x8,
        (
            "Our second floor is popular among patrons\x01",
            "looking to make reservations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We have the pleasure of serving important\x01",
            "public figures here, like Arios MacLaine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He visits us once a month to enjoy a meal\x01",
            "with his daughter, actually.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_3DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3F15")

    ChrTalk(
        0x8,
        (
            "With the festival fast approaching, we've begun\x01",
            "to receive reservation after reservation. Frankly,\x01",
            "they're making it somewhat tough to coordinate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Stocking up on the proper ingredients, designing\x01",
            "the restaurant decorations... We've certainly got\x01",
            "quite a lot on our plate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_3F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3FFD")

    ChrTalk(
        0x8,
        (
            "Selteo's always claiming that he's 'busy,' but that\x01",
            "doesn't stop him from coming out of the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He continues to insist bringing out dishes\x01",
            "to our female patrons. Honestly, what am\x01",
            "I to do with that boy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_3FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_40C3")

    ChrTalk(
        0x8,
        (
            "We ran into a little trouble with our\x01",
            "inventory, but worry not, I adjusted\x01",
            "everything with the chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can 100 percent guarantee that you\x01",
            "will be met with our usual flavors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_40C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4156")

    ChrTalk(
        0x8,
        (
            "We have a pair of newlyweds here\x01",
            "eating right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. Perhaps I'll send them a nice\x01",
            "bottle of wine later. On the house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_4156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4228")

    ChrTalk(
        0x8,
        (
            "Our patron on the second floor made a\x01",
            "reservation for his business meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The second floor is for reservations only,\x01",
            "actually. We welcome you to make one\x01",
            "yourself whenever you'd like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E2")

    label("loc_4228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_42E2")

    ChrTalk(
        0x8,
        "Good day, everyone. Welcome to Vingt-Sept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Is this for dine-in or carry out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you wish to do both, that can be arranged.\x01",
            "Simply say so when placing your order.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E2")

    Jump("loc_342D")

    label("loc_42E7")

    TalkEnd(0x8)
    Return()

    # Function_9_3420 end

    def Function_10_42EB(): pass

    label("Function_10_42EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_43FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4360")

    ChrTalk(
        0xFE,
        "Oh, dinnertime rush already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tonight's going to be busy. I can already tell.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_43F6")

    label("loc_4360")


    ChrTalk(
        0xFE,
        (
            "I guess I'll have Selteo concentrate on\x01",
            "coming up with the new menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cooking all these orders by myself is going\x01",
            "to be pretty hard, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F6")

    Jump("loc_56D8")

    label("loc_43FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_452A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44CA")

    ChrTalk(
        0xFE,
        (
            "We're starting to receive complaints from\x01",
            "customers who keep getting bizarre dishes\x01",
            "that they definitely didn't order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Must be more of Selteo's prototype\x01",
            "entrees.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4525")

    label("loc_44CA")


    ChrTalk(
        0xFE,
        "I try not to keep him on a short leash, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...how else is he going to learn?\x02",
    )

    CloseMessageWindow()

    label("loc_4525")

    Jump("loc_56D8")

    label("loc_452A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_46E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4643")

    ChrTalk(
        0xFE,
        (
            "People keep saying that there was a big\x01",
            "accident in the Harbor District this morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, well, we should be far enough away\x01",
            "that it doesn't affect customer traffic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sudden spike in accidents is problematic\x01",
            "for us, to say the least.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_46E0")

    label("loc_4643")


    ChrTalk(
        0xFE,
        (
            "At this rate, people aren't going to\x01",
            "want to go out for a meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If these accidents don't stop, we're going to\x01",
            "have quite the dilemma on our hands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E0")

    Jump("loc_56D8")

    label("loc_46E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4884")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E4")

    ChrTalk(
        0xFE,
        (
            "I recently gave Selteo an assignment to\x01",
            "work on during his shift, but guess what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The buffoon has done nothing but chase\x01",
            "girls since he clocked in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has to start training if he ever wants\x01",
            "to become a chef here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_487F")

    label("loc_47E4")


    ChrTalk(
        0xFE,
        (
            "I'm hoping that he'll do an adequate job\x01",
            "in coming up with the new menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, I can't retire in peace until he\x01",
            "finally decides to grow up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_487F")

    Jump("loc_56D8")

    label("loc_4884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4AA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49CC")

    ChrTalk(
        0xFE,
        (
            "On the last day of the Anniversary Festival,\x01",
            "Hoisdorf, the manager, gave us a hand in the\x01",
            "kitchen for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He may run the place, but don't let that fool\x01",
            "you. He's just as good in the kitchen as me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, it'd be nice if Hoisdorf helped out\x01",
            "in the kitchen on a more regular basis.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A9D")

    label("loc_49CC")


    ChrTalk(
        0xFE,
        (
            "He's an efficient chef, and I can hardly ever\x01",
            "think of any complaints about the taste. He\x01",
            "might be better than me, to be honest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if we'll ever get the chance to work\x01",
            "side by side again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9D")

    Jump("loc_56D8")

    label("loc_4AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4CB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C1B")

    ChrTalk(
        0xFE,
        (
            "It's looking like we're also throwing a small\x01",
            "event for the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Little while ago, Selteo told us he came up\x01",
            "with a brilliant idea, and he's thinking about\x01",
            "a plan on how to execute whatever it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Funnily enough, he said that a conversation\x01",
            "with Nonno was his biggest inspiration. That\x01",
            "girl gets him, for some reason.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4CB1")

    label("loc_4C1B")


    ChrTalk(
        0xFE,
        (
            "It's looking like we're also throwing a small\x01",
            "event for the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Selteo's brainstorming a plan for it right now,\x01",
            "actually.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB1")

    Jump("loc_56D8")

    label("loc_4CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4E3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DA9")

    ChrTalk(
        0xFE,
        (
            "I've been up to my neck organizing our festival\x01",
            "schedule with Hoisdorf the past few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, we have to come up with a\x01",
            "separate menu for reserved seating and\x01",
            "figure out the schedule for each day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4E38")

    label("loc_4DA9")


    ChrTalk(
        0xFE,
        (
            "By the way, Hoisdorf's mostly been the one\x01",
            "trying to figure out the reservations menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That man really has his work cut out for him.\x02",
    )

    CloseMessageWindow()

    label("loc_4E38")

    Jump("loc_56D8")

    label("loc_4E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4ED2")

    ChrTalk(
        0xFE,
        (
            "Nonno would definitely be the one\x01",
            "calling the shots in a relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pity the poor sap that gets married\x01",
            "to her someday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D8")

    label("loc_4ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4F61")

    ChrTalk(
        0xFE,
        (
            "You know how the saying goes. If you\x01",
            "don't work, you don't eat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish Selteo would stop goofing around\x01",
            "while working.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D8")

    label("loc_4F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4FD9")

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival is just\x01",
            "one month away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's bound to bring in heavy traffic\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D8")

    label("loc_4FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_51EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5172")

    ChrTalk(
        0xFE,
        (
            "Ever since we were both apprentices, Hoisdorf's\x01",
            "always wanted to run his own restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I remember him telling me how he wanted to\x01",
            "create a place where people can savor fine\x01",
            "cuisine with a lively, family friendly atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who would've thought that a master chef like\x01",
            "him would come up with a crazy dream like that?\x01",
            "Haha, and I'm the fool who went along with him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_51E7")

    label("loc_5172")


    ChrTalk(
        0xFE,
        (
            "Who would've thought that he'd come up\x01",
            "with a crazy idea like this? And who knew\x01",
            "I'd be dragged along with him?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51E7")

    Jump("loc_56D8")

    label("loc_51EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5373")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5300")

    ChrTalk(
        0xFE,
        (
            "It looks like the railway deliveries are\x01",
            "running late today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're going to make it through the day!\x01",
            "Hoisdorf already thought up an alternate\x01",
            "menu and everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I intend to throw in a bit of my own\x01",
            "personal flavor in there, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_536E")

    label("loc_5300")


    ChrTalk(
        0xFE,
        (
            "Hoisdorf managed to think up another\x01",
            "menu right on the spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's quick on his toes, that Hoisdorf.\x02",
    )

    CloseMessageWindow()

    label("loc_536E")

    Jump("loc_56D8")

    label("loc_5373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_54C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_545C")

    ChrTalk(
        0xFE,
        "All right, we've got an order for two here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh? If you need to place an order, you\x01",
            "can ask one of the waiters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though, if I'm honest, I'd still probably\x01",
            "make you something if you asked me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_54C1")

    label("loc_545C")


    ChrTalk(
        0xFE,
        (
            "Go on, try me. Whisper in my ear the\x01",
            "right dish...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...and I'll consider making it! Hahaha!\x02",
    )

    CloseMessageWindow()

    label("loc_54C1")

    Jump("loc_56D8")

    label("loc_54C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_55AD")

    ChrTalk(
        0xFE,
        (
            "Cooking is a process that requires vigor,\x01",
            "sincerity, and enjoyment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how busy you get, nothing\x01",
            "matters if you lose your cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's about time I teach Selteo what it\x01",
            "means to think like a chef.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D8")

    label("loc_55AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_56D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5684")

    ChrTalk(
        0xFE,
        (
            "And that should be a wrap on today's\x01",
            "prep...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, not bad. Thirty years here, and I\x01",
            "am still number one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have a good feeling about this flavor.\x01",
            "I'm going to roll with it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_56D8")

    label("loc_5684")


    ChrTalk(
        0xFE,
        (
            "I have to hurry and finish prepping the\x01",
            "ingredients before our lunchtime rush.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56D8")

    TalkEnd(0xFE)
    Return()

    # Function_10_42EB end

    def Function_11_56DC(): pass

    label("Function_11_56DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56FD")
    Call(0, 38)
    Return()

    label("loc_56FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A2F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5727")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A2A")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",           # 0
            "Give Food\x01",      # 1
            "Leave\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 12)
    Jump("loc_5A25")

    label("loc_577B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A25")
    Call(0, 40)
    Call(0, 41)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5858")

    ChrTalk(
        0xFE,
        (
            "It looks like you don't have any peculiar\x01",
            "dishes on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you manage to find ten or more\x01",
            "different kinds of them, come see me.\x01",
            "The reward will be worth it, trust me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A16")

    label("loc_5858")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_591B")

    ChrTalk(
        0xFE,
        (
            "Sorry. I need more peculiar dishes than\x01",
            "this, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you manage to find ten or more\x01",
            "different kinds of them, come see me.\x01",
            "The reward will be worth it, trust me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A16")

    label("loc_591B")


    ChrTalk(
        0xFE,
        "Ready to show me what you've got?\x02",
    )

    CloseMessageWindow()

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "[Report]\x01",      # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5976")
    Call(0, 39)
    Return()

    label("loc_5976")


    ChrTalk(
        0xFE,
        (
            "Hmm, all right. Remember, the sky's the limit\x01",
            "when it comes to how many you bring me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keep finding new peculiar dishes and then\x01",
            "lemme check them out!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A16")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A25")

    label("loc_5A25")

    Jump("loc_5727")

    label("loc_5A2A")

    Jump("loc_5A32")

    label("loc_5A2F")

    Call(0, 12)

    label("loc_5A32")

    TalkEnd(0xFE)
    Return()

    # Function_11_56DC end

    def Function_12_5A36(): pass

    label("Function_12_5A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B1B")

    ChrTalk(
        0xA,
        (
            "The new menu is finally starting to take\x01",
            "shape. Thank Aidios!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "And this time, I'm pretty confident in it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Today's another great day to search for\x01",
            "a beauty who'll taste-test my cuisine! ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5BB3")

    label("loc_5B1B")


    ChrTalk(
        0xA,
        (
            "After hearing complaints about how my\x01",
            "dishes looked, I made sure to improve\x01",
            "their overall aesthetic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "After all, the customer is always right.\x02",
    )

    CloseMessageWindow()

    label("loc_5BB3")

    Jump("loc_6C90")

    label("loc_5BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5CFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C7F")

    ChrTalk(
        0xA,
        (
            "I've been going around serving prototype\x01",
            "dishes to random customers lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Sadly, no one touched them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't fathom why. Do they really look\x01",
            "that bad...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5CFA")

    label("loc_5C7F")


    ChrTalk(
        0xA,
        (
            "Time to make a new menu. Maybe it'd be\x01",
            "better to stick with the classics, but sprinkle\x01",
            "in a few original dishes, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CFA")

    Jump("loc_6C90")

    label("loc_5CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5ECE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DBF")

    ChrTalk(
        0xA,
        (
            "Hey, don't you think the girls sitting in\x01",
            "those center seats are pretty cute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I sure do. I think I'll give them some of\x01",
            "my prototype dishes. On the house!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5EC9")

    label("loc_5DBF")


    ChrTalk(
        0xA,
        (
            "'Behold, an original recipe made with you\x01",
            "specifically in mind!' With a line like that,\x01",
            "any one of them is as good as mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And besides, chatting with a pretty girl and\x01",
            "hearing some constructive criticism on my\x01",
            "recipes is killing two birds with one stone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC9")

    Jump("loc_6C90")

    label("loc_5ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6011")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FBE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F03")
    Jump("loc_5F0A")

    label("loc_5F03")

    OP_93(0xA, 0x10E, 0x0)

    label("loc_5F0A")


    ChrTalk(
        0xA,
        (
            "Hmm, let me think. Traditional entrees are\x01",
            "usually focused around meat or seafood...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But what if I scrap that entirely and use\x01",
            "some rare ingredients as the base?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_600C")

    label("loc_5FBE")


    ChrTalk(
        0xA,
        (
            "Leave me alone! I'm trying to come up\x01",
            "with what's going on the new menu!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_600C")

    Jump("loc_6C90")

    label("loc_6011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6120")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60DA")

    ChrTalk(
        0xA,
        (
            "Now that the Anniversary Festival's over\x01",
            "with, I'll finally have some wiggle room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You think I should take it easy today and\x01",
            "find me some cuties? 'Cause I sure do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_611B")

    label("loc_60DA")


    ChrTalk(
        0xA,
        (
            "Hehehe... Oh, I can't wait until today's\x01",
            "lunch rush starts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_611B")

    Jump("loc_6C90")

    label("loc_6120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_61D6")

    ChrTalk(
        0xA,
        (
            "Since it's festival time, I'm sure a ton\x01",
            "of enthusiastic girls are going to stop\x01",
            "by to feast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't worry, ladies! I'll match your\x01",
            "enthusiasm, and then some!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C90")

    label("loc_61D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_630B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62AA")

    ChrTalk(
        0xA,
        (
            "Whenever the Anniversary Festival rolls\x01",
            "around, we always have to make certain\x01",
            "adjustments to our schedule and menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Unfortunately, I can't find the motivation\x01",
            "to help out...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6306")

    label("loc_62AA")


    ChrTalk(
        0xA,
        (
            "*sigh* All I want is to go chill outside and\x01",
            "sneak peeks at all the girls. Life sucks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6306")

    Jump("loc_6C90")

    label("loc_630B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_63E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6326")
    Call(0, 14)
    Jump("loc_63E0")

    label("loc_6326")

    OP_93(0xA, 0xB4, 0x0)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        "A-All I did was bring that girl her food...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You think I'm some kind of idiot? You\x01",
            "were obviously trying to hit on her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Well, no more! Back to work, Selteo!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_63E0")

    Jump("loc_6C90")

    label("loc_63E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6520")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C2")

    ChrTalk(
        0xA,
        "One plate of spaghetti, coming right up! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This dish is for that cutie sitting at\x01",
            "the middle table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hehehe. If I take it to her, I'm sure we\x01",
            "could have a wonderful conversation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_651B")

    label("loc_64C2")


    ChrTalk(
        0xA,
        (
            "I like to spontaneously put all my energy\x01",
            "into orders...if it's for the right girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_651B")

    Jump("loc_6C90")

    label("loc_6520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_66A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6647")

    ChrTalk(
        0xA,
        (
            "Phew, finally. I thought that lunchtime\x01",
            "rush was never going to end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since the festival's almost here, business\x01",
            "has been getting way too hectic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Still, it doesn't seem to faze Braun.\x01",
            "He always has time to spare after orders.\x01",
            "How the heck does he do it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_66A4")

    label("loc_6647")


    ChrTalk(
        0xA,
        (
            "If I were as fast as him, I would have way\x01",
            "more time to chat with our lady customers...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66A4")

    Jump("loc_6C90")

    label("loc_66A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_680D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67C7")

    ChrTalk(
        0xA,
        (
            "This random girl is always drinking coffee\x01",
            "in the back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After taking a closer look, I noticed that she\x01",
            "was actually pretty cute. So, I took a quick\x01",
            "break and tried talking to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "She didn't say a word to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Man, talk about depressing...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6808")

    label("loc_67C7")


    ChrTalk(
        0xA,
        "Wait. Am I...ugly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Being ignored is REALLY depressing.\x02",
    )

    CloseMessageWindow()

    label("loc_6808")

    Jump("loc_6C90")

    label("loc_680D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6954")

    ChrTalk(
        0xA,
        "Crossbell is home to a bunch of beauties.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You got our big star, Ilya Platiere, and the\x01",
            "influential woman in finance, the lovely\x01",
            "Mariabell Crois, just to name a couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even your ordinary girl walking around town\x01",
            "cares about recent fashion trends. It's no\x01",
            "wonder why I'm so drawn to them. Hehehe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C90")

    label("loc_6954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_69E7")

    ChrTalk(
        0xA,
        (
            "Darn it. Barely any girls have stopped\x01",
            "by to eat today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Wait, there's still the lunchtime rush! The\x01",
            "battle isn't over yet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C90")

    label("loc_69E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6A9D")

    ChrTalk(
        0xA,
        (
            "Gah, I hate lunchtime! Is it even possible\x01",
            "to get busier than this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh* Only thing that could make this hell\x01",
            "better is if all the customers were girls...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C90")

    label("loc_6A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6C90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BCC")

    ChrTalk(
        0xA,
        (
            "Every day, we have loads of people stop by\x01",
            "the restaurant looking for a bite to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On top of that, a lot of them include some\x01",
            "pretty hot ladies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And yet here I am, slaving away in the\x01",
            "kitchen all day... It doesn't give me any\x01",
            "time to check out the customers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6C90")

    label("loc_6BCC")


    ChrTalk(
        0xA,
        (
            "I didn't come to Crossbell to be weighed\x01",
            "down by the burden of labor! I'm here to\x01",
            "meet girls. Lots of them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At this rate, I'll never finish today's work.\x01",
            "Gotta love this freakin' job...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C90")

    Return()

    # Function_12_5A36 end

    def Function_13_6C91(): pass

    label("Function_13_6C91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6DE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D57")
    TurnDirection(0xFE, 0xE, 0)

    ChrTalk(
        0xFE,
        (
            "Terribly sorry, but we accidentally made\x01",
            "a mistake when taking inventory...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you would like a cup of black tea, I'd\x01",
            "be more than happy to serve you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6DDB")

    label("loc_6D57")


    ChrTalk(
        0xFE,
        (
            "(So, Selteo really did use up the majority\x01",
            "of our coffee bean stock, did he?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(*sigh* That puts us in a bit of a bind...)\x02",
    )

    CloseMessageWindow()

    label("loc_6DDB")

    Jump("loc_7987")

    label("loc_6DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EB5")

    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Today's slightly less crowded than usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose that's better than being slammed\x01",
            "with customers. Though, small crowds aren't\x01",
            "great for our paychecks, either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6F1E")

    label("loc_6EB5")


    ChrTalk(
        0xFE,
        (
            "I wonder, should we focus our efforts\x01",
            "on bringing in new customers like we\x01",
            "did during the festival?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F1E")

    Jump("loc_7987")

    label("loc_6F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6F95")

    ChrTalk(
        0xFE,
        "So many police officers today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've been patrolling the city since\x01",
            "morning, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7987")

    label("loc_6F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_70FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_709D")

    ChrTalk(
        0xFE,
        "Is something bothering Selteo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like, he came to ask me my opinion about\x01",
            "entrees, and he never does that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'Can you think of any weird or exotic dishes\x01",
            "we could make?' He asked that and then ran\x01",
            "away. Should I be worried?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_70FA")

    label("loc_709D")


    ChrTalk(
        0xFE,
        (
            "Selteo sometimes blurts out the strangest things.\x01",
            "I never know what to expect from him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70FA")

    Jump("loc_7987")

    label("loc_70FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_71CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7171")

    ChrTalk(
        0xFE,
        "Welcome, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, what a cutie pie. Would you like a kids\x01",
            "menu for her?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_71CA")

    label("loc_7171")


    ChrTalk(
        0xFE,
        (
            "Around this time, we usually have plenty of\x01",
            "open seats. Certainly enough for three.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71CA")

    Jump("loc_7987")

    label("loc_71CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_71E0")
    Call(0, 34)
    Jump("loc_7987")

    label("loc_71E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7310")

    ChrTalk(
        0xFE,
        (
            "Our manager is busy preparing for the festival.\x01",
            "Lucky for him, all of us employees lend him a\x01",
            "hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every year, we throw together a drink service\x01",
            "and even come up with little souvenirs for\x01",
            "the customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And we turn the little flags we put in kids'\x01",
            "meals into festival ones.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7987")

    label("loc_7310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_73BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_732B")
    Call(0, 14)
    Jump("loc_73B5")

    label("loc_732B")


    ChrTalk(
        0xFE,
        (
            "I swear, Selteo will come up with any reason\x01",
            "to leave the kitchen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's rush hour! Can't he stay put and do his job\x01",
            "for once?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73B5")

    Jump("loc_7987")

    label("loc_73BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7441")

    ChrTalk(
        0xFE,
        (
            "Is it just me, or are today's customers super\x01",
            "nice for some reason?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It makes me want them to have a nice meal.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7987")

    label("loc_7441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7484")

    ChrTalk(
        0xFE,
        "Welcome to Vingt-Sept!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What can I get you?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7987")

    label("loc_7484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7555")

    ChrTalk(
        0xFE,
        (
            "Second floor seats are for reservations\x01",
            "only. With a reservation, you can even\x01",
            "order your entire meal in advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have quite a few regulars who bring\x01",
            "their families along for meals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7987")

    label("loc_7555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7704")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7662")

    ChrTalk(
        0xFE,
        (
            "The manager and Braun have been\x01",
            "friends forever. They're inseparable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They even work together to make decisions\x01",
            "about the restaurant's management.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Staying close friends after all these\x01",
            "years... I think that's pretty admirable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_76FF")

    label("loc_7662")


    ChrTalk(
        0xFE,
        (
            "The manager and Braun have been\x01",
            "friends forever. They're inseparable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They even work together to make decisions\x01",
            "about the restaurant's management.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76FF")

    Jump("loc_7987")

    label("loc_7704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7822")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77A8")

    ChrTalk(
        0xFE,
        "Welcome, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now, we're serving our breakfast\x01",
            "menu. If you haven't had anything yet,\x01",
            "hurry and place your order, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_781D")

    label("loc_77A8")


    ChrTalk(
        0xFE,
        (
            "Right now, we're serving our breakfast\x01",
            "menu. If you haven't had anything yet,\x01",
            "hurry and place your order, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_781D")

    Jump("loc_7987")

    label("loc_7822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7895")

    ChrTalk(
        0xFE,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew, lunch is always when we're our\x01",
            "busiest. But, c'mon, I can do this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7987")

    label("loc_7895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7987")

    ChrTalk(
        0xFE,
        (
            "Pardon me! Coming through!\x01",
            "Two lunch specials, hot and ready!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You all should find yourselves a table!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can get pretty hectic during the lunch rush.\x01",
            "If you sit and wait patiently, I promise we'll be\x01",
            "with you shortly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7987")

    TalkEnd(0xFE)
    Return()

    # Function_13_6C91 end

    def Function_14_798B(): pass

    label("Function_14_798B")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        (
            "Selteooooo...? You asking for a noogie or\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I-I didn't do anything wrong! I'm innocent!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Innocent?! It looks to me like you're\x01",
            "neglecting work. Back to the kitchen!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_14_798B end

    def Function_15_7A69(): pass

    label("Function_15_7A69")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7AFD")
    Jump("loc_7B47")

    label("loc_7AFD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B1D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B47")

    label("loc_7B1D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B3D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B47")

    label("loc_7B3D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B47")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D33")

    ChrTalk(
        0xFE,
        "#2600FHello, Elie. Everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FGetting an early lunch, Ernest?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2606FOh, no. I'm just on break.\x02\x03",
            "#2600FI'll be attending a public hearing with\x01",
            "the mayor this evening.\x02\x03",
            "I'm just double-checking the data that will\x01",
            "be presented now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FInteresting. I know I've said this a thousand\x01",
            "times, but thank you for helping Grandfather.\x01",
            "It really means a lot to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(He looks really busy. Even busier than us.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7E3F")

    label("loc_7D33")

    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "#2601FAccording to our data, we can't exactly deny\x01",
            "the Imperial Faction's request...\x02\x03",
            "#2603FThen again, if we present this, the Republican\x01",
            "Faction will go into an uproar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(It'd be rude to bother him while he's working.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0104F(Shall we go?)\x02",
    )

    CloseMessageWindow()

    label("loc_7E3F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_7A69 end

    def Function_16_7E47(): pass

    label("Function_16_7E47")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7EDB")
    Jump("loc_7F25")

    label("loc_7EDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7EFB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F25")

    label("loc_7EFB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F1B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F25")

    label("loc_7F1B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F25")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7FF9")

    ChrTalk(
        0xFE,
        "Apparently, they've run out of coffee.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unbelievable! How is it possible for a\x01",
            "restaurant to run out of coffee? What\x01",
            "would be the point of coming here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94CB")

    label("loc_7FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8075")

    ChrTalk(
        0xFE,
        "The city's quiet today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And is it just me, or have there been\x01",
            "fewer police officers roaming around?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94CB")

    label("loc_8075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_816E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8117")

    ChrTalk(
        0xFE,
        "*sip* ...O-Oh, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't find my issue of the Crossbell Times.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must have left it at home before heading out.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8169")

    label("loc_8117")


    ChrTalk(
        0xFE,
        (
            "My blood pressure spikes whenever I think\x01",
            "about how the diet meeting went...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8169")

    Jump("loc_94CB")

    label("loc_816E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_82E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82A3")

    ChrTalk(
        0xFE,
        "*sip* Ah, how lovely...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today's Crossbell Times' front page article\x01",
            "focused on the diet's budget proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For grown men's faces to turn red when\x01",
            "asked about it, it must not be going well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, this is what always happens. I, for\x01",
            "one, think it's quite amusing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_82DD")

    label("loc_82A3")


    ChrTalk(
        0xFE,
        (
            "Diet members insulting one another?\x01",
            "I live for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82DD")

    Jump("loc_94CB")

    label("loc_82E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8440")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83DF")

    ChrTalk(
        0xFE,
        "*sip* Ah, how marvelous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm thankful that the festive mood has\x01",
            "finally started to dissipate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Though, it seems that Arios is out on\x01",
            "another business trip again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I swear, that man is hardly in Crossbell!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_843B")

    label("loc_83DF")


    ChrTalk(
        0xFE,
        (
            "Even though he's a Crossbellan through\x01",
            "and through, Arios is hardly ever in the\x01",
            "state.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_843B")

    Jump("loc_94CB")

    label("loc_8440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_85D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_850C")

    ChrTalk(
        0xFE,
        "*sip*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that the CGF commander is constantly\x01",
            "throwing and attending extravagant parties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, he never does his work and\x01",
            "simply meanders about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_85CC")

    label("loc_850C")


    ChrTalk(
        0xFE,
        (
            "Rumor has it that the CGF commander loves\x01",
            "fancy receptions and parties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but wonder if the Crossbell Times\x01",
            "is planning to run an expose to highlight all of\x01",
            "his misdeeds.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85CC")

    Jump("loc_94CB")

    label("loc_85D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_87B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86D6")

    ChrTalk(
        0xFE,
        "*sip* You know about Mr. Crois, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, he's the CEO of the International Bank\x01",
            "of Crossbell and is famous for his philanthropic\x01",
            "efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's amazing that he finds time to help those\x01",
            "in need while staying so busy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_87B4")

    label("loc_86D6")


    ChrTalk(
        0xFE,
        (
            "Speaking of the IBC, did you know that it's\x01",
            "the largest banking group in the world?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's amazing that he finds time to help those\x01",
            "in need while staying so busy... Mr. Crois is\x01",
            "something special, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B4")

    Jump("loc_94CB")

    label("loc_87B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_8879")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8853")

    ChrTalk(
        0xFE,
        "*sip* ...Oh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm out of coffee already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, perhaps I'm nearing my limit for sitting\x01",
            "and buying just one cup.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8874")

    label("loc_8853")


    ChrTalk(
        0xFE,
        "Time to go home, I suppose.\x02",
    )

    CloseMessageWindow()

    label("loc_8874")

    Jump("loc_94CB")

    label("loc_8879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8960")

    ChrTalk(
        0xFE,
        "*sip* Hear the latest Arc en Ciel news?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Supposedly, they selected a rookie to play\x01",
            "as the new show's co-star.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What was her name again? I swear that I\x01",
            "saw it in a magazine, in bold print...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8A04")

    label("loc_8960")


    ChrTalk(
        0xFE,
        (
            "I've heard that this particular rookie hasn't\x01",
            "had any experience with stage plays yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How someone like that snagged the role\x01",
            "of co-star, I have no idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A04")

    Jump("loc_94CB")

    label("loc_8A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B41")

    ChrTalk(
        0xFE,
        "*sip* People've gone mad for Arc en Ciel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hear that people scrambled to try and snag\x01",
            "tickets for their new show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yet another example of the common folk not\x01",
            "knowing when to give up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's much smarter to save yourself the effort\x01",
            "when you know your odds are slim.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8B8C")

    label("loc_8B41")


    ChrTalk(
        0xFE,
        "*sip* *sip*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I assure you, I'm not jealous\x01",
            "or anything like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B8C")

    Jump("loc_94CB")

    label("loc_8B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8DDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D2E")

    ChrTalk(
        0xFE,
        "*sip* Mainz is quite the interesting town.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a mining village surrounded by loads\x01",
            "of mountains to the north.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's become relatively advanced in the past\x01",
            "few years, so it's certainly with the times\x01",
            "more than Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though, it's still a mere countryside village.\x01",
            "It's certainly not the type of place you'd go\x01",
            "to for sightseeing or things of that nature.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8DD8")

    label("loc_8D2E")


    ChrTalk(
        0xFE,
        (
            "Mainz is an old mining village surrounded\x01",
            "by the mountains to the north.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though, it's still a mere countryside village.\x01",
            "It's not exactly a tourist destination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD8")

    Jump("loc_94CB")

    label("loc_8DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8FEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F50")

    ChrTalk(
        0xFE,
        "*sip* Have you heard about Armorica Village?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say a fair amount of traders make\x01",
            "their way there to conduct business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, their vegetables ARE quite tasty, and\x01",
            "with all the produce they have, they could\x01",
            "probably even open their own market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Willingly going out into the wild countryside\x01",
            "to make a deal? Oh, what genius!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8FEA")

    label("loc_8F50")


    ChrTalk(
        0xFE,
        (
            "Granted, there are many other ways to run\x01",
            "a successful business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Willingly going out into the wild countryside\x01",
            "to make a deal? Oh, what genius!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FEA")

    Jump("loc_94CB")

    label("loc_8FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_917F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90EF")

    ChrTalk(
        0xFE,
        "*sip* Finally, some peace and quiet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that the police intervened with that\x01",
            "mess those rabble caused downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, no one was arrested. Always\x01",
            "tripping up in the execution; that's our\x01",
            "police for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_917A")

    label("loc_90EF")


    ChrTalk(
        0xFE,
        (
            "Unfortunately for us fine folk, the police refuse\x01",
            "to have a backbone. Doesn't the law say that\x01",
            "criminals are supposed to be punished?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_917A")

    Jump("loc_94CB")

    label("loc_917F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_937E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_929D")

    ChrTalk(
        0xFE,
        "*sip* Another article about the guild?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, the Crossbell Times sure loves featuring\x01",
            "bracers on the front cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know they're a popular subject, but couldn't\x01",
            "they focus a bit more on criticizing our diet?\x01",
            "Seems a bit more relevant in my eyes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9379")

    label("loc_929D")


    ChrTalk(
        0xFE,
        (
            "I think that the Crossbell Times should focus\x01",
            "less on bracers and more on the issues that\x01",
            "directly affect us. AKA, the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what do I know about journalism? It's\x01",
            "just more interesting to me, personally.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9379")

    Jump("loc_94CB")

    label("loc_937E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_94CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9450")

    ChrTalk(
        0xFE,
        "*sip* I do enjoy my time at this restaurant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The hustle and bustle keeps things fresh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Besides, reading here with a cup of coffee\x01",
            "in hand relaxes me like nothing else.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_94CB")

    label("loc_9450")


    ChrTalk(
        0xFE,
        (
            "I do love how crazy it can get in here.\x01",
            "That, combined with reading and sipping\x01",
            "on a bit of coffee, is very relaxing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94CB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_7E47 end

    def Function_17_94D3(): pass

    label("Function_17_94D3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9567")
    Jump("loc_95B1")

    label("loc_9567")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9587")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95B1")

    label("loc_9587")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95A7")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95B1")

    label("loc_95A7")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_95B1")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x11, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9730")

    ChrTalk(
        0x11,
        (
            "Oh, my! What a superb design! I suppose\x01",
            "I shouldn't have expected anything less\x01",
            "from you, Kendall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "You flatter me, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "So...what exactly was that other job you\x01",
            "wanted to ask me about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, of course. There is a project in the works\x01",
            "involving the construction of a new hotel in the\x01",
            "Imperial capital.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9853")

    label("loc_9730")


    ChrTalk(
        0x11,
        (
            "We would like to bring you on board to\x01",
            "undertake this challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Oh, say no more. Your face says everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Man's journey calls him to constantly seek out\x01",
            "new and exciting things. And it's our duty to\x01",
            "respond to that task. I accept your offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Haha. I'm glad you agree.\x02",
    )

    CloseMessageWindow()

    label("loc_9853")

    SetChrSubChip(0xF, 0x0)
    TalkEnd(0xF)
    Return()

    # Function_17_94D3 end

    def Function_18_985B(): pass

    label("Function_18_985B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_98ED")

    ChrTalk(
        0xFE,
        (
            "Well, since I'm here, I might as well give\x01",
            "the menu a taste test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One can never be too sure with new\x01",
            "places, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A4B")

    label("loc_98ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9A4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99B3")

    ChrTalk(
        0xFE,
        (
            "I'm meeting with an extremely important\x01",
            "client today. Failure is not an option!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, I must hurry, make reservations, and\x01",
            "get my act together before he arrives!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9A4B")

    label("loc_99B3")


    ChrTalk(
        0xFE,
        (
            "This restaurant is well known throughout\x01",
            "Crossbell for its magnificent cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm off to make my reservation and\x01",
            "entertain my client.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A4B")

    TalkEnd(0xFE)
    Return()

    # Function_18_985B end

    def Function_19_9A4F(): pass

    label("Function_19_9A4F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AE3")
    Jump("loc_9B2D")

    label("loc_9AE3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B03")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B2D")

    label("loc_9B03")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B23")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B2D")

    label("loc_9B23")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9B2D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9BFE")

    ChrTalk(
        0xFE,
        (
            "Phew, I'm stuffed. I can't come up with\x01",
            "a single complaint about that meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time I come to Crossbell, I'll have\x01",
            "to drag my friends along, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C5E")

    label("loc_9BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9C5E")

    ChrTalk(
        0xFE,
        "Mmm, this is delicious!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Food this good, at this low\x01",
            "a price? That's a steal!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C5E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_9A4F end

    def Function_20_9C66(): pass

    label("Function_20_9C66")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CFA")
    Jump("loc_9D44")

    label("loc_9CFA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9D1A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D44")

    label("loc_9D1A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D3A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D44")

    label("loc_9D3A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D44")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9E22")

    ChrTalk(
        0xFE,
        (
            "I always make sure to take my family\x01",
            "out to eat at least once a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's partly because I start to worry\x01",
            "about my mother when I haven't seen\x01",
            "her in a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EB6")

    label("loc_9E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9EB6")

    ChrTalk(
        0xFE,
        (
            "I had a feeling this place would offer\x01",
            "some homestyle cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Delicious food at affordable prices.\x01",
            "Just like the good old days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EB6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_9C66 end

    def Function_21_9EBE(): pass

    label("Function_21_9EBE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F52")
    Jump("loc_9F9C")

    label("loc_9F52")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9F72")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F9C")

    label("loc_9F72")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F92")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F9C")

    label("loc_9F92")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F9C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A076")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "I don't like the fact that my mother-in-law\x01",
            "is living by herself. Isn't that dangerous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just, please be careful. If anything\x01",
            "happens, I'll come running.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A117")

    label("loc_A076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A117")

    ChrTalk(
        0xFE,
        (
            "My mother-in-law is running late. And we\x01",
            "planned to eat together a while ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering her age, I can't help but feel\x01",
            "worried about her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A117")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_9EBE end

    def Function_22_A11F(): pass

    label("Function_22_A11F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A1B3")
    Jump("loc_A1FD")

    label("loc_A1B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A1D3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1FD")

    label("loc_A1D3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1F3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1FD")

    label("loc_A1F3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1FD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "Apologies, dearie. I swear I left on time,\x01",
            "but I must have taken my sweet time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hand me the menu, will you? I'll order\x01",
            "something for you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_A11F end

    def Function_23_A2C2(): pass

    label("Function_23_A2C2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A356")
    Jump("loc_A3A0")

    label("loc_A356")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A376")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3A0")

    label("loc_A376")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A396")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3A0")

    label("loc_A396")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3A0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A456")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3E0")
    Call(0, 25)
    Jump("loc_A451")

    label("loc_A3E0")


    ChrTalk(
        0xFE,
        "He's got quite the stomach!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well. Once we're back in Erebonia, he\x01",
            "is going to be training nonstop!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A451")

    Jump("loc_A587")

    label("loc_A456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A4D3")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "No, the Entertainment District is out of the\x01",
            "question!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If trouble cropped up, we'd be suspended!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A587")

    label("loc_A4D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A587")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4EE")
    Call(0, 25)
    Jump("loc_A587")

    label("loc_A4EE")


    ChrTalk(
        0xFE,
        (
            "We're prestigious members of the famous\x01",
            "Imperial riding club, Nines!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you don't mind, we're busy building up\x01",
            "energy for the next tournament.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A587")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_A2C2 end

    def Function_24_A58F(): pass

    label("Function_24_A58F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A623")
    Jump("loc_A66D")

    label("loc_A623")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A643")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A66D")

    label("loc_A643")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A663")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A66D")

    label("loc_A663")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A66D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6AD")
    Call(0, 25)
    Jump("loc_A711")

    label("loc_A6AD")

    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "*munch* *munch* *chomp* *crunch*\x01",
            "*chomp* *munch* *crunch* *munch*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Another plate, sir!\x02",
    )

    CloseMessageWindow()

    label("loc_A711")

    Jump("loc_A83B")

    label("loc_A716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A7B4")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "The scenery here isn't too bad, but I can't say\x01",
            "I'm very interested in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I much prefer places that let me have fun!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A83B")

    label("loc_A7B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A83B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7CF")
    Call(0, 25)
    Jump("loc_A83B")

    label("loc_A7CF")

    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "*munch* *munch* *chomp* *crunch*\x01",
            "*chomp* *munch* *crunch* *munch*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "One more plate for me, sir!\x02",
    )

    CloseMessageWindow()

    label("loc_A83B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_A58F end

    def Function_25_A843(): pass

    label("Function_25_A843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A90E")
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    ChrTalk(
        0x16,
        (
            "We came to sightsee, but all we've done\x01",
            "is eat at this restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "That's okay. For now, eat up! You can't\x01",
            "train on an empty stomach, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "I hear you, coach!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A9A7")

    label("loc_A90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A91C")
    Jump("loc_A9A7")

    label("loc_A91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A9A7")
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    ChrTalk(
        0x16,
        "Eat up! Go, go, gooo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "After you finish, we'll hit every tourist\x01",
            "spot before evening comes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Okay, coach!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_A9A7")

    Return()

    # Function_25_A843 end

    def Function_26_A9A8(): pass

    label("Function_26_A9A8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AA3C")
    Jump("loc_AA86")

    label("loc_AA3C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA5C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AA86")

    label("loc_AA5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA7C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AA86")

    label("loc_AA7C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA86")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_AB46")

    ChrTalk(
        0xFE,
        (
            "G-Great going, me. Who expected something\x01",
            "like this to happen during our honeymoon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'll just have to redeem myself\x01",
            "somehow!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD08")

    label("loc_AB46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_AC78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC12")

    ChrTalk(
        0xFE,
        (
            "Let's see... Next up is the casino, and then\x01",
            "we're spending the night at that fancy hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm. Where was the hotel located again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It should be nearby, right...?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_AC73")

    label("loc_AC12")


    ChrTalk(
        0xFE,
        (
            "O-Oh, crap... I think I forgot where\x01",
            "the hotel is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "C'mon, c'mon! I have to remember...\x02",
    )

    CloseMessageWindow()

    label("loc_AC73")

    Jump("loc_AD08")

    label("loc_AC78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_AD08")

    ChrTalk(
        0xFE,
        "My wife and I are here on our honeymoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell City is gorgeous, isn't it? You never\x01",
            "know what will catch your eye here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD08")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_A9A8 end

    def Function_27_AD10(): pass

    label("Function_27_AD10")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ADA4")
    Jump("loc_ADEE")

    label("loc_ADA4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ADC4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADEE")

    label("loc_ADC4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADE4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADEE")

    label("loc_ADE4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ADEE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_AF88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF08")

    ChrTalk(
        0xFE,
        (
            "I got turned around in the Entertainment\x01",
            "District last night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...when all of a sudden, this dreamy young\x01",
            "man appeared and showed me the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* His smile is burnt into my mind and\x01",
            "won't go away...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_AF83")

    label("loc_AF08")


    ChrTalk(
        0xFE,
        (
            "Despite being younger, he exuded this aura\x01",
            "of mystery and passion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I wonder if I'll ever see him again...\x02",
    )

    CloseMessageWindow()

    label("loc_AF83")

    Jump("loc_B0C8")

    label("loc_AF88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B01E")

    ChrTalk(
        0xFE,
        (
            "My husband has been acting strange for\x01",
            "quite some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps he's just nervous. This is our first\x01",
            "time abroad and all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0C8")

    label("loc_B01E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B0C8")

    ChrTalk(
        0xFE,
        (
            "My husband planned out everything for our\x01",
            "honeymoon, making all of the reservations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This way, we know what we want to see\x01",
            "and when we want to see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0C8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_AD10 end

    def Function_28_B0D0(): pass

    label("Function_28_B0D0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x1A)
    ClearChrFlags(0x1A, 0x10)
    TurnDirection(0x1A, 0x0, 0)
    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B164")
    Jump("loc_B1AE")

    label("loc_B164")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B184")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1AE")

    label("loc_B184")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1A4")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1AE")

    label("loc_B1A4")

    OP_52(0x1A, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B1AE")

    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1A, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_B2C0")
    SetChrSubChip(0x1A, 0x0)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "C-Can't we stop here for today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Yes, please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Aaargh! This is so frustrating!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "You said you want to settle this before\x01",
            "the Anniversary Festival, right? Right?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B863")

    label("loc_B2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B3C6")
    SetChrSubChip(0x1A, 0x0)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "U-Um. *fidgets*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "About that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Come, now. There's no need to be so\x01",
            "nervous. It's just a marriage interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "You live in the same neighborhood, don't\x01",
            "you? It's not like you're strangers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B863")

    label("loc_B3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_B543")
    SetChrSubChip(0x1A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B50F")

    ChrTalk(
        0x1A,
        (
            "Well, let's move on. How about you two\x01",
            "tell each other about your hobbies?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "Um, I like reading. I-I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "I, uh, enjoy arranging flowers.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        "That's the most I've got out of them all day...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Just relax a little!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B53E")

    label("loc_B50F")


    ChrTalk(
        0x1A,
        "P-Please...just relax. I'm begging you...\x02",
    )

    CloseMessageWindow()

    label("loc_B53E")

    Jump("loc_B863")

    label("loc_B543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_B6DD")
    SetChrSubChip(0x1A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B640")

    ChrTalk(
        0x1A,
        (
            "Well, then, I assume that since you've\x01",
            "decided to meet, you're finally ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Y-Yeah. Ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "U-U-Um... R-Right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        (
            "Are you two listening? I said that you\x01",
            "shouldn't act so stiff.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B6D8")

    label("loc_B640")


    ChrTalk(
        0x1A,
        (
            "Well, then, I assume that since you've\x01",
            "decided to meet, you're finally ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Are you two listening?! I said that you\x01",
            "shouldn't act so stiff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6D8")

    Jump("loc_B863")

    label("loc_B6DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B863")
    SetChrSubChip(0x1A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7C0")

    ChrTalk(
        0x1A,
        (
            "So, what do you think about the weather\x01",
            "today? The sun is really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        (
            "Guys, you have to TALK! The conversation\x01",
            "isn't going anywhere like this!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B863")

    label("loc_B7C0")


    ChrTalk(
        0x1A,
        "As I was saying, the sun is really shining.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Come, now. There's no need to be so\x01",
            "nervous. It's just a marriage interview.\x01",
            "It's not like you're strangers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B863")

    SetChrSubChip(0x1A, 0x0)
    TalkEnd(0x1A)
    Return()

    # Function_28_B0D0 end

    def Function_29_B86B(): pass

    label("Function_29_B86B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B8FF")
    Jump("loc_B949")

    label("loc_B8FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B91F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B949")

    label("loc_B91F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B93F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B949")

    label("loc_B93F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B949")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_B9F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B98D")
    Call(0, 28)
    Jump("loc_B9ED")

    label("loc_B98D")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "C-Can't we stop here for today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Yes, please...\x02",
    )

    CloseMessageWindow()

    label("loc_B9ED")

    Jump("loc_BD24")

    label("loc_B9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BA61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA0D")
    Call(0, 28)
    Jump("loc_BA5C")

    label("loc_BA0D")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "U-Um. *fidgets*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "About that...\x02",
    )

    CloseMessageWindow()

    label("loc_BA5C")

    Jump("loc_BD24")

    label("loc_BA61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_BB8D")

    ChrTalk(
        0x1A,
        (
            "Well, how about you two tell each other\x01",
            "about your hobbies?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "Um, I like reading. I-I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "I, uh, enjoy arranging flowers.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        "That's the most I've got out of them all day...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Just relax a little!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_BD24")

    label("loc_BB8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_BC7C")

    ChrTalk(
        0x1A,
        (
            "Well, then, I assume that since you've\x01",
            "decided to meet, you're finally ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Y-Yeah. Ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "U-U-Um... R-Right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        (
            "Are you two listening? I said that you\x01",
            "shouldn't act so stiff.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_BD24")

    label("loc_BC7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BD24")

    ChrTalk(
        0x1A,
        "So, how about this heat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        (
            "Guys, you have to TALK! The conversation\x01",
            "isn't going anywhere like this!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)

    label("loc_BD24")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_B86B end

    def Function_30_BD2C(): pass

    label("Function_30_BD2C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BDC0")
    Jump("loc_BE0A")

    label("loc_BDC0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BDE0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BE0A")

    label("loc_BDE0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE00")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BE0A")

    label("loc_BE00")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BE0A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BED3")

    ChrTalk(
        0xFE,
        (
            "I was finally able to experience an\x01",
            "Arc en Ciel show yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...and it was AMAZING! I'm definitely\x01",
            "going to pick up the fanbook I saw.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFED")

    label("loc_BED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BFED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF76")

    ChrTalk(
        0xFE,
        (
            "The festival ended, but we've\x01",
            "decided to extend our stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, we haven't been able to see\x01",
            "Mishelam or Arc en Ciel yet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_BFED")

    label("loc_BF76")


    ChrTalk(
        0xFE,
        (
            "At the very least, I won't go home until I've\x01",
            "gone to Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And I've got to go on a shopping spree, too!\x02",
    )

    CloseMessageWindow()

    label("loc_BFED")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_BD2C end

    def Function_31_BFF5(): pass

    label("Function_31_BFF5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C089")
    Jump("loc_C0D3")

    label("loc_C089")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C0A9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0D3")

    label("loc_C0A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0C9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0D3")

    label("loc_C0C9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C0D3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C18C")

    ChrTalk(
        0xFE,
        (
            "The chef keeps on peeking out of the\x01",
            "kitchen, for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He even waved at me when our eyes\x01",
            "locked... What's his deal?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C22A")

    label("loc_C18C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C22A")

    ChrTalk(
        0xFE,
        "I was just looking into Arc en Ciel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From what I've heard, I should be\x01",
            "able to find tickets for this month's\x01",
            "show somewhere in the city...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C22A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_BFF5 end

    def Function_32_C232(): pass

    label("Function_32_C232")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C301")

    ChrTalk(
        0xFE,
        (
            "Well, then, what should I check\x01",
            "out first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People say Crossbell has issues maintaining\x01",
            "public order, but I'll just stay away from things\x01",
            "that seem sketchy. That way, I'll be safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4AB")

    label("loc_C301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C4AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C455")

    ChrTalk(
        0xFE,
        (
            "I came into Crossbell City this morning\x01",
            "by train. I was so excited to try all of the\x01",
            "delicacies...but, oh, how wrong I was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't tell you why, but the chef keeps\x01",
            "bringing me these really...weird dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's going on in this restaurant? Does he\x01",
            "keep getting my order wrong or something...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_C4AB")

    label("loc_C455")


    ChrTalk(
        0xFE,
        (
            "What's going on here? Is the chef getting\x01",
            "confused when I order or something...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4AB")

    TalkEnd(0xFE)
    Return()

    # Function_32_C232 end

    def Function_33_C4AF(): pass

    label("Function_33_C4AF")

    TalkBegin(0xFE)
    Call(0, 34)
    TalkEnd(0xFE)
    Return()

    # Function_33_C4AF end

    def Function_34_C4B9(): pass

    label("Function_34_C4B9")

    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0xB, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C54D")
    Jump("loc_C597")

    label("loc_C54D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C56D")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C597")

    label("loc_C56D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C58D")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C597")

    label("loc_C58D")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C597")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrSubChip(0xD, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_C68F")

    ChrTalk(
        0xD,
        (
            "#2100FI managed to convince City Hall to show\x01",
            "me all the registered names again.\x02\x03",
            "#2103FI made sure to copy down everything,\x01",
            "too, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Geez. Please just tell meeeee.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C7BA")

    label("loc_C68F")


    ChrTalk(
        0xD,
        (
            "#2100FWell, take a look at this guy's picture\x01",
            "in the margin right there.\x02\x03",
            "You've met him before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Huh. Maybe so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He was kind of a haughty-looking\x01",
            "middle-aged man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Who is he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100FThat's a secret!\x02\x03",
            "But... If I can get a big scoop,\x01",
            "I might just owe you something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_C7BA")

    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_34_C4B9 end

    def Function_35_C7C3(): pass

    label("Function_35_C7C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 7)), scpexpr(EXPR_END)), "loc_C8ED")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "Didn't you run into some trouble with the\x01",
            "mafia after the Anniversary Festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't hear much about you afterwards,\x01",
            "so I was starting to get a little anxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, you're all right, so everything's okay.\x01",
            "Good luck with all the CPD business, Tio!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    Jump("loc_CC92")

    label("loc_C8ED")


    ChrTalk(
        0xFE,
        "*gaaaaaaasp*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        "H-Hello there, Tio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FLong time no see, Chief Roberts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou're from the Epstein Foundation, right?\x02\x03",
            "Uh, did you come to leave Tio a new weapon\x01",
            "or something again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Actually, I heard that the Special Support Section\x01",
            "was involved in something dangerous recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahem. They were just some silly rumors\x01",
            "from Gironde, though. Nothing more than\x01",
            "that, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FI am sorry. I did not mean to worry you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FIt was gettin' pretty crazy for a bit, but\x01",
            "everything's cool now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FYes, there's no need to worry. The past two to\x01",
            "three weeks have been relatively peaceful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "V-Very well, then. I'm glad to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, Tio! I have the latest model orbal staff\x01",
            "with me. Put it to good use, okay?\x02",
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
        "#0211FLloyd was right, after all...\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    SetScenarioFlags(0xD0, 7)

    label("loc_CC92")

    TalkEnd(0xFE)
    Return()

    # Function_35_C7C3 end

    def Function_36_CC96(): pass

    label("Function_36_CC96")

    EventBegin(0x0)
    Fade(500)
    OP_68(58650, 500, -8880, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 58000, -1000, -9000, 90)
    SetChrPos(0x102, 57900, -1000, -8200, 90)
    SetChrPos(0x103, 56550, -1000, -9000, 90)
    SetChrPos(0x104, 56450, -1000, -8200, 90)
    OP_93(0x20, 0x10E, 0x0)
    SetChrSubChip(0x20, 0x0)
    OP_0D()

    ChrTalk(
        0x20,
        (
            "#11POh, yeah. Some engineer-lookin' guy\x01",
            "stopped by recently. Left something\x01",
            "he called an 'orbal staff' with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#11PSaid it's some fancy, new weapon...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#11P...but who the heck would I ever sell\x01",
            "a fishy thing like this to?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#0105F#5PAn orbal staff, you said? That's what\x01",
            "Tio uses, isn't it?\x02\x03",
            "Didn't she say it was still in the testing\x01",
            "phase of its development, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305F#5PForget who you're sellin' it to.\x01",
            "How are you able to sell it in\x01",
            "the first place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F#5PThe man looked like an engineer?\x01",
            "This whole thing is setting off all\x01",
            "sorts of alarms for me, personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206F#6PActually, that man might have been\x01",
            "my boss.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D007():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D007)
    Sleep(50)

    def lambda_D017():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D017)
    Sleep(50)

    def lambda_D027():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D027)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        "#0305F#5PBoss, eh? From the foundation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211F#6PYes, exactly. He may have come to\x01",
            "drop off a newer model of the orbal\x01",
            "staff for me to test.\x02\x03",
            "#0206FI do not understand why he could\x01",
            "not simply give it to me directly...\x02",
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
        0x101,
        (
            "#0012F#11P(Umm, yeah. Why couldn't he have\x01",
            "just handed it to her himself?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#11PNot sure what the deal with this thing is,\x01",
            "but I can sell it to the girl, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#11PBuy it, then. I already had\x01",
            "to pay for the shipment.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 58000, -1000, -8600, 90)
    SetScenarioFlags(0x4C, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_D272")
    SetScenarioFlags(0x4C, 4)

    label("loc_D272")

    EventEnd(0x5)
    Return()

    # Function_36_CC96 end

    def Function_37_D275(): pass

    label("Function_37_D275")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch06900.itc", 0x1E)
    LoadChrToIndex("chr/ch06902.itc", 0x1F)
    LoadChrToIndex("chr/ch37302.itc", 0x20)
    LoadChrToIndex("apl/ch50422.itc", 0x21)
    OP_68(6500, 1300, 9000, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrPos(0x24, 6500, 0, 7750, 0)
    SetChrPos(0x102, 6500, 0, 10250, 180)
    SetChrPos(0x103, 7750, 0, 9000, 270)
    SetChrPos(0x104, 5250, 0, 9000, 90)
    SetChrPos(0x101, 15000, 0, 9000, 270)
    SetChrPos(0x109, 17000, 0, 9000, 270)
    SetChrPos(0x19F, 16000, 0, 9000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#5P#0103FLloyd and Anton are late. What's\x01",
            "taking them so long?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FWho can say? I do know it is quite\x01",
            "rude to keep a lady waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0304FTsk, tsk, tsk. Dudes put just as much\x01",
            "care into getting dressed as ladies put\x01",
            "into getting dolled up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x104, 500)

    ChrTalk(
        0x24,
        (
            "#12P#1900FWow, Randy! You must be pretty experienced\x01",
            "if you know that off the top of your head.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x24, 500)

    ChrTalk(
        0x104,
        (
            "#6P#0300FYou can tell? I do what I can not to brag.\x02\x03",
            "#0300FHow 'bout goin' on a date with me next time,\x01",
            "Fran? I'd make sure to show you the coolest\x01",
            "places around town. You deserve it, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "#12P#1909FAw. You flatter me, Randy.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#11P#0111F(Randy, are you seriously hitting on her?\x01",
            "At a time like this?)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#6P#0309F(It was just a little joke to lighten\x01",
            "the mood!)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "Sorry about the wait, everyone.\x02",
    )

    CloseMessageWindow()
    OP_68(7750, 1100, 9000, 3000)
    MoveCamera(33, 25, 0, 3000)

    def lambda_D6ED():
        OP_97(0x101, 0xFFFFE98A, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D6ED)

    def lambda_D707():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D707)
    Sleep(50)

    def lambda_D71B():
        OP_97(0x19F, 0xFFFFE5A2, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_D71B)

    def lambda_D735():
        OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19F, 2, lambda_D735)
    Sleep(50)

    def lambda_D749():
        OP_97(0x109, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D749)

    def lambda_D763():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D763)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_D7BF():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D7BF)
    Sleep(50)

    def lambda_D7CF():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D7CF)
    Sleep(50)

    def lambda_D7DF():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D7DF)
    Sleep(50)

    def lambda_D7EF():
        OP_93(0x24, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_D7EF)
    WaitChrThread(0x101, 1)

    def lambda_D800():
        OP_97(0x101, 0x0, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D800)
    WaitChrThread(0x19F, 1)

    def lambda_D81E():
        OP_97(0x19F, 0x0, 0x0, 0xFFFFFB1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_D81E)
    WaitChrThread(0x101, 1)

    def lambda_D83C():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D83C)
    WaitChrThread(0x19F, 1)

    def lambda_D84D():
        OP_93(0x19F, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_D84D)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x19F, 1)
    OP_6F(0x79)

    ChrTalk(
        0x24,
        "#6P#1905FOh, it's Lloyd and Noey! And, er...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x19F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x19F,
        "#11PU-Uhh... Good afternoon.\x02",
    )

    CloseMessageWindow()
    OP_64(0x19F)

    ChrTalk(
        0x19F,
        (
            "#11PLong time no see... N-No, I mean...\x01",
            "sorry to make you wait so long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "#6P#1900FWhy hello, Anton.\x02",
    )

    CloseMessageWindow()
    OP_63(0x19F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19F,
        "#11PY-Y-You...know my name?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#6P#1900FOh, right. Lloyd and the others\x01",
            "told me your name earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PAhaha...hahaha... Got'cha.\x01",
            "(Got a bit too excited over that one...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0111F(Aren't you guys a little late?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0006F(Sorry about that. Choosing a present\x01",
            "took longer than we anticipated...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200F(Well, at least you were able to find\x01",
            "something.)\x02\x03",
            "(Is it nice?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#0500F(Umm, well, it should be fine. I don't\x01",
            "think it's too bad, if that means anything.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x24, 500)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#6P#0304FAll right, you two. Save the chitchat\x01",
            "for the meal.\x02\x03",
            "#0300FFran doesn't have too long a break,\x01",
            "right? Better not waste any time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x104, 500)

    ChrTalk(
        0x24,
        "#12P#1905FGood point.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x19F, 500)

    ChrTalk(
        0x24,
        "#6P#1900FWell, Anton, shall we find a table?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11PY-Yeah! Definitely!\x02",
    )

    CloseMessageWindow()

    def lambda_DC82():
        OP_97(0x24, 0xFFFFE0C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_DC82)
    Sleep(50)

    def lambda_DC9F():
        OP_97(0x19F, 0xFFFFE0C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_DC9F)
    Sleep(500)

    def lambda_DCBC():
        OP_93(0x101, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DCBC)

    def lambda_DCC9():
        OP_93(0x102, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DCC9)

    def lambda_DCD6():
        OP_93(0x103, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DCD6)

    def lambda_DCE3():
        OP_93(0x104, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DCE3)

    def lambda_DCF0():
        OP_93(0x109, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DCF0)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x19F, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#6P#0304FWeeell, I say we move on up to the\x01",
            "second floor.\x02\x03",
            "#0300FIt'll be kinda hard for us to keep watch\x01",
            "on 'em from here, y'know?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DDA9():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DDA9)

    def lambda_DDB6():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DDB6)

    def lambda_DDC3():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DDC3)

    def lambda_DDD0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DDD0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x101,
        "#11P#0005FYou want to eavesdrop on them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0309FC'mon, you can't tell me that you aren't\x01",
            "worried about how this'll go down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0204FWatching over our clients until the request\x01",
            "is complete is part of the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FThat's right. It's our duty to see\x01",
            "this through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#0506FSorry, but I am a little nervous about\x01",
            "this whole thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0x101, 0x109, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5P#0003FYou, too?\x02\x03",
            "#0000FWell, I guess you have a point. Besides,\x01",
            "Anton looks like he's sweating bullets...\x02\x03",
            "Maybe keeping an eye on them is for the\x01",
            "best. We can keep him in check.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0309FSweet! Since it's decided,\x01",
            "let's head upstairs! ☆\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#11P#0006F(Someone's not taking this very seriously...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(2000, 6500, 9730, 0)
    MoveCamera(48, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x19F, 0x20)
    SetChrSubChip(0x19F, 0x0)
    SetChrFlags(0x19F, 0x4)
    SetChrFlags(0x19F, 0x8000)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x19F, -1100, 100, 2300, 270)
    SetChrPos(0x24, -5350, 100, 2300, 90)
    SetChrPos(0x101, 0, 5000, 10000, 180)
    SetChrPos(0x102, 750, 5000, 9750, 180)
    SetChrPos(0x104, 1500, 5000, 10000, 180)
    SetChrPos(0x109, -750, 5000, 9750, 180)
    SetChrPos(0x103, -1500, 5000, 10000, 180)
    OP_68(0, 6500, 9750, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0x157C)
    OP_6F(0x79)
    Fade(500)
    OP_68(-3240, 1100, 2340, 0)
    MoveCamera(36, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    SetCameraDistance(19000, 3000)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)

    ChrTalk(
        0x19F,
        (
            "#11PU-Uh, yeah. They told m-me that you\x01",
            "still remembered me, Fran...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#6P#1909FWell, of course. It happened on the last\x01",
            "day of the Anniversary Festival. How\x01",
            "could I forget?\x02\x03",
            "#1900FThat sure was a rough day... You haven't\x01",
            "dropped your wallet again, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11P'C-Course not!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PAfter all the effort you spent to find it, I'm\x01",
            "never letting it out of my sight again!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x24)

    ChrTalk(
        0x24,
        "#6P#1909FAhaha! You're a riot, Anton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11P(Y-Yes...! I don't understand what part\x01",
            "of that was funny, but I think things are\x01",
            "going okay?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#6P#1905FThat reminds me, Anton. After I found\x01",
            "your wallet, you kept on spacing out a\x01",
            "lot.\x02\x03",
            "#1900FYou know, I was worried that you came\x01",
            "down with a fever or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11P#2SI was probably just captivated by your\x01",
            "good looks...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x24,
        "#6P#1905FHmmm? Did you say something?\x02",
    )

    CloseMessageWindow()
    OP_63(0x19F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x19F,
        "#11PN-Nope! Hahaha...\x02",
    )

    CloseMessageWindow()
    OP_64(0xFFFF)
    Fade(500)
    OP_68(0, 6500, 9730, 0)
    MoveCamera(48, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#5P#0304FPoor Anton still has a long way to\x01",
            "go when it comes to ladies.\x02\x03",
            "#0300FYou ain't gonna be able to pick up chicks\x01",
            "if you can't say that stuff without mumblin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FBut, you know, they seem to be getting\x01",
            "along pretty well. Fran is chatting away,\x01",
            "like usual.\x02\x03",
            "#0012FAnton, on the other hand...still looks pretty tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#0503FFran's about as sociable as you can get.\x01",
            "Definitely way more than me, at least.\x02\x03",
            "#0500FShe would act like this even if she only\x01",
            "just met the person.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x109, 500)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#6P#0205FNoel, are you all right?\x02\x03",
            "#0200FYou appear to be bothered by something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x109, 0x103, 500)
    Sleep(750)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#11P#0502FWell, I wouldn't go that far...\x02\x03",
            "#0506FIt's just... Sure, she's always well liked\x01",
            "by everyone, but I've never seen her\x01",
            "actually flirt with anyone before.\x02\x03",
            "#0508FAnd yet she's acting unusually friendly\x01",
            "with Anton...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#11P#0102FYou're just worried about your\x01",
            "sister, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#6P#0505FI-I mean...\x02\x03",
            "#0504FI guess that's it. She's my little sister,\x01",
            "you know? Of course I'm worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000F(I guess she's the type of older\x01",
            "sister to worry easily.)\x02\x03",
            "#0006F(I sure hope I don't give Cecile\x01",
            "cause for concern like this.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0305FWhoa! Guys, look! That right there is the\x01",
            "face of a man who knows what he wants.\x02\x03",
            "#0309FI think he's finally pullin' the trigger!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_EB38():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EB38)

    def lambda_EB45():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EB45)

    def lambda_EB52():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EB52)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    Fade(500)
    OP_68(-3240, 1100, 2340, 0)
    MoveCamera(36, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    OP_0D()
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_64(0x24)
    OP_63(0x19F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_64(0x19F)
    OP_63(0x19F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x19F)

    ChrTalk(
        0x19F,
        "#11PU-Umm... Hey, Fran!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "#6P#1905FYes? Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PWell, I just want to explain why I was\x01",
            "searching for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PI wanted to show my gratitude to you for\x01",
            "not giving up on finding my wallet during\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11PSo, will you accept this?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_EE85")
    OP_2C(0x2A, 0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Anton gave Fran a stuffed Mishy plush.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x24,
        (
            "#6P#1905FA Mishy plush?\x02\x03",
            "#1909FOh, wow! Thank you, Anton!\x02\x03",
            "I actually already own one, but I've\x01",
            "been meaning to get a second one\x01",
            "lately!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11P(C-Crap. She already has one? She\x01",
            "still looks so happy, though! I don't\x01",
            "know how to process this!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11P(Well, it's now or never, Anton.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_F521")

    label("loc_EE85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_EFFB")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Anton gave Fran a jar of ice jam.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x24,
        (
            "#6P#1905FIsn't this that rare, imported jam\x01",
            "that Times sells?\x02\x03",
            "#1900FThank you so much, Anton! I can't\x01",
            "say I was expecting something like\x01",
            "this. Almost feels like it's New Year's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11P(Crap! New Year's? Did I pick wrong,\x01",
            "after all?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11P(S-Still, it's now or never, Anton!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_F521")

    label("loc_EFFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_F1C9")
    OP_2C(0x2A, 0x3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Anton gave Fran a knitted Pom beanie.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x24,
        (
            "#6P#1905FWow, wow, wow! A white Pom hat!\x02\x03",
            "#1900FMy sister, Noey, actually likes to wear\x01",
            "a white hat like this when not in uniform.\x02\x03",
            "This is perfect. I've wanted a white\x01",
            "hat to match hers for a while now!\x02\x03",
            "#1909FThank you SO much, Anton! I swear\x01",
            "I'll treasure it forever and always!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11P(Y-Yes! She loves it!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11P(Here we go! It's now or never, Anton!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_F521")

    label("loc_F1C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_F398")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Anton gave Fran a pair of Strega boots.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x24,
        (
            "#6P#1905FAren't these those new Strega Corporation\x01",
            "boots?\x02\x03",
            "#1900FI think I read somewhere that these are all\x01",
            "the rage among girls lately. Actually, I'm\x01",
            "pretty sure I saw a girl wearing them earlier.\x02\x03",
            "Boots aren't exactly my thing, but I promise\x01",
            "I'll take good care of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11P(N-Not her thing? Did I screw up?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11P(Either way, it's now or never, Anton!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_F521")

    label("loc_F398")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_F521")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Anton gave Fran a pink moon necklace.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x24,
        (
            "#6P#1905FWait... I think I saw this in a magazine a\x01",
            "while ago! Isn't it insanely expensive?!\x02\x03",
            "A-Are you sure I can have this?\x02\x03",
            "#1900FUm, well, thank you. I'll cherish it, Anton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11P(I knew it! That necklace was way too\x01",
            "nice a gift for the first date!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11P(S-Still, it's now or never, Anton!)\x02",
    )

    CloseMessageWindow()

    label("loc_F521")


    ChrTalk(
        0x19F,
        "#11PF-Fran! D-Do you have someone you like?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x24)
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x24,
        (
            "#6P#1905FHuh? Um... No, not really.\x02\x03",
            "#1904FOh!\x02\x03",
            "#1909FBut there IS someone I love with\x01",
            "all my heart! ㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    StopBGM(0x1F4)
    Sound(889, 0, 100, 0)

    ChrTalk(
        0x19F,
        "#11P#4S...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x24)
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x24,
        "#6P#1905FWh-What's the matter, Anton?\x02",
    )

    CloseMessageWindow()
    OP_64(0x24)

    ChrTalk(
        0x104,
        "#N#0306F(Uh-oh. Was he already shot down?)\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#N#0006F(I think the fact that Fran didn't mean\x01",
            "anything by the comment made it cut\x01",
            "even deeper...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#N#0106F(Sadly, I don't think there's anything we\x01",
            "can really do in a case like this.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#N#0203F(Shall we pray for him?)\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#N#0505F(...)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    PlayBGM("ed7005", 0)

    ChrTalk(
        0x19F,
        "#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11PH-Hahaha... Don't worry, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11P...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x19F, 0xFF)
    SetChrSubChip(0x19F, 0x0)
    SetChrPos(0x19F, -1100, 0, 3300, 270)
    Sound(820, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x24,
        "#6P#1905FAnton?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11PSorry. I gotta go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PFran. I really hope you and that\x01",
            "person...work out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "#6P#1905FWhat?\x02",
    )

    CloseMessageWindow()

    def lambda_F899():
        OP_97(0x19F, 0x1B58, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_F899)
    Sleep(3000)
    Fade(500)
    OP_68(7790, 1400, 6860, 0)
    MoveCamera(41, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19800, 0)
    EndChrThread(0x19F, 0x1)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrPos(0x19F, 7000, 0, 9000, 0)
    SetChrPos(0x24, 0, 0, 9000, 0)
    SetChrPos(0x101, 8500, 0, 4750, 0)
    SetChrPos(0x109, 7750, 0, 3750, 0)
    SetChrPos(0x102, 9250, 0, 4250, 0)
    SetChrPos(0x103, 7750, 0, 2750, 0)
    SetChrPos(0x104, 9250, 0, 3250, 0)

    def lambda_F968():
        OP_97(0x19F, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_F968)

    def lambda_F982():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F982)
    Sleep(30)

    def lambda_F99F():
        OP_97(0x109, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F99F)
    Sleep(30)

    def lambda_F9BC():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F9BC)
    Sleep(30)

    def lambda_F9D9():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F9D9)
    Sleep(30)

    def lambda_F9F6():
        OP_97(0x104, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F9F6)
    OP_0D()
    WaitChrThread(0x19F, 1)
    OP_93(0x19F, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_FAA7")

    ChrTalk(
        0x19F,
        "#5POh, hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PThanks for everything. Because of you,\x01",
            "I was able to see Fran's beautiful smile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC71")

    label("loc_FAA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_FB18")

    ChrTalk(
        0x19F,
        "#5POh, hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PThanks for helping me out with the\x01",
            "present and everything. I mean it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC71")

    label("loc_FB18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_FB94")

    ChrTalk(
        0x19F,
        "#5POh, hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PThanks for everything. Because of you,\x01",
            "I was able to see Fran's beautiful smile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC71")

    label("loc_FB94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_FC05")

    ChrTalk(
        0x19F,
        "#5POh, hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PThanks for helping me out with the\x01",
            "present and everything. I mean it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC71")

    label("loc_FC05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_FC71")

    ChrTalk(
        0x19F,
        "#5POh, hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PThanks for helping me out with the\x01",
            "present and everything. I mean it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC71")


    ChrTalk(
        0x101,
        "#12P#0006FA-Anton, I don't know what to say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PDon't bother. I don't need to be comforted\x01",
            "or babied. This happens to me all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PMy life is, and always will be, a clumsy\x01",
            "series of trial and error. Maybe someday,\x01",
            "things will work out for a guy like me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#12P#0206FI do not quite follow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#5PHaha... Didn't you notice?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PThat tranquil, happy face when Fran\x01",
            "said she has someone she loves...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PAfter I saw that, I knew I was going\x01",
            "nowhere fast. I just had to give up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#5PAnd that's that, friends.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_FF00():
        OP_97(0x19F, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_FF00)
    Sleep(1000)

    def lambda_FF1D():
        OP_93(0x101, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FF1D)
    Sleep(50)

    def lambda_FF2D():
        OP_93(0x102, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FF2D)
    Sleep(50)

    def lambda_FF3D():
        OP_93(0x103, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FF3D)
    Sleep(50)

    def lambda_FF4D():
        OP_93(0x104, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FF4D)
    Sleep(50)

    def lambda_FF5D():
        OP_93(0x109, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FF5D)
    Sleep(1000)

    def lambda_FF6D():
        OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19F, 2, lambda_FF6D)
    WaitChrThread(0x19F, 1)
    WaitChrThread(0x19F, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x104,
        "#12P#0306FWhew. That guy is ULTRA depressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FIt may take some time, but I'm sure he'll\x01",
            "be fine.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x24,
        "Fran's Voice",
        "Aw... Anton really did leave.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_10098():
        OP_93(0x101, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10098)

    def lambda_100A5():
        OP_93(0x102, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_100A5)

    def lambda_100B2():
        OP_93(0x103, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_100B2)

    def lambda_100BF():
        OP_93(0x104, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_100BF)

    def lambda_100CC():
        OP_93(0x109, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_100CC)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)

    def lambda_100E1():
        OP_97(0x24, 0x2134, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_100E1)
    Sleep(2500)

    def lambda_100FE():
        OP_93(0x101, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_100FE)
    Sleep(50)

    def lambda_1010E():
        OP_93(0x102, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1010E)
    Sleep(50)

    def lambda_1011E():
        OP_93(0x103, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1011E)
    Sleep(50)

    def lambda_1012E():
        OP_93(0x104, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1012E)
    Sleep(50)

    def lambda_1013E():
        OP_93(0x109, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1013E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x24, 1)
    OP_93(0x24, 0xB4, 0x1F4)

    ChrTalk(
        0x24,
        (
            "#5P#1905FHe must have been running late for\x01",
            "his airship or something, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#0507FF-Fran!\x02",
    )

    CloseMessageWindow()
    OP_97(0x109, 0x0, 0x0, 0xCB2, 0x1388, 0x0)
    TurnDirection(0x109, 0x24, 0)
    TurnDirection(0x24, 0x109, 500)

    ChrTalk(
        0x24,
        (
            "#11P#1905FNoey? What's up? You look like you\x01",
            "saw a ghost or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0503FFran, give it to me straight...\x02\x03",
            "#0501F#4SWho's this person you supposedly love?!\x02\x03",
            "#0501F#4SIs it Lloyd?!\x02\x03",
            "#0505F#4SOr, don't tell me... Randy?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0011FWh-Whoa, hold on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0206F(I was wondering why the sergeant major\x01",
            "was being so quiet... This answers that\x01",
            "question, then.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0309FOh, boy. Now that the cat's outta the\x01",
            "bag, it looks li--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#5P#0109FHey, Randy? I'm going to stop you\x01",
            "right there. Don't make things even\x01",
            "more complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0306F(Th-That smile could stop a Rhinocider...)\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)

    ChrTalk(
        0x109,
        (
            "#6P#0508FYou tell me everything, don't you? Why\x01",
            "would you hide something as big as this\x01",
            "from me?\x02\x03",
            "#0510FHe isn't some troublemaker that you can't\x01",
            "tell anyone about, is he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#11P#1906FC-Calm down a little, Noey.\x01",
            "Everyone is looking at us funny...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0501FThere's no time! Tell me!\x02\x03",
            "Pretend the rest of them are sacks of\x01",
            "potatoes or something!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x24, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x24,
        (
            "#11P#1906FOh, geez, Noey...\x02\x03",
            "#1900FIf you want to know that bad, I'll give\x01",
            "you a hint.\x02\x03",
            "#1904FThat special someone works in the\x01",
            "Crossbell Guardian Force and has a\x01",
            "very strong sense of justice.\x02\x03",
            "#1902FAnd they've always been as kind as\x01",
            "can be to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0505FHe's in the CGF? He isn't stationed\x01",
            "at Tangram Gate, is he?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "#11P#1909FThey are! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0506FI never knew someone in my unit\x01",
            "was that close to you!\x02\x03",
            "#0508FIs it Jack? Burrell?! No, wait... Is it\x01",
            "Mr. Temas from the mess hall?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006FThis is getting a little out of hand...\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x24,
        (
            "#11P#1906F*sigh* I'm disappointed, Noey. I thought\x01",
            "you would've figured it out by now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#0501FYou didn't give me much to go on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#11P#1902FAre you really going to make me say it?\x02\x03",
            "#1909FIsn't it obvious that I was talking about\x01",
            "you? ㈱\x02",
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
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x109,
        "#6P#0505F#4SYou're kidding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "#11P#1905FOopsie! My break's almost over!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x101, 500)

    ChrTalk(
        0x24,
        (
            "#5P#1909FI'll see you all later! Take good\x01",
            "care of Noey for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0012FY-Yeah. See ya, Fran.\x02",
    )

    CloseMessageWindow()

    def lambda_10B4A():
        OP_97(0x24, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_10B4A)
    Sleep(1000)

    def lambda_10B67():
        OP_93(0x101, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10B67)
    Sleep(50)

    def lambda_10B77():
        OP_93(0x102, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10B77)
    Sleep(50)

    def lambda_10B87():
        OP_93(0x103, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10B87)
    Sleep(50)

    def lambda_10B97():
        OP_93(0x104, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10B97)
    Sleep(1000)

    def lambda_10BA7():
        OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_10BA7)
    WaitChrThread(0x19F, 1)
    WaitChrThread(0x19F, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#12P#0304FHaha. So that's how it was, eh?\x02\x03",
            "#0300FDoubt Fran will know about romance\x01",
            "for a while, with a head like that on\x01",
            "her shoulders.\x02\x03",
            "#0309FAt least the sergeant major here can\x01",
            "rest easy for now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x109, 0x21)
    Sleep(200)
    SetChrSubChip(0x109, 0x0)
    Sleep(200)
    SetChrSubChip(0x109, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(200)
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    ChrTalk(
        0x109,
        "#5P#0506F#40WOh, thank Aidios... Thank you...\x02",
    )

    CloseMessageWindow()

    def lambda_10D49():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10D49)
    Sleep(50)

    def lambda_10D59():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10D59)
    Sleep(50)

    def lambda_10D69():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10D69)
    Sleep(50)

    def lambda_10D79():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10D79)
    WaitChrThread(0x101, 1)

    def lambda_10D8A():
        OP_97(0x101, 0x0, 0x0, 0x640, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10D8A)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        "#11P#0011FH-Hey, are you doing all right, Sergeant Major?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#0509FSorry about that. It's just, I suddenly\x01",
            "felt a wave of exhaustion hit me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0102FAw. You really were worried about her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#0506FYeah, I...might have gone a little overboard\x01",
            "there. Sorry, guys. I never meant to let you\x01",
            "see that side of me.\x02\x03",
            "#0500FThank you for helping me\x01",
            "with this mess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0012FStill, I can't help but feel bad for Anton.\x01",
            "Do you think he'll ever love again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0204FAre not you feeling sorry for yourself,\x01",
            "too, Lloyd?\x02\x03",
            "#0202FI saw your eyes light up when Fran\x01",
            "said there was someone she loved.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#5P#0011FThat definitely didn't happen! And I'd\x01",
            "really appreciate it if you didn't make\x01",
            "misleading comments like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0304FAnyway, we can always go check on\x01",
            "Anton when we're free later.\x02\x03",
            "#0300FFor now, I'd say our job here is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FYeah, I guess so.\x02\x03",
            "Ready to go, guys?\x02",
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
            "[A Sincere Favor]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x19F, 0x80)
    SetChrBattleFlags(0x19F, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    RemoveParty(0x9E, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_68(8500, 1500, 9000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 8500, 0, 9000, 180)
    SetChrPos(0x1, 8500, 0, 9000, 180)
    SetChrPos(0x2, 8500, 0, 9000, 180)
    SetChrPos(0x3, 8500, 0, 9000, 180)
    OP_29(0x2A, 0x1, 0x9)
    OP_29(0x2A, 0x4, 0x10)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_37_D275 end

    def Function_38_1127C(): pass

    label("Function_38_1127C")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x0, 0xA, 0)
    Fade(800)
    OP_68(-51320, 1500, 3430, 0)
    MoveCamera(41, 23, -2, 0)
    OP_6E(540, 0)
    SetCameraDistance(13800, 0)
    SetChrPos(0x101, -50000, 0, 3500, 270)
    SetChrPos(0x102, -48800, 0, 3500, 270)
    SetChrPos(0x103, -50000, 0, 4900, 270)
    SetChrPos(0x104, -48800, 0, 4900, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11330")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, -47860, 0, 4640, 270)
    Jump("loc_1135B")

    label("loc_11330")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1135B")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, -47860, 0, 4640, 270)

    label("loc_1135B")

    OP_0D()

    ChrTalk(
        0xA,
        "#6POh, no! What do I do?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PThe manager and Braun won't help\x01",
            "me... What in the world do I do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FExcuse me. We received a request from\x01",
            "an employee here named Selteo. Do you\x01",
            "know him, by any chance?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(-50110, 1300, 4210, 1000)
    OP_95(0xA, -51650, 0, 4140, 2000, 0x0)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(200)

    ChrTalk(
        0xA,
        (
            "#6PYou came to help me?! Oh, thank you,\x01",
            "thank you! You're the, um...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FSpecial Support Section. Pleasure to\x01",
            "make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0100FWe'd love to help you, if you'll have us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0309FYep! The customer is always right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FWe're always here to help.\x01",
            "(I get the feeling I'm becoming some sort of errand boy.)\x02\x03",
            "So, your request. It involves searching\x01",
            "for something, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6PYes, that's right! Save me, man!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PYou see, I was told by the manager to try\x01",
            "and come up with a new dish for the\x01",
            "restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PBut yeah... It's not going well. I've reached\x01",
            "my creative limit. It's useless. It's all useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FWell, that kind of thing happens\x01",
            "to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0303FEven if you're a pro chef, it's not that\x01",
            "easy to always be comin' up with new\x01",
            "stuff, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PBasically. Having to cook for celebrities from\x01",
            "time to time doesn't make it any easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6PSo, that's why I need you to help me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PI heard that your division mingles with the\x01",
            "public a lot, so I thought that you might\x01",
            "have been to your fair share of restaurants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PI'm looking for dishes that are truly unique.\x01",
            "Entrees that you sometimes make when\x01",
            "thinking outside the box!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0203FAs in, peculiar dishes?\x02\x03",
            "#0200FKinda like when you set out to cook an omelet\x01",
            "rice but wind up with something completely\x01",
            "different. Is that what you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6PExactly! That's the very essence of cuisine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PThere's a fine line between failure and\x01",
            "success! That, my friends, is where new\x01",
            "ideas wait for us!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#6PSo, you guys cook, too? That's perfect!\x01",
            "Now my expectations are sky-high!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0012FI don't think anything we make is fit for a\x01",
            "professional chef, personally...\x02\x03",
            "#0000FAnyway, I think we understand your issue\x01",
            "now. We just need to bring you peculiar\x01",
            "dishes we've made, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PYep, that'd be great. I want to compare all\x01",
            "of them, so I'll need at least ten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PBut I mean, the more, the merrier. Cook\x01",
            "as many as you can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PThat about wraps it up, I think. My\x01",
            "taste buds and I will be waiting!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Creative Cooks Wanted!]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -50150, 0, 4140, 270)
    SetChrPos(0xA, -52030, 0, 3650, 270)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11D64")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_11D64")

    OP_29(0x29, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_38_1127C end

    def Function_39_11D6D(): pass

    label("Function_39_11D6D")

    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(800)
    OP_68(-50110, 1300, 4210, 0)
    MoveCamera(41, 23, -2, 0)
    OP_6E(540, 0)
    SetCameraDistance(13800, 0)
    SetChrPos(0x101, -50000, 0, 3500, 270)
    SetChrPos(0x102, -48800, 0, 3500, 270)
    SetChrPos(0x103, -50000, 0, 4900, 270)
    SetChrPos(0x104, -48800, 0, 4900, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11E1D")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, -47860, 0, 4640, 270)
    Jump("loc_11E48")

    label("loc_11E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11E48")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, -47860, 0, 4640, 270)

    label("loc_11E48")

    SetChrPos(0xA, -51650, 0, 4140, 90)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#6PWell, I'll go ahead and take those,\x01",
            "if you don't mind.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11F1D")

    ChrTalk(
        0xA,
        (
            "#6PHmm... It's less than I was hoping for, but\x01",
            "hopefully there's a spark of inspiration\x01",
            "hiding among them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12229")

    label("loc_11F1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11FAF")
    OP_2C(0x29, 0x2)

    ChrTalk(
        0xA,
        (
            "#6PHmm... Yeah, this should be enough.\x01",
            "After I get done sampling, I'm going to\x01",
            "come up with the greatest dish ever!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12229")

    label("loc_11FAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1204E")
    OP_2C(0x29, 0x4)

    ChrTalk(
        0xA,
        (
            "#6PStill, who would've guessed that you'd find\x01",
            "this many...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PSuccess! I can totally make an original dish\x01",
            "with this one!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12229")

    label("loc_1204E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12229")
    OP_2C(0x29, 0x6)

    ChrTalk(
        0xA,
        (
            "#6PMan, just who are you guys?\x01",
            "You literally brought me every dish\x01",
            "imaginable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PYou guys sure know your Crossbellan\x01",
            "cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FHaha, we'll take your word for it.\x02\x03",
            "I suppose we do cook for ourselves just\x01",
            "about every day, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300FYeah. Turns out, we each have our own\x01",
            "specialties we're good at. I make a mean\x01",
            "mapo tofu, if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PWow. You all really do have the hearts of\x01",
            "chefs... I'm touched.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12229")

    Call(0, 42)

    ChrTalk(
        0xA,
        (
            "#6PAnyway, you guys are lifesavers. Thinking\x01",
            "about what would've happened if I didn't\x01",
            "come up with a new recipe... *shiver*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0005FUh, what exactly would've happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PY-Yeah, you don't want to know. Forget\x01",
            "I said anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#6PAh, right. Want to try a bite of the test\x01",
            "dish? I still have to thank you, y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PThe taste isn't quite there yet, but behold\x01",
            "my creation: Truffle and Fish Eyeball Soup!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12478")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_12478")

    Sleep(1200)

    ChrTalk(
        0x103,
        (
            "#11P#0211FRegardless of how it tastes, it looks\x01",
            "absolutely horrid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0106FIt's certainly an...odd combination.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0300F'Preciate the offer, but I'll pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PReally? What a shame. I was hoping\x01",
            "to get some early feedback...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_12A0D")

    ChrTalk(
        0xA,
        "#6POh, well, I'll just give you this instead.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1273A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x10)

    ChrTalk(
        0xA,
        (
            "#6PYou remember that creamy soup that\x01",
            "you gave me before? Looking at that,\x01",
            "I was struck with culinary genius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PBut since it's a little too plain, I thought it\x01",
            "wouldn't be popular with the customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6PStill, feel free to try it out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12854")

    label("loc_1273A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1BE, 1)

    ChrTalk(
        0xA,
        (
            "#6PI made the dish using the Truffle and\x01",
            "Fish Eyeball Soup as a base, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6P...since it's a little too plain, I can't\x01",
            "exactly put it on the menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6PAnyway, feel free to try it sometime.\x02",
    )

    CloseMessageWindow()

    label("loc_12854")


    ChrTalk(
        0x101,
        (
            "#11P#0000FThanks.\x02\x03",
            "#0003FI don't see what's so bad about\x01",
            "a dish being plain, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#6PHmm? You say something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006FNothing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100F(Perhaps his palate is a tad\x01",
            "TOO sophisticated...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PSweet. I'll go ahead and start\x01",
            "sampling everything, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PThanks for doing this, guys. If I need\x01",
            "anything else, I'll give you a call!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0200FWe are available any time.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_12BFD")

    label("loc_12A0D")


    ChrTalk(
        0xA,
        "#6POh, right. Take this, as thanks.\x02",
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
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1F5, 1)

    ChrTalk(
        0xA,
        (
            "#6PThat baby works wonders whenever\x01",
            "you get yourself food poisoning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0005FTh-Thanks, Selteo.\x02\x03",
            "#0006FYou really are putting your heart and\x01",
            "soul into this job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PWell, there's a lot riding on this. And\x01",
            "as a chef, I've got to answer the call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PThanks for doing this, guys. If I need\x01",
            "anything else, I'll give you a call!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FWe'll be waiting.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_12BFD")

    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Creative Cooks Wanted!]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -50150, 0, 4140, 270)
    SetChrPos(0xA, -52030, 0, 3650, 270)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12CAC")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_12CAC")

    OP_29(0x29, 0x4, 0x10)
    OP_29(0x29, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_39_11D6D end

    def Function_40_12CBA(): pass

    label("Function_40_12CBA")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_END)), "loc_12CDD")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12CDD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_END)), "loc_12CF6")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12CF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_END)), "loc_12D0F")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D0F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_END)), "loc_12D28")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_END)), "loc_12D41")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_END)), "loc_12D5A")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_END)), "loc_12D73")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D73")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_END)), "loc_12D8C")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D8C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_END)), "loc_12DA5")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12DA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_END)), "loc_12DBE")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12DBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_END)), "loc_12DD7")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12DD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_END)), "loc_12DF0")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12DF0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_END)), "loc_12E09")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_END)), "loc_12E22")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_END)), "loc_12E3B")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E3B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_END)), "loc_12E54")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E54")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_END)), "loc_12E6D")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_END)), "loc_12E86")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E86")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_END)), "loc_12E9F")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E9F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_END)), "loc_12EB8")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12EB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_END)), "loc_12ED1")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12ED1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_END)), "loc_12EEA")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12EEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_END)), "loc_12F03")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12F03")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_END)), "loc_12F1C")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12F1C")

    Return()

    # Function_40_12CBA end

    def Function_41_12F1D(): pass

    label("Function_41_12F1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F31")
    Jump("loc_13461")

    label("loc_12F31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F66")

    ChrTalk(
        0xA,
        "You have...1 peculiar dish.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_12F66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F9D")

    ChrTalk(
        0xA,
        "You have...2 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_12F9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FD4")

    ChrTalk(
        0xA,
        "You have...3 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_12FD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1300B")

    ChrTalk(
        0xA,
        "You have...4 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_1300B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13042")

    ChrTalk(
        0xA,
        "You have...5 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_13042")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13079")

    ChrTalk(
        0xA,
        "You have...6 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_13079")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130B0")

    ChrTalk(
        0xA,
        "You have...7 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_130B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130E7")

    ChrTalk(
        0xA,
        "You have...8 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_130E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1311E")

    ChrTalk(
        0xA,
        "You have...9 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_1311E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13156")

    ChrTalk(
        0xA,
        "You have...10 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_13156")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1318E")

    ChrTalk(
        0xA,
        "You have...11 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_1318E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131C6")

    ChrTalk(
        0xA,
        "You have...12 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_131C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131FE")

    ChrTalk(
        0xA,
        "You have...13 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_131FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13236")

    ChrTalk(
        0xA,
        "You have...14 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_13236")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1326E")

    ChrTalk(
        0xA,
        "You have...15 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_1326E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132A6")

    ChrTalk(
        0xA,
        "You have...16 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_132A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132DE")

    ChrTalk(
        0xA,
        "You have...17 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_132DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13316")

    ChrTalk(
        0xA,
        "You have...18 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_13316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1334E")

    ChrTalk(
        0xA,
        "You have...19 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_1334E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13386")

    ChrTalk(
        0xA,
        "You have...20 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_13386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133BE")

    ChrTalk(
        0xA,
        "You have...21 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_133BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133F6")

    ChrTalk(
        0xA,
        "You have...22 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_133F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1342E")

    ChrTalk(
        0xA,
        "You have...23 peculiar dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13461")

    label("loc_1342E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13461")

    ChrTalk(
        0xA,
        "You have...24 peculiar dishes.\x02",
    )

    CloseMessageWindow()

    label("loc_13461")

    Return()

    # Function_41_12F1D end

    def Function_42_13462(): pass

    label("Function_42_13462")

    ClearScenarioFlags(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_END)), "loc_13475")
    SubItemNumber(0x192, 1)

    label("loc_13475")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_END)), "loc_13485")
    SubItemNumber(0x195, 1)

    label("loc_13485")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_END)), "loc_13495")
    SubItemNumber(0x198, 1)

    label("loc_13495")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_END)), "loc_134A5")
    SubItemNumber(0x19B, 1)

    label("loc_134A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_END)), "loc_134B5")
    SubItemNumber(0x19E, 1)

    label("loc_134B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_END)), "loc_134C5")
    SubItemNumber(0x1A1, 1)

    label("loc_134C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_END)), "loc_134D5")
    SubItemNumber(0x1A4, 1)

    label("loc_134D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_END)), "loc_134E5")
    SubItemNumber(0x1A7, 1)

    label("loc_134E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_END)), "loc_134F5")
    SubItemNumber(0x1AA, 1)

    label("loc_134F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_END)), "loc_13505")
    SubItemNumber(0x1AD, 1)

    label("loc_13505")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_END)), "loc_13515")
    SubItemNumber(0x1B0, 1)

    label("loc_13515")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_END)), "loc_13525")
    SubItemNumber(0x1B3, 1)

    label("loc_13525")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_END)), "loc_13535")
    SubItemNumber(0x1B6, 1)

    label("loc_13535")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_END)), "loc_13545")
    SubItemNumber(0x1B9, 1)

    label("loc_13545")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_END)), "loc_13558")
    SubItemNumber(0x1BC, 1)
    SetScenarioFlags(0x2, 1)

    label("loc_13558")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_END)), "loc_13568")
    SubItemNumber(0x1BF, 1)

    label("loc_13568")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_END)), "loc_13578")
    SubItemNumber(0x1C2, 1)

    label("loc_13578")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_END)), "loc_13588")
    SubItemNumber(0x1C5, 1)

    label("loc_13588")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_END)), "loc_13598")
    SubItemNumber(0x1C8, 1)

    label("loc_13598")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_END)), "loc_135A8")
    SubItemNumber(0x1CB, 1)

    label("loc_135A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_END)), "loc_135B8")
    SubItemNumber(0x1CE, 1)

    label("loc_135B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_END)), "loc_135C8")
    SubItemNumber(0x1D1, 1)

    label("loc_135C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_END)), "loc_135D8")
    SubItemNumber(0x1D4, 1)

    label("loc_135D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_END)), "loc_135E8")
    SubItemNumber(0x1D7, 1)

    label("loc_135E8")

    Return()

    # Function_42_13462 end

    SaveToFile()

Try(main)
