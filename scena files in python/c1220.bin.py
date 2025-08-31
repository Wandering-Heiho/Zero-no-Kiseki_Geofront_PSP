from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1220.bin",                # FileName
        "c1220",                    # MapName
        "c1220",                    # Location
        0x0020,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 32, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1220",                  # 0
        "Receptionist Tria",      # 1
        "MacKennon",              # 2
        "Reins",                  # 3
        "Grace",                  # 4
        "Reporter A",             # 5
        "Reporter B",             # 6
        "Reporter C",             # 7
        "Reporter D",             # 8
    ))

    AddCharChip((
        "chr/ch26602.itc",                   # 00
        "chr/ch28100.itc",                   # 01
        "chr/ch06000.itc",                   # 02
        "chr/ch06002.itc",                   # 03
        "chr/ch26700.itc",                   # 04
    ))

    DeclNpc(5789,    0,       -430,    270,  341,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(5099,    0,       60020,   0,    261,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-519,    0,       360,     0,    261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 17,  -6.510000228881836,    5.110000133514404,     -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.255000114440918,     -2.555000066757202,    0.10000000149011612,   1.0])

    DeclActor(4100,    0,       -520,    1500,    5500,    1800,    -470,    0x007E, 0,  3,  0x0000)
    DeclActor(7270,    0,       54230,   1000,    7270,    1400,    54230,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_278",          # 00, 0
        "Function_1_330",          # 01, 1
        "Function_2_56E",          # 02, 2
        "Function_3_608",          # 03, 3
        "Function_4_72C",          # 04, 4
        "Function_5_AE5",          # 05, 5
        "Function_6_C6D",          # 06, 6
        "Function_7_2AE9",         # 07, 7
        "Function_8_4725",         # 08, 8
        "Function_9_585E",         # 09, 9
        "Function_10_6907",        # 0A, 10
        "Function_11_6A84",        # 0B, 11
        "Function_12_6DAB",        # 0C, 12
        "Function_13_93B9",        # 0D, 13
        "Function_14_95A9",        # 0E, 14
        "Function_15_AD24",        # 0F, 15
        "Function_16_B2A5",        # 10, 16
        "Function_17_B3EA",        # 11, 17
    ))


    def Function_0_278(): pass

    label("Function_0_278")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2B8"),
        (1, "loc_2C4"),
        (2, "loc_2D0"),
        (3, "loc_2DC"),
        (4, "loc_2E8"),
        (5, "loc_2F4"),
        (6, "loc_300"),
        (SWITCH_DEFAULT, "loc_30C"),
    )


    label("loc_2B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_300")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_30C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_32F")

    Return()

    # Function_0_278 end

    def Function_1_330(): pass

    label("Function_1_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_343")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_36C")
    SetChrPos(0x9, 3100, 20, -890, 90)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3AA")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 820, 0, 220, 0)
    ClearChrFlags(0xB, 0x40)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_56D")

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3B8")
    Jump("loc_56D")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3CB")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3DE")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3EC")
    Jump("loc_56D")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3FA")
    Jump("loc_56D")

    label("loc_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_40D")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_420")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_438")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x10)
    Jump("loc_56D")

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_44B")
    SetChrFlags(0xA, 0x80)
    Jump("loc_56D")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_459")
    Jump("loc_56D")

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_467")
    Jump("loc_56D")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_497")
    OP_93(0xA, 0x10E, 0x0)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x9, -2140, 0, 450, 90)
    SetChrFlags(0x9, 0x10)
    Jump("loc_56D")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4D7")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 470, 0, 56880, 180)
    Jump("loc_56D")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_502")
    OP_93(0xA, 0x10E, 0x0)
    SetChrPos(0x9, -2140, 0, 450, 90)
    SetChrFlags(0x9, 0x10)
    Jump("loc_56D")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_510")
    Jump("loc_56D")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_550")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 3580, 0, 60060, 90)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    OP_93(0x9, 0x10E, 0x0)
    Jump("loc_56D")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_568")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x10)
    Jump("loc_56D")

    label("loc_568")

    SetChrFlags(0xA, 0x80)

    label("loc_56D")

    Return()

    # Function_1_330 end

    def Function_2_56E(): pass

    label("Function_2_56E")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_590")
    OP_66(0x1, 0x1)

    label("loc_590")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A9")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_5AF")

    label("loc_5A9")

    OP_10(0x0, 0x1)
    OP_10(0x5, 0x0)

    label("loc_5AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CB")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5E2")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5E2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5E2")

    label("loc_5E2")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_5F5")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_607")
    OP_65(0x0, 0x1)

    label("loc_607")

    Return()

    # Function_2_56E end

    def Function_3_608(): pass

    label("Function_3_608")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_69C")
    Jump("loc_6E6")

    label("loc_69C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BC")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E6")

    label("loc_6BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DC")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E6")

    label("loc_6DC")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E6")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_721")
    Call(0, 4)
    Jump("loc_724")

    label("loc_721")

    Call(0, 6)

    label("loc_724")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_3_608 end

    def Function_4_72C(): pass

    label("Function_4_72C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7D6")

    ChrTalk(
        0x8,
        (
            "Fantastic job, everyone!\x01",
            "Keep up the good work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I could tell Grace was delighted, too,\x01",
            "judging from all of her hooting\x01",
            "and hollering.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D9")

    label("loc_7D6")

    Call(0, 6)

    label("loc_7D9")

    Jump("loc_AE4")

    label("loc_7DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_ACD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC8")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Talk]\x01",               # 0
            "[Submit Photos]\x01",      # 1
            "[Cancel]\x01",             # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_909")
    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8F7")

    ChrTalk(
        0x8,
        (
            "Grace was actually the driving force\x01",
            "behind the push for a tour guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All of us at the Crossbell Times appreciate\x01",
            "your assistance in this next publication.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_8F7")

    Call(0, 6)

    label("loc_8FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AC3")

    label("loc_909")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB0")
    OP_60(0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_93C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_953")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_953")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_96A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_96A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_981")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_981")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_998")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_998")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_9AF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_9C6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_9DD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_9F4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A0B")
    Call(0, 13)
    Jump("loc_AAB")

    label("loc_A0B")


    ChrTalk(
        0x101,
        (
            "#0005F(Whoops... Grace gave us a quota of\x01",
            "at least five photos.)\x02\x03",
            "#0003F(We'd better take a few more, or else\x01",
            "we'll face her wrath...)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AAB")

    Jump("loc_AC3")

    label("loc_AB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC3")
    OP_60(0x0)
    Return()

    label("loc_AC3")

    Jump("loc_7F5")

    label("loc_AC8")

    Jump("loc_AE4")

    label("loc_ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_AE1")
    Call(0, 11)
    Jump("loc_AE4")

    label("loc_AE1")

    Call(0, 6)

    label("loc_AE4")

    Return()

    # Function_4_72C end

    def Function_5_AE5(): pass

    label("Function_5_AE5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B79")
    Jump("loc_BC3")

    label("loc_B79")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B99")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BC3")

    label("loc_B99")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB9")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BC3")

    label("loc_BB9")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BC3")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    ChrTalk(
        0x8,
        "Ah, excuse me. People are hard at work here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please go to the front of the desk if you have\x01",
            "any inquiries. Thanks!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_5_AE5 end

    def Function_6_C6D(): pass

    label("Function_6_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D99")

    ChrTalk(
        0x8,
        (
            "Grace took off to sniff out her 'next big scoop,'\x01",
            "as she likes to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She dragged poor Reins with her on the way\x01",
            "out the door. I figure he's going to have to\x01",
            "follow her all over town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Grace had a serious look on her face today.\x01",
            "I imagine she came across something dire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE8")

    label("loc_D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DA7")
    Jump("loc_2AE8")

    label("loc_DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_ED2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E2A")

    ChrTalk(
        0x8,
        "Last night was absolutely dreadful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Grace's article isn't responsible for\x01",
            "this giant mess, is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECD")

    label("loc_E2A")


    ChrTalk(
        0x8,
        (
            "The Crossbell Times had to temporarily\x01",
            "suspend its publication today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We are terribly sorry for the inconvenience this\x01",
            "has brought our loyal readers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_ECD")

    Jump("loc_2AE8")

    label("loc_ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1003")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F51")

    ChrTalk(
        0x8,
        (
            "Oh, Grace...\x01",
            "Would it kill her to write something a little\x01",
            "less contentious every once in a while?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FFE")

    label("loc_F51")


    ChrTalk(
        0x8,
        (
            "That Grace Lynn...\x01",
            "Off she goes, writing yet another controversial article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* Diet members have been bombarding us\x01",
            "with complaints nonstop because of her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_FFE")

    Jump("loc_2AE8")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10B1")

    ChrTalk(
        0x8,
        (
            "Now that the Anniversary Festival is over,\x01",
            "hasn't the city become much quieter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though, I bet things will pick right back up again\x01",
            "starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE8")

    label("loc_10B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1115")

    ChrTalk(
        0x8,
        (
            "We released our special issue today. Make\x01",
            "sure to pick up a copy for yourselves!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE8")

    label("loc_1115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11A5")

    ChrTalk(
        0x8,
        "Hmm, the park's pretty noisy today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Are they all going to check out the popular\x01",
            "touristy spots after the parade's over?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE8")

    label("loc_11A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_12D2")

    ChrTalk(
        0x8,
        (
            "Are you all excited for today's parade?\x01",
            "It's basically the Anniversary Festival's\x01",
            "main event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our reporters just went rushing out the building\x01",
            "with their cameras in hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's almost as if everyone in Crossbell manages\x01",
            "to temporarily let go of their worries at festivals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE8")

    label("loc_12D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B0")

    ChrTalk(
        0x8,
        (
            "Hey, everyone... I heard about yesterday's\x01",
            "events. Sounds like you had it hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I won't try to pry any details out of you,\x01",
            "but given the satisfied look on Grace's face,\x01",
            "I think I get the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FHaha, really? Color me impressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FI was bracing myself for the worst when Grace\x01",
            "showed up to be the MC...\x02\x03",
            "#0100FI must admit, though. Grace managed to\x01",
            "liven things up, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FShe was a touch aggravating. We must look\x01",
            "into a method to exact our revenge on her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0009FHaha, I'm with you there. Maybe we can shake\x01",
            "some information out of her next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "H-Hahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This might be the first time I've seen anybody\x01",
            "behave this way towards Grace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 3)
    Jump("loc_17FD")

    label("loc_15B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16C3")

    ChrTalk(
        0x8,
        (
            "Grace isn't here right now, if you're looking for her.\x01",
            "She's probably up to no good again, considering\x01",
            "she left the building with a smirk on her face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I recall her mentioning a vast sea of scoops waiting\x01",
            "out there for her, all thanks to the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FD")

    label("loc_16C3")


    ChrTalk(
        0x8,
        (
            "I'm surprised you guys are trying to get back\x01",
            "at Grace. She usually just gets under most\x01",
            "people's skin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys at the Special Support Section\x01",
            "must be awfully composed.\x02",
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
        "#0006FW-Well, not exactly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17FD")

    Jump("loc_2AE8")

    label("loc_1802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1885")

    ChrTalk(
        0x8,
        "Isn't it oddly noisy outside?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I suppose they're using the stage outside\x01",
            "for a performance right about now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE8")

    label("loc_1885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_19E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1936")

    ChrTalk(
        0x8,
        "Everybody left the building in high spirits today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They're probably out there having the time of\x01",
            "their lives covering the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DC")

    label("loc_1936")


    ChrTalk(
        0x8,
        "Welcome to the Crossbell News Service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All of our reporters have been busy as heck\x01",
            "running around town for material because\x01",
            "of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19DC")

    Jump("loc_2AE8")

    label("loc_19E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1B63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A7D")

    ChrTalk(
        0x8,
        (
            "*sigh* I'd even settle for B section seats.\x01",
            "Are there really no tickets left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Maybe the editor-in-chief can help me out...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B5E")

    label("loc_1A7D")


    ChrTalk(
        0x8,
        (
            "Arc en Ciel's private show starts\x01",
            "in only a little under two weeks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm totally envious of each and every one of\x01",
            "our reporters that gets to cover it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I unfortunately missed out on buying\x01",
            "tickets for myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B5E")

    Jump("loc_2AE8")

    label("loc_1B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C4C")

    ChrTalk(
        0x8,
        (
            "I'm sure you have to jump through a ton of\x01",
            "hoops to become a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You definitely can't be a weakling and give up.\x01",
            "If you want to become the real deal, you\x01",
            "have to make it through thick and thin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD9")

    label("loc_1C4C")


    ChrTalk(
        0x8,
        (
            "Reins looked a little depressed today...\x01",
            "What's got him feeling down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's strange for him, considering he's usually\x01",
            "so cheery.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CD9")

    Jump("loc_2AE8")

    label("loc_1CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1F00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DB9")

    ChrTalk(
        0x8,
        (
            "Did you know those mobsters from Revache & Co.\x01",
            "visit our offices every once in a while?\x01",
            "*sigh*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't comprehend how the editor-in-chief can remain\x01",
            "composed when he deals with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFB")

    label("loc_1DB9")


    ChrTalk(
        0x8,
        (
            "Some mobsters from Revache & Co. come by\x01",
            "every once in a while to speak with the editor-\x01",
            "in-chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They haven't committed any acts of violence, but\x01",
            "they definitely aren't shy when it comes to threatening\x01",
            "and intimidating him in any way they can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*sigh* Yep. Definitely not a fan of scary guys like them.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1EFB")

    Jump("loc_2AE8")

    label("loc_1F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_20FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FCA")

    ChrTalk(
        0x8,
        (
            "Grace is looking pretty busy these days.\x01",
            "I wonder what she's up to this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* I'm just praying she doesn't write another\x01",
            "article that showers us in complaints.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F7")

    label("loc_1FCA")


    ChrTalk(
        0x8,
        (
            "Grace has been busy as heck running around\x01",
            "collecting information lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've hardly seen her in the office ever since she\x01",
            "got back from her business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is she trying to dig up dirt on another celebrity?\x01",
            "Sounds like we've got another ticking time bomb\x01",
            "waiting for her out there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20F7")

    Jump("loc_2AE8")

    label("loc_20FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_22D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_220B")

    ChrTalk(
        0x8,
        (
            "I don't know if you guys knew this, but we\x01",
            "distributed tickets for the private performance\x01",
            "to the media so they could review it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Unfortunately for me, I'm not a reporter.\x01",
            "I have to stand in line like a normal person\x01",
            "to purchase a ticket.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CB")

    label("loc_220B")


    ChrTalk(
        0x8,
        "I overheard it by chance, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They finally started selling tickets for Arc en Ciel's\x01",
            "newest production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* That sure sounds nice...\x01",
            "I wish I could watch them, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_22CB")

    Jump("loc_2AE8")

    label("loc_22D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_23B4")

    ChrTalk(
        0x8,
        (
            "Grace isn't here right now, if you're looking for her.\x01",
            "She's probably up to no good again, considering\x01",
            "she left the building with a smirk on her face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm guessing she's on the hunt for her latest scoop.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AE8")

    label("loc_23B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_251D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_244A")

    ChrTalk(
        0x8,
        (
            "Ah... Do you all have business with the Crossbell\x01",
            "News Service?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You can direct any of your inquiries to yours truly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2518")

    label("loc_244A")


    ChrTalk(
        0x8,
        (
            "Our company relocated to this building\x01",
            "about a year ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We haven't gotten around to cleaning up, so\x01",
            "we've got a bunch of junk lying around.\x01",
            "If only I could find the time to organize it all...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2518")

    Jump("loc_2AE8")

    label("loc_251D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_27D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2620")

    ChrTalk(
        0x8,
        (
            "We're beginning to receive complaints about\x01",
            "articles other than the ones written by Grace...\x01",
            "This is starting to get a little bit out of hand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Would it kill everyone to tone down the\x01",
            "divisive rhetoric every once in a while?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D3")

    label("loc_2620")


    ChrTalk(
        0x8,
        (
            "We actually put a lot of effort into our finance,\x01",
            "international, entertainment, and local news\x01",
            "sections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, our local news... They keep uncovering\x01",
            "scandals, all thanks to a certain someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* Oh, Grace...\x01",
            "I doubt she'll ever write an article that isn't\x01",
            "bombastic.\x02",
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
        "#0006F(She sure seems like a handful...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_27D3")

    Jump("loc_2AE8")

    label("loc_27D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_28DB")

    ChrTalk(
        0x8,
        (
            "The Crossbell News Service is a great place\x01",
            "to have angry citizens storm in and yell at us\x01",
            "over the contents of news articles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Umm... Please tell me if you're unhappy\x01",
            "with anything. I can get in touch with the\x01",
            "editor-in-chief for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE8")

    label("loc_28DB")


    ChrTalk(
        0x8,
        "Welcome to the Crossbell News Service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Are you here to lodge a complaint about\x01",
            "one of our articles?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298B")

    ChrTalk(
        0x101,
        "#0005FHuh? No, I wasn't planning on it...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A49")

    label("loc_298B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C4")

    ChrTalk(
        0x102,
        "#0105FHmm? No, not particularly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A49")

    label("loc_29C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A0E")

    ChrTalk(
        0x103,
        "#0205F...? I have no reason to lodge a complaint.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A49")

    label("loc_2A0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A49")

    ChrTalk(
        0x104,
        "#0305FHmm? Nah. Not today, pretty lady.\x02",
    )

    CloseMessageWindow()

    label("loc_2A49")


    ChrTalk(
        0x8,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you'd like to voice a comment for any\x01",
            "of the stories we run, please let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'll call the editor-in-chief for you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2AE8")

    Return()

    # Function_6_C6D end

    def Function_7_2AE9(): pass

    label("Function_7_2AE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2BA3")

    ChrTalk(
        0xFE,
        (
            "Hmm? Interested in our Fulitzer Prize,\x01",
            "are we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really care if you look at it, but\x01",
            "don't get your grubby fingers all over\x01",
            "our prestigious award, okay?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4721")

    label("loc_2BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2C62")

    ChrTalk(
        0xFE,
        (
            "The airport was shut down, but my investigation\x01",
            "came up short when I went to go check it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn... What the hell's up with this\x01",
            "recent chain of incidents?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D42")

    label("loc_2C62")


    ChrTalk(
        0xFE,
        (
            "I went to investigate the airport 'cause I heard\x01",
            "it was shut down, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The First Division is cunning, I'll give them\x01",
            "that. They were able to avoid my questions\x01",
            "like it was nothing. Damn, this is frustrating.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2D42")

    Jump("loc_4721")

    label("loc_2D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2E8B")

    ChrTalk(
        0x9,
        (
            "I found out that the airport has been\x01",
            "shut down all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I can never rely on CPD announcements, so\x01",
            "I'll just have to take a look for myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Do me a favor. Make sure Grace takes a\x01",
            "good, hard look at those photos on her\x01",
            "desk when she gets back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, sir. I'll see to it that it happens.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4721")

    label("loc_2E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_30AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2F48")

    ChrTalk(
        0xFE,
        (
            "This area serves as Crossbell's business district.\x01",
            "It's supposed to be one of the safest places\x01",
            "in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should we get a back door installed\x01",
            "here, too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2F48")


    ChrTalk(
        0xFE,
        (
            "Figures. Take off that fresh coat of paint\x01",
            "and it's easy to see just how dangerous\x01",
            "Crossbell really is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, our old office building had a\x01",
            "back door, just in case the company was\x01",
            "ever attacked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That way, in the case of an emergency,\x01",
            "the paper could still be published.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The show must go on, as they say.\x01",
            "That was our pride.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_30A9")

    Jump("loc_4721")

    label("loc_30AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_319E")

    ChrTalk(
        0xFE,
        (
            "We've been sniffing out news of a bunch of skirmishes\x01",
            "involving the mafia taking place around the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gimme a break... Are they in the middle of\x01",
            "some petty dispute again?\x01",
            "Damn it. They need to get over themselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4721")

    label("loc_319E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3226")

    ChrTalk(
        0xFE,
        "Oh, it's almost lunchtime.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll hit up the stall by the park.\x01",
            "Man, I can't get enough of their noodles.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4721")

    label("loc_3226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3474")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3381")

    ChrTalk(
        0xFE,
        (
            "The Fulitzer Prize is a prestigious award given\x01",
            "to only the greatest of journalists throughout Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I personally believe that there's no higher honor that\x01",
            "one who is dedicated to journalism can receive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Check out that bad boy on the shelf.\x01",
            "That's a certificate for the Fulitzer Prize.\x01",
            "A beauty, ain't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346F")

    label("loc_3381")


    ChrTalk(
        0xFE,
        "You know about the Fulitzer Prize, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a prestigious award given to only the\x01",
            "greatest of journalists throughout Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I personally believe that there's no higher honor than\x01",
            "to dedicate yourself to journalism.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_346F")

    Jump("loc_4721")

    label("loc_3474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_35ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3508")

    ChrTalk(
        0xFE,
        (
            "I still have to develop the photos and double-check\x01",
            "them... Am I going to make it in time for\x01",
            "tomorrow's special issue?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35E8")

    label("loc_3508")


    ChrTalk(
        0xFE,
        (
            "I got way too carried away during the parade\x01",
            "and took far too many photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds like the others took a bunch, too...\x01",
            "I need to hurry up and develop them, or none\x01",
            "of mine will get chosen for the special issue!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_35E8")

    Jump("loc_4721")

    label("loc_35ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_36A1")

    ChrTalk(
        0xFE,
        (
            "Oh, I think I've still got a little bit of time\x01",
            "before the parade begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd better get some grub while I still can.\x01",
            "Heaven forbid I get hungry during it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4721")

    label("loc_36A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_373E")

    ChrTalk(
        0xFE,
        "Oh. You have some business here or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but try and keep it down, will you?\x01",
            "I don't have time to take care of visitors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4721")

    label("loc_373E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_37BF")

    ChrTalk(
        0xFE,
        (
            "Hmm... What about this picture?\x01",
            "Everybody's taking too many photos, so\x01",
            "it's a pain to get them all developed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4721")

    label("loc_37BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3980")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3895")

    ChrTalk(
        0xFE,
        (
            "Excellent. We'll be able to write some great articles\x01",
            "on the Anniversary Festival, at this rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I can't shake the feeling that I played\x01",
            "right into the editor-in-chief's hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397B")

    label("loc_3895")


    ChrTalk(
        0xFE,
        (
            "Damn, that was a close call...\x01",
            "I barely made it on time with my last article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The editor-in-chief even made me write\x01",
            "in all of the captions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's whatever. We managed to break a\x01",
            "massive story thanks to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_397B")

    Jump("loc_4721")

    label("loc_3980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3ACB")

    ChrTalk(
        0xFE,
        (
            "That certificate sitting on the shelf over\x01",
            "there is from the time our company won\x01",
            "the famed Fulitzer Prize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We used to have a legendary journalist in our\x01",
            "ranks at the time. It was all thanks to him that\x01",
            "we received this humbling award.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was a remarkable achievement\x01",
            "for the Crossbell News Service.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4721")

    label("loc_3ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3C63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BDC")

    ChrTalk(
        0xFE,
        (
            "Reins has become a pretty talented cameraman\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His reflexes are sharp, and his photos help\x01",
            "add flavor to our duller articles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's our go-to guy when we need to capture\x01",
            "photos for more important topics, like\x01",
            "Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C5E")

    label("loc_3BDC")


    ChrTalk(
        0xFE,
        (
            "Reins has become a pretty talented cameraman\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That serious personality of his is the perfect\x01",
            "foil for Grace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C5E")

    Jump("loc_4721")

    label("loc_3C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3D24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3D1C")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        "(Well, he's still the newest face at the CNS.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(I gotta show him some upfront action to give\x01",
            "an idea how fast us reporters need to work.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    Jump("loc_3D1F")

    label("loc_3D1C")

    Call(0, 10)

    label("loc_3D1F")

    Jump("loc_4721")

    label("loc_3D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3F00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E48")

    ChrTalk(
        0xFE,
        (
            "I've decided to entrust Reins with\x01",
            "the local news photography and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He might be a rookie, but man, this guy\x01",
            "sure knows how to deliver. His skills as\x01",
            "a photographer shine brightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh. A bit more mentoring, and he's\x01",
            "sure to become a great reporter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EFB")

    label("loc_3E48")


    ChrTalk(
        0xFE,
        "All right, 'bout time I go looking for new stories.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got Arc en Ciel's private performance\x01",
            "and the Anniversary Festival next month.\x01",
            "Things are about to get hectic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EFB")

    Jump("loc_4721")

    label("loc_3F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3F65")

    ChrTalk(
        0xFE,
        "Geez, what's there to be nervous about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm trying to throw you a bone here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4721")

    label("loc_3F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4119")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_404A")

    ChrTalk(
        0xFE,
        (
            "Hmm... 'Bold, New Companies Sponsored by the IBC'?\x01",
            "I've definitely got a good feeling about this article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right, an interview with the CEO of the IBC\x01",
            "would really bring this article together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4114")

    label("loc_404A")


    ChrTalk(
        0xFE,
        (
            "Oh, what's up? Are you here to see Grace?\x01",
            "She's off on a business trip, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given the time of day, she's probably out snapping\x01",
            "photos of Heimdallr, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_9E(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x9, 0x10)

    label("loc_4114")

    Jump("loc_4721")

    label("loc_4119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4361")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42AD")
    OP_4B(0xB, 0xFF)
    OP_93(0xFE, 0x10E, 0x0)

    ChrTalk(
        0x9,
        (
            "Not only is it an extravagant event, but\x01",
            "we'll even be collaborating with the\x01",
            "one and only Imperial Chronicle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You planning on going, Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2104FOf course I am! What better chance than the\x01",
            "Imperial Memorial Ceremony will I have at\x01",
            "meeting the Imperial family?!\x02\x03",
            "#2102FEven if for just a minute, I'm going to\x01",
            "hold royalty in the palm of my hand!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_435C")

    label("loc_42AD")

    OP_4B(0xB, 0xFF)
    OP_93(0xFE, 0x10E, 0x0)

    ChrTalk(
        0xFE,
        (
            "You won't hear me complaining, as long as\x01",
            "you get the editor-in-chief's permission.\x01",
            "Knock 'em dead, Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2109FThank ya! ♪\x01",
            "You can leave it to me!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_435C")

    Jump("loc_4721")

    label("loc_4361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44BD")

    ChrTalk(
        0xFE,
        (
            "*puff*... These are the photos for this\x01",
            "issue's local news section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the CPD's whatchamacallit section, right?\x01",
            "Hmm, maybe we should postpone the article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, Grace said she'd cover that team\x01",
            "some other time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(I'm pretty worried for what's\x01",
            "to come in her article...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_452C")

    label("loc_44BD")


    ChrTalk(
        0xFE,
        (
            "As for the CPD's newly-formed what's-it's-face\x01",
            "section... Well, let's just postpone this article\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_452C")

    Jump("loc_4721")

    label("loc_4531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_45DE")

    ChrTalk(
        0xFE,
        (
            "Wait, really? Are you seriously not here for\x01",
            "information on the raid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you don't have any business with us, then scram.\x01",
            "You're getting in our way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4721")

    label("loc_45DE")


    ChrTalk(
        0xFE,
        "*puff*...*puff*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh? What's the matter with you guys?\x01",
            "You trying to invade us or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh. If you wanted to ambush our editorial department,\x01",
            "then you're 100 years too early, pals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be it the mafia or whoever you guys are,\x01",
            "the Crossbell Times won't be taken down!\x01",
            "Be sure to remember that, kids.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4721")

    TalkEnd(0xFE)
    Return()

    # Function_7_2AE9 end

    def Function_8_4725(): pass

    label("Function_8_4725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4B5A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_4877")

    ChrTalk(
        0xB,
        (
            "#2103FI'll keep on covering the diet session while\x01",
            "I dig up dirt on Speaker Hartmann and the\x01",
            "mafia's connection.\x02\x03",
            "I'll also keep my eyes peeled for this whole\x01",
            "drug kerfuffle, while I'm at it.\x02\x03",
            "#2100FOh, yeah. And if you learn anything on your end,\x01",
            "then holler for me and I'll be there in a jiffy!\x01",
            "Thank ya!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B52")

    label("loc_4877")


    ChrTalk(
        0xB,
        (
            "#2103FInvestigation awaits!\x02\x03",
            "...\x02\x03",
            "#2102FSay, how'd you guys get tangled up\x01",
            "with that Lechter kid, anyhow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FWe kinda just bumped into him by accident, y'know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FWe don't really know what that guy's deal is,\x01",
            "much less why he's in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2100FHmm, alas, we're at a loss...\x01",
            "But I DO feel like I've heard that\x01",
            "name somewhere before, though.\x02\x03",
            "#2103FLechter, Lechter...\x01",
            "Just where was it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FWe think he's from the Empire, if that helps.\x01",
            "Perhaps you've heard about him while reporting there.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#2105FOooh, that might have been it.\x01",
            "But where exactly in the Empire?\x02\x03",
            "#2103FWell, we have bigger fish to fry with all this\x01",
            "other coverage that requires the Grace touch!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 0)

    label("loc_4B52")

    TalkEnd(0xFE)
    Jump("loc_585D")

    label("loc_4B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_52C6")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BF7")
    Jump("loc_4C41")

    label("loc_4BF7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C17")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C41")

    label("loc_4C17")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C37")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C41")

    label("loc_4C37")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C41")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 3)), scpexpr(EXPR_END)), "loc_4D88")

    ChrTalk(
        0xB,
        (
            "#2100FMy dearest friends, how've your recent\x01",
            "endeavors been treating you?\x02\x03",
            "#2109FRemember, if you stumble across any\x01",
            "comical cases, be sure to come let me\x01",
            "know, 'kay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F*sigh* Come on, everyone.\x01",
            "Let's get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#2106FGeez! Could you be any colder?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_52BA")

    label("loc_4D88")

    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#2105FOh, my besties are here!\x02\x03",
            "#2102FWow. It's been a long time, hasn't it?\x01",
            "Did you all read up on that thrilling\x01",
            "incident with the monsters last month?\x02\x03",
            "#2109FDon't you worry, my friends. Grace here\x01",
            "knows you've busted your humps!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FIt's nice to see you again, Grace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FNow that you mention it. You didn't write\x01",
            "that article, did you, Grace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2100FCorrect. Alas, I was away from Crossbell, covering\x01",
            "a different event that needed the Grace touch.\x02\x03",
            "#2103FTo be honest, I was hoping I could be the SSS's sole\x01",
            "reporter. I like writing articles about you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FOur hypothesis was accurate, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FWell, gettin' dunked on all the time by your\x01",
            "articles can wear you down, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2103FGeez! It's like you can't understand the immense\x01",
            "love I harbor for the SSS. It's like mama bird\x01",
            "watching her chicks grow up!\x02\x03",
            "#2109FThe fact that we met here must signify\x01",
            "our fated connection to one another!\x01",
            "You've even had a funny way of operating, lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FHey, Grace. You're in the middle of your break,\x01",
            "right? Sorry for interrupting you like that.\x01",
            "We'll get out of your hair now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FGood luck with your strenuous 'work.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2105FWh-What?\x01",
            "You're leaving me already?\x02\x03",
            "#2106FAw, c'mon. Don't you think you've been\x01",
            "treating me a little too coldly?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 3)

    label("loc_52BA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_585D")

    label("loc_52C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55F6")
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "#2100FOh, my beloved SSS has come again.\x02\x03",
            "#2109FHello, hello. How's life treating you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_END)), "loc_53C3")

    ChrTalk(
        0x101,
        "#0006FDon't 'hello, hello' us, Grace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FWe saw you felt it necessary to write another\x01",
            "scathing article about us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545D")

    label("loc_53C3")


    ChrTalk(
        0x101,
        "#0006FDon't try to hide behind your smooth talk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FYou aren't going to use that case from before\x01",
            "to make us out to be fools again, are you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_545D")


    ChrTalk(
        0xB,
        (
            "#2102FC'mon, guys! Turn those frowns upside down!\x02\x03",
            "Things may look a bit shaky right now,\x01",
            "but trust me, I'm rooting for you!\x02\x03",
            "#2103FAh. You'll have to forgive me, but I'm\x01",
            "actually a teensy bit busy this week.\x01",
            "Don't have much time for chitchat, you know?\x02\x03",
            "#2102FKeep those enthralling comments on the tip of your\x01",
            "tongue until my schedule clears up, 'kay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FF-Fine...\x02",
    )

    CloseMessageWindow()
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    SetScenarioFlags(0x6D, 1)
    Jump("loc_585A")

    label("loc_55F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_56E5")
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "#2102FSorry, but I'm going to be a teensy bit\x01",
            "busy this week, so I don't have much\x01",
            "time for chitchat, you know?\x02\x03",
            "Keep those enthralling comments on the tip of your\x01",
            "tongue until my schedule clears up, 'kay?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x0)
    Jump("loc_585A")

    label("loc_56E5")

    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "Not only is it an extravagant event, but\x01",
            "we'll even be collaborating with the\x01",
            "one and only Imperial Chronicle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You planning on going, Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2103FOf course I am! What better chance than the\x01",
            "Imperial Memorial Ceremony will I have at\x01",
            "meeting the Imperial family?!\x02\x03",
            "#2109FEven if for just a minute, I'm going to\x01",
            "hold royalty in the palm of my hand!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_585A")

    TalkEnd(0xFE)

    label("loc_585D")

    Return()

    # Function_8_4725 end

    def Function_9_585E(): pass

    label("Function_9_585E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_5986")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_590F")

    ChrTalk(
        0xFE,
        (
            "(Oh, I really, really, really don't\x01",
            "want to cover the mafia...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Covering that chaotic diet session would\x01",
            "have been a million times better!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5981")

    label("loc_590F")

    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        "Hmm... I'm going to cover the diet! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(D-Does that mean I have to\x01",
            "cover the... *gulp*)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xB, 0xFF)

    label("loc_5981")

    Jump("loc_6903")

    label("loc_5986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5A4F")

    ChrTalk(
        0xFE,
        (
            "Seems like Grace already rushed out,\x01",
            "looking for her latest scoop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She left it to me to cover the rest of the diet session...\x01",
            "*sigh* Guess I'll try my hardest to do a good job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6903")

    label("loc_5A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5C4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5ACD")

    ChrTalk(
        0xFE,
        "You just missed Grace, if you were looking for her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wonder where she ran off to this time...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C49")

    label("loc_5ACD")


    ChrTalk(
        0xFE,
        (
            "Okay! I've gotta cover the closing ceremony and the\x01",
            "Business Owners' Association's stage events today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh! Maybe I can snap some photos of the ship\x01",
            "bound for Mishelam afterwards.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xFE,
        (
            "That reminds me. Grace just left the building\x01",
            "a few moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a little hard for me to find motivation to start working\x01",
            "without Grace's direction.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5C49")

    Jump("loc_6903")

    label("loc_5C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5E3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5D09")

    ChrTalk(
        0xFE,
        (
            "Hmm... Do I want to go to Central Square or the\x01",
            "stage setup in the Harbor District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd be willing to bet that Grace would exclaim\x01",
            "'Why not go to both?!'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E38")

    label("loc_5D09")


    ChrTalk(
        0xFE,
        "Oh, the SSS guys are here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you come to visit Grace? She's up on the\x01",
            "second floor putting her next article together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She didn't have enough 'breathtaking' photos, as she\x01",
            "liked to put it, so she ordered me to go take some more.\x01",
            "*sigh* That's another round through the city, I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5E38")

    Jump("loc_6903")

    label("loc_5E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5FFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5EE8")

    ChrTalk(
        0xFE,
        (
            "Grace has been investigating something that\x01",
            "has her giddy with enthusiasm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't say I've seen her face around the office\x01",
            "lately, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FF7")

    label("loc_5EE8")


    ChrTalk(
        0xFE,
        (
            "Arc en Ciel's private performance should be starting soon...\x01",
            "At least, according to their own schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, that reminds me. Grace has been doing some\x01",
            "sort of secret investigation lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She hardly ever shows her face around the office nowadays.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5FF7")

    Jump("loc_6903")

    label("loc_5FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_61E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_60BB")

    ChrTalk(
        0xFE,
        (
            "I suppose I shouldn't complain, considering I get to\x01",
            "cover Arc en Ciel's performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I'd rather be treated more as a reporter\x01",
            "and less as a cameraman...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61DB")

    label("loc_60BB")


    ChrTalk(
        0xFE,
        (
            "It's been decided that I'll be accompanying the head\x01",
            "reporter as their cameraman for the up-and-coming\x01",
            "Arc en Ciel performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, the editor-in-chief is cruel. He basically told\x01",
            "me to not worry about writing an article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*grumble* Well, I suppose this is fine, too...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_61DB")

    Jump("loc_6903")

    label("loc_61E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_623A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6232")

    ChrTalk(
        0xFE,
        (
            "C-Can you please reconsider?\x01",
            "That was my only column!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6235")

    label("loc_6232")

    Call(0, 10)

    label("loc_6235")

    Jump("loc_6903")

    label("loc_623A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6402")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_62D7")

    ChrTalk(
        0xFE,
        (
            "I'm responsible for writing the article about the\x01",
            "wolf attacks in our latest issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd love it if you all read through it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_63FD")

    label("loc_62D7")


    ChrTalk(
        0xFE,
        "Oh, the SSS is here again. What's up, everyone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm responsible for writing the article about the\x01",
            "wolf attacks in our latest issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the first time I've had my article\x01",
            "selected as the front-page story! I'm on\x01",
            "top of the world!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I still haven't gotten over it, yet!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_63FD")

    Jump("loc_6903")

    label("loc_6402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6559")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6485")

    ChrTalk(
        0xFE,
        "A total rookie like me, in charge of the local news?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, man... I don't even know where to begin.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6554")

    label("loc_6485")


    ChrTalk(
        0xFE,
        (
            "Grace is out on a job, so I'M being placed\x01",
            "in charge of the local news this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C-Crap, my nerves are getting the best of me.\x01",
            "MacKennon sure loves to put me in the most\x01",
            "ridiculous situations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_6554")

    Jump("loc_6903")

    label("loc_6559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_662B")

    ChrTalk(
        0xFE,
        (
            "Oh, yeah. Grace is out on a job this week,\x01",
            "if you were looking for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I gotta say, it's actually pretty quiet without her around.\x01",
            "I might even admit that I'm a little lonely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677C")

    label("loc_662B")


    ChrTalk(
        0xFE,
        (
            "Now that Grace is out of town, our editing session\x01",
            "went a lot quicker than it usually does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's pretty normal for her to go full throttle\x01",
            "during our sessions, so they usually end\x01",
            "up devolving into heated arguments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, she can write one hell of an interesting article,\x01",
            "so I don't necessarily think it's a bad thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_677C")

    Jump("loc_6903")

    label("loc_6781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6822")

    ChrTalk(
        0xFE,
        (
            "It might only be a small article, but I'm still\x01",
            "glad that they're trusting me with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All right! I gotta knock this one outta the park!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6903")

    label("loc_6822")


    ChrTalk(
        0xFE,
        "Okay, the next topic is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, hey, guys. I recently received permission to\x01",
            "start writing my own articles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huzzah!\x01",
            "Though it's just a tiny column in the culture\x01",
            "section, I can't help but be filled with joy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_6903")

    TalkEnd(0xFE)
    Return()

    # Function_9_585E end

    def Function_10_6907(): pass

    label("Function_10_6907")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xA,
        "Huh? You need a cameraman?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yeah. I heard you're a real pro at taking photos.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We don't have a cameraman to help cover\x01",
            "Arc en Ciel yet. You mind doing me this favor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Uhh... I still have a bunch of work I need to\x01",
            "do for my cooking column...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "We'll just go ahead and postpone that for a while.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "W-What? No way...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_10_6907 end

    def Function_11_6A84(): pass

    label("Function_11_6A84")

    EventBegin(0x0)
    Fade(500)
    OP_68(3050, 1520, -1840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, 2700, 20, -2000, 90)
    SetChrPos(0x102, 2700, 20, -700, 90)
    SetChrPos(0x103, 1400, 20, -2000, 90)
    SetChrPos(0x104, 1400, 20, -700, 90)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CC2")

    ChrTalk(
        0x8,
        "#11PWelcome to the Crossbell News Service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHow may we help you today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FHello, we're the Special Support Section.\x02\x03",
            "We're here to follow up on the support request\x01",
            "you submitted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, it's nice to meet you all.\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe person responsible for submitting the request\x01",
            "wishes to explain it to you in person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PDo you mind? Is now a good time?\x02",
    )

    CloseMessageWindow()
    OP_29(0x18, 0x1, 0x0)
    Call(0, 12)
    Jump("loc_6DAA")

    label("loc_6CC2")


    ChrTalk(
        0x8,
        (
            "#11PHave you taken care of all of your current business?\x01",
            "This might take a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe person responsible for submitting the request\x01",
            "wishes to explain it to you in person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PDo you mind? Is now a good time?\x02",
    )

    CloseMessageWindow()
    Call(0, 12)

    label("loc_6DAA")

    Return()

    # Function_11_6A84 end

    def Function_12_6DAB(): pass

    label("Function_12_6DAB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6DE2"),
        (1, "loc_928C"),
        (SWITCH_DEFAULT, "loc_939F"),
    )


    label("loc_6DE2")

    OP_60(0x0)

    ChrTalk(
        0x101,
        "#12P#0000FYeah, we're fine to help you out right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PWonderful.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EB7")

    ChrTalk(
        0x8,
        (
            "#11PI know it's bothersome, but please go\x01",
            "upstairs to the second floor.\x01",
            "She should be waiting for you all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F2D")

    label("loc_6EB7")


    ChrTalk(
        0x8,
        (
            "#11PI know it's bothersome, but please go\x01",
            "upstairs to the second floor. I'll call and\x01",
            "let her know you're ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F2D")


    ChrTalk(
        0x101,
        (
            "#12P#0000FOkay, sounds good.\x02\x03",
            "#0003F(Anyway, should we head upstairs?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(63810, 1500, -70, 0)
    MoveCamera(38, 27, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(27050, 0)
    LoadChrToIndex("chr/ch20200.itc", 0x1E)
    LoadChrToIndex("chr/ch30202.itc", 0x1F)
    LoadChrToIndex("chr/ch23600.itc", 0x20)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xC, 67320, 0, 12770, 0)
    SetChrPos(0xD, 57840, 0, 6320, 0)
    SetChrPos(0xE, 67050, 0, -170, 135)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 60010, 150, 10690, 270)
    SetChrPos(0x101, 58200, 0, 11760, 135)
    SetChrPos(0x102, 58650, 0, 12660, 135)
    SetChrPos(0x103, 57000, 0, 11920, 135)
    SetChrPos(0x104, 57480, 0, 13060, 135)
    OP_68(58950, 1500, 9840, 8000)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_70C3():
        OP_95(0xFE, 67320, 0, 5770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_70C3)
    WaitChrThread(0xC, 1)

    def lambda_70E1():
        OP_95(0xFE, 55550, 0, 5030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_70E1)
    OP_6F(0x1)
    Fade(1000)
    OP_68(57910, 1500, 11780, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(20010, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#11P#2109FHello, hello. My wonderful friends from the\x01",
            "Special Support Section! ㈱\x02",
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
        "#12P#0003FI-It's you, Grace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0106FWhy am I not surprised?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_73DD")

    ChrTalk(
        0xB,
        (
            "#11P#2105FGeez! What the heck did I ever do to you guys?!\x01",
            "Pretty rude reaction to give one of your most\x01",
            "loyal fans.\x02\x03",
            "#2109FYou should all be rejoicing at the fact that you've\x01",
            "been graced by my presence while I'm oh-so busy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FI am not sure I understand where you are\x01",
            "coming from.\x02\x03",
            "#0200FThat is unimportant, though. Would you\x01",
            "please proceed with an explanation of\x01",
            "what your support request entails?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E5A")

    label("loc_73DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_786C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76C6")

    ChrTalk(
        0xB,
        (
            "#11P#2100FExcellent work yesterday!\x02\x03",
            "#2109FI just added the finishing touches to an exciting\x01",
            "article about yesterday's race!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FShe's turnin' it into an article, eh? Can't say I\x01",
            "didn't see that one comin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2100FYou bet'cha! We're featuring it in an extra-special\x01",
            "issue of the Crossbell Times that we'll be publishing\x01",
            "on the final day of the festival!\x02\x03",
            "#2109FYour ventures always make for superb stories,\x01",
            "so I'll be keeping a close eye on you! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006F(She's building us up just to\x01",
            "tear us down, isn't she?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203F(That has been the pattern thus far, yes.)\x02\x03",
            "#0200FMore importantly, Grace...\x01",
            "Would you please proceed with an explanation\x01",
            "of what your support request entails?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 0)
    Jump("loc_7867")

    label("loc_76C6")


    ChrTalk(
        0xB,
        (
            "#11P#2105FGeez! What the heck did I ever do to you guys?!\x01",
            "Pretty rude reaction to give one of your most\x01",
            "loyal fans.\x02\x03",
            "#2109FYou should all be rejoicing at the fact that you've\x01",
            "been graced by my presence while I'm oh-so busy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FI am not sure I understand where you are\x01",
            "coming from.\x02\x03",
            "#0200FThat is unimportant, though. Would you please\x01",
            "proceed with an explanation of what your\x01",
            "support request entails?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7867")

    Jump("loc_7E5A")

    label("loc_786C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CB9")

    ChrTalk(
        0xB,
        (
            "#11P#2109FI love you guys so much! That scoop earlier\x01",
            "was exactly what I was looking for!\x02\x03",
            "I know I can always count on the valiant SSS!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F*sigh* Always the smooth-talker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FYou do realize that our job is not to provide\x01",
            "you with stories, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0106FThe situation was quite messy, but...\x02\x03",
            "#0100FI'm a little relieved that the article was primarily\x01",
            "sympathetic towards Grandfather's struggles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2106FWeeell, I'm kind of barred from writing pieces on\x01",
            "the Imperial Faction, so it wouldn't be fair if\x01",
            "I only criticized Mayor MacDowell, right?\x02\x03",
            "#2100FAnd besides, your grandfather's popularity with\x01",
            "the citizens is off the charts! Heck, I like\x01",
            "the old guy myself.\x02\x03",
            "#2102FMaybe I shouldn't be saying this as a journalist,\x01",
            "but...I really try to cut the guy some slack,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0100FThank you, Grace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FIt's fine to sympathize with him a little, isn't it?\x01",
            "Reporters are people, too, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FMore importantly, Grace...\x01",
            "Would you please proceed with an explanation\x01",
            "of what your support request entails?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB5, 1)
    Jump("loc_7E5A")

    label("loc_7CB9")


    ChrTalk(
        0xB,
        (
            "#11P#2105FGeez! What the heck did I ever do to you guys?!\x01",
            "Pretty rude reaction to give one of your most\x01",
            "loyal fans.\x02\x03",
            "#2109FYou should all be rejoicing at the fact that you've\x01",
            "been graced by my presence while I'm oh-so busy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FI am not sure I understand where you are\x01",
            "coming from.\x02\x03",
            "#0200FThat is unimportant, though. Would you please\x01",
            "proceed with an explanation of what your\x01",
            "support request entails?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E5A")


    ChrTalk(
        0xB,
        (
            "#11P#2106FSheesh, I figured you'd react like that.\x02\x03",
            "#2100FAnyway, let me give you the rundown. You\x01",
            "probably got the gist of it when reading the\x01",
            "request, but I'll give you some more details.\x02\x03",
            "The Crossbell Times is aiming to publish an\x01",
            "additional issue meant to act as a tour guide.\x02\x03",
            "#2109FAaaand your best friend, Grace, is leading\x01",
            "the charge! Isn't this my most fabulous idea\x01",
            "ever?! Eh? Eh?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0309FGotta admit, I'm on board!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0003FPlease continue, Grace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2100FRight! So, I'd like for you all to go take photos\x01",
            "to use in the magazine.\x02\x03",
            "I only need the snazziest shots you can take\x01",
            "of Crossbell's most popular sightseeing spots.\x02\x03",
            "#2106FMonsters roam the highways, so we aren't the\x01",
            "most suited to go straight into the front lines\x01",
            "to get some great action shots, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FHowever...I have my reservations as to whether\x01",
            "any of us are qualified for the job.\x02\x03",
            "We cannot guarantee the level of quality you\x01",
            "aim to seek with the photographs we take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2106FReins is already busy enough, thanks to how\x01",
            "crazy the Anniversary Festival is. He's usually\x01",
            "my right-hand photographer, but, alas...\x02\x03",
            "#2100FOh, well. I've prepared a nice little memo for\x01",
            "you guys that outlines all of the best tourist\x01",
            "spots to take photos. I'm counting on you to\x01",
            "bring some fantastic shots!\x02\x03",
            "#2106FAs long as at least one of you has the tiniest\x01",
            "bit of experience handling a camera, then I\x01",
            "think we'll manage.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x102,
        "#5P#0106FI...suppose that would be me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8481():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8481)

    def lambda_848E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_848E)

    def lambda_849B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_849B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0xB,
        "#11P#2105FWhoa, seriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FYou have experience taking photos, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0300FHuh. News to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FCurious. I would believe you would\x01",
            "need to use an orbal camera for\x01",
            "quite a while to master it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_859A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_859A)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#5P#0112FW-Well, it was a hobby of mine while\x01",
            "I was studying abroad.\x02\x03",
            "#0113FOf course, it's been quite some time\x01",
            "since then. I've probably gotten\x01",
            "a bit rusty at it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2102FIt'll get the job done! Trust me, it's still\x01",
            "better than being completely green!\x02\x03",
            "#2100FWell, now that we've resolved that issue...\x01",
            "are you feeling up to the task?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_870A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_870A)

    def lambda_8717():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8717)

    def lambda_8724():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8724)

    def lambda_8731():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8731)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x101,
        (
            "#12P#0000FYeah, we should be good to go.\x01",
            "We accept your request, Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2109FOh, my heroes! ㈱\x01",
            "Well, then. Here you go!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x33B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33B, 1)

    ChrTalk(
        0x101,
        (
            "#12P#0000FSo, all we need to do is find scenic spots\x01",
            "around Crossbell and take some photos\x01",
            "with this camera, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2102FBingo. I'd better not find any scratches\x01",
            "on it when you bring it back, 'kay?\x02\x03",
            "#2105FOh, right. There's one more thing I'd\x01",
            "advise you to be cautious of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0305FLay it on us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2100FThe Erebonian Empire's border can be seen as\x01",
            "clear as day from Bellguard Gate, as can the\x01",
            "Calvardian border from Tangram Gate.\x02\x03",
            "#2100FIt's a huge no-no to include any pictures of them\x01",
            "in our magazine, so please do try and avoid\x01",
            "snapping any shots of them, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0105FIs it due to political tensions?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2106FIndeed it is, Elie. Circumstances on our\x01",
            "side prohibit us from using them, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FOkay, so taking any photos of the border\x01",
            "is a no-go... Anything else we should know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2100FYep! I'm setting a minimum quota of five photos\x01",
            "to submit. Feel free to take more than that,\x01",
            "if you can!\x02\x03",
            "We're going to publish it at the end of the\x01",
            "festival, so feel free to take your time\x01",
            "finding the best spots.\x02\x03",
            "#2109FAfter all, the more photos you can take,\x01",
            "the more it'll help us out in the long run!\x02\x03",
            "#2100FHmm, yeah. That's about it, for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2100FWhen you've wrapped everything up,\x01",
            "just let our receptionist know, and\x01",
            "she'll give me a ring.\x02\x03",
            "#2109FWell, anyway. Back to work, I go!\x01",
            "I'll be eagerly awaiting your results!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5850, 1500, 940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18590, 0)
    SetChrPos(0x101, -4700, 0, 2100, 225)
    SetChrPos(0x102, -4700, 0, 800, 315)
    SetChrPos(0x103, -6000, 0, 800, 45)
    SetChrPos(0x104, -6000, 0, 2100, 135)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#0009FHaha... Some people never change.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FCan't say I've met many ladies with a personality\x01",
            "as wild as hers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FI think it's safe to assume that Grace is\x01",
            "incapable of running out of energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0206FWhere exactly is she able to muster up\x01",
            "her limitless vitality from?\x02\x03",
            "#0211FWell, regardless. She managed to skillfully\x01",
            "redirect all of her busywork onto us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0303FEh, who cares? Didn't sound like she\x01",
            "was in too big a hurry for the photos...\x02\x03",
            "#0300FS'pose we should just remember to take\x01",
            "photos as work takes us on our rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FTrue enough. Entrusting the photography\x01",
            "to Elie will ensure that this request will\x01",
            "be completed with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0112FP-Please lower your expectations.\x01",
            "It was just a small hobby of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FI'm sure you'll be fine, Elie. Let's just make\x01",
            "sure to remember to take some photographs\x01",
            "when we come across some scenic spots.\x02",
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
            "[The Many Famous Views of Crossbell]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetChrPos(0x0, -4930, 0, 1860, 90)
    OP_29(0x18, 0x1, 0x1)
    SetScenarioFlags(0x0, 5)
    EventEnd(0x5)
    Jump("loc_93AE")

    label("loc_928C")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#12P#0006FSorry, we're a little busy at the moment.\x01",
            "We'll try to get back to you as soon as we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, really? That's unfortunate.\x01",
            "Well, you know where to find us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please come by again if you find a time that\x01",
            "is convenient for you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    EventEnd(0x5)
    Jump("loc_93AE")

    label("loc_939F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93AE")

    label("loc_93AE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_6DAB end

    def Function_13_93B9(): pass

    label("Function_13_93B9")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3050, 1520, -1840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18370, 0)
    SetChrPos(0x101, 2700, 20, -2000, 90)
    SetChrPos(0x102, 2700, 20, -700, 90)
    SetChrPos(0x103, 1400, 20, -2000, 90)
    SetChrPos(0x104, 1400, 20, -700, 90)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11POh, wow...\x01",
            "It looks like you managed to take a lot of photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'll call Grace and let her know.\x01",
            "Are you ready to submit them?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Not Yet]\x01",      # 0
            "[Submit]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9518"),
        (1, "loc_9598"),
        (SWITCH_DEFAULT, "loc_95A3"),
    )


    label("loc_9518")

    OP_60(0x0)

    ChrTalk(
        0x8,
        (
            "#11PUnderstood. Please take your time and come\x01",
            "back when you're ready to submit them.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 2710, 20, -1270, 90)
    EventEnd(0x5)
    Jump("loc_95A8")

    label("loc_9598")

    OP_60(0x0)
    Call(0, 14)
    Jump("loc_95A8")

    label("loc_95A3")

    Jump("loc_95A8")

    label("loc_95A8")

    Return()

    # Function_13_93B9 end

    def Function_14_95A9(): pass

    label("Function_14_95A9")


    ChrTalk(
        0x101,
        "#12P#0000FOkay, this should be all of them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYep, looks like you managed to take enough of them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAlso, could you return the orbal camera you\x01",
            "borrowed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PWe'll start developing the photos right away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FAh, I nearly forgot about that.\x01",
            "I'm excited to see how they turned out.\x02",
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
            "Returned ",
            scpstr(SCPSTR_CODE_ITEM, 0x33B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x33B, 1)

    ChrTalk(
        0x8,
        "#11PYep, we'll get right on it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAnyway, Grace should be waiting on the second floor.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis181.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis180.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis182.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis183.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis184.itp")
    CreatePortrait(5, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis185.itp")
    CreatePortrait(6, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis186.itp")
    CreatePortrait(7, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis187.itp")
    CreatePortrait(8, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis188.itp")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 60010, 150, 10690, 270)
    SetChrPos(0x101, 58200, 0, 11760, 135)
    SetChrPos(0x102, 58650, 0, 12660, 135)
    SetChrPos(0x103, 57000, 0, 11920, 135)
    SetChrPos(0x104, 57480, 0, 13060, 135)
    OP_68(57910, 1500, 11780, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(20010, 0)
    SetCameraDistance(19010, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0xB,
        (
            "#11P#2100FWelcome back, guys! A job well done.\x02\x03",
            "The photos you brought are finally\x01",
            "developed and raring to go.\x02\x03",
            "#2102FLet's take a peek, shall we? ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0101F*gulp*\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_9B3E")
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    AnonymousTalk(
        0xB,
        (
            "#2100FAhh, the rustic landscape of\x01",
            "the Old Armorica Road.\x02\x03",
            "#2102FJust one glance fills me with tranquility!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    label("loc_9B3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_9BD8")
    Sound(18, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    AnonymousTalk(
        0xB,
        (
            "#2100FOh, this one's Armorica's flower garden.\x02\x03",
            "#2109FTheir delicious honey is to die for!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    label("loc_9BD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_9CCC")
    Sound(18, 0, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)

    AnonymousTalk(
        0xB,
        (
            "#2105FOh, wow. Are these the mysterious ruins hanging\x01",
            "over by the mouth of the Lupinus River?\x02\x03",
            "#2100FRemove the monsters from the equation,\x01",
            "and this would be THE ideal dating spot.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)

    label("loc_9CCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_9D83")
    Sound(18, 0, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)

    AnonymousTalk(
        0xB,
        (
            "#2105FWhat the heck? Where'd you even take this?\x02\x03",
            "#2102FI gotta say, the emptiness brings about a\x01",
            "soothing tranquility.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)

    label("loc_9D83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_9EAD")
    Sound(18, 0, 100, 0)
    OP_C9(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x4, 0x3)

    AnonymousTalk(
        0xB,
        (
            "#2109FAnd here's the money shot! It wouldn't be a\x01",
            "sightseeing tour guide without Mainz Mountain\x01",
            "Path's waterfall!\x02\x03",
            "#2100FIt truly is a sight to behold, isn't it?\x01",
            "I can't help but stare at it longingly\x01",
            "when I take the bus out to Mainz.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x4, 0x3)

    label("loc_9EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_9FC4")
    Sound(18, 0, 100, 0)
    OP_C9(0x7, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x7, 0x3)

    AnonymousTalk(
        0xB,
        (
            "#2102FOh, you even managed to snap a shot of the\x01",
            "railway! Is this the one near West Crossbell\x01",
            "Highway?\x02\x03",
            "#2109FI've seen my fair share of train fanatics out in\x01",
            "the city, so I'm glad we managed to get one\x01",
            "photo of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x7, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x7, 0x3)

    label("loc_9FC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_A0A8")
    Sound(18, 0, 100, 0)
    OP_C9(0x6, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x6, 0x3)

    AnonymousTalk(
        0xB,
        (
            "#2100FIs this...Stargazer's Tower?\x02\x03",
            "#2102FIt's not exactly the safest place to tread\x01",
            "through, but it's still a nice and quiet spot\x01",
            "away from the bustle of the city.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x6, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x6, 0x3)

    label("loc_A0A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_A1A3")
    Sound(18, 0, 100, 0)
    OP_C9(0x5, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x5, 0x3)

    AnonymousTalk(
        0xB,
        (
            "#2105FWhoa! Ruins?! You're telling me there's a place\x01",
            "like this on the Mainz Mountain Path?\x02\x03",
            "#2102FIt looks like some kind of ancient temple...\x01",
            "I can just feel the mystery oozing from it!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x5, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x5, 0x3)

    label("loc_A1A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_A2E0")
    Sound(18, 0, 100, 0)
    OP_C9(0x8, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x8, 0x3)

    AnonymousTalk(
        0xB,
        (
            "#2105FYou're kidding me! None of our records indicate\x01",
            "a ruin like this on the Ancient Battlefield!\x02\x03",
            "#2109FIt definitely gives me that Middle Ages fortress\x01",
            "vibe...\x02\03",
            "If we convinced bracers to guard the place,\x01",
            "it could be an outstanding tourist attraction!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x8, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x8, 0x3)

    label("loc_A2E0")


    ChrTalk(
        0xB,
        (
            "#11P#2109FUnbelievable! Each and every one of\x01",
            "them is flawless! Masterfully done, Elie!\x02\x03",
            "If I'm being totally honest, this is the kind of\x01",
            "work that puts professionals to shame!\x01",
            "Consider me impressed!\x02\x03",
            "#2106FI'd better start looking into a way to convince\x01",
            "Elie to replace Reins as our main photographer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0111FI-I think you're laying on the compliments\x01",
            "a little thick...\x02\x03",
            "#0100FI'm relieved you enjoyed them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0309FHaha! You hear that, Mademois-Elie?\x01",
            "'Masterfully done,' she says!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A60D")
    OP_2C(0x18, 0x3)

    ChrTalk(
        0xB,
        (
            "#11P#2100FNot only were the photos fantastic, but\x01",
            "you even managed to give me a double\x01",
            "helping. You guys are the best!\x02\x03",
            "I think we're totally set. ㈱\x02\x03",
            "#2109FAll that's left to do is to add a nifty\x01",
            "little introduction, and then it'll be\x01",
            "completely finished! All right!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x18, 0x1, 0xB)
    Jump("loc_A737")

    label("loc_A60D")


    ChrTalk(
        0xB,
        (
            "#11P#2100FReaching the quota will do wonders\x01",
            "for our progress, I assure you.\x02\x03",
            "Though we could still use a few more,\x01",
            "I'm sure Reins will be able to give me\x01",
            "a hand later.\x02\x03",
            "#2102FAll that's left to do is to add a nifty little\x01",
            "introduction, and then it'll be completely\x01",
            "finished! All right!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x18, 0x1, 0xC)

    label("loc_A737")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#12P#0000FI'm glad to hear that, Grace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2100FI see it was wise to trust in the eye of a\x01",
            "detective. You were able to track down all\x01",
            "these glorious spots like it was nothing!\x02\x03",
            "#2102FHeaven forbid I admit this, but a tour guide\x01",
            "written by you might even surpass my own!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FI hope you are not implying another request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2109FNo, no. Anyway, the SSS really saved\x01",
            "my skin! I'll keep you guys on speed-\x01",
            "dial for whenever I need you, 'kay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FYes, well...instead of that, just submit\x01",
            "another support request, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#2100FYeah, yeah. Thanks, everyone. ㈱\x02\x03",
            "#2109FWell, then. Duty calls, so I'll leave you be.\x02\x03",
            "Bye-bye! ♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5850, 1500, 940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18590, 0)
    SetChrPos(0x101, -4700, 0, 2100, 225)
    SetChrPos(0x102, -4700, 0, 800, 315)
    SetChrPos(0x103, -6000, 0, 800, 45)
    SetChrPos(0x104, -6000, 0, 2100, 135)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0006FMan, leave it to Grace to submit a request\x01",
            "that makes us work up a sweat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0104FTrue, but I hadn't held a camera in so long\x01",
            "that I sort of got a kick out of it.\x02\x03",
            "#0100FI actually don't mind doing requests like this\x01",
            "every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FHaha. You were definitely actin' like a kid\x01",
            "in a toy store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0206FOn the other hand, keeping up with Grace can\x01",
            "become exhausting after a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FHahaha... Yeah, you can say that again.\x02",
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
            "[The Many Famous Views of Crossbell]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -4930, 0, 1860, 90)
    SetChrPos(0x1, -4930, 0, 1860, 90)
    SetChrPos(0x2, -4930, 0, 1860, 90)
    SetChrPos(0x3, -4930, 0, 1860, 90)
    OP_29(0x18, 0x4, 0x10)
    SetScenarioFlags(0x0, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_95A9 end

    def Function_15_AD24(): pass

    label("Function_15_AD24")

    EventBegin(0x0)
    Fade(500)
    OP_68(6050, 1400, 53360, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19570, 0)
    SetChrPos(0x101, 5650, 0, 53610, 90)
    SetChrPos(0x102, 5650, 0, 54540, 90)
    SetChrPos(0x103, 4400, 0, 53610, 90)
    SetChrPos(0x104, 4400, 0, 54540, 90)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#5P#0100FThis is the certificate given to the journalist\x01",
            "awarded the Fulitzer Prize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FThe Fulitzer Prize... That is the award given to most\x01",
            "impactful journalist in a given year, if I remember\x01",
            "correctly.\x02\x03",
            "#0203F'Over the three-month period of the Hundred Days War,\x01",
            "this journalist was committed to delivering war\x01",
            "coverage rife with honesty and a sense of justice.'\x02\x03",
            "'In commemoration of this achievement, he is hereby\x01",
            "awarded the Fulitzer Prize. November S1192'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FRight... This should be the 'mark of a splendid\x01",
            "correspondent' Phantom Thief B mentioned.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, 6440, 0, 53840, 1000, 0x0)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A card is affixed to the back of the certificate of\x01",
            "commendation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x104,
        "#6P#0300FFound our lil' fella.\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 5650, 0, 53610, 1000, 0x0)

    def lambda_B0C8():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B0C8)

    def lambda_B0D5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B0D5)

    def lambda_B0E2():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B0E2)

    def lambda_B0EF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B0EF)
    Sleep(400)

    ChrTalk(
        0x101,
        "#12P#0005FLet's read our next clue.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　This is my final riddle.\x01",
            "　In this city of gray, visit the elegant\x01",
            "　abode of the elder who arbitrates!\x02",
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
        0x103,
        "#12P#0200F'Elegant abode of the elder who arbitrates'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0105F...\x01",
            "(I-It can't be...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5420, 0, 54040, 90)
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x22, 0x1, 0x6)
    SetScenarioFlags(0x0, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_AD24 end

    def Function_16_B2A5(): pass

    label("Function_16_B2A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2BB")
    Call(0, 15)
    Jump("loc_B3E9")

    label("loc_B2BB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Over the three-month period of the Hundred Days War,\x01",
            "this journalist was committed to delivering war\x01",
            "coverage rife with honesty and a sense of justice.\x02\x03",
            "In commemoration of this achievement, he is hereby\x01",
            "awarded the Fulitzer Prize.\x01",
            "November S1192\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)

    label("loc_B3E9")

    Return()

    # Function_16_B2A5 end

    def Function_17_B3EA(): pass

    label("Function_17_B3EA")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5A7")

    ChrTalk(
        0x8,
        "E-Excuse me!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B458():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B458)
    Sleep(50)

    def lambda_B468():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_B468)
    Sleep(50)

    def lambda_B478():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_B478)
    Sleep(50)

    def lambda_B488():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_B488)
    Sleep(50)

    def lambda_B498():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x4, 2, lambda_B498)
    Sleep(50)

    def lambda_B4A8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_B4A8)
    WaitChrThread(0x0, 2)
    Fade(1000)
    OP_68(-2860, 1510, 720, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "I'm sorry, but the editorial department is closed\x01",
            "to the general public for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please redirect any of your inquiries to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FOh, really? Our mistake.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_B5FA")

    label("loc_B5A7")


    ChrTalk(
        0x101,
        (
            "#0003FThey don't want us to go to the second floor,\x01",
            "so let's not bother them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5FA")

    Sleep(50)
    SetChrPos(0x0, -6370, 20, 2470, 180)
    EventEnd(0x4)
    Return()

    # Function_17_B3EA end

    SaveToFile()

Try(main)
