from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c047c.bin",                # FileName
        "c047c",                    # MapName
        "c047c",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 37, 0, 1, 0, 2],
    )

    BuildStringList((
        "c047c",                  # 0
        "Proprietor Drake",       # 1
        "Cherry",                 # 2
        "Galetti",                # 3
        "Elinda",                 # 4
        "Raytarossa",             # 5
        "Old Man Rick",           # 6
        "Miner Gantz",            # 7
        "Miner Marlow",           # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Tourist",                # 12
        "Erebonian Noble",        # 13
        "Tourist",                # 14
        "Philia",                 # 15
        "Lan",                    # 16
        "Ada",                    # 17
    ))

    AddCharChip((
        "chr/ch20002.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch20402.itc",                   # 02
        "chr/ch34300.itc",                   # 03
        "chr/ch23600.itc",                   # 04
        "chr/ch25800.itc",                   # 05
        "chr/ch25900.itc",                   # 06
        "chr/ch26902.itc",                   # 07
        "chr/ch27000.itc",                   # 08
        "chr/ch27100.itc",                   # 09
        "chr/ch33100.itc",                   # 0A
        "chr/ch33302.itc",                   # 0B
        "chr/ch30702.itc",                   # 0C
        "chr/ch26200.itc",                   # 0D
    ))

    DeclNpc(-899,    4000,    21299,   180,  261,  0x0, 0,   5,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6199,    -1000,   8000,    270,  261,  0x0, 0,   9,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       -1000,   13649,   180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6500,   -1000,   6000,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(1350,    -949,    11500,   0,    261,  0x0, 0,   11,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   0,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(6699,    4250,    17979,   90,   277,  0x0, 0,   12,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(6510,    4000,    18979,   135,  261,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       -1000,   4219,    360,  405,  0x0, 0,   1,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-3019,   -1000,   3390,    315,  277,  0x0, 0,   3,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-4519,   -1000,   9789,    225,  261,  0x0, 0,   4,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(50,      4000,    18950,   0,    261,  0x0, 0,   7,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-4570,   -1000,   13279,   0,    405,  0x0, 0,   10,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-3400,   -949,    4409,    270,  261,  0x0, 0,   2,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-900,    4000,    20000,   2000,    -900,    5500,    21300,   0x007E, 0,  3,  0x0000)
    DeclActor(5240,    -1000,   8000,    1200,    6200,    500,     8000,    0x007E, 0,  7,  0x0000)
    DeclActor(-920,    -1000,   12050,   1700,    0,       500,     13650,   0x007E, 0,  9,  0x0000)
    DeclActor(-4500,   -1000,   6000,    1500,    -6500,   500,     6000,    0x007E, 0,  11, 0x0000)
    DeclActor(7530,    4000,    17960,   1800,    7530,    5500,    17960,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    15750,   1800,    7530,    5500,    15750,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    13410,   1800,    7530,    5500,    13410,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    10460,   1800,    7530,    5500,    10460,   0x007C, 0,  26, 0x0000)
    DeclActor(7530,    4000,    8300,    1800,    7530,    5500,    8300,    0x007C, 0,  26, 0x0000)

    ScpFunction((
        "Function_0_460",          # 00, 0
        "Function_1_518",          # 01, 1
        "Function_2_5AF",          # 02, 2
        "Function_3_5EE",          # 03, 3
        "Function_4_5F2",          # 04, 4
        "Function_5_EBC",          # 05, 5
        "Function_6_1012",         # 06, 6
        "Function_7_10D6",         # 07, 7
        "Function_8_10DA",         # 08, 8
        "Function_9_17A9",         # 09, 9
        "Function_10_17AD",        # 0A, 10
        "Function_11_1D80",        # 0B, 11
        "Function_12_1D84",        # 0C, 12
        "Function_13_2171",        # 0D, 13
        "Function_14_27F1",        # 0E, 14
        "Function_15_2DC6",        # 0F, 15
        "Function_16_339E",        # 10, 16
        "Function_17_377F",        # 11, 17
        "Function_18_39F3",        # 12, 18
        "Function_19_39FD",        # 13, 19
        "Function_20_3AAA",        # 14, 20
        "Function_21_3CDB",        # 15, 21
        "Function_22_3DC8",        # 16, 22
        "Function_23_4196",        # 17, 23
        "Function_24_45DB",        # 18, 24
        "Function_25_4669",        # 19, 25
        "Function_26_4735",        # 1A, 26
        "Function_27_47C2",        # 1B, 27
        "Function_28_4855",        # 1C, 28
    ))


    def Function_0_460(): pass

    label("Function_0_460")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4A0"),
        (1, "loc_4AC"),
        (2, "loc_4B8"),
        (3, "loc_4C4"),
        (4, "loc_4D0"),
        (5, "loc_4DC"),
        (6, "loc_4E8"),
        (SWITCH_DEFAULT, "loc_4F4"),
    )


    label("loc_4A0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4AC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4B8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4C4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4D0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4DC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_4F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_500")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_517")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_500")

    label("loc_517")

    Return()

    # Function_0_460 end

    def Function_1_518(): pass

    label("Function_1_518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_527")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 28)

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_550")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x8, -4570, -1000, 14750, 180)
    SetChrFlags(0x8, 0x10)
    Jump("loc_5AE")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_55E")
    Jump("loc_5AE")

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_571")
    SetChrFlags(0x8, 0x10)
    Jump("loc_5AE")

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_58E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_589")
    SetChrFlags(0x8, 0x10)

    label("loc_589")

    Jump("loc_5AE")

    label("loc_58E")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x11, 1000, -1000, 3500, 315)

    label("loc_5AE")

    Return()

    # Function_1_518 end

    def Function_2_5AF(): pass

    label("Function_2_5AF")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -6000, -1000, 16000, 5000, 5000, 0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5ED")
    OP_65(0x0, 0x1)

    label("loc_5ED")

    Return()

    # Function_2_5AF end

    def Function_3_5EE(): pass

    label("Function_3_5EE")

    Call(0, 4)
    Return()

    # Function_3_5EE end

    def Function_4_5F2(): pass

    label("Function_4_5F2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_684")
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x8,
        (
            "It is good to see you again, Count.\x01",
            "It's been far too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please take one of the VIP seats\x01",
            "over in the back.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_EB8")

    label("loc_684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_6F1")

    ChrTalk(
        0x8,
        (
            "I welcome you to Barca Casino,\x01",
            "everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "We hope to give you the time of your life.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EB8")

    label("loc_6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 1)), scpexpr(EXPR_END)), "loc_841")

    ChrTalk(
        0x8,
        (
            "The city is awfully congested thanks to the\x01",
            "festival, so I'm a touch worried about children\x01",
            "getting lost in the crowds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If he's not in the Entertainment District, is there\x01",
            "a possibility he followed the parade over to\x01",
            "Central Square?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I sincerely apologize for not being able to\x01",
            "offer you much help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1B")

    label("loc_841")


    ChrTalk(
        0x8,
        (
            "The city's a lot more congested thanks\x01",
            "to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm a touch worried about children getting\x01",
            "lost in the crowds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWell, actually... We're in the middle of searching\x01",
            "for one right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "O-Oh. Really? My apologies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm. I cannot recall seeing any children\x01",
            "on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As for the first floor, I'd advise you ask\x01",
            "Cherry for more details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If Cherry hasn't seen the missing child, then\x01",
            "odds are he hasn't set foot in here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 1)

    label("loc_A1B")

    Jump("loc_EB8")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AB8")

    ChrTalk(
        0x8,
        (
            "The city's a lot more congested thanks\x01",
            "to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm a touch worried about children getting\x01",
            "lost in the crowds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1A")

    label("loc_AB8")


    ChrTalk(
        0x8,
        (
            "I welcome you to Barca Casino,\x01",
            "everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "We hope to give you the time of your life.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B1A")

    Jump("loc_EB8")

    label("loc_B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_BA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(
        0x8,
        (
            "I believe it's about time for you to\x01",
            "return home, miss.\x01",
            "You've yet to turn 20, if I'm not mistaken.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA2")

    label("loc_B9F")

    Call(0, 5)

    label("loc_BA2")

    Jump("loc_EB8")

    label("loc_BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C5F")

    ChrTalk(
        0x8,
        (
            "...Ah, damn it.\x01",
            "Wanna switch spots with me, Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FHell naw. Take some personal responsibility,\x01",
            "my man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Damn you. The hell you sulkin' for?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C62")

    label("loc_C5F")

    Call(0, 6)

    label("loc_C62")

    Jump("loc_EB8")

    label("loc_C67")

    TurnDirection(0x8, 0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D13")

    ChrTalk(
        0x8,
        (
            "Sure, we get a ton of customers, but\x01",
            "that's no problem for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's cute of you to worry about me, but\x01",
            "I'll contact you if anything pops up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB8")

    label("loc_D13")


    ChrTalk(
        0x8,
        "Back again, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You had the time of your life yesterday,\x01",
            "so you're here to see me again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FNope. Duty calls, my friend.\x02\x03",
            "Good to see your casino's still alive\x01",
            "and kickin', eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah. Haven't been having much trouble\x01",
            "these days, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's cute of you to worry about me, but\x01",
            "I'll contact you if anything pops up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FGot'cha. I'll be back again soon to\x01",
            "see how things are goin'.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_EB8")

    TalkEnd(0x8)
    Return()

    # Function_4_5F2 end

    def Function_5_EBC(): pass

    label("Function_5_EBC")

    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x13, 0x0)

    ChrTalk(
        0x8,
        (
            "Is it not time for you to return home,\x01",
            "miss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm a little busy at the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "What?! Wait, stop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "C'moooooon! Today's the festival!\x01",
            "Don't be such a spoilsport!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FD2")

    ChrTalk(
        0x104,
        (
            "#0303F(Heh. That's rare. Owner's havin' a\x01",
            "hard time keeping up.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100A")

    label("loc_FD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_100A")

    ChrTalk(
        0x101,
        "#0003F(He's surprisingly popular.)\x02",
    )

    CloseMessageWindow()

    label("loc_100A")

    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_5_EBC end

    def Function_6_1012(): pass

    label("Function_6_1012")

    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x13, 0x0)

    ChrTalk(
        0x13,
        "Hey there, Mr. Owner. How old are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Is it true you're ex-mafia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With all due respect, miss, you're drunk.\x01",
            "How about we leave it at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Aawwww... ㈱㈱\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_6_1012 end

    def Function_7_10D6(): pass

    label("Function_7_10D6")

    Call(0, 8)
    Return()

    # Function_7_10D6 end

    def Function_8_10DA(): pass

    label("Function_8_10DA")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",          # 0
            "Exchange\x01",      # 1
            "Leave\x01",         # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_113C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_113C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115C")
    OP_AF(0x40)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17A0")

    label("loc_115C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1170")
    Jump("loc_17A0")

    label("loc_1170")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1216")

    ChrTalk(
        0x9,
        (
            "Today's the last day to take advantage\x01",
            "of our big Anniversary Festival promotion!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Go out there and have some fun! ☆\x02",
    )

    CloseMessageWindow()
    Jump("loc_17A0")

    label("loc_1216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_12A3")

    ChrTalk(
        0x9,
        (
            "Looks like everybody ran back here\x01",
            "as soon as the parade ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "C'mon, everyone! Do your best to\x01",
            "win some miraaa! ☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A0")

    label("loc_12A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_14E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 3)), scpexpr(EXPR_END)), "loc_132E")

    ChrTalk(
        0x9,
        (
            "What a cutie! I don't think he came\x01",
            "to the casino, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I looove watching every customer,\x01",
            "you know? ☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DF")

    label("loc_132E")


    ChrTalk(
        0x101,
        (
            "#0001F(I would hope he didn't wander into the casino,\x01",
            "but I'll ask if she knows something about Colin.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if she knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        "Aw, he's gone missing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I don't think he came by here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sure a lovely little boy would stand out\x01",
            "in our casino! ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, I guess you're right. Thank\x01",
            "you for cooperating, ma'am.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)

    label("loc_14DF")

    Jump("loc_17A0")

    label("loc_14E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1573")

    ChrTalk(
        0x9,
        (
            "Looks like everybody ran back here\x01",
            "as soon as the parade ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "C'mon, everyone! Do your best to\x01",
            "spend some miraaa! ☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A0")

    label("loc_1573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_165C")

    ChrTalk(
        0x9,
        (
            "Even though the owner is all rugged-looking,\x01",
            "he's surprisingly super popular!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "*sigh* I guess that's just how it goes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I bet it's that dangerous aura that keeps\x01",
            "attracting all sorts of new customers. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A0")

    label("loc_165C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1706")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16B1")

    ChrTalk(
        0x9,
        (
            "C'mon, Gantz! You can do it!\x01",
            "Just keep dropping mira! ☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1701")

    label("loc_16B1")


    ChrTalk(
        0x9,
        "Gantz is here again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Teehee. I bet he came to lose some more. ☆\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1701")

    Jump("loc_17A0")

    label("loc_1706")


    ChrTalk(
        0x9,
        "Welcome to Barca Casino!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've prepared some more fabulous prizes\x01",
            "for the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I hope you're all up for the challenge! ☆\x02",
    )

    CloseMessageWindow()

    label("loc_17A0")

    Jump("loc_10E7")

    label("loc_17A5")

    TalkEnd(0x9)
    Return()

    # Function_8_10DA end

    def Function_9_17A9(): pass

    label("Function_9_17A9")

    Call(0, 10)
    Return()

    # Function_9_17A9 end

    def Function_10_17AD(): pass

    label("Function_10_17AD")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D7C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                # 0
            "Play Poker\x01",          # 1
            "Play Blackjack\x01",      # 2
            "Leave\x01",               # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1820")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1820")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186B")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_186B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B6")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_18B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18CA")
    Jump("loc_1D77")

    label("loc_18CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D77")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_197E")

    ChrTalk(
        0xA,
        (
            "The count's challenger will be\x01",
            "the owner himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha. Such an important customer must be\x01",
            "offered the highest challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A1D")

    label("loc_197E")


    ChrTalk(
        0xA,
        (
            "The count loves to drop by more often around\x01",
            "this time of year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Given his generosity, he is obviously one of our\x01",
            "regular members of the VIP room.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1A1D")

    Jump("loc_1D77")

    label("loc_1A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1AC5")

    ChrTalk(
        0xA,
        "Everybody has their own unique ability.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Know your limit, play within it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The end result will be obvious if you\x01",
            "try to push your luck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D77")

    label("loc_1AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B8D")

    ChrTalk(
        0xA,
        (
            "You ever think about how gambling gets\x01",
            "super intense without even realizing it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The Anniversary Festival isn't an excuse for\x01",
            "people to start acting without restraint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5F")

    label("loc_1B8D")


    ChrTalk(
        0xA,
        (
            "Anyone who gambles should know\x01",
            "to mind their manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Festival or not, nothing good will come\x01",
            "out of people failing to show some\x01",
            "restraint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Maybe it'd be a good call to\x01",
            "give some extra chips.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1C5F")

    Jump("loc_1D77")

    label("loc_1C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D06")

    ChrTalk(
        0xA,
        (
            "The Entertainment District is definitely a\x01",
            "hotspot for tourists to come and visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh* I'm so over today. This is just\x01",
            "WAY too packed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D77")

    label("loc_1D06")


    ChrTalk(
        0xA,
        "Welcome. You've found the cards table.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What say you to a good match as an\x01",
            "Anniversary Festival memory?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D77")

    Jump("loc_17BA")

    label("loc_1D7C")

    TalkEnd(0xA)
    Return()

    # Function_10_17AD end

    def Function_11_1D80(): pass

    label("Function_11_1D80")

    Call(0, 12)
    Return()

    # Function_11_1D80 end

    def Function_12_1D84(): pass

    label("Function_12_1D84")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",               # 0
            "Play Roulette\x01",      # 1
            "Leave\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DEB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1DEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E36")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_1E36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E4A")
    Jump("loc_2168")

    label("loc_1E4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2168")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1FB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F22")

    ChrTalk(
        0xB,
        (
            "We've made it to the last day of the festival...\x01",
            "I bet something exciting will happen!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's just pure speculation, though.\x01",
            "Would you like to try your hand?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB4")

    label("loc_1F22")


    ChrTalk(
        0xB,
        (
            "Welcome. Would you like to spin\x01",
            "the roulette?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've made it to the last day of the festival...\x01",
            "I bet something exciting will happen!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1FB4")

    Jump("loc_2168")

    label("loc_1FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1FF8")

    ChrTalk(
        0xB,
        "I hope you've all been enjoying yourselves.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2168")

    label("loc_1FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2077")

    ChrTalk(
        0xB,
        "Welcome to the Barca Casino.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We have an opening available right now.\x01",
            "Would you like to give it a spin?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2168")

    label("loc_2077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20E5")

    ChrTalk(
        0xB,
        "Don't go easy on each other, now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Mercy is for the weak. Such is the\x01",
            "law of gambling!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2168")

    label("loc_20E5")


    ChrTalk(
        0xB,
        (
            "People like to take more risks during\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thank you for joining us.\x01",
            "We still have some open seats.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2168")

    Jump("loc_1D91")

    label("loc_216D")

    TalkEnd(0xB)
    Return()

    # Function_12_1D84 end

    def Function_13_2171(): pass

    label("Function_13_2171")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2205")
    Jump("loc_224F")

    label("loc_2205")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2225")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_224F")

    label("loc_2225")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2245")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_224F")

    label("loc_2245")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_224F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_234B")

    ChrTalk(
        0xC,
        "O-Oh... Isn't that the Erebonian noble, Count Carlisle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "He's an influential noble in eastern Erebonia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The rumors claiming that he visits the\x01",
            "Anniversary Festival every year are true...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E9")

    label("loc_234B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_241B")

    ChrTalk(
        0xC,
        (
            "It appears today's Arc en Ciel performance\x01",
            "was a success, as per usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I only wish to be able to experience it once more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Do you think it'd be possible to find\x01",
            "tickets anywhere?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E9")

    label("loc_241B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_25AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_24A3")

    ChrTalk(
        0xC,
        "Is he doing all of the office work by his lonesome?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "The poor mayor has a lot resting on his shoulders.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A7")

    label("loc_24A3")


    ChrTalk(
        0xC,
        (
            "Mayor MacDowell is constantly being summoned\x01",
            "for conferences and parties during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I suppose those responsibilities are packaged\x01",
            "with the position of mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Wasn't his private secretary arrested?\x01",
            "How does his office work get done?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_25A7")

    Jump("loc_27E9")

    label("loc_25AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2662")

    ChrTalk(
        0xC,
        (
            "There are supposed counterfeit dealers that\x01",
            "appear in Crossbell around this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Theirs is a business that takes\x01",
            "advantage of the public's desires.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2762")

    label("loc_2662")


    ChrTalk(
        0xC,
        "Have you already heard about this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There are supposed counterfeit dealers that\x01",
            "appear in Crossbell around this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "They tried to sell counterfeit brand-name\x01",
            "goods to the department store once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Do they not sound treacherous to you?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2762")

    Jump("loc_27E9")

    label("loc_2767")


    ChrTalk(
        0xC,
        (
            "Ilya Platiere was even more stunning than\x01",
            "the rumors had claimed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "She alone was more than worth\x01",
            "the price of admission.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_2171 end

    def Function_14_27F1(): pass

    label("Function_14_27F1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2885")
    Jump("loc_28CF")

    label("loc_2885")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28A5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28CF")

    label("loc_28A5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28C5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28CF")

    label("loc_28C5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28CF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_29B9")

    ChrTalk(
        0xD,
        (
            "Oh, drat! I can feel my luck fading away\x01",
            "as the end of the festival draws near.\x01",
            "The last day's always a sad one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No, no! Today's the day I NEED to hit\x01",
            "the jackpot!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A86")

    label("loc_29B9")


    ChrTalk(
        0xD,
        "I'm going to win big today if it's the last thing I do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I gotta rake in the dough while I still can...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I feel like my luck is going to disappear as soon as\x01",
            "the Anniversary Festival ends.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2A86")

    Jump("loc_2DBE")

    label("loc_2A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2BF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2B26")

    ChrTalk(
        0xD,
        (
            "It's just a festival, but I can see reporters and\x01",
            "officers are much busier than they usually are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Out on the job, are we?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BEE")

    label("loc_2B26")


    ChrTalk(
        0xD,
        (
            "Streets are busy as heck with tourists,\x01",
            "all thanks to that parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Was that miss a reporter? Saw a\x01",
            "young man with a camera following\x01",
            "her, so I guess so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hoho. That's some hard work.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2BEE")

    Jump("loc_2DBE")

    label("loc_2BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2CF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2C5D")

    ChrTalk(
        0xD,
        "Feeling pretty good about the slots today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "It's time to make some money!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CEB")

    label("loc_2C5D")


    ChrTalk(
        0xD,
        (
            "Damn that battle axe! She tried to stop me\x01",
            "from going to the casino again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmph! I still have time, so I can't\x01",
            "give up just yet!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2CEB")

    Jump("loc_2DBE")

    label("loc_2CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2D44")

    ChrTalk(
        0xD,
        "Here they come! It's coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hohoho! I can't stop laughing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DBE")

    label("loc_2D44")


    ChrTalk(
        0xD,
        "Here come the tokens!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I knew I could count on the Anniversary Festival\x01",
            "to bless me with good luck on the slots!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DBE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_27F1 end

    def Function_15_2DC6(): pass

    label("Function_15_2DC6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E5A")
    Jump("loc_2EA4")

    label("loc_2E5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E7A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EA4")

    label("loc_2E7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E9A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EA4")

    label("loc_2E9A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EA4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_302F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FAC")

    ChrTalk(
        0xFE,
        "Argh... I lost again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't get it. I was on fire yesterday!\x01",
            "Shouldn't my luck have carried over?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Damn it, I'll redeem myself tonight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203F...Budding symptoms of addiction.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_302A")

    label("loc_2FAC")


    ChrTalk(
        0xFE,
        (
            "I don't get it, I was on fire yesterday!\x01",
            "Shouldn't my luck have carried over?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Damn it, I'll redeem myself tonight!\x02",
    )

    CloseMessageWindow()

    label("loc_302A")

    Jump("loc_3396")

    label("loc_302F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_30DD")

    ChrTalk(
        0xFE,
        "Hey, listen up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was on a roll on this slot machine\x01",
            "yesterday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it wasn't really enough for me to\x01",
            "break even, but don't sweat the details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3396")

    label("loc_30DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_32E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3246")

    ChrTalk(
        0xFE,
        (
            "I couldn't even win ONE simple game\x01",
            "of roulette yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Couldn't that damn ball have\x01",
            "gone just one rege to the right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FMood of the Goddess depends on luck, man!\x02\x03",
            "#0309FMy life would be complete if She blessed me\x01",
            "with a bit more of it now and then, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FStop sympathizing with him, Randy!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_32E0")

    label("loc_3246")


    ChrTalk(
        0xFE,
        (
            "Couldn't that damn ball have\x01",
            "gone just one rege to the right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "DAMN IT ALL!\x01",
            "I'm going to make all my money back\x01",
            "with these cursed slot machines!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E0")

    Jump("loc_3396")

    label("loc_32E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3300")
    Call(0, 17)
    Jump("loc_3396")

    label("loc_3300")


    ChrTalk(
        0xFE,
        (
            "Ugh... My head is still pounding.\x01",
            "I guess I still have a hangover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dang. I almost envy Logy. Poor soul's\x01",
            "already burnt up all of his money.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3396")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_2DC6 end

    def Function_16_339E(): pass

    label("Function_16_339E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3481")

    ChrTalk(
        0xFE,
        (
            "He managed to win big yesterday, but\x01",
            "he got all cocky today. His mira went\x01",
            "up in a big cloud of smoke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the end of the day, you gotta realize\x01",
            "that casinos are just trying to make\x01",
            "a profit from you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_377B")

    label("loc_3481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_34FB")

    ChrTalk(
        0xFE,
        (
            "Bit of a rare sight to see\x01",
            "Gantz winning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'd better quit before\x01",
            "I get ahead of myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_377B")

    label("loc_34FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_36D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3611")

    ChrTalk(
        0xFE,
        (
            "I've been coming to the casino with\x01",
            "Gantz every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All he does is aim for the big jackpot,\x01",
            "so he rarely ever wins a game...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't you think it's a bit delusional\x01",
            "to think he'll win back all his losses\x01",
            "with a single extraordinary win?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_36CF")

    label("loc_3611")


    ChrTalk(
        0xFE,
        (
            "Y'know, Gantz has been obsessed\x01",
            "with winning a fortune at the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't you think it's a bit delusional\x01",
            "to think he'll win back all his losses\x01",
            "with a single extraordinary win?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36CF")

    Jump("loc_377B")

    label("loc_36D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_377B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36EF")
    Call(0, 17)
    Jump("loc_377B")

    label("loc_36EF")


    ChrTalk(
        0xFE,
        (
            "I tagged along with Gantz to the city\x01",
            "so I could goof off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to hang around here until\x01",
            "the Anniversary Festival wraps up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_377B")

    TalkEnd(0xFE)
    Return()

    # Function_16_339E end

    def Function_17_377F(): pass

    label("Function_17_377F")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0xF, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_381B")
    Jump("loc_3865")

    label("loc_381B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_383B")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3865")

    label("loc_383B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_385B")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3865")

    label("loc_385B")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3865")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    TurnDirection(0xF, 0xE, 0)

    ChrTalk(
        0xE,
        (
            "Ugh...\x01",
            "My head's still throbbing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "You probably had too many shots, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Our mayor's pretty generous. It was\x01",
            "kind of him to offer to buy us all drinks\x01",
            "during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "And thanks to that, Logy's still enjoying\x01",
            "his beauty sleep over at Der Ziegel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, either way, I had an awesome time\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    OP_93(0xF, 0x87, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_17_377F end

    def Function_18_39F3(): pass

    label("Function_18_39F3")

    TalkBegin(0xFE)
    Call(0, 19)
    TalkEnd(0xFE)
    Return()

    # Function_18_39F3 end

    def Function_19_39FD(): pass

    label("Function_19_39FD")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x11,
        "Good luck, sweetie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Make our wallets ten times bigger, and let's hit up\x01",
            "Mishelam for a sweet celebration afterwards!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hahaha! Leave it to me!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_19_39FD end

    def Function_20_3AAA(): pass

    label("Function_20_3AAA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B3E")
    Jump("loc_3B88")

    label("loc_3B3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B5E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B88")

    label("loc_3B5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B7E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B88")

    label("loc_3B7E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B88")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3BEB")
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x15,
        (
            "Next time! Next time, I'll...\x01",
            "Damn it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD3")

    label("loc_3BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3C8B")

    ChrTalk(
        0x15,
        "Aww... I was on fire the whole night.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Sh-She managed to empty my pockets\x01",
            "on the very last game!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "M-My mira...\x01",
            "My mountain of chips!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD3")

    label("loc_3C8B")


    ChrTalk(
        0x15,
        "Do you play, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Hahaha. Try not to get beaten\x01",
            "too much, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_3AAA end

    def Function_21_3CDB(): pass

    label("Function_21_3CDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3D15")

    ChrTalk(
        0x11,
        "D-Don't get too carried away, dear.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DC4")

    label("loc_3D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3D7D")

    ChrTalk(
        0x11,
        "Waaaaah... That was my last game!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That damn dealer had to have\x01",
            "cheated, right?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC4")

    label("loc_3D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3DC1")

    ChrTalk(
        0x11,
        "Woohoo! Victory is mine again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "What a show!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DC4")

    label("loc_3DC1")

    Call(0, 19)

    label("loc_3DC4")

    TalkEnd(0xFE)
    Return()

    # Function_21_3CDB end

    def Function_22_3DC8(): pass

    label("Function_22_3DC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3EDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3E4A")

    ChrTalk(
        0x12,
        "It sure feels good to earn some cash.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I'm absolutely stopping by this\x01",
            "casino again next year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED5")

    label("loc_3E4A")


    ChrTalk(
        0x12,
        (
            "My pockets are just FILLED with money\x01",
            "I won this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I think I'll hit up the casinos even longer\x01",
            "next Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_3ED5")

    Jump("loc_4192")

    label("loc_3EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_401A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3F7C")

    ChrTalk(
        0x12,
        (
            "I need to play longer on days where\x01",
            "I'm pulling a lucky streak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Naturally, I'm mature enough\x01",
            "to know when to throw in the towel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4015")

    label("loc_3F7C")


    ChrTalk(
        0x12,
        "I'm feeling lucky today, punk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "On days like today, I need to play\x01",
            "for longer, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I once again feel luck coursing through my veins!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_4015")

    Jump("loc_4192")

    label("loc_401A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_40F9")

    ChrTalk(
        0x12,
        (
            "There's a big difference between\x01",
            "losing and just losing mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Don't just give up because you lost SOME mira!\x01",
            "An astounding victory is still within your reach!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Gambling really makes you think...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4192")

    label("loc_40F9")


    ChrTalk(
        0x12,
        (
            "Roulette is a series of battles...\x01",
            "Almost like a war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "When you get excited and start\x01",
            "getting cocky, you lose mira...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Self-control is key.\x02",
    )

    CloseMessageWindow()

    label("loc_4192")

    TalkEnd(0xFE)
    Return()

    # Function_22_3DC8 end

    def Function_23_4196(): pass

    label("Function_23_4196")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_422A")
    Jump("loc_4274")

    label("loc_422A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_424A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4274")

    label("loc_424A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_426A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4274")

    label("loc_426A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4274")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_43C3")
    SetChrSubChip(0x13, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4318")

    ChrTalk(
        0x13,
        "*glug* *glug* Paaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Stoopid Drake... Why da hell won't he jusht gimme\x01",
            "shome attention?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43BE")

    label("loc_4318")


    ChrTalk(
        0x13,
        (
            "*glug* That damn Drake keepsh brushin' me\x01",
            "off... *hic* What'sh da big idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "To hell with him! And to hell with good company!\x01",
            "*glug* *glug* *glug* *glug*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_43BE")

    Jump("loc_45D3")

    label("loc_43C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4481")

    ChrTalk(
        0x13,
        (
            "I wanna hang out with da owner, but he'sh been\x01",
            "tellin' me to shove off! *hic*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Pretty rude, dude. Stiiill, he's so cuuute when\x01",
            "he'sh all sherious. K-U-E-T-E! CUTE! ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45D3")

    label("loc_4481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_453C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4534")
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x13, 0x0)

    ChrTalk(
        0x13,
        (
            "Drake, you big bully! *hic* Make a shweet girl\x01",
            "cry, why don'tcha?! Hurt me shome more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "...Mmmmm. Actually, I might be into that. ㈱㈱\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_4537")

    label("loc_4534")

    Call(0, 5)

    label("loc_4537")

    Jump("loc_45D3")

    label("loc_453C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_45D0")

    ChrTalk(
        0x13,
        "Mmm... I think Drake is my type. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "The hotel sounds so dull right now. Maybe I'll\x01",
            "just spend the rest of my day here. ㈱㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45D3")

    label("loc_45D0")

    Call(0, 6)

    label("loc_45D3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_4196 end

    def Function_24_45DB(): pass

    label("Function_24_45DB")

    TalkBegin(0xFE)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x14,
        "I hope to enjoy myself once again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Has the room been prepared, Drake?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It has. Allow me to lead you to the back.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_24_45DB end

    def Function_25_4669(): pass

    label("Function_25_4669")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4734")
    OP_29(0x46, 0x1, 0x2)

    ChrTalk(
        0x101,
        (
            "#0003F(All right, that's a wrap on the Entertainment\x01",
            "District's investigation.)\x02\x03",
            "#0001F(Looks like the Back Alley is next...\x01",
            "Let's continue the investigation there!)\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)

    label("loc_4734")

    Return()

    # Function_25_4669 end

    def Function_26_4735(): pass

    label("Function_26_4735")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Play Slots\x01",      # 0
            "Leave\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47BE")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_47BE")

    TalkEnd(0xFF)
    Return()

    # Function_26_4735 end

    def Function_27_47C2(): pass

    label("Function_27_47C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4854")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_47F0")
    Sleep(500)
    Jump("loc_4838")

    label("loc_47F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4807")
    Sleep(150)
    Jump("loc_4838")

    label("loc_4807")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_481E")
    Sleep(200)
    Jump("loc_4838")

    label("loc_481E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4835")
    Sleep(300)
    Jump("loc_4838")

    label("loc_4835")

    Sleep(400)

    label("loc_4838")

    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    Jump("Function_27_47C2")

    label("loc_4854")

    Return()

    # Function_27_47C2 end

    def Function_28_4855(): pass

    label("Function_28_4855")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch36300.itc", 0x1E)
    LoadChrToIndex("chr/ch36400.itc", 0x1F)
    LoadChrToIndex("chr/ch36500.itc", 0x20)
    LoadEffect(0x0, "event\\ev300_00.eff")
    LoadEffect(0x1, "event\\ev399_00.eff")
    ClearMapObjFlags(0x7, 0x4)
    OP_68(-4120, 4270, 6410, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(20500, 0)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x104, -3700, -1200, 6430, 315)
    SetChrPos(0x16, -3370, -1000, 7440, 315)
    SetChrPos(0x18, -2450, -1000, 5890, 315)
    SetChrPos(0x17, -3450, -1000, 5410, 315)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrChipByIndex(0x18, 0x20)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    OP_68(-6000, 0, 8000, 0)
    MoveCamera(43, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -5950, -70, 8050, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    MoveCamera(33, 33, 0, 4000)
    SetCameraDistance(17500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(-4120, 0, 6410, 2000)
    MoveCamera(80, 23, 0, 2000)
    SetCameraDistance(19000, 2000)
    Sleep(3000)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 136000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1332, 255, 100, 0)
    Sound(506, 0, 100, 0)
    Sound(565, 0, 100, 0)
    Sleep(5000)
    Sound(85, 0, 100, 0)
    Sleep(500)
    Sound(1290, 255, 100, 0)

    def lambda_4A60():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_4A60)

    def lambda_4A6D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_4A6D)

    def lambda_4A7A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_4A7A)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    BeginChrThread(0x16, 1, 0, 27)
    BeginChrThread(0x18, 1, 0, 27)
    BeginChrThread(0x17, 1, 0, 27)
    Sleep(2000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 7)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_4855 end

    SaveToFile()

Try(main)
