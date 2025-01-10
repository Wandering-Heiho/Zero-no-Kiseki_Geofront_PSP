from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1040.bin",                # FileName
        "c1040",                    # MapName
        "c1040",                    # Location
        0x0015,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 21, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1040",                  # 0
        "Marcy",                  # 1
        "Marcy",                  # 2
        "Sarina",                 # 3
        "Eugot",                  # 4
        "Clarice",                # 5
        "Azel",                   # 6
        "Estelle",                # 7
        "Estelle",                # 8
        "Joshua",                 # 9
        "Fran",                   # 10
    ))

    AddCharChip((
        "chr/ch21800.itc",                   # 00
        "chr/ch20500.itc",                   # 01
        "chr/ch34200.itc",                   # 02
        "chr/ch10400.itc",                   # 03
        "apl/ch50375.itc",                   # 04
        "chr/ch21802.itc",                   # 05
        "chr/ch00600.itc",                   # 06
        "chr/ch00602.itc",                   # 07
        "chr/ch00702.itc",                   # 08
        "chr/ch08500.itc",                   # 09
    ))

    DeclNpc(48880,   29,      -55000,  135,  261,  0x0, 0,   0,   0,   0,   2,   0,   6,   255,  0)
    DeclNpc(46400,   29,      -53479,  270,  389,  0x0, 0,   5,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(3789,    0,       55279,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-2410,   29,      52169,   225,  261,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(3660,    29,      -56599,  90,   261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1029,    29,      55659,   90,   405,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(53740,   0,       51459,   90,   405,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(52040,   150,     53650,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(49200,   150,     53560,   90,   469,  0x0, 0,   8,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-400,    29,      -53770,  135,  389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)

    DeclActor(51690,   0,       5670,    1200,    51690,   1500,    5670,    0x007C, 0,  22, 0x0000)
    DeclActor(-4890,   0,       -52820,  1200,    -4890,   1500,    -52820,  0x007C, 0,  23, 0x0000)

    ScpFunction((
        "Function_0_27C",          # 00, 0
        "Function_1_334",          # 01, 1
        "Function_2_35F",          # 02, 2
        "Function_3_38A",          # 03, 3
        "Function_4_3B5",          # 04, 4
        "Function_5_647",          # 05, 5
        "Function_6_6E8",          # 06, 6
        "Function_7_1BD7",         # 07, 7
        "Function_8_1E32",         # 08, 8
        "Function_9_30BD",         # 09, 9
        "Function_10_3935",        # 0A, 10
        "Function_11_579B",        # 0B, 11
        "Function_12_5865",        # 0C, 12
        "Function_13_5A7E",        # 0D, 13
        "Function_14_5B39",        # 0E, 14
        "Function_15_5BB2",        # 0F, 15
        "Function_16_5EE7",        # 10, 16
        "Function_17_6387",        # 11, 17
        "Function_18_6B11",        # 12, 18
        "Function_19_6C1C",        # 13, 19
        "Function_20_741E",        # 14, 20
        "Function_21_7BD2",        # 15, 21
        "Function_22_832B",        # 16, 22
        "Function_23_84F2",        # 17, 23
    ))


    def Function_0_27C(): pass

    label("Function_0_27C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2BC"),
        (1, "loc_2C8"),
        (2, "loc_2D4"),
        (3, "loc_2E0"),
        (4, "loc_2EC"),
        (5, "loc_2F8"),
        (6, "loc_304"),
        (SWITCH_DEFAULT, "loc_310"),
    )


    label("loc_2BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_304")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_310")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_31C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_333")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_333")

    Return()

    # Function_0_27C end

    def Function_1_334(): pass

    label("Function_1_334")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35E")
    OP_94(0xFE, 0xFFFFF204, 0xCD3C, 0xFFFFFA24, 0xC602, 0x3E8)
    Sleep(300)
    Jump("Function_1_334")

    label("loc_35E")

    Return()

    # Function_1_334 end

    def Function_2_35F(): pass

    label("Function_2_35F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_389")
    OP_94(0xFE, 0xBC16, 0xFFFF213A, 0xBDCE, 0xFFFF2FB8, 0x3E8)
    Sleep(300)
    Jump("Function_2_35F")

    label("loc_389")

    Return()

    # Function_2_35F end

    def Function_3_38A(): pass

    label("Function_3_38A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B4")
    OP_94(0xFE, 0xFFFFFC90, 0xFFFF2F04, 0xFFFFF6F0, 0xFFFF263A, 0x3E8)
    Sleep(300)
    Jump("Function_3_38A")

    label("loc_3B4")

    Return()

    # Function_3_38A end

    def Function_4_3B5(): pass

    label("Function_4_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3C3")
    Jump("loc_646")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3D1")
    Jump("loc_646")

    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_40D")
    SetChrPos(0xA, 2500, 30, 55660, 270)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_408")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_408")

    Jump("loc_646")

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_420")
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_46F")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_646")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_487")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_49F")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4B7")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_646")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C5")
    Jump("loc_646")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xB, 2590, 30, 55740, 135)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_520")
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_55B")
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_59B")
    SetChrPos(0xA, 3790, 0, 55280, 180)
    SetChrPos(0xB, 3990, 30, 54010, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_646")

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5B3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_646")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5DD")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -1120, 30, -53900, 225)
    BeginChrThread(0xB, 0, 0, 3)
    Jump("loc_646")

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5EB")
    Jump("loc_646")

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5F9")
    Jump("loc_646")

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_622")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61D")
    SetChrFlags(0x8, 0x80)

    label("loc_61D")

    Jump("loc_646")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_646")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_646")
    SetChrFlags(0x8, 0x80)

    label("loc_646")

    Return()

    # Function_4_3B5 end

    def Function_5_647(): pass

    label("Function_5_647")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_660")
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    Jump("loc_666")

    label("loc_660")

    OP_10(0x0, 0x1)
    OP_10(0xB, 0x0)

    label("loc_666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_682")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_699")

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_699")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_699")

    label("loc_699")

    OP_65(0x0, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BB")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_6BB")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D5")
    OP_66(0x1, 0x1)

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E7")
    OP_66(0x1, 0x1)

    label("loc_6E7")

    Return()

    # Function_5_647 end

    def Function_6_6E8(): pass

    label("Function_6_6E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7AE")

    ChrTalk(
        0xFE,
        (
            "The person living in the place across from me\x01",
            "moved out about half a month ago. Place is\x01",
            "probably still vacant, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They were always apathetic, from what I remember.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_86B")

    ChrTalk(
        0xFE,
        (
            "Now that I think about it... How'd the\x01",
            "diet's budget session go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Depending on how it went, I'm sure the budget\x01",
            "will have considerable influence on the stock market.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_86B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_92E")

    ChrTalk(
        0xFE,
        (
            "Hmm, I think the newest issue of the Crossbell Times\x01",
            "releases tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They'd temporarily suspended their publications,\x01",
            "so I've been on edge waiting for it to come back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_92E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A22")

    ChrTalk(
        0xFE,
        (
            "Sounds like there was some huge kerfuffle over\x01",
            "in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And speaking of the harbor, all you have to do is go north\x01",
            "up the road outside here to get there, right?\x01",
            "Th-That's a little too close for comfort...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B47")

    ChrTalk(
        0xFE,
        (
            "Ah, fantastic. The Anniversary Festival photos I mailed to\x01",
            "my family have finally reached them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My children gave me a big\x01",
            "'Thank you!' over the phone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sniff* I haven't talked to them in\x01",
            "such a long time...so you know,\x01",
            "I can't help but feel homesick.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BD5")

    label("loc_B47")


    ChrTalk(
        0xFE,
        (
            "No, I have to snap out of it!\x01",
            "Now's not the time to feel that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll just have to bear the fact that I'm working\x01",
            "away from home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD5")

    Jump("loc_1BD3")

    label("loc_BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_BE8")
    Jump("loc_1BD3")

    label("loc_BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8B")

    ChrTalk(
        0xFE,
        "Oh, oops. My orbal camera is dead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to take pictures of the fireworks, so\x01",
            "hopefully, I can recharge it by this evening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D16")

    label("loc_C8B")


    ChrTalk(
        0xFE,
        (
            "It's unfortunate that it'll take a while for my\x01",
            "camera to be repaired, but at least using the\x01",
            "orbal stores around here is convenient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D16")

    Jump("loc_1BD3")

    label("loc_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_DB4")

    ChrTalk(
        0xFE,
        "That parade was absolutely sublime...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was my first time handling an orbal camera,\x01",
            "but I'm sure I took some great photographs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_E91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E48")

    ChrTalk(
        0xFE,
        (
            "I promised my family I'd take pictures of\x01",
            "the parade to send to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I-I need to hurry up and finish my work!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E8C")

    label("loc_E48")


    ChrTalk(
        0xFE,
        (
            "If I don't pick up the pace, the parade\x01",
            "will start without me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8C")

    Jump("loc_1BD3")

    label("loc_E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_F23")

    ChrTalk(
        0xFE,
        "Oh, no. An urgent task came in from the main office.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha. It doesn't look like I'll be\x01",
            "going outside today, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_FB4")

    ChrTalk(
        0xFE,
        "All right, I've got my wallet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, I'd like to tour the festival with my\x01",
            "family currently living in the Empire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_105B")

    ChrTalk(
        0xFE,
        (
            "Hmm. Hopefully, I can take some time off\x01",
            "next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, I'd love to tour the highly-anticipated\x01",
            "Anniversary Festival with my family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_105B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1248")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1194")

    ChrTalk(
        0xFE,
        (
            "The IBC is home to the largest brokerage firm\x01",
            "in all of Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're our business competitors, but\x01",
            "in all honesty, we actually have our moments\x01",
            "where we must rely on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My company entrusted a portion of their\x01",
            "stocks to them in order to keep a steady\x01",
            "market price.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1243")

    label("loc_1194")


    ChrTalk(
        0xFE,
        (
            "The IBC's brokerage firm is my\x01",
            "company's largest competitor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, there have been times where we\x01",
            "have relied on them, too. Life isn't only about\x01",
            "picking fights.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1243")

    Jump("loc_1BD3")

    label("loc_1248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1417")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1356")

    ChrTalk(
        0xFE,
        (
            "Stock prices have been mediocre at best,\x01",
            "thanks to the recent chain of accidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The warehouse company where the incident took\x01",
            "place has taken a huge price hit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The companies caught up in this mess are\x01",
            "rather worse for wear.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1412")

    label("loc_1356")


    ChrTalk(
        0xFE,
        (
            "Stock prices have been mediocre at best,\x01",
            "thanks to the recent chain of accidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure it'll rebound soon, but there are many\x01",
            "unlucky companies taking a hit in their prices.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1412")

    Jump("loc_1BD3")

    label("loc_1417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1502")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D6")

    ChrTalk(
        0xFE,
        (
            "I'd like to take a vacation to go visit my family\x01",
            "back home in Erebonia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I work for a brokerage firm, so I don't\x01",
            "have much time for vacations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14FD")

    label("loc_14D6")


    ChrTalk(
        0xFE,
        "Work transfers truly are painful.\x02",
    )

    CloseMessageWindow()

    label("loc_14FD")

    Jump("loc_1BD3")

    label("loc_1502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_15C1")

    ChrTalk(
        0xFE,
        (
            "The price of septium mined in Mainz\x01",
            "has begun to slightly decline...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... This stock will likely affect my\x01",
            "company's market price. I'd better\x01",
            "investigate the cause.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_15C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1660")

    ChrTalk(
        0xFE,
        (
            "How am I supposed to take an afternoon nap with\x01",
            "all of this noise? This has become unbearable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This apartment's walls sure are thin.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_1660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1847")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1790")

    ChrTalk(
        0xFE,
        (
            "A young couple moved in\x01",
            "next door recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I went to greet them, I was met\x01",
            "by an energetic girl with twintails and\x01",
            "a quiet, black-haired young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I seem to recall them claiming that\x01",
            "they're bracers. I would imagine\x01",
            "they're a reliable pair of youngsters.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1842")

    label("loc_1790")


    ChrTalk(
        0xFE,
        (
            "A young couple moved\x01",
            "next door recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're an energetic girl with twintails, and\x01",
            "a quiet, black-haired young man. They're\x01",
            "apparently members of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1842")

    Jump("loc_1BD3")

    label("loc_1847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196E")

    ChrTalk(
        0xFE,
        (
            "My job involves investigating speculation and\x01",
            "the direction of Crossbell's stock prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "See, information on neighboring countries\x01",
            "flows through Crossbell's economy and market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Information is absolutely crucial in order for\x01",
            "a brokerage firm to survive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A16")

    label("loc_196E")


    ChrTalk(
        0xFE,
        (
            "Hmm, I wonder if the Republic's still\x01",
            "dealing with terrible weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to wrap up this summary of the recent\x01",
            "stock market movements and report it to HQ.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A16")

    Jump("loc_1BD3")

    label("loc_1A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B31")

    ChrTalk(
        0xFE,
        (
            "I work for a brokerage firm based\x01",
            "in the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was offered a job transfer to THE Crossbell,\x01",
            "the mother of the international stock market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Living in Crossbell has been about as convenient\x01",
            "as I was anticipating it would be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BD3")

    label("loc_1B31")


    ChrTalk(
        0xFE,
        (
            "Here's the thing, though. Everything's all\x01",
            "Eastern-style around here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And considering I'm Erebonian, it's definitely\x01",
            "taken some time getting used to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD3")

    TalkEnd(0xFE)
    Return()

    # Function_6_6E8 end

    def Function_7_1BD7(): pass

    label("Function_7_1BD7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C6B")
    Jump("loc_1CB5")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C8B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CB5")

    label("loc_1C8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CAB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CB5")

    label("loc_1CAB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CB5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1E2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D96")

    ChrTalk(
        0xFE,
        (
            "I sent the photos I took during the\x01",
            "Anniversary Festival to my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trust me, those photos are absolutely worth\x01",
            "seeing. My daughter will love them!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E2A")

    label("loc_1D96")


    ChrTalk(
        0xFE,
        (
            "Oh, I messed up. I completely forgot to\x01",
            "send them a letter along with the photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, well. Too late now. I just hope they're doing well.\x02",
    )

    CloseMessageWindow()

    label("loc_1E2A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_1BD7 end

    def Function_8_1E32(): pass

    label("Function_8_1E32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_200F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F6D")

    ChrTalk(
        0xFE,
        (
            "I'm going to be honest with you. I've totally\x01",
            "changed my opinion on the Testaments,\x01",
            "compared to when I first met them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was even thinking about bringing Eugot\x01",
            "to Azel's workplace so that we could\x01",
            "enjoy a meal together for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Keep it a secret from him, though, okay?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_200A")

    label("loc_1F6D")


    ChrTalk(
        0xFE,
        (
            "I was thinking about bringing Eugot\x01",
            "to Azel's workplace so that we could\x01",
            "enjoy a meal together some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Keep it a secret from him, though, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_200A")

    Jump("loc_30B9")

    label("loc_200F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_20D2")

    ChrTalk(
        0xFE,
        (
            "I feel like our family's become a bit more\x01",
            "cheerful ever since Azel began working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Life's still a bit difficult, but as long as we maintain\x01",
            "the status quo, we'll be okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B9")

    label("loc_20D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2269")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D1")
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xFE,
        "Yep. Everything is fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aw, you hurried back home for me?\x01",
            "You have your occasional cute moments, Azel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Is that really necessary? I was seriously worried\x01",
            "about you, so I don't appreciate the mockery.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2264")

    label("loc_21D1")


    ChrTalk(
        0xFE,
        (
            "Azel was worried about that incident that happened\x01",
            "last night, so he came to check on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm so happy, it could bring a tear to my eye.\x02",
    )

    CloseMessageWindow()

    label("loc_2264")

    Jump("loc_30B9")

    label("loc_2269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2301")

    ChrTalk(
        0xFE,
        (
            "Eugot's got Sunday School over at the\x01",
            "cathedral today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get worried when I leave him home alone,\x01",
            "so I warmly welcome the help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B9")

    label("loc_2301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_235A")

    ChrTalk(
        0xFE,
        "I'm off to work, Eugot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Be a good boy and watch the house, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_30B9")

    label("loc_235A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2439")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D9")

    ChrTalk(
        0xFE,
        (
            "Those two gangs caused a big ruckus\x01",
            "downtown yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Geez, when will those kids learn?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2434")

    label("loc_23D9")


    ChrTalk(
        0xFE,
        (
            "Ugh, I'm going to give Azel the sternest\x01",
            "talking-to he's ever had when he comes home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2434")

    Jump("loc_30B9")

    label("loc_2439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2531")

    ChrTalk(
        0xFE,
        (
            "Azel told me that he wanted to spend half of the\x01",
            "Anniversary Festival hanging out with his fellow\x01",
            "delinquent friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think they called themselves the 'Testaments'?\x01",
            "Who knows? Maybe they're not as bad as I think\x01",
            "they are.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B9")

    label("loc_2531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_266E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2621")

    ChrTalk(
        0xFE,
        (
            "I went and told Azel that he has no choice but\x01",
            "to come home during next month's festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been awaiting the Anniversary Festival for\x01",
            "a long time, so I'd like to spend it with my family.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2669")

    label("loc_2621")


    ChrTalk(
        0xFE,
        (
            "Let's both look forward to some\x01",
            "fun times next month. Okay, Eugot?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2669")

    Jump("loc_30B9")

    label("loc_266E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2704")

    ChrTalk(
        0xFE,
        (
            "Right, we can't exactly afford anything\x01",
            "TOO expensive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, it's been a while since the two of us could\x01",
            "sit back and relax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B9")

    label("loc_2704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_277B")

    ChrTalk(
        0xFE,
        "Anyway, Eugot. I'm off to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I took some time off, so I have to return\x01",
            "to work with a bang!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B9")

    label("loc_277B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_296A")

    ChrTalk(
        0xFE,
        (
            "My brother Azel recently joined a gang\x01",
            "of delinquents... Last I heard, he started a\x01",
            "part-time job in the Downtown District, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I tried to get him to quit, but he promised me\x01",
            "that he'd do honest work and return home\x01",
            "sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Azel's apparently working at a bar his\x01",
            "friend owns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He promised that he would take responsibility and\x01",
            "reimburse me for the hospital bills he racked up...\x01",
            "I suppose I'll just wait and see if he keeps his word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A41")

    label("loc_296A")


    ChrTalk(
        0xFE,
        (
            "Granted, I'm still wary about Azel\x01",
            "being a member of that gang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm relieved that he said he'd finally\x01",
            "come home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I usually know how to keep my cool. I guess\x01",
            "raising my voice at him worked this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A41")

    Jump("loc_30B9")

    label("loc_2A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB0")

    ChrTalk(
        0xFE,
        (
            "My little brother's been living downtown for a while,\x01",
            "so I've decided to take some time off from work\x01",
            "in order to bring him back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though it's entirely a familial matter,\x01",
            "my boss told me it's being treated as a\x01",
            "paid vacation... He's a kind man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll try paying the Downtown District\x01",
            "a little visit tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C24")

    label("loc_2BB0")


    ChrTalk(
        0xFE,
        (
            "I...think I'll pay the Downtown District a little\x01",
            "visit tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must bring Azel back, no matter what.\x02",
    )

    CloseMessageWindow()

    label("loc_2C24")

    Jump("loc_30B9")

    label("loc_2C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2DDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D17")

    ChrTalk(
        0xFE,
        (
            "My fool of a brother refuses to return\x01",
            "from the Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I contacted the hospital, they said\x01",
            "it's already about time for his release...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is my chance! I need to go and\x01",
            "get him!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DD8")

    label("loc_2D17")


    ChrTalk(
        0xFE,
        (
            "I've been supporting our family, so I was a little\x01",
            "hesitant to take time off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, as Azel's guardian, it's my duty\x01",
            "to make sure he returns home using\x01",
            "whatever means necessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DD8")

    Jump("loc_30B9")

    label("loc_2DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2F77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB7")

    ChrTalk(
        0xFE,
        (
            "I received a notice from St. Ursula\x01",
            "that Azel had been hospitalized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The injury isn't life-threatening, but\x01",
            "it still seemed pretty serious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What the heck did that idiot do?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F72")

    label("loc_2EB7")


    ChrTalk(
        0xFE,
        (
            "I can't believe he went and got injured\x01",
            "while I wasn't there to watch him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Azel is so stupid... He must take great\x01",
            "pleasure in doing everything in his\x01",
            "power to make me worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F72")

    Jump("loc_30B9")

    label("loc_2F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_30B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3020")

    ChrTalk(
        0xFE,
        (
            "My other brother, Azel, hasn't come\x01",
            "home for a whole week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm almost positive that he's been\x01",
            "staying with all those delinquents...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30B9")

    label("loc_3020")


    ChrTalk(
        0xFE,
        (
            "My brother, Azel, hasn't come\x01",
            "home for a whole week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you happen to stumble across him, could you\x01",
            "tell him that I miss him and to come home?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B9")

    TalkEnd(0xFE)
    Return()

    # Function_8_1E32 end

    def Function_9_30BD(): pass

    label("Function_9_30BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_31A5")

    ChrTalk(
        0xFE,
        (
            "I plan to start working right after I graduate\x01",
            "from Sunday School, just like Sarina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd really like to become a bracer, 'cause\x01",
            "then I'd be able to treat my brother and\x01",
            "sister to all kinds of tasty meals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_31A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_325D")

    ChrTalk(
        0xFE,
        "My sister looks a lot happier these days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before Azzy said he'd come home, she always\x01",
            "seemed a little heartbroken. I can't lie, I'm\x01",
            "pretty happy about it, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_325D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3295")

    ChrTalk(
        0xFE,
        "I wonder how Azzy's doing at work...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_3295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_32A3")
    Jump("loc_3931")

    label("loc_32A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_332E")

    ChrTalk(
        0xFE,
        (
            "Oh, all right. I'll be fine. I'll go over to\x01",
            "Miss Clarice's place for the day again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Have a good day at work, Sis!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_332E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33F0")

    ChrTalk(
        0xFE,
        (
            "Apparently, something super crazy happened in\x01",
            "the Downtown District where my brother and his\x01",
            "friends were hanging out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That sounds so cool. I wish I coulda seen it, too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_33F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_34D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348F")

    ChrTalk(
        0xFE,
        (
            "Darn... If only I could hang out with Azzy\x01",
            "all the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess it's okay, though.\x01",
            "C'mon, Sis! Let's go play together!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_34CD")

    label("loc_348F")


    ChrTalk(
        0xFE,
        (
            "I'll never be lonely as long as I've got\x01",
            "Sis by my side!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CD")

    Jump("loc_3931")

    label("loc_34D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3512")

    ChrTalk(
        0xFE,
        (
            "Heheh. Azel came and played\x01",
            "bracers with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_3512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3596")

    ChrTalk(
        0xFE,
        "So, next month is the Anniversary Festival...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sure has been a while since I got to\x01",
            "play with my brother.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_3596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_35D9")

    ChrTalk(
        0xFE,
        (
            "I'll wait for you over at\x01",
            "Miss Clarice's place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_35D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3653")

    ChrTalk(
        0xFE,
        "Sis looks really happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Azzy started working, and Sis said that'll\x01",
            "make life a lot easier for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_3653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_36C8")

    ChrTalk(
        0xFE,
        (
            "Sis went to go meet with Azzy over\x01",
            "in the Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I-I wonder if she'll be fine...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_36C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3750")

    ChrTalk(
        0xFE,
        (
            "Azzy hasn't come back home for\x01",
            "a while now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's he even doing? Geez.\x01",
            "Sis has been super worried about him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_3750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_37CF")

    ChrTalk(
        0xFE,
        (
            "Hey, hey! C'mon, let's pretend\x01",
            "to be bracers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hah! Take this, and that! Yaaah!\x01",
            "Bracers are INVINCIBLE!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_37CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3810")

    ChrTalk(
        0xFE,
        "Will Azzy be okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He isn't hurt, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3931")

    label("loc_3810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3931")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B7")

    ChrTalk(
        0xFE,
        (
            "Bracers are the awesomest thing in\x01",
            "all of Crossbell, and that's a fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't wanna brag, but I got to\x01",
            "meet THE Arios MacLaine!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3931")

    label("loc_38B7")


    ChrTalk(
        0xFE,
        (
            "I don't wanna brag, but I got to\x01",
            "meet THE Arios MacLaine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't that super amazing?!\x01",
            "He was like, the coolest!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3931")

    TalkEnd(0xFE)
    Return()

    # Function_9_30BD end

    def Function_10_3935(): pass

    label("Function_10_3935")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_39D3")

    ChrTalk(
        0xFE,
        "Oh, dear. It's gotten late, hasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fran seemed fairly busy when I went to\x01",
            "visit her earlier. I hope she made time\x01",
            "for lunch...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5794")

    label("loc_39D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3AAC")

    ChrTalk(
        0xFE,
        (
            "Fran forgot her lunch today, so I went to\x01",
            "drop it off at the police station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, she seemed fairly busy, so I decided\x01",
            "to not bother her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What could have happened to make her so busy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5794")

    label("loc_3AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3CCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C11")

    ChrTalk(
        0xFE,
        (
            "I heard something horrible happened in the\x01",
            "Harbor District recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fran isn't a detective, so she shouldn't have to\x01",
            "investigate crime scenes, but nonetheless,\x01",
            "I still worry for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The CPD has been getting involved in many\x01",
            "dangerous incidents lately, so I've just become\x01",
            "more and more worried for my daughter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CC6")

    label("loc_3C11")


    ChrTalk(
        0xFE,
        (
            "I know it's only natural for you officers to\x01",
            "get involved in the front lines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't concern yourself too much with other\x01",
            "people's worries. I know you all have jobs\x01",
            "to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CC6")

    Jump("loc_5794")

    label("loc_3CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4070")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA6")
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        "Oh, if it isn't Noel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0505FHi, Mom.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FWhat's goin' on here? Why's this\x01",
            "feel hella awkward?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FI wouldn't say that... It's just, we see\x01",
            "each other pretty often, so there's no\x01",
            "need for a teary-eyed reunion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYou all seem like a tight-knit family.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0102FI'm sure that must make you happy, Mrs. Seeker.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        "Perhaps a little bit.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    ChrTalk(
        0xFE,
        (
            "Noel, please keep in contact more\x01",
            "regularly, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fran and I are constantly worried about you.\x01",
            "You know how much we love you, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0506FM-Mom... Please don't say embarrassing\x01",
            "things like that in front of the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FSuspicions confirmed. Noel is the type to\x01",
            "be spoiled by her family.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_406B")

    label("loc_3FA6")


    ChrTalk(
        0xFE,
        (
            "Attention, Noel Seeker! You had better start\x01",
            "contacting me more often, am I understood?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0506FYou don't have to keep repeating it, Mom.\x01",
            "I already understood you the first time. Sheesh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_406B")

    Jump("loc_5794")

    label("loc_4070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_42A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A9")

    ChrTalk(
        0xFE,
        (
            "We had a dinner party with Sarina's family\x01",
            "on the final day of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unfortunately, Fran was worried about\x01",
            "a distressed tourist, so she ended up\x01",
            "coming home later than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a second, I thought Fran had finally\x01",
            "bagged herself a nice boyfriend...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_429E")

    label("loc_41A9")


    ChrTalk(
        0xFE,
        (
            "But, it turns out that she was just helping a distressed\x01",
            "tourist on the last day of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both of my daughters are at the prime dating age,\x01",
            "so I really hope that at least one of them can\x01",
            "find themselves a good man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_429E")

    Jump("loc_5794")

    label("loc_42A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_436A")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, Sarina and the eldest\x01",
            "of her two brothers are coming home today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering it's a special occasion, I figured,\x01",
            "'Why not invite them to dinner with me?'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5794")

    label("loc_436A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_443A")

    ChrTalk(
        0xFE,
        (
            "I went for a bit of light shopping at Times while the\x01",
            "parade was happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was lucky enough to catch the tail end of the\x01",
            "wonderful festivities as I was walking out.\x01",
            "Perfect timing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5794")

    label("loc_443A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_455C")

    ChrTalk(
        0xFE,
        (
            "Hmm, today's the fourth day of the festival,\x01",
            "so the big parade is going to happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll swoop in and finish all the shopping I've been\x01",
            "meaning to do while everybody's distracted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet the department store will be deserted\x01",
            "while the parade's happening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5794")

    label("loc_455C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4661")

    ChrTalk(
        0xFE,
        (
            "Well, then, I think I'll venture forth into\x01",
            "this wild Anniversary Festival, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Noel and Fran went to explore the events occurring\x01",
            "in the Harbor District on the first day of the festival.\x01",
            "I was thinking I'd take a bit of a peek myself!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5794")

    label("loc_4661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4787")

    ChrTalk(
        0xFE,
        "Noel and Fran were able to come home yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Later that afternoon, they went to an\x01",
            "event over in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, it warms my heart to see my daughters'\x01",
            "sisterly bond. Unfortunately, I think that may deter\x01",
            "men from approaching them...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4892")

    label("loc_4787")


    ChrTalk(
        0xFE,
        (
            "Noel and Fran have been incredibly close\x01",
            "for as long as I can remember. Those two\x01",
            "were always being silly together as kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess their strong relationship makes it harder\x01",
            "for men to approach them... I bet my daughters\x01",
            "aren't having the easiest of times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4892")

    Jump("loc_5794")

    label("loc_4897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4AAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49BF")

    ChrTalk(
        0xFE,
        (
            "Now that I think about it, I'm pretty sure\x01",
            "that Noel said she'd be home for the first\x01",
            "day of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since then, all Fran can go on about anymore\x01",
            "is how it's, 'One month until the Anniversary\x01",
            "Festival!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, I'm glad they're so close.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AA5")

    label("loc_49BF")


    ChrTalk(
        0xFE,
        (
            "Noel was apparently able to take a vacation day\x01",
            "for the opening day of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure the Guardian Force has their fair share of\x01",
            "work still, so I hope asking for a day off wasn't\x01",
            "unreasonable of her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AA5")

    Jump("loc_5794")

    label("loc_4AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4C82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA8")

    ChrTalk(
        0xFE,
        (
            "I was a street vendor back in the day, so I'll\x01",
            "have you know that this area is my domain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I used to operate where Cronk's stall is. I let\x01",
            "him have the spot when I retired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm glad he's passionate about trading.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C7D")

    label("loc_4BA8")


    ChrTalk(
        0xFE,
        (
            "I used to operate where Cronk's stall is. I let\x01",
            "him have the spot when I retired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Retiring stallholders usually pass their spots\x01",
            "on to the next person on the waiting list.\x01",
            "Such is marketplace tradition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C7D")

    Jump("loc_5794")

    label("loc_4C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4D6B")

    ChrTalk(
        0xFE,
        (
            "I believe today's the day I look\x01",
            "after little Eugot, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a rare opportunity, so I think\x01",
            "I'll whip up a special feast!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be sure to let Fran have the leftovers\x01",
            "for dinner...if there are any.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5794")

    label("loc_4D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4F69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB6")

    ChrTalk(
        0xFE,
        (
            "I received a nice letter from my sweet, little\x01",
            "Noel over from Tangram Gate the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The contents of the letter were a little on\x01",
            "the vague side, but I'm just glad that she's\x01",
            "alive and well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That girl never remembers to send us\x01",
            "any letters, so Fran and I are always\x01",
            "worried about her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F64")

    label("loc_4EB6")


    ChrTalk(
        0xFE,
        (
            "My Noel doesn't do a good job of\x01",
            "contacting me often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, considering she's a sergeant major\x01",
            "of the CGF, I can't imagine she has much\x01",
            "time to write us letters...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F64")

    Jump("loc_5794")

    label("loc_4F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_50A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4F86")
    Call(0, 11)
    Jump("loc_50A0")

    label("loc_4F86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_5088")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4FA4")
    Call(0, 11)
    Jump("loc_5083")

    label("loc_4FA4")


    ChrTalk(
        0xC,
        (
            "I came up with the idea to read books to\x01",
            "the little boy I watch next door, so I went\x01",
            "and borrowed a book from the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's quite an interesting story! If you all get\x01",
            "the chance, you should give it a read.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5083")

    Jump("loc_50A0")

    label("loc_5088")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_509D")
    Call(0, 21)
    Jump("loc_50A0")

    label("loc_509D")

    Call(0, 11)

    label("loc_50A0")

    Jump("loc_5794")

    label("loc_50A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_51E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_50C2")
    Call(0, 12)
    Jump("loc_51DC")

    label("loc_50C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_51C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_50E0")
    Call(0, 12)
    Jump("loc_51BF")

    label("loc_50E0")


    ChrTalk(
        0xC,
        (
            "I came up with the idea to read books to\x01",
            "the little boy I watch next door, so I went\x01",
            "and borrowed a book from the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's quite an interesting story! If you all get\x01",
            "the chance, you should give it a read.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_51BF")

    Jump("loc_51DC")

    label("loc_51C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_51D9")
    Call(0, 21)
    Jump("loc_51DC")

    label("loc_51D9")

    Call(0, 12)

    label("loc_51DC")

    Jump("loc_5794")

    label("loc_51E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_531D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_51FE")
    Call(0, 13)
    Jump("loc_5318")

    label("loc_51FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_5300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_521C")
    Call(0, 13)
    Jump("loc_52FB")

    label("loc_521C")


    ChrTalk(
        0xC,
        (
            "I came up with the idea to read books to\x01",
            "the little boy I watch next door, so I went\x01",
            "and borrowed a book from the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's quite an interesting story! If you all get\x01",
            "the chance, you should give it a read.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_52FB")

    Jump("loc_5318")

    label("loc_5300")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_5315")
    Call(0, 21)
    Jump("loc_5318")

    label("loc_5315")

    Call(0, 13)

    label("loc_5318")

    Jump("loc_5794")

    label("loc_531D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_55E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5500")

    ChrTalk(
        0xFE,
        (
            "My daughter works as an operator\x01",
            "down at the police department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm unfortunately a bit ignorant when it comes\x01",
            "to these fancy, newfangled positions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how many times she tries to tell\x01",
            "me about her work, it flies over my head.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54F8")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005F(Huh, doesn't this sound like someone we know?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F(I get the impression that this is Fran's mother.)\x02",
    )

    CloseMessageWindow()

    label("loc_54F8")

    SetScenarioFlags(0x0, 3)
    Jump("loc_55E0")

    label("loc_5500")


    ChrTalk(
        0xFE,
        (
            "My daughter works as an operator\x01",
            "down at the police department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm a bit ignorant when it comes to these fancy,\x01",
            "newfangled positions. No matter how many times\x01",
            "she tries to explain her work, it flies over my head.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E0")

    Jump("loc_5794")

    label("loc_55E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5794")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_570C")

    ChrTalk(
        0xFE,
        "I'm blessed to have two lovely daughters.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My eldest is in the CGF, while my youngest\x01",
            "is with the CPD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having two well-behaved, loving\x01",
            "daughters is all a mother could ask for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Her daughter works for the CPD?\x01",
            "Is it somebody I've already met?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5794")

    label("loc_570C")


    ChrTalk(
        0xFE,
        (
            "My daughters are doing great work for\x01",
            "the CGF and CPD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A blessing like that is more than\x01",
            "a mother like me could ever ask for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5794")

    SetScenarioFlags(0x71, 6)
    TalkEnd(0xFE)
    Return()

    # Function_10_3935 end

    def Function_11_579B(): pass

    label("Function_11_579B")


    ChrTalk(
        0xFE,
        (
            "Sarina asked me if I could look after\x01",
            "Eugot for her for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know she went downtown to search for her\x01",
            "little brother, but still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The law doesn't mean much there, so I'm worried.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_11_579B end

    def Function_12_5865(): pass

    label("Function_12_5865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E1")

    ChrTalk(
        0xFE,
        (
            "My neighbor, Sarina, works hard\x01",
            "to provide for her family by herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though she's young, her commitment to her family\x01",
            "is admirable. I'm so proud of you, Sarina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My little Fran's grown up to be a fine policewoman.\x01",
            "Actually, I think it's about time for her to head home\x01",
            "from work, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That girl gets lonely a little too easily, to be honest.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5A7D")

    label("loc_59E1")


    ChrTalk(
        0xFE,
        (
            "She may not let it show, but she actually\x01",
            "gets lonely fairly easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should try to get her to become a little\x01",
            "more independent, like Sarina is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A7D")

    Return()

    # Function_12_5865 end

    def Function_13_5A7E(): pass

    label("Function_13_5A7E")


    ChrTalk(
        0xFE,
        "I wonder if Fran's hard at work right now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I know how she can be, but I promise you\x01",
            "that she's more reliable than you'd think.\x01",
            "Maybe I don't need to worry about her...\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_13_5A7E end

    def Function_14_5B39(): pass

    label("Function_14_5B39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5BAE")

    ChrTalk(
        0xFE,
        "Sis, are you all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You live so close to the Harbor District,\x01",
            "so I got a little worried...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BAE")

    TalkEnd(0xFE)
    Return()

    # Function_14_5B39 end

    def Function_15_5BB2(): pass

    label("Function_15_5BB2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_5EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D56")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle is staring intensely at the shelf filled\x01",
            "with sneakers.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        (
            "#0801FOookay... Just to be extra careful,\x01",
            "I'm gonna go ahead and change\x01",
            "into my lucky sneakers.\x02\x03",
            "#0803FDecisions, decisions... The anniversary edition\x01",
            "looks like it has good footing, but the limited\x01",
            "edition's soles are firmer.\x02\x03",
            "#0802FAaaaaaargh! I like both of them too much\x01",
            "to properly make a decision!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 5)
    Jump("loc_5EE3")

    label("loc_5D56")


    ChrTalk(
        0xE,
        (
            "#0809FIt's looking like we might have to take immediate\x01",
            "action on this whole mafia ordeal, so I'm doing a\x01",
            "once-over of my equipment to be extra careful.\x02\x03",
            "#0802FDon'tcha guys think it's totally important to have\x01",
            "a good pair of shoes on your feet?\x02\x03",
            "#0804FThis might come as a real shocker, but I\x01",
            "totally recommend trying out Stregas!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012F(So, is she a spokesperson for Strega, or what?)\x02",
    )

    CloseMessageWindow()

    label("loc_5EE3")

    TalkEnd(0xFE)
    Return()

    # Function_15_5BB2 end

    def Function_16_5EE7(): pass

    label("Function_16_5EE7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F7B")
    Jump("loc_5FC5")

    label("loc_5F7B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F9B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FC5")

    label("loc_5F9B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FBB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FC5")

    label("loc_5FBB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FC5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_637F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6285")

    ChrTalk(
        0x10,
        "#0900FOh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#0809FIt's good to see you all again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FHey, you two.\x01",
            "Huh, wait a second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FAre you two living here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#0804FWe sure are! We'll be hunkering down\x01",
            "here while we're in Crossbell.\x02\x03",
            "#0802FThough, we're not usually around during the day,\x01",
            "but you're still welcome to come around whenever\x01",
            "you feel like it! Deal? Deal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FS-Sounds good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I am a little curious as to what kind of relationship\x01",
            "the two of them are engaged in.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303F(They have the same last name, but they sure as\x01",
            "hell don't look like a pair of siblings to me.)\x02\x03",
            "#0305F(Oh, snap! Are they married?!)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 5)
    Jump("loc_637F")

    label("loc_6285")


    ChrTalk(
        0xF,
        (
            "#0802FIt's getting kinda late, but there should still\x01",
            "be time to knock out some requests.\x02\x03",
            "#0809FCrossbell's never short on work for us\x01",
            "to do, so it's pretty darn satisfying to\x01",
            "get so much done every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012F(Is she always this cheery?)\x02",
    )

    CloseMessageWindow()

    label("loc_637F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_5EE7 end

    def Function_17_6387(): pass

    label("Function_17_6387")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_641B")
    Jump("loc_6465")

    label("loc_641B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_643B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6465")

    label("loc_643B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_645B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6465")

    label("loc_645B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6465")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_67B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_672F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_65D0")

    ChrTalk(
        0x101,
        "#0005FOh, back from the guild already, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#0900FYeah. They've dismissed us for the time being.\x02\x03",
            "#0903FWe're under the impression that Heiyue won't\x01",
            "retaliate for a while.\x02\x03",
            "#0901FFor now, we've been put on standby within the city,\x01",
            "given the unpredictable nature of the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6727")

    label("loc_65D0")


    ChrTalk(
        0x10,
        (
            "#0900FThey left us on standby at the guild to be prepared for\x01",
            "an immediate response if the situation escalated,\x01",
            "but they've dismissed us for the time being.\x02\x03",
            "#0903FWe're under the impression that they won't\x01",
            "retaliate for a while.\x02\x03",
            "#0901FFor now, we've been put on standby within the city,\x01",
            "given the unpredictable nature of the situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6727")

    SetScenarioFlags(0x0, 6)
    Jump("loc_67B1")

    label("loc_672F")


    ChrTalk(
        0x10,
        (
            "#0903FThis is one heck of a dispute between the two mafias...\x02\x03",
            "#0901FI hope we'll be able to prevent disaster from striking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67B1")

    Jump("loc_6B09")

    label("loc_67B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D1")
    Call(0, 16)
    Jump("loc_6B09")

    label("loc_67D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69DD")

    ChrTalk(
        0x104,
        (
            "#0303F(Yo, ladykiller.)\x02\x03",
            "#0301F(Give it to me straight. What kinda relationship\x01",
            "do you and Estelle got goin' on anyway?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#0905F(W-Well... It's a bit of a long story.\x01",
            "I was actually adopted into her\x01",
            "family when I was 11.)\x02\x03",
            "#0910F(And, uh, after we both became\x01",
            "bracers...we sort of started dating.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F(Oh, man! They are a thing!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0204F(Case: solved.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(So they grew up together\x01",
            "and they're a couple now?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0109F(I suppose that explains how they're\x01",
            "always so in sync.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6B09")

    label("loc_69DD")


    ChrTalk(
        0x10,
        (
            "#0901FBy the way, I heard you guys had to\x01",
            "deal with the mafia's war hounds.\x01",
            "That must have been rough.\x02\x03",
            "#0902FI'm sure we'll all run into our fair share of troubles,\x01",
            "but let's keep doing our best, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FDefinitely. I have to admit, it's pretty\x01",
            "encouraging to hear that from you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B09")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_6387 end

    def Function_18_6B11(): pass

    label("Function_18_6B11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B26")
    Call(0, 19)
    Jump("loc_6C18")

    label("loc_6B26")


    ChrTalk(
        0x11,
        (
            "#11P#6405FHmm... Shouldn't Noey be coming home tonight?\x02\x03",
            "#6409FI can't believe it's almost been ten whole days\x01",
            "since we last had dinner as a family.\x02\x03",
            "And I finally got to meet KeA in the flesh today!\x01",
            "This has been the best day off ever!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C18")

    TalkEnd(0xFE)
    Return()

    # Function_18_6B11 end

    def Function_19_6C1C(): pass

    label("Function_19_6C1C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1050, 1500, -53430, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17330, 0)
    SetChrPos(0x101, -400, 30, -52100, 180)
    SetChrPos(0xEF, -1600, 30, -52500, 135)
    SetChrPos(0x153, -1500, 30, -53770, 90)
    SetChrSubChip(0x11, 0x0)
    OP_93(0x11, 0x87, 0x0)
    OP_0D()

    ChrTalk(
        0x153,
        "#6P#1105FOh, it's Fran!\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x11, 0x153, 500)

    ChrTalk(
        0x11,
        "#11P#6405FWha...?! KeA?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0002FOh, so this must be where\x01",
            "your family lives, huh, Fran?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D72")

    ChrTalk(
        0x102,
        "#6P#0102FAre you taking the day off?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E07")

    label("loc_6D72")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DBF")

    ChrTalk(
        0x103,
        "#6P#0202FShe appears to have taken a vacation day.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E07")

    label("loc_6DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E07")

    ChrTalk(
        0x104,
        "#6P#0300FDitchin' the ol' station for the day, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_6E07")

    TurnDirection(0x11, 0xEF, 500)

    ChrTalk(
        0x11,
        (
            "#11P#6406FYep! I finally get to use a vacation day,\x01",
            "now that the festival's finally over...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x153, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#11P#6409FBut I never would have guessed I'd be\x01",
            "visited by the lovely KeA today!\x02\x03",
            "#6400FWe've only spoken to each other through\x01",
            "the terminal, so this is our first meeting\x01",
            "in person, right? Welcome to my house!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#6P#1100FThanks!\x02\x03",
            "#1110FBut Fran, you're wearing totally different\x01",
            "clothes than when I see you on the terminal...\x02\x03",
            "#1109FI think you look really cute in pink.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#11P#6409FTh-Thank you, KeA.\x02\x03",
            "#6401FYou're waaay cuter than I am, though. I'm amazed\x01",
            "by how absolutely adorable you are when I'm not\x01",
            "looking at you through some hunk of metal.\x02\x03",
            "#6406FYou. Are. So. Cute. Cute! Cuuuuuuute!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)
    TurnDirection(0x11, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#11P#6401FL-Lloyd! I wanna walk through the\x01",
            "city with KeA, too!\x02\x03",
            "#6406FPlease, oh, pleeease\x01",
            "take me with you!\x02",
        )
    )

    CloseMessageWindow()
    Sound(892, 0, 100, 0)
    OP_63(0x11, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7210")

    ChrTalk(
        0x102,
        "#6P#0109FD-Deep breaths, Fran.\x02",
    )

    CloseMessageWindow()
    Jump("loc_72B3")

    label("loc_7210")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7270")

    ChrTalk(
        0x103,
        (
            "#6P#0203FAhem! Fran, you would be wise to\x01",
            "lower your dopamine levels.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B3")

    label("loc_7270")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72B3")

    ChrTalk(
        0x104,
        "#6P#0309FL-Let's take a chill pill, eh, Fran?\x02",
    )

    CloseMessageWindow()

    label("loc_72B3")


    ChrTalk(
        0x101,
        (
            "#5P#0012FI hate to break it to you, but we have\x01",
            "plans after this...\x02\x03",
            "#0002FI promise we'll find some time for\x01",
            "you and KeA to hang out, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#11P#6401FAw, darn. It's a promise, then, okay?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x153, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#11P#6409FI'll be sure to go on walks and play a lot\x01",
            "with you next time, KeA. Okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#6P#1109FThat sounds super fun!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -1150, 30, -53080, 135)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0xB6, 5)
    EventEnd(0x5)
    Return()

    # Function_19_6C1C end

    def Function_20_741E(): pass

    label("Function_20_741E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_68(51230, 1420, 3870, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 50930, 0, 3560, 0)
    SetChrPos(0x102, 52070, 0, 3560, 0)
    SetChrPos(0x103, 50930, 0, 2150, 0)
    SetChrPos(0x104, 52070, 0, 2150, 0)
    SetChrPos(0x8, 45830, -1840, 0, 0)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_95(0x101, 51620, 0, 4810, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)
    Sound(810, 0, 100, 0)
    Sleep(300)
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
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#0000FExcuse me! Is anybody home?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1400)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    ChrTalk(
        0x103,
        "#12P#0200FI fail to detect any presence inside, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0003FI guess this place is actually vacant, then.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man's Voice",
        "Oh, what are you all doing over there?\x02",
    )

    CloseMessageWindow()

    def lambda_7657():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7657)

    def lambda_7664():

        label("loc_7664")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_7664")

    QueueWorkItem2(0x102, 1, lambda_7664)

    def lambda_7676():

        label("loc_7676")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_7676")

    QueueWorkItem2(0x103, 1, lambda_7676)

    def lambda_7688():

        label("loc_7688")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_7688")

    QueueWorkItem2(0x104, 1, lambda_7688)
    OP_68(50380, 1420, 1610, 2000)
    OP_95(0x8, 49910, 0, 0, 2000, 0x0)
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(500)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        "#12PThat there's a vacant room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0305FHeh. Looks like we were right on the money.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PYeah, last tenant moved away\x01",
            "about half a month ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PIf you guys are looking for a place to stay,\x01",
            "I'd go take it up with the landlord, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_77CB():

        label("loc_77CB")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_77CB")

    QueueWorkItem2(0x101, 1, lambda_77CB)
    OP_95(0x8, 51410, 30, -1640, 2000, 0x0)
    OP_95(0x8, 51410, 0, -7420, 2000, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Sleep(300)
    Fade(500)
    OP_68(51230, 1420, 3870, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    Sleep(100)

    def lambda_784E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_784E)

    def lambda_785B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_785B)

    def lambda_7868():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7868)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0003FWell, I guess the vacancy on East Street\x01",
            "was referring to this apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FDid the previous tenant not file the proper\x01",
            "papers or somethin' when he split?\x01",
            "Man, how lazy can ya get?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FThat reminds me. The City Hall receptionist\x01",
            "had mentioned that their records may not\x01",
            "be completely accurate.\x02\x03",
            "#0206FI now understand what she meant by it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FOkay, so the vacancy on East Street is\x01",
            "Room 202 at Acacia Apartments...\x01",
            "(I should write down all the details...)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B31")

    ChrTalk(
        0x101,
        (
            "#0003FGreat. Now that we've confirmed the\x01",
            "locations of each vacancy, our work\x01",
            "here is done.\x02\x03",
            "#0000FLet's head back to City Hall and\x01",
            "report our findings.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x1E)
    Jump("loc_7B66")

    label("loc_7B31")


    ChrTalk(
        0x101,
        "#0000FAll right. Let's move on to the next one.\x02",
    )

    CloseMessageWindow()

    label("loc_7B66")

    Sleep(200)
    SetChrPos(0x0, 51710, 0, 4590, 180)
    SetChrPos(0x1, 51710, 0, 4590, 180)
    SetChrPos(0x2, 51710, 0, 4590, 180)
    SetChrPos(0x3, 51710, 0, 4590, 180)
    ClearChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 48880, 30, -55000, 135)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 7)
    EventEnd(0x5)
    Return()

    # Function_20_741E end

    def Function_21_7BD2(): pass

    label("Function_21_7BD2")

    EventBegin(0x0)
    Fade(500)
    OP_68(3230, 1530, -56000, 0)
    MoveCamera(62, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, 2610, 30, -55580, 135)
    SetChrPos(0x102, 4019, 0, -54690, 180)
    SetChrPos(0x103, 2360, 30, -54400, 135)
    SetChrPos(0x104, 3880, 0, -53400, 180)
    TurnDirection(0xC, 0x101, 0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 6)), scpexpr(EXPR_END)), "loc_7CA2")

    ChrTalk(
        0x101,
        (
            "#6P#0000FExcuse me, Miss Clarice.\x01",
            "Do you have a moment?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CD3")

    label("loc_7CA2")


    ChrTalk(
        0x101,
        "#6P#0000FExcuse me... Are you Miss Clarice?\x02",
    )

    CloseMessageWindow()

    label("loc_7CD3")


    ChrTalk(
        0xC,
        "#11POh, yes. How may I help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FWe're here because of a support request\x01",
            "we received from the city's library.\x02\x03",
            "#0000FAre you borrowing any books from the\x01",
            "library that you've yet to return?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#11POh! I am! I completely forgot about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POh, dear. I'm afraid this book is\x01",
            "long overdue by now, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FIt appears she had a lapse in her\x01",
            "memory and forgot to return it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI suppose I'm becoming more\x01",
            "forgetful with age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P*sigh* I'm sure Noel wouldn't let me\x01",
            "hear the end of this if she found out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PA-Anyway, please wait a moment\x01",
            "while I get it for you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_95(0xC, 2250, 0, -57250, 2000, 0x0)
    OP_95(0xC, -1980, 0, -57290, 2000, 0x0)
    OP_0D()
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 3660, 30, -56600, 315)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xC,
        "#11PThis should be the one.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2D6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D6, 1)
    TurnDirection(0x102, 0x101, 500)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#11P#0105FOh, this book...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0305FWhat's up, Mademois-Elie?\x01",
            "You read this before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FYes, actually.\x02\x03",
            "It's one of the most popular fairy tales\x01",
            "at the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhenever my neighbor, Sarina, goes to work,\x01",
            "she always asks if I can watch after her little\x01",
            "brother, Eugot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PSo, I thought that it might be a fun idea to read\x01",
            "books together, which led me to this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PI'm glad he seemed to enjoy the story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FOh, really?\x01",
            "(I kind of want to read it now, too...)\x02\x03",
            "#0000FWell, thank you very much for your\x01",
            "cooperation, Miss Clarice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11POh, not at all. The pleasure was mine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PBelieve me, I'll make sure to return\x01",
            "books on time from now on!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x5, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8317")
    OP_29(0x5, 0x1, 0x1F)

    label("loc_8317")

    SetChrPos(0x0, 2610, 30, -55580, 135)
    EventEnd(0x5)
    Return()

    # Function_21_7BD2 end

    def Function_22_832B(): pass

    label("Function_22_832B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8354")
    Call(0, 20)
    Jump("loc_84EE")

    label("loc_8354")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84C8")
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

    ChrTalk(
        0x102,
        "#0100FIs this room also vacant?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FIt's not on the list, so perhaps\x01",
            "the tenant is just out right now.\x01",
            "Though I can't say for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FAccording to City Hall's documents,\x01",
            "the East Street vacancy is located to\x01",
            "the right of the Bracer Guild.\x02\x03",
            "We should make our way there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_84EE")

    label("loc_84C8")

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

    label("loc_84EE")

    TalkEnd(0xFF)
    Return()

    # Function_22_832B end

    def Function_23_84F2(): pass

    label("Function_23_84F2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_885D")
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x101,
        "#0005FWhat's this stuffed animal?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x0, 500)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#6400FOh, that's Banban the Bear!\x01",
            "He's my partner in crime, my kindred spirit!\x02\x03",
            "#6409FIsn't he cute? I actually bought him as part of a\x01",
            "matching set with someone very important to me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x11, 500)
    Sleep(200)

    ChrTalk(
        0x153,
        (
            "#1109FWow, you're right! He's super-duper cute!\x02\x03",
            "#1110FHey, Fran. How old's Banban the Bear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6409FBanban's three years old! I'm so happy\x01",
            "that KeA also understands just how\x01",
            "cute Banban really is!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8759")

    ChrTalk(
        0x102,
        (
            "#0102F(I'm glad that these two seem to be\x01",
            "hitting it off...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87EC")

    label("loc_8759")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87AB")

    ChrTalk(
        0x103,
        (
            "#0202F(These two are quite compatible with\x01",
            "each other.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87EC")

    label("loc_87AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87EC")

    ChrTalk(
        0x104,
        "#0302F(They're like two peas in a pod, eh?)\x02",
    )

    CloseMessageWindow()

    label("loc_87EC")


    ChrTalk(
        0x101,
        (
            "#0004F(Yeah, it's hard to believe they've only\x01",
            "talked through the terminal until now...)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_93(0x11, 0x87, 0x1F4)
    SetScenarioFlags(0xD1, 0)
    Jump("loc_88B0")

    label("loc_885D")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran's favorite stuffed animal sits here.\x01",
            "Its name is Banban the Bear.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_88B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C6B")

    ChrTalk(
        0x109,
        "#0505FOh, what's this doing out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWhat's wrong, Noel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FOh, nothing. Just that this stuffed\x01",
            "animal belongs to Fran.\x02\x03",
            "#0503FI'm pretty sure she named it Banban or\x01",
            "something... Either way, she adores it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_END)), "loc_8A5B")

    ChrTalk(
        0x104,
        (
            "#0300FHey, ain't that the matching pair to\x01",
            "your bear, Noel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004FHow very much like Fran to name and love a\x01",
            "stuffed animal as if it were her own child.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B16")

    label("loc_8A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_END)), "loc_8B16")

    ChrTalk(
        0x101,
        (
            "#0000FHaha, that's right. Fran told us something\x01",
            "like that before, didn't she?\x02\x03",
            "#0004FHow very much like Fran to name and love a\x01",
            "stuffed animal as if it were her own child.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BD2")

    ChrTalk(
        0x109,
        (
            "#0503F(T-Truth be told, I also own a stuffed animal...)\x02\x03",
            "#0508F(Not that I'd ever admit it, though.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F...?\x01",
            "(I suspect that Noel is hiding\x01",
            "something from us.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C63")

    label("loc_8BD2")


    ChrTalk(
        0x109,
        (
            "#0500FIsn't that the truth?\x02\x03",
            "#0508F*sigh* If only I were as charming as her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(Noel appeared to be depressed for a\x01",
            "moment there.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C63")

    SetScenarioFlags(0xD1, 1)
    Jump("loc_8DB9")

    label("loc_8C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CCE")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran's favorite stuffed animal sits here.\x02\x03",
            "Its name is Banban the Bear.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8DB9")

    label("loc_8CCE")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran's favorite stuffed animal sits here.\x01",
            "It appears to be a matching pair with Noel's.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#0503F(Maybe I should name my bear, too...)\x02\x03",
            "#0506F(Nope! No way! I'm not nearly girly enough\x01",
            "to do something that embarrassing.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DB9")

    TalkEnd(0xFF)
    Return()

    # Function_23_84F2 end

    SaveToFile()

Try(main)
