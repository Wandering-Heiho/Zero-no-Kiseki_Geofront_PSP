from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0510.bin",                # FileName
        "t0510",                    # MapName
        "t0510",                    # Location
        0x003D,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 61, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0510",                  # 0
        "Mayor Bickson",          # 1
        "Mayor Bickson",          # 2
        "Anna",                   # 3
        "Anna",                   # 4
        "Miner Marlow",           # 5
        "Miner Max",              # 6
        "Miner Max",              # 7
        "Lurieda",                # 8
        "Miranda",                # 9
        "Old Lady Bilma",         # 10
        "Mine Chief Hoffmann",    # 11
    ))

    AddCharChip((
        "chr/ch26200.itc",                   # 00
        "apl/ch50130.itc",                   # 01
        "chr/ch22700.itc",                   # 02
        "chr/ch23300.itc",                   # 03
        "chr/ch24300.itc",                   # 04
        "chr/ch23200.itc",                   # 05
        "chr/ch23202.itc",                   # 06
        "chr/ch20100.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch20102.itc",                   # 0C
        "chr/ch26302.itc",                   # 0D
        "chr/ch26202.itc",                   # 0E
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

    DeclNpc(-889,    750,     3319,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-889,    949,     2640,    90,   341,  0x0, 0,   6,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-6530,   750,     59,      270,  261,  0x0, 0,   7,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(860,     949,     5179,    180,  469,  0x0, 0,   12,  0,   255, 255, 0,   6,   255,  0)
    DeclNpc(153559,  0,       3329,    135,  389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(154710,  300,     2500,    315,  471,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(150729,  250,     100,     270,  469,  0x0, 0,   14,  0,   255, 255, 0,   8,   255,  0)
    DeclNpc(147369,  0,       4179,    333,  261,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(96099,   0,       4219,    0,    261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(49209,   0,       4369,    0,    261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(97459,   150,     -1169,   0,    469,  0x0, 0,   13,  0,   255, 255, 0,   13,  255,  0)

    ScpFunction((
        "Function_0_288",          # 00, 0
        "Function_1_340",          # 01, 1
        "Function_2_5D6",          # 02, 2
        "Function_3_615",          # 03, 3
        "Function_4_7BF",          # 04, 4
        "Function_5_15CC",         # 05, 5
        "Function_6_219F",         # 06, 6
        "Function_7_267A",         # 07, 7
        "Function_8_2CAB",         # 08, 8
        "Function_9_3252",         # 09, 9
        "Function_10_4056",        # 0A, 10
        "Function_11_5000",        # 0B, 11
        "Function_12_51BC",        # 0C, 12
        "Function_13_622A",        # 0D, 13
        "Function_14_6812",        # 0E, 14
        "Function_15_8251",        # 0F, 15
        "Function_16_9549",        # 10, 16
        "Function_17_A123",        # 11, 17
    ))


    def Function_0_288(): pass

    label("Function_0_288")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2C8"),
        (1, "loc_2D4"),
        (2, "loc_2E0"),
        (3, "loc_2EC"),
        (4, "loc_2F8"),
        (5, "loc_304"),
        (6, "loc_310"),
        (SWITCH_DEFAULT, "loc_31C"),
    )


    label("loc_2C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_2D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_2E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_2EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_2F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_304")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_310")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_31C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_328")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_33F")

    Return()

    # Function_0_288 end

    def Function_1_340(): pass

    label("Function_1_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_35D")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_566")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_370")
    SetChrFlags(0x9, 0x80)
    Jump("loc_566")

    label("loc_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_37E")
    Jump("loc_566")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_38C")
    Jump("loc_566")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A4")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_566")

    label("loc_3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_414")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40F")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3F9")
    SetChrPos(0x8, -1010, 750, -630, 180)
    Jump("loc_40F")

    label("loc_3F9")

    SetChrPos(0x8, -1010, 750, -630, 0)
    SetChrFlags(0x8, 0x10)

    label("loc_40F")

    Jump("loc_566")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_484")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_469")
    SetChrPos(0x8, -1010, 750, -630, 180)
    Jump("loc_47F")

    label("loc_469")

    SetChrPos(0x8, -1010, 750, -630, 0)
    SetChrFlags(0x8, 0x10)

    label("loc_47F")

    Jump("loc_566")

    label("loc_484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4F4")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_4D9")
    SetChrPos(0x8, -1010, 750, -630, 180)
    Jump("loc_4EF")

    label("loc_4D9")

    SetChrPos(0x8, -1010, 750, -630, 0)
    SetChrFlags(0x8, 0x10)

    label("loc_4EF")

    Jump("loc_566")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_50C")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_566")

    label("loc_50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_51A")
    Jump("loc_566")

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_528")
    Jump("loc_566")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_536")
    Jump("loc_566")

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_549")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_566")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_561")
    ClearChrFlags(0xC, 0x80)

    label("loc_561")

    ClearChrFlags(0xD, 0x80)

    label("loc_566")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_594")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_5BD")

    label("loc_594")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_5BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D5")
    Event(0, 17)

    label("loc_5D5")

    Return()

    # Function_1_340 end

    def Function_2_5D6(): pass

    label("Function_2_5D6")

    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FD")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_614")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_614")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_614")

    Return()

    # Function_2_5D6 end

    def Function_3_615(): pass

    label("Function_3_615")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C0")

    ChrTalk(
        0x8,
        (
            "You did well taking care of those monsters\x01",
            "in that abandoned shaft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems I'm once again in your debt.\x01",
            "Until we meet again, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB")

    label("loc_6C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B8")

    ChrTalk(
        0x8,
        (
            "To get inside of the abandoned mine, you gotta go\x01",
            "all the way to the door in the back and use the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I really appreciate you all agreeing to take\x01",
            "care of the monsters hiding in there. Just\x01",
            "stay safe now, you hear?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB")

    label("loc_7B8")

    Call(0, 16)

    label("loc_7BB")

    TalkEnd(0xFE)
    Return()

    # Function_3_615 end

    def Function_4_7BF(): pass

    label("Function_4_7BF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_853")
    Jump("loc_89D")

    label("loc_853")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_873")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89D")

    label("loc_873")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_893")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89D")

    label("loc_893")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_89D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8D0")
    Jump("loc_15C4")

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_95E")

    ChrTalk(
        0xFE,
        "I'll leave this entire situation with Gantz to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you figure anything out, please do not\x01",
            "hesitate to contact me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C4")

    label("loc_95E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A3E")
    SetChrSubChip(0x9, 0x1)

    ChrTalk(
        0xFE,
        "Gantz has been missing for two weeks now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that he hasn't gotten caught up\x01",
            "in anything dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but with that gambling addiction of his,\x01",
            "I can't help but expect the worst.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Jump("loc_15C4")

    label("loc_A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC0")

    ChrTalk(
        0xFE,
        (
            "Yesterday, there was an Erebonian merchant named\x01",
            "Felicia who came to negotiate a deal for\x01",
            "some of our septium crystals...again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's been coming to me to talk about it\x01",
            "more times than I can count now. I finally\x01",
            "gave in to her persistence and sold her some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With that relentless nature, it's no surprise\x01",
            "she's the daughter of a successful one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C59")

    label("loc_BC0")


    ChrTalk(
        0xFE,
        (
            "Felicia seems to be quite the\x01",
            "interesting merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With that relentless nature, it's no surprise\x01",
            "she's the daughter of a successful merchant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C59")

    Jump("loc_15C4")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D29")

    ChrTalk(
        0xFE,
        (
            "Tonight, Felicia intends to come negotiate\x01",
            "a deal for a bit of our septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She has spunk, I'll admit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Depending on how our talk goes,\x01",
            "I might actually agree to her terms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C4")

    label("loc_D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_DC4")

    ChrTalk(
        0xFE,
        (
            "Mainz seems to have had its fair share\x01",
            "of tourists this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to make sure to warn everyone\x01",
            "not to enter the mine later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C4")

    label("loc_DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE6")

    ChrTalk(
        0xFE,
        (
            "In honor of the opening day of the Anniversary\x01",
            "Festival, we held a grand party last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho. You should have seen those youngsters\x01",
            "in the mining crew dig into that feast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone looked like they had a great time,\x01",
            "so I think it was a success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FAB")

    label("loc_EE6")


    ChrTalk(
        0xFE,
        (
            "Many of the younger miners went over\x01",
            "to Crossbell City to enjoy the festivities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure they've built up a lot of stress. I do\x01",
            "hope they can take the chance to relax and\x01",
            "have some fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAB")

    Jump("loc_15C4")

    label("loc_FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_11CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1106")

    ChrTalk(
        0xFE,
        (
            "There's been a merchant doing business\x01",
            "in town as of late... Felicia, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I appreciate her aggressive nature and mindset,\x01",
            "but I still think she has quite a ways to go if she\x01",
            "wants to make it as a merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears she's set her sights on our\x01",
            "septium crystals... Hmm, what to do,\x01",
            "what to do...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11C6")

    label("loc_1106")


    ChrTalk(
        0xFE,
        (
            "Felicia seems determined to stay in\x01",
            "Mainz as long as it takes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She may look young, but it is clear that\x01",
            "she has plenty of mira. I expected no\x01",
            "less from a self-proclaimed merchant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C6")

    Jump("loc_15C4")

    label("loc_11CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_13D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1310")

    ChrTalk(
        0xFE,
        (
            "The Special Support Section really helped\x01",
            "us out in that unfortunate incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think that those strings of monster attacks\x01",
            "were coordinated by a group of people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We were nearly ensnared by\x01",
            "the mafia's clever trap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, thank you for your help in this\x01",
            "crazy situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13CF")

    label("loc_1310")


    ChrTalk(
        0xFE,
        (
            "It shouldn't be long before we regain what\x01",
            "we lost from delaying our excavation plans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My heart goes out to the mining crew, but I\x01",
            "need them to work hard for a little while longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CF")

    Jump("loc_15C4")

    label("loc_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_13E2")
    Jump("loc_15C4")

    label("loc_13E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_15BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1533")

    ChrTalk(
        0xFE,
        (
            "We can't rely on the Crossbell Guardian Force\x01",
            "and I can't, in good conscience, plead the guild\x01",
            "for protection...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And it should be obvious that I'm hesitant to involve\x01",
            "myself and the town with those mobsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if you all are confident you can solve\x01",
            "this mess, then I'll put my trust in you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15B6")

    label("loc_1533")


    ChrTalk(
        0xFE,
        (
            "The Special Support Section, right? That\x01",
            "name doesn't ring any bells...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Still, I'll trust you four to resolve this mess.\x02",
    )

    CloseMessageWindow()

    label("loc_15B6")

    Jump("loc_15C4")

    label("loc_15BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_15C4")

    label("loc_15C4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_7BF end

    def Function_5_15CC(): pass

    label("Function_5_15CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_162D")

    ChrTalk(
        0xFE,
        "You all saved the town.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "From the bottom of my heart, thank you.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_162D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16D1")

    ChrTalk(
        0xFE,
        (
            "Excavation work went on in the\x01",
            "abandoned mine for quite a few years.\x01",
            "It goes down pretty far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, everyone. Try not to get hurt.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_16DF")
    Jump("loc_219B")

    label("loc_16DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1834")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AA")

    ChrTalk(
        0xFE,
        (
            "Bickson went all the way to Crossbell\x01",
            "City so he could see Gantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...From what I've heard, Gantz has been\x01",
            "acting very unusual, even for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just what happened?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_182F")

    label("loc_17AA")


    ChrTalk(
        0xFE,
        (
            "No matter. I'm just relieved to hear Gantz\x01",
            "is alive and well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The townsfolk were rather relieved\x01",
            "when they heard the news.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182F")

    Jump("loc_219B")

    label("loc_1834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_18DD")

    ChrTalk(
        0xFE,
        (
            "I don't know what happened to him, but\x01",
            "please, find him as soon as you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know that the entire mining crew is\x01",
            "extremely worried about him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219B")

    label("loc_18DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_18EB")
    Jump("loc_219B")

    label("loc_18EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A27")

    ChrTalk(
        0xFE,
        (
            "I'll admit, I flinched a little bit\x01",
            "when I heard Miss Felicia was\x01",
            "from the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, she ended up being an extraordinarily\x01",
            "kind and gentle girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was expecting her to be like those snotty\x01",
            "Imperial soldiers, but I was wrong. Maybe\x01",
            "Erebonians aren't all bad, after all...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AF5")

    label("loc_1A27")


    ChrTalk(
        0xFE,
        (
            "I was expecting her to be like those snotty\x01",
            "Imperial soldiers, but I was wrong. Maybe\x01",
            "I have the wrong image of Erebonians...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In retrospect, it's embarrassing of me\x01",
            "to have judged her so quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF5")

    Jump("loc_219B")

    label("loc_1AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1BA2")

    ChrTalk(
        0xFE,
        (
            "Just so you know, my husband is rooting\x01",
            "for the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think he has a soft spot for hardworking\x01",
            "youngsters like yourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219B")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C1E")

    ChrTalk(
        0xFE,
        "We've never had this many tourists before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure it's because of Crossbell turning\x01",
            "70 this year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219B")

    label("loc_1C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D0D")

    ChrTalk(
        0xFE,
        (
            "I should cut my husband a little slack. I'm sure\x01",
            "he has just as much trouble working on the\x01",
            "excavation plans as the miners do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it is the Anniversary Festival, so it shouldn't\x01",
            "hurt to flatter him a little bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219B")

    label("loc_1D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE6")

    ChrTalk(
        0xFE,
        (
            "Due to Mainz's location, we haven't had the\x01",
            "luxury of having many ingredients on hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's always very tiring to have to take\x01",
            "the orbal bus every time we need to go shopping,\x01",
            "but it looks like that might not be a problem soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A trader from Crossbell City named Harold\x01",
            "Hayworth occasionally visits to sell us produce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having access to crops like that has\x01",
            "been a lifesaver. Not to mention that\x01",
            "it's all from Armorica Village!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F74")

    label("loc_1EE6")


    ChrTalk(
        0xFE,
        (
            "Mr. Hayworth seems to have a strong grasp\x01",
            "on how supply and demand works in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's a reliable man and an admirable\x01",
            "trader.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F74")

    Jump("loc_219B")

    label("loc_1F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2045")

    ChrTalk(
        0xFE,
        (
            "My husband works on the excavation\x01",
            "plans with Mine Chief Hoffmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They have to do this every day so that\x01",
            "Mainz doesn't surpass the septium quota\x01",
            "mandated by the state government.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219B")

    label("loc_2045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_2053")
    Jump("loc_219B")

    label("loc_2053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2192")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2159")

    ChrTalk(
        0xFE,
        (
            "I can't bring myself to trust those men\x01",
            "in black from before, no matter how\x01",
            "hard I may try to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They went out of their way to make a\x01",
            "deal with us, right after the CGF left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where exactly did their confidence\x01",
            "come from?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_218D")

    label("loc_2159")


    ChrTalk(
        0xFE,
        (
            "What in the world could those men\x01",
            "be plotting?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218D")

    Jump("loc_219B")

    label("loc_2192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_219B")

    label("loc_219B")

    TalkEnd(0xFE)
    Return()

    # Function_5_15CC end

    def Function_6_219F(): pass

    label("Function_6_219F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2233")
    Jump("loc_227D")

    label("loc_2233")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2253")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_227D")

    label("loc_2253")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2273")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_227D")

    label("loc_2273")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_227D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_24C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2463")

    ChrTalk(
        0xFE,
        (
            "My husband told me about Gantz\x01",
            "over the phone. Apparently, he\x01",
            "disappeared this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, what should I do...? I don't know\x01",
            "how the townsfolk would handle it if\x01",
            "I told them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now all I can do is pray\x01",
            "to the Goddess that Gantz comes back\x01",
            "safe and sound.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_245B")

    ChrTalk(
        0x10A,
        (
            "#0600FWe really don't have any time to lose.\x01",
            "Let's head back to the city and search\x01",
            "Revache's hideout while we still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_245B")

    SetScenarioFlags(0x0, 1)
    Jump("loc_24C2")

    label("loc_2463")


    ChrTalk(
        0xFE,
        (
            "Oh, our beloved Goddess Aidios...\x01",
            "Please, I beg you to let Gantz come\x01",
            "back home safely...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C2")

    Jump("loc_2672")

    label("loc_24C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_24D5")
    Jump("loc_2672")

    label("loc_24D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_24E3")
    Jump("loc_2672")

    label("loc_24E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_24F1")
    Jump("loc_2672")

    label("loc_24F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_25F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2595")
    SetChrSubChip(0xB, 0x2)

    ChrTalk(
        0xFE,
        "You're right. We need to be proactive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If he's gotten wrapped up in something\x01",
            "dangerous, we're in a race against time.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x0, 1)
    Jump("loc_25F4")

    label("loc_2595")


    ChrTalk(
        0xFE,
        (
            "Oh, you all... Thank you for all your help\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, enjoy your stay in Mainz.\x02",
    )

    CloseMessageWindow()

    label("loc_25F4")

    Jump("loc_2672")

    label("loc_25F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2607")
    Jump("loc_2672")

    label("loc_2607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2615")
    Jump("loc_2672")

    label("loc_2615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2623")
    Jump("loc_2672")

    label("loc_2623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2631")
    Jump("loc_2672")

    label("loc_2631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_263F")
    Jump("loc_2672")

    label("loc_263F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_264D")
    Jump("loc_2672")

    label("loc_264D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_265B")
    Jump("loc_2672")

    label("loc_265B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2669")
    Jump("loc_2672")

    label("loc_2669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2672")

    label("loc_2672")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_219F end

    def Function_7_267A(): pass

    label("Function_7_267A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_268B")
    Jump("loc_2CA7")

    label("loc_268B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2699")
    Jump("loc_2CA7")

    label("loc_2699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_26A7")
    Jump("loc_2CA7")

    label("loc_26A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_26B5")
    Jump("loc_2CA7")

    label("loc_26B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_26C3")
    Jump("loc_2CA7")

    label("loc_26C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26D1")
    Jump("loc_2CA7")

    label("loc_26D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_26DF")
    Jump("loc_2CA7")

    label("loc_26DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_26ED")
    Jump("loc_2CA7")

    label("loc_26ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26FB")
    Jump("loc_2CA7")

    label("loc_26FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2709")
    Jump("loc_2CA7")

    label("loc_2709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2717")
    Jump("loc_2CA7")

    label("loc_2717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_2725")
    Jump("loc_2CA7")

    label("loc_2725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_286D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_280B")

    ChrTalk(
        0xFE,
        (
            "*sigh* Everyone's probably packing\x01",
            "up about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it. Why did I have to be\x01",
            "attacked by a stupid monster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll be a challenge just holding a pickaxe\x01",
            "by the time I get out of this bed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2868")

    label("loc_280B")


    ChrTalk(
        0xFE,
        (
            "*sigh* It'll be a challenge just holding\x01",
            "a pickaxe by the time I get out\x01",
            "of this bed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2868")

    Jump("loc_2CA7")

    label("loc_286D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_END)), "loc_2A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288F")
    SetScenarioFlags(0x67, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_288F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298D")

    ChrTalk(
        0xFE,
        (
            "I'm supposed to help Marlow learn\x01",
            "the ropes, but I can't really do much\x01",
            "with the sorry state I'm in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All of this is that damn mutt's fault...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time it shows up, I'm gonna beat it\x01",
            "silly with the dull end of my shovel.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A40")

    label("loc_298D")


    ChrTalk(
        0xFE,
        (
            "That damn wolf bit me real good.\x01",
            "I can't even afford to go to work\x01",
            "with the state I'm in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time it shows up, I'm gonna beat it\x01",
            "silly with the dull end of my shovel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A40")

    Jump("loc_2CA7")

    label("loc_2A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A67")
    SetScenarioFlags(0x67, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A67")

    TurnDirection(0xC, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BBE")

    ChrTalk(
        0xC,
        "Max, how are you holding up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I heard your leg got bit by a monster...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, that happened. The wound isn't\x01",
            "anything to worry about, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Chief told me not to come to\x01",
            "work until I've recovered, sad\x01",
            "to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "O-Oh, I see... Well, I guess it's\x01",
            "wise to not push yourself before\x01",
            "you've recovered.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CA7")

    label("loc_2BBE")


    ChrTalk(
        0xD,
        (
            "Bah! This is pathetic. A scrape like\x01",
            "this is nothing. Why are they making\x01",
            "me stay here while everyone else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hey, I think some rest will do you good.\x01",
            "If you move around on it too much, it\x01",
            "might not heal correctly, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA7")

    TalkEnd(0xFE)
    Return()

    # Function_7_267A end

    def Function_8_2CAB(): pass

    label("Function_8_2CAB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D3F")
    Jump("loc_2D89")

    label("loc_2D3F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D5F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D89")

    label("loc_2D5F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D7F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D89")

    label("loc_2D7F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D89")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2F4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EAA")

    ChrTalk(
        0xFE,
        "Today marks the end of the Anniversary Festival...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Think I might invite the mine chief and Mayor Bickson\x01",
            "to come down to Der Ziegel and toss back a few drinks\x01",
            "with me. Could probably get Logy, too, while I'm at it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F47")

    label("loc_2EAA")


    ChrTalk(
        0xFE,
        (
            "Might as well get everyone down to\x01",
            "Der Ziegel tonight for a drinking party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like paying the mayor back for\x01",
            "treating us to drinks last time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F47")

    Jump("loc_324A")

    label("loc_2F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2FFF")

    ChrTalk(
        0xFE,
        (
            "You know, having a family really\x01",
            "is the best thing in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm able to work my hardest in the\x01",
            "mine because my wife is always\x01",
            "lending me her support.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_324A")

    label("loc_2FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_31D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3121")

    ChrTalk(
        0xFE,
        (
            "Even if it's pretty physically taxing,\x01",
            "I've always liked my job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mine chief drafts excavation plans\x01",
            "every day, and it's up to the muscle to\x01",
            "make it all happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never been too good at using my noggin,\x01",
            "so it's really the perfect job for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31CF")

    label("loc_3121")


    ChrTalk(
        0xFE,
        (
            "In this field, as long as you have the\x01",
            "strength, the rest will work itself out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never been too good at using my noggin,\x01",
            "so it's really the perfect job for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CF")

    Jump("loc_324A")

    label("loc_31D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_324A")

    ChrTalk(
        0xFE,
        "Last night was an absolute blast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got so wasted, I can't even remember\x01",
            "how many drinks I downed!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_324A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_2CAB end

    def Function_9_3252(): pass

    label("Function_9_3252")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_331E")

    ChrTalk(
        0xFE,
        (
            "Max has been working harder than\x01",
            "usual, as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm happy to see that he's motivated\x01",
            "about his job. I hope he works as hard as\x01",
            "he can, as long as he doesn't get hurt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4052")

    label("loc_331E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_33DA")

    ChrTalk(
        0xFE,
        (
            "There was some sort of bell\x01",
            "sound coming from the ruins\x01",
            "over the last few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like it just disappeared yesterday,\x01",
            "though. I wonder what it was, exactly?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4052")

    label("loc_33DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_348C")

    ChrTalk(
        0xFE,
        (
            "If I have the time right, the miners should\x01",
            "be heading home right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I imagine they want to soothe their aching\x01",
            "bones and get ready for tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4052")

    label("loc_348C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3535")

    ChrTalk(
        0xFE,
        (
            "My husband has been telling me all about\x01",
            "how hard Logy's been working lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could it be? Has Logy finally learned what\x01",
            "it takes to be a miner?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4052")

    label("loc_3535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3617")

    ChrTalk(
        0xFE,
        (
            "My husband is working hard in\x01",
            "the mine today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mining isn't just important for Mainz.\x01",
            "It's crucial to the prosperity of\x01",
            "Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but feel proud of Max\x01",
            "whenever I think of that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4052")

    label("loc_3617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_36CB")

    ChrTalk(
        0xFE,
        (
            "After resting for so long,\x01",
            "Max will finally be able to go back\x01",
            "to work tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to put my heart and soul into\x01",
            "tomorrow's lunchbox. He earned it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4052")

    label("loc_36CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_37A2")

    ChrTalk(
        0xFE,
        (
            "I'm happy that Max is taking the time to\x01",
            "rest and recover from his injury. I was\x01",
            "dreadfully worried when it happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see... Maybe I'll brew some tea\x01",
            "for the two of us so we can relax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4052")

    label("loc_37A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_389C")

    ChrTalk(
        0xFE,
        (
            "My husband is known for being one of the\x01",
            "hardest working miners despite being so young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He can still be a bit rash sometimes and isn't a\x01",
            "stranger to getting hurt on the job. I think that's\x01",
            "part of what makes him cute, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4052")

    label("loc_389C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_395A")

    ChrTalk(
        0xFE,
        (
            "Since it's the Anniversary Festival,\x01",
            "I don't mind that much if Max drinks,\x01",
            "but I wish he'd show a little restraint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just want to make sure he stays in good health.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4052")

    label("loc_395A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3B6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA8")

    ChrTalk(
        0xFE,
        (
            "I always wake up early every morning\x01",
            "so I can start making my husband's lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure he gets pretty hungry with how demanding\x01",
            "his job can get, so I always make sure to fill his\x01",
            "lunchbox as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing makes me happier than when\x01",
            "he comes home and doesn't have a single leftover.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B65")

    label("loc_3AA8")


    ChrTalk(
        0xFE,
        (
            "My morning routine consists of waking\x01",
            "up and cramming together a lunchbox\x01",
            "that Max will love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing makes me happier than when\x01",
            "he comes home and doesn't have a single leftover.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B65")

    Jump("loc_4052")

    label("loc_3B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C40")

    ChrTalk(
        0xFE,
        (
            "Max has fully recovered from the injury\x01",
            "that monster gave him, at long last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's definitely enthusiastic about it.\x01",
            "'I have to make up for all the lost\x01",
            "time, dear!' he told me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CBF")

    label("loc_3C40")


    ChrTalk(
        0xFE,
        (
            "Max has finally recovered from the injury\x01",
            "that monster gave him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He left for the mine with a giant\x01",
            "grin on his face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBF")

    Jump("loc_4052")

    label("loc_3CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_3CD2")
    Jump("loc_4052")

    label("loc_3CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_3EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DA8")

    ChrTalk(
        0xFE,
        (
            "Just be quiet, dear. A big, strong man like\x01",
            "you shouldn't be complaining this much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can't do anything about your\x01",
            "circumstances, so it's best if you\x01",
            "shush and go to sleep!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E9C")

    label("loc_3DA8")


    ChrTalk(
        0xFE,
        (
            "A big, strong man complaining and grumbling\x01",
            "like this...? I can see his poor masculinity fading\x01",
            "away before my very eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Listen, dear. You still have to take it\x01",
            "easy, even for a little injury like that.\x01",
            "Now be quiet and go to sleep!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E9C")

    Jump("loc_4052")

    label("loc_3EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EC3")
    SetScenarioFlags(0x67, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA8")

    ChrTalk(
        0xFE,
        (
            "My husband was recently\x01",
            "attacked by a monster on his way\x01",
            "home from work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm just glad his wound isn't too serious.\x01",
            "If I were him, I'd be thinking, 'I'm so lucky\x01",
            "to get a few days off from work! ☆'\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4052")

    label("loc_3FA8")


    ChrTalk(
        0xFE,
        (
            "Anyone would have gotten hurt if they\x01",
            "were ambushed while it was dark out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I were him, I'd be thinking, 'I'm so lucky\x01",
            "to get a few days off from work! ☆'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4052")

    TalkEnd(0xFE)
    Return()

    # Function_9_3252 end

    def Function_10_4056(): pass

    label("Function_10_4056")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_413C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4075")
    Call(0, 11)
    Jump("loc_4137")

    label("loc_4075")


    ChrTalk(
        0xFE,
        (
            "It looked like the mayor's wife had something\x01",
            "important to talk about with my husband last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Judging by the grave expression he had\x01",
            "afterwards, it couldn't have been good news...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4137")

    Jump("loc_4FFC")

    label("loc_413C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4219")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4158")
    Call(0, 11)
    Jump("loc_4214")

    label("loc_4158")


    ChrTalk(
        0xFE,
        (
            "Phew, thank goodness...\x01",
            "They finally found Gantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've heard the rumors about ghosts\x01",
            "haunting the ruins, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought he might have been spirited\x01",
            "away or something...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4214")

    Jump("loc_4FFC")

    label("loc_4219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_42C6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4235")
    Call(0, 11)
    Jump("loc_42C1")

    label("loc_4235")


    ChrTalk(
        0xFE,
        (
            "The mining crew carries the weight of\x01",
            "the town on their shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why Mayor Bickson makes sure\x01",
            "to always treat them well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42C1")

    Jump("loc_4FFC")

    label("loc_42C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4381")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E2")
    Call(0, 11)
    Jump("loc_437C")

    label("loc_42E2")


    ChrTalk(
        0xFE,
        (
            "I was just out delivering my husband's\x01",
            "lunchbox to him earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The way his face lights up when he sees\x01",
            "his food always puts me in a good mood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_437C")

    Jump("loc_4FFC")

    label("loc_4381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_442C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_439D")
    Call(0, 11)
    Jump("loc_4427")

    label("loc_439D")


    ChrTalk(
        0xFE,
        "I wonder how Hoffman is doing today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna be pretty busy till noon,\x01",
            "so I'll have to remember to bring\x01",
            "him his lunch later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4427")

    Jump("loc_4FFC")

    label("loc_442C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_460F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4576")

    ChrTalk(
        0xFE,
        (
            "Alec is starting to realize the miners aren't\x01",
            "just doing their jobs 'cause it's fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish he would think about working\x01",
            "somewhere safer instead of being all gung-ho\x01",
            "about something as dangerous as mining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's enough having to worry about my\x01",
            "husband coming home safely, but my\x01",
            "son, too?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_460A")

    label("loc_4576")


    ChrTalk(
        0xFE,
        (
            "All I want is for my son to find a safe,\x01",
            "stable career.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's enough having to worry about my\x01",
            "husband coming home safely, but my\x01",
            "son, too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460A")

    Jump("loc_4FFC")

    label("loc_460F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4687")

    ChrTalk(
        0xFE,
        (
            "I noticed that Alec seems to be down\x01",
            "in the dumps since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did something happen to him?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FFC")

    label("loc_4687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_47B6")

    ChrTalk(
        0xFE,
        (
            "My husband's position as mine chief puts him in\x01",
            "charge of the entire mining crew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alec said his father is what\x01",
            "inspired him to want to be\x01",
            "a miner someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm happy that he looks up to his father.\x01",
            "On the other hand, mining is a dangerous\x01",
            "profession. I can't help but worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FFC")

    label("loc_47B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_487F")

    ChrTalk(
        0xFE,
        (
            "If you took a good look at Hoffmann today,\x01",
            "you never would have guessed that he was\x01",
            "completely drunk last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband can be quite the heavyweight,\x01",
            "if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FFC")

    label("loc_487F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F9")

    ChrTalk(
        0xFE,
        (
            "Yesterday, Alec came home with\x01",
            "scratches all over him... What am\x01",
            "I going to do with that boy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They weren't anything major, but if he keeps on\x01",
            "goofing around without paying attention to his\x01",
            "surroundings, he'll go headfirst off a cliff someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Boys will be boys... I only wish they would\x01",
            "think about how much I have to worry\x01",
            "about them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4AB0")

    label("loc_49F9")


    ChrTalk(
        0xFE,
        (
            "The only reason he's covered in scratches\x01",
            "is because he doesn't pay attention to where\x01",
            "he's going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I only wish Hoffmann and Alec would\x01",
            "consider how much they make me worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AB0")

    Jump("loc_4FFC")

    label("loc_4AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4C65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE0")

    ChrTalk(
        0xFE,
        (
            "My son Alec was running like crazy\x01",
            "around town earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do wish he would be careful. It's not very\x01",
            "safe with all the heavy-duty equipment lying\x01",
            "around town...and there's cliffs, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If he isn't careful, he's going to drag himself\x01",
            "home half dead one day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4C60")

    label("loc_4BE0")


    ChrTalk(
        0xFE,
        (
            "Alec should exercise caution for once\x01",
            "in his life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If he doesn't, he's going to end up\x01",
            "hurting himself badly someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C60")

    Jump("loc_4FFC")

    label("loc_4C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_4C73")
    Jump("loc_4FFC")

    label("loc_4C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_4E48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DB4")

    ChrTalk(
        0xFE,
        (
            "For years now, septium mines haven't\x01",
            "been known as the safest workplace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Monsters are known to be attracted to\x01",
            "the septium in there and try to make nests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've gotten safer nowadays thanks to\x01",
            "the orbal lamps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I still get uneasy whenever my husband\x01",
            "heads off to work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E43")

    label("loc_4DB4")


    ChrTalk(
        0xFE,
        (
            "It's starting to get dark... I better find Alec\x01",
            "and drag him back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want what happened to Max end\x01",
            "up happening to him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E43")

    Jump("loc_4FFC")

    label("loc_4E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4FFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E6A")
    SetScenarioFlags(0x67, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F76")

    ChrTalk(
        0xFE,
        (
            "*sigh* Children can't seem to get enough\x01",
            "of sneaking into places they shouldn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really hope Alec didn't sneak into the mine\x01",
            "again and cause everyone trouble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all the monster attacks recently,\x01",
            "I wish he would be more careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4FFC")

    label("loc_4F76")


    ChrTalk(
        0xFE,
        (
            "Alec LOVES to find dangerous places\x01",
            "to explore, and it's quite the pain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why do boys always seem to\x01",
            "love finding trouble?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FFC")

    TalkEnd(0xFE)
    Return()

    # Function_10_4056 end

    def Function_11_5000(): pass

    label("Function_11_5000")


    ChrTalk(
        0xFE,
        (
            "The mines have gotten a lot busier\x01",
            "again. I hope Hoffman doesn't end\x01",
            "up working himself silly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm sure he'll be fine as long\x01",
            "as he keeps eating my handmade\x01",
            "lunches I pour my heart into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You all look like you're busy, too.\x01",
            "While you're here, how about learning\x01",
            "how to make my specialty lunchbox?\x02",
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
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B8),
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
            scpstr(SCPSTR_CODE_ITEM, 0x1B8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xE)
    Return()

    # Function_11_5000 end

    def Function_12_51BC(): pass

    label("Function_12_51BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_52E6")

    ChrTalk(
        0xFE,
        (
            "Logy's always been prone to slacking off any way\x01",
            "he can, so imagine my surprise when I hear he's\x01",
            "been taking his work seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was worried he didn't like going into work, but it\x01",
            "seems he's come around. Perhaps he's putting his\x01",
            "best foot forward as the older sibling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6226")

    label("loc_52E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_53C6")

    ChrTalk(
        0xFE,
        (
            "Honestly, I'm worried Logy is just going to go\x01",
            "right back to goofing off once Gantz comes back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that he's actually taking his job seriously, I would\x01",
            "prefer it if he took this experience to heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6226")

    label("loc_53C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_5475")

    ChrTalk(
        0xFE,
        (
            "Logy and Amy should be getting back\x01",
            "any minute now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll have to prepare a special dinner tonight,\x01",
            "since Logy's been working so hard recently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6226")

    label("loc_5475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_552D")

    ChrTalk(
        0xFE,
        (
            "Amazingly, Logy has actually been\x01",
            "taking his job seriously for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm convinced that he's only able to focus\x01",
            "because that Gantz isn't there to distract him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6226")

    label("loc_552D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_561A")

    ChrTalk(
        0xFE,
        (
            "Are you aware that there are some old ruins near\x01",
            "the cliffs southwest of Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That place has been around ever since I was young.\x01",
            "No one knows anything about it except that it's the\x01",
            "remains of an ancient temple.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6226")

    label("loc_561A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5706")

    ChrTalk(
        0xFE,
        (
            "Logy's nasty habit of slacking off never fails\x01",
            "to make me worry for that boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't matter to me whether he stays a\x01",
            "miner or not. I just want to see him be\x01",
            "passionate about something for once in his life...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6226")

    label("loc_5706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5799")

    ChrTalk(
        0xFE,
        (
            "My granddaughter Amy has been\x01",
            "trying to chat up any men that\x01",
            "come into Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She'll never get tired of that,\x01",
            "will she...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6226")

    label("loc_5799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_58BD")

    ChrTalk(
        0xFE,
        (
            "In the seventy years since Crossbell State was\x01",
            "founded, the Empire and Republic's bickering\x01",
            "has caused a lot of trouble for Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's calmed down somewhat, thanks\x01",
            "to the Non-Aggression Pact, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...not many people in Mainz legitimately\x01",
            "trust the government.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6226")

    label("loc_58BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5A58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59DE")

    ChrTalk(
        0xFE,
        (
            "My grandson thought it would be a good idea\x01",
            "to go to a drinking party last night, even though\x01",
            "he is a lightweight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And sure enough, he wasn't able to\x01",
            "drag himself home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I guess I'll walk on over to the\x01",
            "bar later and check out the damage.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A53")

    label("loc_59DE")


    ChrTalk(
        0xFE,
        (
            "Amy calling him an introvert must\x01",
            "have really been bothering him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll go see how he's holding up later.\x02",
    )

    CloseMessageWindow()

    label("loc_5A53")

    Jump("loc_6226")

    label("loc_5A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5C12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B7F")

    ChrTalk(
        0xFE,
        (
            "Nowadays, you rarely see young\x01",
            "men willingly join the mining crew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the contrary, most youngsters in\x01",
            "Mainz claim that they're going to live\x01",
            "sophisticated lives as merchants...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While that makes me a tad bit blue,\x01",
            "I guess it's just a sign of the times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C0D")

    label("loc_5B7F")


    ChrTalk(
        0xFE,
        (
            "Most men nowadays are trading in a\x01",
            "pickaxe for a ledger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While that makes me a tad bit blue,\x01",
            "I guess it's just a sign of the times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C0D")

    Jump("loc_6226")

    label("loc_5C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5E24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D4D")

    ChrTalk(
        0xFE,
        (
            "The septium mined in Mainz is well known\x01",
            "for its abundance and magnificent quality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On top of that, septium of all seven elements\x01",
            "can be found in our mines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you don't believe me, I'll have you know\x01",
            "that foreign merchants travel to Mainz all\x01",
            "the time in order to buy it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5E1F")

    label("loc_5D4D")


    ChrTalk(
        0xFE,
        (
            "The septium mined in Mainz is well known\x01",
            "for its abundance and its magnificent quality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately, that abundance has been on a\x01",
            "slow decline...but merchants still travel\x01",
            "far and wide in order to buy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E1F")

    Jump("loc_6226")

    label("loc_5E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_5E32")
    Jump("loc_6226")

    label("loc_5E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_6010")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F95")

    ChrTalk(
        0xFE,
        (
            "I have two granchildren and they're both\x01",
            "quite a hassle to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My grandson Logy is one of the miners,\x01",
            "but he tends to slack on the job and try\x01",
            "to sneak away during his shifts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And my granddaughter Amy is obsessed\x01",
            "with finding a boyfriend for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Where did I go wrong while raising them...?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_600B")

    label("loc_5F95")


    ChrTalk(
        0xFE,
        "Both of my grandkids are such trouble makers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Logy, Amy... Where did I go wrong\x01",
            "while raising you two...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_600B")

    Jump("loc_6226")

    label("loc_6010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6032")
    SetScenarioFlags(0x67, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_617C")

    ChrTalk(
        0xFE,
        (
            "Ownership of Crossbell has long been\x01",
            "disputed between Erebonia and Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The septium produced here in Mainz has\x01",
            "been one of the leading causes of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nowadays, Crossbell's prosperity comes from\x01",
            "being Zemuria's leading trade center, but that\x01",
            "doesn't mean septium mining isn't still important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6226")

    label("loc_617C")


    ChrTalk(
        0xFE,
        (
            "Calvard and Erebonia have fought over\x01",
            "control of Crossbell for the longest time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One of the largest reasons for that is the\x01",
            "septium from this very mining town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6226")

    TalkEnd(0xFE)
    Return()

    # Function_12_51BC end

    def Function_13_622A(): pass

    label("Function_13_622A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_62BE")
    Jump("loc_6308")

    label("loc_62BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_62DE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6308")

    label("loc_62DE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62FE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6308")

    label("loc_62FE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6308")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6446")

    ChrTalk(
        0xFE,
        (
            "The abandoned part of the mine\x01",
            "has become a bit of a problem\x01",
            "for the crew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, no use in worrying about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Either way, we're far too short on hands to deal with it.\x01",
            "Once the youngsters get back, we'll\x01",
            "figure out what to do about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 1)
    Jump("loc_680A")

    label("loc_6446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_650F")

    ChrTalk(
        0xFE,
        (
            "I feel bad about causing Miranda\x01",
            "to worry all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That being said, the mining crew is the\x01",
            "pride of the town. No matter what danger\x01",
            "we may face, we can't run away from it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_680A")

    label("loc_650F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_66D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6614")

    ChrTalk(
        0xFE,
        (
            "Baeckerei, the owner of the general store,\x01",
            "used to be my senior in the mines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I owe every mining skill in my arsenal\x01",
            "thanks to his teachin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The town may have entrusted me with\x01",
            "the mine, but I'll never match up to him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_66CD")

    label("loc_6614")


    ChrTalk(
        0xFE,
        (
            "Baeckerei, the owner of the general store,\x01",
            "used to be my senior in the mines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm forever in his debt. I may have\x01",
            "become a full-fledged miner, but I'll\x01",
            "never match up to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66CD")

    Jump("loc_680A")

    label("loc_66D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_673B")

    ChrTalk(
        0xFE,
        (
            "My son told me that he wants to be\x01",
            "a miner like me, someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm a proud father.\x02",
    )

    CloseMessageWindow()
    Jump("loc_680A")

    label("loc_673B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_680A")

    ChrTalk(
        0xFE,
        (
            "Apparently, Gantz and Marlow are going\x01",
            "to stay in the city during the Anniversary\x01",
            "Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They can do whatever, but an old man\x01",
            "like myself would much rather take it easy\x01",
            "in my hometown.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_680A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_622A end

    def Function_14_6812(): pass

    label("Function_14_6812")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    OP_68(500, 2250, -9500, 0)
    MoveCamera(312, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(35500, 0)
    SetChrPos(0x101, 700, 750, -8600, 0)
    SetChrPos(0x102, -500, 750, -8600, 0)
    SetChrPos(0x103, 700, 750, -10000, 0)
    SetChrPos(0x104, -500, 750, -10000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrPos(0x8, -850, 750, 5450, 180)
    SetChrPos(0xA, -1900, 750, 5450, 180)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")
    FadeToBright(1000, 0)
    OP_68(500, 2250, -8000, 1800)

    def lambda_6952():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6952)

    def lambda_696C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_696C)
    Sleep(100)

    def lambda_6980():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6980)

    def lambda_699A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_699A)
    Sleep(50)

    def lambda_69AE():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_69AE)

    def lambda_69C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_69C8)
    Sleep(80)

    def lambda_69DC():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_69DC)

    def lambda_69F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_69F6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_0D()
    OP_6F(0x1)

    NpcTalk(
        0x8,
        "Man's Voice",
        "#1200524V#3PWhat? You're already back?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1200525V#0005F#6PExcuse us...\x02",
    )

    CloseMessageWindow()
    OP_68(500, 2250, 2500, 3000)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#1200526V#11PDidn't you hear me? I can't make\x01",
            "a decision just like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200527V#11PCome back some oth--\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#1200528V#11PHmm, what's this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1200529V#5POh, my, you aren't the people who\x01",
            "we just spoke to, are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(500, 2250, 0, 3000)

    def lambda_6C27():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C27)
    Sleep(100)

    def lambda_6C44():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C44)
    Sleep(50)

    def lambda_6C61():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C61)
    Sleep(80)

    def lambda_6C7E():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C7E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#1200530V#11PO-Oh... Pardon my rudeness.\x01",
            "I'm Bickson, Mainz's mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200531V#0000F#6PUmm, it's fine, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200532V#0100F#6PWe apologize for visiting at such\x01",
            "a stressful time for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200533V#11PW-Well, I wouldn't say I'm\x01",
            "particularly bothered by it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200534V#11PWho exactly are you folks?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x101,
        (
            "#1200535V#1POh, right. Crossbell Police Department,\x01",
            "Special Support Section.\x02\x03",
            "#1200536VWe came to ask you about the recent\x01",
            "monster attack, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1080, 2950, 3060, 0)
    MoveCamera(322, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33750, 0)
    OP_68(1080, 1950, 3060, 4000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 2450, 950, 2780, 270)
    SetChrPos(0x102, 2450, 950, 3780, 270)
    SetChrPos(0x103, 1100, 950, 1500, 0)
    SetChrPos(0x104, 1100, 950, 5100, 180)
    SetChrPos(0x8, -800, 950, 2780, 90)
    SetChrPos(0xA, -800, 950, 3780, 90)
    SetChrChipByIndex(0x8, 0x6)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xB, 0xC)
    SetChrSubChip(0xB, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#1200537V#5PAh, so that's it. You're with the city's\x01",
            "police department, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200538V#5PAt first, I thought you were bracer rookies\x01",
            "who decided to swing by Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200539V#0012F#12PYeah, we get that a lot.\x02\x03",
            "#1200540V#0001FYou see, we already asked around town,\x01",
            "trying to dig up any information we could.\x02\x03",
            "#1200541VAccording to what we heard, there hasn't\x01",
            "been just one isolated case...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200542V#5PYou heard correctly. Now, there have been\x01",
            "three separate attacks in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200543V#5PEach instance took place at night, and\x01",
            "no one was injured during the first two...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200544V#5PBut two days ago, the culprits drew blood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1200545V#11PLuckily, he only suffered minor injuries, but the\x01",
            "damage caused by the beasts is getting worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1200546V#11PAs a result, the whole town is too nervous to\x01",
            "step outside at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200547V#0003F#12PThat's worse than I thought...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200548V#0101F#2PAnd nothing came of the Guardian\x01",
            "Force's investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200549V#5PZilch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200550V#5PThose wolves, or whatever they are,\x01",
            "are too cunning for their own good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200551V#5PHowever, the CGF is still the CGF!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200552V#5PWhat do they think they are doing,\x01",
            "abandoning us after not solving a thing...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200553V#5PDoesn't that just grind your gears?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200554V#0006F#12PI understand your confusion, sir.\x01",
            "(Looks like they got a lot to worry about...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200555V#0305F#2PYou probably requested help from\x01",
            "the Bracer Guild, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200556V#5PYes, well...before the CGF arrived in Mainz,\x01",
            "we submitted a request to the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200557V#5PSad to say, the guild was too caught up in\x01",
            "something and couldn't send anyone here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200558V#5PThey wouldn't be able to protect us every\x01",
            "day, either, so we had to rely on the CGF\x01",
            "in the end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200559V#0203F#6PAnd now even the CGF has withdrawn.\x01",
            "They were not able to help much in the end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200560V#5PExactly... It's like my father used to say:\x01",
            "When it rains, it pours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200561V#5PSince I had nothing else to lose, I decided\x01",
            "I might as well ask the guild for help again,\x01",
            "but someone else knocked on my door first...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200562V#5PI'm sure you saw them before you came in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200563V#0001F#12PYou mean Revache.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200564V#0101F#2PIf you don't mind me asking, what did\x01",
            "they want to talk to you about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200565V#5PI don't mind sharing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200566V#5PWith the CGF gone, Revache has offered to\x01",
            "become the town's new bodyguards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200567V#5PThe beasts could attack at any time, they told me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1200568V#0005F#12PB-Bodyguards...? THEM?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200569V#0301F#2PInterestin'... I doubt they're doin' it outta\x01",
            "the kindness of their heart, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200570V#5PNo, they aren't. But they also weren't\x01",
            "planning on taking mira as payment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200571V#5PInstead, they wish to build a monopoly\x01",
            "on our septium operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200572V#0105F#2PA monopoly on your mine?\x02\x03",
            "#1200573V#0101FThe state government should have\x01",
            "the mining rights, shouldn't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200574V#5PYes. To ensure we don't mine too much, we\x01",
            "have to abide by government mandates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200575V#5PBecause there's an international demand for\x01",
            "septium, we can't go overboard with selling it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200576V#5PHowever, who we sell our septium to\x01",
            "is ultimately left to our discretion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200577V#0200F#6PFor them, playing bodyguard obscures the\x01",
            "real objective: controlling Mainz's septium\x01",
            "industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1200578V#5PBe that as it may, we still have partnerships\x01",
            "we've built up with merchants over the years...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1200579V#5PNo matter which way I try to look at it,\x01",
            "this whole thing is a disaster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200580V#0103F#2PI'm sorry to hear that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200581V#0306F#2PThings seem to go straight to Gehenna\x01",
            "whenever Revache is involved...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#1200582V#0003F#12PMayor Bickson, how do you feel about letting\x01",
            "us handle the attacks from here on out?\x02\x03",
            "#1200583V#0000FI think we're capable of cracking this case.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(100)
    SetChrSubChip(0x104, 0x1)

    ChrTalk(
        0x102,
        "#1200584V#0105F#2PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200585V#0205F#6PLloyd, are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200586V#5PHmm... You said you are the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200587V#5PIs it really smart to rely on the\x01",
            "police rather than the CGF or\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200588V#0004F#12PYou can trust us with this, sir.\x02\x03",
            "#1200589V#0000FIf things go according to plan, we can\x01",
            "have this solved by tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(34250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x5C, 0)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_6812 end

    def Function_15_8251(): pass

    label("Function_15_8251")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch00802.itc", 0x22)
    LoadChrToIndex("chr/ch20102.itc", 0x24)
    OP_68(600, 2450, -6850, 0)
    MoveCamera(317, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23150, 0)
    SetChrPos(0x101, -120, 750, -5500, 0)
    SetChrPos(0x102, 240, 750, -6920, 0)
    SetChrPos(0x103, 590, 750, -8250, 0)
    SetChrPos(0x104, 180, 660, -9440, 0)
    SetChrPos(0x109, -880, 750, -7550, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrPos(0x8, 970, 750, -210, 0)
    SetChrPos(0xA, -6080, 750, -320, 270)
    FadeToBright(1000, 0)
    OP_68(600, 2450, -5350, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#4100513V#0000F#6PExcuse us. It's the Special Support Section.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        "#4100514V#11PYes, yes. I've been waiting for you all.\x02",
    )

    CloseMessageWindow()
    OP_68(600, 2450, -3350, 2500)

    def lambda_83F1():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_83F1)

    def lambda_8406():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8406)

    def lambda_841B():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_841B)

    def lambda_8430():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8430)

    def lambda_8445():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8445)

    def lambda_845A():
        OP_95(0xFE, -190, 750, -830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_845A)
    TurnDirection(0xA, 0x103, 500)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#4100515V#11PApologies for making you come all this way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100516V#11PTruth be told, I intended to go\x01",
            "see you in the city, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100517V#0004F#6PPlease, don't worry about that. We were\x01",
            "in the area, so stopping by wasn't an\x01",
            "inconvenience or anything.\x02\x03",
            "#4100518V#0001FSo, would you mind explaining the\x01",
            "support request to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4100519V#11POf course. Please take a seat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4100520V#5PI'll pour some tea. Just one second.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(840, 2950, 3300, 0)
    MoveCamera(317, 20, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19000, 0)
    OP_68(840, 1950, 3300, 3000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x101, 2450, 950, 2780, 270)
    SetChrPos(0x102, 2450, 950, 3880, 270)
    SetChrPos(0x103, 1100, 950, 1500, 0)
    SetChrPos(0x104, 1450, 950, 5100, 180)
    SetChrPos(0x109, 400, 950, 5100, 180)
    SetChrPos(0x8, -800, 950, 2780, 90)
    SetChrPos(0xA, -800, 950, 3880, 90)
    SetChrChipByIndex(0x8, 0x6)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#4100521V#0003F#12PI see.\x02\x03",
            "#4100522V#0001FIn summary, one of your miners, Gantz,\x01",
            "traveled to Crossbell City almost two weeks\x01",
            "ago and hasn't been back since?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4100523V#5PYes, precisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4100524V#5PYou see, he's a gambler at heart.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100525V#5PPeople have even told me that he would\x01",
            "go to the city's Entertainment District on\x01",
            "weekends to gamble at the casino...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4100526V#11PThe fact that he hasn't contacted anyone\x01",
            "for two whole weeks has us worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4100527V#11PEveryone around town is wondering where\x01",
            "he's gone or if something happened to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100528V#0108F#12PThat's...definitely strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100529V#0208F#6PThere may be some specific reason he has not\x01",
            "returned, such as being involved in an accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100530V#0506F#11PHmm. At the very least, I hope he wasn't\x01",
            "attacked by the monsters that have started\x01",
            "to appear on the city outskirts...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#4100531V#0305F#11PWhat if the miner is just a damn good\x01",
            "gambler? A guy could make a killin' in\x01",
            "the casino, if he plays his cards right.\x02\x03",
            "#4100532V#0309FIf I were him and that happened, I'd be\x01",
            "chillin' in Mishelam with a drink in one hand\x01",
            "and the other around a pretty lady's waist.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#4100533V#0006F#12PYeah, I doubt that's the case...\x01",
            "For starters, he isn't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100534V#0202F#6PRandy makes a valid point about gambling,\x01",
            "though. We cannot ignore the possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4100535V#5PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100536V#5PI don't mean to interrupt, but I don't\x01",
            "see that happening.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4100537V#0005F#12PWhy's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100538V#0102F#12PYou said he loves to gamble. Are there any other\x01",
            "relevant qualities about him we should know of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100539V#5PHaha, well, Gantz is the least serious person\x01",
            "I've ever had the pleasure of knowing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100540V#5P...while he may love gambling to death,\x01",
            "he's absolutely horrible at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100541V#5POn top of that, he's got the luck of a man who\x01",
            "would keel over from a splinter. Every time he\x01",
            "comes home, his wallet is as dry as a desert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100542V#0012F#12PI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100543V#0303F#11PIn that case, he might make some cash in the\x01",
            "lottery, but, without any real skill, I doubt he'd\x01",
            "win much in a poker game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100544V#0211F#6PPerhaps he took out a sum of mira and ran off\x01",
            "before the loan sharks could catch him...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100545V#0106F#12PW-Well, that's another possibility to consider.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100546V#5PThat was actually one of the scenarios\x01",
            "we considered before you arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4100547V#11PWere that the case, I have no idea how\x01",
            "we'd find him...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#4100548V#0004F#12PUnderstood. Mayor Bickson, you can\x01",
            "leave finding Gantz to us.\x02\x03",
            "#4100549V#0000FFor now, we'll start with investigating the\x01",
            "casino and other places he may have visited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100550V#5PThank you, Lloyd. I'll leave this\x01",
            "matter in your hands, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100551V#5PIf you learn anything, could you contact\x01",
            "my house by phone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100552V#0000F#12POf course, sir. Let me write down\x01",
            "your phone number while I'm here...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x8, 0x5)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x24)
    OP_68(-500, 2250, -3500, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    SetChrPos(0x0, -500, 750, -3500, 180)
    SetChrPos(0x1, -500, 750, -3500, 180)
    SetChrPos(0x2, -500, 750, -3500, 180)
    SetChrPos(0x3, -500, 750, -3500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x8, -1200, 750, 600, 180)
    SetChrPos(0xA, -6530, 750, 60, 270)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xC1, 2)
    OP_29(0x4A, 0x1, 0x2)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_8251 end

    def Function_16_9549(): pass

    label("Function_16_9549")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-70, 2450, -3180, 0)
    MoveCamera(309, 28, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(29780, 0)
    SetChrPos(0x101, 0, 750, -2700, 0)
    SetChrPos(0x102, -1300, 750, -2700, 0)
    SetChrPos(0x103, 0, 0, -4000, 0)
    SetChrPos(0x104, -1300, 0, -4000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95E2")
    OP_93(0x8, 0x0, 0x0)
    Jump("loc_95E9")

    label("loc_95E2")

    OP_93(0x8, 0xB4, 0x0)

    label("loc_95E9")

    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C8F")

    ChrTalk(
        0x8,
        "#11PWhat to do...what to do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI can't send in the mine chief to exterminate\x01",
            "those monsters. That'd be an execution...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FGood afternoon, Mayor Bickson.\x02\x03",
            "Special Support Section here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11POh, you came! I was hoping\x01",
            "that you'd get here soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FYou submitted a support request, right?\x02\x03",
            "Something about monsters in the mine...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYes. We're in a bit of a pickle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PDeep in the mine, there's an abandoned area\x01",
            "that has already been fully excavated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PLast night, monsters began to rampage in\x01",
            "there, causing our mining crew problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FMonsters running amok in the mine\x01",
            "definitely doesn't sound safe.\x02\x03",
            "Does that sort of thing happen often?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FMany cases have been reported in\x01",
            "various countries that mine septium.\x02\x03",
            "#0200FThough the cause has not been explained\x01",
            "yet, monsters are naturally attracted to\x01",
            "septium crystals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0301FI've heard that before a load of times.\x01",
            "The suckers can't get enough of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FI think I remember learning about that as\x01",
            "well. No matter the country, mines always\x01",
            "face the risk of attracting monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0003FSo that's how it is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNormally, our miners are tough enough\x01",
            "to be able to drive away monsters\x01",
            "without any issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut most of the miners are in the city,\x01",
            "celebrating the Anniversary Festival.\x01",
            "We're short on manpower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe abandoned mine entrance may be locked,\x01",
            "but there's no telling how dangerous things will\x01",
            "get if left unattended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAnd if you'd accept, I would like for you folks\x01",
            "to exterminate all the monsters in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PSo, what do you think?\x02",
    )

    CloseMessageWindow()
    OP_29(0x1C, 0x1, 0x0)
    Jump("loc_9DBF")

    label("loc_9C8F")


    ChrTalk(
        0x8,
        (
            "#11PDeep in the mine, there's an abandoned area that\x01",
            "has already been fully excavated. Unfortunately,\x01",
            "monsters have started to run amok in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'd like for you to exterminate all the monsters\x01",
            "in that section of the mine before the festival\x01",
            "ends, if possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PWhat do you think?\x02",
    )

    CloseMessageWindow()

    label("loc_9DBF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9DFD"),
        (1, "loc_9FE1"),
        (SWITCH_DEFAULT, "loc_A0E3"),
    )


    label("loc_9DFD")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#6P#0000FUnderstood. We'll take care of these\x01",
            "monsters for you, no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PReally? I'm in your debt, once again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PPlease, take this with you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x346),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x346, 1)

    ChrTalk(
        0x8,
        (
            "#11PUse that key to unlock the abandoned\x01",
            "mine's gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'll be awaiting the good news.\x01",
            "Try to be careful, all right?\x02",
        )
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
            "[Mine Monster Cleanup]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x1C, 0x1, 0x1)
    SetScenarioFlags(0x1, 0)
    Jump("loc_A0F2")

    label("loc_9FE1")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#6P#0006FI'm really sorry, but we can't accept\x01",
            "this request right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe mine is safe for now, but\x01",
            "I can't ignore this for very long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you find the time, please come\x01",
            "let me know that you can do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0F2")

    label("loc_A0E3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F2")

    label("loc_A0F2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x10)
    SetChrPos(0x0, -610, 750, -2790, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_9549 end

    def Function_17_A123(): pass

    label("Function_17_A123")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-70, 2450, -3180, 0)
    MoveCamera(309, 28, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(29780, 0)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1010, 750, -630, 180)
    SetChrPos(0x101, 0, 750, -2700, 0)
    SetChrPos(0x102, -1300, 750, -2700, 0)
    SetChrPos(0x103, 0, 0, -4000, 0)
    SetChrPos(0x104, -1300, 0, -4000, 0)
    OP_4B(0x8, 0xFF)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11PSo you managed to get rid of all\x01",
            "those pesky monsters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FYes, sir. They won't be an issue anymore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FFor the time being, no further monsters\x01",
            "should try to settle in that area.\x02\x03",
            "Your remaining miners should be safe\x01",
            "to work during the festival. At least until\x01",
            "the rest of the mining crew returns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThat's music to my ears. I must\x01",
            "find some way to thank you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAh, how about this?\x02",
    )

    CloseMessageWindow()
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)
    Sound(17, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#6P#0205FThat is a LOT of sepith...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0309FWhoa, whoa, whoa! You sure you're allowed\x01",
            "to give us this mountain of sepith?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0011FY-You're pulling our leg, right?\x02\x03",
            "#0003FMayor Bickson, I'm not sure if it'd be\x01",
            "appropriate to accept a reward like this.\x01",
            "This seems more suited for bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FB-Besides, isn't sepith a valuable export\x01",
            "from your mines? We can't take so much\x01",
            "of it away from you, can we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PPlease, you're overthinking this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSepith is merely fragments of septium, you know.\x01",
            "It's the 'freebie' we get while mining septium, in\x01",
            "a manner of speaking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe government may regulate what we do\x01",
            "with septium, but they couldn't give a hoot\x01",
            "about what we do with sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHonestly, I wish I could have given\x01",
            "you more than what I did. It's always\x01",
            "nice to get sepith off my hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FI-I never thought about it like that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHaha. In a way, you all are helping\x01",
            "me by accepting this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PPlease, allow me to give this to you\x01",
            "as a token of my appreciation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#6P#0003FIf you say it's okay, we'll gladly take it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PGood man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBefore you leave, let me say thank you\x01",
            "one last time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'm happy to return the favor if you\x01",
            "ever need anything from me.\x02",
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
            "[Mine Monster Cleanup]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1C, 0x4, 0x10)
    SetScenarioFlags(0x1, 0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -610, 750, -2790, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_A123 end

    SaveToFile()

Try(main)
