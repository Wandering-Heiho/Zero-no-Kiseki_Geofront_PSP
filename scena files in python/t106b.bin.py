from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t106b.bin",                # FileName
        "t106b",                    # MapName
        "t106b",                    # Location
        0x0043,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 2, 0, 3],
    )

    BuildStringList((
        "t106b",                  # 0
        "Peter",                  # 1
        "Master Fisherman Lloyd", # 2
        "Tourist",                # 3
    ))

    AddCharChip((
        "chr/ch24202.itc",                   # 00
        "chr/ch37500.itc",                   # 01
        "chr/ch32202.itc",                   # 02
    ))

    DeclNpc(-102470, 150,     2529,    90,   341,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-100779, 0,       -490,    90,   261,  0x0, 0,   1,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(100470,  150,     2609,    90,   341,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)

    ScpFunction((
        "Function_0_110",          # 00, 0
        "Function_1_1C8",          # 01, 1
        "Function_2_1F3",          # 02, 2
        "Function_3_1F4",          # 03, 3
        "Function_4_1F5",          # 04, 4
        "Function_5_46E",          # 05, 5
        "Function_6_5CE",          # 06, 6
    ))


    def Function_0_110(): pass

    label("Function_0_110")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_150"),
        (1, "loc_15C"),
        (2, "loc_168"),
        (3, "loc_174"),
        (4, "loc_180"),
        (5, "loc_18C"),
        (6, "loc_198"),
        (SWITCH_DEFAULT, "loc_1A4"),
    )


    label("loc_150")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_15C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_168")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_174")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_180")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_18C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_198")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1C7")

    Return()

    # Function_0_110 end

    def Function_1_1C8(): pass

    label("Function_1_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F2")
    OP_94(0xFE, 0xFFFE6DDA, 0x122, 0xFFFE7D66, 0xFFFFF8E4, 0x3E8)
    Sleep(400)
    Jump("Function_1_1C8")

    label("loc_1F2")

    Return()

    # Function_1_1C8 end

    def Function_2_1F3(): pass

    label("Function_2_1F3")

    Return()

    # Function_2_1F3 end

    def Function_3_1F4(): pass

    label("Function_3_1F4")

    Return()

    # Function_3_1F4 end

    def Function_4_1F5(): pass

    label("Function_4_1F5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_289")
    Jump("loc_2D3")

    label("loc_289")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D3")

    label("loc_2A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D3")

    label("loc_2C9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390")

    ChrTalk(
        0xFE,
        (
            "Branch Manager Cerdan did me a favor\x01",
            "and booked this room for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cerdan makes quite a bit working\x01",
            "for the guild, you know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_466")

    label("loc_390")


    ChrTalk(
        0xFE,
        (
            "Still, renting a three-person suite for just the two\x01",
            "of us might have been a little overkill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha! If you need a room, Lloyd, I don't\x01",
            "mind letting you snag one of the beds.\x01",
            "Anything for a fellow member!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_466")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_1F5 end

    def Function_5_46E(): pass

    label("Function_5_46E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F9")

    ChrTalk(
        0xFE,
        "Sure is a fancy hotel...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My comrades here in Crossbell never fail\x01",
            "to take care of me. They're a good bunch.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5CA")

    label("loc_4F9")


    ChrTalk(
        0xFE,
        (
            "On top of that, the fishing is a thrill,\x01",
            "and the food is always top notch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I return to Liberl, I'm going to have to\x01",
            "launch a big advertising campaign if I ever\x01",
            "hope to compete with this branch!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA")

    TalkEnd(0xFE)
    Return()

    # Function_5_46E end

    def Function_6_5CE(): pass

    label("Function_6_5CE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_662")
    Jump("loc_6AC")

    label("loc_662")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_682")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AC")

    label("loc_682")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AC")

    label("loc_6A2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "*yawn*...It's been a loooong day. Might be a little\x01",
            "early, but I think I'm going to turn in for the night.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_5CE end

    SaveToFile()

Try(main)
