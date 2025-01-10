from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1620.bin",                # FileName
        "t1620",                    # MapName
        "t1620",                    # Location
        0x0055,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 85, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1620",                  # 0
    ))

    AddCharChip((
        "chr/ch29400.itc",                   # 00
        "chr/ch29200.itc",                   # 01
    ))

    DeclActor(-3000,   0,       64599,   1000,    -3000,   1200,    64599,   0x007C, 0,  5,  0x0000)
    DeclActor(-880,    0,       62400,   1000,    -880,    1200,    62400,   0x007C, 0,  6,  0x0000)
    DeclActor(-880,    0,       58300,   1000,    -880,    1200,    58300,   0x007C, 0,  7,  0x0000)
    DeclActor(880,     0,       58300,   1000,    880,     1200,    58300,   0x007C, 0,  8,  0x0000)
    DeclActor(880,     0,       62400,   1000,    880,     1200,    62400,   0x007C, 0,  9,  0x0000)
    DeclActor(3000,    0,       64599,   1000,    3000,    1200,    64599,   0x007C, 0,  10, 0x0000)
    DeclActor(5100,    0,       62400,   1000,    5100,    1200,    62400,   0x007C, 0,  4,  0x0000)
    DeclActor(5100,    0,       58300,   1000,    5100,    1200,    58300,   0x007C, 0,  11, 0x0000)
    DeclActor(6940,    0,       58300,   1000,    6940,    1200,    58300,   0x007C, 0,  12, 0x0000)
    DeclActor(6940,    0,       62400,   1000,    6940,    1200,    62400,   0x007C, 0,  13, 0x0000)
    DeclActor(9000,    0,       64599,   1000,    9000,    1200,    64599,   0x007C, 0,  14, 0x0000)
    DeclActor(11500,   0,       62400,   1000,    11500,   1200,    62400,   0x007C, 0,  15, 0x0000)
    DeclActor(11500,   0,       55800,   1000,    11500,   1200,    55800,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_2B8",          # 00, 0
        "Function_1_370",          # 01, 1
        "Function_2_393",          # 02, 2
        "Function_3_3B0",          # 03, 3
        "Function_4_7F2",          # 04, 4
        "Function_5_C84",          # 05, 5
        "Function_6_D4A",          # 06, 6
        "Function_7_E10",          # 07, 7
        "Function_8_ED6",          # 08, 8
        "Function_9_F9C",          # 09, 9
        "Function_10_1062",        # 0A, 10
        "Function_11_1128",        # 0B, 11
        "Function_12_11EE",        # 0C, 12
        "Function_13_12B4",        # 0D, 13
        "Function_14_137A",        # 0E, 14
        "Function_15_1440",        # 0F, 15
        "Function_16_1506",        # 10, 16
        "Function_17_15CC",        # 11, 17
    ))


    def Function_0_2B8(): pass

    label("Function_0_2B8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2F8"),
        (1, "loc_304"),
        (2, "loc_310"),
        (3, "loc_31C"),
        (4, "loc_328"),
        (5, "loc_334"),
        (6, "loc_340"),
        (SWITCH_DEFAULT, "loc_34C"),
    )


    label("loc_2F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_304")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_310")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_31C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_328")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_334")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_340")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_34C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_36F")

    Return()

    # Function_0_2B8 end

    def Function_1_370(): pass

    label("Function_1_370")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_392")
    Event(0, 3)

    label("loc_392")

    Return()

    # Function_1_370 end

    def Function_2_393(): pass

    label("Function_2_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AA")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_3AA")

    OP_1B(0xE, 0x0, 0x11)
    Return()

    # Function_2_393 end

    def Function_3_3B0(): pass

    label("Function_3_3B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(250, 1000, 52660, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 0, 0, 52500, 0)
    SetChrPos(0x102, 1200, 0, 52500, 0)
    SetChrPos(0x103, 0, 0, 51300, 0)
    SetChrPos(0x104, 1200, 0, 51300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45E")
    SetChrPos(0x109, -1200, 0, 51900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_489")

    label("loc_45E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_489")
    SetChrPos(0x10A, -1200, 0, 51900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_489")

    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0000FThis is the research ward's reference\x01",
            "room, right?\x02\x03",
            "And, somehow, Flora got the overdue\x01",
            "book mixed up with the other books on\x01",
            "one of these shelves.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2900, 1000, 60120, 4000)
    MoveCamera(45, 19, 0, 4000)
    OP_6E(440, 4000)
    SetCameraDistance(28640, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(250, 1000, 52660, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_622")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_622")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#0006FYeah, this is a lot more than I was\x01",
            "expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0106FThis may take a while...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FWhat a waste of time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FIt's all a part of the job. No choice\x01",
            "but to tear apart this place and find\x01",
            "the sucker, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FRight. Let's give this our best shot,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_791")

    ChrTalk(
        0x109,
        "#6P#0501FI'll help out, too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B3")

    label("loc_791")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B3")

    ChrTalk(
        0x10A,
        "#6P#0603F...\x02",
    )

    CloseMessageWindow()

    label("loc_7B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7D8")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_7D8")

    SetChrPos(0x0, 0, 0, 52500, 0)
    OP_29(0x28, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_3_3B0 end

    def Function_4_7F2(): pass

    label("Function_4_7F2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x2D8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D8, 1)
    EventBegin(0x0)
    Fade(500)
    OP_68(4520, 1000, 62040, 0)
    MoveCamera(54, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19850, 0)
    SetChrPos(0x101, 4140, 0, 61890, 90)
    SetChrPos(0x102, 3110, 0, 62550, 90)
    SetChrPos(0x103, 2910, 0, 60910, 45)
    SetChrPos(0x104, 4100, 0, 63510, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E7")
    SetChrPos(0x109, 4030, 0, 60190, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_912")

    label("loc_8E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_912")
    SetChrPos(0x10A, 4030, 0, 60190, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_912")

    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0005FWait a second...!\x02\x03",
            "#0000FYep, there's the library's stamp.\x01",
            "This must be the book Flora\x01",
            "checked out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AF")

    ChrTalk(
        0x109,
        "#12P#0500FWe did it!\x02",
    )

    CloseMessageWindow()

    label("loc_9AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A3B")

    ChrTalk(
        0x102,
        "#6P#0106FTh-Thank goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0211FI was on the verge of developing\x01",
            "an irrational hatred of bookshelves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B35")

    label("loc_A3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AA9")

    ChrTalk(
        0x102,
        "#6P#0100FThank goodness it was here, after all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0206FI need to recharge.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B35")

    label("loc_AA9")


    ChrTalk(
        0x102,
        "#6P#0100FWe're lucky to have found it so quickly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FI am just relieved we did not have to\x01",
            "analyze every single bookshelf.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B35")


    ChrTalk(
        0x104,
        (
            "#5P#0300FWell, our job's become a heck of a lot\x01",
            "easier, now that we've found it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        "#0000FExactly. Ready to move, everyone?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C22")

    ChrTalk(
        0x10A,
        (
            "#12P#0606F(What are they thinking, squandering\x01",
            "time in a place like this...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C22")

    OP_29(0x28, 0x1, 0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4B")
    OP_29(0x28, 0x1, 0x1F)

    label("loc_C4B")

    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C7A")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_C7A")

    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_4_7F2 end

    def Function_5_C84(): pass

    label("Function_5_C84")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0F")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_D46")

    label("loc_D0F")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D46")

    TalkEnd(0xFF)
    Return()

    # Function_5_C84 end

    def Function_6_D4A(): pass

    label("Function_6_D4A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD5")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 1)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_E0C")

    label("loc_DD5")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E0C")

    TalkEnd(0xFF)
    Return()

    # Function_6_D4A end

    def Function_7_E10(): pass

    label("Function_7_E10")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9B")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 2)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_ED2")

    label("loc_E9B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_ED2")

    TalkEnd(0xFF)
    Return()

    # Function_7_E10 end

    def Function_8_ED6(): pass

    label("Function_8_ED6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F61")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_F98")

    label("loc_F61")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F98")

    TalkEnd(0xFF)
    Return()

    # Function_8_ED6 end

    def Function_9_F9C(): pass

    label("Function_9_F9C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1027")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 4)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_105E")

    label("loc_1027")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_105E")

    TalkEnd(0xFF)
    Return()

    # Function_9_F9C end

    def Function_10_1062(): pass

    label("Function_10_1062")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10ED")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 5)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1124")

    label("loc_10ED")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1124")

    TalkEnd(0xFF)
    Return()

    # Function_10_1062 end

    def Function_11_1128(): pass

    label("Function_11_1128")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B3")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 6)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_11EA")

    label("loc_11B3")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_11EA")

    TalkEnd(0xFF)
    Return()

    # Function_11_1128 end

    def Function_12_11EE(): pass

    label("Function_12_11EE")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1279")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 7)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_12B0")

    label("loc_1279")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_12B0")

    TalkEnd(0xFF)
    Return()

    # Function_12_11EE end

    def Function_13_12B4(): pass

    label("Function_13_12B4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133F")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1376")

    label("loc_133F")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1376")

    TalkEnd(0xFF)
    Return()

    # Function_13_12B4 end

    def Function_14_137A(): pass

    label("Function_14_137A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1405")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 1)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_143C")

    label("loc_1405")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_143C")

    TalkEnd(0xFF)
    Return()

    # Function_14_137A end

    def Function_15_1440(): pass

    label("Function_15_1440")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CB")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 2)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1502")

    label("loc_14CB")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1502")

    TalkEnd(0xFF)
    Return()

    # Function_15_1440 end

    def Function_16_1506(): pass

    label("Function_16_1506")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1591")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd searched the bookshelf, top to bottom.\x02\x03",
            "Unfortunately, Flora's overdue book wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_15C8")

    label("loc_1591")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The overdue book is not on this bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_15C8")

    TalkEnd(0xFF)
    Return()

    # Function_16_1506 end

    def Function_17_15CC(): pass

    label("Function_17_15CC")

    EventBegin(0x1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 0)
    MenuCmd(1, 0, "[Exit research ward]")
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(1, 0, "[Cancel]")
    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_163E"),
        (1, "loc_164D"),
        (2, "loc_167A"),
        (SWITCH_DEFAULT, "loc_1689"),
    )


    label("loc_163E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1689")

    label("loc_164D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1675")

    label("loc_166B")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1675")

    Jump("loc_1689")

    label("loc_167A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1689")

    label("loc_1689")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_16A5"),
        (1, "loc_17FC"),
        (2, "loc_1817"),
        (SWITCH_DEFAULT, "loc_1832"),
    )


    label("loc_16A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17A3")

    ChrTalk(
        0x101,
        (
            "#0005FWe still don't know whether Doctor Guenter\x01",
            "is here or not, but the receptionist should be\x01",
            "able to tell us.\x02\x03",
            "#0000FBesides, we aren't hospital staff, so it wouldn't\x01",
            "be a good idea to go barging in on them.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 50500, 0)
    EventEnd(0x4)
    Jump("loc_1832")

    label("loc_17A3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17CD")
    SetScenarioFlags(0x5C, 0)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_17F7")

    label("loc_17CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17EC")
    SetScenarioFlags(0x5C, 1)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_17F7")

    label("loc_17EC")

    EventEnd(0x5)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_17F7")

    Jump("loc_1832")

    label("loc_17FC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Jump("loc_1832")

    label("loc_1817")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 50500, 0)
    EventEnd(0x4)
    Jump("loc_1832")

    label("loc_1832")

    Return()

    # Function_17_15CC end

    SaveToFile()

Try(main)
