from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0220.bin",                # FileName
        "c0220",                    # MapName
        "c0220",                    # Location
        0x000D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 13, 0, 8, 0, 9],
    )

    BuildStringList((
        "c0220",                  # 0
        "Mr. Grimwood",           # 1
        "Mr. Grimwood",           # 2
        "Pete",                   # 3
        "BOA Officer",            # 4
        "Harold",                 # 5
    ))

    AddCharChip((
        "chr/ch05900.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch05902.itc",                   # 02
        "chr/ch27602.itc",                   # 03
        "chr/ch09302.itc",                   # 04
        "chr/ch00000.itc",                   # 05
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

    DeclNpc(0,       0,       0,       0,    385,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4510,    1169,    15779,   180,  341,  0x0, 0,   2,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(12869,   1000,    4809,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2259,    140,     5500,    90,   469,  0x0, 0,   3,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(2259,    140,     5500,    90,   389,  0x0, 0,   4,   0,   255, 255, 0,   17,  255,  0)

    DeclActor(14350,   1000,    -70,     2000,    14350,   2500,    -70,     0x007C, 0,  19, 0x0000)

    ScpFunction((
        "Function_0_228",          # 00, 0
        "Function_1_2E0",          # 01, 1
        "Function_2_355",          # 02, 2
        "Function_3_380",          # 03, 3
        "Function_4_3D8",          # 04, 4
        "Function_5_430",          # 05, 5
        "Function_6_488",          # 06, 6
        "Function_7_4E0",          # 07, 7
        "Function_8_51A",          # 08, 8
        "Function_9_839",          # 09, 9
        "Function_10_88C",         # 0A, 10
        "Function_11_116A",        # 0B, 11
        "Function_12_4374",        # 0C, 12
        "Function_13_45CA",        # 0D, 13
        "Function_14_475D",        # 0E, 14
        "Function_15_6501",        # 0F, 15
        "Function_16_660F",        # 10, 16
        "Function_17_66B7",        # 11, 17
        "Function_18_6851",        # 12, 18
        "Function_19_6F02",        # 13, 19
        "Function_20_6F34",        # 14, 20
        "Function_21_9ACB",        # 15, 21
        "Function_22_9B20",        # 16, 22
        "Function_23_9B75",        # 17, 23
        "Function_24_9BCA",        # 18, 24
        "Function_25_9C1F",        # 19, 25
        "Function_26_C503",        # 1A, 26
    ))


    def Function_0_228(): pass

    label("Function_0_228")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_268"),
        (1, "loc_274"),
        (2, "loc_280"),
        (3, "loc_28C"),
        (4, "loc_298"),
        (5, "loc_2A4"),
        (6, "loc_2B0"),
        (SWITCH_DEFAULT, "loc_2BC"),
    )


    label("loc_268")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_274")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_280")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_28C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_298")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2DF")

    Return()

    # Function_0_228 end

    def Function_1_2E0(): pass

    label("Function_1_2E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_354")
    OP_95(0xFE, 6850, 1000, 14410, 2000, 0x0)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 10890, 1000, 14410, 2000, 0x0)
    OP_95(0xFE, 10890, 1000, 17280, 2000, 0x0)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 10890, 1000, 14410, 2000, 0x0)
    Jump("Function_1_2E0")

    label("loc_354")

    Return()

    # Function_1_2E0 end

    def Function_2_355(): pass

    label("Function_2_355")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37F")
    OP_94(0xFE, 0x2684, 0x321E, 0x32BE, 0x3D86, 0x3E8)
    Sleep(300)
    Jump("Function_2_355")

    label("loc_37F")

    Return()

    # Function_2_355 end

    def Function_3_380(): pass

    label("Function_3_380")


    def lambda_385():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_385)

    def lambda_396():
        OP_95(0xFE, 3850, 30, 680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_396)
    WaitChrThread(0x101, 1)

    def lambda_3B4():
        OP_95(0xFE, 5780, 30, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B4)
    WaitChrThread(0x101, 1)
    Sleep(100)
    OP_93(0x101, 0x0, 0x3E8)
    Return()

    # Function_3_380 end

    def Function_4_3D8(): pass

    label("Function_4_3D8")


    def lambda_3DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3DD)

    def lambda_3EE():
        OP_95(0xFE, 3800, 30, -350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EE)
    WaitChrThread(0x102, 1)

    def lambda_40C():
        OP_95(0xFE, 4820, 30, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40C)
    WaitChrThread(0x102, 1)
    Sleep(100)
    OP_93(0x102, 0x0, 0x3E8)
    Return()

    # Function_4_3D8 end

    def Function_5_430(): pass

    label("Function_5_430")


    def lambda_435():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_435)

    def lambda_446():
        OP_95(0xFE, 2990, 30, 650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_446)
    WaitChrThread(0x103, 1)

    def lambda_464():
        OP_95(0xFE, 3680, 30, 1810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_464)
    WaitChrThread(0x103, 1)
    Sleep(100)
    OP_93(0x103, 0x0, 0x3E8)
    Return()

    # Function_5_430 end

    def Function_6_488(): pass

    label("Function_6_488")


    def lambda_48D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_48D)

    def lambda_49E():
        OP_95(0xFE, 1820, 30, -550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_49E)
    WaitChrThread(0x104, 1)

    def lambda_4BC():
        OP_95(0xFE, 2840, 30, 2150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4BC)
    WaitChrThread(0x104, 1)
    Sleep(100)
    OP_93(0x104, 0x0, 0x3E8)
    Return()

    # Function_6_488 end

    def Function_7_4E0(): pass

    label("Function_7_4E0")


    def lambda_4E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E5)

    def lambda_4F6():
        OP_95(0xFE, 2910, 30, 430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F6)
    WaitChrThread(0xFE, 1)
    Sleep(100)
    OP_93(0xFE, 0x0, 0x3E8)
    Return()

    # Function_7_4E0 end

    def Function_8_51A(): pass

    label("Function_8_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_554")
    SetChrPos(0x8, 7200, 1000, 18560, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 6750, 1020, 14000, 270)
    Jump("loc_7EC")

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_57D")
    SetChrPos(0x9, 6600, 140, 5500, 270)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_7EC")

    label("loc_57D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_5B7")
    SetChrPos(0x8, 1930, 1020, 17480, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 930, 1000, 16580, 0)
    Jump("loc_7EC")

    label("loc_5B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5DC")
    SetChrPos(0xA, 11280, 1000, 14370, 0)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_7EC")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5FB")
    SetChrPos(0xA, 5010, 1020, 12770, 0)
    Jump("loc_7EC")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_60E")
    SetChrFlags(0x9, 0x80)
    Jump("loc_7EC")

    label("loc_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_648")
    SetChrPos(0x8, 5270, 1020, 12800, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 4180, 1020, 12800, 90)
    Jump("loc_7EC")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0x9, 6600, 140, 5500, 270)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_7EC")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_690")
    SetChrPos(0x9, 6600, 140, 5500, 270)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_7EC")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6AF")
    SetChrPos(0xA, 6020, 1020, 15940, 270)
    Jump("loc_7EC")

    label("loc_6AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6BD")
    Jump("loc_7EC")

    label("loc_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6DC")
    SetChrPos(0xA, 5130, 1020, 12990, 0)
    Jump("loc_7EC")

    label("loc_6DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_716")
    SetChrPos(0x8, 1930, 1020, 17480, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 13280, 1000, -1500, 180)
    Jump("loc_7EC")

    label("loc_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_724")
    Jump("loc_7EC")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_732")
    Jump("loc_7EC")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_740")
    Jump("loc_7EC")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_77A")
    SetChrPos(0x8, 5270, 1020, 12800, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 4180, 1020, 12800, 90)
    Jump("loc_7EC")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A5")
    SetChrFlags(0x9, 0x80)

    label("loc_7A5")

    Jump("loc_7EC")

    label("loc_7AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7B8")
    Jump("loc_7EC")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_7CB")
    SetChrFlags(0xA, 0x80)
    Jump("loc_7EC")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7DE")
    SetChrFlags(0x9, 0x80)
    Jump("loc_7EC")

    label("loc_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7EC")
    SetChrFlags(0x9, 0x80)

    label("loc_7EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_807")
    Event(0, 26)
    Jump("loc_838")

    label("loc_807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_822")
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_838")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_838")
    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_838")

    Return()

    # Function_8_51A end

    def Function_9_839(): pass

    label("Function_9_839")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_852")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_858")

    label("loc_852")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_874")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_88B")

    label("loc_874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_88B")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_88B")

    label("loc_88B")

    Return()

    # Function_9_839 end

    def Function_10_88C(): pass

    label("Function_10_88C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_979")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AA")
    Call(0, 18)
    Jump("loc_974")

    label("loc_8AA")


    ChrTalk(
        0xFE,
        (
            "#2200FIn the meantime, I'll start looking\x01",
            "into Revache & Co.\x02\x03",
            "The confusion probably won't spread\x01",
            "too fast for now, but I don't see that\x01",
            "lasting for more than a day.\x02\x03",
            "I recommend you work quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_974")

    Jump("loc_1166")

    label("loc_979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_987")
    Jump("loc_1166")

    label("loc_987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_AAD")

    ChrTalk(
        0xFE,
        (
            "#2200FI have other work to do, but this whole\x01",
            "Heiyue matter is really bothering me.\x02\x03",
            "#2203FAbnormal physical abilities... Actually,\x01",
            "I feel like I heard about something like\x01",
            "that during an incident involving a cult.\x02\x03",
            "#2200FIt's probably my imagination, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0208F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1166")

    label("loc_AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_ABB")
    Jump("loc_1166")

    label("loc_ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_AC9")
    Jump("loc_1166")

    label("loc_AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD9")

    ChrTalk(
        0x8,
        (
            "#2200FHello, everyone. Harold already filled\x01",
            "me in on everything that happened.\x02\x03",
            "I'm happy to hear that you found Colin\x01",
            "before any harm could come to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FIt was close, but we managed.\x02\x03",
            "#0005FBy the way, Mr. Grimwood...\x02\x03",
            "#0000FYou wouldn't happen to be the lawyer that\x01",
            "helped Mr. Hayworth in the past, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2202FAll I did was help him climb out from\x01",
            "that hole of debt he was stuck in.\x02\x03",
            "#2203FBack then, he was in deep with a corrupt,\x01",
            "mafia-backed loan shark.\x02\x03",
            "#2200FHis interest rates were hardly what I would\x01",
            "call fair, so I lent him my aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FThat must have been horrible for him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FI'd bet anything that Revache was\x01",
            "the one pullin' the strings there, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FThey truly are quite the despicable lot.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EF7")

    label("loc_DD9")


    ChrTalk(
        0xFE,
        (
            "#2200FWallet, check... Keys, check...\x02\x03",
            "Considering it's the final day of the festival\x01",
            "and all, I decided Pete and I would take a\x01",
            "stroll around the city and enjoy ourselves.\x02\x03",
            "After all, a boatload of work awaits us\x01",
            "tomorrow. We might as well take the day\x01",
            "to relax and recharge, no?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF7")

    Jump("loc_1166")

    label("loc_EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_10CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1057")

    ChrTalk(
        0x8,
        (
            "#2200F*sigh* Where could I have\x01",
            "put that blasted folder?\x02\x03",
            "#2203FAt this rate, I'm going to be late for\x01",
            "my afternoon appointment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FIn the thick of things, huh, Mr. Grimwood?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200FYes, that's one way to put it. Since the\x01",
            "Anniversary Festival is next month, the\x01",
            "amount of appointments has skyrocketed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10C8")

    label("loc_1057")


    ChrTalk(
        0x8,
        (
            "#2200FI assure you, organization is not my forte.\x02\x03",
            "*sigh* I better go ahead and get Pete to\x01",
            "lend me a hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C8")

    Jump("loc_1166")

    label("loc_10CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E8")
    Call(0, 12)
    Jump("loc_1166")

    label("loc_10E8")

    TurnDirection(0x8, 0xA, 0)

    ChrTalk(
        0xFE,
        (
            "#2203FUm... Are you sure that's what happened?\x02\x03",
            "#2200FM-My apologies, Pete. I'll try to control\x01",
            "myself next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1166")

    TalkEnd(0xFE)
    Return()

    # Function_10_88C end

    def Function_11_116A(): pass

    label("Function_11_116A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11FE")
    Jump("loc_1248")

    label("loc_11FE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_121E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1248")

    label("loc_121E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_123E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1248")

    label("loc_123E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1248")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_127B")
    Jump("loc_436C")

    label("loc_127B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1369")

    ChrTalk(
        0xFE,
        (
            "#2200FI'll contact Sergei if I find out anything\x01",
            "about the missing persons case.\x02\x03",
            "#2203FThough, judging by the looks on your faces,\x01",
            "it doesn't seem to be an average case of\x01",
            "people going missing.\x02\x03",
            "Hmm... How concerning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436C")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1A39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190A")

    ChrTalk(
        0xFE,
        (
            "#2200FOh? Up and at it early this morning, aren't\x01",
            "we?\x02\x03",
            "Has something happened? If you need to\x01",
            "discuss anything, feel free to take a seat--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FNo, actually, sir...\x02\x03",
            "#0001FWe have reports that Heiyue Trading,\x01",
            "Ltd. was raided by a group of unknown\x01",
            "assailants.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "#2205FBy Aidios, is that true?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155A")

    ChrTalk(
        0x104,
        (
            "#0300FWe're on our way to go check it out\x01",
            "now, actually.\x02\x03",
            "Everything we've heard points to\x01",
            "Revache bein' our perps, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F8")

    label("loc_155A")


    ChrTalk(
        0x104,
        (
            "#0300FYeah, we just checked it out.\x02\x03",
            "Everything we saw points to Revache\x01",
            "bein' the culprit. The idiots even brought\x01",
            "out heavy machine guns for the raid.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F8")


    ChrTalk(
        0xFE,
        (
            "#2203FAn attack like that in the harbor...?\x02\x03",
            "#2201FI...can't say I understand what was going\x01",
            "through their heads.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#2201FRevache, that is.\x02\x03",
            "I can comprehend wanting to attack their\x01",
            "main competitor, but something about this\x01",
            "sounds sloppy--as if it wasn't planned...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe were actually thinking the same thing.\x02\x03",
            "Nothing about this suggests the beginning\x01",
            "of a full-fledged war between the mafias.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2201FHmm... Either way, we need to be cautious.\x02\x03",
            "I have no doubt businesses are going to\x01",
            "flock to the office once they hear the news.\x01",
            "With luck, they'll tell me something useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThank you, sir. Honestly, I don't think we've\x01",
            "ever stopped by without owing you another\x01",
            "favor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 6)
    Jump("loc_1A34")

    label("loc_190A")


    ChrTalk(
        0xFE,
        (
            "#2203FRaiding a competitor in such a populated area...?\x01",
            "Something about that doesn't sit right with me.\x02\x03",
            "#2201FAnyway, a lot of businesses will be feeling uneasy\x01",
            "because of the situation. And we still can't ignore\x01",
            "the possibility of retaliation by Heiyue.\x02\x03",
            "Be careful with all this, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A34")

    Jump("loc_436C")

    label("loc_1A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_20AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F32")

    ChrTalk(
        0xFE,
        "#2200FOh? Good afternoon, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHello, sir. It's been a while.\x02\x03",
            "You look like you're in a rush. Have\x01",
            "an appointment somewhere today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2201FIndeed. The more trouble the mafia stirs\x01",
            "up, the more I find on my plate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FThe mafia? As in Revache?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2203FYes. They've been up to some especially\x01",
            "shameful affairs...\x02\x03",
            "Property speculation, forcibly employing\x01",
            "bouncers at the Entertainment District...\x02\x03",
            "#2200FOne such circumstance ended with the\x01",
            "assault of a civilian, causing the poor\x01",
            "man to be sent to St. Ursula.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FTch. In other words, the guys over in\x01",
            "Revache are professional extortionists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2201FThat's certainly true, but...something\x01",
            "about how this is unfolding is odd...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "#2201FAre you patrolling the city, by chance?\x01",
            "If so, could you do me a favor and pay\x01",
            "extra attention for me?\x02\x03",
            "#2203FFor more ordinary circumstances, I'd\x01",
            "usually have the bracers be my eyes\x01",
            "and ears, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E2E")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1E2E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E54")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1E54")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E7A")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1E7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA0")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1EA0")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#0000FNo problem. You can count on us, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500F(There really are a lot of people relying\x01",
            "on the Special Support Section.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 5)
    Jump("loc_20A8")

    label("loc_1F32")


    ChrTalk(
        0xFE,
        (
            "#2200FToday, I'm going to meet with some company's\x01",
            "president who had a threat letter delivered to\x01",
            "his door.\x02\x03",
            "#2203FAfter taking care of it, I'd love to get back to the\x01",
            "office early, but I'm afraid things may not work\x01",
            "out that way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Poor Mr. Grimwood...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(We better keep our eyes peeled like we said.\x01",
            "You know, to make his life a little easier.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A8")

    Jump("loc_436C")

    label("loc_20AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_20BE")
    Call(0, 13)
    Jump("loc_436C")

    label("loc_20BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2457")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23ED")

    ChrTalk(
        0xFE,
        "#2205FHello there, Lloyd. Working alone today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FWell, only temporarily...\x02\x03",
            "#0000F(Might as well ask Mr. Grimwood about\x01",
            "Colin, too.)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked if\x01",
            "he knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xFE,
        "#2201FHmm? Harold's son has gone missing...?\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "#2203FI'm sorry, Lloyd. Right before the parade\x01",
            "started, a client ran in here looking for\x01",
            "some business advice.\x02\x03",
            "#2201FThis surprise appointment lasted the\x01",
            "entirety of the parade, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FThat's unlucky, sir. But as always,\x01",
            "thanks for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2203FYou know, I imagine Mrs. Hayworth is\x01",
            "beside herself with worry.\x02\x03",
            "#2201FLloyd, you must find this boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FY-Yes, sir. (Does he know something\x01",
            "about this that we don't...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    Jump("loc_2452")

    label("loc_23ED")


    ChrTalk(
        0xFE,
        (
            "#2203F...I imagine Mrs. Hayworth is beside\x01",
            "herself with worry.\x02\x03",
            "#2201FLloyd, you must find him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2452")

    Jump("loc_436C")

    label("loc_2457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2468")
    Call(0, 13)
    Jump("loc_436C")

    label("loc_2468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_27E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271A")

    ChrTalk(
        0xFE,
        (
            "#2203FIt, uh, seems as though I got caught\x01",
            "up in the moment last night and had\x01",
            "a few more drinks than necessary...\x02\x03",
            "This headache isn't going to make\x01",
            "today's work any easier, that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#0303F(Y'know, I actually ran into a bear once,\x01",
            "back in the Guardian Force...)\x02\x03",
            "#0300F(And honestly, Mr. Grimwood could pass\x01",
            "as its brother, lookin' like this.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2624")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2624")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_264A")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_264A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2670")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2670")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2696")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2696")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0006F(Please, for the love of Aidios, don't\x01",
            "let him hear you! I would prefer it if\x01",
            "Mr. Grimwood KEPT liking us...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27DF")

    label("loc_271A")


    ChrTalk(
        0xFE,
        (
            "#2203FIt, uh, seems as though I got caught\x01",
            "up in the moment last night and had\x01",
            "a few more drinks than necessary...\x02\x03",
            "This headache isn't going to make\x01",
            "today's work any easier, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27DF")

    Jump("loc_436C")

    label("loc_27E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28C3")

    ChrTalk(
        0xFE,
        (
            "#2200FHmm, this should be a solid first draft...\x02\x03",
            "You see, I was summoned to the symposium\x01",
            "being held this afternoon by some government\x01",
            "big-wigs, for whatever reason.\x02\x03",
            "Phew. I'd rather not screw this up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436C")

    label("loc_28C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2DD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEE")

    ChrTalk(
        0xFE,
        (
            "#2200FOh, hello. Have you four been making\x01",
            "your way around the festivities?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah, you could say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2200FHaha, that's good to hear.\x02\x03",
            "With the brave heroes who stopped Mayor\x01",
            "MacDowell's assassination on patrol, I'm\x01",
            "sure the citizenry will feel safe and secure.\x02",
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
        "#0302FWeeeell, when you say it like that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203F...It is quite embarrassing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FAgreed. I'm not sure if we deserve that\x01",
            "much flattery, Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2202FReally? But isn't it the truth? I don't see\x01",
            "any reason to be so humble, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FAnyway, sir, are you planning to go and\x01",
            "enjoy the Anniversary Festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2200FI'd like to, but unfortunately, I have work\x01",
            "and other things for the time being.\x02\x03",
            "#2203FAs you know, many enterprises operate\x01",
            "out of Crossbell, and they won't rest\x01",
            "because of a festival.\x02\x03",
            "#2200FI still want to find some time to take\x01",
            "a look around, if possible. It IS the\x01",
            "Anniversary Festival, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 6)
    Jump("loc_2DCC")

    label("loc_2CEE")


    ChrTalk(
        0xFE,
        (
            "#2200FIn the meantime, I've got some work\x01",
            "to wrap up.\x02\x03",
            "But still, I want to find some time to\x01",
            "take a look around, if possible.\x02\x03",
            "#2202FAfter all, I'm sure Pete would enjoy\x01",
            "the chance to goof off every once\x01",
            "in a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCC")

    Jump("loc_436C")

    label("loc_2DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_30A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3011")

    ChrTalk(
        0xFE,
        (
            "#2200FNice to see you, everyone.\x02\x03",
            "#2201FI heard that the threat letter case was\x01",
            "transferred to the First Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0105FYou knew already? I'm impressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2200FOh, no. Detective Dudley stopped by\x01",
            "earlier, that's all.\x02\x03",
            "He wanted to verify some new intel\x01",
            "about Yin and Heiyue's possible ties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FDudley's working on the case?\x02\x03",
            "#0003FWell, the First Division isn't wasting\x01",
            "any time, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FEh, not like there's anything we can\x01",
            "do about it now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 6)
    Jump("loc_30A1")

    label("loc_3011")


    ChrTalk(
        0xFE,
        (
            "#2201FArc en Ciel is in danger, hmm?\x02\x03",
            "#2203FA part of me hopes that this is all some\x01",
            "elaborate prank, but perhaps that's too\x01",
            "optimistic...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A1")

    Jump("loc_436C")

    label("loc_30A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_31EB")

    ChrTalk(
        0xFE,
        (
            "#2203FWe can't definitively say whether or not\x01",
            "there's a connection between Yin and\x01",
            "Heiyue.\x02\x03",
            "#2201FHowever, the fact remains that Heiyue's\x01",
            "branch manager is quite the cunning man.\x02\x03",
            "And considering that behind the facade of\x01",
            "trade hides an enormous crime syndicate,\x01",
            "I recommend you all be extremely careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436C")

    label("loc_31EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3633")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3530")

    ChrTalk(
        0xFE,
        (
            "#2200FOh, everyone. It's been a while.\x02\x03",
            "If the news has been any indication,\x01",
            "the Special Support Section has really\x01",
            "found its footing, hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWell...maybe. But we still can't hold\x01",
            "a candle to someone like you, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FYeah, those Revache thugs we caught\x01",
            "were basically bailed out as soon as\x01",
            "their rights were read.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2203FWell, it's common knowledge that the mafia\x01",
            "are deeply ingrained in Crossbellan society.\x02\x03",
            "#2200FThat being said, I believe your actions have\x01",
            "drawn out the light that was dimming in a\x01",
            "great many of the citizenry's hearts.\x02\x03",
            "I, too, was snapped out of that daze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThank you, Mr. Grimwood. Your words\x01",
            "mean more than you could ever know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2200FHaha, oh, no. I'm the one who should\x01",
            "be thanking you.\x02\x03",
            "Keep up the good work, Special Support\x01",
            "Section.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 5)
    Jump("loc_362E")

    label("loc_3530")


    ChrTalk(
        0xFE,
        (
            "#2200FLike many others, I was skeptical when\x01",
            "Sergei first told me about you. However...\x02\x03",
            "...you four have vastly surpassed my\x01",
            "hopes and expectations. Your actions\x01",
            "have spoken a thousand words.\x02\x03",
            "Please continue to work hard, Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_362E")

    Jump("loc_436C")

    label("loc_3633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3777")

    ChrTalk(
        0xFE,
        (
            "#2200FI primarily take jobs from clients that operate in\x01",
            "Crossbell City, but...\x02\x03",
            "Lately, perhaps due to the recent market growth,\x01",
            "the number of traders who take their business\x01",
            "to Armorica and Mainz has increased drastically.\x02\x03",
            "By the same token, my trips outside the city have\x01",
            "increased, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3851")

    label("loc_3777")


    ChrTalk(
        0xFE,
        (
            "#2200FSince I prefer a more hands-on approach\x01",
            "to my work, I always make sure to inspect\x01",
            "the places related to the cases I take.\x02\x03",
            "Thanks to that, I've started to take a lot\x01",
            "more business trips than previous years.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3851")

    Jump("loc_436C")

    label("loc_3856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E21")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#2200FThe Special Support Section?\x02\x03",
            "Has something popped up again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHuh? Oh, it's nothing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FWhat harm is there in telling him\x01",
            "about the case? After all,\x01",
            "he might know something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2200FNow that's smart thinking!\x02\x03",
            "Everything comes from discussion,\x01",
            "so ask me whatever you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWell, if you insist.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that the SSS has taken a case\x01",
            "revolving around the appearances of wolf-like\x01",
            "monsters throughout Crossbell State.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0xFE,
        (
            "#2200FWolf-like, you say? I certainly have\x01",
            "heard of them, but...\x02\x03",
            "#2203F...unfortunately, it's outside my area\x01",
            "of expertise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FHaha, no biggie. We figured as much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FHow did you come to hear about it,\x01",
            "Mr. Grimwood?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2200FAh, yes...\x02\x03",
            "A Mainz merchant recently asked me for an\x01",
            "appointment. He wanted to discuss the effects\x01",
            "the monsters were having on his business.\x02\x03",
            "#2203FHowever, thanks to the CGF's patrols, the\x01",
            "monsters haven't appeared since. The\x01",
            "appointment ultimately fell through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FThat corroborates the report we were given.\x01",
            "There don't seem to have been any new attacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FYeah. I say we still start our investigation\x01",
            "in Armorica Village, like we planned.\x02\x03",
            "#0000FAs always, we appreciate your help,\x01",
            "Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2200FMy pleasure. I'm just sorry that I couldn't\x01",
            "provide more help than I did.\x02\x03",
            "Remember, if you need anything else,\x01",
            "my doors are always open.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 0)
    Jump("loc_402C")

    label("loc_3E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F90")

    ChrTalk(
        0xFE,
        (
            "#2201FMy apologies, everyone. Monsters aren't\x01",
            "exactly my cup of tea.\x02\x03",
            "#2203FHowever, the fact that the same group\x01",
            "has appeared all over Crossbell is quite\x01",
            "bizarre, don't you think?\x02\x03",
            "Is it really normal for monster packs to\x01",
            "migrate that frequently?\x02\x03",
            "#2200FOh, well. Good luck with your\x01",
            "investigation, everyone. I'll be cheering\x01",
            "you on as usual.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_402C")

    label("loc_3F90")


    ChrTalk(
        0xFE,
        (
            "#2200FMy apologies, everyone. Monsters aren't\x01",
            "exactly my cup of tea.\x02\x03",
            "However, you can count on me cheering\x01",
            "for the Special Support Section's success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402C")

    Jump("loc_436C")

    label("loc_4031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_4363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_427C")

    ChrTalk(
        0xFE,
        (
            "#2200FOf course, I'd be overjoyed if the story I\x01",
            "told you four turned out to be a solid lead.\x02\x03",
            "Feel free to come visit again. If there's\x01",
            "anything else I can do to help you,\x01",
            "you can count on me to try.\x02\x03",
            "#2203FWell, I can't promise that I'll always be\x01",
            "able to help, but you won't know until you\x01",
            "stop by!\x02\x03",
            "#2201FConcern alone doesn't solve legal cases.\x01",
            "That's what's so tricky about them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FY-Yeah, that makes sense. I assure you,\x01",
            "Mr. Grimwood, if the opportunity comes\x01",
            "up, we'll take you up on your offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2202FGood to hear. I'll be waiting!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_435E")

    label("loc_427C")


    ChrTalk(
        0xFE,
        (
            "#2210FIf you need anything else, feel free to stop\x01",
            "by the office.\x02\x03",
            "#2200FAnd if I'm not around, you can always leave\x01",
            "a message with my assistant, Pete.\x02\x03",
            "Trust me, his skills when it comes to office\x01",
            "work far surpass mine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435E")

    Jump("loc_436C")

    label("loc_4363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_436C")

    label("loc_436C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_116A end

    def Function_12_4374(): pass

    label("Function_12_4374")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0xA, 0x8, 0)

    ChrTalk(
        0xA,
        (
            "Mr. Grimwood, you know last month's big\x01",
            "case? The payment we got doesn't line up\x01",
            "with what we initially wrote down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200FOh, that one? The client was in a bit of\x01",
            "a pinch when it came to financial security,\x01",
            "so I gave him a discount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Huh? Again?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Sir, we'll end up in the red if you keep\x01",
            "doing that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2205FY-You don't say...?\x02\x03",
            "#2203FSorry, Pete. I'll try to cut back on the\x01",
            "discounts in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh* You say that, but it's not like\x01",
            "you're going to change, sir!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "How can you be a lawyer and\x01",
            "be so ignorant about finances?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_12_4374 end

    def Function_13_45CA(): pass

    label("Function_13_45CA")

    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "Yes, the food stalls that were hit had most\x01",
            "of their proceeds stolen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We're lucky that the thieves were caught,\x01",
            "but it still caused a mountain of issues for\x01",
            "said stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now, they're looking for some sort of compensation\x01",
            "from the Business Owners' Association. You know, for\x01",
            "their troubles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2200FWell, I can tell you're sincere, at least.\x02\x03",
            "Very well. I'll take your case.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_13_45CA end

    def Function_14_475D(): pass

    label("Function_14_475D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4961")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48CD")

    ChrTalk(
        0x101,
        (
            "#0000FExcuse me, do you have a minute?\x02\x03",
            "I was wondering if you've been looking\x01",
            "after a kitten here, by any chance. If you\x01",
            "know anyone who is, that works, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "A kitten...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You know that this is a law office, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We can't let a cat live in here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FKid makes a good point.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8, 0x1, 0x5)
    Jump("loc_495C")

    label("loc_48CD")


    ChrTalk(
        0xFE,
        (
            "We can't let a cat wander around in\x01",
            "here, even if we wanted to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That definitely wasn't what I was\x01",
            "expecting to be asked about today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_495C")

    Jump("loc_64FD")

    label("loc_4961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4A5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A0A")

    ChrTalk(
        0xFE,
        "Something strange is happening...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've been getting so many phone calls\x01",
            "about Revache & Co. today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did something happen to them?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A55")

    label("loc_4A0A")


    ChrTalk(
        0xFE,
        "I've got a bad feeling about this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, be careful, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_4A55")

    Jump("loc_64FD")

    label("loc_4A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4AD5")

    ChrTalk(
        0xFE,
        "Mr. Grimwood has got a bunch of work to do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you busy working, too? If so,\x01",
            "work hard, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64FD")

    label("loc_4AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4C00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B69")

    ChrTalk(
        0xFE,
        (
            "Good morning. Did you need to talk\x01",
            "to Mr. Grimwood about something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He just started working on today's\x01",
            "agenda.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4BFB")

    label("loc_4B69")


    ChrTalk(
        0xFE,
        (
            "Morning cleaning is an important job\x01",
            "for an assistant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since Mr. Grimwood doesn't really care\x01",
            "about it, it's up to me to do it for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BFB")

    Jump("loc_64FD")

    label("loc_4C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4DC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D2C")

    ChrTalk(
        0xFE,
        "Mr. Grimwood is hard at work today, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The schedule says he has appointments\x01",
            "with five businesses in the city, and...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xFE,
        "C'mon, Mr. Grimwood, we need to hurry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2203FI-I know, Pete. At least let me finish up\x01",
            "these documents before heading out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4DC1")

    label("loc_4D2C")


    ChrTalk(
        0xFE,
        (
            "I'm sorry, everyone. Mr. Grimwood is\x01",
            "about to leave for some meetings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's not an emergency, would you\x01",
            "mind coming later this evening?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DC1")

    Jump("loc_64FD")

    label("loc_4DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_50A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD4")

    ChrTalk(
        0xFE,
        (
            "Oh, the Special Support Section? Sorry,\x01",
            "Mr. Grimwood is out on a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've been getting a lot of appointments\x01",
            "from foreign businesses lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, that's too bad. We were meaning to\x01",
            "ask him about how protective custody of\x01",
            "KeA will work.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4F53")

    ChrTalk(
        0x102,
        (
            "#0100FWell, there's nothing we can do about it.\x01",
            "Let's just stop by some other time, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FCC")

    label("loc_4F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4F9A")

    ChrTalk(
        0x103,
        (
            "#0200FWe can always see him some other\x01",
            "time, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FCC")

    label("loc_4F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4FCC")

    ChrTalk(
        0x104,
        "#0300FEh, there's always next time.\x02",
    )

    CloseMessageWindow()

    label("loc_4FCC")

    SetScenarioFlags(0x0, 1)
    Jump("loc_509B")

    label("loc_4FD4")


    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is out on a business trip.\x01",
            "You'd be surprised how many appointments\x01",
            "we've been getting from foreign businesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We ended up getting swamped with\x01",
            "work after the festival ended.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_509B")

    Jump("loc_64FD")

    label("loc_50A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5183")
    TurnDirection(0xA, 0x8, 0)

    ChrTalk(
        0xFE,
        "*cough* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood, aren't you forgetting\x01",
            "something? Like, the festival pamphlet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Remember, it lists the best order to\x01",
            "see all the food stalls, so try not to\x01",
            "get it mixed up, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64FD")

    label("loc_5183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_52AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_524C")

    ChrTalk(
        0xFE,
        (
            "They really went all out with this\x01",
            "year's parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Can't say I was expecting that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood could have at least taken\x01",
            "a little time off for the festival...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_52A8")

    label("loc_524C")


    ChrTalk(
        0xFE,
        (
            "I almost wish we'd get fewer appointments so\x01",
            "he could take a break every now and then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52A8")

    Jump("loc_64FD")

    label("loc_52AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5365")

    ChrTalk(
        0xFE,
        "A missing child?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We wouldn't know. Mr. Grimwood and\x01",
            "I didn't get to go watch the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could still hear all the fun parade music\x01",
            "from in here, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64FD")

    label("loc_5365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_548E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_542E")

    ChrTalk(
        0xFE,
        (
            "They really went all out with\x01",
            "this year's parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Can't say I was expecting that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood could have at least taken\x01",
            "a little time off for the festival...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5489")

    label("loc_542E")


    ChrTalk(
        0xFE,
        (
            "I almost wish we'd get less appointments\x01",
            "so he could take a break every now and\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5489")

    Jump("loc_64FD")

    label("loc_548E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_561C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5597")

    ChrTalk(
        0xFE,
        (
            "After yesterday's international symposium,\x01",
            "Mr. Grimwood went to a big dinner with a\x01",
            "lot of the attendees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, he doesn't handle drinks\x01",
            "very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yet he still drank quite a bit. Pretty\x01",
            "careless of him, if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5617")

    label("loc_5597")

    TurnDirection(0xA, 0x9, 0)

    ChrTalk(
        0xFE,
        (
            "Here, Mr. Grimwood. Something to\x01",
            "help clear your hangover!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Geez, sir. Try to remember your\x01",
            "limits next time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5617")

    Jump("loc_64FD")

    label("loc_561C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_580F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5779")

    ChrTalk(
        0xFE,
        (
            "In the afternoon, an international symposium is\x01",
            "going to be held in City Hall's reception hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'The current state and future of Crossbell...'\x01",
            "Guess they're going to talk about crime,\x01",
            "commerce, mira, and all that kinda stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood was invited to attend, but\x01",
            "I just hope he remembers when it starts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_580A")

    label("loc_5779")


    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is planning to attend the\x01",
            "international symposium that's being\x01",
            "held later today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just hope he remembers when it starts.\x02",
    )

    CloseMessageWindow()

    label("loc_580A")

    Jump("loc_64FD")

    label("loc_580F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_59C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F6")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood always treats me like I'm\x01",
            "a little kid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I mean, why the heck would I be\x01",
            "interested in some dumb festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Mr. Grimwood wanted to see it,\x01",
            "that'd be another story, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_59BD")

    label("loc_58F6")


    ChrTalk(
        0xFE,
        (
            "Ahem. I'm studying law under Mr. Grimwood\x01",
            "to become a great lawyer like him someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, if Mr. Grimwood told me he really wanted\x01",
            "to go to the parade, I'd naturally accompany\x01",
            "my teacher...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59BD")

    Jump("loc_64FD")

    label("loc_59C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5A8C")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood has another business trip\x01",
            "scheduled for next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's really been busy lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to prepare everything now so that\x01",
            "Mr. Grimwood isn't unorganized later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64FD")

    label("loc_5A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5BE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B49")

    ChrTalk(
        0xFE,
        (
            "I bet Crossbell would lose its mind if something\x01",
            "bad happened to Ilya Platiere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why did this have to happen right\x01",
            "before the Anniversary Festival...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5BDF")

    label("loc_5B49")


    ChrTalk(
        0xFE,
        (
            "I've heard a little bit about the situation\x01",
            "from Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No wonder he's so worried. Crossbell\x01",
            "would go crazy if something happened...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BDF")

    Jump("loc_64FD")

    label("loc_5BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5D33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C74")

    ChrTalk(
        0xFE,
        "Did you need Mr. Grimwood for something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He just took a break from work, so he\x01",
            "should be free to talk to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D2E")

    label("loc_5C74")


    ChrTalk(
        0xFE,
        (
            "If I remember correctly, Heiyue's Crossbell\x01",
            "branch manager is named Cao Lee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood tells me that you should watch\x01",
            "yourself around him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please be careful, everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_5D2E")

    Jump("loc_64FD")

    label("loc_5D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5EA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E26")

    ChrTalk(
        0xFE,
        (
            "*sigh* We've been getting more appointments\x01",
            "than usual as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It must be due to the odd influx of accidents\x01",
            "and legal disputes this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's definitely gotten more hectic here,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5E9F")

    label("loc_5E26")


    ChrTalk(
        0xFE,
        (
            "Accidents, legal disputes... Things have\x01",
            "been extra crazy around the office this\x01",
            "year, especially for Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E9F")

    Jump("loc_64FD")

    label("loc_5EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5F4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EBF")
    Call(0, 12)
    Jump("loc_5F47")

    label("loc_5EBF")

    TurnDirection(0xA, 0x8, 0)

    ChrTalk(
        0xFE,
        (
            "There's been times where you've\x01",
            "completely forgotten to collect\x01",
            "your pay at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm getting tired of it, to be frank!\x02",
    )

    CloseMessageWindow()

    label("loc_5F47")

    Jump("loc_64FD")

    label("loc_5F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_611F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6085")

    ChrTalk(
        0xFE,
        (
            "Sorting through information is just another\x01",
            "thing I need to learn to become a lawyer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there's something I don't understand,\x01",
            "I can always turn to Mr. Grimwood to\x01",
            "explain it to me. I really owe him a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though, I wish he would keep things\x01",
            "as organized as I left them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_611A")

    label("loc_6085")


    ChrTalk(
        0xFE,
        (
            "Despite being super busy, Mr. Grimwood\x01",
            "finds the time to help with my studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be forever grateful for him agreeing\x01",
            "to be my teacher.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_611A")

    Jump("loc_64FD")

    label("loc_611F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6184")

    ChrTalk(
        0xFE,
        "Are you a client?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you need Mr. Grimwood, he's over\x01",
            "at his desk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_625E")

    label("loc_6184")


    ChrTalk(
        0xFE,
        (
            "You know, Mr. Grimwood is great at a lot\x01",
            "of things, but organizing isn't one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These files on the shelf are practically useless\x01",
            "if you don't arrange them by judicial precedent\x01",
            "and chronological order.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_625E")

    Jump("loc_64FD")

    label("loc_6263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6352")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood said that he should be\x01",
            "back sometime this afternoon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Weird. Did he take on some other job?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Sometimes I get worried about\x01",
            "Mr. Grimwood's health. It's not good to\x01",
            "work nonstop like he does.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64FD")

    label("loc_6352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_64FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_643B")

    ChrTalk(
        0xFE,
        "Oh. Are you a client?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry, but Mr. Grimwood is out currently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business with him, please wait\x01",
            "over by the front until he comes back.\x01",
            "Feel free to sit down on one of the couches.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_64FD")

    label("loc_643B")


    ChrTalk(
        0xFE,
        (
            "Oh, sorry for the late introduction, everyone.\x01",
            "I'm Pete, Mr. Grimwood's assistant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm studying hard here to become a great\x01",
            "lawyer someday, one who can beat even\x01",
            "Mr. Grimwood himself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64FD")

    TalkEnd(0xFE)
    Return()

    # Function_14_475D end

    def Function_15_6501(): pass

    label("Function_15_6501")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6595")
    Jump("loc_65DF")

    label("loc_6595")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_65B5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65DF")

    label("loc_65B5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65D5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65DF")

    label("loc_65D5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65DF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Call(0, 13)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_6501 end

    def Function_16_660F(): pass

    label("Function_16_660F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66B6")
    OP_29(0x46, 0x1, 0xB)

    ChrTalk(
        0x101,
        (
            "#0001F(That should about cover West Street...)\x02\x03",
            "#0003F(I wonder how the search is going on\x01",
            "everyone else's end.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3308F(...)\x02",
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 7)

    label("loc_66B6")

    Return()

    # Function_16_660F end

    def Function_17_66B7(): pass

    label("Function_17_66B7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_674B")
    Jump("loc_6795")

    label("loc_674B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_676B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6795")

    label("loc_676B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_678B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6795")

    label("loc_678B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6795")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xC,
        (
            "#3608FWhere in the world are you, Rizero...?\x02\x03",
            "#3610FI refuse to believe a trader like yourself\x01",
            "would up and vanish without saying a\x01",
            "word.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_66B7 end

    def Function_18_6851(): pass

    label("Function_18_6851")

    EventBegin(0x0)
    Fade(500)
    OP_68(7200, 2320, 17750, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 6800, 1000, 17000, 0)
    SetChrPos(0x102, 7600, 1000, 16850, 0)
    SetChrPos(0x103, 6800, 1000, 15750, 0)
    SetChrPos(0x104, 7600, 1000, 15600, 0)
    OP_93(0x8, 0x0, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#2200FYes, this is Grimwood Law Office.\x02\x03",
            "#2203FHmm, really? That's the first I've heard\x01",
            "about it, too... Yes... Of course...\x02\x03",
            "#2200FNo, no. I'm terribly sorry about all of\x01",
            "this. If you need anything, please just\x01",
            "give me a call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FMr. Grimwood, was that about...?\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#2200FOh, welcome.\x02\x03",
            "Yes, well, no one has been able to get in\x01",
            "touch with Revache & Co.\x02\x03",
            "Because of that, I've been getting call after\x01",
            "call from companies who do business with\x01",
            "them and their competitors...\x02\x03",
            "I still have no idea what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FLloyd, do you think this is related to...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2205FWait, do you know something about this?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FEverything is still in the air, but...\x02\x03",
            "#0001F...Revache & Co. is completely empty.\x02\x03",
            "We can only assume that all of its\x01",
            "employees left to go somewhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2205FYou're absolutely positive?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FPlease, Mr. Grimwood. We'd like for\x01",
            "you to keep this confidential for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FThe CPD is in the middle of figuring\x01",
            "out how to best tackle the situation...\x02\x03",
            "So it might take some time to fully\x01",
            "assess the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2203FHmm, I'm afraid that the chaos will\x01",
            "only grow with the passage of time.\x02\x03",
            "#2201FVery well. In the meantime, I'll keep\x01",
            "conducting my own investigation into\x01",
            "Revache & Co.\x02\x03",
            "If there's anything I can do to keep\x01",
            "the situation from spiraling out of\x01",
            "control, I'll do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThank you, sir. We'll leave that to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FY'know, I doubt the mafia will leave\x01",
            "things like this for too long. I say we\x01",
            "try to hurry it up.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 7200, 1000, 17000, 0)
    SetScenarioFlags(0xED, 3)
    EventEnd(0x5)
    Return()

    # Function_18_6851 end

    def Function_19_6F02(): pass

    label("Function_19_6F02")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears to be locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_19_6F02 end

    def Function_20_6F34(): pass

    label("Function_20_6F34")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    OP_68(3700, 900, -600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 12600, 1000, 5600, 225)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrPos(0x101, -900, 0, -200, 90)
    SetChrPos(0x102, -900, 0, -200, 90)
    SetChrPos(0x103, -900, 0, -200, 90)
    SetChrPos(0x104, -900, 0, -200, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02200.itp")
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(650)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(650)
    BeginChrThread(0x103, 3, 0, 23)
    Sleep(650)
    BeginChrThread(0x104, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x10)

    NpcTalk(
        0x8,
        "Man's Voice",
        "#0400843VForget something, Detective?\x02",
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

    def lambda_7142():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7142)
    Sleep(50)

    def lambda_7152():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7152)
    Sleep(50)

    def lambda_7162():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7162)
    Sleep(50)

    def lambda_7172():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7172)
    OP_68(12600, 1500, 5600, 2000)
    OP_6F(0x1)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Bearded Man",
        (
            "#0400844V#6P#2200FOh, pardon me. I mistook you all for\x01",
            "someone else.\x02\x03",
            "#0400845VWelcome to the Grimwood Law Office.\x01",
            "How can I help you today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400846V#0000FOh, um...\x02",
    )

    CloseMessageWindow()

    def lambda_7269():
        OP_95(0xFE, 9500, 1000, -400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7269)
    Sleep(1500)
    Fade(500)
    OP_68(3700, 1100, -600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x103, 0x5A, 0x0)
    WaitChrThread(0x8, 1)

    def lambda_72D9():
        OP_95(0xFE, 4900, 0, -400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_72D9)
    WaitChrThread(0x8, 1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("Bearded Man")

    AnonymousTalk(
        0xFF,
        (
            "#0400847VNo need to hold back. If you have a\x01",
            "question, ask away.\x02\x03",
            "#0400848VThen again, you four look quite\x01",
            "young. Do you have questions about\x01",
            "loans?\x02\x03",
            "#0400849VOr perhaps you're looking for\x01",
            "potential business partners?\x02\x03",
            "#0400850VCome, now. Ask me anything!\x02",
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

    ChrTalk(
        0x101,
        "#0400851V#6P#0005FN-No, sir, it's nothing like that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400852V#3P#0305F(This guy's got a lotta energy.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400853V#6P#0205F(So this is the famous Grizzly Grim.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400854V#0102F(I see the rumors are true.)\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Bearded Man",
        (
            "#0400855V#11P#2205FHold on...\x02\x03",
            "#0400856VNow that I've taken a closer look,\x01",
            "I can't help but feel as if I've seen\x01",
            "you somewhere before, young man.\x02\x03",
            "#0400857V#2200FAre you one of the kids that used to\x01",
            "live in this neighborhood?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400858V#6P#0012FHaha, you remember me?\x02\x03",
            "#0400859V#0000FYou're right. I lived in one of the apartment\x01",
            "complexes here about three years ago.\x02\x03",
            "#0400860V#0004FAllow me to properly introduce myself.\x01",
            "My name is Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Bearded Man",
        (
            "#0400861V#11P#2202FYou did live here? Yes, that explains\x01",
            "why you look so familiar.\x02\x03",
            "#0400862V#2205FWait...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Bearded Man",
        (
            "#0400863V#11P#2205FBannings?!\x02\x03",
            "#0400864VThen you're Guy Bannings' younger\x01",
            "brother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400865V#6P#0005FHuh? Y-Yeah, I am.\x02\x03",
            "#0400866V#0000FYou knew my brother, then?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Bearded Man",
        "#0400867V#11P#2203FMore than just knew him, we...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    NpcTalk(
        0x8,
        "Bearded Man",
        (
            "#0400868V#11P#2200FNever mind. I suppose you're here\x01",
            "to discuss something important.\x02\x03",
            "#0400869VCome on in. You can fill me in on the\x01",
            "details once we take a seat.\x02\x03",
            "#0400870V#2203FOh, and where are my manners?\x02\x03",
            "#0400871V#2202FI'm Ian Grimwood, lawyer and owner\x01",
            "of this law firm.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x7D0)
    OP_68(4600, 1000, 5600, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 6600, 140, 5500, 270)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 2320, 140, 5800, 90)
    SetChrPos(0x102, 2320, 140, 4700, 90)
    SetChrPos(0x103, 4100, 140, 7400, 180)
    SetChrPos(0x104, 5000, 140, 7400, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    WaitBGM()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#0400872V#2203FI see. I was wondering when I would\x01",
            "meet that Special Support Section\x01",
            "Sergei was telling me about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(20500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x8,
        (
            "#0400873V#11P#2202FI actually read about you in the most\x01",
            "recent issue of the Crossbell Times.\x02\x03",
            "#0400874VYou certainly showed diligence and spunk\x01",
            "right out of the gate, didn't you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_END)), "loc_7CA9")

    ChrTalk(
        0x101,
        (
            "#0400875V#6P#0012FYeah, well, they sure took some liberties\x01",
            "with that article...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D02")

    label("loc_7CA9")


    ChrTalk(
        0x101,
        (
            "#0400876V#6P#0012FSounds like our first job might have been\x01",
            "a little exaggerated...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D02")


    ChrTalk(
        0x8,
        (
            "#0400877V#11P#2203FSo Guy's younger brother is a police officer\x01",
            "now, too? Oh, how time flies...\x02\x03",
            "#0400878VI can only assume this is Aidios' will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400879V#6P#0005FMr. Grimwood, what sort of relationship\x01",
            "did you have with my brother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400880V#11P#2202FWell, the same one you and I will have.\x01",
            "Guy used to drop by occasionally to\x01",
            "exchange information with me.\x02\x03",
            "#0400881VBut, as I'm sure you know, he was an\x01",
            "incredibly talented detective.\x02\x03",
            "#0400882VI'd wager he helped me far more than\x01",
            "I was able to help him.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x102,
        (
            "#0400883V#6P#0105FH-Hold on. There's something we're\x01",
            "missing here.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 0x1)
    Sleep(200)

    ChrTalk(
        0x102,
        "#0400884V#12P#0105FLloyd, your older brother is a detective...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)

    ChrTalk(
        0x104,
        (
            "#0400885V#5P#0302FThe hell, man? Why didn't you tell\x01",
            "us about him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400886V#1P#0200F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400887V#6P#0000FSorry, guys. I guess it never really crossed\x01",
            "my mind.\x02\x03",
            "#0400888V#0004FBesides... Guy's not with us anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400889V#12P#0101F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400890V#6P#0008FHe was killed in the line of duty.\x02\x03",
            "#0400891V#0002FAbout three years ago, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400892V#12P#0108FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400893V#5P#0301FThat explains why you moved away\x01",
            "from the city for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400894V#11P#2203FMy deepest and most sincere condolences.\x02\x03",
            "#0400895V#2201FBelieve it or not, I've conducted my own\x01",
            "investigations into that particular incident...\x02\x03",
            "#0400896VSadly, any leads that may exist eluded me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400897V#6P#0008FI-I see...\x02\x03",
            "#0400898V#0003FWell, let's just forget about his case for now.\x01",
            "It's not why we're here.\x02\x03",
            "#0400899V#0001FMr. Grimwood, I've already laid out our\x01",
            "case to you.\x02\x03",
            "#0400900VIf you have any information pertaining\x01",
            "to Revache and its activities, please,\x01",
            "tell us.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)

    ChrTalk(
        0x8,
        "#0400901V#11P#2203FRevache, hmm?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#0400902V#11P#2201FThat unsavory group is nothing but bad news.\x02\x03",
            "#0400903VIllegal dealings with both the Empire and the\x01",
            "Republic...\x02\x03",
            "#0400904V...the selling of stolen goods, mira laundering...\x02\x03",
            "#0400905V...weapon trafficking, operating as the middleman\x01",
            "for hiring jaegers... And that doesn't come close\x01",
            "to scratching the surface of their crimes.\x02\x03",
            "#0400906VHowever, no matter what sort of illegalities they've\x01",
            "committed, the fact remains that they were able to\x01",
            "take advantage of Crossbell's very unique situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400907V#6P#0005FCrossbell's unique situation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400908V#6P#0103FWhat he means is, while trade and\x01",
            "commerce have grown exponentially\x01",
            "over the past few years...\x02\x03",
            "#0400909V#0101F...Crossbell's political foundation has\x01",
            "begun to quickly deteriorate. Right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400910V#11P#2201FWell put. Crossbellan politics are currently in an\x01",
            "extremely fragile state.\x02\x03",
            "#0400911VMost politicians choose to align themselves with\x01",
            "either Erebonia or Calvard, and are nothing more\x01",
            "than greedy, power-hungry leeches.\x02\x03",
            "#0400912V#2203FThere's even a bill circulating within the diet that\x01",
            "cracks down on the mafia, but it won't be approved.\x01",
            "Too many diet members are connected to Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400913V#6P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400914V#5P#0301FAre you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400915V#6P#0106FUnfortunately, he is.\x02\x03",
            "#0400916V#0101FThe number of diet members tied to the\x01",
            "mafia is higher than I want to admit.\x02\x03",
            "#0400917VThat is probably the reason why the police\x01",
            "can't touch them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400918V#1P#0203FReality truly can be cold and cruel.\x02\x03",
            "#0400919V#0201FDoes that mean Revache can commit any\x01",
            "crime they want with no repercussions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400920V#11P#2200FNo, it hasn't gotten to that point yet.\x02\x03",
            "#0400921VIf they don't control themselves, they would\x01",
            "end up angering a majority of Crossbellans\x01",
            "and our surrounding nations.\x02\x03",
            "#0400922VTherefore, Revache has been treading a very\x01",
            "thin line in order to avoid directly interfering\x01",
            "with the citizenry's daily lives.\x02\x03",
            "#0400923V#2203FAnd as long as they don't cross that line,\x01",
            "the police can't lay a finger on them.\x02\x03",
            "#0400924V#2201FYou may wonder why they constantly look\x01",
            "down on people. Well, that's your answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400925V#6P#0108F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400926V#6P#0013FThis can't be real...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400927V#5P#0306FReality ain't so pretty.\x02\x03",
            "#0400928V#0302FBehind the city's glamorous facade are\x01",
            "shadows hell-bent on stirrin' up trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400929V#1P#0208FYes. I am curious as to how many classified\x01",
            "police documents detail these activities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400930V#11P#2203FAnyway, that's essentially all I know\x01",
            "about Revache.\x02\x03",
            "#0400931V#2201FHowever, I need to mention that the\x01",
            "situation with the mafia has taken a\x01",
            "turn.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400932V#6P#0005FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400933V#6P#0101FCould you explain?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400934V#11P#2201FWell, according to intel the CPD just\x01",
            "received...\x02\x03",
            "#0400935V...a new faction strong enough to rival\x01",
            "Revache has finally surfaced.\x02\x03",
            "#0400936VAnd I don't doubt that strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400937V#6P#0005FA new faction? Surely it's not the\x01",
            "Bracer Guild, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400938V#11P#2203FFor all intents and purposes, the Bracer Guild\x01",
            "is a positive establishment. This particular one\x01",
            "I'm talking about, however, is less so.\x02\x03",
            "#0400939V#2201FYou see, there's a powerful organization that\x01",
            "operates out of Calvard's Eastern Quarter.\x02\x03",
            "#0400940VAnd it's already managed to worm its way\x01",
            "into Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400941V#6P#0007FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400942V#6P#0101FYou're certain of this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400943V#11P#2203FYes. Previous rumors on this organization turned\x01",
            "out to be true, so I have no reason to be skeptical\x01",
            "now.\x02\x03",
            "#0400944V#2201FThey're called Heiyue.\x02\x03",
            "#0400945VJust recently, a new commercial unit, registered\x01",
            "under the name of Heiyue Trading Ltd, opened\x01",
            "for business in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400946V#6P#0001FHeiyue?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400947V#1P#0201FQuite the Eastern name.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400948V#5P#0303FThis could potentially escalate to a brawl\x01",
            "between two crime syndicates.\x02\x03",
            "#0400949V#0301FThat petty fight we saw between the street\x01",
            "gangs would be nothin' compared to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400950V#11P#2203FThe calm before the storm, if you will.\x02\x03",
            "#0400951VSo far, neither group has had the audacity to\x01",
            "make their struggle public.\x02\x03",
            "#0400952V#2201FHowever, I would be surprised if they weren't\x01",
            "already battling each other behind closed\x01",
            "doors, using a variety of methods.\x02\x03",
            "#0400953VThe First Division seems to be keeping a\x01",
            "close eye on the whole thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400954V#6P#0005FThe First Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400955V#6P#0105FSo the man with glasses who left\x01",
            "right when we arrived was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400956V#11P#2200FYes. That was Detective Dudley,\x01",
            "from the First Division.\x02\x03",
            "#0400957VCoincidentally, he was asking me\x01",
            "questions on the same topic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400958V#6P#0103FA coincidence, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400959V#6P#0008F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x103, 0x2)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#0400960V#1P#0205FLloyd?\x02\x03",
            "#0400961VIs there something bothering you?\x01",
            "You went quiet all of a sudden...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)

    ChrTalk(
        0x104,
        "#0400962V#5P#0301FLemme guess. You noticed something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400963V#6P#0003FYeah. I still need time to sort it all out\x01",
            "in my head, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 3300, 0, 5800, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0400964V#6P#0000FThank you very much, Mr. Grimwood.\x02\x03",
            "#0400965VWithout your help, we wouldn't have\x01",
            "been able to find the lead we needed\x01",
            "to put this case to bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400966V#11P#2203FThat so? I'm glad I was of assistance.\x02\x03",
            "#0400967V#2202FSergei has always been a tremendous help\x01",
            "to me. So, from both a personal and moral\x01",
            "standpoint, I support your work 100 percent.\x02\x03",
            "#0400968VIf you ever run into any problems, you can\x01",
            "always stop by my office and chat with me.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
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
    NewScene("c0200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_6F34 end

    def Function_21_9ACB(): pass

    label("Function_21_9ACB")


    def lambda_9AD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9AD0)

    def lambda_9AE1():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9AE1)
    WaitChrThread(0x101, 1)

    def lambda_9AFF():
        OP_95(0xFE, 2500, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9AFF)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_21_9ACB end

    def Function_22_9B20(): pass

    label("Function_22_9B20")


    def lambda_9B25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9B25)

    def lambda_9B36():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B36)
    WaitChrThread(0x102, 1)

    def lambda_9B54():
        OP_95(0xFE, 2500, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B54)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_22_9B20 end

    def Function_23_9B75(): pass

    label("Function_23_9B75")


    def lambda_9B7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9B7A)

    def lambda_9B8B():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9B8B)
    WaitChrThread(0x103, 1)

    def lambda_9BA9():
        OP_95(0xFE, 1200, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9BA9)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_23_9B75 end

    def Function_24_9BCA(): pass

    label("Function_24_9BCA")


    def lambda_9BCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9BCF)

    def lambda_9BE0():
        OP_95(0xFE, 300, 0, -200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9BE0)
    WaitChrThread(0x104, 1)

    def lambda_9BFE():
        OP_95(0xFE, 1200, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9BFE)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_24_9BCA end

    def Function_25_9C1F(): pass

    label("Function_25_9C1F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    OP_68(3700, 900, -600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 6200, 0, 8000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrPos(0x101, -900, 0, -200, 90)
    SetChrPos(0x102, -900, 0, -200, 90)
    SetChrPos(0x103, -900, 0, -200, 90)
    SetChrPos(0x104, -900, 0, -200, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02200.itp")
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(650)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(650)
    BeginChrThread(0x103, 3, 0, 23)
    Sleep(650)
    BeginChrThread(0x104, 3, 0, 24)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_9DA6():

        label("loc_9DA6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9DA6")

    QueueWorkItem2(0x101, 2, lambda_9DA6)
    WaitChrThread(0x102, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_9DCE():

        label("loc_9DCE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9DCE")

    QueueWorkItem2(0x102, 2, lambda_9DCE)
    WaitChrThread(0x103, 3)

    def lambda_9DE4():

        label("loc_9DE4")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9DE4")

    QueueWorkItem2(0x103, 2, lambda_9DE4)
    WaitChrThread(0x104, 3)

    def lambda_9DFA():

        label("loc_9DFA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9DFA")

    QueueWorkItem2(0x104, 2, lambda_9DFA)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#2100842V#12P#0000FExcuse us, sir.\x02",
    )

    CloseMessageWindow()
    OP_68(6200, 900, 8000, 1500)
    OP_6F(0x1)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0xE1, 0x1F4)

    ChrTalk(
        0x8,
        "#2100843V#2205FOh, come in, come in.\x02",
    )

    CloseMessageWindow()

    def lambda_9E95():
        OP_95(0xFE, 6200, 0, 1400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9E95)
    Sleep(1500)
    Fade(500)
    OP_68(3700, 900, -600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    WaitChrThread(0x8, 1)

    def lambda_9EE9():
        OP_95(0xFE, 4900, 0, -400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9EE9)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x10E, 0x1F4)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 5)), scpexpr(EXPR_END)), "loc_9FF8")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x8,
        "#2100844VContinuing to work hard, I see.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        "#2100845V#6P#0009FI could say the same to you, Mr. Grimwood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A175")

    label("loc_9FF8")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x8,
        (
            "#2100846VIt's been a while, hasn't it?\x02\x03",
            "#2100847VYou know, I've been hearing a lot\x01",
            "of stories about the Special\x01",
            "Support Section.\x02\x03",
            "All of which are very positive,\x01",
            "I might add.\x02",
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

    ChrTalk(
        0x101,
        (
            "#2100848V#6P#0009FWell, I'm sure you've been working just as\x01",
            "hard as us, Mr. Grimwood, if not more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A175")


    ChrTalk(
        0x102,
        "#2100849V#0102FRight. You look as busy as always, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100850V#2202F#11PHaha, well, you get used to it in this\x01",
            "line of work.\x02\x03",
            "#2100851V#2201FThat aside, something must have\x01",
            "happened, right?\x02\x03",
            "#2100852VThe looks on your faces make that\x01",
            "clear as day.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#2100853V#6P#0205FImpressive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100854V#3P#0300FHaha, was it that obvious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100855V#2203F#11PYou must remember, I see a mountain of\x01",
            "clients every day who wear a face like that\x01",
            "as they walk through my door.\x02\x03",
            "#2100856V#2200FLucky for you, I'm taking a break from work\x01",
            "right now, so you can ask me anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100857V#6P#0004FThank you, Mr. Grimwood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100858V#0100FI think we'll take you up on your\x01",
            "kind offer.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x7D0)
    OP_68(4600, 1000, 5600, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 6600, 140, 5500, 270)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 2320, 140, 5800, 90)
    SetChrPos(0x102, 2320, 140, 4700, 90)
    SetChrPos(0x103, 4100, 140, 7400, 180)
    SetChrPos(0x104, 5000, 140, 7400, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    SetCameraDistance(20500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x8,
        (
            "#2100859V#11P#2201FA threat letter sent to Arc en Ciel, hmm?\x02\x03",
            "#2100860VAnd you're curious as to whether the\x01",
            "author, Yin, is tied to Revache?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x101,
        "#2100861V#6P#0001FYes, sir. Do you have any idea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100862V#11P#2203FWell, unfortunately, I don't have any\x01",
            "information that connects the two of them...\x02\x03",
            "#2100863V...but that doesn't mean that I've never\x01",
            "heard the name Yin before.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2100864V#6P#0005FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100925V#6P#0101FWhat do you know about him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100866V#11P#2201FWell, I have no evidence that points\x01",
            "towards this being the same person...\x02\x03",
            "#2100867VWith that in mind, do you still want to\x01",
            "hear what I have to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100868V#6P#0000FYes, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100869V#5P#0300FHell, I think we'd take any clue we\x01",
            "can get our hands on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100870V#11P#2203FVery well, then. It all happened when\x01",
            "I went on a business trip to Calvard.\x02\x03",
            "#2100871VWhile walking about, I heard a bizarre\x01",
            "urban legend from a local.\x02\x03",
            "#2100872V#2201FIt involves a legendary xiongshou\x01",
            "referred to as Yin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100873V#6P#0001FSame as our perp...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100874V#6P#0101FIt certainly is an Eastern name.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100875V#1P#0205FWhat exactly is a xiongshou?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#2100876V#11P#0303FSomethin' along the lines of assassin\x01",
            "or killer.\x02\x03",
            "#2100877V#0300FPretty sure that's what they call 'em\x01",
            "in most of the Eastern regions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100878V#11P#2200FAren't you well informed?\x02\x03",
            "#2100879V#2203FI'd say it's somewhat similar to how we\x01",
            "customarily call mercenaries 'jaegers.'\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)

    ChrTalk(
        0x101,
        (
            "#2100880V#6P#0001FYou mentioned this was an urban\x01",
            "legend. There's more to it, I assume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100881V#11P#2201FYes, well, it's said that no one knows\x01",
            "for sure whether Yin is real or not.\x02\x03",
            "#2100882VThough, supposedly, he's said to wear a\x01",
            "mask and shawl of ebony, and he's never\x01",
            "once allowed someone to see his face.\x02\x03",
            "#2100883V#2203FHe appears and vanishes with the\x01",
            "shadows and has never let his prey\x01",
            "escape his fangs...\x02\x03",
            "#2100884V#2201FIn other words, he's a phantom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100885V#6P#0005FA phantom...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100886V#5P#0301FPretty silly story, if ya ask me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100887V#1P#0203FI suppose that is why it is called an\x01",
            "urban legend, Randy.\x02\x03",
            "#2100888V#0200FHowever, why would this so-called\x01",
            "legendary assassin send a threat\x01",
            "to Ilya Platiere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100889V#6P#0108FI didn't make the connection at first, either...\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2100890V#12P#0101FWhat if it's not Revache he's tied to, but\x01",
            "Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100891V#6P#0001FYeah, I was thinking the same thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100892V#11P#2201FHmm. It's true that Heiyue is a powerful\x01",
            "organization operating out of Calvard's\x01",
            "Eastern Quarter...\x02\x03",
            "#2100893VYou may be right. I wouldn't be shocked\x01",
            "if they knew the Eastern assassin.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#2100894V#11P#0300FThat'd definitely help Garcia's reaction\x01",
            "make more sense.\x02\x03",
            "#2100895V#0303FWe know for a fact that Revache and\x01",
            "Heiyue are facin' off against each other.\x02\x03",
            "#2100896V#0301FAnd if Heiyue and Yin are teaming up...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2100897V#5P#0205FDespite not being directly tied to Revache,\x01",
            "it would be highly likely that the mafia is\x01",
            "acutely aware of his presence.\x02\x03",
            "#2100898V#0202FThat, in and of itself, would support Lloyd\x01",
            "and Elie's theory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100899V#11P#2203FHmm, an intriguing thought.\x02\x03",
            "#2100900V#2200FBut that brings us back to your previous\x01",
            "question, Tio. Why would Yin threaten\x01",
            "Ilya Platiere, the lead star of Arc en Ciel?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2100901V#6P#0008FWell...we still need to figure that one out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100902V#1P#0200FWe know that Ilya and Revache's don\x01",
            "had an argument at a party...\x02\x03",
            "#2100903VCould it somehow be related to that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100904V#12P#0106FI don't know... It didn't really sound like\x01",
            "something that warranted a threat.\x02\x03",
            "#2100905V#0101FBesides, why would Heiyue react if\x01",
            "they're against Revache?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100906V#11P#0306FYeah, that doesn't make much sense.\x02\x03",
            "#2100907V#0301FDo you think we're dealing with someone\x01",
            "else who goes by the name Yin?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#2100908V#6P#0003FNot necessarily. We should assume that\x01",
            "every clue we've found so far is crucial to\x01",
            "the success of this case.\x02\x03",
            "#2100909VIt'd be irresponsible to disregard them just\x01",
            "because things aren't lining up right now.\x02\x03",
            "#2100910V#0001FHey, guys...\x02\x03",
            "#2100911VWhy don't we try paying Heiyue a visit?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#2100912V#12P#0105FWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100913V#11P#0301FWhoa, man. Where the hell did that come\x01",
            "from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100914V#6P#0006FThink about it like this.\x02\x03",
            "#2100915VWe know that Heiyue is strong enough for\x01",
            "Revache to keep an eye on them.\x02\x03",
            "#2100916V#0008FTo Revache, Heiyue is a rival that continues\x01",
            "to spread its influence and chip away at their\x01",
            "clutch of Crossbell's criminal underworld...\x02\x03",
            "#2100917V#0013FDepending on the circumstances, they could\x01",
            "prove even more dangerous than Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100918V#12P#0108FYou may be right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100919V#1P#0201FI see. This might be the perfect chance\x01",
            "to check whether or not that is true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100920V#11P#0306FHold up. Are we sure we're gonna be\x01",
            "okay if we suddenly barge in on 'em?\x02\x03",
            "#2100921V#0301FWe have no idea what kinda people\x01",
            "we're up against, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100922V#11P#2203FHmm, actually...\x02\x03",
            "#2100923V#2200FI recently met the manager of Heiyue\x01",
            "Trading's Crossbell branch.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        "#2100924V#6P#0005FSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100865V#6P#0105FWhy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100926V#11P#2200FHe requested an audit of the company to\x01",
            "ensure that there were no legal barricades\x01",
            "to the business operating in Crossbell.\x02\x03",
            "#2100927V#2203FI saw no harm in the request, so I accepted\x01",
            "the job...\x02\x03",
            "#2100928V#2201F...and it was then that I met him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100929V#6P#0001FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100930V#6P#0101FWhat kind of impression did he give off?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100931V#11P#2203FHmm... The word 'shrewd' certainly\x01",
            "comes to mind.\x02\x03",
            "#2100932VDespite his age, he's able to enrapture\x01",
            "others with his aloof manners and way\x01",
            "of speaking.\x02\x03",
            "#2100933V#2200FWell, at any rate, he struck me as somebody\x01",
            "who tends to think outside the box.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100934V#1P#0201FAn intellectual, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100935V#5P#0306FSounds like he's gonna be a hassle.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#2100936V#11P#0301FYou really think we can just walk in and\x01",
            "be like, 'Hey, man, wanna answer a few\x01",
            "questions?'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100937V#6P#0003FTrue. We have a valid reason to see\x01",
            "him, though.\x02\x03",
            "#2100938V#0000FWhat do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100939V#11P#0302F*sigh* Oh, this'll be fun.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2100940V#5P#0202FI am also quite curious about this\x01",
            "branch manager...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2100941V#12P#0103FSame here. I know a bit about Revache,\x01",
            "but Heiyue... We'll be going into this blind.\x02\x03",
            "#2100942V#0101FThis is a good opportunity for us to learn\x01",
            "more about how they operate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100943V#6P#0004FIt's decided, then.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2100944V#6P#0000FThanks for all your help, Mr. Grimwood.\x02\x03",
            "#2100945VIt looks like we'll be able to press on with\x01",
            "our investigation after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100946V#11P#2203FI'm happy to hear that.\x02\x03",
            "#2100947V#2202FHaha. You're reminding me of how Guy\x01",
            "used to work his cases.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2100948V#6P#0005FReally...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100949V#11P#2203FAnyway, Heiyue works under the guise of\x01",
            "a respectable trading company.\x02\x03",
            "#2100950VStopping by their office shouldn't cause\x01",
            "too much of a stir...\x02\x03",
            "#2100951V#2201FHowever, never forget that their true\x01",
            "identity is that of a massive, influential\x01",
            "crime syndicate.\x02\x03",
            "#2100952VDon't let your guard down around them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100953V#6P#0001FYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100954V#6P#0104FWe'll keep that in mind.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
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
    OP_68(4000, 1330, 2800, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 4000, 30, 2800, 180)
    SetChrPos(0x1, 4000, 30, 2800, 180)
    SetChrPos(0x2, 4000, 30, 2800, 180)
    SetChrPos(0x3, 4000, 30, 2800, 180)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x81, 0)
    OP_29(0x42, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_25_9C1F end

    def Function_26_C503(): pass

    label("Function_26_C503")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(4200, 1300, 5210, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, -1310, 0, 460, 90)
    SetChrPos(0x102, -1310, 0, -430, 90)
    SetChrPos(0x103, -1310, 0, 460, 90)
    SetChrPos(0x104, -1310, 0, -430, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C5EB")
    SetChrPos(0x10A, -1310, 0, -430, 90)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_C5EB")

    SetCameraDistance(19000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0xC,
        "#3601FMaybe we should contact the authorities, Ian...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2203F#11PHmm, but if we are proven wrong, this could\x01",
            "end up disastrous for him.\x02\x03",
            "#2201FI say we confirm our suspicions, first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3608FYou're probably right...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(103, 0, 100, 0)
    Fade(500)
    OP_68(640, 1300, 70, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 3)
    Sleep(800)
    OP_68(4330, 1300, 4160, 4000)
    BeginChrThread(0x102, 3, 0, 4)
    Sleep(950)
    BeginChrThread(0x103, 3, 0, 5)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    BeginChrThread(0x104, 3, 0, 6)
    Sleep(950)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C76E")
    BeginChrThread(0x10A, 3, 0, 7)

    label("loc_C76E")

    Sleep(50)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0xC, 0x2)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    ChrTalk(
        0x9,
        "#2205F#5POh, hello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600F#5PThe Special Support Section...\x02\x03",
            "#3609FHaha! Ian, I think Aidios might be shining\x01",
            "down on us today. They might be just what\x01",
            "we need to put an end to this matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2202F#5PIndeed. They have impeccable timing.\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C90F")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_C90F")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#0105F#12PExcuse me, but what exactly are you\x01",
            "talking about...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305F#12PSomethin' happen to you two?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2203F#5PWell, it's actually about the manager\x01",
            "of the trading company I mentioned\x01",
            "yesterday.\x02\x03",
            "#2201FSupposedly, he's gone off the grid.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAA1")
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_CAA1")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005F#12PReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3603F#5PIt appears so. You see, I'm acquaintances\x01",
            "with the Rizero Trade Company's owner....\x02\x03",
            "#3601F...and he isn't at home, nor do his\x01",
            "employees know where he is.\x02\x03",
            "So, I was just asking Ian whether or not\x01",
            "we should involve the police.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        "#0006F#11PI think I understand the situation...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0208F#12PDo you think he has...vanished?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CDF5")
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)

    ChrTalk(
        0x10A,
        (
            "#0603F#11PWell, due to the current circumstances, I'm\x01",
            "afraid the police won't be able to respond\x01",
            "right away.\x02\x03",
            "#0600FWould you care if we left the Special Support\x01",
            "Section handle this?\x02\x03",
            "I can get it cleared with the department once\x01",
            "I find the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2202F#5PIf Detective Dudley says we can rely on\x01",
            "you all, that's what we'll do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600F#5PIt's in your hands.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#11PDon't worry, we'll get to the bottom of it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CF89")

    label("loc_CDF5")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0003F#11PI'm sorry, Mr. Hayworth, but considering\x01",
            "the current state of things, the police may\x01",
            "have a hard time responding quickly.\x02\x03",
            "#0001FWith that in mind, would you mind if we\x01",
            "took the case?\x02\x03",
            "I'm sure that the department would\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600F#5POf course. Look into this for me, all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F#11PWill do. It might take some time, but you\x01",
            "can count on us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF89")

    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0001F#12PAlso, Mr. Grimwood. If you find any leads\x01",
            "on the missing people, could you forward\x01",
            "them to the chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2201F#5PYes, I can do that. Be careful, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0004F#12PWill do, sir.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#0308F#6P(Now that this is outta the way, we should\x01",
            "probably hurry it up...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0013F#11P(Agreed. Let's try not to take any more\x01",
            "unnecessary detours.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D12C")

    ChrTalk(
        0x10A,
        "#11P#0601F(Let's move!)\x02",
    )

    CloseMessageWindow()

    label("loc_D12C")

    OP_5A()
    SetChrPos(0x0, 5780, 30, 2800, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0xC8, 3)
    OP_29(0x4C, 0x1, 0xB)
    EventEnd(0x5)
    Return()

    # Function_26_C503 end

    SaveToFile()

Try(main)
