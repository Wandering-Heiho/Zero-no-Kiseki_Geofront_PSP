from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0350.bin",                # FileName
        "c0350",                    # MapName
        "c0350",                    # Location
        0x002D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0350",                  # 0
        "Bond",                   # 1
        "Creil",                  # 2
        "Sunita",                 # 3
        "Marie",                  # 4
        "Bond",                   # 5
        "Sunita",                 # 6
        "Sophia",                 # 7
    ))

    AddCharChip((
        "chr/ch27600.itc",                   # 00
        "chr/ch27602.itc",                   # 01
        "chr/ch33300.itc",                   # 02
        "chr/ch34400.itc",                   # 03
        "chr/ch34402.itc",                   # 04
        "chr/ch39000.itc",                   # 05
        "chr/ch09400.itc",                   # 06
    ))

    DeclNpc(-850,    0,       2529,    180,  261,  0x0, 0,   0,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(5590,    0,       -2119,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6920,    4000,    10069,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(5179,    4000,    5559,    315,  261,  0x0, 0,   5,   0,   0,   4,   0,   12,  255,  0)
    DeclNpc(7800,    4500,    7300,    0,    389,  0x0, 0,   1,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(7099,    4500,    7300,    0,    389,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-2150,   0,       3400,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)

    ScpFunction((
        "Function_0_1BC",          # 00, 0
        "Function_1_274",          # 01, 1
        "Function_2_29F",          # 02, 2
        "Function_3_2CA",          # 03, 3
        "Function_4_2F5",          # 04, 4
        "Function_5_320",          # 05, 5
        "Function_6_81B",          # 06, 6
        "Function_7_8B8",          # 07, 7
        "Function_8_11C6",         # 08, 8
        "Function_9_2A23",         # 09, 9
        "Function_10_33CD",        # 0A, 10
        "Function_11_4340",        # 0B, 11
        "Function_12_4538",        # 0C, 12
        "Function_13_478E",        # 0D, 13
        "Function_14_4D35",        # 0E, 14
        "Function_15_56E5",        # 0F, 15
        "Function_16_5A2D",        # 10, 16
        "Function_17_6230",        # 11, 17
    ))


    def Function_0_1BC(): pass

    label("Function_0_1BC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1FC"),
        (1, "loc_208"),
        (2, "loc_214"),
        (3, "loc_220"),
        (4, "loc_22C"),
        (5, "loc_238"),
        (6, "loc_244"),
        (SWITCH_DEFAULT, "loc_250"),
    )


    label("loc_1FC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_208")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_214")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_220")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_22C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_238")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_244")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_250")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_25C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_273")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_25C")

    label("loc_273")

    Return()

    # Function_0_1BC end

    def Function_1_274(): pass

    label("Function_1_274")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29E")
    OP_94(0xFE, 0x51E, 0xF6E, 0xFFFFF704, 0x154, 0x3E8)
    Sleep(300)
    Jump("Function_1_274")

    label("loc_29E")

    Return()

    # Function_1_274 end

    def Function_2_29F(): pass

    label("Function_2_29F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C9")
    OP_94(0xFE, 0xFFFFF2EA, 0x30C0, 0x3E8, 0x39C6, 0x3E8)
    Sleep(300)
    Jump("Function_2_29F")

    label("loc_2C9")

    Return()

    # Function_2_29F end

    def Function_3_2CA(): pass

    label("Function_3_2CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F4")
    OP_94(0xFE, 0x884, 0xFFFFFAEC, 0x1784, 0x168, 0x3E8)
    Sleep(300)
    Jump("Function_3_2CA")

    label("loc_2F4")

    Return()

    # Function_3_2CA end

    def Function_4_2F5(): pass

    label("Function_4_2F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31F")
    OP_94(0xFE, 0x119E, 0xDA2, 0x1716, 0x1BBC, 0x3E8)
    Sleep(300)
    Jump("Function_4_2F5")

    label("loc_31F")

    Return()

    # Function_4_2F5 end

    def Function_5_320(): pass

    label("Function_5_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_336")
    Event(0, 14)

    label("loc_336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_386")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 5350, 4000, 6980, 180)
    SetChrPos(0xA, 5350, 4000, 6410, 0)
    SetChrPos(0xE, 5590, 0, -2120, 180)
    SetChrFlags(0xA, 0x10)
    Jump("loc_80B")

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3CE")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, -1000, 0, 3400, 270)
    SetChrPos(0xA, -1060, 4000, 13010, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3C9")
    SetChrFlags(0xE, 0x10)

    label("loc_3C9")

    Jump("loc_80B")

    label("loc_3CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_425")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -1210, 4000, 13380, 135)
    SetChrPos(0xA, 5230, 4000, 6980, 180)
    SetChrPos(0xB, 5230, 4000, 6250, 0)
    BeginChrThread(0xB, 0, 0, 0)
    BeginChrThread(0x8, 0, 0, 2)
    SetChrFlags(0xA, 0x10)
    Jump("loc_80B")

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_46F")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -2100, 4000, 17500, 270)
    SetChrPos(0xA, 1450, 4000, 9960, 315)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46A")
    SetChrFlags(0xA, 0x10)

    label("loc_46A")

    Jump("loc_80B")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4A5")
    SetChrPos(0x8, -1210, 4000, 13380, 135)
    BeginChrThread(0x8, 0, 0, 2)
    SetChrPos(0xA, 3490, 4000, 8150, 315)
    Jump("loc_80B")

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4DF")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrPos(0xA, 3490, 4000, 8150, 315)
    Jump("loc_80B")

    label("loc_4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_501")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_80B")

    label("loc_501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_54B")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -1210, 4000, 13380, 135)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_80B")

    label("loc_54B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5A1")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrPos(0xA, 5230, 4000, 6980, 180)
    SetChrPos(0xB, 5230, 4000, 6250, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_80B")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5FC")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 5230, 4000, 6980, 180)
    SetChrPos(0xB, 5230, 4000, 6250, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_80B")

    label("loc_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_61B")
    SetChrPos(0xA, 3310, 4000, 4760, 270)
    Jump("loc_80B")

    label("loc_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_67C")
    SetChrPos(0x8, -1210, 4000, 13380, 135)
    BeginChrThread(0x8, 0, 0, 2)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 5230, 4000, 6980, 180)
    SetChrPos(0xB, 5230, 4000, 6420, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_677")
    SetChrFlags(0xA, 0x10)

    label("loc_677")

    Jump("loc_80B")

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6C7")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrPos(0xA, 5250, 4000, 8250, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6C2")
    SetChrFlags(0xA, 0x10)

    label("loc_6C2")

    Jump("loc_80B")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_77A")
    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_721")
    SetChrPos(0xA, 5250, 4000, 8250, 180)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71C")
    SetChrFlags(0xA, 0x10)

    label("loc_71C")

    Jump("loc_775")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_END)), "loc_754")
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_775")

    label("loc_754")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrSubChip(0xC, 0x1)
    SetChrSubChip(0xD, 0x2)

    label("loc_775")

    Jump("loc_80B")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7BF")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 3760, 0, -450, 270)
    BeginChrThread(0xA, 0, 0, 3)
    Jump("loc_80B")

    label("loc_7BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7F2")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_80B")

    label("loc_7F2")

    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80B")
    SetChrFlags(0xA, 0x10)

    label("loc_80B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_81A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 16)

    label("loc_81A")

    Return()

    # Function_5_320 end

    def Function_6_81B(): pass

    label("Function_6_81B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_834")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_83A")

    label("loc_834")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_856")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_86D")

    label("loc_856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_86D")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_86D")

    label("loc_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_897")
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B7")
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_8B7")

    Return()

    # Function_6_81B end

    def Function_7_8B8(): pass

    label("Function_7_8B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_9DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_968")

    ChrTalk(
        0x8,
        (
            "Screw the manager. Where does he get off\x01",
            "tellin' me I have a big ego?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Who the hell does he think got us through\x01",
            "that absolute clown show?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D8")

    label("loc_968")


    ChrTalk(
        0x8,
        "Huh? The hell are you guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm kinda on edge right now. Just,\x01",
            "do me a favor and piss off for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_9D8")

    Jump("loc_11C2")

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A50")

    ChrTalk(
        0x8,
        "Wait, aren't I totally awesome?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, whatever. It's all the same anyway!\x01",
            "Hahaha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B20")

    label("loc_A50")


    ChrTalk(
        0x8,
        (
            "What a bunch of morons... The price of\x01",
            "those stocks friggin' tanked in three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "They seriously couldn't see that comin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The CNS business magazine is run by\x01",
            "a circus of clowns! Hahahaha!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B20")

    Jump("loc_11C2")

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_CA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BB2")

    ChrTalk(
        0x8,
        (
            "Man, what should I do with these fat stacks\x01",
            "of cash? Maybe I'll throw down for a\x01",
            "brand-spankin' new orbal car...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9F")

    label("loc_BB2")


    ChrTalk(
        0x8,
        (
            "Whew... This is pretty nice. Ordering from\x01",
            "a catalog was a pretty sick idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Doesn't this car look sick? Just look\x01",
            "at this bad boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a man working the stock market, I've\x01",
            "always wanted to get my hands on an\x01",
            "orbal car.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C9F")

    Jump("loc_11C2")

    label("loc_CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_CB2")
    Jump("loc_11C2")

    label("loc_CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_CC0")
    Jump("loc_11C2")

    label("loc_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_CCE")
    Jump("loc_11C2")

    label("loc_CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D8C")
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "I explained it to my wife as clear as day,\x01",
            "but she still doesn't understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She can't understand why I'd ever\x01",
            "want an orbal car.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3E")

    label("loc_D8C")


    ChrTalk(
        0x8,
        "My wife's family is well off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I guess that's why she's uninterested\x01",
            "in these sorts of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But I was expecting her to at least give me\x01",
            "a yes or no answer...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E3E")

    Jump("loc_11C2")

    label("loc_E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_100D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EE2")

    ChrTalk(
        0x8,
        "This is a pretty big opportunity for us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I should hear my wife's opinion before\x01",
            "I make any hasty decisions, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1008")

    label("loc_EE2")


    ChrTalk(
        0x8,
        "Our company's performance has been spectacular.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll be helping them launch a new branch office\x01",
            "in the Kreuzen province of eastern Erebonia\x01",
            "next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm... There's something troubling me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The management at my company asked\x01",
            "me if I'd like to become a branch manager...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1008")

    Jump("loc_11C2")

    label("loc_100D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_101B")
    Jump("loc_11C2")

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1029")
    Jump("loc_11C2")

    label("loc_1029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1037")
    Jump("loc_11C2")

    label("loc_1037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1045")
    Jump("loc_11C2")

    label("loc_1045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10DE")

    ChrTalk(
        0x8,
        "My wife is about as relaxed as a person can get.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Suppose I can't really fault her for it...\x01",
            "Guess I'll just brew the tea myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C2")

    label("loc_10DE")


    ChrTalk(
        0x8,
        (
            "I finally managed to get a break from work,\x01",
            "so I think I'll take this opportunity to drink\x01",
            "my wife's excellent black tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Actually... Where even is she? I don't see her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "She might be watering the plants still.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11C2")

    TalkEnd(0xFE)
    Return()

    # Function_7_8B8 end

    def Function_8_11C6(): pass

    label("Function_8_11C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E8")
    Call(0, 15)
    Return()

    label("loc_11E8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_127C")
    Jump("loc_12C6")

    label("loc_127C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_129C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12C6")

    label("loc_129C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12C6")

    label("loc_12BC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12C6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_14D9")
    OP_64(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1427")

    ChrTalk(
        0xFE,
        "You have to be kidding me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I take ONE day off during the Anniversary Festival\x01",
            "and I suffer a loss?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only that, but it was in one of my favorite\x01",
            "clients' stocks... This is just RICH.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to find some way to make up for\x01",
            "these losses before it goes public...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C2")

    label("loc_1427")


    ChrTalk(
        0xFE,
        (
            "I work for the best securities firm in Crossbell,\x01",
            "so this CAN'T become public...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll need to make up for these losses by\x01",
            "the end of the week...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C2")

    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2A1B")

    label("loc_14D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_155E")

    ChrTalk(
        0xC,
        "Man, I'm starving.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Think I might order myself a pizza. The wife and\x01",
            "daughter aren't coming back for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_155E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_163D")

    ChrTalk(
        0xC,
        "Okay, now for the Reinford Company stocks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The best opportunities tend to arise while everybody\x01",
            "is busy celebrating, instead of paying attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "A stockbroker can't afford to feel exhausted.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_163D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_186A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_170F")

    ChrTalk(
        0xC,
        (
            "Businesses are booming, and stocks are rising\x01",
            "more than I expected this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is a do-or-die moment for a stockbroker\x01",
            "like myself... I can't slack off for a single second.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_170F")


    ChrTalk(
        0xC,
        (
            "People who pay attention during the festivities will\x01",
            "notice that some stocks begin to skyrocket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Arc en Ciel has been fantastic, and Mishelam's theme\x01",
            "park shows promise for Crossbell's economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've heard that hotels are totally booked and some\x01",
            "restaurants are filled with reservations. Pretty\x01",
            "fascinating, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1865")

    Jump("loc_2A1B")

    label("loc_186A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_19DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18F0")

    ChrTalk(
        0xC,
        (
            "It's pretty lonely without the wife and kid here, but\x01",
            "I'll continue to keep working hard for their sakes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D6")

    label("loc_18F0")


    ChrTalk(
        0xC,
        (
            "My wife looked like she was about to pass out from\x01",
            "boredom, so I told her to check out the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "All of a sudden, her purse was loaded and ready to go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Did she really wanna check out the festival\x01",
            "that badly?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19D6")

    Jump("loc_2A1B")

    label("loc_19DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1BED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AA0")

    ChrTalk(
        0xC,
        (
            "Stockbrokers like myself have to kick it into high gear\x01",
            "during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "When every day's a fierce battle, there's clearly\x01",
            "no time to take a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE8")

    label("loc_1AA0")


    ChrTalk(
        0xC,
        (
            "Crossbell's market shifts all over the place during\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Everyone's trying to make a quick buck, so the\x01",
            "stock market overheats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm willing to bet Crossbell's economy is going\x01",
            "to have its fair share of violent flare-ups and\x01",
            "cool-downs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I can't afford to lose focus for even a moment.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BE8")

    Jump("loc_2A1B")

    label("loc_1BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CCC")

    ChrTalk(
        0xC,
        (
            "I'll still have a massive load of work\x01",
            "to deal with, regardless of whether\x01",
            "I transfer to the Empire or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm also worried about my family, so I chose\x01",
            "to continue working my hardest here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E67")

    label("loc_1CCC")


    ChrTalk(
        0xC,
        (
            "So, I actually ended up turning down the\x01",
            "offer to become a manager for one of\x01",
            "the Erebonian branches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm already constantly exhausted, and my wife\x01",
            "and I agreed it's best for the family to stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I thought this would have been my big\x01",
            "break as a stockbroker...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But now that I think about it, I already have\x01",
            "a massive load of work to deal with, whether\x01",
            "I transfer to the Empire or not.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E67")

    Jump("loc_2A1B")

    label("loc_1E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_21C1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2014")

    ChrTalk(
        0xFE,
        (
            "Some bracer paid us a visit yesterday.\x01",
            "He simply asked us if we'd be able to\x01",
            "take in a stray kitten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was obviously surprised, but apparently,\x01",
            "Sunita had been secretly taking care of\x01",
            "it for a while now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe that silly daughter of mine\x01",
            "never mentioned it to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, we've now added another member to\x01",
            "the family, and it's all thanks to that bracer!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20DD")

    label("loc_2014")


    ChrTalk(
        0xFE,
        (
            "As per the bracer's suggestion, we decided\x01",
            "to adopt the stray kitten. I'm sure Sunita is\x01",
            "more than happy about our decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Given the circumstances, I'm glad\x01",
            "we decided to keep it up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DD")

    Jump("loc_21BC")

    label("loc_20E2")


    ChrTalk(
        0xFE,
        (
            "My cute little Sunita hasn't left the kitten's\x01",
            "side since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Taking care of a pet is no easy feat, so a part\x01",
            "of me thought she'd easily give up. However,\x01",
            "I don't think I have anything to worry about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BC")

    Jump("loc_2A1B")

    label("loc_21C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_26BF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2367")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FF")

    ChrTalk(
        0xFE,
        (
            "Sunita is completely devoted to caring\x01",
            "for that little kitten of ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'd think she would have asked me if we\x01",
            "could keep the kitten if she loves it so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, considering how Sunita usually acts,\x01",
            "she was probably too worried I'd refuse\x01",
            "to let the cat stay.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2362")

    label("loc_22FF")


    ChrTalk(
        0xFE,
        "At any rate, I thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. My Sunita seems to have caused you\x01",
            "all a bit of trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2362")

    Jump("loc_26BA")

    label("loc_2367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_END)), "loc_2474")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2403")

    ChrTalk(
        0xFE,
        (
            "Sunita must have gone somewhere outside\x01",
            "to play again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How strange... She's always pestering me\x01",
            "to read her stories...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_246F")

    label("loc_2403")


    ChrTalk(
        0xFE,
        (
            "Sunita's been acting a little odd\x01",
            "as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps she's finally entered her\x01",
            "rebellious phase.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246F")

    Jump("loc_26BA")

    label("loc_2474")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_24E4")

    ChrTalk(
        0xFE,
        "We don't keep pets in our home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm sorry we couldn't be of any help to you.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xC, 0x1)
    Return()

    label("loc_24E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E2")

    ChrTalk(
        0xFE,
        (
            "I figured I could use a break from work, so\x01",
            "I'm reading my daughter a book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way... You're not responsible for\x01",
            "damaging all of my documents, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, never mind. Don't pay me any mind.\x01",
            "I'm just talking to myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26AE")

    label("loc_25E2")


    ChrTalk(
        0xFE,
        (
            "Sometimes when I leave my documents\x01",
            "on the table, they get all torn up... It ends\x01",
            "up making my work much more difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sunita clearly would never do such a thing,\x01",
            "so who might the culprit be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xC, 0x1)
    Return()

    label("loc_26BA")

    Jump("loc_2A1B")

    label("loc_26BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_27EF")
    SetChrSubChip(0xC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278D")

    ChrTalk(
        0xFE,
        "Okay, I need those documents for the bonds.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, right.\x01",
            "They got torn up last week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, but seriously. What would possess someone\x01",
            "to do something so terrible?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27EA")

    label("loc_278D")


    ChrTalk(
        0xFE,
        (
            "It ends up causing me so much trouble when\x01",
            "important documents get torn up like that...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27EA")

    Jump("loc_2A1B")

    label("loc_27EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_28C0")

    ChrTalk(
        0xC,
        (
            "A myriad of financial tools have been developed\x01",
            "in recent years, thus increasing the demand for\x01",
            "financial advisers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You wouldn't want an amateur handling\x01",
            "your mira, would you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_28C0")


    ChrTalk(
        0xC,
        (
            "Did you all know this? Crossbell has been a\x01",
            "bastion for commerce and the securities industry\x01",
            "ever since its founding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm a stockbroker at a securities and exchange\x01",
            "company, actually. We deal in stocks and bonds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "A myriad of financial tools have been developed\x01",
            "in recent years, thus increasing the demand for\x01",
            "financial advisers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2A1B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_11C6 end

    def Function_9_2A23(): pass

    label("Function_9_2A23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2B49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A8A")

    ChrTalk(
        0x9,
        "There's no way my husband would ever...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "He's such an honest man...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B44")

    label("loc_2A8A")


    ChrTalk(
        0x9,
        "My husband hasn't come back home yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Excuse me... D-Do you think my husband\x01",
            "has run away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's no way my husband would ever...\x01",
            "I'm worried sick right now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2B44")

    Jump("loc_33C9")

    label("loc_2B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C03")

    ChrTalk(
        0x9,
        "M-My husband still hasn't come home yet...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Could you please find him for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FOf course, ma'am. The police are already\x01",
            "hard at work trying to find him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C9")

    label("loc_2C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2D88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C9B")

    ChrTalk(
        0x9,
        (
            "Sophia's holding a cooking class at\x01",
            "her house tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll be sure to engage in a bit of\x01",
            "gossip time with the girls.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D83")

    label("loc_2C9B")


    ChrTalk(
        0x9,
        (
            "Sunita's about the same age as the\x01",
            "Hayworth family's son, Colin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sure there'll be plenty of fun\x01",
            "topics to gossip about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The weekly cooking class is being held tomorrow.\x01",
            "I can't wait to talk with all the girls.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2D83")

    Jump("loc_33C9")

    label("loc_2D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2DFD")

    ChrTalk(
        0x9,
        "My husband seems a little down these days...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I hope nothing bad has happened to him at work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_33C9")

    label("loc_2DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2E9C")

    ChrTalk(
        0xFE,
        (
            "Sunita's been playing with that\x01",
            "adorable little kitten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm admittedly a little jealous.\x01",
            "I wonder if they'd let me join in on the fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C9")

    label("loc_2E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F32")

    ChrTalk(
        0x9,
        (
            "I don't exactly understand what Bond\x01",
            "does for work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think everything will be okay\x01",
            "as long as he follows his heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3042")

    label("loc_2F32")


    ChrTalk(
        0x9,
        (
            "My husband said his job is giving him the choice\x01",
            "to transfer to the Empire and leave us behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Naturally, I told him that it's ultimately\x01",
            "his decision to make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's HIS career, after all. I think everything\x01",
            "will be okay as long as he follows his heart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3042")

    Jump("loc_33C9")

    label("loc_3047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_322D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3189")

    ChrTalk(
        0xFE,
        (
            "Sunita started taking care of the cutest\x01",
            "little kitten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Supposedly my husband was already\x01",
            "aware of the situation, but dear me,\x01",
            "it was quite the shock.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Sunita and her little kitten are just the\x01",
            "two most adorable peas in a pod.\x01",
            "I'm admittedly a little jealous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3228")

    label("loc_3189")


    ChrTalk(
        0xFE,
        (
            "Oh, no! I promised Sophia that I'd\x01",
            "show up to her cooking class today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd better stop fawning over the kitten\x01",
            "and hurry up, otherwise I'll be late.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3228")

    Jump("loc_33C9")

    label("loc_322D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_323B")
    Jump("loc_33C9")

    label("loc_323B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_32EB")

    ChrTalk(
        0x9,
        (
            "Bond still works himself to the bone even when\x01",
            "he's at home. What a strange husband I have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Or does perhaps every man in Zemuria\x01",
            "behave the same way?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C9")

    label("loc_32EB")


    ChrTalk(
        0xFE,
        (
            "Even when my husband's at home, all\x01",
            "he does is work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He enjoys reading to our daughter, at\x01",
            "the very least. Though, I still wish he'd\x01",
            "rest a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bond must really love his job.\x01",
            "*sigh* Oh, that man...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_33C9")

    TalkEnd(0xFE)
    Return()

    # Function_9_2A23 end

    def Function_10_33CD(): pass

    label("Function_10_33CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_33FD")

    ChrTalk(
        0xA,
        (
            "*hic* *sob*\x01",
            "...Fatheeeer!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433C")

    label("loc_33FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_35B0")
    OP_63(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Father has... F-Father has\x01",
            "disappeared!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*hic* *sob*\x01",
            "W-Waaaaaaaaaaaaah!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_354E")

    ChrTalk(
        0x103,
        (
            "#0200FI am certain this was the family that\x01",
            "adopted the stray kitten from before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108FThe husband looked like he was\x01",
            "such a kind man, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FYeah... We should try to hurry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_35A8")

    label("loc_354E")


    ChrTalk(
        0x103,
        "#0200FHe has a daughter, so how could he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FYeah... We should try to hurry.\x02",
    )

    CloseMessageWindow()

    label("loc_35A8")

    SetScenarioFlags(0x0, 2)
    Jump("loc_433C")

    label("loc_35B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_364B")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "Hey, Marie... What do you think could\x01",
            "have happened to Father?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Do you know anything about it, Marie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1SFunyan...?#3S\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_433C")

    label("loc_364B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3937")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_END)), "loc_3785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_36EC")

    ChrTalk(
        0xA,
        (
            "Mother has a cooking class to\x01",
            "attend today... I feel like she's\x01",
            "always too laid-back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I-I need to get my act together!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3780")

    label("loc_36EC")


    ChrTalk(
        0xA,
        (
            "F-Father must be exhausted from\x01",
            "working all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm sure that's why he's acting weird...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I need to do something to cheer him up!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3780")

    Jump("loc_3932")

    label("loc_3785")

    OP_64(0xA)

    ChrTalk(
        0xA,
        "Father...\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FHmm? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    ChrTalk(
        0xA,
        "I-It's nothing.\x02",
    )

    CloseMessageWindow()
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "It's just that...uhm...\x01",
            "For the last little while, Father's been acting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hahaha! You goddamned morons!\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x13B, 0x2EE)

    ChrTalk(
        0xA,
        "...What has happened to Father?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Hmm? He seems really off to me\x01",
            "for some reason...)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0xCD, 0)

    label("loc_3932")

    Jump("loc_433C")

    label("loc_3937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_39A6")
    OP_93(0xFE, 0x13B, 0x0)

    ChrTalk(
        0xFE,
        "What has happened to Father?\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        "I-It's nothing.\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x13B, 0x0)
    Jump("loc_433C")

    label("loc_39A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3A24")

    ChrTalk(
        0xFE,
        "Father said he'd play with me today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I guess he's too busy with work\x01",
            "to pay attention to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433C")

    label("loc_3A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3AAE")

    ChrTalk(
        0xA,
        (
            "Bad girl, Marie! You have to take a\x01",
            "bath today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm going to scrub the heck outta you\x01",
            "and make you squeaky clean!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433C")

    label("loc_3AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3B57")
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    ChrTalk(
        0xA,
        "Oh...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0xA, 0xB, 750)
    Sleep(750)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "Ahem! You have to show better manners\x01",
            "in front of guests, Marie!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BDF")

    label("loc_3B57")


    ChrTalk(
        0xA,
        "Hey, Marie! I brought you some milk!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's first-class milk straight from\x01",
            "Armorica Village!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I bet it's super tasty! ♪\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3BDF")

    Jump("loc_433C")

    label("loc_3BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3C6F")

    ChrTalk(
        0xA,
        (
            "Hmm... I wonder what Mother and\x01",
            "Father were talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I-I feel like it's something I wasn't\x01",
            "supposed to hear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433C")

    label("loc_3C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3DAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3CDD")

    ChrTalk(
        0xA,
        "Marie's a very spoiled kitty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't help but pet her every time\x01",
            "I see her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA9")

    label("loc_3CDD")

    OP_4B(0xB, 0xFF)
    Sound(823, 0, 100, 0)

    ChrTalk(
        0xA,
        "Eek! Marie, that tickles!\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    ChrTalk(
        0xA,
        (
            "I-I bet Marie's the most spoiled kitty\x01",
            "to ever live!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Marie gets lonely if I don't pet her\x01",
            "every once in a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_3DA9")

    Jump("loc_433C")

    label("loc_3DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3F58")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E74")
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Marie! Marie!\x01",
            "Come and play with me!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 750)
    Sleep(750)

    ChrTalk(
        0xA,
        "Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A-Ahem...\x01",
            "Marie's full of energy today.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x2EE)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_3EB5")

    label("loc_3E74")


    ChrTalk(
        0xA,
        "A-Ahem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What a relief! Marie's full of energy\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB5")

    Jump("loc_3F53")

    label("loc_3EBA")


    ChrTalk(
        0xA,
        "Yaaay! Marie's back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A bracer girl found her and brought her\x01",
            "back to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    TurnDirection(0xA, 0xB, 750)
    Sleep(750)

    ChrTalk(
        0xA,
        (
            "Marie! Marie!\x01",
            "Come and play with me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F53")

    Jump("loc_433C")

    label("loc_3F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4065")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3FC4")

    ChrTalk(
        0xA,
        "I'll take good care of Marie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ahem! Isn't she such a playful\x01",
            "little kitty?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4060")

    label("loc_3FC4")


    ChrTalk(
        0xA,
        (
            "Marie! Marie!\x01",
            "Look this way! ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 500)
    Sleep(500)

    ChrTalk(
        0xA,
        "A-Ahem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Thank you for your help today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "O-Only for that, though!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_4060")

    Jump("loc_433C")

    label("loc_4065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4101")

    ChrTalk(
        0xA,
        (
            "Apparently, Father's in a lot of trouble because\x01",
            "some of his important papers were ruined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I-I wouldn't know anything about that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_433C")

    label("loc_4101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_422B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4166")

    ChrTalk(
        0xA,
        (
            "He wasn't even able to play\x01",
            "with me today...\x01",
            "Don't bother him right now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4226")

    label("loc_4166")


    ChrTalk(
        0xA,
        (
            "I'm sure Father's busy doing some kind of\x01",
            "super hard work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After all, he's an important person\x01",
            "called a 'stockbroker.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't annoy him, otherwise I'll\x01",
            "be mad at you forever!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4226")

    Jump("loc_433C")

    label("loc_422B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_42AA")

    ChrTalk(
        0xA,
        "Oh. Do you people need something from me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "How rude of you to talk to a lady you don't\x01",
            "even know! Hmph!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433C")

    label("loc_42AA")


    ChrTalk(
        0xA,
        "I folded my pajamas and put them in the drawer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't rely on Mother very much, so I have\x01",
            "to pick up her share of the work.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_433C")

    TalkEnd(0xFE)
    Return()

    # Function_10_33CD end

    def Function_11_4340(): pass

    label("Function_11_4340")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4362")
    Call(0, 15)
    Return()

    label("loc_4362")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43F6")
    Jump("loc_4440")

    label("loc_43F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4416")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4440")

    label("loc_4416")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4436")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4440")

    label("loc_4436")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4440")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_44E5")

    ChrTalk(
        0xD,
        "I-I don't know anything!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmph! I'm busy reading a book with\x01",
            "F-Father, so could you please go away?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452C")

    label("loc_44E5")


    ChrTalk(
        0xD,
        "I'm having Father read me a book.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Could you please go away?!\x02",
    )

    CloseMessageWindow()

    label("loc_452C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_11_4340 end

    def Function_12_4538(): pass

    label("Function_12_4538")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_455F")

    ChrTalk(
        0xB,
        "#1SFunyaan...#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_455F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4586")

    ChrTalk(
        0xB,
        "#1SFunyaanyaa...#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_4586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_45AA")

    ChrTalk(
        0xB,
        "#1SFunyan...?#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_45AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_45CD")

    ChrTalk(
        0xB,
        "#1SFunyaa...#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_45CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_45F0")

    ChrTalk(
        0xB,
        "#1SFunyan...#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_45F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4613")

    ChrTalk(
        0xB,
        "#1SNya-o...?#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_4613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4635")

    ChrTalk(
        0xB,
        "#1SNya-o...#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_4635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4658")

    ChrTalk(
        0xB,
        "#1SNyaon...?#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_4658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4679")

    ChrTalk(
        0xB,
        "#1SNya-...#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_4679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_469B")

    ChrTalk(
        0xB,
        "#1SNya-o...#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_469B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_46D9")
    OP_63(0xB, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0xB,
        "#1SFunyaaan...!#3S\x02",
    )

    CloseMessageWindow()
    OP_64(0xB)
    Jump("loc_478A")

    label("loc_46D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4702")

    ChrTalk(
        0xB,
        "#1SNnyannyan... ♪#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_4702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4724")

    ChrTalk(
        0xB,
        "#1SNya-o...#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_4724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_474D")

    ChrTalk(
        0xB,
        "#1SNnyannyan... ♪#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_474D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4772")

    ChrTalk(
        0xB,
        "#1SNyaon... ♪#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_478A")

    label("loc_4772")


    ChrTalk(
        0xB,
        "#1SFunyaa... ♪#3S\x02",
    )

    CloseMessageWindow()

    label("loc_478A")

    TalkEnd(0xFE)
    Return()

    # Function_12_4538 end

    def Function_13_478E(): pass

    label("Function_13_478E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4A0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4823")

    ChrTalk(
        0xE,
        (
            "#3701FWhere could her husband have\x01",
            "disappeared to?\x02\x03",
            "He wasn't the kind of man that would\x01",
            "easily abandon his family...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A05")

    label("loc_4823")


    ChrTalk(
        0xE,
        (
            "#3701FOh, the Special Support Section...\x02\x03",
            "Creil and sweet little Sunita have\x01",
            "calmed down a little bit. I think\x01",
            "they're still terribly worried, though...\x02\x03",
            "#3708FNot that I can blame them one bit.\x01",
            "After all, I was barely able to hold myself\x01",
            "together when Colin went missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI'm sorry, Mrs. Hayworth, but could you\x01",
            "stay by their side a little longer?\x02\x03",
            "I assure you, the CPD is doing everything\x01",
            "they can to locate Bond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3700FOf course. Leave them in my hands.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4A05")

    Jump("loc_4D31")

    label("loc_4A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4D31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4AA6")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xE,
        (
            "#3700FI know it's hard, Creil, but you have\x01",
            "to try and calm down a little bit.\x02\x03",
            "I'm sure your husband is well and fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_4D31")

    label("loc_4AA6")


    ChrTalk(
        0xE,
        (
            "#3708FCreil's a good friend of mine, so I've met her\x01",
            "husband on numerous occasions.\x02\x03",
            "Please don't tell me that he's been involved\x01",
            "in some sort of accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FPlease try to not fill their heads with any more\x01",
            "worries than there already are, Mrs. Hayworth.\x02\x03",
            "#0100FWe should endeavor to keep\x01",
            "his family as calm as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#3705FY-You're right. My apologies,\x01",
            "it wasn't intentional...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FIt's not worth worryin' your head over the\x01",
            "endless possibilities in times like this.\x02\x03",
            "#0300FProbably a swell idea to pour the\x01",
            "upset lady some tea, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3700FY-Yes. You're right.\x01",
            "I'll do just that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x9, 750)
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 3)

    label("loc_4D31")

    TalkEnd(0xFE)
    Return()

    # Function_13_478E end

    def Function_14_4D35(): pass

    label("Function_14_4D35")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_68(1000, 1400, -3250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 1500, 50, -6500, 360)
    SetChrPos(0x102, 500, 50, -6750, 360)
    SetChrPos(0x103, 1500, 50, -7750, 360)
    SetChrPos(0x104, 500, 50, -8000, 360)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4DEC():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DEC)

    def lambda_4E06():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E06)
    Sleep(50)

    def lambda_4E1A():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E1A)

    def lambda_4E34():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E34)
    Sleep(50)

    def lambda_4E48():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4E48)

    def lambda_4E62():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4E62)
    Sleep(50)

    def lambda_4E76():
        OP_97(0xFE, 0x0, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4E76)

    def lambda_4E90():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4E90)
    SetCameraDistance(21000, 2500)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#0001F#11PAccording to the First Division's\x01",
            "data, this should be the house...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#0205FI see a familiar face.\x02",
    )

    CloseMessageWindow()
    OP_68(-1750, 1400, 3120, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "E-Excuse me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I... What should I do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3701FI know it's hard, Creil, but you\x01",
            "have to calm down.\x02\x03",
            "As things stand, we really need\x01",
            "to go find some help.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1750, 1400, 2120, 3000)

    def lambda_504F():
        OP_95(0x101, -750, 0, 1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_504F)
    Sleep(50)

    def lambda_506C():
        OP_95(0x102, -1750, 0, 1250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_506C)
    Sleep(50)

    def lambda_5089():
        OP_95(0x103, -750, 0, 250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5089)
    Sleep(50)

    def lambda_50A6():
        OP_95(0x104, -1750, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50A6)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x0)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x0)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x0)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0005FIs that you, Mrs. Hayworth?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_5139():
        TurnDirection(0xE, 0x101, 350)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5139)
    Sleep(50)

    def lambda_5149():
        TurnDirection(0x9, 0x101, 350)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5149)
    Sleep(1000)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0xE,
        (
            "#3705FOh, the Special Support Section!\x02\x03",
            "#3700FOh, thank Aidios you're here.\x01",
            "You see, something dreadful has happened,\x01",
            "and we were about to seek some help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FIs it regarding the owner of this house?\x01",
            "I believe he's a stockbroker, if I'm not\x01",
            "mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PY-Yes, you're right. He is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWhen I woke up this morning...my husband\x01",
            "was nowhere to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI-I tried looking around the neighborhood with\x01",
            "Sophia, but we had no luck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYou must be really worried right now...\x02\x03",
            "#0013FI'm sorry to ask this, but has your husband\x01",
            "been acting odd recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHmm... Now that you mention it, he was.\x01",
            "My daughter noticed it some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FUgh. Figures.\x02\x03",
            "#0301FWhy'd he have to go poof in the middle of the night?\x01",
            "Gonna be a real pain in the ass to find witnesses.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54F2")

    ChrTalk(
        0x101,
        (
            "#0008FYeah, looks like it. At any rate, let's add\x01",
            "him to the list of missing people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_552B")

    label("loc_54F2")


    ChrTalk(
        0x101,
        "#0008FYeah, we've yet to come up with the method...\x02",
    )

    CloseMessageWindow()

    label("loc_552B")

    TurnDirection(0x101, 0xE, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0000FYou seem to be well acquainted with this\x01",
            "family, Mrs. Hayworth.\x02\x03",
            "#0003FThe CPD is conducting a search for Bond,\x01",
            "but it may take some time for us to find him.\x02\x03",
            "#0001FWould you be willing to stay with the family\x01",
            "for a little while longer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3700FYes, gladly.\x02\x03",
            "My husband should also be back from\x01",
            "work soon anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0004FThank you. We'll leave them to you, then.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x9, 0xE, 0)
    TurnDirection(0xE, 0x9, 0)
    SetChrPos(0x0, -750, 0, 1550, 360)
    SetScenarioFlags(0xC8, 2)
    OP_29(0x4C, 0x1, 0xA)
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_14_4D35 end

    def Function_15_56E5(): pass

    label("Function_15_56E5")

    EventBegin(0x0)
    Fade(500)
    OP_68(6990, 5400, 8640, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(250, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, 6520, 4000, 8470, 135)
    SetChrPos(0x102, 5180, 4000, 9390, 135)
    SetChrPos(0x103, 4850, 4000, 8420, 135)
    SetChrPos(0x104, 6210, 4000, 9940, 135)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0000F(Looks like a child lives in this home...)\x02\x03",
            "Excuse me, sir. Do you have a moment?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)
    Sleep(300)

    ChrTalk(
        0xC,
        "#11PHmm? Could I help you with something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FWe're with the CPD, and we're\x01",
            "conducting a small investigation.\x02\x03",
            "Do you happen to own a cat,\x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PNo, we don't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PSunita, sweetheart. Do you know anything\x01",
            "about this?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x2)

    ChrTalk(
        0xD,
        "#6PI-I don't know anything!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#12PHmph! I'm busy reading a book\x01",
            "with F-Father, so could you\x01",
            "please go away?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FSwing and a miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI would recommend we extend our\x01",
            "search in the neighborhood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FYou're right. There's a chance we overlooked\x01",
            "something, so one more round wouldn't hurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 5580, 4000, 8480, 180)
    SetChrSubChip(0xD, 0x2)
    OP_29(0x8, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_15_56E5 end

    def Function_16_5A2D(): pass

    label("Function_16_5A2D")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(-700, 1400, 560, 0)
    MoveCamera(46, 28, 0, 0)
    OP_6E(190, 0)
    SetCameraDistance(43500, 0)
    SetChrPos(0x101, -1260, 0, -1250, 0)
    SetChrPos(0x102, -1260, 0, -2800, 0)
    SetChrPos(0x103, -100, 0, -1250, 0)
    SetChrPos(0x104, -100, 0, -2800, 0)
    SetChrPos(0x8, -120, 0, 2930, 180)
    SetChrPos(0xA, -410, 0, 70, 0)
    SetChrPos(0xB, -1270, 0, 370, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xA, 0x40)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#5PYou've been wanting to keep a kitten?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POh... So this is what it's been all about!\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xA,
        "#12PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI've been worried about Sunita's\x01",
            "odd behavior this last little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFor example, she kept going out on her own\x01",
            "without telling us what she was doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe cat may have torn up my documents,\x01",
            "but I suppose they weren't THAT important...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PSo...you aren't mad at Marie, then, Father?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PCan we please keep Marie, then?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHaha. Yes. Of course, sweetheart.\x01",
            "I'm happy to say we've added a new\x01",
            "member to our family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, Sunita... It's your responsibility\x01",
            "to properly take care of Marie. Understood?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PO-Of course! Thank you so much, Father!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xA, 2, 0, 17)
    Sleep(600)
    OP_95(0xA, -210, 0, 2170, 6000, 0x0)
    Sound(804, 0, 100, 0)
    OP_A6(0x8, 0x0, 0x1E, 0x1F4, 0x9C4)
    OP_95(0xB, -1010, 0, 1980, 1000, 0x0)
    OP_93(0xB, 0x2D, 0x12C)
    Sleep(800)
    OP_68(-550, 1400, -890, 2500)
    Sleep(2500)

    ChrTalk(
        0x104,
        "#11P#0300FA happy ending to this story, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FI'm happy for her. She seems\x01",
            "to have a very loving father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FAgreed... I can ascertain the kitten\x01",
            "will also be pleased.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#11P#0200FHowever, Lloyd... It was unnecessary of\x01",
            "the police to escalate the issue as far\x01",
            "as we did, correct?\x02\x03",
            "#0203FI had you confused for a bracer, rather\x01",
            "than a detective.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x190)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#0012FHaha. Guess you're right. It's our duty to help\x01",
            "people, though.\x02\x03",
            "#0000FWe call ourselves the 'Special Support Section,'\x01",
            "don't we? I'd say these kinds of tasks are right\x01",
            "up our alley.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_60B6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_60B6)

    def lambda_60C3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_60C3)

    def lambda_60D0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_60D0)

    def lambda_60DD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_60DD)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0000F#6PAnyway, that's a wrap.\x01",
            "Let's head out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0304F#11PSounds like a plan, my man.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Search for the Kitten's Owner]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    EndChrThread(0xA, 0x2)
    SetChrPos(0x0, -200, 0, -1320, 180)
    SetChrPos(0xA, 5250, 4000, 8250, 180)
    SetChrPos(0xB, 5180, 4000, 5560, 315)
    SetChrPos(0xC, 40, 4150, 18170, 90)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x40)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_29(0x8, 0x4, 0x10)
    OP_29(0x8, 0x1, 0x9)
    OP_C7(0x1, 0x1000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_5A2D end

    def Function_17_6230(): pass

    label("Function_17_6230")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6255")
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_17_6230")

    label("loc_6255")

    Return()

    # Function_17_6230 end

    SaveToFile()

Try(main)
