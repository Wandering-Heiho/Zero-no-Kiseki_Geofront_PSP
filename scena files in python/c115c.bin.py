from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c115c.bin",                # FileName
        "c115c",                    # MapName
        "c115c",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 1, 0, 2],
    )

    BuildStringList((
        "c115c",                  # 0
        "Receptionist Rebecca",   # 1
        "Receptionist Fran",      # 2
        "Receptionist Fran",      # 3
        "Inspector Donovan",      # 4
        "Detective Raymond",      # 5
        "Officer",                # 6
        "Chief Jolich",           # 7
        "Detective Emma",         # 8
        "Suspect",                # 9
        "Officer",                # 10
        "Chief Sergei",           # 11
        "Young Man",              # 12
        "Kilika",                 # 13
        "Counterfeit Dealer",     # 14
        "Detective Raymond",      # 15
        "Officer Kate",           # 16
    ))

    AddCharChip((
        "chr/ch30400.itc",                   # 00
        "chr/ch06900.itc",                   # 01
        "chr/ch06902.itc",                   # 02
        "chr/ch30100.itc",                   # 03
        "chr/ch30100.itc",                   # 04
        "chr/ch21000.itc",                   # 05
        "chr/ch30000.itc",                   # 06
        "chr/ch30300.itc",                   # 07
        "chr/ch30200.itc",                   # 08
        "chr/ch30500.itc",                   # 09
        "chr/ch30202.itc",                   # 0A
        "chr/ch24102.itc",                   # 0B
        "chr/ch30600.itc",                   # 0C
        "chr/ch02502.itc",                   # 0D
        "chr/ch23602.itc",                   # 0E
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

    DeclNpc(-100,    0,       15399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(3000,    0,       15930,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-9600,   100,     18239,   270,  469,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-125379, 0,       19520,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-125080, 150,     16309,   90,   469,  0x0, 0,   13,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(-122440, 150,     16180,   270,  469,  0x0, 0,   14,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-122300, 150,     16500,   270,  469,  0x0, 0,   11,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-125080, 150,     16500,   90,   469,  0x0, 0,   10,  0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-59229,  29,      21360,   270,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)

    DeclEvent(0x0000, 0, 31,  -12.699999809265137,   19.8700008392334,      -0.5,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.233333587646484,     -9.9350004196167,      0.1428571492433548,    1.0])

    DeclActor(-100,    0,       14400,   1100,    -100,    1500,    15400,   0x007E, 0,  3,  0x0000)
    DeclActor(2770,    0,       14280,   1000,    3000,    1500,    15930,   0x007E, 0,  7,  0x0000)
    DeclActor(-34480,  0,       20000,   1000,    -34480,  1000,    20000,   0x007C, 0,  18, 0x0000)
    DeclActor(-9850,   0,       16000,   1000,    -9850,   1500,    16000,   0x007C, 0,  32, 0x0000)
    DeclActor(-9850,   0,       13750,   1000,    -9850,   1500,    13750,   0x007C, 0,  32, 0x0000)

    ScpFunction((
        "Function_0_464",          # 00, 0
        "Function_1_51C",          # 01, 1
        "Function_2_75D",          # 02, 2
        "Function_3_7C9",          # 03, 3
        "Function_4_7CD",          # 04, 4
        "Function_5_DF1",          # 05, 5
        "Function_6_1832",         # 06, 6
        "Function_7_1936",         # 07, 7
        "Function_8_193A",         # 08, 8
        "Function_9_26E3",         # 09, 9
        "Function_10_2A53",        # 0A, 10
        "Function_11_2BE7",        # 0B, 11
        "Function_12_2F61",        # 0C, 12
        "Function_13_3094",        # 0D, 13
        "Function_14_341F",        # 0E, 14
        "Function_15_3561",        # 0F, 15
        "Function_16_363F",        # 10, 16
        "Function_17_389B",        # 11, 17
        "Function_18_3B67",        # 12, 18
        "Function_19_3BF2",        # 13, 19
        "Function_20_3E27",        # 14, 20
        "Function_21_4125",        # 15, 21
        "Function_22_4247",        # 16, 22
        "Function_23_4304",        # 17, 23
        "Function_24_58B7",        # 18, 24
        "Function_25_5B2C",        # 19, 25
        "Function_26_69FB",        # 1A, 26
        "Function_27_7AF5",        # 1B, 27
        "Function_28_7B89",        # 1C, 28
        "Function_29_7BF8",        # 1D, 29
        "Function_30_9D83",        # 1E, 30
        "Function_31_AEEE",        # 1F, 31
        "Function_32_AF9C",        # 20, 32
    ))


    def Function_0_464(): pass

    label("Function_0_464")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_4A4"),
        (1, "loc_4B0"),
        (2, "loc_4BC"),
        (3, "loc_4C8"),
        (4, "loc_4D4"),
        (5, "loc_4E0"),
        (6, "loc_4EC"),
        (SWITCH_DEFAULT, "loc_4F8"),
    )


    label("loc_4A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_504")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_51B")

    Return()

    # Function_0_464 end

    def Function_1_51C(): pass

    label("Function_1_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_52B")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 29)

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_57B")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -12850, 0, 7690, 90)
    SetChrPos(0xC, -11260, 0, 7690, 270)
    SetChrPos(0xE, -11040, 0, 13810, 90)
    Jump("loc_75C")

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_598")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_598")

    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0xB, -10370, 0, 7070, 270)
    SetChrPos(0x17, -11980, 0, 8189, 135)
    SetChrPos(0xE, -11930, 0, 7110, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -58050, 0, 15900, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_75C")

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_637")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -58050, 0, 15900, 90)
    Jump("loc_75C")

    label("loc_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6E0")
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_67B")
    SetChrPos(0xB, -124850, 0, 14920, 45)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_6B9")

    label("loc_67B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_697")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_6B9")

    label("loc_697")

    SetChrPos(0xB, -57730, 0, 16309, 180)
    SetChrPos(0xC, -57730, 0, 14480, 0)

    label("loc_6B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6DB")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -11040, 0, 13810, 90)

    label("loc_6DB")

    Jump("loc_75C")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_75C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x10, -12850, 0, 7690, 90)
    SetChrPos(0xD, -11260, 0, 7690, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -11040, 0, 13810, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_757")
    SetChrPos(0xE, -58050, 0, 15900, 90)
    Jump("loc_75C")

    label("loc_757")

    SetChrFlags(0xE, 0x80)

    label("loc_75C")

    Return()

    # Function_1_51C end

    def Function_2_75D(): pass

    label("Function_2_75D")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_779")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    Jump("loc_7C8")

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_787")
    Jump("loc_7C8")

    label("loc_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7A3")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_65(0x1, 0x1)
    Jump("loc_7C8")

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7B1")
    Jump("loc_7C8")

    label("loc_7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7BF")
    Jump("loc_7C8")

    label("loc_7BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7C8")

    label("loc_7C8")

    Return()

    # Function_2_75D end

    def Function_3_7C9(): pass

    label("Function_3_7C9")

    Call(0, 4)
    Return()

    # Function_3_7C9 end

    def Function_4_7CD(): pass

    label("Function_4_7CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_811")
    TalkBegin(0x8)
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80C")
    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0x8)
    Call(0, 25)
    Return()

    label("loc_80C")

    Jump("loc_832")

    label("loc_811")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_832")
    Call(0, 23)
    Return()

    label("loc_832")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D38")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88B")

    ChrTalk(
        0x8,
        "Thank you so much for handling the extermination.\x02",
    )

    CloseMessageWindow()

    label("loc_88B")


    ChrTalk(
        0x8,
        (
            "Oh, that's right. Did you hear the news? The CPD\x01",
            "is currently conducting an information survey about\x01",
            "local monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FReally? What exactly does that entail?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, it starts with your Combat Notebook's monster\x01",
            "entries. You've been keeping it up-to-date, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once you defeat a monster, officers are supposed\x01",
            "to record their information in their notebooks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The survey's simple. After you've recorded\x01",
            "enough monster data, come show it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That information will be conglomerated and become\x01",
            "the foundation for our new security procedures. It's\x01",
            "quite the smart idea, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B68")

    ChrTalk(
        0x102,
        (
            "#0100FI can't disagree. I'm glad to see that we're thinking\x01",
            "things out before accidents happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C67")

    label("loc_B68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF4")

    ChrTalk(
        0x103,
        (
            "#0200FIndeed. The amount of foresight demonstrated\x01",
            "by the department is admirable. Not to mention,\x01",
            "unprecedented.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C67")

    label("loc_BF4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C67")

    ChrTalk(
        0x104,
        (
            "#0300FWell, look at us, takin' action for a change. That\x01",
            "in itself is pretty damn reassuring.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C67")


    ChrTalk(
        0x8,
        "Of course. After all, this is to protect the citizenry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, I nearly forgot! Whenever you supply me with\x01",
            "information, I'll give you a small bonus, too.\x01",
            "Make sure to stop by when you can, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 2)
    SetScenarioFlags(0x1, 3)

    label("loc_D38")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DED")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                      # 0
            "Show Combat Notebook\x01",      # 1
            "Leave\x01",                     # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 4)
    Call(0, 30)
    Jump("loc_DE8")

    label("loc_DB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DCC")
    Jump("loc_DE8")

    label("loc_DCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_DE8")

    Jump("loc_D42")

    label("loc_DED")

    TalkEnd(0x8)
    Return()

    # Function_4_7CD end

    def Function_5_DF1(): pass

    label("Function_5_DF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F15")

    ChrTalk(
        0x8,
        "Keep it up, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Let me know once you've finished ticketing\x01",
            "those illegally parked cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll contact the Metropolitan Division upon\x01",
            "your return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FSure, sounds good. Thanks for not making\x01",
            "us have to chase after them ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1831")

    label("loc_F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1036")

    ChrTalk(
        0x8,
        (
            "Once you have filled out a certain amount of entries\x01",
            "in your Combat Notebook, please bring it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll be using the information you gather to put\x01",
            "more effective safety procedures in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You'll even get a small bonus, so please stop by\x01",
            "whenever you can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1831")

    label("loc_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10CB")

    ChrTalk(
        0x8,
        "Keep up the good work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys must be extra busy, no thanks to\x01",
            "Anniversary Festival's tendency to attract\x01",
            "crime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1831")

    label("loc_10CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1188")

    ChrTalk(
        0x8,
        (
            "The closing ceremony is slated to begin after\x01",
            "the cathedral bell has tolled in the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's about time for everyone to gather together\x01",
            "and help with that, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1831")

    label("loc_1188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_1305")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126C")

    ChrTalk(
        0x8,
        (
            "It just isn't an Anniversary Festival without\x01",
            "children getting separated from their parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think around twenty of them got lost this year...\x01",
            "I hope they aren't traumatized by the ordeal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1300")

    label("loc_126C")


    ChrTalk(
        0x8,
        (
            "This goes without saying, but each and\x01",
            "every single one of their parents must be\x01",
            "worried sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It's your sworn duty to help them reunite.\x02",
    )

    CloseMessageWindow()

    label("loc_1300")

    Jump("loc_1831")

    label("loc_1305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1447")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BF")

    ChrTalk(
        0x8,
        (
            "Phew... That was an endless torrent of people.\x01",
            "I'm sure glad that's over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Poor Fran looks utterly exhausted.\x01",
            "I think I'll send her home early today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1442")

    label("loc_13BF")


    ChrTalk(
        0x8,
        (
            "Are you looking for Fran? She's over by\x01",
            "the vending machines, taking a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Why not strike up a conversation with her?\x02",
    )

    CloseMessageWindow()

    label("loc_1442")

    Jump("loc_1831")

    label("loc_1447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1584")

    ChrTalk(
        0x8,
        (
            "Are we all ready for the parade? It'll be\x01",
            "traversing the city today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure we'll be bombarded with dozens of\x01",
            "questions about it. Not to mention, we'll\x01",
            "have to guide plenty of confused tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I know the workload is going to be insane,\x01",
            "but it's okay. We'll get through this together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1831")

    label("loc_1584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_17D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D2")

    ChrTalk(
        0x8,
        (
            "There's a symposium being held at\x01",
            "City Hall later today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't think the average person's going to\x01",
            "be interested in it, though. Apparently, scholars\x01",
            "from across the continent will be in attendance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The mayor, the IBC CEO, and Mr. Grimwood\x01",
            "will be there participating on Crossbell's behalf.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17D1")

    label("loc_16D2")


    ChrTalk(
        0x8,
        (
            "The CPD will be in charge of the security detail,\x01",
            "but they'll be receiving assistance from none\x01",
            "other than Arios MacLaine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Upper management isn't exactly thrilled about\x01",
            "the idea, but we have to keep up appearances\x01",
            "in front of the other nations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D1")

    Jump("loc_1831")

    label("loc_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1831")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17F3")
    Call(0, 6)
    Jump("loc_1831")

    label("loc_17F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_END)), "loc_182E")
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1829")
    FadeToDark(1000, 0, -1)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    TalkEnd(0x8)
    Return()

    label("loc_1829")

    Jump("loc_1831")

    label("loc_182E")

    Call(0, 6)

    label("loc_1831")

    Return()

    # Function_5_DF1 end

    def Function_6_1832(): pass

    label("Function_6_1832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18DA")

    ChrTalk(
        0x8,
        "Hello, SSS. How are you doing today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm not too surprised, but it's absurdly\x01",
            "crowded this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Good luck with your support requests.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1935")

    label("loc_18DA")


    ChrTalk(
        0x8,
        "It's absurdly crowded this year.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Good luck with your support requests, everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_1935")

    Return()

    # Function_6_1832 end

    def Function_7_1936(): pass

    label("Function_7_1936")

    Call(0, 8)
    Return()

    # Function_7_1936 end

    def Function_8_193A(): pass

    label("Function_8_193A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB8")

    ChrTalk(
        0x9,
        (
            "#1903FWe're at the homestretch! Just one more\x01",
            "day of the Anniversary Festival to go.\x02\x03",
            "#1900FKeep up the good work, guys.\x01",
            "We'll get through this together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha. Thanks for the support, Fran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(The most critical period of the festival\x01",
            "begins now...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(I don't want to get her involved,\x01",
            "so let's keep her in the dark.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C5D")

    label("loc_1AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAF")

    ChrTalk(
        0x9,
        (
            "#1905FOh, yeah. Chief Sergei's attending a meeting\x01",
            "somewhere here right now.\x02\x03",
            "#1900FDid you want to go see him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FNo, that's okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWe're almost there, Fran. Just one\x01",
            "last push to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1900FAh, yeah.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1C5D")

    label("loc_1BAF")


    ChrTalk(
        0x9,
        (
            "#1900FThe last day's been pretty crazy, but,\x01",
            "I should be able to manage. I think...\x02\x03",
            "#1906FPhew... I'm pretty glad I didn't have to\x01",
            "work during the opening day, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5D")

    Jump("loc_26DF")

    label("loc_1C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_1CFD")

    ChrTalk(
        0x9,
        (
            "#1900FOh, hey everyone.\x02\x03",
            "Your client, Mr. Hayworth just left.\x01",
            "He should be waiting for you near\x01",
            "the fountain outside.\x02\x03",
            "Good luck, guys!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_1CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1D0B")
    Jump("loc_26DF")

    label("loc_1D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1E53")
    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran is using a communication device.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#1903FYes, yes...\x02\x03",
            "#1901FThe parade will begin at 12PM today\x01",
            "in front of City Hall.\x02\x03",
            "It'll travel a full cycle around the city,\x01",
            "starting from the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4E")

    ChrTalk(
        0x101,
        (
            "#0000F(She looks pretty busy. We probably\x01",
            "shouldn't bother her.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4E")

    Jump("loc_26DF")

    label("loc_1E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2096")

    ChrTalk(
        0x9,
        (
            "#1900FHey, guys. Good work yesterday!\x02\x03",
            "Sounds like you played an active role\x01",
            "alongside the bracers in dealing with\x01",
            "the delinquents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FW-Weeelll, I'm not sure I'd call it\x01",
            "an 'active role.'\x02\x03",
            "#0006FIn retrospect, I feel like we may have shirked\x01",
            "our duties as police officers a little too much.\x01",
            "It felt like we were kinda just playing around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FIt all worked out in the end, so what's the harm?\x02\x03",
            "Anyway, I'm pretty sore from all\x01",
            "that running around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0111FServes you right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1909FHehehe.\x01",
            "Seriously, though. Good job, guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2173")

    label("loc_2096")


    ChrTalk(
        0x9,
        (
            "#1900FRebecca and I have been busy as heck, too.\x02\x03",
            "They've got that symposium going on today,\x01",
            "but we're getting flooded with questions about\x01",
            "tomorrow's parade.\x02\x03",
            "#1906F*sigh*\x01",
            "Oh, boy. Tomorrow's going to be a toughie.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2173")

    Jump("loc_26DF")

    label("loc_2178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_221E")

    ChrTalk(
        0x9,
        (
            "#1900FHey, everyone. Those darn delinquents\x01",
            "are causing a ruckus in the harbor.\x02\x03",
            "I know it's pain to deal with them,\x01",
            "but can you get them to stop?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_221E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2613")

    ChrTalk(
        0x9,
        (
            "#1900FHi, everyone!\x02\x03",
            "#1909FHeehee. I had a much-needed day off yesterday.\x02\x03",
            "It's been a while since I got to spend some\x01",
            "quality time with Noey.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_256A")

    ChrTalk(
        0x9,
        (
            "#1900FOh, yeah. Of course you'd know, Lloyd.\x01",
            "We went to that concert together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0009FHaha, yeah. I had a lot of fun,\x01",
            "so thanks for inviting me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0111FOh, what's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FOh, I know what you guys are talkin' about.\x01",
            "I was at the concert, too, actually.\x02\x03",
            "#0309FI was dancin' my ass off with some lovely\x01",
            "ladies, courtesy of the staff at St. Ursula\x01",
            "Medical College. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2477")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2477")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_249D")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_249D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C3")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_24C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24E9")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_24E9")

    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#0211FPlease refrain from excessively\x01",
            "indulging yourself, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha, sounds like we missed each other.\x02",
    )

    CloseMessageWindow()
    Jump("loc_260B")

    label("loc_256A")


    ChrTalk(
        0x101,
        (
            "#0000FHaha, sounds like you had fun.\x02\x03",
            "Anyway, I hope we continue to support\x01",
            "each other during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1900FYeah, sounds good to me!\x02",
    )

    CloseMessageWindow()

    label("loc_260B")

    SetScenarioFlags(0xB1, 3)
    Jump("loc_26DF")

    label("loc_2613")


    ChrTalk(
        0x9,
        (
            "#1900FDoesn't the Anniversary Festival make you\x01",
            "tackle a bunch of odd jobs?\x02\x03",
            "I'm sure you're going to have to deal with\x01",
            "a lot more support requests than usual,\x01",
            "but try not to go too crazy with them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26DF")

    TalkEnd(0x9)
    Return()

    # Function_8_193A end

    def Function_9_26E3(): pass

    label("Function_9_26E3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2777")
    Jump("loc_27C1")

    label("loc_2777")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2797")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27C1")

    label("loc_2797")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27B7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27C1")

    label("loc_27B7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27C1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295D")

    ChrTalk(
        0xFE,
        (
            "#1906F*sigh* I'm exhausted...\x02\x03",
            "#1900FHow many questions regarding the parade\x01",
            "have I answered already...?\x02\x03",
            "#1906FI can finally catch my breath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha. Good to see you alive and kicking, Fran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FYeah, these crowds are insane.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHow 'bout some juice, madame?\x01",
            "That'll perk you up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1906FOoh, you know how to please a lady!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A4B")

    label("loc_295D")


    ChrTalk(
        0xFE,
        (
            "#1903FOkay, break time's over.\x01",
            "It's time to bust my hump again!\x02\x03",
            "#1901FThere's still one day of the Anniversary\x01",
            "Festival to get through!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Noel and Fran may have polar opposite\x01",
            "personalities, but they're equally diligent.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_26E3 end

    def Function_10_2A53(): pass

    label("Function_10_2A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A61")
    Jump("loc_2BE6")

    label("loc_2A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2B44")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Don't you think they should add reinforcements\x01",
            "to the security detail for the closing ceremony?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's going to be a ton of people there.\x01",
            "Things could get real bad if they aren't\x01",
            "on their A game.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_2BE6")

    label("loc_2B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2B52")
    Jump("loc_2BE6")

    label("loc_2B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2BDD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BD5")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Sheesh, Granny...\x01",
            "Have you bothered to reflect on your actions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It doesn't look like it.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_2BD8")

    label("loc_2BD5")

    Call(0, 26)

    label("loc_2BD8")

    Jump("loc_2BE6")

    label("loc_2BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2BE6")

    label("loc_2BE6")

    Return()

    # Function_10_2A53 end

    def Function_11_2BE7(): pass

    label("Function_11_2BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2D2B")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB0")

    ChrTalk(
        0xFE,
        "Oh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The detectives are busy having a meeting about\x01",
            "the security detail for the closing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, I wanted to get in on the action, too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2D23")

    label("loc_2CB0")


    ChrTalk(
        0xFE,
        (
            "Anyway, this should be the last day we have\x01",
            "to deal with this insane crowd.\x01",
            "Let's look sharp out there, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D23")

    TalkEnd(0xFE)
    Jump("loc_2F60")

    label("loc_2D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2D39")
    Jump("loc_2F60")

    label("loc_2D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D47")
    Jump("loc_2F60")

    label("loc_2D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2F57")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F4F")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DF0")
    Jump("loc_2E3A")

    label("loc_2DF0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E10")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E3A")

    label("loc_2E10")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E30")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E3A")

    label("loc_2E30")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E3A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Hmm... I just can't seem to get used to\x01",
            "conducting interrogations, no matter how\x01",
            "many of them I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can detain some snot-nosed punks\x01",
            "like it's nothing, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Is he going to survive this career choice?)\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2F52")

    label("loc_2F4F")

    Call(0, 26)

    label("loc_2F52")

    Jump("loc_2F60")

    label("loc_2F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F60")

    label("loc_2F60")

    Return()

    # Function_11_2BE7 end

    def Function_12_2F61(): pass

    label("Function_12_2F61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2F72")
    Jump("loc_3090")

    label("loc_2F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2FF7")

    ChrTalk(
        0xFE,
        "We had a higher turnout than what was projected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's almost as if Crossbell's population\x01",
            "doubled overnight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3090")

    label("loc_2FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3005")
    Jump("loc_3090")

    label("loc_3005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3013")
    Jump("loc_3090")

    label("loc_3013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3090")

    ChrTalk(
        0xFE,
        "Suspect apprehended!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This dirtbag thought he could try and\x01",
            "ruin the festive atmosphere with his\x01",
            "mischief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3090")

    TalkEnd(0xFE)
    Return()

    # Function_12_2F61 end

    def Function_13_3094(): pass

    label("Function_13_3094")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_31C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3135")

    ChrTalk(
        0xFE,
        "Ah, it's still as crowded as ever out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever. I'm just out here to\x01",
            "buy some coffee.\x01",
            "Don't worry about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_31BC")

    label("loc_3135")


    ChrTalk(
        0xFE,
        "I'm actually supposed to be in the middle of a meeting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You didn't see anything, okay?\x01",
            "I am a figment of your imagination...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BC")

    Jump("loc_341B")

    label("loc_31C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3256")

    ChrTalk(
        0xFE,
        "So, is the Second Division going to help us, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Metropolitan Division already has their\x01",
            "hands full enough as it is...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_341B")

    label("loc_3256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3264")
    Jump("loc_341B")

    label("loc_3264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_336B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3313")

    ChrTalk(
        0xFE,
        (
            "Donovan and his men just brought in\x01",
            "a bunch of supposed criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What is it with this crowd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Isn't everybody a little too excited?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3366")

    label("loc_3313")


    ChrTalk(
        0xFE,
        (
            "Well, everybody's just enjoying the festive\x01",
            "mood of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3366")

    Jump("loc_341B")

    label("loc_336B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_341B")

    ChrTalk(
        0xFE,
        (
            "Yeah, I don't have time to sip on this\x01",
            "coffee at a snail's pace. We're way too\x01",
            "busy right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, thanks for helping me out today.\x01",
            "See you guys around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_341B")

    TalkEnd(0xFE)
    Return()

    # Function_13_3094 end

    def Function_14_341F(): pass

    label("Function_14_341F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3430")
    Jump("loc_355D")

    label("loc_3430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_34B9")

    ChrTalk(
        0xFE,
        "Sounds like the parade's finally over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll head back to guarding the priority\x01",
            "locations in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_355D")

    label("loc_34B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_355D")

    ChrTalk(
        0xFE,
        (
            "Dudley's out on a business trip\x01",
            "to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why would he go on a one-day trip\x01",
            "during a busy period like this?\x01",
            "What is the top brass thinking?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_355D")

    TalkEnd(0xFE)
    Return()

    # Function_14_341F end

    def Function_15_3561(): pass

    label("Function_15_3561")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C5")

    ChrTalk(
        0xFE,
        (
            "Screw you!\x01",
            "I didn't do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm not guilty! You can't prove anything!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_363B")

    label("loc_35C5")


    ChrTalk(
        0xFE,
        (
            "How was I supposed to know the\x01",
            "police would be at a place like that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I exercise my right to remain silent!\x02",
    )

    CloseMessageWindow()

    label("loc_363B")

    TalkEnd(0xFE)
    Return()

    # Function_15_3561 end

    def Function_16_363F(): pass

    label("Function_16_363F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3749")
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        "Raymond, the interrogation rooms are all full!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What should we do?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Never fear. When the going gets tough, the\x01",
            "tough get going! To the conference room!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, it's time for some more patrollin'.\x01",
            "To Station Street, we go!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_3897")

    label("loc_3749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3849")

    ChrTalk(
        0xFE,
        (
            "We've received many police reports from the\x01",
            "Harbor and Entertainment Districts, so we need\x01",
            "to up the officer count on our patrols there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What a pain... I'm going to have to book\x01",
            "it if I want to be able to take a break.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3897")

    label("loc_3849")


    ChrTalk(
        0xFE,
        (
            "Heck, who am I kidding? It's already about time\x01",
            "I return to my patrol...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3897")

    TalkEnd(0xFE)
    Return()

    # Function_16_363F end

    def Function_17_389B(): pass

    label("Function_17_389B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_392F")
    Jump("loc_3979")

    label("loc_392F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_394F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3979")

    label("loc_394F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_396F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3979")

    label("loc_396F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3979")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AEC")
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        (
            "#5SY-Y-You...! How dare you waltz in here like\x01",
            "you own the place! The gall! The nerve! I'm\x01",
            "going to make you pay, I swear it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#5SOh, yes. Come next year, you won't know\x01",
            "what hit you! Remember that, you punks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yeah, yeah, yeah. Don't make me put\x01",
            "the cuffs back on you, Granny.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x1, 2)
    Jump("loc_3B5F")

    label("loc_3AEC")

    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xFE,
        (
            "#5SNext year, I'll be back and better than\x01",
            "ever! You'll rue the day you decided to\x01",
            "cross me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B5F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_389B end

    def Function_18_3B67(): pass

    label("Function_18_3B67")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3BE6")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Interrogation Room - Occupied]\x01",
            "        Metropolitan Division\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_3BEF")

    label("loc_3BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3BEF")

    label("loc_3BEF")

    EventEnd(0x1)
    Return()

    # Function_18_3B67 end

    def Function_19_3BF2(): pass

    label("Function_19_3BF2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C86")
    Jump("loc_3CD0")

    label("loc_3C86")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CA6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CD0")

    label("loc_3CA6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CC6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CD0")

    label("loc_3CC6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CD0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D07")
    Call(0, 20)
    Jump("loc_3E1F")

    label("loc_3D07")


    ChrTalk(
        0xFE,
        (
            "#1004F*puff* Whew... Nothing like a good cigarette\x01",
            "to celebrate that parade ending. I thought it\x01",
            "was never going to stop moving.\x02\x03",
            "#1000FAnd don't get me started on the crowd. They\x01",
            "make things ten times harder than it needs to\x01",
            "be. Besides, I've lost all my reading time, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E1F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_3BF2 end

    def Function_20_3E27(): pass

    label("Function_20_3E27")


    ChrTalk(
        0xFE,
        (
            "#1005FStopping by the department?\x02\x03",
            "#1006FI tried playing hooky on the roof earlier, but as\x01",
            "soon as they found me, they loaded my desk\x01",
            "with new assignments...\x02\x03",
            "'There's no one as qualified as you,' they said.\x01",
            "Yeah. Qualified, my ass...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FPlease try to be at least a little productive, Chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FYeah! We're bustin' our asses out\x01",
            "there, man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0201FDo you not have any shame?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1000FC'mon, don't be like that. Here, consider\x01",
            "this a bonus for working so hard.\x02",
        )
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
            scpstr(SCPSTR_CODE_ITEM, 0x2CD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0xFE,
        (
            "#1006FI originally planned on reading that the\x01",
            "rest of the day, but things don't always\x01",
            "go the way we want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F*sigh* So you were neglecting work to\x01",
            "catch up on some light reading...?\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber(0x2CD, 1)
    SetScenarioFlags(0x9C, 7)
    Return()

    # Function_20_3E27 end

    def Function_21_4125(): pass

    label("Function_21_4125")

    TalkBegin(0xFE)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xFE,
        (
            "D-Don't underestimate the Black Emperors!\x01",
            "You can't keep us down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#1006FYeah, whatever. Listen, I don't particularly\x01",
            "care about your cause. Now, give me names.\x02\x03",
            "#1000FKeep in mind, I'm not going to play your silly\x01",
            "games. Just give me your name, you punk.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_4125 end

    def Function_22_4247(): pass

    label("Function_22_4247")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Due to the unexpected crowd this year, we're\x01",
            "running a little short-handed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could be wrong, but I've got a feeling that the\x01",
            "worst is yet to come... Be careful, everyone!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_4247 end

    def Function_23_4304(): pass

    label("Function_23_4304")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(-140, 1540, 13420, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    SetChrPos(0x101, 400, 0, 13450, 0)
    SetChrPos(0x102, -600, 0, 13200, 0)
    SetChrPos(0x103, 400, 0, 11950, 0)
    SetChrPos(0x104, -600, 0, 11700, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        "#5PHey, it's the guys from the SSS.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P*sigh* I figured it'd get busier than\x01",
            "past years, but this is too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYeah, we know how you feel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0104FUs police officers have our plates\x01",
            "full during this festive period.\x02\x03",
            "#0100FBy the way, we received a support request\x01",
            "from the Metropolitan Division. Are the ones\x01",
            "in charge of the request in right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, you mean the request regarding\x01",
            "ticketing illegally parked cars?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThey're usually out and about, so it\x01",
            "may take a while to get a hold of them.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_45AE():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45AE)
    Sleep(100)

    def lambda_45BE():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_45BE)

    def lambda_45CB():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_45CB)

    def lambda_45D8():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_45D8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#11P#0000FWhat do you say guys? Wait here until\x01",
            "we hear about the request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FI am fine with it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FYeah, let's knock this one out.\x02",
    )

    CloseMessageWindow()

    def lambda_4696():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4696)

    def lambda_46A3():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_46A3)

    def lambda_46B0():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_46B0)

    def lambda_46BD():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_46BD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#12P#0000FLooks like we're in agreement, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PUnderstood. I'll call them immediately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFeel free to wait in the conference room\x01",
            "until they arrive.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_68(-62770, 2140, 17220, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22390, 0)
    OP_68(-62770, 1540, 17220, 2000)
    SetChrPos(0x101, -60500, 150, 20150, 180)
    SetChrPos(0x102, -64000, 150, 20150, 180)
    SetChrPos(0x103, -60500, 150, 15850, 0)
    SetChrPos(0x104, -64000, 150, 15850, 0)
    SetChrPos(0xE, -64599, 40, 8400, 0)
    SetChrPos(0x17, -65400, 40, 8250, 0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    OP_4B(0xE, 0xFF)
    OP_4B(0x17, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#5P#0003FWe've been waiting here an awfully long time...\x01",
            "They must be pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FYeah, not much we can do about it.\x01",
            "Festival must get real overwhelmin'.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(103, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x1)
    OP_68(-63070, 1540, 14720, 0)
    MoveCamera(37, 13, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23450, 0)
    OP_68(-63070, 1540, 14720, 1000)

    def lambda_49C1():
        OP_97(0xE, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_49C1)

    def lambda_49DB():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_49DB)
    Sleep(50)

    def lambda_49EF():
        OP_97(0x17, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_49EF)

    def lambda_4A09():
        OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4A09)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xE, 2)
    OP_93(0xE, 0x2D, 0x1F4)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x17, 2)
    OP_93(0x17, 0x2D, 0x1F4)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#12PHey, sorry about that! We were\x01",
            "dealing with something urgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#6PSorry for making you guys wait.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FDon't worry about it.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-61850, 1500, 18250, 0)
    MoveCamera(52, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24440, 0)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0x103, 0x2)
    SetChrSubChip(0x104, 0x2)
    SetChrPos(0xE, -57450, 0, 15000, 0)
    SetChrPos(0x17, -57200, 0, 16400, 0)

    def lambda_4B33():
        OP_97(0xE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B33)
    Sleep(50)

    def lambda_4B50():
        OP_97(0x17, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4B50)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x10E, 0x1F4)
    WaitChrThread(0x17, 1)
    OP_93(0x17, 0x10E, 0x1F4)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -59750, 0, 19900, 135)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, -63250, 0, 19900, 90)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -59750, 0, 16100, 45)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -63250, 0, 16100, 90)
    ClearChrFlags(0x104, 0x4)
    Sound(820, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#11PThanks. I'm the Metropolitan Division's\x01",
            "Chief Jolich.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PAnd I'm Officer Kate, of the same\x01",
            "designation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PThanks for lending us a hand,\x01",
            "Special Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005F(Looks like we'll have to give a formal\x01",
            "introduction this time around...)\x02\x03",
            "#0001FI'm Lloyd Bannings of the Special Support\x01",
            "Section, and these three are my colleagues.\x02\x03",
            "We know you're swamped with work, but\x01",
            "would you mind explaining the details of\x01",
            "the request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PNo problem. Allow me to explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PBut first, I think that's enough with the formalities.\x01",
            "I don't mind if we speak more casually now.\x02",
        )
    )

    CloseMessageWindow()
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
        0x17,
        "#5PSorry, our chief likes to take things easy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAnyway, I think this was written in the support\x01",
            "request. I'd like for you to ticket any illegally\x01",
            "parked vehicles on the outskirts of town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThis goes without saying, but we're seriously\x01",
            "lacking the manpower to handle this right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAll you have to do is write down the car's license\x01",
            "plate number, attach a warning sticker, and fine\x01",
            "them if they're parked illegally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FIs that really all you'd like for us to do?\x01",
            "You don't need us to tow them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PDon't worry about it. Giving them a\x01",
            "fine is more than adequate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PA lot of people drove in from the Empire\x01",
            "or the Republic, so they don't know the\x01",
            "parking rules. Towing would be too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PMore importantly, some of the cars you'll\x01",
            "be checking already have parking permits.\x02",
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
        "#12P#0200FParking permits...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PYeah, not every car is necessarily parked\x01",
            "there illegally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PSome of them obtained permits to park there\x01",
            "beforehand, so you'll need to exercise caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FCool. We'll keep our eyes peeled for which\x01",
            "ones already bought permits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FOkay, I think I understand the procedure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FAnd I recall a few cars being parked at\x01",
            "the eastern and western exits of town.\x02\x03",
            "#0000FIt'd be smart of us to check both exits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FIndeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11POkay, let me give you this list of permit holders.\x02",
    )

    CloseMessageWindow()

    def lambda_5486():
        OP_97(0x101, 0x2EE, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5486)

    def lambda_54A0():
        OP_95(0xE, -58490, 30, 19160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_54A0)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x87, 0x1F4)
    WaitChrThread(0xE, 1)
    Sleep(1000)
    OP_96(0xE, 0xFFFF1F96, 0x0, 0x4844, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x2DB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2DB, 1)

    ChrTalk(
        0x17,
        (
            "#5PAnd while you're at it, take this pack\x01",
            "of warning stickers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#5PWe like to call these our 'illegal parking tools'!\x02",
    )

    CloseMessageWindow()

    def lambda_55AB():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55AB)
    OP_96(0x17, 0xFFFF1CA8, 0x1E, 0x4DBC, 0x7D0, 0x0)
    Sleep(1000)
    OP_96(0x17, 0xFFFF2090, 0x0, 0x4DBC, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x348),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x348, 1)

    ChrTalk(
        0x101,
        "#6P#0000FOkay, got it.\x02",
    )

    CloseMessageWindow()

    def lambda_564B():
        OP_93(0xE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_564B)

    def lambda_5658():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5658)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xE,
        (
            "#11PPlease report to Rebecca once you've\x01",
            "completed our request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PKate and I are going to hit the city,\x01",
            "so we'll be gone all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FUnderstood. We'll give our report\x01",
            "to Rebecca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FWhat say you we scoot on over\x01",
            "to the city limits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FThat sounds good to me.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Illegal Parking Crackdown]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_4C(0xE, 0xFF)
    OP_4C(0x17, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    OP_49()
    OP_68(-65099, 1500, 14250, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -65099, 0, 14250, 180)
    SetChrPos(0x1, -65099, 0, 14250, 180)
    SetChrPos(0x2, -65099, 0, 14250, 180)
    SetChrPos(0x3, -65099, 0, 14250, 180)
    OP_29(0x17, 0x1, 0x0)
    SetScenarioFlags(0x0, 1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_23_4304 end

    def Function_24_58B7(): pass

    label("Function_24_58B7")


    ChrTalk(
        0x8,
        (
            "Hey, everyone. How's the request to ticket\x01",
            "those illegally parked cars going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please notify me once you're ready to\x01",
            "hand over your report. I'll contact\x01",
            "the Metropolitan Division.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Report]\x01",       # 0
            "[Not Yet]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ABA")

    ChrTalk(
        0x101,
        (
            "#0000FWe're all ready to give our report.\x01",
            "Could you contact them, please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Understood. I'll take care of it now.\x01",
            "I apologize for the inconvenience, but do\x01",
            "you mind waiting again until they're here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FNot at all. We understand they're busy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B2B")

    label("loc_5ABA")


    ChrTalk(
        0x8,
        (
            "Please report to me once you've\x01",
            "completed your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I will contact the Metropolitan Division\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B2B")

    Return()

    # Function_24_58B7 end

    def Function_25_5B2C(): pass

    label("Function_25_5B2C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xE, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_68(-57380, 1600, 17520, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    OP_68(-57380, 900, 17520, 3000)
    SetChrPos(0x101, -57500, 0, 17000, 0)
    SetChrPos(0x102, -56750, 0, 16500, 0)
    SetChrPos(0x103, -58250, 0, 15500, 0)
    SetChrPos(0x104, -57500, 0, 15000, 0)
    SetChrPos(0xE, -57500, 0, 19000, 180)
    SetChrPos(0x17, -58500, 0, 19250, 180)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#12P#0003FThat's it for the report.\x02\x03",
            "#0000FHere's the list of license plates for\x01",
            "any illegally parked cars.\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)

    ChrTalk(
        0xE,
        "#5PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PFantastic job, everyone. You even managed\x01",
            "to avoid giving out any erroneous fines.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EC6")
    OP_2C(0x17, 0x2)
    OP_29(0x17, 0x1, 0x16)

    ChrTalk(
        0x102,
        (
            "#12P#0100FYes, we tried our hardest to avoid\x01",
            "making any mistakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FMany of the owners were from either the\x01",
            "Republic or the Empire, so we were\x01",
            "nervous about making errors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PSorry for putting you guys in that position.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI wouldn't have minded you guys doing a\x01",
            "rush job. That's usually how it goes for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6018")

    label("loc_5EC6")

    OP_29(0x17, 0x1, 0x15)

    ChrTalk(
        0xE,
        (
            "#5PYou, uh, didn't make any mistakes, though.\x01",
            "Did you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#0005FU-Uhh...\x02\x03",
            "#0006F(I'm not feeling too confident on that one...\x01",
            "We kinda did it in a hurry.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PAh, well. Not much you can do about it now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAnd if I'm being perfectly honest, we don't\x01",
            "put much effort into doing this, either!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6018")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0x17, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0x17,
        (
            "#5PWhat are you talking about, Chief?!\x01",
            "We take our job very seriously!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x17, 500)

    ChrTalk(
        0xE,
        "#11PSorry, sorry.\x02",
    )

    CloseMessageWindow()

    def lambda_6109():
        OP_93(0xE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6109)

    def lambda_6116():
        OP_93(0x17, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6116)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x17, 1)

    ChrTalk(
        0x17,
        (
            "#5PAnyway. It looks like we've managed to write\x01",
            "off one task from our to-do list.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PThanks, guys! This should give us a\x01",
            "bit more breathing room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PRight. Allow me to give you my thanks.\x01",
            "You can definitely count on the SSS\x01",
            "to take care of your work, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FHah. Can't even escape the handyman\x01",
            "treatment at headquarters, can we?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_6816")
    OP_2C(0x17, 0x2)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x102, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#0105FHey, Lloyd. Shouldn't we tell them\x01",
            "about the inconsistency?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x102, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#0005FOh, yeah. I forgot about that...\x02",
    )

    CloseMessageWindow()

    def lambda_6353():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6353)

    def lambda_6360():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6360)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x101,
        "#12P#0001FHey, actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PHmm? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FWe noticed something strange with\x01",
            "the license plates.\x02\x03",
            "There were two cars that shared the same\x01",
            "license plate number across both exits.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#0001FI believe the license plate number\x01",
            "was 'CL 1101.'\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x17,
        (
            "#5PW-Wait, seriously?\x01",
            "Could one of the plates be a forgery?!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x17)

    ChrTalk(
        0xE,
        "#5PI would think so.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x17, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#5PYou need to pay a fee to obtain a\x01",
            "parking permit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PNot to mention, you have to pay a daily fee\x01",
            "to park there. You'll have to fork over a hefty\x01",
            "amount of mira to park there the whole festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PSomeone probably wanted to skip out on\x01",
            "springing for two separate permits.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12P#0306FWow, what a cheap ass. Coulda been worse,\x01",
            "though. At least he ain't out there committin'\x01",
            "any serious crimes, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FAgreed.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x17, 500)

    ChrTalk(
        0xE,
        (
            "#5PHmm. Kate, do me a favor and check\x01",
            "this out for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#5PYes, sir!\x02",
    )

    CloseMessageWindow()

    label("loc_6816")


    ChrTalk(
        0x101,
        (
            "#12P#0001FAnyway, it looks like our job here\x01",
            "is done. We'll be taking our leave now.\x02\x03",
            "#0000FIf you ever need assistance again, the SSS\x01",
            "will gladly tackle the case for you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_68CC():
        OP_93(0xE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_68CC)

    def lambda_68D9():
        OP_93(0x17, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_68D9)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x17, 1)

    ChrTalk(
        0xE,
        "#5PThanks. We'll be counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PThe festival has been dumping loads of\x01",
            "work on us, but let's keep up the hustle!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Illegal Parking Crackdown]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, -25580, 0, 11350, 180)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    OP_29(0x17, 0x4, 0x10)
    SetScenarioFlags(0x0, 2)
    EventEnd(0x5)
    Return()

    # Function_25_5B2C end

    def Function_26_69FB(): pass

    label("Function_26_69FB")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-59660, 1500, 14140, 0)
    MoveCamera(38, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25010, 0)
    SetChrPos(0xB, -57730, 0, 16309, 225)
    SetChrPos(0xC, -57730, 0, 14480, 270)
    SetChrPos(0x101, -60000, 30, 14500, 45)
    SetChrPos(0x102, -60000, 0, 13000, 45)
    SetChrPos(0x103, -61500, 0, 14500, 45)
    SetChrPos(0x104, -61500, 0, 13000, 45)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#0000FGood to see you, Inspector Donovan.\x02\x03",
            "We're here to ask about that support request\x01",
            "you submitted. Are you free right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PHmm, I suppose I can find the time. Thanks\x01",
            "for coming, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PYeah. We really appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0105FSo what exactly does the request entail?\x02\x03",
            "#0101FJudging by the submission, it sounded like\x01",
            "it was quite urgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PYou can say that again. Take a seat, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0309FSomething's tellin' me that we've got\x01",
            "some legit police work ahead of us.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-60460, 1900, 19460, 0)
    MoveCamera(48, 13, 0, 0)
    OP_6E(-3450, 0)
    SetCameraDistance(36130, 0)
    OP_68(-60460, 900, 19460, 3000)
    SetChrPos(0xB, -58000, 0, 18000, 270)
    SetChrPos(0xC, -57360, 0, 19780, 270)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -60550, 150, 15950, 0)
    SetChrPos(0x102, -60550, 150, 20000, 180)
    SetChrPos(0x103, -64050, 150, 20000, 180)
    SetChrPos(0x104, -64050, 150, 15950, 0)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xB,
        (
            "#11PNow, then. About the reason we've called you\x01",
            "in today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PWell, we want the Special Support Section to\x01",
            "help us expose a counterfeit dealer, who should\x01",
            "be on their way to Crossbell as we speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FA counterfeit dealer? Could you explain more?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FThey are traders that illegally sell seemingly\x01",
            "genuine accessories and orbments.\x02\x03",
            "They use the logos of famous brands. In other\x01",
            "words, they deal in fakes.\x02\x03",
            "#0200FIt qualifies as a minor criminal offense under\x01",
            "Crossbell State law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PSh-She really had all that memorized?\x01",
            "'Cause, yeah, that's the general idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PEvery year, loads of counterfeit dealers try\x01",
            "their hand in Crossbell, posing as tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHigh-class watches from the Verne Company,\x01",
            "vintage Strega products, not to mention a\x01",
            "boatload of septium trinkets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PTaking advantage of unsuspecting customers\x01",
            "has earned these crooks a whole lot of mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0301FMakin' some cash by deceiving innocents...\x01",
            "That's just messed up, man.\x02\x03",
            "#0303FLemme get this straight. You want us to\x01",
            "help you take these guys down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PExactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PWe should really be handling this ourselves,\x01",
            "but there's just too many of these reports\x01",
            "to deal with every year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PIf we leave them unchecked for too long,\x01",
            "it's going to hurt manufacturers and retailers\x01",
            "trying to make a living, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PWe'll need to crack down on these guys\x01",
            "if we want to restore people's faith in the CPD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FI'm with you there.\x01",
            "I understand the situation.\x02\x03",
            "#0001FIf you truly think the SSS is suited for the job,\x01",
            "then allow us to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PExcellent. I'm in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FOkay, so what would you like for\x01",
            "us to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11POkay, so here's the deal. I think they've got\x01",
            "three points of entry: Crossbell Station, the\x01",
            "airport, and Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PWe'll take care of the station and airport,\x01",
            "and you guys can be on the lookout\x01",
            "at the border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThe Second Division is short-staffed,\x01",
            "so we can't afford to send people\x01",
            "all the way out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAnd besides, I'm pretty sure you guys\x01",
            "are well acquainted with Deputy\x01",
            "Commander Baelz, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PYou're best suited to cooperate with her\x01",
            "if we need to come up with any\x01",
            "countermeasures against them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0103FIt's as you say. I wouldn't be surprised if\x01",
            "she were more willing to cooperate with\x01",
            "us than with other CPD officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FOh, hell no! I'm totally cool with finishing\x01",
            "the job without havin' to see her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11POkay, looks like we've got everything in order.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PWe'll start by covering the airport and station.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PYou guys rendezvous over at Tangram\x01",
            "Gate and contact the Guardian Force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FUnderstood.\x01",
            "We'll depart for Tangram Gate immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PThanks, we're counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PSee you guys later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 27)
    BeginChrThread(0xC, 3, 0, 28)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    Fade(1000)
    OP_68(-61410, 900, 18100, 0)
    MoveCamera(61, 17, 0, 0)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x104, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#0000FOkay. You guys want to head to\x01",
            "Tangram Gate now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FWe should explain the situation to Deputy\x01",
            "Commander Baelz and request for her\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Exposing the Counterfeit Dealers]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-61760, 1530, 15420, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -61760, 30, 15420, 180)
    SetChrPos(0x1, -61760, 30, 15420, 180)
    SetChrPos(0x2, -61760, 30, 15420, 180)
    SetChrPos(0x3, -61760, 30, 15420, 180)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
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
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_29(0x1B, 0x1, 0x1)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_26_69FB end

    def Function_27_7AF5(): pass

    label("Function_27_7AF5")

    OP_68(-64370, 900, 15160, 6000)
    MoveCamera(59, 17, 0, 6000)

    def lambda_7B16():
        OP_95(0xFE, -58000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7B16)
    WaitChrThread(0xB, 1)

    def lambda_7B34():
        OP_95(0xFE, -65200, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7B34)
    WaitChrThread(0xB, 1)
    Sound(103, 0, 100, 0)

    def lambda_7B58():
        OP_95(0xFE, -65200, 0, 8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7B58)

    def lambda_7B72():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_7B72)
    WaitChrThread(0xB, 1)
    Sound(104, 0, 100, 0)
    Return()

    # Function_27_7AF5 end

    def Function_28_7B89(): pass

    label("Function_28_7B89")

    Sleep(500)

    def lambda_7B91():
        OP_95(0xFE, -57360, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7B91)
    WaitChrThread(0xC, 1)

    def lambda_7BAF():
        OP_95(0xFE, -65200, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7BAF)
    WaitChrThread(0xC, 1)

    def lambda_7BCD():
        OP_95(0xFE, -65200, 0, 9300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7BCD)

    def lambda_7BE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_7BE7)
    WaitChrThread(0xC, 1)
    Return()

    # Function_28_7B89 end

    def Function_29_7BF8(): pass

    label("Function_29_7BF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x1, 0x10)
    LoadChrToIndex("chr/ch07300.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03400.itp")
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    OP_68(-123940, 2500, 16390, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22600, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, -35500, 0, 16000, 0)
    SetChrPos(0x102, -34000, 0, 16000, 0)
    SetChrPos(0x103, -35500, 0, 14500, 0)
    SetChrPos(0x104, -34000, 0, 14500, 0)
    SetChrPos(0x14, -34750, 0, 13000, 0)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -34750, 0, 17500, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
    Sleep(500)
    OP_68(-123940, 1500, 16390, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x16,
        (
            "#6PUhh...\x01",
            "Could I ask for your name, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P...Hah. Like I'd give my name to some\x01",
            "lanky brat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#6PL-Lanky?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PListen here, Granny...\x01",
            "Do you have any idea what you've done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PYou're aware we've already arrested\x01",
            "all of your friends, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#6PSo can it, and give in already.\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x15,
        (
            "#11P#5SY-Y-You insolent, disrespectful hooligan!\x01",
            "Did your parents teach you no etiquette?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x15,
        (
            "#11P#5SWhen talking to a lady, you must at least\x01",
            "offer her a cup of tea! Common courtesy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6PH-Huh? S-Sure, whatever. I'll bring you a\x01",
            "cup later, okay...?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-35320, 1500, 15470, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23600, 0)
    SetCameraDistance(22600, 2000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#0006FUh... Is Raymond going to be all right\x01",
            "handling her by himself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PShe's a tough nut, that's for sure. But don't\x01",
            "worry, we can crack her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PBesides, this is a secure facility. She won't\x01",
            "be getting out of here any time soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0106FI don't know... I could see her brute-forcing\x01",
            "her way out of anything, quite honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203FI agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PBy the way, who's the beautiful young lady\x01",
            "over there?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8179():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8179)
    Sleep(150)

    def lambda_8189():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8189)
    Sleep(70)

    def lambda_8199():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8199)
    Sleep(150)

    def lambda_81A9():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_81A9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#11P#0305FY'know, now that I think about it, I never\x01",
            "asked!\x02\x03",
            "#0300F'Scuse me, ma'am. We're going to need\x01",
            "your name and occupation, please. For\x01",
            "police business, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("Black-Haired Woman")

    AnonymousTalk(
        0xFF,
        (
            "#12PKilika Rouran, at your service.\x02\x03",
            "I'm a Calvardian entertainment producer.\x02\x03",
            "I came to Crossbell...well, let's say it was by chance.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x104,
        (
            "#11P#0304FKilika, eh? Gotta say, I dig it.\x02\x03",
            "#0309FAnd you're a producer, to boot? You definitely look\x01",
            "the part, and I mean that in the best of ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FShe helped us apprehend the suspect, Inspector\x01",
            "Donovan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PIs that right? Hmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PExcuse our poor manners, ma'am. The CPD\x01",
            "thanks you for your invaluable cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIf you like, I'm sure we can scrounge up a reward\x01",
            "for you. Can't guarantee it'll be much, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12P#3404FPlease, don't bother.\x02\x03",
            "#3400FI hardly think my contribution was worth\x01",
            "that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PHaha. Well, if you say so. I'm sure our\x01",
            "bookkeeper will appreciate that, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85F3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_85F3)
    Sleep(150)

    def lambda_8603():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8603)
    Sleep(70)

    def lambda_8613():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8613)
    Sleep(150)

    def lambda_8623():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8623)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x103,
        "#12P#0211FPlease remain professional, Inspector.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FActually, I've been wondering... How did the\x01",
            "stakeouts at the train station and airport go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POh, that? Luckily, the other dealers\x01",
            "were caught and arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POn top of that, we were able to confiscate all\x01",
            "of the counterfeit items they were carrying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PSo, if all goes according to plan, they'll be out\x01",
            "of business for the rest of the year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0105F'Rest of the year'? Implying that there will be\x01",
            "other years?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYes, well...in addition to a stern warning, they\x01",
            "will also be prohibited from entering Crossbell\x01",
            "for a month. But that's about it, most likely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FY-You're not going to detain them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FSo...what you're really sayin' is that our work\x01",
            "didn't do jack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PTio said it before. According to state law, it's\x01",
            "only a minor criminal offense. And since\x01",
            "they're foreigners, we can't do much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PTrust me, I understand how disheartening it\x01",
            "can be. But this is as much as we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PNow, now. Don't be discouraged. You four\x01",
            "did fine work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PEspecially when you consider the fact that\x01",
            "they'll be out of commission for the festival.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Raymond's Voice")
    SetMessageWindowPos(-50, 20, -1, -1)

    AnonymousTalk(
        0x16,
        "#2SD-Donovan... Please help me...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#5PWhoops. It sounds like Raymond needs\x01",
            "some saving from that devil spawn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PAnyway, good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYour effectiveness was most definitely\x01",
            "noted, let me assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FThank you, Inspector. You can give us\x01",
            "a call any time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D8D")

    ChrTalk(
        0xB,
        "#5POh, right. I forgot to tell you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PThat tourist you falsely accused was let\x01",
            "go, finally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PThe brass made sure to give them a gift\x01",
            "and a basketful of apologies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PJust hold back on the rash decisions\x01",
            "from here on out, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0006FW-We're sorry, sir. It won't happen again.\x02",
    )

    CloseMessageWindow()

    label("loc_8D8D")

    OP_93(0xB, 0x0, 0x1F4)

    def lambda_8D99():
        OP_95(0xFE, -34750, 0, 18800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8D99)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x1)
    Sleep(500)

    def lambda_8DD2():
        OP_95(0xFE, -34750, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8DD2)

    def lambda_8DEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8DEC)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x1)

    ChrTalk(
        0x14,
        (
            "#12P#3401FCrossbell's authority really is as weak as\x01",
            "the rumors say. Well, I suppose I cannot\x01",
            "be surprised about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FWhat do you mean?\x02",
    )

    CloseMessageWindow()
    OP_68(-35070, 1500, 14300, 1000)

    def lambda_8EC7():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EC7)

    def lambda_8ED4():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8ED4)

    def lambda_8EE1():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8EE1)

    def lambda_8EEE():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8EEE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x14,
        (
            "#12P#3403FLaws are created to protect the citizenry's\x01",
            "well-being, and yet...\x02\x03",
            "...Crossbell is no more than an obedient\x01",
            "pup to Erebonia and Calvard.\x02\x03",
            "#3400FSurely you've noticed that bitter truth on\x01",
            "more than one occasion, right? It has to\x01",
            "be extremely frustrating, I imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12P#3404FDon't be so glum. After all...for continuing\x01",
            "to fight against the status quo, you ought\x01",
            "to be praised.\x02\x03",
            "#3402FThough I suppose it's none of my business as\x01",
            "a Calvardian. Regardless, I'd advise you to not\x01",
            "give up. I'm sure your efforts will pay off one day.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xB4, 0x190)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#0011FKilika...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0305FSo what's your plan now? Already found\x01",
            "a place to crash?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#3404FYes, I have. A room in the Entertainment\x01",
            "District's fancy hotel. Millennium, was it?\x02\x03",
            "Anyway, I plan on staying there for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FWe'd be more than happy to give you a\x01",
            "tour of the city, but I'd have to check our\x01",
            "schedule...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#3400FI appreciate the gesture, but I'm\x01",
            "well acquainted with Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0205FYou said the Entertainment District...?\x02\x03",
            "#0200FDoes that perhaps have something to\x01",
            "do with the motive behind your visit?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#12P#3400FYou ARE a sharp one, aren't you?\x02\x03",
            "That's right. I've come to see Arc en Ciel.\x02\x03",
            "#3404FIf possible, I was hoping to get them to agree\x01",
            "to performing in the Republic. A tour, perhaps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FYou're looking to book them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12P#3404FWhy, of course. Arc en Ciel is an enchanting\x01",
            "septium vein, lying dormant in Crossbell...\x02\x03",
            "Have they the charisma to capture Calvard\x01",
            "with their magical shows? Can they create a\x01",
            "vortex of enthusiasm for theatre there?\x02\x03",
            "#3402FDetermining that is my mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FI see...\x02\x03",
            "#0003F(So when she was talking about a jewel\x01",
            "at Tangram Gate, she was talking about\x01",
            "Arc en Ciel all along?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x14)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_END)), "loc_9780")

    ChrTalk(
        0x14,
        (
            "#12P#3404FYou're an interesting bunch. Unrefined, yet true\x01",
            "to yourselves.\x02\x03",
            "#3402FAnd true professionals as well, deducing\x01",
            "who the culprit was like that. That wasn't\x01",
            "something that comes to people easily.\x02\x03",
            "Let's both do our best from here on out, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9992")

    label("loc_9780")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_9892")

    ChrTalk(
        0x14,
        (
            "#12P#3404FYou're an interesting bunch. Unrefined, yet true\x01",
            "to yourselves.\x02\x03",
            "#3400FAnd, despite investigating, you chose me as the\x01",
            "culprit at the end of the day. We can just chalk\x01",
            "that up to inexperience.\x02\x03",
            "Let's both do our best from here on out, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9992")

    label("loc_9892")


    ChrTalk(
        0x14,
        (
            "#12P#3404FYou're an interesting bunch. Unrefined, yet true\x01",
            "to yourselves.\x02\x03",
            "#3400FAnd, despite investigating, you chose me as the\x01",
            "culprit at the end of the day. We can just chalk\x01",
            "that up to inexperience.\x02\x03",
            "Let's both do our best from here on out, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9992")


    ChrTalk(
        0x101,
        (
            "#5P#0003FY-Yeah.\x02\x03",
            "#0000FThank you for your assistance again, Kilika.\x02\x03",
            "If there's anything you need while you're here,\x01",
            "please don't hesitate to contact us. We'd love\x01",
            "an opportunity to return the favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12P#3402FIf the opportunity arises, I certainly won't.\x02\x03",
            "#3404FWell, then. If you'll excuse me, I'll be off.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xB4, 0x1F4)

    def lambda_9ADE():
        OP_95(0xFE, -34750, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9ADE)
    WaitChrThread(0x14, 1)

    def lambda_9AFC():
        OP_95(0xFE, -28000, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9AFC)
    WaitChrThread(0x14, 1)

    ChrTalk(
        0x102,
        (
            "#5P#0106F*sigh* This request was more than I was\x01",
            "expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FYou're tellin' me.\x02\x03",
            "#0309FBut, hey! Thanks to that, I was able to meet\x01",
            "that hot piece of lady.\x02\x03",
            "#0304FMan, I thought I was used to checkin' out\x01",
            "Eastern chicks, but...damn, that Kilika is\x01",
            "on another level.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9C37():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9C37)

    ChrTalk(
        0x103,
        "#6P#0206FYou are incorrigible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FHaha. Well, at least he didn't say it in front\x01",
            "of her, I guess.\x02\x03",
            "Is everyone ready to get going?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Exposing the Counterfeit Dealers]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_29(0x1B, 0x4, 0x10)
    SetChrPos(0xB, -124850, 0, 14920, 45)
    SetChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    SetMapObjFlags(0x1, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_7BF8 end

    def Function_30_9D83(): pass

    label("Function_30_9D83")

    ClearScenarioFlags(0x1, 4)
    ClearScenarioFlags(0x1, 5)
    ClearScenarioFlags(0x1, 6)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D96")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9FB9")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DD5")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_9FB4")

    label("loc_9DD5")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E09")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_9FB4")

    label("loc_9E09")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E3D")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_9FB4")

    label("loc_9E3D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E71")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_9FB4")

    label("loc_9E71")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EA5")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_9FB4")

    label("loc_9EA5")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9ED9")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_9FB4")

    label("loc_9ED9")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F0D")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_9FB4")

    label("loc_9F0D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F41")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_9FB4")

    label("loc_9F41")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F78")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    Jump("loc_9FB4")

    label("loc_9F78")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xEE), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9FAF")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 6)
    Jump("loc_9FB4")

    label("loc_9FAF")

    Jump("loc_9FB9")

    label("loc_9FB4")

    Jump("loc_9D96")

    label("loc_9FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_AD77")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-900, 1540, 13420, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A043")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0xEF, 300, 40, 13000, 0)
    SetChrPos(0x153, -900, 40, 11800, 0)
    Jump("loc_A16B")

    label("loc_A043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0B5")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x109, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_A16B")

    label("loc_A0B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A127")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x10A, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_A16B")

    label("loc_A127")

    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)

    label("loc_A16B")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "It looks to me like you've been hard at\x01",
            "work filling out your Combat Notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd like to record your information into\x01",
            "our database. Mind if I see it for a minute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWith pleasure.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1800)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Thank you very much. Here's your\x01",
            "notebook back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Let me gather your compensation...\x01",
            "Please accept this.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A34A")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "500 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x1.\x02",
        )
    )

    AddItemNumber(0x38E, 1)
    Jump("loc_A679")

    label("loc_A34A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3A5")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "1,000 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2.\x02",
        )
    )

    AddItemNumber(0x38E, 2)
    Jump("loc_A679")

    label("loc_A3A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A400")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "1,500 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3.\x02",
        )
    )

    AddItemNumber(0x38E, 3)
    Jump("loc_A679")

    label("loc_A400")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A45B")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "2,000 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x4.\x02",
        )
    )

    AddItemNumber(0x38E, 4)
    Jump("loc_A679")

    label("loc_A45B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4B6")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "2,500 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5.\x02",
        )
    )

    AddItemNumber(0x38E, 5)
    Jump("loc_A679")

    label("loc_A4B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A511")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "3,000 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x6.\x02",
        )
    )

    AddItemNumber(0x38E, 6)
    Jump("loc_A679")

    label("loc_A511")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A56C")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "3,500 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x7.\x02",
        )
    )

    AddItemNumber(0x38E, 7)
    Jump("loc_A679")

    label("loc_A56C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5C7")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "4,000 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x8.\x02",
        )
    )

    AddItemNumber(0x38E, 8)
    Jump("loc_A679")

    label("loc_A5C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A622")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "4,500 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x9.\x02",
        )
    )

    AddItemNumber(0x38E, 9)
    Jump("loc_A679")

    label("loc_A622")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A679")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "5,000 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10.\x02",
        )
    )

    AddItemNumber(0x38E, 10)

    label("loc_A679")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6B1")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2.\x02",
        )
    )

    AddItemNumber(0x395, 2)
    CloseMessageWindow()
    Jump("loc_A6E0")

    label("loc_A6B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A6E0")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x395, 1)
    CloseMessageWindow()

    label("loc_A6E0")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A843")

    ChrTalk(
        0x8,
        (
            "Don't forget to stop by once you've\x01",
            "collected more monster data, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks. We will.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A7B5")

    ChrTalk(
        0x102,
        "#0100FOf course. We'll see to it that we visit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A83E")

    label("loc_A7B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A7FC")

    ChrTalk(
        0x103,
        "#0200FNo need to worry. I will analyze more.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A83E")

    label("loc_A7FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A83E")

    ChrTalk(
        0x104,
        "#0300FYou better watch your backs, monsters!\x02",
    )

    CloseMessageWindow()

    label("loc_A83E")

    Jump("loc_ACF4")

    label("loc_A843")


    ChrTalk(
        0x8,
        (
            "Thank you so much for going out of your\x01",
            "way to gather this much data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You see, I asked all the other detectives\x01",
            "to help out, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...but I think the Special Support Section\x01",
            "were the only ones who took it seriously.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A98D")

    ChrTalk(
        0x104,
        (
            "#0300FYou know us. We're bustin' our\x01",
            "asses all over the place for work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA6F")

    label("loc_A98D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9FC")

    ChrTalk(
        0x102,
        (
            "#0100FWell, our jobs require us to traverse\x01",
            "all over Crossbell, so it's no big deal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA6F")

    label("loc_A9FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA6F")

    ChrTalk(
        0x103,
        (
            "#0200FWe travel all over Crossbell on a daily basis.\x01",
            "It's only natural we would collect data.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA6F")


    ChrTalk(
        0x101,
        (
            "#0000FWe also have our fair share of fights...\x02\x03",
            "Either way, the important thing is that\x01",
            "we were able to help you out, Rebecca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You really are a dependable bunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since you've already gathered more\x01",
            "than a sufficient amount of data for HQ,\x01",
            "this marks the end of my request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thank you all so much for seeing it\x01",
            "through to the end. You deserve a\x01",
            "special reward for this occasion.\x02",
        )
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
            "Received \x07\x02",
            "10,000 mira\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(10000)

    ChrTalk(
        0x8,
        (
            "I might still have some requests in the\x01",
            "near future. When that time comes,\x01",
            "I hope I can rely on the SSS again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOf course. Our doors are always open.\x02",
    )

    CloseMessageWindow()

    label("loc_ACF4")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD12")
    Jump("loc_AD4C")

    label("loc_AD12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD2F")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_AD4C")

    label("loc_AD2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD4C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_AD4C")

    label("loc_AD4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AD58")
    ClearScenarioFlags(0x1, 3)

    label("loc_AD58")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_AEED")

    label("loc_AD77")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE52")

    ChrTalk(
        0x8,
        (
            "Since you've already gathered a more\x01",
            "than a sufficient amount of data for HQ,\x01",
            "this marks the end of my request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope I can rely on the SSS again for\x01",
            "any requests I may have in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEED")

    label("loc_AE52")


    ChrTalk(
        0x8,
        (
            "It appears your Combat Notebook is\x01",
            "coming along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please come show it to me once you've\x01",
            "gathered a bit more data. I'll record it\x01",
            "in our database.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEED")

    Return()

    # Function_30_9D83 end

    def Function_31_AEEE(): pass

    label("Function_31_AEEE")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0003FWe don't have any business upstairs...\x02\x03",
            "#0000FAnd I think we'd all rather not get chewed out\x01",
            "by the vice commissioner, so let's not risk it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_31_AEEE end

    def Function_32_AF9C(): pass

    label("Function_32_AF9C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B78F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B45D")

    ChrTalk(
        0x101,
        (
            "#0005FYou know, this has been bothering\x01",
            "me for a while now...\x02\x03",
            "#0001FWhat exactly is this thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FYeah, it kinda caught my eye, too.\x02\x03",
            "#0300FThere's a bunch of juice and coffee\x01",
            "on display... What gives?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202FThis would be an orbal vending machine.\x01",
            "Is this the first time you have seen one?\x02\x03",
            "#0204FIf you insert mira coins into this slot, you\x01",
            "can choose the drink you want, and the\x01",
            "machine dispenses it accordingly.\x02\x03",
            "Since they were originally developed by\x01",
            "the Epstein Foundation, you would often\x01",
            "find them all over their research facilities...\x02\x03",
            "#0202FApparently, they are being tested out in\x01",
            "Crossbell as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWow, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FWere ya aware of these gadgets, Mademois-Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FNo. This is my first time seeing one, too.\x02\x03",
            "#0100FIt's hard to believe that all these inventions\x01",
            "by the Epstein Foundation are starting to\x01",
            "pop up all over Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FGranted, I have heard that they have some\x01",
            "incredibly influential and wealthy sponsors...\x02\x03",
            "#0200FPlease resort to coins if you intend on using it.\x01",
            "Bills are incompatible with this model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThanks for the heads-up.\x01",
            "(I'm kinda curious... I should\x01",
            "try it out at least once, right?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B787")

    label("loc_B45D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbal vending machine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0005FI think I'll come here to buy myself\x01",
            "a drink next time I'm thirsty.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5A1")

    ChrTalk(
        0x103,
        (
            "#0200FYes. This is a vending machine developed\x01",
            "by the Epstein Foundation.\x02\x03",
            "I believe Crossbell is one of the regions\x01",
            "designated to experiment with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B733")

    label("loc_B5A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B679")

    ChrTalk(
        0x102,
        (
            "#0100FThis is a vending machine developed\x01",
            "by the Epstein Foundation, isn't it?\x02\x03",
            "If I remember correctly, Tio said that\x01",
            "they've been placed all around Crossbell\x01",
            "for their experimental stage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B733")

    label("loc_B679")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B733")

    ChrTalk(
        0x104,
        (
            "#0300FA vending machine created by the\x01",
            "Epstein Foundation, eh?\x02\x03",
            "Accordin' to Tio Tot, the foundation has\x01",
            "been using Crossbell as a testing\x01",
            "ground for these suckers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B733")


    ChrTalk(
        0x101,
        (
            "#0000FLeave it to Crossbell to incorporate\x01",
            "a broad spectrum of new technology.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B787")

    SetScenarioFlags(0x95, 3)
    Jump("loc_B7A6")

    label("loc_B78F")

    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B7A6")

    TalkEnd(0xFF)
    Return()

    # Function_32_AF9C end

    SaveToFile()

Try(main)
