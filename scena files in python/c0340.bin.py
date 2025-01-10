from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0340.bin",                # FileName
        "c0340",                    # MapName
        "c0340",                    # Location
        0x002D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0340",                  # 0
        "Izuri",                  # 1
        "Ferrick",                # 2
        "Cindy",                  # 3
        "Izuri",                  # 4
        "Anri",                   # 5
        "Yunks",                  # 6
    ))

    AddCharChip((
        "chr/ch21700.itc",                   # 00
        "chr/ch21702.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch22200.itc",                   # 04
        "chr/ch27600.itc",                   # 05
    ))

    DeclNpc(40669,   0,       9600,    360,  389,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(32659,   0,       5679,    180,  261,  0x0, 0,   2,   0,   0,   3,   0,   10,  255,  0)
    DeclNpc(4980,    0,       8989,    89,   261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(36700,   250,     2000,    270,  261,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(5329,    0,       3990,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(689,     0,       990,     225,  389,  0x0, 0,   5,   0,   0,   2,   0,   15,  255,  0)

    ScpFunction((
        "Function_0_194",          # 00, 0
        "Function_1_24C",          # 01, 1
        "Function_2_359",          # 02, 2
        "Function_3_384",          # 03, 3
        "Function_4_3AF",          # 04, 4
        "Function_5_3FC",          # 05, 5
        "Function_6_427",          # 06, 6
        "Function_7_7A7",          # 07, 7
        "Function_8_7FA",          # 08, 8
        "Function_9_107F",         # 09, 9
        "Function_10_2052",        # 0A, 10
        "Function_11_33CF",        # 0B, 11
        "Function_12_34C2",        # 0C, 12
        "Function_13_443D",        # 0D, 13
        "Function_14_457B",        # 0E, 14
        "Function_15_4A5E",        # 0F, 15
    ))


    def Function_0_194(): pass

    label("Function_0_194")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1D4"),
        (1, "loc_1E0"),
        (2, "loc_1EC"),
        (3, "loc_1F8"),
        (4, "loc_204"),
        (5, "loc_210"),
        (6, "loc_21C"),
        (SWITCH_DEFAULT, "loc_228"),
    )


    label("loc_1D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_204")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_210")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_21C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_228")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_234")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_24B")

    Return()

    # Function_0_194 end

    def Function_1_24C(): pass

    label("Function_1_24C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_358")

    def lambda_25C():
        OP_96(0x8, 0x9858, 0x0, 0x2008, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_25C)

    def lambda_276():
        OP_96(0x9, 0x9858, 0x0, 0x22F6, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_276)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    Sleep(200)

    def lambda_29B():
        OP_96(0x8, 0x9664, 0x0, 0x1E78, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_29B)

    def lambda_2B5():
        OP_96(0x9, 0x9664, 0x0, 0x2166, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2B5)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    Sleep(200)

    def lambda_2DA():
        OP_96(0x8, 0x9858, 0x0, 0x1DB0, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2DA)

    def lambda_2F4():
        OP_96(0x9, 0x9858, 0x0, 0x209E, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2F4)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    Sleep(200)

    def lambda_319():
        OP_96(0x8, 0x9A4C, 0x0, 0x1EDC, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_319)

    def lambda_333():
        OP_96(0x9, 0x9A4C, 0x0, 0x21CA, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_333)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    Sleep(200)
    Jump("Function_1_24C")

    label("loc_358")

    Return()

    # Function_1_24C end

    def Function_2_359(): pass

    label("Function_2_359")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_383")
    OP_94(0xFE, 0xFFFFF510, 0xFFFFFF56, 0x11D0, 0x94C, 0x3E8)
    Sleep(300)
    Jump("Function_2_359")

    label("loc_383")

    Return()

    # Function_2_359 end

    def Function_3_384(): pass

    label("Function_3_384")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AE")
    OP_94(0xFE, 0x7738, 0x1126, 0x852A, 0x1D38, 0x3E8)
    Sleep(300)
    Jump("Function_3_384")

    label("loc_3AE")

    Return()

    # Function_3_384 end

    def Function_4_3AF(): pass

    label("Function_4_3AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FB")
    OP_95(0xFE, 1790, 0, 500, 900, 0x0)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 1790, 0, 1500, 900, 0x0)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Jump("Function_4_3AF")

    label("loc_3FB")

    Return()

    # Function_4_3AF end

    def Function_5_3FC(): pass

    label("Function_5_3FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_426")
    OP_94(0xFE, 0xF32, 0x2C6, 0x139C, 0x2634, 0x3E8)
    Sleep(300)
    Jump("Function_5_3FC")

    label("loc_426")

    Return()

    # Function_5_3FC end

    def Function_6_427(): pass

    label("Function_6_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_45B")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 5020, 0, 7310, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_7A6")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4A0")
    SetChrPos(0x9, 1790, 0, 1100, 270)
    SetChrPos(0xA, -180, 0, 1100, 90)
    BeginChrThread(0x9, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B")
    SetChrFlags(0xA, 0x10)

    label("loc_49B")

    Jump("loc_7A6")

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4CA")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x9, 40670, 0, 9600, 360)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_7A6")

    label("loc_4CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4EE")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3670, 0, 9770, 0)
    Jump("loc_7A6")

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_506")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_7A6")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_523")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_7A6")

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_57D")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, 5310, 0, 4019, 90)
    SetChrPos(0xA, 1090, 0, 620, 315)
    SetChrPos(0xC, 280, 0, 1480, 135)
    Jump("loc_7A6")

    label("loc_57D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5D7")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 4980, 0, 8220, 135)
    SetChrPos(0xA, 5020, 0, 7310, 89)
    SetChrPos(0xC, 2970, 0, 4630, 270)
    SetChrFlags(0xA, 0x10)
    Jump("loc_7A6")

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_640")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 760, 0, 340, 0)
    SetChrPos(0xA, 1420, 0, 1650, 225)
    SetChrPos(0xC, -30, 0, 1380, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63B")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_63B")

    Jump("loc_7A6")

    label("loc_640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_68F")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x8, 600, 0, 960, 0)
    SetChrPos(0xA, -5660, -500, 3990, 90)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_7A6")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6B4")
    SetChrPos(0x9, 40670, 0, 9600, 360)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_7A6")

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6FE")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x8, 39000, 0, 8200, 360)
    SetChrPos(0x9, 39000, 0, 8950, 180)
    BeginChrThread(0x8, 1, 0, 1)
    Jump("loc_7A6")

    label("loc_6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_743")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x9, 3150, 0, 8500, 90)
    SetChrPos(0xA, 4850, 0, 8500, 270)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_7A6")

    label("loc_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_760")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_7A6")

    label("loc_760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_76E")
    Jump("loc_7A6")

    label("loc_76E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_793")
    SetChrPos(0xA, 4340, 0, 5610, 315)
    BeginChrThread(0xA, 0, 0, 5)
    Jump("loc_7A6")

    label("loc_793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7A1")
    Jump("loc_7A6")

    label("loc_7A1")

    SetChrFlags(0xA, 0x80)

    label("loc_7A6")

    Return()

    # Function_6_427 end

    def Function_7_7A7(): pass

    label("Function_7_7A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C0")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_7C6")

    label("loc_7C0")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_7C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7F9")

    label("loc_7E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7F9")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7F9")

    label("loc_7F9")

    Return()

    # Function_7_7A7 end

    def Function_8_7FA(): pass

    label("Function_8_7FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_847")

    ChrTalk(
        0x8,
        "It's awfully noisy down there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "What's going on?\x02",
    )

    CloseMessageWindow()
    Jump("loc_107B")

    label("loc_847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_921")

    ChrTalk(
        0x8,
        (
            "The Anniversary Festival's main attraction\x01",
            "has come to an end. I'm pleased my lovely\x01",
            "grandchildren were able to enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, only one more event remains.\x01",
            "I believe it's happening tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107B")

    label("loc_921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_986")

    ChrTalk(
        0x8,
        (
            "Now that I've finished doing the laundry,\x01",
            "I think I'll go out for a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11")

    label("loc_986")


    ChrTalk(
        0x8,
        (
            "We take care of the household chores as\x01",
            "a family this time every week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Dividing the tasks allows us to finish\x01",
            "in record time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A11")

    Jump("loc_107B")

    label("loc_A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B01")

    ChrTalk(
        0x8,
        (
            "My son works at the IBC, and his wife\x01",
            "works at one of their foreign branches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I understand they have busy lives, but\x01",
            "to not be able to attend the festival with\x01",
            "their children is a little sad, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCF")

    label("loc_B01")


    ChrTalk(
        0x8,
        (
            "It may be the Anniversary Festival, but both\x01",
            "my son and his wife are busy with work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* Well, it's not particularly\x01",
            "my problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure my grandchildren will be\x01",
            "disappointed, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_BCF")

    Jump("loc_107B")

    label("loc_BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CA1")

    ChrTalk(
        0x8,
        (
            "I think I'll take my grandchildren out on a\x01",
            "little walk around the neighborhood today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Anniversary Festival is a historical event,\x01",
            "so we should enjoy it in moderation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D30")

    label("loc_CA1")


    ChrTalk(
        0x8,
        (
            "There's no rush. The festival isn't going\x01",
            "anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Okay, the doors are properly locked up.\x01",
            "I haven't forgotten anything, have I?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D30")

    Jump("loc_107B")

    label("loc_D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_E71")
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DF0")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0x8,
        (
            "I may be an old granny these days, but I was\x01",
            "quite the fancy silver-haired lady in my day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I knew how to put on the moves, so to speak.\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_E68")

    label("loc_DF0")


    ChrTalk(
        0x8,
        "Okay, lower your hips...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lightly place your hands here, and allow\x01",
            "yourself to be mesmerized by the rhythm.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E68")

    OP_4C(0x9, 0xFF)
    Jump("loc_107B")

    label("loc_E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F0F")

    ChrTalk(
        0x8,
        (
            "I've made plans to meet up with an\x01",
            "old friend of mine today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I imagine it'll turn into a bragging competition\x01",
            "over our grandchildren.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107B")

    label("loc_F0F")


    ChrTalk(
        0x8,
        (
            "Ferrick is a bit frivolous, but\x01",
            "he's a kind child deep down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Cindy's definitely a bit of a cocky one,\x01",
            "but she's bright and does a great\x01",
            "job with the chores.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As for Anri...he's really had\x01",
            "such a lively smile recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Being surrounded by my grandchildren makes\x01",
            "this old gal as happy as can be.\x01",
            "They're the best gift my son has ever given me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_107B")

    TalkEnd(0xFE)
    Return()

    # Function_8_7FA end

    def Function_9_107F(): pass

    label("Function_9_107F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1113")
    Jump("loc_115D")

    label("loc_1113")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1133")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_115D")

    label("loc_1133")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1153")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_115D")

    label("loc_1153")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_115D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_12A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11C0")

    ChrTalk(
        0xB,
        "Hmm. What's the matter with Bond?\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A1")

    label("loc_11C0")


    ChrTalk(
        0xB,
        (
            "Our neighbor, Sophia, just came by to ask\x01",
            "if I had seen Bond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I recall correctly, he lives in our neighborhood\x01",
            "and works as a broker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I suppose I haven't seen him recently...\x01",
            "Is everything okay with him?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12A1")

    Jump("loc_204A")

    label("loc_12A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_146F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_134E")

    ChrTalk(
        0xB,
        (
            "Most Crossbellans don't expect much\x01",
            "from the diet anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That pitiful thing is so pointless that they\x01",
            "may as well stop holding them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_146A")

    label("loc_134E")


    ChrTalk(
        0xB,
        (
            "The Crossbell Diet has been repeating the\x01",
            "exact same pattern for the past 70 years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "One year the Imperial Faction rises into power,\x01",
            "the next year, the Republican Faction. Rinse\x01",
            "and repeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What a load of baloney. It's only natural\x01",
            "that we'd all lose interest in it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_146A")

    Jump("loc_204A")

    label("loc_146F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_15FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14FE")

    ChrTalk(
        0xB,
        (
            "Learning alongside your friends is more\x01",
            "vital than having good test results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "At least, that's what I believe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F7")

    label("loc_14FE")


    ChrTalk(
        0xB,
        (
            "It looks like Anri was able to get a perfect\x01",
            "score on his Sunday School test again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm glad, but he needs to learn that there's\x01",
            "more to life than studying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm sure he would learn even more\x01",
            "if he talked with his friends in class.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_15F7")

    Jump("loc_204A")

    label("loc_15FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1683")

    ChrTalk(
        0xB,
        (
            "My son may be a manager at the IBC,\x01",
            "but he still has a ways to go before he\x01",
            "can properly support a family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1720")

    label("loc_1683")


    ChrTalk(
        0xB,
        (
            "Just because you have the rare opportunity for\x01",
            "a break doesn't mean you should be lazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You have to use those chances to be\x01",
            "with your family...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1720")

    Jump("loc_204A")

    label("loc_1725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1833")

    ChrTalk(
        0xB,
        (
            "Even members of noble families have\x01",
            "their own quirks and different attitudes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although, I suppose my friends do act\x01",
            "dignified all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I imagine that shouldering the name of a noble\x01",
            "family requires a certain amount of decorum.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A1B")

    label("loc_1833")


    ChrTalk(
        0xB,
        (
            "Many of my old acquaintances are\x01",
            "from various noble households.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Every distinguished family in Crossbell comes\x01",
            "from a lineage of successful traders...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's no surprise those famous families have produced\x01",
            "a number of dignitaries over the years...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "While I hardly appreciate the notion of\x01",
            "descending from a 'distinguished' family,\x01",
            "they are all very much dignified people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I imagine that shouldering the name of a noble\x01",
            "family requires a certain amount of decorum.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A1B")

    Jump("loc_204A")

    label("loc_1A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AAE")

    ChrTalk(
        0xB,
        "Anri's becoming a lot more sociable these days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I bet he managed to make some friends.\x01",
            "I'm grateful to them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6C")

    label("loc_1AAE")


    ChrTalk(
        0xB,
        (
            "I get the feeling Anri has been playing outside\x01",
            "much more often these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And to think he was just a shy, little boy before...\x01",
            "Maybe he managed to find himself a good friend.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B6C")

    Jump("loc_204A")

    label("loc_1B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1C20")

    ChrTalk(
        0xB,
        "I think I'll sort through everyone's old clothes today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hopefully, that should make it so the kids\x01",
            "don't make a fuss when the season starts\x01",
            "to change.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204A")

    label("loc_1C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1D92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CA5")

    ChrTalk(
        0xB,
        "I'm knitting Anri a pair of pajamas.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hand-knitted clothes do a heck of a job\x01",
            "at keeping you warmer!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8D")

    label("loc_1CA5")


    ChrTalk(
        0xB,
        "I'm knitting Anri some pajamas.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, I guess it wouldn't hurt to spend\x01",
            "some mira for something nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anri's still young, though. Hand-knitted\x01",
            "clothes feel warmer, so it's okay for me\x01",
            "to cheap out this one time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D8D")

    Jump("loc_204A")

    label("loc_1D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E11")

    ChrTalk(
        0xB,
        (
            "I wish for these children to grow up\x01",
            "gaining many experiences that'll\x01",
            "teach them right from wrong.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF9")

    label("loc_1E11")


    ChrTalk(
        0xB,
        (
            "As we all know, there is plenty of good\x01",
            "and evil in this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As our society continues to progress,\x01",
            "I think the line between them will blur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's my hope that they'll grow up being\x01",
            "able to distinguish this line.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1EF9")

    Jump("loc_204A")

    label("loc_1EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F60")

    ChrTalk(
        0xB,
        (
            "Even if they end up being\x01",
            "a little reckless, a kid should\x01",
            "always be energetic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204A")

    label("loc_1F60")


    ChrTalk(
        0xB,
        (
            "My son gave Anri quite the scolding\x01",
            "for playing in such a dangerous place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But if you ask me, a boy his age should\x01",
            "be allowed to be a little reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Staying energetic is one of the\x01",
            "most important things for a kid.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_204A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_107F end

    def Function_10_2052(): pass

    label("Function_10_2052")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2165")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_209E")

    ChrTalk(
        0x9,
        (
            "Damn it! Today's not supposed to\x01",
            "be my turn!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_209E")


    ChrTalk(
        0x9,
        (
            "Stupid Cindy... How dare she dump\x01",
            "her chores onto me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Argh! Parties are being held all\x01",
            "over the city, now that the diet\x01",
            "is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm not going to make it in time\x01",
            "at this rate!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2160")

    Jump("loc_33CB")

    label("loc_2165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_22D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_21D0")

    ChrTalk(
        0x9,
        "Hasn't the diet adjourned already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'm tired of pointlessly waiting here!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22CE")

    label("loc_21D0")


    ChrTalk(
        0x9,
        (
            "I'm planning to attend the annual\x01",
            "budget celebration that should be\x01",
            "starting soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once I've heard Cindy's opinion,\x01",
            "I'll get Granny to give me a once-over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'm dressed to impress!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "All that's left to do is wait for the diet to end.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_22CE")

    Jump("loc_33CB")

    label("loc_22D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_24F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_239A")

    ChrTalk(
        0x9,
        (
            "Once the budget meeting has adjourned,\x01",
            "there are going to be some huge parties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is my one chance to become chummy with\x01",
            "some superstars! I'd better not screw up!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F0")

    label("loc_239A")


    ChrTalk(
        0x9,
        (
            "All right, I think I'm going to get dressed and\x01",
            "ask for Cindy's opinion on my threads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once the budget meeting has adjourned,\x01",
            "there are going to be some huge parties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Some of the business world's biggest\x01",
            "names, like IBC CEO Dieter Crois,\x01",
            "are going to be in attendance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. I'm trying to attend the same\x01",
            "party as him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_24F0")

    Jump("loc_33CB")

    label("loc_24F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_26B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25BA")

    ChrTalk(
        0x9,
        (
            "I've gotten pretty good at mixing into\x01",
            "some fancy parties these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Not going to lie, the political world can get\x01",
            "pretty scary when you get into the thick of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AF")

    label("loc_25BA")


    ChrTalk(
        0x9,
        (
            "I managed to worm my way into some party\x01",
            "sponsored by the Republican Faction once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently, all of the members were talking\x01",
            "smack about the plans during the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Man, the world of politics can be\x01",
            "pretty ruthless, can't it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_26AF")

    Jump("loc_33CB")

    label("loc_26B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_27BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_272A")

    ChrTalk(
        0x9,
        "Even my old man has to submit to Granny.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Gives me some nice laughs, that's for sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_27B5")

    label("loc_272A")


    ChrTalk(
        0x9,
        "My old man's taking a break from work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's a bit uncomfortable being around him,\x01",
            "considering we hardly see each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_27B5")

    Jump("loc_33CB")

    label("loc_27BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_28DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2855")

    ChrTalk(
        0x9,
        (
            "Now that the diet is in session, there's been\x01",
            "a lot more parties happening around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha. Which one do I go to today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D7")

    label("loc_2855")


    ChrTalk(
        0x9,
        (
            "I managed to buy myself a white tuxedo\x01",
            "with the money I had saved up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha. Time to rock the hell out of it tonight.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_28D7")

    Jump("loc_33CB")

    label("loc_28DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2966")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x9,
        (
            "Wow, to think that Granny used to be\x01",
            "a pro dancer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's pretty shocking, but I gotta hand it\x01",
            "to Granny!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_33CB")

    label("loc_2966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_29E4")
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_29D8")

    ChrTalk(
        0x9,
        "This is exactly why I'm asking you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I need to brush up on my dancing\x01",
            "skills!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29DB")

    label("loc_29D8")

    Call(0, 11)

    label("loc_29DB")

    OP_4C(0xA, 0xFF)
    Jump("loc_33CB")

    label("loc_29E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2B33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A74")

    ChrTalk(
        0x9,
        (
            "I can't embarrass myself like some\x01",
            "chump in front of all the ladies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Getting some practice will do me wonders.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B2E")

    label("loc_2A74")


    ChrTalk(
        0x9,
        (
            "Hmph. I've got a handsome face, so\x01",
            "why aren't I getting invited to parties?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I racked my brain and figured it out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I blow at dancing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I need to practice, and fast.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2B2E")

    Jump("loc_33CB")

    label("loc_2B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2C6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2BBB")

    ChrTalk(
        0x9,
        "Guess I'll do the laundry now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Man, why can't we just hire a maid to\x01",
            "handle all of this menial crap?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C66")

    label("loc_2BBB")


    ChrTalk(
        0x9,
        "We all take turns doing the chores here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Damn it! I had plans to hang out with\x01",
            "a friend from the Empire today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, well... I can't really defy Granny.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C66")

    Jump("loc_33CB")

    label("loc_2C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2E77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D2D")

    ChrTalk(
        0x9,
        (
            "Having to participate in high society is\x01",
            "no easy task, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I need to study a bunch, otherwise I'll have\x01",
            "no clue what the heck anybody's talking about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2D2D")


    ChrTalk(
        0x9,
        (
            "I went over to Times and bought myself two\x01",
            "colossal textbooks. One about politics, and\x01",
            "the other about economics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll need to learn about these kinds of topics\x01",
            "if I want to move up the societal leaderboard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I should look for 'Party Manners for Dummies'...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'm going to be readier than ever next time!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E72")

    Jump("loc_33CB")

    label("loc_2E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3084")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2ED6")

    ChrTalk(
        0x9,
        (
            "It's surprisingly hard to pretend like I'm a part\x01",
            "of high society.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307F")

    label("loc_2ED6")


    ChrTalk(
        0x9,
        (
            "I made acquaintances with the wife of some\x01",
            "famous company's president at a recent party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. I'm pretty excited to have conversed with\x01",
            "a celebrity like herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I know she was an economic theorist and all,\x01",
            "but I was still shocked by how smart she was.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "She kept using big words, so I kept nodding and\x01",
            "smiling while pretending like I had any idea\x01",
            "what she was talking about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_307F")

    Jump("loc_33CB")

    label("loc_3084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_31F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_311D")

    ChrTalk(
        0x9,
        "Granny lent me a really nice suit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if it was my pops' from when\x01",
            "he was a kid. I think I'll keep this a secret.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31EC")

    label("loc_311D")


    ChrTalk(
        0x9,
        (
            "Granny lent me a really nice suit when I\x01",
            "told her I was going to a party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha! I finally did it! I'll totally make my debut\x01",
            "into high society with this suit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Bless your kind soul, Granny!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_31EC")

    Jump("loc_33CB")

    label("loc_31F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_32BB")

    ChrTalk(
        0x9,
        (
            "Crossbell's high society's pretty famous,\x01",
            "considering all the celebrities and top\x01",
            "dogs of the business world that are in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Heheh... Think it's my turn to get in on the action.\x02",
    )

    CloseMessageWindow()
    Jump("loc_33CB")

    label("loc_32BB")


    ChrTalk(
        0x9,
        (
            "A dinner party where ladies and gentlemen gather...\x01",
            "That's the beauty of high society!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Actually, a certain wealthy someone's throwing\x01",
            "a pretty fancy party tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heh. Think I'll try to get in on the fun, too.\x01",
            "My interest in high society is insatiable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_33CB")

    TalkEnd(0xFE)
    Return()

    # Function_10_2052 end

    def Function_11_33CF(): pass

    label("Function_11_33CF")


    ChrTalk(
        0x9,
        "Hey, Sis! Be my dance partner for a bit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Huuuuuuh?! Why the heck should I do that?\x01",
            "Go practice by yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "How the heck am I supposed to dance on\x01",
            "my own, you dumbo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What?! You're the dumbo! Big, stupid,\x01",
            "dumbo brother!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_33CF end

    def Function_12_34C2(): pass

    label("Function_12_34C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_36DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_356B")

    ChrTalk(
        0xA,
        (
            "My brother wanted me to grade\x01",
            "his sense of fashion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't particularly mind, but boy, he\x01",
            "sure has a lot of free time on his hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36D6")

    label("loc_356B")

    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xA, 500)

    ChrTalk(
        0xA,
        "Eh. I guess it IS a pretty good outfit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If I take a long, hard look at you,\x01",
            "you're pretty handsome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wanna do me the honor of rephrasing that\x01",
            "'long, hard look' into something nicer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What do you want me to do? You look more\x01",
            "plain than vanilla ice cream at first glance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Whoa, Cindy! Cut me some slack here, will ya?!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x9, 0xFF)

    label("loc_36D6")

    Jump("loc_4439")

    label("loc_36DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_38C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_377F")

    ChrTalk(
        0xA,
        (
            "I bet Sophia must be pretty happy\x01",
            "having such a nice husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope I can find a great husband like that\x01",
            "soon... Just kidding! ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BF")

    label("loc_377F")


    ChrTalk(
        0xA,
        (
            "I'd be able to finish these chores early\x01",
            "if Anri'd give me a hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I just remembered that Mr. Hayworth said\x01",
            "he started working again recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I passed by him a little while ago, and\x01",
            "I noticed that he's looking a lot happier\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's almost as if I could feel the\x01",
            "love bursting outta him!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_38BF")

    Jump("loc_4439")

    label("loc_38C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3938")

    ChrTalk(
        0xA,
        "Aaaaaaaaaah! I got a Mishy strap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This is, like, the rarest Mishy!\x01",
            "It must be my lucky day!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_3938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_39BE")

    ChrTalk(
        0xA,
        (
            "Gotta wash the plates, or I'll\x01",
            "never have a date! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I need to hurry up so I can go and\x01",
            "check out the parade!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_39BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3A06")

    ChrTalk(
        0xA,
        "What should I buy at the department store?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A19")

    label("loc_3A06")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Call(0, 13)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)

    label("loc_3A19")

    Jump("loc_4439")

    label("loc_3A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AA1")

    ChrTalk(
        0xA,
        "Hurry up, Granny! We gotta get moving!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Geez, Anri! You're such a slowpoke!\x01",
            "Hurry up and get ready already!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4439")

    label("loc_3AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3B23")

    ChrTalk(
        0xA,
        (
            "I can't help but feel that Sophia\x01",
            "is hiding something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It's nothing more than a hunch, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C62")

    label("loc_3B23")


    ChrTalk(
        0xA,
        (
            "Sophia makes sure to go to\x01",
            "Mass every week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Not only is she super nice, but she's\x01",
            "also awesome at cooking and helps\x01",
            "her husband with his work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And yet I can't help but feel that\x01",
            "she's hiding something... She gets\x01",
            "this really sad look on her face at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It's nothing more than a hunch, though.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3C62")

    Jump("loc_4439")

    label("loc_3C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3E41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D27")

    ChrTalk(
        0xA,
        (
            "Dad usually has to go to work super early\x01",
            "in the morning and comes home late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think I'd like my future husband to work\x01",
            "somewhere with more reasonable hours.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3C")

    label("loc_3D27")


    ChrTalk(
        0xA,
        "Dad works as a manager at the IBC.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He told me he's the boss, so I guess he's\x01",
            "an important person there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He usually has to go to work super early\x01",
            "in the morning, and comes home late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wish he'd give himself a bit of a break and\x01",
            "relax for a little while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3E3C")

    Jump("loc_4439")

    label("loc_3E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3ECC")
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3EC0")

    ChrTalk(
        0xA,
        "Stop being so nutty over high society!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm pretty busy here, so deal with it\x01",
            "on your own!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3EC0")

    Call(0, 11)

    label("loc_3EC3")

    OP_4C(0x9, 0xFF)
    Jump("loc_4439")

    label("loc_3ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_402D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3F6A")

    ChrTalk(
        0xA,
        (
            "I have to go to Sophia's house for\x01",
            "cooking class now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're going to learn how to make a gratin\x01",
            "full of fresh seafood today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4028")

    label("loc_3F6A")


    ChrTalk(
        0xA,
        (
            "I have to go to Sophia's house for\x01",
            "cooking classes now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mmm... We're going to learn how to make\x01",
            "a gratin full of fresh seafood today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yep... I think this should be enough.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4028")

    Jump("loc_4439")

    label("loc_402D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_41C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_40D6")

    ChrTalk(
        0xA,
        (
            "I have cooking class at Sophia's house\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh* I wish my brother would give me a\x01",
            "helping hand instead of playing all the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C2")

    label("loc_40D6")


    ChrTalk(
        0xA,
        (
            "I have cooking class at Sophia's house\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Sophia's awesome at cooking, so I go\x01",
            "over there sometimes to learn a thing\x01",
            "or two from her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I have to hurry up and finish the chores\x01",
            "so I can get ready to head on over.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_41C2")

    Jump("loc_4439")

    label("loc_41C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_436E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_424B")

    ChrTalk(
        0xA,
        "Hmm. I think this should be enough seasoning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Not to brag, but I'm pretty proficient in housework.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4369")

    label("loc_424B")


    ChrTalk(
        0xA,
        "Hmm. I think this should be enough seasoning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Not to brag, but I'm pretty proficient in housework.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When I was little, Granny taught me everything\x01",
            "I know. Thanks to her, my cooking is something\x01",
            "to boast about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't you think I'd be an\x01",
            "awesome wife in the future?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4369")

    Jump("loc_4439")

    label("loc_436E")


    ChrTalk(
        0xA,
        (
            "Mom and Dad are always super busy, so\x01",
            "Granny's basically the head of the household.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ferrick, Anri, and I were practically\x01",
            "raised by her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And that being the case...we're all\x01",
            "Granny's kids!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4439")

    TalkEnd(0xFE)
    Return()

    # Function_12_34C2 end

    def Function_13_443D(): pass

    label("Function_13_443D")


    ChrTalk(
        0xA,
        (
            "I wanna go to the department store\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anri, dear. Is there some place you'd\x01",
            "like to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wanna see all the food stalls over\x01",
            "in the Harbor District!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That sounds like a good idea. Let's\x01",
            "head over that way today, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just let me know if you get tired\x01",
            "of walking, dear. Okay?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_13_443D end

    def Function_14_457B(): pass

    label("Function_14_457B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_465B")

    ChrTalk(
        0xFE,
        (
            "I was assigned to help with the\x01",
            "housework today... Guess I'll\x01",
            "probably be late for playtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do you think Ryu is behaving right now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He always goes off the rails when I don't\x01",
            "check in on him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A5A")

    label("loc_465B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_47C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_46FE")

    ChrTalk(
        0xC,
        (
            "So apparently, Ryu tried to chase down\x01",
            "the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Can't say I'm surprised. He's always had\x01",
            "as much energy as a suped-up orbment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BF")

    label("loc_46FE")


    ChrTalk(
        0xC,
        (
            "Today was as exhausting as I was expecting\x01",
            "it to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, by the way. Apparently, Ryu went to\x01",
            "go to check out the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I saw him arguing with his father.\x01",
            "W-Will he be okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_47BF")

    Jump("loc_4A5A")

    label("loc_47C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_484E")

    ChrTalk(
        0xC,
        "Umm... The laundry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Are you all going to see the parade?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It looks crowded out there, so\x01",
            "please be careful!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A5A")

    label("loc_484E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_48CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_48B7")

    ChrTalk(
        0xC,
        "Granny's going to take me later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Granny's always been super kind to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_48CA")

    label("loc_48B7")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Call(0, 13)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)

    label("loc_48CA")

    Jump("loc_4A5A")

    label("loc_48CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_495E")

    ChrTalk(
        0xC,
        (
            "She's usually a bit more strict, but she\x01",
            "gives me spending money for the festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Today's definitely going to be fun!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A5A")

    label("loc_495E")

    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "Oh, you're all here. What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm getting ready to go out\x01",
            "with my family right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Granny's usually a bit more strict, but she\x01",
            "gives me spending money for the festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Today's definitely going to be fun!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4A5A")

    TalkEnd(0xFE)
    Return()

    # Function_14_457B end

    def Function_15_4A5E(): pass

    label("Function_15_4A5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4B27")

    ChrTalk(
        0xD,
        (
            "Now that I think about it... My mother has always\x01",
            "delegated the housework to me since I was a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I can only assume it's because she wanted\x01",
            "to educate me on everything...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BAB")

    label("loc_4B27")


    ChrTalk(
        0xD,
        "My mother is forcing me to clean the house.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "Today was supposed to be a rare day off, too...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4BAB")

    TalkEnd(0xFE)
    Return()

    # Function_15_4A5E end

    SaveToFile()

Try(main)
