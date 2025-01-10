from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0410.bin",                # FileName
        "e0410",                    # MapName
        "e0410",                    # Location
        0x00A0,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 270, 1, 160, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0410",                  # 0
        "Young Man",              # 1
        "Girl",                   # 2
        "Man",                    # 3
        "Father",                 # 4
        "Mother",                 # 5
        "Boy",                    # 6
        "Merchant",               # 7
        "Woman",                  # 8
        "Carla",                  # 9
        "Old Man",                # 10
        "Old Lady",               # 11
        "Passenger",              # 12
        "Passenger",              # 13
        "Passenger",              # 14
        "Passenger",              # 15
        "Passenger",              # 16
        "Passenger",              # 17
        "SE制御",                 # 18
    ))

    AddCharChip((
        "chr/ch22002.itc",                   # 00
        "chr/ch22102.itc",                   # 01
        "chr/ch32302.itc",                   # 02
        "chr/ch21002.itc",                   # 03
        "chr/ch21102.itc",                   # 04
        "chr/ch21400.itc",                   # 05
        "chr/ch32202.itc",                   # 06
        "chr/ch33302.itc",                   # 07
        "chr/ch33202.itc",                   # 08
        "chr/ch21802.itc",                   # 09
        "chr/ch20702.itc",                   # 0A
        "chr/ch21902.itc",                   # 0B
        "chr/ch27602.itc",                   # 0C
        "chr/ch23702.itc",                   # 0D
        "chr/ch24400.itc",                   # 0E
        "chr/ch24202.itc",                   # 0F
        "chr/ch32402.itc",                   # 10
        "chr/ch21602.itc",                   # 11
        "chr/ch22202.itc",                   # 12
        "chr/ch20402.itc",                   # 13
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

    DeclNpc(-1899,   150,     4300,    0,    421,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-1899,   150,     5739,    180,  421,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(2200,    150,     3299,    180,  421,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-1600,   150,     750,     180,  421,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-1600,   150,     -750,    0,    421,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-3000,   0,       0,       225,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-1600,   150,     -3299,   0,    421,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(2200,    150,     -1799,   180,  421,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-1990,   150,     2970,    180,  469,  0x0, 2,   8,   0,   255, 255, 0,   31,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 24,  3.5,                   -7.849999904632568,    0.0,                   6.25,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3999999761581421,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.75,                 3.1399998664855957,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 26,  0.0,                   10.5,                  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -5.25,                 -0.0,                  1.0])
    DeclEvent(0x0000, 0, 27,  0.0,                   -10.0,                 0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.0,                   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 28,  0.0,                   9.5,                   0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.75,                 -0.0,                  1.0])

    ScpFunction((
        "Function_0_514",          # 00, 0
        "Function_1_5CC",          # 01, 1
        "Function_2_62F",          # 02, 2
        "Function_3_94C",          # 03, 3
        "Function_4_B8F",          # 04, 4
        "Function_5_D71",          # 05, 5
        "Function_6_10A6",         # 06, 6
        "Function_7_12E2",         # 07, 7
        "Function_8_14AF",         # 08, 8
        "Function_9_15B5",         # 09, 9
        "Function_10_17BD",        # 0A, 10
        "Function_11_19BE",        # 0B, 11
        "Function_12_1D77",        # 0C, 12
        "Function_13_209E",        # 0D, 13
        "Function_14_212E",        # 0E, 14
        "Function_15_24A0",        # 0F, 15
        "Function_16_2643",        # 10, 16
        "Function_17_27ED",        # 11, 17
        "Function_18_2968",        # 12, 18
        "Function_19_2D30",        # 13, 19
        "Function_20_30F8",        # 14, 20
        "Function_21_37A6",        # 15, 21
        "Function_22_3B64",        # 16, 22
        "Function_23_4129",        # 17, 23
        "Function_24_42D2",        # 18, 24
        "Function_25_43D6",        # 19, 25
        "Function_26_4D5E",        # 1A, 26
        "Function_27_4DCD",        # 1B, 27
        "Function_28_4E1D",        # 1C, 28
        "Function_29_4E9F",        # 1D, 29
        "Function_30_5396",        # 1E, 30
        "Function_31_551C",        # 1F, 31
        "Function_32_6EC3",        # 20, 32
        "Function_33_894A",        # 21, 33
        "Function_34_8983",        # 22, 34
        "Function_35_89CE",        # 23, 35
    ))


    def Function_0_514(): pass

    label("Function_0_514")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_554"),
        (1, "loc_560"),
        (2, "loc_56C"),
        (3, "loc_578"),
        (4, "loc_584"),
        (5, "loc_590"),
        (6, "loc_59C"),
        (SWITCH_DEFAULT, "loc_5A8"),
    )


    label("loc_554")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_560")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_56C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_578")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_584")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_590")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_59C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5CB")

    Return()

    # Function_0_514 end

    def Function_1_5CC(): pass

    label("Function_1_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5E0")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 32)
    Jump("loc_62E")

    label("loc_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_61C")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 17)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_62E")

    label("loc_61C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_62E")
    ClearScenarioFlags(0x5C, 2)
    SetScenarioFlags(0x0, 1)
    Event(0, 29)

    label("loc_62E")

    Return()

    # Function_1_5CC end

    def Function_2_62F(): pass

    label("Function_2_62F")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_66E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_93C")
    ModifyEventFlags(0, 0, 0x80)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_6B1"),
        (1, "loc_761"),
        (2, "loc_829"),
        (3, "loc_8CE"),
        (SWITCH_DEFAULT, "loc_920"),
    )


    label("loc_6B1")

    ModifyEventFlags(1, 1, 0x80)
    SetMapObjFlags(0x2, 0x10)
    OP_78(0x3, 0xF)
    SetChrPos(0xF, 0, 0, -9450, 0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x13, 0x9)
    SetChrChipByIndex(0x14, 0xA)
    SetChrSubChip(0x14, 0x1)
    SetChrChipByIndex(0x15, 0xB)
    SetChrChipByIndex(0x16, 0xC)
    SetChrPos(0x13, -2620, 150, 500, 180)
    SetChrPos(0x14, 1740, 150, 540, 180)
    SetChrPos(0x15, 2870, 150, 540, 180)
    SetChrPos(0x16, 2290, 150, 5520, 180)
    EndChrThread(0x14, 0xFF)
    Jump("loc_920")

    label("loc_761")

    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    SetMapObjFlags(0x2, 0x10)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x2)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x13, 0xD)
    SetChrChipByIndex(0x14, 0xE)
    SetChrChipByIndex(0x15, 0xF)
    SetChrChipByIndex(0x16, 0x7)
    SetChrChipByIndex(0x17, 0x10)
    SetChrChipByIndex(0x18, 0x2)
    SetChrPos(0x13, -1680, 150, -2120, 180)
    SetChrPos(0x14, -3070, 0, -2450, 270)
    SetChrPos(0x15, 2430, 150, -4380, 180)
    SetChrPos(0x16, 2390, 150, 1950, 0)
    SetChrPos(0x17, 2390, 150, 3090, 180)
    SetChrPos(0x18, -2260, 150, 5600, 180)
    BeginChrThread(0x14, 0, 0, 0)
    Jump("loc_920")

    label("loc_829")

    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    SetMapObjFlags(0x2, 0x10)
    ModifyEventFlags(1, 3, 0x80)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x2)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrChipByIndex(0x14, 0x12)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x13)
    SetChrChipByIndex(0x16, 0x3)
    SetChrPos(0x13, 1950, 150, -2080, 180)
    SetChrPos(0x14, 2710, 150, -1990, 180)
    SetChrPos(0x15, 2210, 0, 4300, 0)
    SetChrPos(0x16, 2280, 0, 5650, 180)
    EndChrThread(0x14, 0xFF)
    Jump("loc_920")

    label("loc_8CE")

    ModifyEventFlags(1, 2, 0x80)
    OP_70(0x2, 0x0)
    OP_78(0x3, 0xF)
    SetChrPos(0xF, 0, 0, 8800, 0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_920")

    label("loc_920")

    BeginChrThread(0x101, 3, 0, 33)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0xF0, 0x0, 0x0, 0x20)

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_94B")
    Sound(450, 1, 100, 0)

    label("loc_94B")

    Return()

    # Function_2_62F end

    def Function_3_94C(): pass

    label("Function_3_94C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E0")
    Jump("loc_A2A")

    label("loc_9E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A00")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2A")

    label("loc_A00")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A20")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2A")

    label("loc_A20")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A2A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_AC9")

    ChrTalk(
        0xFE,
        "How impatient can she get?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shouldn't we be taking it easy instead\x01",
            "of stressing ourselves out?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B87")

    label("loc_AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_B54")

    ChrTalk(
        0x8,
        (
            "We're going on a trip to\x01",
            "Erebonia from Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hahaha, I can't wait to tour\x01",
            "all the Empire's popular spots.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B87")

    label("loc_B54")

    Call(0, 18)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B87")
    Call(0, 23)

    label("loc_B87")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_94C end

    def Function_4_B8F(): pass

    label("Function_4_B8F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C23")
    Jump("loc_C6D")

    label("loc_C23")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C43")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C6D")

    label("loc_C43")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C63")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C6D")

    label("loc_C63")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C6D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_CE6")

    ChrTalk(
        0xFE,
        (
            "Hey. Why hasn't the train left yet?\x01",
            "Can you not hurry it up?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D69")

    label("loc_CE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_D36")

    ChrTalk(
        0x9,
        (
            "That silly inspection is over,\x01",
            "isn't it? If so, go away!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D69")

    label("loc_D36")

    Call(0, 18)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D69")
    Call(0, 23)

    label("loc_D69")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_B8F end

    def Function_5_D71(): pass

    label("Function_5_D71")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E05")
    Jump("loc_E4F")

    label("loc_E05")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E25")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E4F")

    label("loc_E25")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E45")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E4F")

    label("loc_E45")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E4F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_FC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_E92")
    Call(0, 25)
    Jump("loc_FC1")

    label("loc_E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F0D")

    ChrTalk(
        0xFE,
        (
            "Oooh, I'm looking forward to seeing the\x01",
            "beautiful scenery during the ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Can't we leave already?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FC1")

    label("loc_F0D")


    ChrTalk(
        0xFE,
        (
            "Oooh, I can't wait to see the\x01",
            "beautiful scenery during the ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The deep green foliage of the\x01",
            "Knox Forest is especially charming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Can't the train leave already?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_FC1")

    Jump("loc_109E")

    label("loc_FC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_106B")

    ChrTalk(
        0xA,
        (
            "Haha, anyway, I'm looking forward\x01",
            "to when we finally leave the station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The views from the train's windows\x01",
            "are a sight to see, trust me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109E")

    label("loc_106B")

    Call(0, 19)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109E")
    Call(0, 23)

    label("loc_109E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_D71 end

    def Function_6_10A6(): pass

    label("Function_6_10A6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_113A")
    Jump("loc_1184")

    label("loc_113A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_115A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1184")

    label("loc_115A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_117A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1184")

    label("loc_117A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1184")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_11FA")

    ChrTalk(
        0xFE,
        (
            "Haha, that liveliness of his reminds me\x01",
            "of a certain someone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DA")

    label("loc_11FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_120F")
    Call(0, 20)
    Jump("loc_12DA")

    label("loc_120F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_12A7")

    ChrTalk(
        0xB,
        (
            "It's been a fairly lengthy\x01",
            "journey from Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*yawn* Maybe I should try to take a\x01",
            "power nap before the train disembarks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DA")

    label("loc_12A7")

    Call(0, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12DA")
    Call(0, 23)

    label("loc_12DA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_10A6 end

    def Function_7_12E2(): pass

    label("Function_7_12E2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1376")
    Jump("loc_13C0")

    label("loc_1376")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1396")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13C0")

    label("loc_1396")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13C0")

    label("loc_13B6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13C0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_1411")

    ChrTalk(
        0xFE,
        "*sigh* What's his issue?\x02",
    )

    CloseMessageWindow()
    Jump("loc_14A7")

    label("loc_1411")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_1426")
    Call(0, 20)
    Jump("loc_14A7")

    label("loc_1426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_1474")

    ChrTalk(
        0xC,
        (
            "I'm trying to calm him down,\x01",
            "but he just won't listen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A7")

    label("loc_1474")

    Call(0, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A7")
    Call(0, 23)

    label("loc_14A7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_12E2 end

    def Function_8_14AF(): pass

    label("Function_8_14AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_1536")

    ChrTalk(
        0xFE,
        (
            "*sniff'* *sniff*...\x01",
            "That man was able to come from\x01",
            "one of the front cars...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's not fair...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B1")

    label("loc_1536")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_154B")
    Call(0, 20)
    Jump("loc_15B1")

    label("loc_154B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_157E")

    ChrTalk(
        0xD,
        "When are we gonna leave...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B1")

    label("loc_157E")

    Call(0, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15B1")
    Call(0, 23)

    label("loc_15B1")

    TalkEnd(0xFE)
    Return()

    # Function_8_14AF end

    def Function_9_15B5(): pass

    label("Function_9_15B5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1649")
    Jump("loc_1693")

    label("loc_1649")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1669")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1693")

    label("loc_1669")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1689")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1693")

    label("loc_1689")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1693")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_1749")

    ChrTalk(
        0xFE,
        (
            "I need to take a minute\x01",
            "to cool my head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until I learn to keep my composure,\x01",
            "my trade career will drown in blunders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B5")

    label("loc_1749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_1782")

    ChrTalk(
        0xE,
        "Oh, hello. Do you need something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_17B5")

    label("loc_1782")

    Call(0, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B5")
    Call(0, 23)

    label("loc_17B5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_15B5 end

    def Function_10_17BD(): pass

    label("Function_10_17BD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1851")
    Jump("loc_189B")

    label("loc_1851")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1871")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_189B")

    label("loc_1871")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1891")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_189B")

    label("loc_1891")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_189B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_192B")

    ChrTalk(
        0xFE,
        "*sigh* Woe is life...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where's my rich knight in shining\x01",
            "armor when I need him?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B6")

    label("loc_192B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1983")
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xF,
        "*sigh* Men are all the same.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Dumb...stupid...idiotic...\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B6")

    label("loc_1983")

    Call(0, 22)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19B6")
    Call(0, 23)

    label("loc_19B6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_17BD end

    def Function_11_19BE(): pass

    label("Function_11_19BE")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_19D9"),
        (1, "loc_1B7B"),
        (2, "loc_1C0A"),
        (SWITCH_DEFAULT, "loc_1D76"),
    )


    label("loc_19D9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A6D")
    Jump("loc_1AB7")

    label("loc_1A6D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A8D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AB7")

    label("loc_1A8D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AAD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AB7")

    label("loc_1AAD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AB7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I'm returning home to Altair\x01",
            "after a nice, short vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My wife and kid are waiting for me!\x01",
            "I can't wait to see their faces again. ♪\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1D76")

    label("loc_1B7B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "You sure are impatient.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We still have a long way to go before we\x01",
            "reach the Republican capital, so you\x01",
            "should relax a bit.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1D76")

    label("loc_1C0A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C9E")
    Jump("loc_1CE8")

    label("loc_1C9E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1CBE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CE8")

    label("loc_1CBE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CDE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CE8")

    label("loc_1CDE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CE8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Ored State is my homeland.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*cough* You see, that's where\x01",
            "I'm taking my grandchild.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1D76")

    label("loc_1D76")

    Return()

    # Function_11_19BE end

    def Function_12_1D77(): pass

    label("Function_12_1D77")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1D92"),
        (1, "loc_1EBB"),
        (2, "loc_1F1B"),
        (SWITCH_DEFAULT, "loc_209D"),
    )


    label("loc_1D92")

    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E29")
    Jump("loc_1E73")

    label("loc_1E29")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E49")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E73")

    label("loc_1E49")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E69")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E73")

    label("loc_1E69")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E73")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Whoa, incredible!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x1)
    TalkEnd(0xFE)
    Jump("loc_209D")

    label("loc_1EBB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*snap* *snap*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally, our big railway trip!\x01",
            "I gotta capture every memory!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_209D")

    label("loc_1F1B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FAF")
    Jump("loc_1FF9")

    label("loc_1FAF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FCF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FF9")

    label("loc_1FCF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FEF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FF9")

    label("loc_1FEF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FF9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "My grandpa's hometown\x01",
            "sounds super awesome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He couldn't stop talking about\x01",
            "how huge the farms are there!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_209D")

    label("loc_209D")

    Return()

    # Function_12_1D77 end

    def Function_13_209E(): pass

    label("Function_13_209E")

    TalkBegin(0xFE)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_20BC"),
        (1, "loc_20EA"),
        (2, "loc_2102"),
        (SWITCH_DEFAULT, "loc_212A"),
    )


    label("loc_20BC")


    ChrTalk(
        0xFE,
        "Start behaving, right this instant!\x02",
    )

    CloseMessageWindow()
    Jump("loc_212A")

    label("loc_20EA")


    ChrTalk(
        0xFE,
        "Zzz... Zzz...\x02",
    )

    CloseMessageWindow()
    Jump("loc_212A")

    label("loc_2102")


    ChrTalk(
        0xFE,
        (
            "Hahahaha!\x01",
            "I'm sorry, I can't!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212A")

    label("loc_212A")

    TalkEnd(0xFE)
    Return()

    # Function_13_209E end

    def Function_14_212E(): pass

    label("Function_14_212E")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2149"),
        (1, "loc_22D8"),
        (2, "loc_2455"),
        (SWITCH_DEFAULT, "loc_249F"),
    )


    label("loc_2149")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21DD")
    Jump("loc_2227")

    label("loc_21DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21FD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2227")

    label("loc_21FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_221D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2227")

    label("loc_221D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2227")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "That inspection officer was eyeing\x01",
            "everyone up and down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know it's a routine thing,\x01",
            "but it still grinds my gears.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_249F")

    label("loc_22D8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_236C")
    Jump("loc_23B6")

    label("loc_236C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_238C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23B6")

    label("loc_238C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23AC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23B6")

    label("loc_23AC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23B6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "When you talk Calvard, you have\x01",
            "to mention their gourmet dishes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Of course, their hot springs, too!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_249F")

    label("loc_2455")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Wahahahaha! I can't get\x01",
            "enough of those, I tell you what!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_249F")

    label("loc_249F")

    Return()

    # Function_14_212E end

    def Function_15_24A0(): pass

    label("Function_15_24A0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2534")
    Jump("loc_257E")

    label("loc_2534")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2554")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_257E")

    label("loc_2554")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2574")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_257E")

    label("loc_2574")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_257E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_25BE"),
        (1, "loc_25C3"),
        (2, "loc_2636"),
        (SWITCH_DEFAULT, "loc_263B"),
    )


    label("loc_25BE")

    Jump("loc_263B")

    label("loc_25C3")


    ChrTalk(
        0xFE,
        (
            "I'm sooo excited for\x01",
            "this girls-only trip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trust me, my husband would\x01",
            "have been a massive buzzkill.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263B")

    label("loc_2636")

    Jump("loc_263B")

    label("loc_263B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_24A0 end

    def Function_16_2643(): pass

    label("Function_16_2643")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26D7")
    Jump("loc_2721")

    label("loc_26D7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26F7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2721")

    label("loc_26F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2717")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2721")

    label("loc_2717")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2721")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2761"),
        (1, "loc_2766"),
        (2, "loc_27E0"),
        (SWITCH_DEFAULT, "loc_27E5"),
    )


    label("loc_2761")

    Jump("loc_27E5")

    label("loc_2766")


    ChrTalk(
        0xFE,
        (
            "This place is pretty glum... Makes\x01",
            "it sort of hard to read in peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe I should move to a window seat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_27E5")

    label("loc_27E0")

    Jump("loc_27E5")

    label("loc_27E5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_2643 end

    def Function_17_27ED(): pass

    label("Function_17_27ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3750, 1000, -7850, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 3750, 0, -7850, 270)
    OP_68(0, 1000, -7850, 3000)

    def lambda_284E():
        OP_97(0x101, 0xFFFFF15A, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_284E)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Fade(500)
    OP_68(0, 1000, 5000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    OP_68(0, 1000, -7850, 7000)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#0001FThere sure are a lot of travelers\x01",
            "here. Can't say I'm surprised.\x02\x03",
            "#0003FI need to make sure to be polite\x01",
            "while questioning each person.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x9, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_17_27ED end

    def Function_18_2968(): pass

    label("Function_18_2968")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1400, 1000, 4980, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16540, 0)
    SetChrPos(0x101, -150, 0, 5000, 270)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x9, 0x1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse me, I'm one of the\x01",
            "assistant inspectors...\x02\x03",
            "I apologize for the inconvenience, but\x01",
            "would you mind me checking your\x01",
            "luggage and entry papers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAh, an inspection?\x01",
            "I suppose it's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PWhaaat? No way!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)

    ChrTalk(
        0x9,
        (
            "#11PI have all my panties\x01",
            "in my luggage, y'know...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        "#5PHmm, good point.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    ChrTalk(
        0x8,
        "#5PSorry, but you heard the lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FNo, hold on! You can't just\x01",
            "refuse. It doesn't work like that!\x02\x03",
            "#0003FIt's regulation, so please work with me.\x01",
            "I'll show the utmost consideration\x01",
            "when inspecting your delicates.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        "#5PSo he says.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYeah. You better, mister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(Th-This is harder than it looks...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x9, 0x1)
    Sleep(2000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0000FAll your luggage and carry-ons\x01",
            "look good and follow our regulations.\x02\x03",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYou're welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PHmph, now scram!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_29(0x9, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_18_2968 end

    def Function_19_2D30(): pass

    label("Function_19_2D30")

    EventBegin(0x0)
    Fade(500)
    OP_68(1440, 1000, 3000, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 800, 0, 2500, 45)
    SetChrSubChip(0xA, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0000FPardon me, I'm an assistant inspector.\x02\x03",
            "I apologize for the inconvenience, but\x01",
            "would you mind me checking your\x01",
            "luggage and entry papers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PAh, yes, of course.\x01",
            "Just one moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PHehehe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FUmm...are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12POh, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PIt's just, the deep green foliage\x01",
            "of the Knox Forest is incredibly\x01",
            "charming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PKnowing that, I couldn't help but\x01",
            "feel a bit giddy before departing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FUh, sounds like you\x01",
            "have a nice hobby there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12POops, I accidentally wasted your\x01",
            "time, didn't I? An inspection, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FOh... Yes, that's right.\x02\x03",
            "#0000FIf you'll excuse me, then...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0000FAll right, your luggage and\x01",
            "papers look good to go.\x02\x03",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PNo, no. Thank YOU for your dedication.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PHehe, now back to my\x01",
            "eager anticipation...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xA, 0x0)
    OP_29(0x9, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_19_2D30 end

    def Function_20_30F8(): pass

    label("Function_20_30F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_338C")
    EventBegin(0x0)
    Fade(500)
    OP_68(-1560, 1000, 0, 0)
    MoveCamera(320, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17360, 0)
    SetChrPos(0x101, -150, 0, 0, 270)
    SetChrSubChip(0xB, 0x2)
    SetChrSubChip(0xC, 0x1)
    SetChrSubChip(0xD, 0x0)
    OP_4B(0xD, 0xFF)
    TurnDirection(0xD, 0x101, 0)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#5PMom...Mom! Can I go explore\x01",
            "the rest of the train cars?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PNo, you can't! Now sit still\x01",
            "until the inspections end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PListen to your mother, son. You\x01",
            "don't want to annoy the inspector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PWhaaaat? But that guy sitting over\x01",
            "there came from the car in front of\x01",
            "ours, so why can't I go, too?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000F(The front train car...? Could that be\x01",
            "the one Mr. Quattro's inspecting?)\x02\x03",
            "(He might have just had some\x01",
            "business with the conductor.)\x02\x03",
            "#0005F(No, wait a second. Maybe\x01",
            "he changed cars after the\x01",
            "inspections began...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 0)
    Jump("loc_378F")

    label("loc_338C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1560, 1000, 0, 0)
    MoveCamera(320, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17360, 0)
    SetChrPos(0x101, -150, 0, 0, 270)
    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0xD, 0x0)
    OP_4B(0xD, 0xFF)
    TurnDirection(0xD, 0x101, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse me, I'm an assistant inspector.\x02\x03",
            "I apologize for the inconvenience, but\x01",
            "would you mind me checking your\x01",
            "luggage and entry papers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAn inspector, are you?\x01",
            "Hmm, very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PHeeey, why haven't\x01",
            "we left yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PWaiting is b o r i n g.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PSweet Aidios, will this child\x01",
            "ever learn patience...?\x01",
            "Pardon my son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FAh, it's no big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FSorry, it'll be a little while longer.\x02\x03",
            "Can you be a good kid for\x01",
            "just a bit longer while we\x01",
            "finish up our job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PI gueeeess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003F(...With that settled, I should\x01",
            "try to wrap this up quickly.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0000FYour luggage and papers are all\x01",
            "up-to-date and follow regulations.\x02\x03",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PGood to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PMister, can you pinky promise me\x01",
            "you'll hurry and let the train leave?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x1)

    ChrTalk(
        0xC,
        (
            "#6PHey, you can't just...! *sigh*\x01",
            "What am I going to do with you...?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0x6)

    label("loc_378F")

    OP_5A()
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xD, 0xE1, 0x0)
    OP_4C(0xD, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_20_30F8 end

    def Function_21_37A6(): pass

    label("Function_21_37A6")

    EventBegin(0x0)
    Fade(500)
    OP_68(-780, 1000, -2950, 0)
    MoveCamera(305, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17320, 0)
    SetChrPos(0x101, -150, 0, -2500, 225)
    SetChrSubChip(0xE, 0x2)
    OP_0D()

    ChrTalk(
        0xE,
        "#5POh? An inspector, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PHow am I supposed to buy that?\x01",
            "Proof! I demand to see proof!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FU-Uh, I don't...\x01",
            "(What do I do?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#0005FWait, this should work.\x01",
            "Take a look at this.\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed the passenger\x01",
            "his Detective Notebook.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12P#0000FI'm from the Crossbell Police Department,\x01",
            "Special Support Section. We're assisting\x01",
            "with inspections today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PPolice? Guess that checks out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThough, doing this is kind of misleading.\x01",
            "Well, whatever. Just get it over with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FTh-Thanks.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0000FDone. Your luggage and\x01",
            "papers look like they're all\x01",
            "valid and up-to-date.\x02\x03",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PHmph, skip the pleasantries.\x01",
            "Just hurry this inspection up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PI'm kind of in a rush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006FY-Yeah. Not too much longer.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xE, 0x0)
    OP_29(0x9, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_21_37A6 end

    def Function_22_3B64(): pass

    label("Function_22_3B64")

    EventBegin(0x0)
    Fade(500)
    OP_68(1430, 1000, -2180, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16540, 0)
    SetChrPos(0x101, 800, 0, -2500, 45)
    SetChrSubChip(0xF, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0000FPardon me, I'm an assistant inspector.\x02\x03",
            "I apologize for the inconvenience, but\x01",
            "would you mind me checking your\x01",
            "luggage and entry papers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PInspector? Not everyday you\x01",
            "see one in such a casual getup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PAnyway, what's the issue?\x01",
            "You find it strange that a woman\x01",
            "is traveling alone, is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FWhat? N-No, that's not...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PFor your information, I wanted nothing\x01",
            "more than to go with my boyfriend!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PBut since he dumped me out of the blue,\x01",
            "I had no choice but to come alone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PBut that won't stop me! I'm going to find\x01",
            "myself a rich, noble boyfriend somewhere\x01",
            "in the Empire!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0011F(Uh...I didn't mean to trigger this story.)\x02\x03",
            "#0006F(Well, nothing I can do about it. I'll just listen\x01",
            "to her while I finish up the inspection...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "#12PYou get it, don't you? Wasn't that,\x01",
            "like, so rude of him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0012FY-Yeah, a real jerk...\x02\x03",
            "#0000FUm, by the way, your luggage and papers\x01",
            "are all good and follow our regulations.\x02\x03",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FY-You okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12PNo, it's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PIt's just...it was refreshing\x01",
            "spilling my heart out to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PI can't remember the last time\x01",
            "someone listened to my problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#12PSay...if you want to, why don't\x01",
            "we run away to Erebonia toge--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0011FS-Sorry, I have a job to do.\x01",
            "It was nice meeting you!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xF, 0x0)
    OP_29(0x9, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_22_3B64 end

    def Function_23_4129(): pass

    label("Function_23_4129")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1000, -7350, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 0, 0, -7350, 180)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#0006F*sigh* That should be the\x01",
            "last of the passengers.\x02\x03",
            "#0000FI didn't notice anything suspicious,\x01",
            "so I should regroup with the others\x01",
            "and report to Mr. Quattro.\x02\x03",
            "#0003F...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0003FIt was kinda nerve-racking doing\x01",
            "these inspections for the first time.\x02\x03",
            "#0001FI didn't overlook anyone, did I?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x9, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_23_4129 end

    def Function_24_42D2(): pass

    label("Function_24_42D2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_437C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[End inspection and leave]\x01",      # 0
            "[Cancel]\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4361")
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_4377")

    label("loc_4361")

    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)

    label("loc_4377")

    Jump("loc_43D5")

    label("loc_437C")


    ChrTalk(
        0x101,
        (
            "#0001FThe inspection isn't over.\x01",
            "I can't leave the train yet.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)

    label("loc_43D5")

    Return()

    # Function_24_42D2 end

    def Function_25_43D6(): pass

    label("Function_25_43D6")

    EventBegin(0x0)
    Fade(500)
    OP_68(1440, 1000, 3000, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 800, 0, 2500, 45)
    SetChrSubChip(0xA, 0x2)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#12PAh, I can hardly wait... I can\x01",
            "feel the scenery calling for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PShouldn't we have left by now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FExcuse me, sir.\x01",
            "Do you have a minute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12POh, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PI thought the inspection\x01",
            "already ended?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FIt had, but there's something\x01",
            "bothering me.\x02\x03",
            "#0001FWith your permission, may\x01",
            "I redo the inspection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PSure, I don't mind.\x01",
            "Forget to check something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PHere's my luggage\x01",
            "and entry papers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FOh, no. I won't be the one\x01",
            "conducting the inspection.\x02\x03",
            "#0001FI'm planning on asking\x01",
            "the official inspector,\x01",
            "Mr. Quattro, to do it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12PQu-Quattro...why? Aren't you more than\x01",
            "capable of doing a silly little inspection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0003FSo, you do know him.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#12PAh! N-No, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FQuattro laid down some ground rules before\x01",
            "we began the inspections.\x02\x03",
            "#0001FOne that stood out to me was, 'You may not\x01",
            "move to another car during inspections.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PO-Of course I know that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PAre you implying I broke that rule?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FYes, I am. Hate to break it to\x01",
            "you, but I have a witness.\x02\x03",
            "That rowdy boy, sitting right over there,\x01",
            "saw you entering from the car up front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PWh-What?! That's preposterous...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PTh-This has got to be some kind of\x01",
            "mistake, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FI'm sure we could confirm the boy's statement\x01",
            "if we asked the train conductor.\x02\x03",
            "#0001FThe question still stands... Why would you\x01",
            "transfer cars?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FIf things went according to plan, you would\x01",
            "have been inspected by Quattro.\x02\x03",
            "But, in spite of the rules, you snuck away\x01",
            "onto this train car...\x02\x03",
            "#0001FThe only logical conclusion is that you didn't\x01",
            "want Quattro to see you.\x02\x03",
            "Am I wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12P...Ah...aaaah...!\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12PP-Please! I'm begging you!\x01",
            "Overlook this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PI just wanted to have a fun, little trip!\x01",
            "Yeah, that's all it is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PL-Look, you said my papers are good\x01",
            "to go, didn't you? If that's the case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FThen it should be fine if Quattro double-checks\x01",
            "them, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xFFFF)

    ChrTalk(
        0xA,
        "#12PWh-What?! N-No, please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FI don't know all the details...\x02\x03",
            "#0001FBut as long as I'm working as an assistant inspector,\x01",
            "I can't ignore any suspicious behavior.\x02\x03",
            "#0003FI'll need you to come with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12PFine...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x9, 0x1, 0xB)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_43D6 end

    def Function_26_4D5E(): pass

    label("Function_26_4D5E")

    EventBegin(0x1)
    OP_D0(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Call(0, 2)
    SetChrPos(0x0, 100, 0, -8640, 0)
    OP_68(100, 1000, -8640, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DCA")
    Call(0, 30)
    Jump("loc_4DCC")

    label("loc_4DCA")

    EventEnd(0x4)

    label("loc_4DCC")

    Return()

    # Function_26_4D5E end

    def Function_27_4DCD(): pass

    label("Function_27_4DCD")

    EventBegin(0x1)
    OP_D0(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Call(0, 2)
    SetChrPos(0x0, 90, 0, 8340, 180)
    OP_68(90, 1000, 8340, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    EventEnd(0x4)
    Return()

    # Function_27_4DCD end

    def Function_28_4E1D(): pass

    label("Function_28_4E1D")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FLet's try to convince Carla to return.\x02\x03",
            "If we take too long, we'll end\x01",
            "up arriving in Altair.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 10, 0, 7210, 180)
    EventEnd(0x4)
    Return()

    # Function_28_4E1D end

    def Function_29_4E9F(): pass

    label("Function_29_4E9F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(280, 1000, 2990, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1800, 0, -7650, 270)
    SetChrPos(0x102, 1800, 0, -8780, 270)
    SetChrPos(0x103, 2950, 0, -8780, 270)
    SetChrPos(0x104, 2950, 0, -7650, 270)
    BeginChrThread(0x101, 3, 0, 33)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0xF0, 0x0, 0x0, 0x20)
    FadeToBright(2000, 0)
    OP_0D()
    OP_68(760, 1000, -4250, 4000)
    Sleep(4300)
    Fade(500)
    OP_68(1750, 1000, -7500, 0)
    SetCameraDistance(16500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#6P#0200FWe cut that close.\x02",
    )

    CloseMessageWindow()

    def lambda_4F9D():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F9D)
    Sleep(15)

    def lambda_4FAD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4FAD)
    Sleep(12)

    def lambda_4FBD():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FBD)
    Sleep(20)

    def lambda_4FCD():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4FCD)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#0106FI wonder if we'll get in trouble for not\x01",
            "following protocol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FOfficers should be allowed to board trains\x01",
            "during emergencies, so we don't have to\x01",
            "worry about that.\x02\x03",
            "#0001FHowever, the problem remains...\x01",
            "What do we do now?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#0105FThe plan was to convince Carla\x01",
            "to return home, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0303FYeah, well, we can't ride on this train\x01",
            "forever, y'know.\x02\x03",
            "#0301FAnd we still gotta drop off those drugs\x01",
            "at St. Ursula, ain't that right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 400)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#6P#0203FThat's true.\x02\x03",
            "#0200FWe have not come this far to simply give up.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    ChrTalk(
        0x101,
        (
            "#5P#0003FYeah, I know. The next stop is Altair,\x01",
            "located at the western edge of Calvard...\x02\x03",
            "#0001FWe should have about 30 minutes.\x02\x03",
            "Until then, let's keep trying to persuade\x01",
            "her to come home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0300FRoger. I'm no quitter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0108FAll right. I hope our words can get\x01",
            "through to her...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2480, 0, -8200, 270)
    OP_29(0x2D, 0x1, 0xC)
    EventEnd(0x5)
    Return()

    # Function_29_4E9F end

    def Function_30_5396(): pass

    label("Function_30_5396")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(100, 1000, -8640, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17060, 0)
    SetChrPos(0x101, 830, 0, -7830, 0)
    SetChrPos(0x102, -300, 0, -7830, 0)
    SetChrPos(0x103, 830, 0, -8680, 0)
    SetChrPos(0x104, -300, 0, -8680, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(-2760, 1000, 3450, 2500)
    Sleep(2500)

    ChrTalk(
        0x102,
        "#0105F(It's Carla...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300F(Hey, finally found her.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(Now we just have to persuade\x01",
            "her to return home.)\x02\x03",
            "(The odds of her listening\x01",
            "to reason still seem slim...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 100, 0, -8640, 0)
    OP_29(0x2D, 0x1, 0xD)
    EventEnd(0x5)
    Return()

    # Function_30_5396 end

    def Function_31_551C(): pass

    label("Function_31_551C")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_68(-1200, 700, 2970, 0)
    MoveCamera(332, 25, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23510, 0)
    SetChrPos(0x101, -280, 0, 2800, 286)
    SetChrPos(0x102, -430, 0, 1750, 286)
    SetChrPos(0x103, 590, 0, 1300, 286)
    SetChrPos(0x104, 740, 0, 2430, 286)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x10,
        (
            "#5PDon't tell me Marsha\x01",
            "missed the train...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PI guess I'm all alone now...\x01",
            "Can I handle this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FLong time no see, Carla.\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    ChrTalk(
        0x10,
        "#5PElie, what are you...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)

    ChrTalk(
        0x10,
        (
            "#5PI-I mean, what a coincidence,\x01",
            "running into you here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PAre these your friends?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5POh, are you planning to spend\x01",
            "a day or two in the Republic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0109FHaha, well, Carla...\x01",
            "(How should I start this...?)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Actually, we came to take you home]\x01",      # 0
            "[We're on a trip to the Republic]\x01",         # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A54")
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x10,
        (
            "#5PD-Don't tell me that Father\x01",
            "put you up to this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PH-How wrong I was! Those aren't friends;\x01",
            "those are your colleagues, aren't they?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    ChrTalk(
        0x10,
        (
            "#5PHmph, your efforts are in vain.\x01",
            "I shall never return home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006F(Guess being blunt was a mistake.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0303F(Tell me 'bout it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106F(I'm sorry, everyone. I might have\x01",
            "made her even more stubborn.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FBe that as it may, why exactly did\x01",
            "you run from home in the first place?\x02\x03",
            "#0200FJudging by the note you left, it is\x01",
            "obvious that you had some motive\x01",
            "behind it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C17")

    label("loc_5A54")

    OP_2C(0x2D, 0x1)

    ChrTalk(
        0x102,
        (
            "#6P#0100FYes, exactly. I thought it'd be fun to see\x01",
            "the Republic's national orchestra with\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PReally? Then we can accompany\x01",
            "each other until we arrive at the\x01",
            "Republican capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PI'm so thankful I ran into you, Elie.\x01",
            "Truth be told, I'm feeling a bit down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PAfter all, I'm alone on\x01",
            "this giant train and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003F(All right, it looks like we've\x01",
            "lowered her guard.)\x02\x03",
            "#0000FWhy exactly are you here, Carla?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C17")


    ChrTalk(
        0x10,
        "#5PW-Well, it's a long story...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    ChrTalk(
        0x10,
        (
            "#5PMy father is always ordering me around,\x01",
            "filling my life with rules and more rules...\x01",
            "Ones he doesn't even respect himself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PAnd this morning was a\x01",
            "perfect example of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PI will never forgive him\x01",
            "for what he did...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0105FWhich was...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0005FWhatever it was, it sounds bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PAfter breakfast, he walked into\x01",
            "my room without knocking!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        "#12P#0305FHuh...? That's it?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    ChrTalk(
        0x10,
        (
            "#5POf course it's not just that!\x01",
            "What if I was changing?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x0)
    Sleep(200)

    ChrTalk(
        0x10,
        (
            "#5PMore importantly, Father's the\x01",
            "one always lecturing me about\x01",
            "how I should always knock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PAnd even though he throws\x01",
            "a fit when I forget to do so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PThis morning, he calmly strode into my room,\x01",
            "commanding me to do this and that, and to\x01",
            "attend a dinner party in the evening, and...and...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PHe pries into every single small\x01",
            "detail of my private life... It's like\x01",
            "he can't do anything BUT that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203F(I can relate with how she feels, but this is\x01",
            "nothing more than a misunderstanding\x01",
            "between father and daughter.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0003F(Hmm, how should we handle this...?)\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Your father is to blame]\x01",             # 0
            "[Did you try locking your door?]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_620F")
    OP_2C(0x2D, 0x1)

    ChrTalk(
        0x101,
        (
            "#11P#0006FThen your father's in the wrong.\x01",
            "I can sympathize with you, Carla.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    ChrTalk(
        0x10,
        "#5PY-You think so, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PHmph, I knew leaving home\x01",
            "was the right decision.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6375")

    label("loc_620F")


    ChrTalk(
        0x101,
        (
            "#11P#0006FUmm, why don't you start\x01",
            "locking the door to your room?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1600, 0x2C, 0x2F, 0x96, 0x1)
    Sound(25, 0, 100, 0)
    SetChrSubChip(0x10, 0x1)
    Sleep(1200)

    ChrTalk(
        0x10,
        (
            "#5PThat's not the point! My point is that\x01",
            "I can't forgive him for being the only\x01",
            "one allowed to be selfish in that house!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PHmph, I've heard enough. I'm\x01",
            "going to Calvard, and that's that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PFather can do whatever\x01",
            "he wants, for all I care!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6375")

    SetChrSubChip(0x10, 0x0)
    Sleep(300)
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    ChrTalk(
        0x10,
        (
            "#5PStill, it's the first time\x01",
            "I've ever left Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P*sigh* The only reason I decided to go\x01",
            "through with this plan was because\x01",
            "Marsha said she'd accompany me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303F(I think I get the gist of this mess,\x01",
            "but she still looks hesitant, right?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0108F(She never had the strongest\x01",
            "heart to begin with...)\x02\x03",
            "(Sure, she ran out of the house in\x01",
            "a hurry...but I bet with every step,\x01",
            "she became more and more uneasy.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003F(Then she should almost\x01",
            "be at her breaking point...)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[It's dangerous to travel alone]\x01",        # 0
            "[Your father is worried about you]\x01",      # 1
            "[Your maid is worried sick]\x01",             # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE0")
    OP_2C(0x2D, 0x5)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x10, 0x1)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#5PI was wondering why I still\x01",
            "hadn't seen Marsha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PN-No! She must have\x01",
            "betrayed me, didn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PU-Unacceptable! I specifically\x01",
            "ordered her not to tell anyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FPlease calm down, Carla.\x02\x03",
            "#0103FIt's true that Marsha informed\x01",
            "us of the situation.\x02\x03",
            "#0100FBut that's only because she's\x01",
            "worried sick about your safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200F'Despite what she says, she doesn't\x01",
            "really want to leave Crossbell...'\x01",
            "Her words, not mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PMarsha...\x01",
            "She really said that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000F'I'm leaving Lady Carla in your hands!'\x01",
            "That was her farewell before we made\x01",
            "our way to the station to find you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0304FWell, I think it'd be best if you\x01",
            "had another talk with your pops.\x02\x03",
            "#0300FInstead of runnin' away, won't\x01",
            "it feel better to say what ya\x01",
            "wanna say to his face?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PY-You may be right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PI had started to think that there\x01",
            "was no one at my side...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x0)
    Sleep(200)
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    ChrTalk(
        0x10,
        (
            "#5PBut if Marsha is waiting for me,\x01",
            "I don't mind returning home.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    ChrTalk(
        0x10,
        (
            "#5PUmm, everyone... Perhaps, could you\x01",
            "stay with me a bit longer and let me\x01",
            "get everything out of my system?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PBesides, I need to start thinking\x01",
            "about what I should say to Father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FSure, we can do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FWe should be near Altair,\x01",
            "but we still have the ride back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FIf you want the company,\x01",
            "we'd be glad to oblige.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x2D, 0x1, 0xE)
    BeginChrThread(0x19, 0, 0, 34)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_6EC2")

    label("loc_6BE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C81")

    ChrTalk(
        0x10,
        "#5PUh, I understand that.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    ChrTalk(
        0x10,
        (
            "#5PBut that's exactly why I'm going\x01",
            "in the first place! I'm going to\x01",
            "show Father I mean business!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D25")

    label("loc_6C81")

    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    ChrTalk(
        0x10,
        (
            "#5PJust like I thought, you all\x01",
            "really were hired by Father.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    ChrTalk(
        0x10,
        "#5PHmph, he can worry all he wants!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PI'm never going back to that city!\x02",
    )

    CloseMessageWindow()

    label("loc_6D25")


    ChrTalk(
        0x101,
        (
            "#11P#0006FIf that's how you feel...\x02\x03",
            "#0008F(It's probably useless to try\x01",
            "and convince her any further.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200F(Agreed. We should be arriving\x01",
            "at Altair momentarily.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0306F(Time's up.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FCarla... Could you at least\x01",
            "tell us how to get in contact\x01",
            "with you in Calvard?\x02\x03",
            "I think that might be enough\x01",
            "for your father to back off.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x2D, 0x1, 0xF)
    BeginChrThread(0x19, 0, 0, 34)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()

    label("loc_6EC2")

    Return()

    # Function_31_551C end

    def Function_32_6EC3(): pass

    label("Function_32_6EC3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20802.itc", 0x1E)
    LoadChrToIndex("chr/ch20902.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("apl/ch50000.itc", 0x21)
    LoadChrToIndex("chr/ch20002.itc", 0x22)
    LoadChrToIndex("chr/ch20102.itc", 0x23)
    LoadChrToIndex("chr/ch21202.itc", 0x24)
    LoadChrToIndex("chr/ch20402.itc", 0x25)
    LoadChrToIndex("chr/ch20502.itc", 0x26)
    LoadChrToIndex("chr/ch22002.itc", 0x27)
    SoundLoad(450)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis000.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis150.itp")
    OP_68(-2530, 900, 950, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(19000, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -2300, 150, 750, 180)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -1600, 150, -750, 0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -2600, 150, -750, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x27)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x13, 1900, 150, 750, 180)
    SetChrPos(0x14, 2900, 150, 750, 180)
    SetChrPos(0x15, -1900, 150, -3300, 0)
    SetChrPos(0x16, 2200, 150, 1800, 0)
    SetChrPos(0x17, 2200, 150, 3300, 180)
    SetChrPos(0x18, -2000, 150, 3300, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0xF0, 0x0, 0x20)
    Sleep(500)
    Sound(2179, 255, 60, 0)
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 33)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0x0, 0xF0, 0x0, 0x20)
    Sound(450, 2, 0, 0)
    BeginChrThread(0x19, 0, 0, 35)
    Sleep(3000)
    SetCameraDistance(21000, 5000)
    FadeToBright(5000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(250)
    SetChrSubChip(0x101, 0x1)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sound(1078, 255, 100, 0)

    NpcTalk(
        0x101,
        "???",
        "#0100048V#11PHuh?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x101, 0x8)
    Sleep(50)
    SetChrSubChip(0x101, 0x9)
    Sleep(50)
    SetChrSubChip(0x101, 0x8)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x8)
    Sleep(50)
    SetChrSubChip(0x101, 0x9)
    Sleep(50)
    SetChrSubChip(0x101, 0x8)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrSubChip(0x101, 0x1)
    Sleep(800)
    SetChrSubChip(0x101, 0x2)
    Sleep(1000)
    Sound(1079, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0100049V#11P#60WWhere am I...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7200", 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0100050V#11P#0006F#30WOh, right...\x02\x03",
            "#0100051V#30WI said goodbye to my aunt and\x01",
            "uncle, double-checked all my\x01",
            "luggage, boarded the train...\x02\x03",
            "#0100052V#0008F#40WAnd...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x12,
        "Old Lady's Voice",
        "#0100053V#1PAre you all right, dear?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-2300, 900, 750, 0)
    MoveCamera(237, 21, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21000, 0)
    OP_68(-2300, 900, 0, 1500)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x11,
        "#0100054VYou jolted right awake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100055VYou looked like you were having a nightmare.\x01",
            "Are you feeling okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100056V#7P#0011FOh, no. I'm fine. Just a little\x01",
            "sleep-deprived, that's all.\x02\x03",
            "#0100057V#0006FI had the strangest dream,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#0100058VHaha. A dream, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100059VWere you, perhaps, being swarmed\x01",
            "by hordes of sexy ladies?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0100060V#7P#0012FWhat? N-No... Can't say it\x01",
            "was that good of a dream.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x2)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#0100061V#5PEnough! Don't tease\x01",
            "the poor boy, dear.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#0100062V#5PHow about a cold lemonade\x01",
            "to perk you up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0100063V#5PI have some chilled inside this bottle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100064V#7P#0000FOh, if you don't mind...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2300, 900, 250, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21000, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x3)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x101, 0x4)
    OP_0D()

    ChrTalk(
        0x101,
        "#0100065V#11P*glug* *glug*\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0x101, 0x3)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0100066V#0014F#11PAaaah...\x02\x03",
            "#0100067V#0002FThanks, I appreciate it!\x01",
            "I'm feeling better already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0100068V#1PI'm glad you enjoyed it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100069V#6PJudging by your appearance,\x01",
            "you aren't Erebonian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#0100070V#6PYou must be from Crossbell, right?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0100071V#0005F#11POh, yes, sir.\x02\x03",
            "#0100072V#0004FI lived abroad for a while, but I'm\x01",
            "moving back to the city again.\x02\x03",
            "#0100073V#0000FSpeaking of which, are you two\x01",
            "also from Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100074V#6PYep. We just took a trip to the Republic,\x01",
            "so we're on our way back now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100075V#6PIf you're coming back from living abroad,\x01",
            "I doubt you'll even recognize Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0100076V#1PIndeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0100077V#1PThe city has changed drastically\x01",
            "over the past two or three years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100078V#0003F#11PI thought that might be the case...\x02\x03",
            "#0100079V#0001FI did pass through the city a few\x01",
            "times by train since I moved away.\x02\x03",
            "#0100080VThey've really added a lot of high-\x01",
            "rises, haven't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100081V#6PThey have. After all, Crossbell's always\x01",
            "been the leading trade city in Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100082V#6PCrossbell's ever-growing finance sector has made\x01",
            "foreign investors more willing to provide funding\x01",
            "for development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100083V#6PThis trend only continued to skyrocket\x01",
            "after the Non-Aggression Pact was\x01",
            "signed a little more than a year ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100084V#6PDepartment stores, office buildings...\x01",
            "With the mira investments pouring in,\x01",
            "these places popped up all over the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0100085V#1PSure, these new facilities are a huge\x01",
            "convenience, but people still struggle\x01",
            "to adapt to the city's rapid growth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0100086V#1PEveryone's always busy with this\x01",
            "or that. It's as if we've become\x01",
            "slaves to time and mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100087V#0008F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0100088V#1POh, pardon us. I know it's been a while\x01",
            "since you last saw your hometown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0100089V#1PWe didn't mean to ruin your return.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100090V#0012F#11PPlease, no harm done.\x02\x03",
            "#0100091V#0002FMy friend told me similar things in\x01",
            "his letters...but, no matter how much\x01",
            "it may change, Crossbell's my home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0100092V#1POf course...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100093V#6PHmm, impressive sentiment coming\x01",
            "from someone your age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100094V#6PCompared to bright young men like you,\x01",
            "these newly elected politicians are just...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100095V#6PBah, whether they side with the Empire\x01",
            "or the Republic, they're nothing but a\x01",
            "bunch of megalomaniacs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100096V#6PCan't trust anyone except\x01",
            "for old Mayor MacDowell.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x2)
    Sleep(300)

    ChrTalk(
        0x12,
        "#0100097V#1PDear, calm down...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#0100098V#1PSorry about that. He tends to get\x01",
            "carried away when it comes to politics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100099V#0000F#11PIt's fine. Those details are good to know.\x02\x03",
            "#0100100VSure, you can get the Crossbell Times\x01",
            "internationally...\x02\x03",
            "#0100101V...but I'd rather hear about current affairs\x01",
            "first-hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#0100102V#6POh, another avid Crossbell Times reader, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100103V#6PThey might cover every passing fad,\x01",
            "but they write some impressive\x01",
            "articles every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100104V#6PI wish they'd dive a bit deeper into\x01",
            "issues with the Crossbell Diet, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100105V#0012F#11PSeems like Crossbell is still facing a\x01",
            "bunch of problems.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0100106V#0005F#2POh...!\x02",
    )

    CloseMessageWindow()
    OP_68(-3300, 900, 250, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_24(0x1C2)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev01.pmf", 0xC8, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    SoundLoad(450)
    OP_68(-2300, 900, 250, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21000, 0)
    EndChrThread(0x19, 0x1)
    Sound(450, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(801, 0, 100, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Conductor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0100107V\x07\x05",
            "Attention all passengers.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#0100108V\x07\x05",
            "We will be arriving in Crossbell City shortly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#0100109V\x07\x05",
            "Passengers bound for Liberl and Remiferia by\x01",
            "airship, please make your way to the airport\x01",
            "upon arrival.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#0100110V\x07\x05",
            "Additionally, per Zemurian Railroad Corporation\x01",
            "bylaws, this train will remain at Crossbell Station\x01",
            "for 30 minutes upon arrival.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#0100111V\x07\x05",
            "Passengers bound for Erebonia, please have your\x01",
            "entry application ready for the inspection officer.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x11,
        (
            "#0100112V\x07\x00",
            "#6PHmm. Sounds like we're almost there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100113V#6PI'd rather not see any of those Imperial\x01",
            "soldiers' ugly mugs, so let's get off as\x01",
            "soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100114V#0012F#11PHaha, will do.\x02\x03",
            "#0100115V#0008F...\x02\x03",
            "#0100116V(It's been three years since then...)\x02\x03",
            "#0100117V(I made sure to keep in contact\x01",
            "with Cecile, but...)\x02\x03",
            "#0100118V#0003F...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x5)
    OP_68(-2300, 900, 750, 1500)
    OP_0D()
    OP_6F(0x1)
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0x6)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("Lloyd")

    AnonymousTalk(
        0xFF,
        (
            "#0100119V#0004F(Guy... Cecile...)\x02\x03",
            "#0100120V(I'm finally back.)\x02\x03",
            "#0100121V#0002F(Back to Crossbell... Our home.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    SetCameraDistance(20500, 3000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    BeginChrThread(0x19, 0, 0, 34)
    OP_6F(0x10)
    OP_CA(0x0, 0x0, 0x3)
    EndChrThread(0x101, 0x3)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    EndChrThread(0x19, 0x0)
    OP_24(0x1C2)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    OP_E3(0xA)
    PlayMovie(0x0, "ed7_op.pmf", 0x2, 0x0)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    StopBGM(0x1F4)
    WaitBGM()
    OP_C7(0x1, 0x10)
    Sleep(2500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_E3(0xB)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x1C2)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_6EC3 end

    def Function_33_894A(): pass

    label("Function_33_894A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8982")
    OP_82(0xA, 0xA, 0x5DC, 0x2EE)
    Sleep(3500)
    OP_82(0xA, 0xA, 0x4B0, 0x1F4)
    Sleep(3500)
    Jump("Function_33_894A")

    label("loc_8982")

    Return()

    # Function_33_894A end

    def Function_34_8983(): pass

    label("Function_34_8983")

    OP_25(0x1C2, 0x64)
    Sleep(200)
    OP_25(0x1C2, 0x5A)
    Sleep(200)
    OP_25(0x1C2, 0x50)
    Sleep(200)
    OP_25(0x1C2, 0x46)
    Sleep(200)
    OP_25(0x1C2, 0x3C)
    Sleep(200)
    OP_25(0x1C2, 0x32)
    Sleep(200)
    OP_25(0x1C2, 0x28)
    Sleep(200)
    OP_25(0x1C2, 0x1E)
    Sleep(200)
    OP_25(0x1C2, 0x14)
    Sleep(200)
    OP_25(0x1C2, 0xA)
    Sleep(200)
    OP_25(0x1C2, 0x0)
    Return()

    # Function_34_8983 end

    def Function_35_89CE(): pass

    label("Function_35_89CE")

    OP_25(0x1C2, 0x0)
    Sleep(300)
    OP_25(0x1C2, 0xA)
    Sleep(300)
    OP_25(0x1C2, 0x14)
    Sleep(300)
    OP_25(0x1C2, 0x1E)
    Sleep(300)
    OP_25(0x1C2, 0x28)
    Sleep(300)
    OP_25(0x1C2, 0x32)
    Sleep(300)
    OP_25(0x1C2, 0x3C)
    Sleep(300)
    OP_25(0x1C2, 0x46)
    Sleep(300)
    OP_25(0x1C2, 0x50)
    Sleep(300)
    OP_25(0x1C2, 0x5A)
    Sleep(300)
    OP_25(0x1C2, 0x64)
    Return()

    # Function_35_89CE end

    SaveToFile()

Try(main)
