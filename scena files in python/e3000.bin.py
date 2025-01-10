from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3000.bin",                # FileName
        "e3000",                    # MapName
        "e3000",                    # Location
        0x00A1,                     # MapIndex
        "ed7104",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 2, 0, 3],
    )

    BuildStringList((
        "e3000",                  # 0
        "Lechter",                # 1
        "Boy",                    # 2
        "Man",                    # 3
        "Woman",                  # 4
        "Tourist",                # 5
        "SE制御",                 # 6
    ))

    AddCharChip((
        "chr/ch07400.itc",                   # 00
        "chr/ch20602.itc",                   # 01
        "chr/ch20202.itc",                   # 02
        "chr/ch20302.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "apl/ch50352.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
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

    DeclNpc(2950,    4099,    -7750,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-1169,   4250,    899,     180,  341,  0x0, 0,   1,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(1029,    4250,    899,     180,  341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(2210,    4250,    899,     180,  341,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       4099,    12760,   0,    257,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_285",          # 01, 1
        "Function_2_2A5",          # 02, 2
        "Function_3_2CB",          # 03, 3
        "Function_4_2E3",          # 04, 4
        "Function_5_2F2",          # 05, 5
        "Function_6_535",          # 06, 6
        "Function_7_6D0",          # 07, 7
        "Function_8_8FD",          # 08, 8
        "Function_9_AB1",          # 09, 9
        "Function_10_B96",         # 0A, 10
        "Function_11_D24",         # 0B, 11
        "Function_12_24B3",        # 0C, 12
        "Function_13_24D4",        # 0D, 13
        "Function_14_24F5",        # 0E, 14
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_213")
    Sleep(600)
    Jump("loc_23C")

    label("loc_213")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22A")
    Sleep(400)
    Jump("loc_23C")

    label("loc_22A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23C")
    Sleep(200)

    label("loc_23C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_284")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Jump("loc_23C")

    label("loc_284")

    Return()

    # Function_0_1F0 end

    def Function_1_285(): pass

    label("Function_1_285")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A4")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1)
    Jump("Function_1_285")

    label("loc_2A4")

    Return()

    # Function_1_285 end

    def Function_2_2A5(): pass

    label("Function_2_2A5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BB")
    Event(0, 14)

    label("loc_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2CA")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)

    label("loc_2CA")

    Return()

    # Function_2_2A5 end

    def Function_3_2CB(): pass

    label("Function_3_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC")
    Call(0, 4)

    label("loc_2DC")

    Sound(479, 1, 100, 0)
    Return()

    # Function_3_2CB end

    def Function_4_2E3(): pass

    label("Function_4_2E3")

    SetChrChipByIndex(0x8, 0x5)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 1)
    Return()

    # Function_4_2E3 end

    def Function_5_2F2(): pass

    label("Function_5_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_308")
    Call(0, 11)
    Jump("loc_534")

    label("loc_308")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E8")

    ChrTalk(
        0x8,
        (
            "#3506FStill, the only thing I'll spill is that I'm\x01",
            "attending this 'party' in the stead of\x01",
            "the old man.\x02\x03",
            "#3500FIf I had known there was a theme park,\x01",
            "I would've come to Crossbell first thing\x01",
            "in the morning... Oh, well. Live and learn.\x02",
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
        "#0012FQuite the playboy, aren't you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3504FOuch, that's pretty rude, y'know?\x01",
            "Gotta do what the heart wants.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_531")

    label("loc_4E8")


    ChrTalk(
        0x8,
        (
            "#3510FShould I check out this rumored\x01",
            "theme park right off the bat?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_531")

    TalkEnd(0x8)

    label("loc_534")

    Return()

    # Function_5_2F2 end

    def Function_6_535(): pass

    label("Function_6_535")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C9")
    Jump("loc_613")

    label("loc_5C9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_613")

    label("loc_5E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_609")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_613")

    label("loc_609")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_613")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D")

    ChrTalk(
        0xFE,
        (
            "Yaaay! I love the cruise ship!\x01",
            "It's so faaast! Zoom!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_698")
    SetScenarioFlags(0xB6, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_698")

    Jump("loc_6C8")

    label("loc_69D")


    ChrTalk(
        0xFE,
        "I wonder if we're almost to Mishelam?\x02",
    )

    CloseMessageWindow()

    label("loc_6C8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_535 end

    def Function_7_6D0(): pass

    label("Function_7_6D0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_764")
    Jump("loc_7AE")

    label("loc_764")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_784")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AE")

    label("loc_784")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AE")

    label("loc_7A4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A1")

    ChrTalk(
        0xFE,
        (
            "I was swamped at work during the\x01",
            "Anniversary Festival, but I finally\x01",
            "found time to spend with my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today's going to be the\x01",
            "ultimate family outing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C")
    SetScenarioFlags(0xB6, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_89C")

    Jump("loc_8F5")

    label("loc_8A1")


    ChrTalk(
        0xFE,
        (
            "I plan to forget all about work,\x01",
            "kick back, and hang out with\x01",
            "my family today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_6D0 end

    def Function_8_8FD(): pass

    label("Function_8_8FD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_991")
    Jump("loc_9DB")

    label("loc_991")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DB")

    label("loc_9B1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DB")

    label("loc_9D1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9DB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I'm so happy that my husband was\x01",
            "able to clear his schedule for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think this will be an adventure\x01",
            "that our son will never forget.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA9")
    SetScenarioFlags(0xB6, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_8FD end

    def Function_9_AB1(): pass

    label("Function_9_AB1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Aren't there loads of fancy\x01",
            "restaurants in Mishelam?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the last decade, my life's journey has been\x01",
            "scouring the continent for gourmet food...\x01",
            "I have high hopes for Crossbell's cuisine!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B92")
    SetScenarioFlags(0xB6, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B92")

    TalkEnd(0xFE)
    Return()

    # Function_9_AB1 end

    def Function_10_B96(): pass

    label("Function_10_B96")

    EventBegin(0x0)
    OP_E5()
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    Call(0, 4)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C5C")
    FadeToBright(1000, 0)
    OP_68(80, 2300, -22430, 0)
    MoveCamera(11, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(85880, 0)
    OP_68(570, 2300, 64420, 18000)
    SetCameraDistance(45950, 13500)
    MoveCamera(11, 16, 0, 13500)
    Sleep(12000)
    OP_0D()

    label("loc_C5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CAF")
    Fade(2000)
    OP_68(60, 4500, -16129, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25520, 0)
    OP_68(60, 4500, 20650, 15000)
    Sleep(12000)
    OP_0D()

    label("loc_CAF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D0B")
    Fade(2000)
    OP_68(-5400, 4500, -20850, 0)
    MoveCamera(152, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29350, 0)
    OP_68(-5400, 4500, 49430, 15000)
    SetCameraDistance(69180, 9000)
    Sleep(12000)
    OP_0D()

    label("loc_D0B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("e0510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_B96 end

    def Function_11_D24(): pass

    label("Function_11_D24")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("apl/ch50351.itc", 0x1E)
    SetCameraDistance(18440, 0)
    OP_68(2260, 5800, -6790, 0)
    MoveCamera(136, 20, 0, 0)
    OP_6E(500, 0)
    SetChrPos(0x101, 2350, 4100, -6500, 180)
    SetChrPos(0x102, 3550, 4100, -6500, 180)
    SetChrPos(0x103, 2350, 4100, -5500, 180)
    SetChrPos(0x104, 3550, 4100, -5500, 180)
    SetChrPos(0x8, 2950, 4100, -8150, 0)
    FadeToBright(1000, 0)
    StopBGM(0xBB8)
    BeginChrThread(0xD, 0, 0, 12)
    SetCameraDistance(16940, 3000)
    OP_6F(0x10)
    OP_0D()
    EndChrThread(0xD, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7525", 1)

    ChrTalk(
        0x8,
        (
            "#3500185V#3509F#11P#67AAhead of us, paradise awaits! ♪\x02\x03",
            "#67ALet's join hands and run along the shore! ♪\x02\x03",
            "#3510F#48AIn a white rowboat, aiming for the island! ♪\x02\x03",
            "#46AGetting captivating tan lines! ♪\x02\x03",
            "#42AParasols, palm trees, and snow cones! ♪\x02\x03",
            "#3504F#60AThe place where you are, that's my paradise! ♪\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    BeginChrThread(0xD, 0, 0, 13)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x3E8)
    EndChrThread(0xD, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7104", 0)

    ChrTalk(
        0x101,
        "#3500191V#0012F#6PHe certainly knows how to entertain himself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500192V#0306F#6PThe fact that he's not a half-bad\x01",
            "singer makes me kinda pissed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500193V#3507F#11PYup. Youth's a blast.\x02\x03",
            "#3500194V#3509FAnd, hey, a certain prince doesn't hold a\x01",
            "monopoly on playing songs while traveling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500195V#0211F#6PWhat are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500196V#0100F#5PUmm, Lechter. Do you have business\x01",
            "at Mishelam?\x02\x03",
            "#3500197VSomething tells me that visiting the\x01",
            "theme park isn't your real objective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500198V#3503F#11POh, didn't I tell you earlier? I'm coming\x01",
            "as a representative.\x02\x03",
            "#3500199V#3501FOne of a certain shrewd, middle-aged dude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500200V#0005F#6PWho are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500201V#3501F#11PHmm, well, I doubt you haven't heard\x01",
            "his name before.\x02\x03",
            "#3500202VThe grumpy guy I'm referring to is\x01",
            "named Giliath Osborne.\x02",
        )
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#3500203V#0011F#6P#4SCome again?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500204V#3505F#11PSee, what did I tell you?\x02\x03",
            "#3500205V#3506FThat guy definitely knows how to keep\x01",
            "up appearances.\x02\x03",
            "#3500206VHe always grooms his beard carefully\x01",
            "to try and make himself look like he's\x01",
            "some charismatic middle-aged man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500207V#0001F#6PThe Imperial Chancellor,\x01",
            "Giliath Osborne...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500208V#0203F#6P...'The Blood and Iron Chancellor.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500209V#0101F#5PI-It can't be... You work for\x01",
            "the Imperial government?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500210V#3504F#11PYeah, but don't freak. I'm just a secretary.\x02\x03",
            "#3500211V#3500FSo, the big cheese in Crossbell is\x01",
            "that Hartmann guy, right?\x02\x03",
            "#3500212VLast year, he and Old Man Giliath had a\x01",
            "not-so-secret powwow. It was a nice lil'\x01",
            "discussion about communication networks.\x02\x03",
            "#3500213VIn order to seal the deal on this\x01",
            "network, I had to get my hands dirty.\x02\x03",
            "#3500214V#3506FGeez, you know how boring\x01",
            "official work is? Real boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500215V#0003F#6PS-Sorry to hear that.\x02\x03",
            "#3500216V#0005FErr, you sure it was okay\x01",
            "to tell us all that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500217V#3500F#11PI don't see why not.\x02\x03",
            "#3500218V#3509FAfter all, you're all going to die here.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x0, 0x7D0)
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
        "#3500219V#0007F#6PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500220V#0301F#6PYou...\x02",
    )

    CloseMessageWindow()
    OP_68(2380, 5800, -6400, 1200)

    def lambda_18BB():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18BB)
    Sleep(50)

    def lambda_18D3():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18D3)
    Sleep(100)

    def lambda_18EB():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18EB)
    Sleep(50)

    def lambda_1903():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1903)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#3500221V#3504F#11PAre you aware of how many of my\x01",
            "subordinates boarded the cruise\x01",
            "ship with me?\x02\x03",
            "#3500222V#3500FDefinitely couldn't count them with\x01",
            "two hands, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500223V#0101F#5PWhat are you after?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500224V#0208F#6PWe are trapped...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500225V#3504F#11PHahaha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    VolumeBGM(0x64, 0xBB8)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#3500226V#3509F#4S#11PAhahahahaha!\x02\x03",
            "#3500227V#3504FOh, man, you should've seen the\x01",
            "looks on your faces.\x02\x03",
            "#3500228V#3502FHow naive can you get? C'mon,\x01",
            "I'm not THAT good an actor!\x02",
        )
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
        0x101,
        "#3500229V#0011F#6PWait a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500230V#0301F#6PYou were jokin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500231V#3509F#11PWow, do you even have to ask?\x02\x03",
            "#3500232VWhile I was on the train to Crossbell, I read\x01",
            "heaps of spy novels. Thought it'd be fun to\x01",
            "put what I learned to the test.\x02\x03",
            "#3500233VBut, wow. Color me surprised, 'cause I didn't\x01",
            "think it'd work THAT well.\x02\x03",
            "#3500234V#3502FGive it to me straight, guys. Did you actually\x01",
            "fall for that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500235V#0012F#6PU-Uhh, maybe...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500236V#0106F#5PYou were so serious... That must have been\x01",
            "what lured us into the joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500237V#3504F#11PThe way you all reacted, I could have sworn\x01",
            "you were police officers trying to infiltrate\x01",
            "the auction or somethin'...\x02\x03",
            "#3500238V#3500FThat'd make for one heck of a spy novel, eh?\x01",
            "You don't hear stories like that every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500239V#0012F#6PH-Haha... Us, police officers? There's no way\x01",
            "that's true, right?\x02\x03",
            "#3500240V#0005FBut, wait a minute...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500241V#0201F#6PAre you implying that you are\x01",
            "attending the auction, as well...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500242V#3504F#11PYup, that's the plan.\x02\x03",
            "#3500243V#3505FBy the way, forget all that nonsense about\x01",
            "me being the Blood and Iron Chancellor's\x01",
            "secretary, too, okay?\x02\x03",
            "#3500244V#3500FI'm just the run-of-the-mill son of a rich,\x01",
            "noble family in the Empire.\x02\x03",
            "#3500245VNoblesse oblige requires me to represent\x01",
            "my pops, who can't make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500246V#0103F#5PI don't know what to believe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500247V#0300F#6PSorry, dude, but you don't strike me\x01",
            "as the son of an Erebonian noble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500248V#3505F#11PWow, how extremely rude!\x02\x03",
            "#3500249V#3504FThe lovely ladies aside, you guys don't\x01",
            "seem very noble, either, now do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500250V#0006F#6PUgh, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500251V#0309F#6PHaha, got us there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500252V#0104F#5PIrrelevant. We received invitations,\x01",
            "same as you.\x02\x03",
            "#3500253V#0100FIt's possible that we'll run into each\x01",
            "other on the way to the mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500254V#3500F#11P...Heh heh.\x02\x03",
            "#3500255V#3504FDang, you guys are a fun bunch.\x01",
            "When the time comes, gimme a call.\x02\x03",
            "#3500256VAfter a while, I might get tired of\x01",
            "keeping old geezers company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500257V#0003F#6PWe'll keep that in mind.\x02\x03",
            "#3500258V#0000FMaybe we'll cross paths at some\x01",
            "point during the auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500259V#3509F#11PSounds good. Take it easy, guys.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetCameraDistance(17190, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    OP_49()
    OP_D5(0x1E)
    SetChrPos(0x0, 2780, 4100, -6430, 180)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 2950, 4100, -7750, 180)
    SetScenarioFlags(0xA3, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_D24 end

    def Function_12_24B3(): pass

    label("Function_12_24B3")

    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Return()

    # Function_12_24B3 end

    def Function_13_24D4(): pass

    label("Function_13_24D4")

    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    Return()

    # Function_13_24D4 end

    def Function_14_24F5(): pass

    label("Function_14_24F5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3500315V\x07\x05",
            "Thank you for your patience.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#3500316V\x07\x05",
            "The cruise ship will be arriving\x01",
            "at Mishelam shortly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#3500317V\x07\x05",
            "Please, don't forget to take\x01",
            "your belongings with you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_25(0x1DF, 0x0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_24F5 end

    SaveToFile()

Try(main)
