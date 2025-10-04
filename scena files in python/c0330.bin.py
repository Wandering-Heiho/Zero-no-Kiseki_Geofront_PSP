from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0330.bin",                # FileName
        "c0330",                    # MapName
        "c0330",                    # Location
        0x002C,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 44, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0330",                  # 0
        "Harold",                 # 1
        "Sophia",                 # 2
        "Colin",                  # 3
        "Harold",                 # 4
        "Sophia",                 # 5
        "Colin",                  # 6
        "Cindy",                  # 7
        "Creil",                  # 8
    ))

    AddCharChip((
        "chr/ch09300.itc",                   # 00
        "chr/ch09302.itc",                   # 01
        "chr/ch09400.itc",                   # 02
        "chr/ch09402.itc",                   # 03
        "chr/ch07200.itc",                   # 04
        "chr/ch07202.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch33300.itc",                   # 07
    ))

    DeclNpc(-340,    0,       4409,    315,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(550,     0,       2039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(37479,   0,       3799,    180,  257,  0x0, 0,   4,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(34450,   200,     3339,    225,  389,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(34340,   200,     519,     315,  389,  0x0, 0,   3,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(31280,   200,     3420,    135,  389,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(33299,   0,       -100,    0,    405,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(35319,   0,       1679,    277,  389,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)

    ScpFunction((
        "Function_0_1E4",          # 00, 0
        "Function_1_29C",          # 01, 1
        "Function_2_2C7",          # 02, 2
        "Function_3_2F2",          # 03, 3
        "Function_4_353",          # 04, 4
        "Function_5_75E",          # 05, 5
        "Function_6_7B1",          # 06, 6
        "Function_7_1780",         # 07, 7
        "Function_8_1B83",         # 08, 8
        "Function_9_1CAD",         # 09, 9
        "Function_10_2FE4",        # 0A, 10
        "Function_11_326D",        # 0B, 11
        "Function_12_3361",        # 0C, 12
        "Function_13_3462",        # 0D, 13
        "Function_14_3650",        # 0E, 14
        "Function_15_3919",        # 0F, 15
        "Function_16_4518",        # 10, 16
        "Function_17_4C60",        # 11, 17
        "Function_18_4D9D",        # 12, 18
        "Function_19_4F52",        # 13, 19
    ))


    def Function_0_1E4(): pass

    label("Function_0_1E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_224"),
        (1, "loc_230"),
        (2, "loc_23C"),
        (3, "loc_248"),
        (4, "loc_254"),
        (5, "loc_260"),
        (6, "loc_26C"),
        (SWITCH_DEFAULT, "loc_278"),
    )


    label("loc_224")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_230")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_23C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_248")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_254")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_260")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_26C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_278")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_284")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_29B")

    Return()

    # Function_0_1E4 end

    def Function_1_29C(): pass

    label("Function_1_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C6")
    OP_94(0xFE, 0x9268, 0x157C, 0x8F48, 0x85C, 0x3E8)
    Sleep(300)
    Jump("Function_1_29C")

    label("loc_2C6")

    Return()

    # Function_1_29C end

    def Function_2_2C7(): pass

    label("Function_2_2C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F1")
    OP_94(0xFE, 0xFFFFF240, 0x80C, 0xC58, 0x139C, 0x3E8)
    Sleep(300)
    Jump("Function_2_2C7")

    label("loc_2F1")

    Return()

    # Function_2_2C7 end

    def Function_3_2F2(): pass

    label("Function_3_2F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_352")
    OP_95(0xFE, 35110, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(2500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(100)
    OP_95(0xFE, 37510, 0, -1160, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(100)
    Jump("Function_3_2F2")

    label("loc_352")

    Return()

    # Function_3_2F2 end

    def Function_4_353(): pass

    label("Function_4_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_393")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, 0, 0, 5360, 180)
    SetChrPos(0xA, 0, 0, 3930, 360)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A6")
    SetChrFlags(0x9, 0x80)
    Jump("loc_75D")

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3FE")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0x9, 35510, 0, 3010, 222)
    SetChrPos(0xA, 37530, 0, -1240, 89)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3F9")
    ClearChrFlags(0xE, 0x10)

    label("loc_3F9")

    Jump("loc_75D")

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_434")
    SetChrPos(0x9, -370, 0, -2190, 180)
    SetChrPos(0xA, -1230, 0, -1880, 135)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_45B")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_75D")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4A7")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 10, 0, -2230, 180)
    SetChrPos(0x9, 32350, 0, 7580, 270)
    SetChrPos(0xA, 30940, 0, 7580, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4BF")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_75D")

    label("loc_4BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_519")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -490, 0, 5140, 180)
    SetChrPos(0x9, 790, 0, 4260, 270)
    SetChrPos(0xA, -690, 0, 3590, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_514")
    SetChrFlags(0x8, 0x10)

    label("loc_514")

    Jump("loc_75D")

    label("loc_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_567")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, -1230, 0, 5370, 135)
    SetChrPos(0xA, -1670, 0, 3900, 45)
    BeginChrThread(0xA, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_562")
    SetChrFlags(0x8, 0x10)

    label("loc_562")

    Jump("loc_75D")

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5BD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x8, 790, 0, 4260, 270)
    SetChrPos(0x9, -490, 0, 5140, 180)
    SetChrPos(0xA, -690, 0, 3590, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_75D")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_61A")
    SetChrPos(0x9, 5170, 0, 3210, 360)
    SetChrPos(0xA, 34480, 0, 5610, 315)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_615")
    SetChrFlags(0x9, 0x10)

    label("loc_615")

    Jump("loc_75D")

    label("loc_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_639")
    SetChrPos(0x9, -370, 0, -2190, 180)
    Jump("loc_75D")

    label("loc_639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_695")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, 35510, 0, 3010, 222)
    SetChrPos(0xA, 38540, 0, 320, 180)
    SetChrPos(0xF, 35110, 0, 1240, 315)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xF, 0, 0, 3)
    Jump("loc_75D")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6CB")
    SetChrPos(0x9, 40930, 0, -1640, 90)
    SetChrPos(0xA, 40920, 0, -410, 135)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_703")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -1230, 0, 5370, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FE")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_6FE")

    Jump("loc_75D")

    label("loc_703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_735")
    SetChrPos(0x9, 4560, 0, 10380, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_730")
    SetChrFlags(0x9, 0x10)

    label("loc_730")

    Jump("loc_75D")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_75D")
    SetChrPos(0x9, 40930, 0, -1640, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_75D")
    SetChrFlags(0x9, 0x10)

    label("loc_75D")

    Return()

    # Function_4_353 end

    def Function_5_75E(): pass

    label("Function_5_75E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_777")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_77D")

    label("loc_777")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_799")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7B0")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7B0")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7B0")

    label("loc_7B0")

    Return()

    # Function_5_75E end

    def Function_6_7B1(): pass

    label("Function_6_7B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_98C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_870")

    ChrTalk(
        0x8,
        (
            "#3600FTo think that one of our neighbors\x01",
            "would disappear... I'd like to assist\x01",
            "you in any way possible.\x02\x03",
            "I plan to support my family to\x01",
            "the best of my ability.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_987")

    label("loc_870")


    ChrTalk(
        0x8,
        (
            "#3600FMy wife has gone to visit Miss Creil.\x02\x03",
            "#3603FYou see, Miss Creil and my wife are\x01",
            "close friends. I'm sure Sophia is\x01",
            "worried about her...\x02\x03",
            "#3600FIt's wonderful that she has a friend she\x01",
            "can lean on in times like these. I intend\x01",
            "on supporting both of them, of course.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_987")

    Jump("loc_177C")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_ECE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 7)), scpexpr(EXPR_END)), "loc_C53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A7B")

    ChrTalk(
        0x8,
        (
            "#3603FThank you so much for yesterday...\x01",
            "And I truly apologize for having you sit\x01",
            "through a long and terrible story.\x02\x03",
            "#3601FPlease forgive me, as I am still trying\x01",
            "to wrap my head around the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4E")

    label("loc_A7B")


    ChrTalk(
        0x8,
        (
            "#3603FThank you so much for yesterday...\x01",
            "And I truly apologize for having you sit\x01",
            "through a long and terrible story.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#3608FThis is merely a gut feeling, but I suspect\x01",
            "that I need no introduction to the girl who\x01",
            "saved Colin yesterday.\x02\x03",
            "#3603FI believe our daughter was sent here from\x01",
            "the heavens to help him.\x02\x03",
            "#3600FHaha. Perhaps I am glorifying her too much.\x01",
            "I'm sorry, but I am still trying to wrap my head\x01",
            "around the situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C4E")

    Jump("loc_EC9")

    label("loc_C53")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#3600FEveryone...\x02\x03",
            "Thank you so much for your help\x01",
            "yesterday. I can't even begin to\x01",
            "imagine how I'll ever repay you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThere's nothing to repay us for, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FIt's reassuring to see that you've all\x01",
            "calmed down, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3603FRight. I had Sophia and Colin\x01",
            "rest for the remainder of the day.\x02\x03",
            "#3600FAlthough, I don't think Colin has\x01",
            "learned his lesson yet. Hahaha...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#3608FWe've already once faced a horrible situation\x01",
            "that taught us the suffering and pain over\x01",
            "the loss of a child...\x02\x03",
            "#3603FAll I wish for now is to live a peaceful\x01",
            "life with my family.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 7)

    label("loc_EC9")

    Jump("loc_177C")

    label("loc_ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1044")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F52")
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "#3600FAre you ready, Colin?\x02\x03",
            "Tell Mom if you get thirsty, okay?\x01",
            "She'll have a canteen with her.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_103F")

    label("loc_F52")


    ChrTalk(
        0x8,
        (
            "#3600FMy son has been shouting about\x01",
            "the parade all morning...\x02\x03",
            "It's rare for us to be able to spend time\x01",
            "together as a family, so I've planned\x01",
            "out a wonderful day for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FBeing a father must be difficult.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_103F")

    Jump("loc_177C")

    label("loc_1044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_11F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1116")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "#3603FSince the foot traffic gets so heavy,\x01",
            "I try not to drive too often during the\x01",
            "Anniversary Festival.\x02\x03",
            "#3600FHow are you feeling, Sophia? Tell\x01",
            "me if you get tired, dear.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_11F1")

    label("loc_1116")


    ChrTalk(
        0x8,
        (
            "#3600FColin suddenly insisted that we go\x01",
            "look at the attractions in the\x01",
            "Harbor District.\x02\x03",
            "Poor kid wore himself out yesterday\x01",
            "and ended up wanting to go home.\x01",
            "Haha... The little rascal never learns.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_11F1")

    Jump("loc_177C")

    label("loc_11F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_14F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1318")

    ChrTalk(
        0x8,
        (
            "#3600FI can't say I'm surprised that Crossbell's\x01",
            "70th anniversary has managed to attract\x01",
            "a record-breaking number of tourists.\x02\x03",
            "I figure Colin will get worn out easily,\x01",
            "so we'll stick to our neighborhood.\x02\x03",
            "I hope you continue to keep up\x01",
            "the good work, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EB")

    label("loc_1318")


    ChrTalk(
        0x8,
        (
            "#3605FHello, everyone. Are you working right now?\x02\x03",
            "#3600FI'm sure it must be difficult, but I hope you\x01",
            "continue to keep up the good work. Anyway,\x01",
            "we're on our way out to have some fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI hope you enjoy yourselves. Going together\x01",
            "as a family is the definitive experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FDon't mind us. Go out there\x01",
            "and enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600FThat we shall do, my friends.\x02\x03",
            "Colin is young, so I think we'll only\x01",
            "make a single trip around the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_14EB")

    Jump("loc_177C")

    label("loc_14F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_END)), "loc_1771")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15F4")

    ChrTalk(
        0x8,
        (
            "#3600FIf you all get tired out there, feel free to\x01",
            "make yourselves at home and take a\x01",
            "break here. Our door is always open to you.\x02\x03",
            "No need to be shy. My time as a trader has\x01",
            "taught me to always show hospitality to all\x01",
            "of my guests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176C")

    label("loc_15F4")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#3605FHello, everyone. I'm glad you're here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FOh... Sorry, Harold. Are we\x01",
            "interrupting you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600FOh, no. Not at all.\x02\x03",
            "But anyway, how are you all doing?\x01",
            "Are you feeling tired at all?\x02\x03",
            "Feel free to stay for a while and take\x01",
            "a nice break. I'm sure you've earned it.\x02\x03",
            "I understand it's not much, but it's the\x01",
            "least I could offer you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_176C")

    Jump("loc_177C")

    label("loc_1771")

    OP_4B(0x9, 0xFF)
    Call(0, 8)
    OP_4C(0x9, 0xFF)

    label("loc_177C")

    TalkEnd(0xFE)
    Return()

    # Function_6_7B1 end

    def Function_7_1780(): pass

    label("Function_7_1780")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1814")
    Jump("loc_185E")

    label("loc_1814")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1834")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_185E")

    label("loc_1834")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1854")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_185E")

    label("loc_1854")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_185E")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1B7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1990")

    ChrTalk(
        0xB,
        (
            "#3608FAfter all this time, you're the first people\x01",
            "I've talked to regarding my late daughter...\x02\x03",
            "I've taken some time to reflect, and I've\x01",
            "decided to take a break from work.\x02\x03",
            "My work may keep us afloat, but my family\x01",
            "is more precious to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7B")

    label("loc_1990")


    ChrTalk(
        0x101,
        (
            "#0000FSorry, Mr. Hayworth. Did we\x01",
            "interrupt your meal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3600FOh, not at all. I'm just taking a short\x01",
            "vacation from my work.\x02\x03",
            "I thought I'd take a few weeks off and\x01",
            "sort through my feelings.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AA3")

    ChrTalk(
        0x102,
        "#0102FI'm sure you must have a lot on your mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFB")

    label("loc_1AA3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AD1")

    ChrTalk(
        0x103,
        "#0202FI understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFB")

    label("loc_1AD1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AFB")

    ChrTalk(
        0x104,
        "#0300FI get ya, man.\x02",
    )

    CloseMessageWindow()

    label("loc_1AFB")


    ChrTalk(
        0xB,
        (
            "#3600FThis last week with my family has been\x01",
            "an absolute dream.\x02\x03",
            "Colin and Sophia were just as happy\x01",
            "about it as I was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B7B")

    SetChrSubChip(0xB, 0x0)
    TalkEnd(0xB)
    Return()

    # Function_7_1780 end

    def Function_8_1B83(): pass

    label("Function_8_1B83")


    ChrTalk(
        0x8,
        (
            "#3600FSorry, the negotiations dragged on.\x02\x03",
            "How has Colin been, by the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3700FHe's begun to enjoy drawing\x01",
            "pictures again.\x02\x03",
            "In fact, he's been begging me for a new\x01",
            "notebook to draw in recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600FHahaha. Good to know.\x01",
            "He's quite the enthusiastic one, isn't he?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x6A, 4)
    Return()

    # Function_8_1B83 end

    def Function_9_1CAD(): pass

    label("Function_9_1CAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1D87")
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1D72")

    ChrTalk(
        0x9,
        (
            "#3701FBut...to see her gentle husband\x01",
            "resorting to such harsh words.\x02\x03",
            "I worry for their relationship...\x01",
            "What could have brought on\x01",
            "such a change in demeanor?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7A")

    label("loc_1D72")

    Call(0, 13)
    ClearChrFlags(0xE, 0x10)

    label("loc_1D7A")

    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_2FE0")

    label("loc_1D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_207E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1ED6")

    ChrTalk(
        0x9,
        (
            "#3700FWork has been productive as of late.\x02\x03",
            "It's not as if every industry is doing\x01",
            "well, but working with my husband\x01",
            "is joyous.\x02\x03",
            "#3708FHaving spilled my heart out to you\x01",
            "may have helped me move on a little.\x02\x03",
            "#3700FMy husband has gone to Armorica\x01",
            "for the day. Please send him my\x01",
            "regards if you run into him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2079")

    label("loc_1ED6")


    ChrTalk(
        0x9,
        (
            "#3700FIt's good to see you again, SSS.\x01",
            "It's been quite some time now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FLikewise, ma'am. Has your husband\x01",
            "gone back to work, Mrs. Hayworth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3700FHe has. Actually, I was a little puzzled\x01",
            "when he told me he needed a break.\x02\x03",
            "#3708FWell, I suppose we've gone through a lot.\x01",
            "I think he wanted to refresh his mindset\x01",
            "before he returned to work.\x02\x03",
            "#3700FAnd thanks to that, business has\x01",
            "been going well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2079")

    Jump("loc_2FE0")

    label("loc_207E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_233E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 0)), scpexpr(EXPR_END)), "loc_20FC")

    ChrTalk(
        0x9,
        (
            "#3700FI think I'll spend the day\x01",
            "playing with Colin.\x02\x03",
            "I'm truly glad... Oh, Goddess, I thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2339")

    label("loc_20FC")


    ChrTalk(
        0x9,
        (
            "#3700FYou've all come again...\x02\x03",
            "Thank you, truly. I don't think I'll\x01",
            "ever be able to repay you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FPlease, Mrs. Hayworth. We were only helping\x01",
            "out those in need. It's our duty as officers,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYou gotta admit, though, Lloyd. Pretty rare of us\x01",
            "to get a request that actually feels like genuine\x01",
            "police work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FDon't hesitate to contact the Special Support\x01",
            "Section again if you ever need it.\x01",
            "We'll always help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3700FUnderstood. I appreciate it.\x02\x03",
            "Thank you again so much, everyone.\x01",
            "I'll be sure to take you up on the offer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 0)

    label("loc_2339")

    Jump("loc_2FE0")

    label("loc_233E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_251E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23C7")

    ChrTalk(
        0x9,
        (
            "#3700FWhen do you think the parade will begin?\x01",
            "Oh, I'll have to hurry if I want to make it\x01",
            "before it begins.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_23C7")


    ChrTalk(
        0x9,
        (
            "#3700FI eventually caved and gave in to\x01",
            "Colin's demands.\x02\x03",
            "*sigh* His misbehavior is leading me to\x01",
            "believe that we've spoiled him too much...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#3708FAh...\x02\x03",
            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FIs something wrong, Mrs. Hayworth?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3708FOh, no...it's nothing.\x02\x03",
            "#3700FI'm going to have to enjoy the\x01",
            "parade as much as possible!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2519")

    Jump("loc_2FE0")

    label("loc_251E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_25D5")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x9,
        (
            "#3701FOh, Colin... I wonder where you heard\x01",
            "about tourist attractions.\x02\x03",
            "Something feels off... I'm a little worried.\x02\x03",
            "The crowd is larger than usual today.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_2FE0")

    label("loc_25D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_25EE")
    OP_4B(0xA, 0xFF)
    Call(0, 12)
    OP_4C(0xA, 0xFF)
    Jump("loc_2FE0")

    label("loc_25EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2741")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_268E")

    ChrTalk(
        0x9,
        (
            "#3700FI regularly pray at the cathedral this\x01",
            "day of the week.\x02\x03",
            "Oh, Colin... How long does it take to\x01",
            "put on a simple pair of socks?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_273C")

    label("loc_268E")

    SetChrPos(0xA, 9860, 4000, 23690, 45)

    ChrTalk(
        0x9,
        (
            "#3700FAre you ready yet, Colin?\x02\x03",
            "I'm going to leave you behind\x01",
            "if you don't hurry up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#100P#3805FNooo! Wait for me, Mama!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 34480, 0, 5610, 315)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_273C")

    Jump("loc_2FE0")

    label("loc_2741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2919")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2804")

    ChrTalk(
        0x9,
        (
            "#3700FMy husband's gone to St. Ursula\x01",
            "Medical College for the day.\x02\x03",
            "I can only assume he's doing them\x01",
            "another favor...for free. That's\x01",
            "very much in-character for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2914")

    label("loc_2804")


    ChrTalk(
        0x9,
        (
            "#3700FMy husband has been offering the people\x01",
            "of Mainz a ten-percent discount ever since\x01",
            "last month's incident.\x02\x03",
            "What a relief. Sales have been holding\x01",
            "steady there.\x01",
            "*sigh* What ever will I do with him?\x02\x03",
            "Though I do find that aspect of\x01",
            "him charming, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2914")

    Jump("loc_2FE0")

    label("loc_2919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A1A")
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A0E")

    ChrTalk(
        0x9,
        (
            "#3700FRight. Now, if you spread the\x01",
            "parsley like this...\x02\x03",
            "Perfect. Just keep doing that.\x01",
            "Any man would be lucky to have\x01",
            "you as a wife in the future, Cindy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "Yay! You really mean it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A11")

    label("loc_2A0E")

    Call(0, 11)

    label("loc_2A11")

    OP_4C(0xE, 0xFF)
    Jump("loc_2FE0")

    label("loc_2A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2BA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AFC")

    ChrTalk(
        0x9,
        (
            "#3700FI usually hold a cooking class on\x01",
            "this day once a week.\x02\x03",
            "Well, I call it a 'class,' but I'm\x01",
            "actually just having fun with\x01",
            "my neighbors.\x02\x03",
            "In any case, I must\x01",
            "continue with my preparations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BA1")

    label("loc_2AFC")


    ChrTalk(
        0x9,
        (
            "#3700FIt's nothing extravagant, but the people of\x01",
            "this neighborhood seem to really enjoy it.\x02\x03",
            "Now if you'll excuse me, I need to\x01",
            "continue with my preparations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA1")

    Jump("loc_2FE0")

    label("loc_2BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_END)), "loc_2C49")

    ChrTalk(
        0x9,
        (
            "#3700FYou're all acquaintances of my\x01",
            "husband, correct?\x02\x03",
            "I'm Harold's wife, Sophia Hayworth.\x01",
            "It's a pleasure to make your\x01",
            "acquaintance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C54")

    label("loc_2C49")

    OP_4B(0x8, 0xFF)
    Call(0, 8)
    OP_4C(0x8, 0xFF)

    label("loc_2C54")

    Jump("loc_2FE0")

    label("loc_2C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_2E56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D45")

    ChrTalk(
        0x9,
        (
            "#3700FI don't exactly have the mind of a trader,\x01",
            "and I doubt I'll ever delve deep enough\x01",
            "to excel at it...\x02\x03",
            "However, if it'll allow me to assist Harold\x01",
            "with his endeavors, I'll keep trying to learn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E51")

    label("loc_2D45")


    ChrTalk(
        0x9,
        "#3700FHmm... These coupons...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "#3700FI usually sort through the coupons\x01",
            "while my husband is out negotiating.\x02\x03",
            "I'm not exactly spectacular in this field,\x01",
            "to be honest...\x02\x03",
            "However, I'll continue to work hard at it\x01",
            "if it allows me to help Harold.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_2E51")

    Jump("loc_2E65")

    label("loc_2E56")

    Call(0, 10)
    OP_93(0x9, 0x0, 0x1F4)
    SetChrFlags(0x9, 0x10)

    label("loc_2E65")

    Jump("loc_2FE0")

    label("loc_2E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_2EEA")

    ChrTalk(
        0x9,
        (
            "#3700FThe food needs to be arranged\x01",
            "like so.\x02\x03",
            "Maybe he'll do me a favor by\x01",
            "coming home early today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF9")

    label("loc_2EEA")

    Call(0, 10)
    OP_93(0x9, 0x5A, 0x1F4)
    SetChrFlags(0x9, 0x10)

    label("loc_2EF9")

    Jump("loc_2FE0")

    label("loc_2EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_2FDD")

    ChrTalk(
        0x9,
        (
            "#3700FI apologize for the misunderstanding.\x02\x03",
            "My husband's a trader, so we constantly\x01",
            "have clients visiting our house.\x02\x03",
            "Please come by again if you ever\x01",
            "need our assistance. We'd love to\x01",
            "try and help you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE0")

    label("loc_2FDD")

    Call(0, 10)

    label("loc_2FE0")

    TalkEnd(0xFE)
    Return()

    # Function_9_1CAD end

    def Function_10_2FE4(): pass

    label("Function_10_2FE4")


    ChrTalk(
        0x9,
        (
            "#3700FOh, are you here to see my husband?\x02\x03",
            "I apologize, but Harold isn't home\x01",
            "at the moment.\x02\x03",
            "I'd be more than happy to relay a\x01",
            "message to him, if you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FO-Oh, uh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#3700FM-My apologies... You aren't my husband's\x01",
            "clients, are you?\x02\x03",
            "That makes a lot more sense, now.\x01",
            "I thought it was strange for a group of young\x01",
            "people to be negotiating with Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FYour husband is involved with commerce,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3700FYes. He's a trader, albeit a relatively\x01",
            "minor one.\x02\x03",
            "I apologize for the misunderstanding.\x02\x03",
            "Please come by again if you ever\x01",
            "need our assistance. We'd love to\x01",
            "try and help you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 5)
    Return()

    # Function_10_2FE4 end

    def Function_11_326D(): pass

    label("Function_11_326D")


    ChrTalk(
        0x9,
        (
            "#3700FI apologize, but I have something\x01",
            "to attend to tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Oh, tomorrow's a church day, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "So you attend Mass every week,\x01",
            "don't you, Sophia? That's pretty\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3708FI'm not sure I would call it 'amazing...'\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_326D end

    def Function_12_3361(): pass

    label("Function_12_3361")


    ChrTalk(
        0x9,
        (
            "#3700FSit still for Mom, Colin. I can't dress you\x01",
            "if you keep squirming around, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3800FHeheh... I scream for ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3700FI know you want some ice cream,\x01",
            "snookums. Shall we go and look\x01",
            "for a stall, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3800FYaaay! Let's go!\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_12_3361 end

    def Function_13_3462(): pass

    label("Function_13_3462")


    ChrTalk(
        0xE,
        (
            "You know, I happened to pass by\x01",
            "your husband yesterday, Creil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I feel like he's become a little strange\x01",
            "these days. Almost as if he's become\x01",
            "more disrespectful.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        "Hmm... I haven't really thought about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "But now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I suppose he might have started using\x01",
            "harsher language recently...maybe?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "U-Uh... So has he, or has he not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3700FCreil is always so relaxed.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_13_3462 end

    def Function_14_3650(): pass

    label("Function_14_3650")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36E4")
    Jump("loc_372E")

    label("loc_36E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3704")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_372E")

    label("loc_3704")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3724")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_372E")

    label("loc_3724")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_372E")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_37C0")

    ChrTalk(
        0xC,
        (
            "#3700FI'd love for you to come visit us again.\x01",
            "I'll be sure to prepare a feast next time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3911")

    label("loc_37C0")


    ChrTalk(
        0xC,
        (
            "#3700FWhat a surprise to see you here.\x02\x03",
            "Would you like to join us for a meal?\x01",
            "As you can see, I've made a lot of food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha. I appreciate it, but we're in the\x01",
            "middle of work right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FSee you again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3700FNot a problem. I'll see you all\x01",
            "again next time, then.\x01",
            "(Is that girl Lloyd's little sister...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3911")

    SetChrSubChip(0xC, 0x0)
    TalkEnd(0xC)
    Return()

    # Function_14_3650 end

    def Function_15_3919(): pass

    label("Function_15_3919")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39E4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3957")
    Call(0, 19)
    Jump("loc_39DF")

    label("loc_3957")


    ChrTalk(
        0xA,
        (
            "#3800FThat kitty likes to walk on the fence\x01",
            "outside sometimes.\x02\x03",
            "#3809FAnd when she sees me looking from\x01",
            "the window, she runs away!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39DF")

    Jump("loc_4514")

    label("loc_39E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3A6B")

    ChrTalk(
        0xA,
        (
            "#3800FMama said she's going to our\x01",
            "neighbor's house today.\x02\x03",
            "#3809FHehehe! I'm going to sleep in\x01",
            "Papa's bed tonight!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4514")

    label("loc_3A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3AC5")

    ChrTalk(
        0xA,
        (
            "#3800FMama said she had to go outside for a bit...\x02\x03",
            "Where did Mama go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4514")

    label("loc_3AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3BCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3B1B")

    ChrTalk(
        0xA,
        (
            "#3800FI'm pretending I'm Papa when he\x01",
            "eats a lot of food!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BCA")

    label("loc_3B1B")


    ChrTalk(
        0xA,
        (
            "#3800FHehehe! Look at this!\x01",
            "This is how he does it!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x59, 0x1F4)

    ChrTalk(
        0xA,
        (
            "#3800F'This looks absolutely delectable.\x01",
            "May I have another one, Sophia?'\x02\x03",
            "*chomp*, *munch* *munch*...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3BCA")

    Jump("loc_4514")

    label("loc_3BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3C42")

    ChrTalk(
        0xA,
        (
            "#3800FI'm helping Mama out today.\x02\x03",
            "Did you know I'm going to become a\x01",
            "trader like Papa someday?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4514")

    label("loc_3C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 1)), scpexpr(EXPR_END)), "loc_3CDE")

    ChrTalk(
        0xA,
        (
            "#3800FI get to hang out with my mama today.\x02\x03",
            "#3809FThanks for helping me out\x01",
            "yesterday!\x02\x03",
            "Say hi to that other girl for me, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EDE")

    label("loc_3CDE")


    ChrTalk(
        0xA,
        (
            "#3800FOh! You're those guys from yesterday!\x02\x03",
            "You know, Mama said we were going to\x01",
            "read a book together today...\x02\x03",
            "But I really wanted to play outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FHaha. Always the rascal, ain'tcha?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FTry not to make your mother worry so\x01",
            "much, okay, Colin?\x02\x03",
            "If that girl hadn't shown up at the right\x01",
            "time yesterday, you would have been\x01",
            "in some serious trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3805FYeah, I know...\x01",
            "I'll stick around with Mama today.\x02\x03",
            "#3809FThanks for helping me again!\x01",
            "Say hi to that other girl for me, too!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 1)

    label("loc_3EDE")

    Jump("loc_4514")

    label("loc_3EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3F7C")

    ChrTalk(
        0xA,
        (
            "#3800FI begged Mama and Papa to watch\x01",
            "the parade, and they said it was okay!\x02\x03",
            "#3809FYaaaaaaay! I'm sooo excited!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_4514")

    label("loc_3F7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4056")

    ChrTalk(
        0xA,
        (
            "#3800FI met a man who came from\x01",
            "reeeallly far away yesterday.\x02\x03",
            "He said he was going to have\x01",
            "fun at the harbor.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#3800FI dunno what he meant, but I wanna\x01",
            "have fun there, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4514")

    label("loc_4056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_406F")
    OP_4B(0x9, 0xFF)
    Call(0, 12)
    OP_4C(0x9, 0xFF)
    Jump("loc_4514")

    label("loc_406F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_40E0")

    ChrTalk(
        0xA,
        (
            "#3800FWatering the plants, watering the plants...\x02\x03",
            "I forgot to water the plants this morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4514")

    label("loc_40E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_41A4")

    ChrTalk(
        0xA,
        (
            "#3800FMaybe, if I'm a good boy...Papa will come\x01",
            "play with me during the festival.\x02\x03",
            "I'm going to be the best boy ever, and then\x01",
            "Mama and Papa will HAVE to play with me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_420F")

    label("loc_41A4")


    ChrTalk(
        0xA,
        (
            "#3800FPapa has to work today.\x02\x03",
            "Mmm...\x02\x03",
            "Do you think he'll play with me at\x01",
            "the festival next month?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_420F")

    Jump("loc_4514")

    label("loc_4214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_42A3")

    ChrTalk(
        0xA,
        (
            "#3800FToday is Mama's cooking class!\x02\x03",
            "#3809FIt's sooo much fun!\x02\x03",
            "I always help out Mama and everyone\x01",
            "else, if they need it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4514")

    label("loc_42A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_42E6")

    ChrTalk(
        0xA,
        (
            "#3800FOh, hi!\x02\x03",
            "I like to help out with cooking!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4514")

    label("loc_42E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_43BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4356")

    ChrTalk(
        0xA,
        (
            "#3800FI can feel it... Papa's home!\x02\x03",
            "That's because I heard Papa's\x01",
            "car pull up!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_43BA")

    label("loc_4356")


    ChrTalk(
        0xA,
        (
            "#3800FPapa should be coming upstairs\x01",
            "any second now...\x02\x03",
            "I think I'll jump up and surprise him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43BA")

    Jump("loc_4514")

    label("loc_43BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_443E")

    ChrTalk(
        0xA,
        (
            "#3800FPapa gave me a goodbye kiss\x01",
            "before he left for work today.\x02\x03",
            "Heheh... I'm glad I got up earlier today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4514")

    label("loc_443E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_44AF")

    ChrTalk(
        0xA,
        (
            "#3800FMy papa works hard as a trader.\x02\x03",
            "Probably why he always leaves\x01",
            "so early in the morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4514")

    label("loc_44AF")


    ChrTalk(
        0xA,
        (
            "#3800FLa la la, lalalaaa! ♪\x01",
            "I'm drawing lotsa stuff today!\x02\x03",
            "You guys wanna play with me,\x01",
            "too?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4514")

    TalkEnd(0xFE)
    Return()

    # Function_15_3919 end

    def Function_16_4518(): pass

    label("Function_16_4518")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45AC")
    Jump("loc_45F6")

    label("loc_45AC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45CC")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45F6")

    label("loc_45CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45EC")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45F6")

    label("loc_45EC")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45F6")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4697")

    ChrTalk(
        0xD,
        (
            "#3809FI'm going to miss your fluffy hair!\x02\x03",
            "#3800FCome and play with me again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FYeah, I'll try!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C58")

    label("loc_4697")

    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x153, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_472B")
    Jump("loc_4775")

    label("loc_472B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_474B")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4775")

    label("loc_474B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_476B")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4775")

    label("loc_476B")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4775")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    ChrTalk(
        0xD,
        (
            "#3805FHuh?\x02\x03",
            "Are you his little sister?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)

    ChrTalk(
        0x153,
        (
            "#1111FSister?\x02\x03",
            "#1110FHey, Lloyd. Am I your sister?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    ChrTalk(
        0x101,
        (
            "#0000FWell, I suppose from Colin's perspective,\x01",
            "it would seem that way.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49B5")

    ChrTalk(
        0x153,
        (
            "#1108FI don't really get it, but okay...\x02\x03",
            "#1111FThen, does that make Elie your big sister?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#0112FHuh? U-Um...\x01",
            "(I suppose Lloyd is the younger brother type...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#0006FThat's not quite how it works, KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F(I'll say...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C55")

    label("loc_49B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B16")

    ChrTalk(
        0x153,
        (
            "#1108FO-Okay...\x02\x03",
            "#1111FSo...does that mean Tio is also your little sister?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x103, 0x153, 500)

    ChrTalk(
        0x103,
        "#0203FHe wishes.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#0006FIt doesn't quite work that way. And, Tio?\x01",
            "Can you stop making things worse?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#0211FIt was merely in jest. Try to read the mood,\x01",
            "Mr. Detective.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C55")

    label("loc_4B16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C55")

    ChrTalk(
        0x153,
        (
            "#1108FO-Okay...\x02\x03",
            "#1111FHey, Randy! Does that mean you're Lloyd's\x01",
            "big brother?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#0309FI'm more like his wise elder.\x02\x03",
            "#0306FHe's young, he's reckless, and he needs someone\x01",
            "to keep him in check.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#0006FWhat are you, my grandpa?\x02",
    )

    CloseMessageWindow()

    label("loc_4C55")

    SetScenarioFlags(0x0, 2)

    label("loc_4C58")

    SetChrSubChip(0xD, 0x0)
    TalkEnd(0xD)
    Return()

    # Function_16_4518 end

    def Function_17_4C60(): pass

    label("Function_17_4C60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4D2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4D0E")
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "How do I put this? Creil is...a bit slow,\x01",
            "I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's not really a big deal, though.\x01",
            "She's an adorable lady.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D26")

    label("loc_4D0E")

    OP_4B(0x9, 0xFF)
    OP_4B(0xF, 0xFF)
    Call(0, 13)
    OP_4C(0x9, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xE, 0x10)

    label("loc_4D26")

    Jump("loc_4D99")

    label("loc_4D2B")

    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4D92")

    ChrTalk(
        0xE,
        "Oh, let me help with the dishes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Heheh... I love these sorts\x01",
            "of things. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D95")

    label("loc_4D92")

    Call(0, 11)

    label("loc_4D95")

    OP_4C(0x9, 0xFF)

    label("loc_4D99")

    TalkEnd(0xFE)
    Return()

    # Function_17_4C60 end

    def Function_18_4D9D(): pass

    label("Function_18_4D9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E35")
    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4E20")

    ChrTalk(
        0xF,
        (
            "Umm... Hmm... I guess he HAS\x01",
            "been acting a little strange lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Should I be worried?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E28")

    label("loc_4E20")

    Call(0, 13)
    ClearChrFlags(0xE, 0x10)

    label("loc_4E28")

    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_4F4E")

    label("loc_4E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4ECF")

    ChrTalk(
        0xF,
        (
            "We always throw ourselves a bit of a\x01",
            "tea party after cooking class ends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Everybody seems to be having\x01",
            "a lot of fun talking today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F4E")

    label("loc_4ECF")


    ChrTalk(
        0xF,
        (
            "The main dish of today's class\x01",
            "is going to be salmon stew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Isn't it wonderful to cook alongside\x01",
            "all your friends?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4F4E")

    TalkEnd(0xFE)
    Return()

    # Function_18_4D9D end

    def Function_19_4F52(): pass

    label("Function_19_4F52")

    EventBegin(0x0)
    Fade(800)
    OP_4B(0xA, 0xFF)
    OP_68(36520, 1500, 4730, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(270, 0)
    SetCameraDistance(30020, 0)
    SetChrPos(0x101, 36580, 0, 5220, 180)
    SetChrPos(0x102, 37720, 0, 5220, 180)
    SetChrPos(0x103, 36580, 0, 6620, 180)
    SetChrPos(0x104, 37720, 0, 6620, 180)
    SetChrPos(0xA, 37190, 0, 3550, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0000FHey, Colin. Do you have a second?\x02\x03",
            "Do you, or anybody you know,\x01",
            "own a cat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#3805FA kitty?\x01",
            "What kinda kitty is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FOh, hold on. It's this little girl right here.\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd retrieved the cat from his jacket\x01",
            "pocket and showed her to Colin.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Sound(823, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        "#12P#3805FOh! I know this kitty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0105FWhoa, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#3800FYeah! She likes to walk on our\x01",
            "fence sometimes.\x02\x03",
            "I haven't seen her much these days,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0303FLooks like our lil' pussycat is from\x01",
            "around these parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FIt also likely narrows down the owner to\x01",
            "somebody living in the Residential District.\x01",
            "Let us continue the search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FGot it. Thanks, Colin. You were a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12P#3809FI'm glad! I hope I see you again soon!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 37320, 0, 5200, 180)
    BeginChrThread(0xA, 0, 0, 1)
    OP_29(0x8, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_19_4F52 end

    SaveToFile()

Try(main)
