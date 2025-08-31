from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1340.bin",                # FileName
        "c1340",                    # MapName
        "c1340",                    # Location
        0x001D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 56000, 0, 14000, 0, 0, 1, 29, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1340",                  # 0
        "Mr. Crois",              # 1
        "Mariabell",              # 2
        "Company Director Baretta",# 3
        "Dolls",                  # 4
        "Dolls",                  # 5
    ))

    AddCharChip((
        "chr/ch05600.itc",                   # 00
        "chr/ch05500.itc",                   # 01
        "chr/ch05602.itc",                   # 02
        "chr/ch05502.itc",                   # 03
        "chr/ch27400.itc",                   # 04
        "apl/ch50093.itc",                   # 05
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(172360,  800,     120099,  0,    374,  0x0, 1,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(172360,  800,     120800,  0,    374,  0x0, 2,   5,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(53000,   0,       45800,   1500,    53000,   1000,    45800,   0x007C, 0,  17, 0x0000)
    DeclActor(55000,   150,     128800,  2500,    55000,   1800,    128800,  0x007E, 0,  4,  0x0000)
    DeclActor(55660,   0,       38920,   1200,    55660,   1000,    38920,   0x007C, 0,  22, 0x0000)
    DeclActor(172500,  0,       121000,  1200,    172500,  1500,    121000,  0x007C, 0,  23, 0x0000)
    DeclActor(172500,  0,       120000,  1200,    172500,  1500,    120250,  0x007C, 0,  23, 0x0000)

    ScpFunction((
        "Function_0_24C",          # 00, 0
        "Function_1_304",          # 01, 1
        "Function_2_59D",          # 02, 2
        "Function_3_5A4",          # 03, 3
        "Function_4_712",          # 04, 4
        "Function_5_716",          # 05, 5
        "Function_6_1255",         # 06, 6
        "Function_7_25E9",         # 07, 7
        "Function_8_2DC2",         # 08, 8
        "Function_9_2DE1",         # 09, 9
        "Function_10_2E03",        # 0A, 10
        "Function_11_2E22",        # 0B, 11
        "Function_12_2E3A",        # 0C, 12
        "Function_13_2E59",        # 0D, 13
        "Function_14_2E78",        # 0E, 14
        "Function_15_2E93",        # 0F, 15
        "Function_16_317C",        # 10, 16
        "Function_17_3715",        # 11, 17
        "Function_18_97EB",        # 12, 18
        "Function_19_98BB",        # 13, 19
        "Function_20_993F",        # 14, 20
        "Function_21_A65A",        # 15, 21
        "Function_22_A697",        # 16, 22
        "Function_23_A8E5",        # 17, 23
    ))


    def Function_0_24C(): pass

    label("Function_0_24C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_28C"),
        (1, "loc_298"),
        (2, "loc_2A4"),
        (3, "loc_2B0"),
        (4, "loc_2BC"),
        (5, "loc_2C8"),
        (6, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2E0"),
    )


    label("loc_28C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_298")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_303")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_303")

    Return()

    # Function_0_24C end

    def Function_1_304(): pass

    label("Function_1_304")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31C")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 2)

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32D")
    Event(0, 16)

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_33B")
    Jump("loc_59C")

    label("loc_33B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_36F")
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 53490, 30, 125950, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_59C")

    label("loc_36F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A3")
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 53490, 30, 125950, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_59C")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3B1")
    Jump("loc_59C")

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_40A")
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 55790, 30, 125880, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 53480, 30, 125770, 90)
    Jump("loc_59C")

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_465")
    ClearChrFlags(0x8, 0x8)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 55790, 30, 125880, 340)
    Jump("loc_59C")

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4E1")
    ClearChrFlags(0x8, 0x8)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 55790, 30, 125880, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 53480, 30, 125770, 90)
    Jump("loc_59C")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4EF")
    Jump("loc_59C")

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_56D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_52C")
    ClearChrFlags(0x8, 0x8)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 55000, 150, 128800, 180)

    label("loc_52C")

    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 167200, 0, 128330, 270)
    Jump("loc_59C")

    label("loc_56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_59C")
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 170830, 0, 120150, 90)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_59C")

    Return()

    # Function_1_304 end

    def Function_2_59D(): pass

    label("Function_2_59D")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_59D end

    def Function_3_5A4(): pass

    label("Function_3_5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BB")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D7")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_5D7")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5E9")
    Jump("loc_67A")

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5F7")
    Jump("loc_67A")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_605")
    Jump("loc_67A")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_613")
    Jump("loc_67A")

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_621")
    Jump("loc_67A")

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_62F")
    Jump("loc_67A")

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_641")
    OP_66(0x1, 0x1)
    Jump("loc_67A")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_653")
    OP_66(0x1, 0x1)
    Jump("loc_67A")

    label("loc_653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_661")
    Jump("loc_67A")

    label("loc_661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_67A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_67A")
    OP_66(0x1, 0x1)

    label("loc_67A")

    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_6EF")

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6EF")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_6EF")

    label("loc_6EF")

    SetMapObjFlags(0x1, 0x10)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_711")
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x2, 0x1)

    label("loc_711")

    Return()

    # Function_3_5A4 end

    def Function_4_712(): pass

    label("Function_4_712")

    Call(0, 5)
    Return()

    # Function_4_712 end

    def Function_5_716(): pass

    label("Function_5_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_808")
    TalkBegin(0x8)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "#2803FYeah. I'll leave the rest to you and Mariabell.\x02\x03",
            "#2800FWould you look at the time? I'm going to\x01",
            "be late to dinner with the mayor.\x01",
            "I'm sorry, but I must take my leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, sir! You can count on us!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    TalkEnd(0x8)
    Jump("loc_1254")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C24")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A5")
    Jump("loc_8EF")

    label("loc_8A5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8C5")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8EF")

    label("loc_8C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E5")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8EF")

    label("loc_8E5")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8EF")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A18")

    ChrTalk(
        0x8,
        (
            "#2800FThe fact of the matter is, I'm leaving on a\x01",
            "business trip this afternoon.\x02\x03",
            "I must finish any remaining work I have\x01",
            "here while I still have the time.\x02\x03",
            "#2806FAs you might expect, I've had nothing but\x01",
            "meetings all day. I'm tired of them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C18")

    label("loc_A18")


    ChrTalk(
        0x8,
        "#2800FHello, ladies and gentlemen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FSorry to interrupt you while you're\x01",
            "in the middle of working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2800FIt's okay. I've nothing but meetings all day.\x02\x03",
            "#2806FCrossbellan blood runs through my veins,\x01",
            "so naturally, I would have liked to have\x01",
            "gone to the parade. But, alas...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2804FRelax, my friend. I was merely joking.\x02\x03",
            "#2800FI hope you all continue striving to work\x01",
            "to the best of your abilities. I know I'll\x01",
            "be doing so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWe definitely will. Thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C18")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Jump("loc_1254")

    label("loc_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1254")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC1")
    Jump("loc_D0B")

    label("loc_CC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE1")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D0B")

    label("loc_CE1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D01")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D0B")

    label("loc_D01")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D0B")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B0")

    ChrTalk(
        0x8,
        (
            "#2800FWhy, hello there, ladies and gentlemen.\x01",
            "How is work treating everybody?\x02\x03",
            "#2809FHahaha. Don't hesitate to stop by my office\x01",
            "if you ever need any advice. When I'm here,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FMan, what a nice guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FI couldn't possibly impose on you while you're\x01",
            "already busy with the Anniversary Festival, Uncle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2804FHaha, quite true. I'm especially occupied thanks\x01",
            "to these conferences and parties as of late, but...\x02\x03",
            "#2800FMy door will always be open to you. If you're\x01",
            "feeling up to the task, would all of you like to\x01",
            "attend a conference with me tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FS-Sir, that would be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206FWe appreciate the offer, but we will have\x01",
            "to decline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2806FOh, is that so? That's too bad.\x02\x03",
            "#2809FHaha, don't worry about having an appointment.\x01",
            "I hope you give my offer some thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(Uncle's uniqueness never fails to impress me.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_124D")

    label("loc_10B0")


    ChrTalk(
        0x8,
        (
            "#2803FI may be incredibly busy through this period\x01",
            "of festivities...\x02\x03",
            "#2800FHowever, I would gladly make time for you.\x01",
            "Don't be concerned about imposing yourselves.\x01",
            "You don't need an appointment to come see me.\x02\x03",
            "#2800FThat being said... I'm sure your work during the\x01",
            "Anniversary Festival will be increasingly difficult.\x02\x03",
            "I hope you continue striving for excellence,\x01",
            "as long as you don't overwork yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124D")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)

    label("loc_1254")

    Return()

    # Function_5_716 end

    def Function_6_1255(): pass

    label("Function_6_1255")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1277")
    Call(0, 20)
    Return()

    label("loc_1277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_13D5")
    TalkBegin(0xFE)

    ChrTalk(
        0x9,
        (
            "#2900FCarla turned to her maid and said they\x01",
            "were off to go sightseeing in Grancel.\x02\x03",
            "#2903FIf her intention was to run away from home, why\x01",
            "would she boldly state that in front of me?\x02\x03",
            "#2900FWell, I'm as busy as I always am,\x01",
            "so I paid no mind to her words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FS-Sorry, it sounds like we interrupted\x01",
            "you at a bad time.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_25E8")

    label("loc_13D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_16B3")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1515")

    ChrTalk(
        0x9,
        (
            "#2901FWell, regardless...\x01",
            "I must ask. What exactly is Speaker Hartmann\x01",
            "trying to do?\x02\x03",
            "#2903FThose colleagues of his left a colossal mess\x01",
            "at the harbor, and yet they haven't made\x01",
            "another move.\x02\x03",
            "#2910FHe may be attending the diet session as he\x01",
            "should be, but he's acting far too carelessly!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AB")

    label("loc_1515")


    ChrTalk(
        0x9,
        (
            "#2906F*sigh* It's a relief to see that the raid didn't\x01",
            "take a toll on the value of our stock.\x02\x03",
            "#2903FHowever, there's no telling what adverse effects\x01",
            "their conflict will have on the economy and\x01",
            "trading if it rages on like it has been.\x02\x03",
            "#2901FListen. I'm going to need my cute, little police\x01",
            "pups to kick it into high gear. Got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FO-Of course, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0104FWe'll do our best, Bell.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_16AB")

    TalkEnd(0xFE)
    Jump("loc_25E8")

    label("loc_16B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_19EA")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_175A")

    ChrTalk(
        0x9,
        (
            "#2903FGive me a break! How dare this nuisance\x01",
            "occur while Father is away?\x02\x03",
            "#2910FI am utterly dumbfounded by Revache's\x01",
            "thought process!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E2")

    label("loc_175A")


    ChrTalk(
        0x9,
        (
            "#2910FHonestly, those imbeciles!\x01",
            "Is there a single brain cell amongst any of them?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FCalm down, Mariabell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FI take it you've already heard\x01",
            "about the situation, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2901FWell, obviously!\x01",
            "It only happened within earshot of here!\x02\x03",
            "#2903FHow DARE those barbarians have a\x01",
            "firefight this close to IBC headquarters?!\x02\x03",
            "#2910FCurse you, Revache! There'll be hell to\x01",
            "pay if this affects stock prices!\x02",
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
        "#0006FIs that right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FWell, considering the position you're in,\x01",
            "I can hardly blame you for being worried.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_19E2")

    TalkEnd(0xFE)
    Jump("loc_25E8")

    label("loc_19EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1DD2")
    TalkBegin(0xFE)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B1B")

    ChrTalk(
        0xA,
        (
            "That reminds me, ma'am. Negotiations begin\x01",
            "this afternoon, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2904FYes, I'll take care of the negotiations.\x02\x03",
            "#2900FI have some personal business to take care of\x01",
            "in the evening, so I'll leave the rest in your\x01",
            "capable hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, ma'am. I won't disappoint.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DC6")

    label("loc_1B1B")


    ChrTalk(
        0x9,
        (
            "#2904FOh, right. I'll see to these documents personally.\x02\x03",
            "#2900FHandle the reports for the bank and the\x01",
            "investment division if you could, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Okay. I'll have them ready to present\x01",
            "at the next board meeting.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#2905FOh, are you looking for my father? I'm afraid he's\x01",
            "out on another business trip.\x02\x03",
            "#2906FOf course, he dumped the remainder of his\x01",
            "work onto me. A splendid performance as\x01",
            "always, Father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FDoes he normally do that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2900FYes. One of his most...unique talents is to\x01",
            "delegate his work onto others.\x02\x03",
            "#2906FIt's practically become second nature for me\x01",
            "to take care of it, at this point.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0x0, 0x0, 0x41EB0, 0x0, 0x0)
    SetScenarioFlags(0x0, 1)

    label("loc_1DC6")

    OP_4C(0xA, 0xFF)
    TalkEnd(0xFE)
    Jump("loc_25E8")

    label("loc_1DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1F99")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1EA8")
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "#2900FAnd on that note, I'm currently taking charge\x01",
            "of his businesses, as well.\x02\x03",
            "May I count on you to complete\x01",
            "that report, Baretta?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, ma'am. I'll begin immediately.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_1F91")

    label("loc_1EA8")


    ChrTalk(
        0x9,
        (
            "#2900FThe IBC always manages at least\x01",
            "twenty different companies.\x02\x03",
            "These are just the business proposals\x01",
            "and reports...\x02\x03",
            "#2906F*sigh* Even with Father's support, it's no\x01",
            "easy task to run this place.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0x0, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_1F91")

    TalkEnd(0xFE)
    Jump("loc_25E8")

    label("loc_1F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_24E2")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2036")
    Jump("loc_2080")

    label("loc_2036")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2056")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2080")

    label("loc_2056")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2076")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2080")

    label("loc_2076")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2080")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2239")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2140")

    ChrTalk(
        0x9,
        (
            "#2904FFather has finally returned.\x02\x03",
            "#2902FCould you come by later in the evening, Elie?\x01",
            "That would be enough to satisfy me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_2140")


    ChrTalk(
        0x9,
        (
            "#2904FThis is nothing more than a casual party, so\x01",
            "only my friends will be in attendance.\x02\x03",
            "#2902FCould you come by later in the evening, Elie?\x01",
            "That would be enough to satisfy me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F8")


    ChrTalk(
        0x102,
        (
            "#0102FHmm... I'll see what I can do, but,\x01",
            "no promises.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D6")

    label("loc_2239")


    ChrTalk(
        0x9,
        (
            "#2909FOh, Elie! Will you be attending\x01",
            "my party?\x02\x03",
            "#2902FIt may be early in the day, but I assure\x01",
            "you it'll be a fantastic time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FDidn't I just accompany you to yesterday's\x01",
            "celebration, Bell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2905FThat may be so, but this is far more casual.\x01",
            "Only my friends will be in attendance.\x02\x03",
            "#2901FHow will I survive if you're not there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FI hate to rain on your parade, but we're\x01",
            "in the middle of working right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2904FI wasn't asking you. Elie can stay here\x01",
            "while you finish in her stead.\x02",
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
        "#0309F(Never fails to be the queen bee, eh?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_24D6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_25E8")

    label("loc_24E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_END)), "loc_25E5")
    TalkBegin(0xFE)

    ChrTalk(
        0x9,
        (
            "#2904FOh, by the way. If you manage to solve\x01",
            "the case you're working on, do notify me.\x02\x03",
            "#2902FI'm interested to see the conclusion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FS-Sure. If we manage to solve the case,\x01",
            "that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI'll be back again soon, Bell.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_25E8")

    label("loc_25E5")

    Call(0, 7)

    label("loc_25E8")

    Return()

    # Function_6_1255 end

    def Function_7_25E9(): pass

    label("Function_7_25E9")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(169000, 1500, 120150, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(200, 0)
    SetCameraDistance(36080, 0)
    SetChrPos(0x101, 169000, 0, 119650, 90)
    SetChrPos(0x102, 168750, 0, 120650, 90)
    SetChrPos(0x103, 167500, 0, 119650, 90)
    SetChrPos(0x104, 167250, 0, 120650, 90)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_93(0x9, 0x10E, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#2902F#11PWelcome to my private room, everyone.\x02\x03",
            "#2904FEveryone but that shameless mutt of yours\x01",
            "is welcome here any time.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0006F#6P(Looks like she's not losing the stink eye\x01",
            "any time soon...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F#6PCan't say I'm surprised a queen like yourself\x01",
            "has their room decked out with fancy-lookin' art.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205F#6PI believe these are all the works of many\x01",
            "famous artists.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 1, 0, 8)
    BeginChrThread(0x104, 1, 0, 9)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_68(170830, 1400, 120150, 1500)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005F#6PHuh?!\x02\x03",
            "#0001FUm... Excuse me, but what are those\x01",
            "things hiding in the back there?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x102, 0xB4, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#0109F#5PThose are Rosenberg Studio dolls, Lloyd.\x02\x03",
            "#0102FThey almost look like they're alive, don't they?\x01",
            "Bell's a bit of a Rosenberg connoisseur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2904F#11PI especially love these precious\x01",
            "little darlings.\x02\x03",
            "#2902FWould you like to give them a\x01",
            "close examination?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F#6PAre you okay with that?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 1, 0, 10)
    BeginChrThread(0x101, 1, 0, 11)
    BeginChrThread(0x102, 1, 0, 12)
    BeginChrThread(0x103, 1, 0, 13)
    BeginChrThread(0x104, 1, 0, 14)
    Sleep(1000)
    OP_68(171960, 1400, 119960, 2500)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x103,
        (
            "#0202F#6PThis is my first time experiencing a Rosenberg doll\x01",
            "up close. The details on the skin are immaculate.\x01",
            "I have never seen such a lifelike doll before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0302F#6PFor real. The thing is absurd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002F#6PWow, this is incredible.\x02\x03",
            "#0004FI've heard they cost a fortune,\x01",
            "but I have to admit...\x01",
            "The quality speaks for itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2904F#11PI don't mind if you touch them, either.\x02\x03",
            "#2902FHowever, I'll see to it that you repay me in full\x01",
            "if they're damaged. Do I make myself clear?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x102, 0xB4, 0x1F4)

    ChrTalk(
        0x102,
        "#0106F#5PBell...\x02",
    )

    CloseMessageWindow()

    def lambda_2CCC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CCC)
    Sleep(50)

    def lambda_2CDC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CDC)
    Sleep(60)

    def lambda_2CEC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CEC)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#0012F#5PPlease tone down the scary threats.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F#5PI am too terrified to consider touching it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2909F#11PHeehee. I was only kidding, dear!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 168730, 0, 120050, 90)
    SetChrPos(0x9, 170830, 0, 120150, 90)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0xB8, 3)
    EventEnd(0x5)
    Return()

    # Function_7_25E9 end

    def Function_8_2DC2(): pass

    label("Function_8_2DC2")

    OP_93(0x103, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(500)
    Return()

    # Function_8_2DC2 end

    def Function_9_2DE1(): pass

    label("Function_9_2DE1")

    Sleep(300)
    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x104, 0x5A, 0x1F4)
    Sleep(500)
    Return()

    # Function_9_2DE1 end

    def Function_10_2E03(): pass

    label("Function_10_2E03")

    OP_95(0x9, 171500, 0, 118600, 2000, 0x0)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(500)
    Return()

    # Function_10_2E03 end

    def Function_11_2E22(): pass

    label("Function_11_2E22")

    Sleep(500)
    OP_95(0x101, 170930, 0, 119600, 2000, 0x0)
    Return()

    # Function_11_2E22 end

    def Function_12_2E3A(): pass

    label("Function_12_2E3A")

    Sleep(600)
    OP_95(0x102, 171100, 0, 121670, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_12_2E3A end

    def Function_13_2E59(): pass

    label("Function_13_2E59")

    Sleep(800)
    OP_95(0x103, 171000, 0, 120710, 2000, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_13_2E59 end

    def Function_14_2E78(): pass

    label("Function_14_2E78")

    Sleep(1000)
    OP_95(0x104, 170010, 0, 121040, 2000, 0x0)
    Sleep(500)
    Return()

    # Function_14_2E78 end

    def Function_15_2E93(): pass

    label("Function_15_2E93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2F40")

    ChrTalk(
        0xFE,
        (
            "As the board of directors, we're obliged to\x01",
            "manage the company in the CEO's absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'd like to apologize to Mariabell for\x01",
            "having burdened her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3178")

    label("loc_2F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2FD0")

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival has the CEO\x01",
            "busier than ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We must offer any support we can give\x01",
            "during this hectic period.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3178")

    label("loc_2FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3079")

    ChrTalk(
        0xFE,
        "Right, here are the reference materials for more details.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The investment division is indicated to\x01",
            "have an extremely high growth rate...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3178")

    label("loc_3079")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Excuse me, but how did you get past\x01",
            "security?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, you're Elie's coworkers,\x01",
            "aren't you? My apologies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However...we are in the middle of a meeting,\x01",
            "so I would appreciate it if you kept quiet.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xA, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_3178")

    TalkEnd(0xFE)
    Return()

    # Function_15_2E93 end

    def Function_16_317C(): pass

    label("Function_16_317C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(55500, 1000, 14000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 57500, 0, 13700, 270)
    SetChrPos(0x102, 57500, 0, 14400, 270)
    SetChrPos(0x103, 57500, 0, 14400, 270)
    SetChrPos(0x104, 57500, 0, 13700, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)

    def lambda_3255():
        OP_96(0xFE, 0xCF08, 0x0, 0x396C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3255)

    def lambda_326F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_326F)
    Sleep(450)

    def lambda_3283():
        OP_96(0xFE, 0xCF08, 0x0, 0x3458, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3283)

    def lambda_329D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_329D)
    Sleep(450)

    def lambda_32B1():
        OP_96(0xFE, 0xD3B8, 0x0, 0x396C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_32B1)

    def lambda_32CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_32CB)
    Sleep(450)

    def lambda_32DF():
        OP_96(0xFE, 0xD3B8, 0x0, 0x3458, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_32DF)

    def lambda_32F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_32F9)
    WaitChrThread(0x102, 1)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)
    Sleep(100)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3366():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3366)
    Sleep(50)

    def lambda_3376():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3376)

    ChrTalk(
        0x101,
        "#2200347V#0005F#5PWow...\x02",
    )

    CloseMessageWindow()
    OP_68(60000, 1000, 4300, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_33BB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_33BB)
    Sleep(100)

    def lambda_33CB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_33CB)
    OP_6F(0x11)
    Sleep(300)
    Fade(1000)
    OP_68(62400, 1200, 0, 0)
    MoveCamera(110, 10, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 54500, 0, 6300, 135)
    SetChrPos(0x102, 54500, 0, 8200, 135)
    SetChrPos(0x103, 53500, 0, 7400, 135)
    SetChrPos(0x104, 55500, 0, 7200, 135)
    OP_68(60000, 1200, 3800, 8000)
    MoveCamera(90, 10, 0, 8000)
    SetCameraDistance(23500, 8000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#2200348V#0002F#5PThis view is amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200349V#0302FPhew. Bet this place cost 'em a mountain\x01",
            "of mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200350V#0204FI have visited the Epstein Foundation's office\x01",
            "in this building, but it hardly compares...\x02\x03",
            "#2200351V#0202FThe view from this floor is exceptional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200352V#0102FI absolutely agree.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(54500, 1100, 7200, 0)
    MoveCamera(76, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    OP_0D()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2200353V#0100F#5PThe CEO's office is at the end of the hallway.\x02\x03",
            "#2200354VI think it'd be rude of us to keep him waiting\x01",
            "after he agreed to meet on such short notice.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_36AC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36AC)
    Sleep(50)

    def lambda_36BC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_36BC)
    Sleep(50)
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x101,
        "#2200355V#11P#0000FGood call.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 53200, 0, 6700, 0)
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    SetScenarioFlags(0x82, 4)
    EventEnd(0x5)
    Return()

    # Function_16_317C end

    def Function_17_3715(): pass

    label("Function_17_3715")

    EventBegin(0x0)
    Fade(1000)
    OP_68(52500, 1000, 45000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 51800, 0, 43000, 0)
    SetChrPos(0x102, 52500, 0, 44400, 0)
    SetChrPos(0x103, 52800, 0, 43000, 0)
    SetChrPos(0x104, 53800, 0, 43000, 0)
    OP_0D()

    def lambda_3794():
        OP_95(0xFE, 52500, 0, 44900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3794)
    WaitChrThread(0x102, 1)
    Sleep(300)
    Sound(811, 0, 100, 0)
    Sleep(800)

    ChrTalk(
        0x102,
        "#2200356V#11P#0102FUncle Dieter? It's Elie.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 52500, 0, 47500, 0)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    NpcTalk(
        0x8,
        "Man's Voice",
        "#2200357V#5P#2SOh! Come in, come in!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200358V#11P#0104FThank you, sir.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    Sleep(300)

    def lambda_388F():
        OP_95(0xFE, 52500, 0, 45900, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_388F)
    OP_0D()
    EndChrThread(0x102, 0x1)
    OP_70(0x2, 0x0)
    SetMapObjFlags(0x2, 0x10)
    LoadChrToIndex("apl/ch50217.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02900.itp")
    OP_68(55000, 1000, 128199, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(19500, 0)
    ClearChrFlags(0x8, 0x8)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    SetChrPos(0x101, 54100, 0, 116900, 0)
    SetChrPos(0x102, 55000, 0, 118300, 0)
    SetChrPos(0x103, 55000, 0, 116900, 0)
    SetChrPos(0x104, 55900, 0, 116900, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetCameraDistance(14500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)
    Fade(1000)
    OP_68(55000, 1100, 128800, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(55000, 1100, 127000, 4000)

    def lambda_3A67():
        OP_95(0xFE, 55000, 0, 125300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A67)
    Sleep(300)

    def lambda_3A84():
        OP_95(0xFE, 54100, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A84)
    Sleep(200)

    def lambda_3AA1():
        OP_95(0xFE, 55900, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AA1)
    Sleep(200)

    def lambda_3ABE():
        OP_95(0xFE, 55000, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3ABE)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)

    NpcTalk(
        0x8,
        "Man in Suit",
        (
            "#2200359V#5P#2800FElie! It's been far too long!\x02\x03",
            "#2200360VClose to half a year, if I remember correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200361V#12P#0109FThat sounds about right. But more importantly,\x01",
            "I'm glad to see you're doing well, Uncle Dieter.\x02\x03",
            "#2200362V#0100FMy apologies for not having scheduled a proper\x01",
            "appointment with you.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man in Suit",
        (
            "#2200363V#5P#2804FDon't talk as though we're strangers!\x01",
            "Please, relax.\x02\x03",
            "#2200364V#2800FYou're my little girl's best friend, and the\x01",
            "daughter of my own good friend as well.\x01",
            "Surely you haven't forgotten.\x02\x03",
            "#2200365VYou are nothing short of family at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200366V#12P#0104FThank you, Uncle.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man in Suit",
        (
            "#2200367V#5P#2800FThink nothing of it. Now, I've heard from my dear,\x01",
            "beloved daughter that you've joined the CPD.\x02\x03",
            "#2200368VWould these be your fellow officers, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200369V#12P#0100FThey are, indeed. We're all part of the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    def lambda_3E87():
        OP_96(0xFE, 0xDC50, 0x0, 0x1EC30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E87)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x101,
        (
            "#2200370V#12P#0004FNice to meet you, sir. My name is\x01",
            "Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200371V#4P#0300FAnd I'm Randy Orlando.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200372V#4P#0204FTio Plato. How do you do?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man in Suit",
        (
            "#2200373V#5P#2804FIt's nice to finally meet the three of you.\x01",
            "I've read all about you in the Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("Man in Suit")

    AnonymousTalk(
        0xFF,
        (
            "#2200374VI am Dieter Crois, CEO of the\x01",
            "International Bank of Crossbell.\x02\x03",
            "#2200375VLloyd, Randy, and Tio, you said?\x02\x03",
            "#2200376VWe're all friends here, so I would\x01",
            "appreciate it if you were at ease\x01",
            "around me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x8, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(860, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#2200407V#12P#0012FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200378V#12P#0205F(Were his teeth gleaming just now?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200379V#12P#0309F(This old dude's a breath of fresh air, eh?)\x02",
    )

    CloseMessageWindow()
    OP_64(0x8)
    Sleep(500)
    SetChrSubChip(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#2200380V#5P#2801FAnyway, shall we get down to business? I believe\x01",
            "you're here to ask me a few questions.\x02\x03",
            "#2200381V#2800FMay I ask what they concern?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2200382V#0103FRight. The thing is...\x02\x03",
            "#2200383V#0101F...we're trying to uncover the truth behind\x01",
            "our current investigation. And as of now...\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6F(0x10)
    OP_68(55180, 1100, 127250, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 54100, 0, 125600, 0)
    SetChrPos(0x102, 55200, 0, 125800, 0)
    SetChrPos(0x103, 54600, 0, 124400, 0)
    SetChrPos(0x104, 55700, 0, 124600, 0)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(19000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x8,
        (
            "#2200384V#5P#2803FI think I understand your predicament.\x02\x03",
            "#2200385V#2801FThis Yin fellow sent an orbmail from the\x01",
            "IBC to your office, did he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200386V#0106FCorrect...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200387V#12P#0203FWe suspect it was sent from the IBC's main\x01",
            "terminal.\x02\x03",
            "#2200388V#0200FThere is a strong possibility Yin took control\x01",
            "of the terminal in order to do just that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200389V#5P#2803FI see, I see...\x02\x03",
            "#2200390VTo be perfectly honest, I have the utmost\x01",
            "confidence in our building's security.\x02\x03",
            "#2200391V#2801FEven more so when it comes to the floor the\x01",
            "main terminal is on. Only a few authorized\x01",
            "individuals can access it as is.\x02\x03",
            "#2200392VFurthermore, you must have the proper\x01",
            "authentication to operate the terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200393V#12P#0001FI know this may be rude of me to ask, but have\x01",
            "any employees with the proper clearance been\x01",
            "acting suspiciously recently?\x02\x03",
            "#2200394VPerhaps a recent hire, or somebody who's been\x01",
            "acting out of the ordinary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200395V#5P#2803FHmm... Not that I can think of. To be frank, there\x01",
            "isn't a single employee I don't trust.\x02\x03",
            "#2200396V#2800F...But that brings me to another thought, Lloyd.\x02\x03",
            "#2200397VHave you not explored any other avenues?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200519V#12P#0005FOthers? Like what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200399V#5P#2804FHmm, let's see... Okay, for example...\x02\x03",
            "#2200400V#2800F...what if I was pretending to be this Yin\x01",
            "character, and I sent you the message?\x02",
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#2200401V#12P#4S#0011FWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200402V#0307FYou're joking, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200403V#0105FY-You must be! That can't be true!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200404V#5P#2809FHah! Calm down, everyone. It was purely\x01",
            "hypothetical, of course.\x02\x03",
            "#2200405V#2800FCould you imagine the headlines if I had\x01",
            "revealed that I was, in fact, a legendary\x01",
            "assassin?\x02\x03",
            "#2200406VThis goes without saying, but reality is\x01",
            "hardly ever that outlandish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200377V#12P#0012FR-Right... Of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200408V#0106FUncle, I would appreciate it if you didn't scare\x01",
            "us like that, even hypothetically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200409V#12P#0203FQuite the practical joker, is he not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200410V#5P#2809FHahaha! I apologize. That was crude of me.\x02\x03",
            "#2200411V#2803FHowever, I would give things a second glance.\x02\x03",
            "#2200412V#2801FIf one of my employees was truly responsible\x01",
            "for sending you the orbmail...\x02\x03",
            "#2200413V...would I not essentially be implicated in that\x01",
            "crime?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#2200574V#0101FI...suppose so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200415V#12P#0205FThat is certainly one way to look at it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200416V#0301FSo, you're tellin' us not to consider any IBC\x01",
            "workers as the suspect?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#2200417V#5P#0001FHey, Tio.\x02\x03",
            "#2200418VThat transmission between the IBC and SSS\x01",
            "terminals...\x02\x03",
            "#2200419VWould it be possible to mask the location it was\x01",
            "sent from?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F44():
        OP_93(0xFE, 0xBE, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4F44)

    def lambda_4F51():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4F51)

    ChrTalk(
        0x103,
        (
            "#2200420V#12P#0203FAn interesting question.\x02\x03",
            "#2200421V#0200FIt IS possible that the IBC's main terminal was\x01",
            "hacked from an external source.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200422V#5P#0005F'Hacked'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200423V#0305FThe hell does that mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200424V#5P#0106FI don't fully understand it myself...\x02\x03",
            "#2200425V#0100F...but I believe it's a technique used for the\x01",
            "unauthorized operation of a terminal, primarily\x01",
            "by breaching one's security system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200426V#12P#0204FThat would be the core of it, yes.\x02\x03",
            "#2200427VAny terminal connected to the orbal network can,\x01",
            "theoretically, be accessed by another terminal.\x02\x03",
            "#2200428V#0200FYou would need to be unbelievably talented\x01",
            "and familiar with the technology, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200429V#5P#2803FPeople capable of accessing terminals through\x01",
            "such means are known as hackers.\x02\x03",
            "#2200430V#2801FThe orbal network is still in its testing phase, so\x01",
            "there are a limited number of places that have\x01",
            "access to terminals.\x02\x03",
            "#2200431VBut despite these limitations, we have already\x01",
            "begun to encounter security issues.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5366():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5366)
    Sleep(100)

    def lambda_5376():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5376)
    Sleep(100)

    def lambda_5386():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5386)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#2200432V#12P#0001FInteresting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200433V#0303FSo, you're tellin' me...\x02\x03",
            "#2200434V#0301F...not only is this Yin guy some crazy assassin,\x01",
            "but he's also an orbal whiz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200435V#0106F#5PI don't think we should jump to conclusions.\x02\x03",
            "#2200436V#0101FThough, we should consider the possibility\x01",
            "that the orbmail was sent from elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200437V#5P#2803FWell, I truly hope the situation is resolved without\x01",
            "having to doubt my loyal employees.\x02\x03",
            "#2200438V#2801FMore importantly, it poses a serious problem if the\x01",
            "main terminal has been hacked.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#2200439V#5P#2804FAh, I have an idea.\x02\x03",
            "#2200440V#2800FWould you like to enter the terminal room and\x01",
            "investigate it for yourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200468V#12P#0005FSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200442V#0105FA-Are you sure that's okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200443V#5P#2800FOf course! You may be able to find evidence\x01",
            "of hacking if you examine the terminal itself.\x02\x03",
            "#2200444VI'll have the staff down there assist you, in\x01",
            "case you have any questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200445V#12P#0002FThat would be incredibly helpful, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200446V#0104FThank you, Uncle. We really appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200447V#5P#2804FMy pleasure. This is an issue that I, too, should\x01",
            "find an answer to, no?\x02\x03",
            "#2200448V#2800FHaha. And I must say, Elie...\x02\x03",
            "#2200449VI get the impression you've been living quite\x01",
            "the fulfilling life these days. Or am I mistaken?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200450V#0105FPardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200451V#5P#2804FI had my reservations when I first heard\x01",
            "that you decided to join the CPD.\x02\x03",
            "#2200452VHowever, I now understand just how valuable\x01",
            "your experiences have been for you.\x02\x03",
            "#2200453V#2800FPlease, allow me to aid you in any way I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200454V#0102FUncle Dieter...\x02\x03",
            "#2200455V#0104FIt's reassuring to hear that from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200456V#5P#2804FI'm glad. Oh, one more thing...\x02\x03",
            "#2200457V#2800FI see great potential in the four of you, now that\x01",
            "we've spoken face-to-face.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        "#2200458V#12P#0005FReally? Why's that?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 56000, 0, 128900, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7001", 0)
    OP_68(56450, 900, 129560, 2500)
    MoveCamera(47, 13, 0, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_5B91():
        OP_95(0xFE, 56000, 0, 131100, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5B91)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#2200459V#2803F#11PI'm sure you have realized this already, but Crossbell\x01",
            "is plagued with a rather...unique set of problems.\x02\x03",
            "#2200460VAnd I'm sure Elie is painfully aware of this as well.\x02\x03",
            "#2200461V#2801FI believe that the most significant problem we face\x01",
            "as a society is that justice has lost all substance.\x01",
            "It has become a shadow of its former self.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2200462V#12P#0001FWhat do you mean, sir? How is that possible?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200463V#0101FCould you elaborate, please?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200464V#2801F#11PThe idea, the very concept of justice, has become\x01",
            "nothing more than an empty vessel. Lip service,\x01",
            "if you will.\x02\x03",
            "#2200465V#2803FEveryone has their own perspective, of course.\x01",
            "There are some that believe justice is dead.\x02\x03",
            "#2200466V#2804FWhatever their opinions are of the present,\x01",
            "one truth remains.\x02\x03",
            "#2200467V#2800FHumans have ever been in pursuit of justice. That is\x01",
            "what drives us forward--gives us the will to move on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200441V#12P#0005F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200469V#12P#0205FIs that really so important?\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x190)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#2200470V#2804F#5PJustice is the foundation of a trustworthy society.\x02\x03",
            "#2200471V#2800FIf criminals were not bound by that justice we call\x01",
            "law...\x02\x03",
            "#2200472V...people would isolate themselves in the safety of\x01",
            "their own homes, never to venture out into what\x01",
            "they see as a dangerous world.\x02\x03",
            "#2200473VIf that were the case, any hope of a functioning\x01",
            "society would disappear.\x02\x03",
            "#2200474V#2803FWhile justice has become somewhat ambiguous\x01",
            "in Crossbell, we still manage to live our lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200475V#12P#0013F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200476V#0108FMaybe so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200477V#2801F#5PPolitical corruption, the criminal underworld...\x02\x03",
            "#2200478VEven if the police cannot tame them, the economic\x01",
            "prosperity we currently experience allows our\x01",
            "citizenry to live their lives in relative comfort.\x02\x03",
            "#2200479VPetty crime is at an all-time low because of it,\x01",
            "but an unseen evil still spreads across our land...\x02\x03",
            "#2200480V#2803FHowever, despite the dire situation, people still\x01",
            "seek justice. From the very core of their being,\x01",
            "they desire it once more.\x02\x03",
            "#2200481VBecause no matter what shape or form justice\x01",
            "takes, people will always pursue the security\x01",
            "that is a trustworthy society.\x02\x03",
            "#2200482V#2800FAnd that is precisely why Crossbell's bracers\x01",
            "experience the popularity they do.\x02",
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
        "#2200509V#12P#0005FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200484V#12P#0204F'Put the safety of civilians above all else.'\x02\x03",
            "#2200485V#0202FThey certainly do seem to be allies of justice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200486V#0306FAin't that the truth.\x02\x03",
            "#2200487V#0301FKinda had a gut feelin' Crossbellans worship the\x01",
            "guild way more than any other country does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200488V#0106FI wholeheartedly agree. It's clear to see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200489V#2803F#5PThe extent to which bracers can exercise justice\x01",
            "is severely limited, however. That has been and\x01",
            "continues to be their fatal flaw.\x02\x03",
            "#2200490VIt's simply impossible for them to resolve the\x01",
            "injustices of this city.\x02\x03",
            "#2200491V#2800FThat is why I expect great things from you.\x01",
            "You may be the cure to the plague Crossbell\x01",
            "struggles against.\x02",
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
        "#2200492V#12P#0011FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200493V#0305FSo...are you tellin' us to start taking down all\x01",
            "the bad guys? That's a large order, Dieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200494V#2804F#5PHah. Trust me, I have no intention of having you\x01",
            "tackle such a childish, naive mission.\x02\x03",
            "#2200495V#2800FYou all, in your own ways, seem to be desperately\x01",
            "pursuing justice.\x02\x03",
            "#2200496VAnd it's important that you show it in ways your\x01",
            "average Crossbellan can comprehend. That way,\x01",
            "they can see that justice is not out of reach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200497V#12P#0002FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200498V#0104FJustice still lives on in Crossbell...\x02\x03",
            "#2200499V#0100FYou want us to give people a reason to believe that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200500V#2800F#5PExactly.\x02\x03",
            "#2200501V#2804FAnd for that reason, every article that the Crossbell\x01",
            "Times publishes on the Special Support Section is\x01",
            "vital to your success. People notice and remember.\x02\x03",
            "#2200502VYou may still be young and inexperienced officers\x01",
            "who make mistakes from time to time, but I believe\x01",
            "everyone will notice your earnest pursuit of justice.\x02\x03",
            "#2200503V#2800FThere will be a fair amount of naysayers. However,\x01",
            "I don't believe that the majority of our citizenry\x01",
            "has a negative perception of you.\x02\x03",
            "#2200504VIn fact, I think they've begun to place their hopes\x01",
            "in the SSS, even if they may not show it quite yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200505V#12P#0003F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x8,
        (
            "#2200506V#5P#2804FHaha! Look at me, delivering a passionate speech\x01",
            "in the heat of the moment.\x02\x03",
            "#2200507V#2800FLet's return to the issue at hand, shall we?\x02\x03",
            "#2200508VI believe I was about to give you permission to go\x01",
            "and inspect the terminal room, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200483V#12P#0005FY-Yes, sir. That's right.\x02\x03",
            "#2200510V#0000FAs long as you're still willing, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200511V#0100FWhere should we go to gain access?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200512V#5P#2801FHmm. Let me see...\x02\x03",
            "#2200513VI would gladly escort you...\x02\x03",
            "#2200514V#2803F...but unfortunately, I have many matters to attend\x01",
            "to once our discussion has concluded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200515V#0106FOh, our apologies. We didn't mean to overstay our\x01",
            "welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200516V#5P#2804FPay it no mind. I enjoyed our brief chat.\x02\x03",
            "#2200517V#2800FHmm... Shall I have one of my employees\x01",
            "take you?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 55200, 0, 116800, 0)
    StopBGM(0xBB8)
    Sound(103, 0, 100, 0)
    Sleep(300)

    NpcTalk(
        0x9,
        "Girl's Voice",
        "#2200518VThat won't be necessary.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    Fade(500)
    OP_68(55200, 1100, 119300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 53600, 0, 125600, 0)
    SetChrPos(0x102, 55200, 0, 125800, 0)
    SetChrPos(0x103, 54100, 0, 124600, 0)
    SetChrPos(0x104, 56300, 0, 125000, 0)
    OP_68(55200, 1100, 124300, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_72AB():
        OP_95(0xFE, 55200, 0, 122800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_72AB)

    def lambda_72C5():
        OP_95(0xFE, 56000, 0, 128900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_72C5)
    OP_0D()
    Sound(104, 0, 100, 0)

    def lambda_72E6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_72E6)
    Sleep(150)

    def lambda_72F6():

        label("loc_72F6")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_72F6")

    QueueWorkItem2(0x103, 2, lambda_72F6)
    Sleep(100)

    def lambda_730B():

        label("loc_730B")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_730B")

    QueueWorkItem2(0x101, 2, lambda_730B)
    Sleep(100)

    def lambda_7320():

        label("loc_7320")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_7320")

    QueueWorkItem2(0x104, 2, lambda_7320)
    WaitChrThread(0x9, 1)
    OP_6F(0x11)

    ChrTalk(
        0x101,
        "#2200398V#5P#0005F(Who is she?)\x02",
    )

    CloseMessageWindow()

    def lambda_735D():
        OP_95(0xFE, 55200, 0, 124200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_735D)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        "#2200520V#5P#0105FBell!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        "#2200521V#2800FAh, so you've returned.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Blonde-Haired Woman")

    AnonymousTalk(
        0xFF,
        (
            "#2200522VYes, Father. I just arrived\x01",
            "moments ago.\x02\x03",
            "#2200523VIt's been too long, Elie!\x02",
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
    OP_68(55240, 1100, 124620, 1000)

    def lambda_74AD():
        OP_95(0xFE, 55200, 0, 123700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_74AD)
    WaitChrThread(0x9, 1)

    def lambda_74CB():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_74CB)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrSubChip(0x102, 0x1)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(100)
    SetChrSubChip(0x102, 0x6)
    Sleep(100)
    SetChrSubChip(0x102, 0x7)
    Sleep(100)
    SetChrSubChip(0x102, 0x6)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)

    ChrTalk(
        0x102,
        "#2200524V#0112FC-Cut it out, Bell...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Blonde-Haired Woman",
        (
            "#2200525V#11P#2904FHmm... How long HAS it been? Two months? Three?\x02\x03",
            "#2200526V#2901FHave you gotten thinner, Elie? Have you been eating\x01",
            "right? We can always fix that, no problem.\x02\x03",
            "#2200527VI also see that your arms and legs have shaped up\x01",
            "nicely, too. Very impressive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200528V#0104FIt's only natural that I'd build some muscle,\x01",
            "given our daily routines.\x02\x03",
            "#2200529V#0102FI may have actually gained a few pounds, believe it\x01",
            "or not.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Blonde-Haired Woman",
        (
            "#2200530V#11P#2905FOh, is that right?\x02\x03",
            "#2200531VNow that you mention it, I can feel that your\x01",
            "muscles have become a bit more flexible.\x02\x03",
            "#2200532V#2909FI must say, this sensation is absolutely marvelous.\x01",
            "It really is something to behold!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200533V#0113FP-Please stop...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2200534V#5P#0012F(She's...bold, isn't she?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200535V#11P#0302F(Thank you, Aidios. I will treasure this moment\x01",
            "for the rest of my life.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200536V#5P#0211F(I get the impression their relationship transcends\x01",
            "your ordinary friendship...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200537V#2804FHasn't this heartfelt reunion carried on long enough,\x01",
            "Mariabell?\x02\x03",
            "#2200538V#2800FOr would you rather our guests continue to stare?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200539V#0112FS-Stare?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Blonde-Haired Woman",
        "#2200540V#12P#2905FOh, dear. Suck away all the fun, Father.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x3)
    Sleep(100)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x9, 0x8)

    def lambda_7AD0():
        OP_96(0xFE, 0xD7A0, 0x0, 0x1E014, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7AD0)
    WaitChrThread(0x9, 1)
    OP_93(0x102, 0x0, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#2200541V#0113F#11PE-Everyone, allow me to introduce my friend.\x02\x03",
            "#2200542V#0102FThis is Mariabell Crois. Uncle Dieter's daughter\x01",
            "and my best friend.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#2200543V#0100FThese are my colleagues, Bell.\x01",
            "Lloyd, Randy, and Tio--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2200544V#12P#2903FEnough with the introductions, dear.\x02\x03",
            "#2200545V#2901FI'd much rather inspect them myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200546V#0105FHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_7C6F():

        label("loc_7C6F")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_7C6F")

    QueueWorkItem2(0x102, 2, lambda_7C6F)

    def lambda_7C81():

        label("loc_7C81")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_7C81")

    QueueWorkItem2(0x8, 2, lambda_7C81)
    BeginChrThread(0x9, 3, 0, 18)
    WaitChrThread(0x9, 3)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        "#2200549V#11P#0012FWh-What?\x02",
    )

    CloseMessageWindow()

    def lambda_7CD3():
        OP_95(0xFE, 53600, 0, 124100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7CD3)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x103, 500)

    def lambda_7CF8():

        label("loc_7CF8")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_7CF8")

    QueueWorkItem2(0x9, 2, lambda_7CF8)
    OP_9E(0x103, 0xD160, 0x1E4C4, 0x15F90, 0x5DC, 0x0)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x9, 0x2)

    ChrTalk(
        0x103,
        "#2200550V#11P#0205FCan I help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2200551V#2909F#5PYou pass, dear. You're as cute\x01",
            "as a button!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(55000, 1100, 125300, 1300)
    MoveCamera(55, 21, 0, 1300)

    def lambda_7DAE():
        OP_95(0xFE, 55000, 0, 125300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7DAE)
    Sleep(300)

    def lambda_7DCB():
        OP_96(0xFE, 0xD7A0, 0x0, 0x1E3FC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7DCB)
    Sleep(300)

    def lambda_7DE8():
        OP_96(0xFE, 0xD1C4, 0x0, 0x1E460, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7DE8)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    TurnDirection(0x9, 0x104, 500)
    Sleep(500)
    TurnDirection(0x9, 0x101, 500)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x9,
        "#2200552V#11P#2901FAnd both of you fail. Miserably.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2200553V#6P#0011F...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200554V#0305F#11PThe hell? I'm cute as a button, too! Cuter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2200555V#11P#2903FHmph! The thought of you mangy mutts being by\x01",
            "my dear Elie's side day in, day out, is revolting...\x02\x03",
            "#2200556V#2901FThe Goddess Herself must be sobbing--no, weeping--\x01",
            "at this tragedy. Absolutely unacceptable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200557V#6P#0006FDid you just call us mutts?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200558V#12P#0101FC-Calm down, Bell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2200559V#11P#2901FAnd what's with your outfits? They are FAR too\x01",
            "casual for someone of Elie's pedigree.\x02\x03",
            "#2200560VYou could at least have the decency to wear an\x01",
            "appropriate suit or something of the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200561V#6P#0005FTh-These... Well, these clothes\x01",
            "make traveling easier.\x02\x03",
            "#2200562V#0012FLike, when we're having to hike\x01",
            "in the mountains or if we have to\x01",
            "trek through difficult terrain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2200563V#11P#2903FQuiet. I didn't ask for any excuses, did I?\x02\x03",
            "#2200564V#2901FYou see, Elie? This is EXACTLY why I didn't\x01",
            "want you to work for the CPD.\x02\x03",
            "#2200565VWhy couldn't you have worked for me instead?\x01",
            "It would have been a much more worthwhile use\x01",
            "of your time AND talent!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 19)

    ChrTalk(
        0x102,
        "#2200566V#12P#0106FThat's enough, Bell!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)

    ChrTalk(
        0x8,
        (
            "#2200567V#2809FHahaha! What a vivacious group of youngsters\x01",
            "you are.\x02\x03",
            "#2200568V#2804FYou're all around the same age, so you should\x01",
            "focus on becoming friendlier. Go out and do\x01",
            "something fun together sometime!\x02\x03",
            "#2200569V#2800FNow, if you'll excuse me, it's time for me to stop\x01",
            "putting off my next appointment.\x02\x03",
            "#2200570VCould you show our guests to the terminal room\x01",
            "later, Bell?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_84B4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_84B4)
    Sleep(150)

    def lambda_84C4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_84C4)
    Sleep(50)

    def lambda_84D4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_84D4)

    def lambda_84E1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_84E1)
    Sleep(50)
    TurnDirection(0x103, 0x8, 500)

    ChrTalk(
        0x9,
        "#2200571V#6P#2905FThe terminal room? Why would I do that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200572V#2800FYou can ask them for the finer details.\x02\x03",
            "#2200573V#2809FFarewell, everyone. It was a pleasure.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85AA():

        label("loc_85AA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_85AA")

    QueueWorkItem2(0x102, 2, lambda_85AA)

    def lambda_85BC():

        label("loc_85BC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_85BC")

    QueueWorkItem2(0x9, 2, lambda_85BC)

    def lambda_85CE():

        label("loc_85CE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_85CE")

    QueueWorkItem2(0x103, 2, lambda_85CE)

    def lambda_85E0():

        label("loc_85E0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_85E0")

    QueueWorkItem2(0x104, 2, lambda_85E0)

    def lambda_85F2():

        label("loc_85F2")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_85F2")

    QueueWorkItem2(0x101, 2, lambda_85F2)
    OP_68(55000, 1100, 121300, 3000)

    def lambda_8615():
        OP_95(0xFE, 55000, 0, 118000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8615)
    WaitChrThread(0x8, 1)

    def lambda_8633():
        OP_95(0xFE, 55000, 0, 115000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8633)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_8656():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8656)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    ClearChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x101, 0x2)
    OP_6F(0x1)
    Sound(104, 0, 100, 0)

    ChrTalk(
        0x102,
        "#2200414V#6P#0105FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200575V#6P#0206FA tactical retreat, if I have ever seen one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2200576V#5P#2906FUgh. That oaf...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(55000, 1100, 125300, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        "#2200577V#6P#0012FTh-Then, could you please lead us to--\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 700)

    ChrTalk(
        0x9,
        "#2200578V#11P#2901FI wasn't finished talking down to you yet!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 700)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#2200579V#2906F#6PYou there, with the fiery red hair and gaudy outfit.\x01",
            "Do you honestly think that is acceptable?\x02\x03",
            "#2200580V#2901FA built physique like yours demands to be\x01",
            "shown off in a suit, like a real man!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88C9():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_88C9)
    Sleep(150)

    def lambda_88D9():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_88D9)
    Sleep(50)
    TurnDirection(0x103, 0x9, 500)

    ChrTalk(
        0x104,
        (
            "#2200581V#0305F#11PWho, me?\x02\x03",
            "#2200582V#0309FSorry to disappoint, but that ain't gonna happen.\x01",
            "I'm a bona fide casanova. I don't need no suits.\x02\x03",
            "#2200583V#0302FDon't get me wrong, though. I would never try to\x01",
            "seduce Mademois-Elie--'specially during a romantic,\x01",
            "moonlit night.\x02\x03",
            "Y'know, like my main man Lloyd right here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 700)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x9,
        "#2200584V#11P#2910F#4SEXCUSE ME?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200585V#6P#0011FRandy, why?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 700)

    ChrTalk(
        0x102,
        (
            "#2200586V#12P#0101FWould you please stop retelling the story in\x01",
            "an intentionally misleading way?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        (
            "#2200587V#6P#0204FI fail to see what exactly he said was misleading.\x02\x03",
            "#2200588V#0202FBesides, your mood has improved dramatically since\x01",
            "last night's fateful rendezvous under the stars.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C1A():
        TurnDirection(0xFE, 0x103, 700)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8C1A)
    Sleep(100)
    TurnDirection(0x101, 0x103, 700)

    ChrTalk(
        0x102,
        "#2200589V#11P#0112FT-Tio, please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200590V#5P#0013FOh, come on! You're making it worse on purpose,\x01",
            "Tio! Don't say you aren't!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8CBC():
        OP_99(0xFE, 0x101, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8CBC)
    WaitChrThread(0x9, 1)
    Sound(804, 0, 100, 0)
    TurnDirection(0x101, 0x9, 700)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8CF6():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8CF6)

    def lambda_8D0F():
        OP_98(0xFE, 0x0, 0xC8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D0F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x9,
        (
            "#2200591V#11P#2909FHeeheheh... Lloyd, wasn't it?\x02\x03",
            "#2200592VCare to elaborate on your friend's little story?\x01",
            "Because there's something I'd like to know.\x02\x03",
            "#2200593V#2910FWhat vile, lecherous things have you done to\x01",
            "my sweet, innocent Elie?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200594V#6P#0012FI haven't done ANYTHING to her! Why would I?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200595V#11P#0113F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200596V#6P#0011FElie? Would you PLEASE back me up here?!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(55100, 1200, 124000, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19500, 0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x4)
    SetChrPos(0x101, 54200, 30, 125400, 135)
    SetChrPos(0x102, 53900, 30, 124000, 90)
    SetChrPos(0x103, 52500, 30, 123400, 90)
    SetChrPos(0x104, 52400, 30, 124400, 90)
    SetChrPos(0x9, 56200, 0, 124000, 270)
    SetCameraDistance(20000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x9,
        (
            "#2200597V#2903F#11PI think I understand the situation now.\x02\x03",
            "#2200598V#2900FShall I show you to the terminal room, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
           "#2200599V#6P#0100FThat would be lovely, Bell.\x01",
           "It's not too much trouble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2200600V#2906F#11POf course not. I'd do anything for you, Elie.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x9)

    ChrTalk(
        0x101,
        "#2200601V#0012FSo...have we cleared up that misunderstanding?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2200602V#2903F#11PHmph. Well, it's not like it matters anymore.\x02\x03",
            "#2200603VI was just worried about what kind of unsavory\x01",
            "group the Special Support Section was.\x02\x03",
            "#2200604V#2902FIn the end, you'll have to prove that you're worthy\x01",
            "of being called Elie's colleagues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200605V#0011FW-Wait...\x01",
            "(Why was I the only one under fire?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200606V#6P#0302F(Dude, I coulda sworn she was about to\x01",
            "chokeslam you back there.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200607V#6P#0204F(I offer you my sympathies, Lloyd.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200608V#6P#0106FI think you've had enough fun, Bell.\x02\x03",
            "#2200609V#0101FCould you show us to the terminal room now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 500)

    ChrTalk(
        0x9,
        (
            "#2200610V#2904F#11POf course. Follow me.\x02\x03",
            "#2200611V#2900FThe terminal room is down on floor B5.\x02\x03",
            "#2200612VShall we board the elevator, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    def lambda_9424():

        label("loc_9424")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_9424")

    QueueWorkItem2(0x102, 2, lambda_9424)

    def lambda_9436():

        label("loc_9436")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_9436")

    QueueWorkItem2(0x103, 2, lambda_9436)

    def lambda_9448():

        label("loc_9448")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_9448")

    QueueWorkItem2(0x104, 2, lambda_9448)

    def lambda_945A():

        label("loc_945A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_945A")

    QueueWorkItem2(0x101, 2, lambda_945A)
    OP_68(55100, 1200, 120000, 3000)

    def lambda_947D():
        OP_95(0xFE, 55000, 0, 117500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_947D)
    WaitChrThread(0x9, 1)

    def lambda_949B():
        OP_95(0xFE, 55000, 0, 115000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_949B)
    Sound(103, 0, 100, 0)
    Sleep(300)

    def lambda_94BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_94BE)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    ClearChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x101, 0x2)
    Sleep(500)
    Fade(500)
    OP_68(53890, 1200, 124430, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
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
        "#2200613V#0006F#5P*sigh* She's a real piece of work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200614V#5P#0105FI promise she's not a bad person.\x02\x03",
            "#2200615V#0106FIt's just, I sometimes can't be sure if she's being\x01",
            "overbearing or overly enthusiastic...or both.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200616V#0300F#5PEh, no biggie. She and her old man sure make\x01",
            "a helluva team, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200617V#0204F#5PThat is unsurprising for the two heads of the\x01",
            "famous International Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    AddParty(0x37, 0xFF, 0xFF)
    OP_68(53000, 1500, 44200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 53000, 0, 44200, 180)
    SetChrPos(0x1, 53000, 0, 44200, 180)
    SetChrPos(0x2, 53000, 0, 44200, 180)
    SetChrPos(0x3, 53000, 0, 44200, 180)
    SetChrPos(0x4, 53000, 0, 44200, 180)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x82, 5)
    ClearScenarioFlags(0x0, 3)
    OP_29(0x43, 0x1, 0x3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_3715 end

    def Function_18_97EB(): pass

    label("Function_18_97EB")


    def lambda_97F0():
        OP_95(0xFE, 56300, 0, 124000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_97F0)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x104, 500)
    Sleep(500)

    ChrTalk(
        0x9,
        "#2200547V#2901FHmm...\x02",
    )

    CloseMessageWindow()

    def lambda_9833():
        OP_95(0xFE, 55200, 0, 122900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9833)
    WaitChrThread(0x9, 1)

    def lambda_9851():
        OP_95(0xFE, 53400, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9851)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x103, 500)
    Sleep(500)

    ChrTalk(
        0x9,
        "#2200548V#5P#2902FI see.\x02",
    )

    CloseMessageWindow()

    def lambda_9897():
        OP_95(0xFE, 52600, 0, 125600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9897)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x101, 500)
    Sleep(500)
    Return()

    # Function_18_97EB end

    def Function_19_98BB(): pass

    label("Function_19_98BB")

    EndChrThread(0x8, 0x2)

    def lambda_98C4():
        OP_95(0xFE, 56000, 0, 130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_98C4)
    WaitChrThread(0x8, 1)

    def lambda_98E2():
        OP_95(0xFE, 58600, 0, 130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_98E2)
    WaitChrThread(0x8, 1)

    def lambda_9900():
        OP_95(0xFE, 58600, 0, 127500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9900)
    WaitChrThread(0x8, 1)

    def lambda_991E():
        OP_95(0xFE, 58000, 0, 126900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_991E)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x9, 500)
    Return()

    # Function_19_98BB end

    def Function_20_993F(): pass

    label("Function_20_993F")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(53290, 1430, 123860, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16630, 0)
    SetChrPos(0x101, 54450, 30, 123460, 0)
    SetChrPos(0x102, 53320, 30, 123460, 0)
    SetChrPos(0x103, 53320, 30, 121930, 0)
    SetChrPos(0x104, 54450, 30, 121930, 0)
    SetChrPos(0x9, 54010, 30, 125480, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#5P#2901FI'm so sick of this!\x01",
            "I've been stuck in meetings all day thanks\x01",
            "to those Revache buffoons!\x02\x03",
            "#2903FFortunately enough, I don't think their little\x01",
            "'raid' will affect our stock prices negatively.\x02\x03",
            "#2901FGrr! I almost want to kick down their door and\x01",
            "demand compensation for all the hassle they've\x01",
            "put me through!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0103FYour life never seems to get any easier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#2900FIt's especially bad right now, since\x01",
            "Father is away at the moment.\x02\x03",
            "#2905FOh, yes.\x01",
            "Did you need something, Elie?\x02\x03",
            "Judging by the crowd you've brought with\x01",
            "you, it doesn't seem to be a personal issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FYes. There's something I need to ask you, Bell.\x02\x03",
            "Carla should have stopped by the IBC\x01",
            "earlier today. Did you happen to see her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#2905FCarla?\x02\x03",
            "#2900FYes, she was here not long ago.\x02\x03",
            "#2904FShe and I are acquaintances through\x01",
            "our social circles.\x02\x03",
            "She came to me claiming she had some\x01",
            "kind of personal emergency.\x02\x03",
            "#2900FAfter that, she withdrew every last mira\x01",
            "in her savings account.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0303FDamn. We were right on the money.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0005FWhy did she have to speak directly to you\x01",
            "for that, Mariabell?\x02\x03",
            "You'd think the receptionist would have been\x01",
            "able to handle her request just fine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#2903FIt has to do with the amount she withdrew.\x02\x03",
            "#2900FUnder normal circumstances, you would need to fill\x01",
            "out the appropriate paperwork.\x01",
            "Today was an exception.\x02\x03",
            "As you might be able to surmise, I am unable to\x01",
            "disclose the exact amount she withdrew. That said...\x01",
            "It was in the hundreds of thousands of mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0205FThat is an exorbitant amount of money.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103FThe truth is, Carla is attempting to run away\x01",
            "from home. We've been tasked with bringing\x01",
            "her back safely.\x02\x03",
            "#0100FDo you know where she might have gone, Bell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#2905FOh. Well, that would explain her rash behavior.\x02\x03",
            "#2903FHmm... Well, judging by the amount she withdrew,\x01",
            "I would assume she's planning to relocate to\x01",
            "a foreign country.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#11P#0000FThat could be it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FIs it possible she had a destination in mind?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5P#2903FWell, now that I think about it...\x02\x03",
            "...I recall a conversation between her and\x01",
            "her maid about sightseeing in Grancel.\x02\x03",
            "#2900FI believe Carla ordered her maid to make\x01",
            "hotel reservations there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0005FGrancel?\x01",
            "Isn't that Liberl's capital city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FSo she's ditchin' this joint for Liberl!\x02",
    )

    CloseMessageWindow()

    def lambda_A378():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A378)

    def lambda_A385():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A385)

    def lambda_A392():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A392)

    def lambda_A39F():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A39F)
    Sleep(800)

    ChrTalk(
        0x103,
        (
            "#12P#0200FShe must have departed for the airport, then.\x02\x03",
            "We may be able to arrive in time if we\x01",
            "proceed with haste. We must notify the\x01",
            "airport's receptionist!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0101FRight! We have to hurry!\x02",
    )

    CloseMessageWindow()

    def lambda_A47A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A47A)

    def lambda_A487():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A487)

    def lambda_A494():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A494)

    def lambda_A4A1():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A4A1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#0001FWe're sorry to have bothered you.\x01",
            "We appreciate your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0101FSee you later, Bell!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#2905FS-Sure...\x02",
    )

    CloseMessageWindow()
    OP_68(55390, 1400, 119040, 1600)
    SetCameraDistance(17100, 1600)
    BeginChrThread(0x104, 0, 0, 21)
    Sleep(220)
    BeginChrThread(0x103, 0, 0, 21)
    Sleep(180)
    BeginChrThread(0x101, 0, 0, 21)
    Sleep(240)
    BeginChrThread(0x102, 0, 0, 21)
    Sleep(200)
    Sound(103, 0, 100, 0)
    Sleep(1500)
    Sound(104, 0, 100, 0)
    Sleep(1500)
    Fade(500)
    OP_68(53680, 1430, 124740, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#5P#2903FThey sure know how to keep busy...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(52870, 1500, 44710, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 52870, 0, 44710, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    OP_29(0x2D, 0x1, 0x8)
    SetScenarioFlags(0x0, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_993F end

    def Function_21_A65A(): pass

    label("Function_21_A65A")

    OP_95(0xFE, 55000, 0, 118710, 5000, 0x1)

    def lambda_A673():
        OP_95(0xFE, 55000, 0, 114830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A673)
    Sleep(100)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_21_A65A end

    def Function_22_A697(): pass

    label("Function_22_A697")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A79E")

    ChrTalk(
        0x102,
        "#0102F(This is Bell's room, isn't it?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhat's wrong, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FOh, it's nothing.\x02\x03",
            "#0100FUncle's office is just down this hallway, Lloyd.\x01",
            "We should go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah, let's.\x02",
    )

    CloseMessageWindow()

    label("loc_A79E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8DE")

    ChrTalk(
        0x138,
        (
            "#2905FOh, that's my private room.\x02\x03",
            "#2902FWould you like to join me for some tea?\x01",
            "It'll be my treat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FHaha. Sorry, we're a little busy right now.\x02\x03",
            "#0000FDo you mind showing us to the terminal room first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2904FNot at all. I'll show you the way.\x02\x03",
            "#2900FShall we board the elevator, then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8DE")

    SetScenarioFlags(0x0, 3)

    label("loc_A8E1")

    TalkEnd(0xFF)
    Return()

    # Function_22_A697 end

    def Function_23_A8E5(): pass

    label("Function_23_A8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_END)), "loc_A9CD")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is an exquisite doll that exhibits lifelike features...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9C5")

    ChrTalk(
        0x101,
        (
            "#0003F(I can't imagine what fate is in store for us if we\x01",
            "scratch it, so let's keep our hands to ourselves.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_A9C5")

    TalkEnd(0xFF)
    Jump("loc_A9D0")

    label("loc_A9CD")

    Call(0, 7)

    label("loc_A9D0")

    Jump("loc_AD26")

    label("loc_A9D5")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is an exquisite doll that exhibits lifelike features...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACA4")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005FHuh?!\x02\x03",
            "#0003FThis is seriously unbelievable...\x01",
            "Is this really just a doll?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FYes, it was crafted at the Rosenberg Studio.\x02\x03",
            "Bell has a huge collection of dolls from there.\x01",
            "If I recall, those two are her favorites.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205FThis is my first time experiencing a Rosenberg doll\x01",
            "up close. The details on the skin are immaculate.\x01",
            "I've never seen such a lifelike doll before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303FThe details on this thing are insane.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI've heard they cost a fortune,\x01",
            "but I have to admit...\x01",
            "The quality speaks for itself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 3)

    label("loc_ACA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD23")

    ChrTalk(
        0x101,
        (
            "#0003F(I can't imagine what fate is in store for us if we\x01",
            "scratch it, so let's keep our hands to ourselves.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_AD23")

    TalkEnd(0xFF)

    label("loc_AD26")

    Return()

    # Function_23_A8E5 end

    SaveToFile()

Try(main)
