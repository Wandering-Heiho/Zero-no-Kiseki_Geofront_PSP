from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1550.bin",                # FileName
        "t1550",                    # MapName
        "t1550",                    # Location
        0x0052,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 82, 0, 1, 0, 3],
    )

    BuildStringList((
        "t1550",                  # 0
        "Shizuku",                # 1
        "Michael",                # 2
        "Michael",                # 3
        "Representative Gable",   # 4
        "Cecile",                 # 5
        "Nurse Cirone",           # 6
        "Nurse Meifa",            # 7
        "Doctor Guenter",         # 8
        "Janitor Dyson",          # 9
        "Estelle",                # 10
        "Joshua",                 # 11
        "Tourist Mash",           # 12
    ))

    AddCharChip((
        "chr/ch29900.itc",                   # 00
        "apl/ch50137.itc",                   # 01
        "apl/ch50145.itc",                   # 02
        "apl/ch50105.itc",                   # 03
        "chr/ch05300.itc",                   # 04
        "chr/ch07100.itc",                   # 05
        "chr/ch29800.itc",                   # 06
        "chr/ch20200.itc",                   # 07
        "apl/ch50144.itc",                   # 08
        "chr/ch00600.itc",                   # 09
        "chr/ch00700.itc",                   # 0A
        "chr/ch34400.itc",                   # 0B
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

    DeclNpc(-97739,  699,     56169,   180,  341,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(6050,    699,     -47549,  270,  341,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(6050,    400,     -47549,  0,    469,  0x0, 0,   8,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-55299,  699,     -47750,  270,  341,  0x0, 0,   1,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-100589, 0,       57319,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-55020,  0,       -49520,  0,    389,  0x0, 0,   0,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-55020,  0,       -49520,  0,    389,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4809,    0,       -48900,  45,   389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-5579,   0,       7090,    0,    389,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-99220,  0,       55110,   45,   405,  0x0, 0,   9,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-99819,  0,       55990,   90,   405,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-8310,   0,       25229,   90,   385,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)

    DeclActor(-22570,  0,       32610,   1200,    -22570,  1500,    32610,   0x007C, 0,  23, 0x0000)
    DeclActor(-98310,  0,       54690,   1200,    -97740,  1500,    56170,   0x007E, 0,  4,  0x0000)
    DeclActor(-6430,   0,       25360,   1200,    -6430,   1500,    25360,   0x007C, 0,  22, 0x0000)

    ScpFunction((
        "Function_0_334",          # 00, 0
        "Function_1_3EC",          # 01, 1
        "Function_2_5C3",          # 02, 2
        "Function_3_5CA",          # 03, 3
        "Function_4_7DB",          # 04, 4
        "Function_5_1D4C",         # 05, 5
        "Function_6_22BF",         # 06, 6
        "Function_7_3066",         # 07, 7
        "Function_8_3080",         # 08, 8
        "Function_9_32F2",         # 09, 9
        "Function_10_347E",        # 0A, 10
        "Function_11_4FFB",        # 0B, 11
        "Function_12_534F",        # 0C, 12
        "Function_13_62B3",        # 0D, 13
        "Function_14_6561",        # 0E, 14
        "Function_15_6633",        # 0F, 15
        "Function_16_6A28",        # 10, 16
        "Function_17_6CA6",        # 11, 17
        "Function_18_6E33",        # 12, 18
        "Function_19_6F2D",        # 13, 19
        "Function_20_6F98",        # 14, 20
        "Function_21_90D3",        # 15, 21
        "Function_22_98D5",        # 16, 22
        "Function_23_9924",        # 17, 23
        "Function_24_A0A5",        # 18, 24
        "Function_25_AE27",        # 19, 25
        "Function_26_BF95",        # 1A, 26
    ))


    def Function_0_334(): pass

    label("Function_0_334")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_374"),
        (1, "loc_380"),
        (2, "loc_38C"),
        (3, "loc_398"),
        (4, "loc_3A4"),
        (5, "loc_3B0"),
        (6, "loc_3BC"),
        (SWITCH_DEFAULT, "loc_3C8"),
    )


    label("loc_374")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_380")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_38C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_398")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3EB")

    Return()

    # Function_0_334 end

    def Function_1_3EC(): pass

    label("Function_1_3EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_404")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 2)

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_417")
    SetChrFlags(0x8, 0x80)
    Jump("loc_595")

    label("loc_417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_44A")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, 4810, 0, -48900, 45)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_595")

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_45D")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_595")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_481")
    SetChrPos(0xC, -99220, 0, 56180, 90)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_595")

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_4C0")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xC, 4810, 0, -48900, 45)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, -10240, 0, 7490, 0)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_595")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_4E9")
    SetChrPos(0xC, 4810, 0, -48900, 45)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_595")

    label("loc_4E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4F7")
    Jump("loc_595")

    label("loc_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_50A")
    SetChrFlags(0x9, 0x80)
    Jump("loc_595")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_52E")
    SetChrPos(0xC, -99220, 0, 56180, 90)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_595")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_53C")
    Jump("loc_595")

    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_54F")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_595")

    label("loc_54F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_55D")
    Jump("loc_595")

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_56B")
    Jump("loc_595")

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_57E")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_595")

    label("loc_57E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_58C")
    Jump("loc_595")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_595")

    label("loc_595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8")
    ClearChrFlags(0x13, 0x80)

    label("loc_5A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C2")
    Event(0, 20)

    label("loc_5C2")

    Return()

    # Function_1_3EC end

    def Function_2_5C3(): pass

    label("Function_2_5C3")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_5C3 end

    def Function_3_5CA(): pass

    label("Function_3_5CA")

    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_61E")
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Jump("loc_705")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_62C")
    Jump("loc_705")

    label("loc_62C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_63A")
    Jump("loc_705")

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_648")
    Jump("loc_705")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_663")
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Jump("loc_705")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_671")
    Jump("loc_705")

    label("loc_671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_67F")
    Jump("loc_705")

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_69A")
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    Jump("loc_705")

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6A8")
    Jump("loc_705")

    label("loc_6A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6B6")
    Jump("loc_705")

    label("loc_6B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6C4")
    Jump("loc_705")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6D2")
    Jump("loc_705")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_6E0")
    Jump("loc_705")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_6EE")
    Jump("loc_705")

    label("loc_6EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_6FC")
    Jump("loc_705")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_705")

    label("loc_705")

    ClearMapObjFlags(0x2, 0x10)
    SetMapObjFlags(0x3, 0x10)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x0, 0x1)

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_745")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x0, 0x1)

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75D")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x0, 0x1)

    label("loc_75D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_775")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x0, 0x1)

    label("loc_775")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78B")
    OP_66(0x1, 0x1)

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A7")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7DA")

    label("loc_7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7DA")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DA")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_7DA")

    Return()

    # Function_3_5CA end

    def Function_4_7DB(): pass

    label("Function_4_7DB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86F")
    Jump("loc_8B9")

    label("loc_86F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_88F")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B9")

    label("loc_88F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AF")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B9")

    label("loc_8AF")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B9")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8EC")
    Jump("loc_1D44")

    label("loc_8EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_99C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_907")
    Call(0, 5)
    Jump("loc_997")

    label("loc_907")


    ChrTalk(
        0x8,
        (
            "#1500FMy father will be visiting tomorrow,\x01",
            "so I'm going to bed early today.\x02\x03",
            "#1502FThe excitement is going to\x01",
            "make it hard to fall asleep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_997")

    Jump("loc_1D44")

    label("loc_99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B7")
    Call(0, 5)
    Jump("loc_A1C")

    label("loc_9B7")


    ChrTalk(
        0x8,
        (
            "#1502FI had been hoping to meet with KeA\x01",
            "during tomorrow's trip.\x02\x03",
            "Tomorrow will be so much fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1C")

    Jump("loc_1D44")

    label("loc_A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3C")
    Call(0, 15)
    Jump("loc_D7A")

    label("loc_A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B48")

    ChrTalk(
        0x8,
        (
            "#1500FThank you again, everyone.\x02\x03",
            "#1508FI still feel kind of bad about\x01",
            "just giving you the leftovers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha, there's no need to, Shizuku.\x01",
            "We'll take good care of it, I promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1500FI'm really happy to hear that...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BB8")

    label("loc_B48")


    ChrTalk(
        0x8,
        (
            "#1500FAnd I hope this present will make\x01",
            "Father happy as well.\x02\x03",
            "Everyone, thank you. Thank you\x01",
            "so, so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB8")

    Jump("loc_D7A")

    label("loc_BBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF2")
    Call(0, 25)
    Jump("loc_D7A")

    label("loc_BF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_CA1")

    ChrTalk(
        0x8,
        (
            "#1508FI'm sorry to make you go along\x01",
            "with my childish request.\x02\x03",
            "This means a lot to me, everyone.\x02\x03",
            "#1508FUm, but please only do it if you have\x01",
            "the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7A")

    label("loc_CA1")


    ChrTalk(
        0x8,
        (
            "#1500FI feel the same. KeA is a wonderful\x01",
            "friend, and the best one I have.\x02\x03",
            "#1502FIt's sort of peculiar. I've never become\x01",
            "friends with someone so soon after\x01",
            "meeting them.\x02\x03",
            "I can't wait to play with KeA again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7A")

    Jump("loc_1D44")

    label("loc_D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_D8D")
    Jump("loc_1D44")

    label("loc_D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_D9B")
    Jump("loc_1D44")

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_EEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8E")

    ChrTalk(
        0x8,
        (
            "#1500FToday, I get to go on a walk with Miss Neues.\x02\x03",
            "Despite my condition, it's still a lot of fun\x01",
            "being able to spend time with her.\x02\x03",
            "#1502FI think I'm jealous of Lloyd. I wish\x01",
            "I had a sister like Cecile, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EE7")

    label("loc_E8E")


    ChrTalk(
        0x8,
        (
            "#1500FI'm going to go on a walk with Miss Neues\x01",
            "later today.\x02\x03",
            "Heehee. I can't wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE7")

    Jump("loc_1D44")

    label("loc_EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_10D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1046")

    ChrTalk(
        0x8,
        (
            "#1500FIt seems that Father is visiting a lot of\x01",
            "places throughout Crossbell today, too.\x02\x03",
            "And recently, he's been going on more\x01",
            "and more business trips to other countries...\x02\x03",
            "#1505FOh, um, but don't think that I'm lonely,\x01",
            "okay? I'm fine.\x02\x03",
            "#1502FActually, I'm really proud that everyone\x01",
            "relies on him, including me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10D4")

    label("loc_1046")


    ChrTalk(
        0x8,
        (
            "#1500FIt seems that Father is visiting a lot of\x01",
            "places throughout Crossbell today, too.\x02\x03",
            "Father's popularity keeps him\x01",
            "busy, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D4")

    Jump("loc_1D44")

    label("loc_10D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10EA")
    Call(0, 13)
    Jump("loc_1D44")

    label("loc_10EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_12B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F6")

    ChrTalk(
        0x8,
        (
            "#1505FOh, the Special Support Section...\x02\x03",
            "#1508FThe Anniversary Festival is finally here, isn't it?\x01",
            "It completely slipped my mind...\x02\x03",
            "I know something so happy is happening within\x01",
            "arm's reach, but it feels as if it's a far-off world...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12AE")

    label("loc_11F6")


    ChrTalk(
        0x8,
        (
            "#1502FI'm sorry, everyone. It's insensitive of me\x01",
            "to talk like this after you have taken time out\x01",
            "of your day to see me.\x02\x03",
            "I promise I'm all right, so please don't worry\x01",
            "about me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AE")

    Jump("loc_1D44")

    label("loc_12B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_16B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F8")

    ChrTalk(
        0x8,
        "#1505FOh? Is that you, Special Support Section?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHuh?! We didn't even open our mouths yet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1500FI thought I recognized the sound of\x01",
            "those footsteps.\x02\x03",
            "I can remember the footsteps of distinct\x01",
            "people, like you and Cecile, quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FYou can tell from just footsteps?\x01",
            "That's really impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1500FHeehee...\x02\x03",
            "#1500FBut, to tell you the truth, every individual\x01",
            "has their own way of walking.\x02\x03",
            "For example, bracers who come to visit\x01",
            "me often, like my father, walk as if they\x01",
            "are always on guard.\x02",
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
        "#0306FGuess we sound pretty vulnerable, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0206FHow demoralizing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FChin up, you two. Anyone is going to look\x01",
            "outclassed when compared to someone\x01",
            "like Arios.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 7)
    Jump("loc_16B4")

    label("loc_15F8")


    ChrTalk(
        0x8,
        "#1508FU-Um... Did I say something rude?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FNo, that's not it. It just reminded us\x01",
            "that we still have a lot of room for\x01",
            "improvement, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1505FAll right, then...?\x02",
    )

    CloseMessageWindow()

    label("loc_16B4")

    Jump("loc_1D44")

    label("loc_16B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1938")

    ChrTalk(
        0x8,
        (
            "#1500FGood morning, everyone.\x02\x03",
            "Lately, Cecile has been telling\x01",
            "me all about your adventures.\x02\x03",
            "She even said you beat up the\x01",
            "monsters who hurt Lytton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FWell, we definitely couldn't have pulled\x01",
            "it off by ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FIt was all thanks to Zeit and his pack.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1500FWell, even so, just hearing that you had\x01",
            "a large role in stopping them makes me\x01",
            "extremely happy.\x02\x03",
            "#1502FI know it must be hard, but keep doing\x01",
            "your best, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FYou can count on it, Shizuku.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FHey, with a cutie like you cheerin' us on,\x01",
            "we're, like, a hundred times stronger!\x01",
            "So keep up the support, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 6)
    Jump("loc_1A03")

    label("loc_1938")


    ChrTalk(
        0x8,
        (
            "#1500FIf the Special Support Section keeps solving\x01",
            "important cases like that one...\x02\x03",
            "Maybe you'll get as strong as\x01",
            "Father someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThat's quite the challenge, but we'll do\x01",
            "our very best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A03")

    Jump("loc_1D44")

    label("loc_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1D1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB1")

    ChrTalk(
        0x8,
        (
            "#1500FAfter I lost my eyesight, my ears adapted\x01",
            "and became very sensitive. Now, once I\x01",
            "hear something, I can always recognize it.\x02\x03",
            "#1508FHowever, I still don't know exactly what\x01",
            "that weird whistling from before was...\x02\x03",
            "#1505FI'm sorry that I can't give you any useful\x01",
            "information, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004FNo, Shizuku. We may not know how relevant the\x01",
            "sound may be, but the more information we have,\x01",
            "the higher our chances of success are.\x02\x03",
            "#0000FAlso, we were able to find some new clues, too,\x01",
            "thanks to your sharp ears.\x02\x03",
            "Personally, I think this whistling will end up being\x01",
            "crucial to our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1502FReally? Well, I'm glad to hear that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D1A")

    label("loc_1CB1")


    ChrTalk(
        0x8,
        (
            "#1500FPlease continue to do your best, everyone.\x02\x03",
            "I hope the sound I heard will be useful to you...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1A")

    Jump("loc_1D44")

    label("loc_1D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1D2D")
    Jump("loc_1D44")

    label("loc_1D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1D3B")
    Jump("loc_1D44")

    label("loc_1D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1D44")

    label("loc_1D44")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_4_7DB end

    def Function_5_1D4C(): pass

    label("Function_5_1D4C")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xC, 0xFF)
    OP_68(-97720, 1000, 55960, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -99230, 0, 55030, 45)
    SetChrPos(0x102, -99560, 0, 54100, 45)
    SetChrPos(0x103, -99230, 0, 56050, 90)
    SetChrPos(0x104, -98280, 0, 53800, 0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0x8, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E96")

    ChrTalk(
        0x8,
        (
            "#1505FOh! Hello, everyone!\x02\x03",
            "#1502FThank you so much for yesterday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha, it was nothing. Besides, we got\x01",
            "something out of it, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FSomeone looks happy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F0B")

    label("loc_1E96")


    ChrTalk(
        0x8,
        "#1502FOh, good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha. Good morning to you, Shizuku.\x01",
            "You're looking pretty happy, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F0B")


    ChrTalk(
        0x8,
        (
            "#1502FMe? Heehee...\x02\x03",
            "Well, I get to go visit the city tomorrow,\x01",
            "so I'm excited about that.\x02\x03",
            "And Father told me that he would be\x01",
            "able to take a break from work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FThat busy geezer managed to get a\x01",
            "day off from guild stuff, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_20E9")

    ChrTalk(
        0x102,
        (
            "#0102FI'm so happy for you, Shizuku.\x02\x03",
            "Now you can give him the present you\x01",
            "made yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1500FThat's my plan!\x02\x03",
            "#1505FOh, and if it's okay with you...\x02\x03",
            "#1502F...would you mind if I came and\x01",
            "played with KeA?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2185")

    label("loc_20E9")


    ChrTalk(
        0x102,
        "#0102FI'm so happy for you, Shizuku.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1500FTh-Thank you. Oh, and if it's okay with you...\x02\x03",
            "#1502F...would you mind if I came and played with KeA?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2185")


    ChrTalk(
        0x101,
        (
            "#0002FOf course you can! You're always\x01",
            "free to stop by.\x02\x03",
            "We have work to do, but the chief and\x01",
            "KeA should be at the SSS building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204FI can already picture KeA's smiling\x01",
            "face when you arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1502FThank you!\x02\x03",
            "I'll make sure to dress up\x01",
            "when I leave tomorrow, then.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -99230, 0, 55030, 45)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0xCC, 2)
    EventEnd(0x5)
    Return()

    # Function_5_1D4C end

    def Function_6_22BF(): pass

    label("Function_6_22BF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2353")
    Jump("loc_239D")

    label("loc_2353")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2373")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239D")

    label("loc_2373")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2393")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239D")

    label("loc_2393")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_239D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2478")

    ChrTalk(
        0xFE,
        (
            "Shizuku told me a few days ago that she\x01",
            "gets to go to Crossbell City today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She doesn't get to go there very often,\x01",
            "so I hope she has loads and loads of fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_305E")

    label("loc_2478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2486")
    Jump("loc_305E")

    label("loc_2486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2587")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2528")

    ChrTalk(
        0xFE,
        "*cough* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I-I'm fine... Just a little fit, that's all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have Miss Neues come check on\x01",
            "me later. I'll be okay.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2582")

    label("loc_2528")


    ChrTalk(
        0xFE,
        "*cough* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "D-Don't worry about me... All I have\x01",
            "to do is take my medicine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2582")

    Jump("loc_305E")

    label("loc_2587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_27DC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2658")

    ChrTalk(
        0xFE,
        (
            "I'm kinda jealous that Shizuku gets to play\x01",
            "with her dad the day after tomorrow. I wanna\x01",
            "leave the hospital, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I just hope she has enough fun for the\x01",
            "both of us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D7")

    label("loc_2658")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2708")

    ChrTalk(
        0xFE,
        (
            "After hearing about Shizuku's present, I\x01",
            "couldn't help but want to give her something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sure, it was just a dumb box, but I'm glad\x01",
            "she could use it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D7")

    label("loc_2708")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_271C")
    Call(0, 26)
    Jump("loc_27D7")

    label("loc_271C")


    ChrTalk(
        0xFE,
        (
            "Earlier, I got a letter from my parents, all\x01",
            "the way in Leman. It even came with a\x01",
            "present, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They got me the toy I've been telling them\x01",
            "about, which made me pretty happy...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D7")

    Jump("loc_305E")

    label("loc_27DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2874")

    ChrTalk(
        0xFE,
        (
            "It'd be amazing if my surgery went well,\x01",
            "but if something goes wrong, Mom and\x01",
            "Dad's mira would go to waste...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What should I do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_305E")

    label("loc_2874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_28BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288F")
    Call(0, 9)
    Jump("loc_28B8")

    label("loc_288F")


    ChrTalk(
        0xFE,
        "I was right. Surgeries ARE scary...\x02",
    )

    CloseMessageWindow()

    label("loc_28B8")

    Jump("loc_305E")

    label("loc_28BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B9")

    ChrTalk(
        0xFE,
        (
            "I got a letter in the mail from my parents\x01",
            "back in Leman earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're working really, really hard to pay\x01",
            "for my hospital and surgery costs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get sad that they aren't here, but...at\x01",
            "least I have Shizuku.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A45")

    label("loc_29B9")


    ChrTalk(
        0xFE,
        (
            "I got a letter in the mail from my parents\x01",
            "back in Leman earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get sad that they aren't here, but...at\x01",
            "least I have Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A45")

    Jump("loc_305E")

    label("loc_2A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A58")
    Jump("loc_305E")

    label("loc_2A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B08")

    ChrTalk(
        0xFE,
        "The Anniversary Festival parade is tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish I could go see it with Shizuku,\x01",
            "but I doubt that's going to happen...\x01",
            "Maybe next year.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B3F")

    label("loc_2B08")


    ChrTalk(
        0xFE,
        (
            "If only I could go see the parade\x01",
            "with Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3F")

    Jump("loc_305E")

    label("loc_2B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2BB4")

    ChrTalk(
        0xFE,
        "The Anniversary Festival...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet that Doctor Guenter is already\x01",
            "out fishing by now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_305E")

    label("loc_2BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BCF")
    Call(0, 8)
    Jump("loc_2C33")

    label("loc_2BCF")


    ChrTalk(
        0xFE,
        (
            "*cough* *cough* It...doesn't look like I'm going\x01",
            "to be able to go to the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C33")

    Jump("loc_305E")

    label("loc_2C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2D3C")

    ChrTalk(
        0xFE,
        (
            "Even though I'm younger than her,\x01",
            "Shizuku has been a good friend to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We go on a lot of walks together and talk\x01",
            "to each other in her room all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shizuku and I have become friends after\x01",
            "spending so much time here together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_305E")

    label("loc_2D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2DE6")

    ChrTalk(
        0xFE,
        (
            "Shizuku talks to me all the time about\x01",
            "all sorts of stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sometimes I wonder what it's like to\x01",
            "not be able to see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It must be really sad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_305E")

    label("loc_2DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2E77")

    ChrTalk(
        0xFE,
        (
            "Miss Neues came to check on me a\x01",
            "little while ago, even though I didn't\x01",
            "call for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wanna be as nice as her someday.\x02",
    )

    CloseMessageWindow()
    Jump("loc_305E")

    label("loc_2E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FAB")

    ChrTalk(
        0xFE,
        "Huh? Oh, good morning, Miss Neues.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#1300FMichael, how are you feeling?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm feeling okay. A lot better than earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1304FThat's what I like to hear.\x02\x03",
            "#1300FRemember, call for a nurse if you need\x01",
            "anything. We'll come running!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "S-Sure... Thanks, Miss Neues.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3050")

    label("loc_2FAB")


    ChrTalk(
        0xFE,
        (
            "I was brought all the way from\x01",
            "Leman State for treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And the doctor said I won't get better\x01",
            "unless I undergo surgery...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "B-But that's so scary...\x02",
    )

    CloseMessageWindow()

    label("loc_3050")

    Jump("loc_305E")

    label("loc_3055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_305E")

    label("loc_305E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_22BF end

    def Function_7_3066(): pass

    label("Function_7_3066")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Zzz... Zzz...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_3066 end

    def Function_8_3080(): pass

    label("Function_8_3080")

    TurnDirection(0xF, 0x9, 0)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x9,
        "*cough*...*cough* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#2403FHaving light coughing fits, are we?\x01",
            "Be sure to take your medicine later.\x01",
            "No excuses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "O-Okay... *cough* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hey, Doctor, what are you going\x01",
            "to do during the festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#2405FHmm. Quite the question, that.\x02\x03",
            "#2400FI suppose I could always pack up my\x01",
            "tackle box, sit down somewhere, cast\x01",
            "my line, and wait for the fish to bite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huh? You aren't going to go to the\x01",
            "actual festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#2406FNope. I don't care too much for the\x01",
            "hustle and bustle of the festival.\x02\x03",
            "After all, crowds drive the fish away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Is that all you think about...?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_8_3080 end

    def Function_9_32F2(): pass

    label("Function_9_32F2")

    TurnDirection(0xC, 0x9, 0)
    SetChrSubChip(0x9, 0x1)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "#1300FSo you still can't decide whether to\x01",
            "undergo the surgery or not, Michael?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Y-Yeah. I know it's good for me and\x01",
            "all, but everything about it is just so\x01",
            "scary, y'know...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1304FI understand completely.\x01",
            "We won't force you to do anything.\x02\x03",
            "#1300FI promise that the doctors will do all\x01",
            "they can while you make up your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Thanks, Miss Neues...\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_9_32F2 end

    def Function_10_347E(): pass

    label("Function_10_347E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3512")
    Jump("loc_355C")

    label("loc_3512")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3532")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_355C")

    label("loc_3532")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3552")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_355C")

    label("loc_3552")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_355C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C6")

    ChrTalk(
        0xFE,
        (
            "Since yesterday, I've had a sneaking\x01",
            "suspicion that Speaker Hartmann has\x01",
            "finally decided to silence me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was admitted to St. Ursula at the speaker's\x01",
            "behest, so I'm almost positive he's monitoring\x01",
            "every move I make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I have to get out of this accursed place.\x01",
            "Perhaps I can escape to the Empire, or...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38BE")

    ChrTalk(
        0x10A,
        (
            "#0600F(Mr. Gable of the diet's Imperial Faction,\x01",
            "suspected of tax evasion. So, this is where\x01",
            "this snake's been hiding?)\x02\x03",
            "#0603F(Oh, and I say suspected because charges were\x01",
            "never brought against him. It was all swept under\x01",
            "the rug, and now no one talks about the man.)\x02\x03",
            "#0600F(It's obvious that Speaker Hartmann has\x01",
            "abandoned the wretch. I doubt his life is\x01",
            "in any real danger.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103F(What a pitiful man. He doesn't realize\x01",
            "that his colleagues have disowned him.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BE")

    SetScenarioFlags(0x0, 2)
    Jump("loc_397E")

    label("loc_38C6")


    ChrTalk(
        0xFE,
        (
            "A-Anyway, I absolutely must find some\x01",
            "way to escape this prison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I dawdle, I have no doubt that the speaker\x01",
            "will use some dastardly method to silence\x01",
            "me once and for all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_397E")

    Jump("loc_4FF3")

    label("loc_3983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B77")

    ChrTalk(
        0xFE,
        (
            "Speaker Hartmann recommended I hide out\x01",
            "at St. Ursula Medical College after some of my\x01",
            "less-than-moral dealings started to be investigated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but he's never made it clear when I should\x01",
            "be discharged, despite how long I wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely Hartmann isn't aware of my plan to\x01",
            "consolidate my power through my secret,\x01",
            "newly-formed connections, right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If so, wouldn't it make the most sense to\x01",
            "take me out while I'm still here?! O-Oh,\x01",
            "I'm going to be sick...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C62")

    label("loc_3B77")


    ChrTalk(
        0xFE,
        (
            "I-It was never my intention to outsmart\x01",
            "the speaker or anything of that nature...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I wanted was to keep squeezing out\x01",
            "as much influence as I could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I keep waiting around, I'll probably be\x01",
            "erased before too long...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C62")

    Jump("loc_4FF3")

    label("loc_3C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D51")

    ChrTalk(
        0xFE,
        (
            "The plan was to hide out in the hospital\x01",
            "until the storm blew over, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...it was just my luck to have the head\x01",
            "nurse be the one to watch over me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh. This place has become quite hostile.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DF9")

    label("loc_3D51")


    ChrTalk(
        0xFE,
        (
            "I can't stand that head nurse. Who does\x01",
            "she think she is, bossing ME around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it all. Why does a diet member like\x01",
            "myself have to go through such torture?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF9")

    Jump("loc_4FF3")

    label("loc_3DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3F94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF6")

    ChrTalk(
        0xFE,
        "It's like the world's turned upside down...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good heavens! Why was I kicked out of the\x01",
            "nurses' station the moment I stepped in?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "S-Still, in the face of the head nurse,\x01",
            "I lose all will to keep protesting...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F8F")

    label("loc_3EF6")


    ChrTalk(
        0xFE,
        "The head nurse is a formidable lady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Me, a powerful member of the Crossbell Diet,\x01",
            "having to submit to the authorities of a mere\x01",
            "hospital...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F8F")

    Jump("loc_4FF3")

    label("loc_3F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_4086")

    ChrTalk(
        0xFE,
        (
            "*sigh* Prank calling the nurses to kill\x01",
            "time doesn't even sound appealing\x01",
            "anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "During my stay here, Hartmann should\x01",
            "be able to cover up my misdeeds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who knows when I'll make my comeback\x01",
            "in the diet, though?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF3")

    label("loc_4086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_40C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40A1")
    Call(0, 11)
    Jump("loc_40C2")

    label("loc_40A1")


    ChrTalk(
        0xFE,
        "I swear, kids these days...\x02",
    )

    CloseMessageWindow()

    label("loc_40C2")

    Jump("loc_4FF3")

    label("loc_40C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_422E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_419B")

    ChrTalk(
        0xFE,
        (
            "Admit yourself to St. Ursula while you wait for\x01",
            "the storm to blow over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's what the speaker recommended I do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "B-But how much longer does he\x01",
            "expect me to stay here?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4229")

    label("loc_419B")


    ChrTalk(
        0xFE,
        (
            "My stunt with the tax evasion should be\x01",
            "long forgotten from the public's minds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-How much longer does he expect me\x01",
            "to stay here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4229")

    Jump("loc_4FF3")

    label("loc_422E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_44D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4412")

    ChrTalk(
        0xFE,
        (
            "That 'event' is going to be held in Mishelam\x01",
            "tomorrow, if I'm not mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Due to some unforeseen circumstances,\x01",
            "I didn't receive an invitation this year, but\x01",
            "next year, I'm sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Mishelam? Isn't that the wellness resort you\x01",
            "can get to using the cruise ship in the harbor?)\x02\x03",
            "#0000F(Do you think he's going there for...that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Maybe? Place also has a ton of five-star\x01",
            "restaurants and a high-class boutique,\x01",
            "so who knows?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_44D1")

    label("loc_4412")


    ChrTalk(
        0xFE,
        (
            "That event is going to be held in Mishelam\x01",
            "tomorrow, if I'm not mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Due to some unforeseen circumstances,\x01",
            "I didn't receive an invitation this year, but\x01",
            "next year, I'm sure...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D1")

    Jump("loc_4FF3")

    label("loc_44D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45DA")

    ChrTalk(
        0xFE,
        (
            "Entertainment is hard to come by in a\x01",
            "lifeless place like this. How utterly dull.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Normally, I attend parties every night and have\x01",
            "Entertainment District hostesses look after my\x01",
            "every need during the Anniversary Festival...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_462D")

    label("loc_45DA")


    ChrTalk(
        0xFE,
        (
            "If I tried to feel up one of the nurses, the head\x01",
            "nurse would have my head...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_462D")

    Jump("loc_4FF3")

    label("loc_4632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_47F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479C")

    ChrTalk(
        0xFE,
        (
            "Yesterday, I politely asked to increase the\x01",
            "quality of my meals a bit, and guess what\x01",
            "they brought me? A tofu burger!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. As if I'm going to be tricked into eating\x01",
            "something as foul as that. Don't these people\x01",
            "know that lunch should consist of steak and wine?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Just how luxurious a life has he been living...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_47EB")

    label("loc_479C")


    ChrTalk(
        0xFE,
        (
            "Everyone knows that you have steak and\x01",
            "a bottle of wine during lunchtime!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47EB")

    Jump("loc_4FF3")

    label("loc_47F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_491E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489B")

    ChrTalk(
        0xFE,
        (
            "You know, next month's Anniversary Festival\x01",
            "is fast approaching us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And with it comes THAT event...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehehe... I can hardly wait.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4919")

    label("loc_489B")


    ChrTalk(
        0xFE,
        (
            "Last year, I was only able to take part in it\x01",
            "thanks to my ties with Speaker Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehehe... I can hardly wait.\x02",
    )

    CloseMessageWindow()

    label("loc_4919")

    Jump("loc_4FF3")

    label("loc_491E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_49F2")

    ChrTalk(
        0xFE,
        (
            "These frugal hospital meals are joyless\x01",
            "occasions. I told them to add steak and\x01",
            "wine to the menu, but to no avail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch. This so-called hospital's service is\x01",
            "a complete and utter disgrace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF3")

    label("loc_49F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4AB9")

    ChrTalk(
        0xFE,
        (
            "So the buffoons running this place put\x01",
            "up a fence to keep monsters out, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hohoho! I'm glad they finally got it\x01",
            "through their thick skulls. I'm to be\x01",
            "protected at all costs!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF3")

    label("loc_4AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4ACA")
    Call(0, 16)
    Jump("loc_4FF3")

    label("loc_4ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_4FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED8")

    ChrTalk(
        0xFE,
        (
            "I heard that one of our staff members\x01",
            "was assaulted by a pack of monsters\x01",
            "about a week ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, what the hell is going on? They DO\x01",
            "realize that my safety must be guaranteed,\x01",
            "do they not?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F(What's up with this old fart? He\x01",
            "looks as healthy as he can get.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(I think I saw this man featured in the\x01",
            "Crossbell Times some time ago.)\x02\x03",
            "#0103F(If I remember correctly, he's a member of\x01",
            "the Crossbell Diet, hospitalized for poor\x01",
            "health after a recent scandal broke out.)\x02\x03",
            "#0101F(In actuality, he's likely hiding here until\x01",
            "everyone forgets about the whole thing.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(So he is faking illness to procure himself\x01",
            "a hospital room? How disgusting.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(Since he's a prominent member of the Imperial\x01",
            "Faction, I assume he was shut up in here to avoid\x01",
            "making the group look bad.)\x02\x03",
            "#0103F(I'm almost certain that if he attempted to\x01",
            "return to the diet now, his previous post will be\x01",
            "long gone.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(They turned him into a scapegoat.\x01",
            "I almost feel sorry for him, in a way.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 2)
    Jump("loc_4FE5")

    label("loc_4ED8")


    ChrTalk(
        0xFE,
        (
            "I heard that, roughly one week ago, one\x01",
            "of the staff members was assaulted by\x01",
            "a pack of monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They aren't skimping out on security,\x01",
            "are they?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I assure you, if I'm hurt in any way, shape,\x01",
            "or form, St. Ursula will incur the wrath of\x01",
            "Speaker Hartmann!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FE5")

    Jump("loc_4FF3")

    label("loc_4FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4FF3")

    label("loc_4FF3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_347E end

    def Function_11_4FFB(): pass

    label("Function_11_4FFB")

    TurnDirection(0xE, 0xB, 0)
    SetChrSubChip(0xB, 0x1)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xB,
        (
            "What do you mean, 'Other patients take\x01",
            "priority'? I called for you first, didn't I?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Do you know who I am?! I'm a member\x01",
            "of the Crossbell Diet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "S-Sorry. The patient over there was having a\x01",
            "genuine medical emergency I had to attend to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "(And get your own magazines, creep!\x01",
            "We have actual jobs to do!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001F(He's in a nasty mood today...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1111FHey, mister. If you don't stop being so\x01",
            "selfish, you're going to get a spanking!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x153, 500)

    ChrTalk(
        0xB,
        "C-Come again...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Pffft...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Wh-What are you laughing about?!\x01",
            "Kids these days, I swear...!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_52A5")

    ChrTalk(
        0x102,
        "#0100FYou're wise beyond your years, KeA.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5340")

    label("loc_52A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_52F1")

    ChrTalk(
        0x103,
        "#0203FThere truly is nothing KeA is afraid of, is there?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5340")

    label("loc_52F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_5340")

    ChrTalk(
        0x104,
        (
            "#0309FHaha! Atta girl, KeDo. Keep callin' the\x01",
            "guy out on his BS.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5340")

    SetChrSubChip(0xB, 0x0)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_11_4FFB end

    def Function_12_534F(): pass

    label("Function_12_534F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5360")
    Jump("loc_62AF")

    label("loc_5360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_5571")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54AB")

    ChrTalk(
        0xC,
        (
            "#1304FAfter Michael took his medicine, he was\x01",
            "out like a light.\x02\x03",
            "#1300FThe fact that his coughing fits\x01",
            "are so sporadic does worry me.\x02\x03",
            "I'm thankful he hasn't given in to this sickness.\x01",
            "His parents' letters and Shizuku's support must\x01",
            "go a long way.\x02\x03",
            "#1308FStill, if only he would have the surgery...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_556C")

    label("loc_54AB")


    ChrTalk(
        0xC,
        (
            "#1300FI'm certainly worried about Michael's coughing\x01",
            "fits, but thanks to Shizuku and his parents'\x01",
            "continual support, he hasn't given in.\x02\x03",
            "#1308FStill, if only he would have the surgery...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_556C")

    Jump("loc_62AF")

    label("loc_5571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_586A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5621")

    ChrTalk(
        0xC,
        (
            "#1302F(Thanks again for your help yesterday,\x01",
            "everyone.)\x02\x03",
            "#1304F(I think you helped Shizuku out in\x01",
            "more ways than one.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_568A")

    label("loc_5621")


    ChrTalk(
        0xC,
        (
            "#1300F(Good timing, Lloyd.)\x02\x03",
            "(Did you hear what Shizuku was\x01",
            "saying?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(What do you mean?)\x02",
    )

    CloseMessageWindow()

    label("loc_568A")

    Jump("loc_5865")

    label("loc_568F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57BB")

    ChrTalk(
        0xC,
        (
            "#1300FOh, Shizuku. It looks like she's started\x01",
            "to enjoy her stay here much more.\x02\x03",
            "#1304FWell, if I were in her shoes and could take some\x01",
            "time to see Ilya, I'd probably be just as happy.\x02\x03",
            "#1302FShe isn't able to get away from the hospital\x01",
            "too much, so I hope she has a lot of fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5865")

    label("loc_57BB")


    ChrTalk(
        0xC,
        (
            "#1300FOh, Shizuku. It looks like she's started\x01",
            "to enjoy her stay here much more.\x02\x03",
            "On top of being able to spend time with\x01",
            "her father, she also gets to see a friend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5865")

    Jump("loc_62AF")

    label("loc_586A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5885")
    Call(0, 15)
    Jump("loc_5E80")

    label("loc_5885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5D0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C1A")

    ChrTalk(
        0xC,
        (
            "#1302FThank you, everyone, for continuing to\x01",
            "support Shizuku.\x02\x03",
            "#1301FNow, that aside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhat's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1302FI just wasn't expecting you to have chosen\x01",
            "a young lady from the CGF, that's all.\x02\x03",
            "#1309FI've got you this time, Lloyd. She MUST be the one. ♪\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59D1")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_59D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59F9")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_59F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A21")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5A21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A49")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5A49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A71")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5A71")

    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#0505FWait, what?\x02\x03",
            "M-Me...and Lloyd?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011FUmm, this is Sergeant Major Noel Seeker...\x01",
            "And would you knock it off?! She's with us\x01",
            "because we're working together on a job.\x02\x03",
            "#0006FGeez, are you planning on doing this\x01",
            "every time I come here with a girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(Honestly, I should have seen it coming...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(It IS a very Cecile thing to do.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309F(I, for one, think it's very endearing!)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 1)
    Jump("loc_5D07")

    label("loc_5C1A")


    ChrTalk(
        0xC,
        (
            "#1305FI don't see what the big deal is. Noel\x01",
            "seems like a lovely girl, doesn't she?\x02\x03",
            "#1306FCan you blame me for wondering when\x01",
            "I'll have my own nieces and nephews?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FHonestly, Cecile... What am I ever going\x01",
            "to do with you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D07")

    Jump("loc_5E80")

    label("loc_5D0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D41")
    Call(0, 25)
    Jump("loc_5E80")

    label("loc_5D41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5E70")

    ChrTalk(
        0xC,
        (
            "#1300FShizuku really wants to give her father\x01",
            "a present for his birthday.\x02\x03",
            "If you're able to gather some things\x01",
            "around St. Ursula, would you mind\x01",
            "bringing them to us?\x02\x03",
            "If it's the Special Support Section,\x01",
            "I have no doubts that you'll find some\x01",
            "lovely materials. Thanks in advance!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E80")

    label("loc_5E70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E80")
    Call(0, 24)

    label("loc_5E80")

    Jump("loc_62AF")

    label("loc_5E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_604C")

    ChrTalk(
        0xC,
        "#1300FWere you able to talk to Doctor Guenter, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FYeah, about that...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that while talking to the doctor,\x01",
            "KeA ended up getting angry and ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1305FOh, poor girl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FYeah, so we're searching for her now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1303FHmm. I'm sorry, but I haven't seen her.\x02\x03",
            "#1308FBut, if she just now ran away, I doubt\x01",
            "she could have gone far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks as always, Cecile.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 4)
    Jump("loc_6112")

    label("loc_604C")


    ChrTalk(
        0xC,
        (
            "#1308FSomething tells me that she isn't hiding\x01",
            "from you. It is KeA we're talking about,\x01",
            "after all.\x02\x03",
            "#1300FI'd say just try looking around the premises\x01",
            "for her. If I see her, I'll let you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6112")

    Jump("loc_62AF")

    label("loc_6117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6217")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6132")
    Call(0, 9)
    Jump("loc_6212")

    label("loc_6132")


    ChrTalk(
        0xC,
        (
            "#1300FIf you're looking for Doctor Guenter,\x01",
            "he should be in the research ward.\x02\x03",
            "Now, he may be lackadaisical, but he's\x01",
            "an excellent doctor.\x02\x03",
            "I wouldn't be surprised if he had some\x01",
            "idea about how to fix KeA's condition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6212")

    Jump("loc_62AF")

    label("loc_6217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6225")
    Jump("loc_62AF")

    label("loc_6225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6233")
    Jump("loc_62AF")

    label("loc_6233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6244")
    Call(0, 13)
    Jump("loc_62AF")

    label("loc_6244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6252")
    Jump("loc_62AF")

    label("loc_6252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6260")
    Jump("loc_62AF")

    label("loc_6260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_626E")
    Jump("loc_62AF")

    label("loc_626E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_627C")
    Jump("loc_62AF")

    label("loc_627C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_628A")
    Jump("loc_62AF")

    label("loc_628A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_6298")
    Jump("loc_62AF")

    label("loc_6298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_62A6")
    Jump("loc_62AF")

    label("loc_62A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_62AF")

    label("loc_62AF")

    TalkEnd(0xFE)
    Return()

    # Function_12_534F end

    def Function_13_62B3(): pass

    label("Function_13_62B3")

    TurnDirection(0xC, 0x8, 0)
    SetChrSubChip(0x8, 0x2)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64E1")

    ChrTalk(
        0x8,
        (
            "#1502FYou took the first day of the festival\x01",
            "off, didn't you, Cecile?\x02\x03",
            "How was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1300FI had a blast.\x02\x03",
            "#1304FAfter going to see Arc en Ciel with\x01",
            "Lloyd, I went to eat with Ilya and\x01",
            "some other friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1500FI'm happy that you had a good time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1304FHow about this, Shizuku?\x02\x03",
            "#1300FI can't take any more time off this year,\x01",
            "but would you want to go to the festival\x01",
            "with me next year?\x02\x03",
            "#1309FWe can go with Lloyd, Arios, and\x01",
            "everyone else. Doesn't that sound fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1502FYes please! I would love that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6558")

    label("loc_64E1")


    ChrTalk(
        0xC,
        (
            "#1309FNext year, let's go to the festival with\x01",
            "Lloyd, Arios, and everyone else, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1502FI would love to!\x02",
    )

    CloseMessageWindow()

    label("loc_6558")

    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_62B3 end

    def Function_14_6561(): pass

    label("Function_14_6561")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65DF")

    ChrTalk(
        0xFE,
        "Hmm, this hospital really is huge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think my house is bigger, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah...probably.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_662F")

    label("loc_65DF")


    ChrTalk(
        0xFE,
        (
            "I think my house is a lot bigger than\x01",
            "this hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah...probably.\x02",
    )

    CloseMessageWindow()

    label("loc_662F")

    TalkEnd(0xFE)
    Return()

    # Function_14_6561 end

    def Function_15_6633(): pass

    label("Function_15_6633")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xC, 0xFF)
    OP_68(-98260, 800, 56110, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19530, 0)
    SetChrPos(0x101, -99650, 0, 54550, 45)
    SetChrPos(0x102, -100000, 0, 53550, 45)
    SetChrPos(0x103, -98500, 0, 53800, 0)
    SetChrPos(0x104, -97830, 0, 53030, 0)
    SetChrPos(0x109, -100480, 0, 55530, 89)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_93(0xC, 0xB4, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0x8, 0x2)
    OP_0D()

    ChrTalk(
        0xC,
        "#5P#1302FOh, Lloyd! It's nice to see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#1502FHello, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FHello, you two.\x02\x03",
            "I really appreciate what you did\x01",
            "the other day, Shizuku.\x02\x03",
            "For becoming friends with KeA, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1505FI-It was nothing. I think I should be\x01",
            "the one thanking you, actually...\x02\x03",
            "#1502FUm, how is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FOh, she's great. Girl's so active, we\x01",
            "have trouble keepin' up with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0102FShe never gets tired of running\x01",
            "around, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FYes, but we are still no closer to\x01",
            "recovering her memories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1508FI'm sorry to hear that.\x02\x03",
            "#1502FUm, could you pass along a message\x01",
            "to KeA? 'I would love to come play with\x01",
            "you sometime soon.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FWill do, Shizuku. Believe me, you're\x01",
            "welcome at the SSS building any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#1302FHeehee...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -99250, 0, 54950, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0xCC, 0)
    EventEnd(0x5)
    Return()

    # Function_15_6633 end

    def Function_16_6A28(): pass

    label("Function_16_6A28")

    TalkBegin(0xD)
    TurnDirection(0xD, 0xB, 0)
    SetChrSubChip(0xB, 0x1)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C10")

    ChrTalk(
        0xB,
        (
            "Aren't you that witch that spilled tomato\x01",
            "soup all over my bedsheets yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "What? Come here to apologize?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Umm, yep. I'm really sorry about\x01",
            "that whole mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I went and washed them again, so mind\x01",
            "if I change them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ahaha, would you look at that? The\x01",
            "stains sort of make it look like you wet\x01",
            "the bed, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-Is this some kind of sick joke? For\x01",
            "the love of the Goddess, why would\x01",
            "you not just bring a new bedsheet?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6C9A")

    label("loc_6C10")


    ChrTalk(
        0xD,
        (
            "Haha, these sheets make it look like\x01",
            "you wet the bed, mister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "C-Cease this laughter! Imagine my\x01",
            "shame if someone overheard you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C9A")

    SetChrSubChip(0xB, 0x0)
    OP_4C(0xD, 0xFF)
    TalkEnd(0xD)
    Return()

    # Function_16_6A28 end

    def Function_17_6CA6(): pass

    label("Function_17_6CA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6CB7")
    Jump("loc_6E2F")

    label("loc_6CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6D4C")

    ChrTalk(
        0xFE,
        (
            "Ouch... I accidentally slammed my rear\x01",
            "end into the ground after this random\x01",
            "girl crashed into me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Geez, what's her deal...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E2F")

    label("loc_6D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6E2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D67")
    Call(0, 11)
    Jump("loc_6E2F")

    label("loc_6D67")


    ChrTalk(
        0xFE,
        (
            "(Heh. Well, that little stunt might have\x01",
            "made me pretty angry, but I'm glad I\x01",
            "got it all out of my system.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(Thanks, kid.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1100FHehehe. I dunno what I did,\x01",
            "but I'm real happy for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E2F")

    TalkEnd(0xFE)
    Return()

    # Function_17_6CA6 end

    def Function_18_6E33(): pass

    label("Function_18_6E33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E48")
    Call(0, 8)
    Jump("loc_6F29")

    label("loc_6E48")


    ChrTalk(
        0xFE,
        (
            "#2400FNow, I know the Anniversary Festival brings\x01",
            "heaps of work along with it, but I sure would\x01",
            "love if a chance to slack off presented itself.\x02\x03",
            "#2406FBoy, oh, boy. Being a doctor isn't everything\x01",
            "it's cracked up to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F29")

    TalkEnd(0xFE)
    Return()

    # Function_18_6E33 end

    def Function_19_6F2D(): pass

    label("Function_19_6F2D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Whew. Already this late?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I say it's about time I head back and\x01",
            "write up my journal entry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_6F2D end

    def Function_20_6F98(): pass

    label("Function_20_6F98")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50105.itc", 0x1E)
    OP_68(-99110, 1000, 54740, 0)
    MoveCamera(52, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(29860, 0)
    SetChrPos(0x101, -99440, 50, 49020, 0)
    SetChrPos(0x102, -100540, 50, 49020, 0)
    SetChrPos(0x103, -100540, 0, 47910, 0)
    SetChrPos(0x104, -99440, 0, 47910, 0)
    SetChrPos(0xC, -99210, 0, 55670, 90)
    SetChrSubChip(0x8, 0x2)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01500.itp")
    FadeToBright(1000, 0)
    SetCameraDistance(28860, 2000)

    def lambda_70B4():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70B4)

    def lambda_70C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70C9)
    Sleep(100)

    def lambda_70DD():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_70DD)

    def lambda_70F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_70F2)
    Sleep(50)

    def lambda_7106():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7106)

    def lambda_711B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_711B)
    Sleep(80)

    def lambda_712F():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_712F)

    def lambda_7144():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7144)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1101481V#0005F#12PCecile...?\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_71F9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_71F9)
    WaitChrThread(0xC, 1)

    ChrTalk(
        0xC,
        "#1101482V#1305F#5PLloyd? What are you doing here?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    NpcTalk(
        0x8,
        "Girl",
        "#1101483V#1505F#5PUm...\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_68(-99570, 1000, 55330, 2500)
    SetCameraDistance(27360, 2500)

    def lambda_7286():
        OP_95(0xFE, -99720, 0, 54250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7286)
    Sleep(200)

    def lambda_72A3():
        OP_95(0xFE, -100830, 0, 54280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_72A3)
    Sleep(100)

    def lambda_72C0():
        OP_95(0xFE, -100790, 0, 53070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_72C0)
    Sleep(150)

    def lambda_72DD():
        OP_95(0xFE, -99570, 0, 53110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_72DD)
    OP_93(0xC, 0x10E, 0x12C)

    def lambda_72FE():
        OP_95(0xFE, -100070, 0, 55900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_72FE)
    WaitChrThread(0xC, 1)
    SetChrSubChip(0x8, 0x2)
    OP_93(0xC, 0xB4, 0x12C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    ChrTalk(
        0x101,
        (
            "#1101484V#0000F#12PThe head nurse told us that you\x01",
            "were working up here.\x02\x03",
            "#1101485VBut, uh, are we interrupting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1101486V#1309F#5PNo, no, not at all.\x02",
    )

    CloseMessageWindow()

    def lambda_73E2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_73E2)
    WaitChrThread(0xC, 1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#1101487V#1302F#6PThese are the people I was telling\x01",
            "you about, Shizuku.\x02\x03",
            "#1101488VThe righteous, law-enforcing police\x01",
            "officers of the CPD!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101489V#0011F#12PIsn't that going a bit far...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101490V#0109F#6PI think you might be overselling us\x01",
            "quite a bit, Cecile.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Girl",
        "#1101491V#1502F#5PHeehee...\x02",
    )

    CloseMessageWindow()
    OP_68(-98580, 1000, 56100, 2000)

    def lambda_7545():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7545)
    Sleep(50)

    def lambda_7555():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7555)
    Sleep(50)

    def lambda_7565():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7565)
    Sleep(50)

    def lambda_7575():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7575)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Girl")

    AnonymousTalk(
        0xFF,
        (
            "#1101492VThank you for everything you\x01",
            "do, officers.\x02\x03",
            "#1101493VMy name is Shizuku MacLaine.\x02",
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
        "#1101494V#0009F#6PWe appreciate that, Shizuku.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1101495V#0005F#6PWait, hold on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101496V#0105F#6PYou said MacLaine?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101497V#0303F#12PThat name definitely rings a few bells.\x02",
    )

    CloseMessageWindow()

    def lambda_7739():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7739)
    WaitChrThread(0xC, 1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#1101498V#1304F#5PPerhaps you've met her father before.\x02\x03",
            "#1101499V#1300FArios MacLaine.\x02",
        )
    )

    CloseMessageWindow()
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
        "#1101500V#0011F#6PSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101501V#0205F#6PThe Divine Blade of Wind...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101502V#0305F#12PThat guy has a kid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101503V#1505F#5PUm... Do you all know my father?\x02",
    )

    CloseMessageWindow()

    def lambda_78D0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_78D0)

    ChrTalk(
        0x101,
        (
            "#1101504V#0012F#6PWell, I guess you could say that.\x02\x03",
            "#1101505V#0000FHe bailed us out of a tight spot a while ago,\x01",
            "but we haven't seen him much since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101506V#1500F#5PI think I understand.\x02\x03",
            "#1101507VDid he offend you somehow? I know\x01",
            "he can be a bit blunt with his words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101508V#0011F#6PN-No, definitely not.\x02\x03",
            "#1101509V#0003FHonestly, it was a little overwhelming\x01",
            "standing in the same room as such an\x01",
            "accomplished man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101510V#0104F#6PHe might have been strict with us, but he\x01",
            "was also considerate and quite reliable.\x02\x03",
            "#1101511V#0102FYou have a wonderful father,\x01",
            "don't you, Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101512V#1502F#5PD-Do you really think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1101513V#1309F#6PAlways the daddy's girl, Shizuku.\x02\x03",
            "#1101514V#1302FStill, whenever he comes to visit, you're\x01",
            "always so shy. You should dote on him\x01",
            "more often!\x02\x03",
            "#1101515V#1309FSay stuff like, 'I love you, Father!' and\x01",
            "give him lots of big hugs, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101516V#1501F#5PB-But Cecile, that's embarrassing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101517V#0009F#6PHaha, that's Cecile for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101518V#0302F#12P(Hard to imagine Mr. Remarkable himself\x01",
            "gettin' pampered by his daughter, eh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101519V#0204F#6P(Agreed. It is quite hard to picture.)\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7D9A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7D9A)
    WaitChrThread(0xC, 1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#1101520V#1301F#5PBy the way, we might have a lead\x01",
            "for your case.\x02\x03",
            "#1101521VShizuku tells me that she noticed something\x01",
            "out of the ordinary that night.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1101522V#0005F#6PShe did?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101523V#1508F#5PUm, well, I remember the night Lytton\x01",
            "was attacked quite vividly.\x02\x03",
            "#1101524VI was having a hard time falling asleep,\x01",
            "so I stayed up reading my braille books...\x02\x03",
            "#1101525VThen, all of a sudden, I heard a scream.\x02",
        )
    )

    CloseMessageWindow()
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
        "#1101526V#0001F#6PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101527V#0101F#6PWhat happened next?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101528V#1508F#5PWell, I was starting to get a little\x01",
            "anxious, so I opened the window\x01",
            "and listened very carefully...\x02\x03",
            "#1101529VI didn't hear any more screams,\x01",
            "but I did hear something that sounded\x01",
            "like breathing.\x02\x03",
            "#1101530VAfter hearing that for a few minutes,\x01",
            "I suddenly heard what sounded like\x01",
            "something jumping...\x02\x03",
            "#1101531VAnd that's when everything stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101532V#0003F#6PInteresting.\x02\x03",
            "#1101533V#0001FDid you tell the CGF all that, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101534V#1501F#5PUm, to be honest, I thought I dreamt\x01",
            "the entire thing...\x02\x03",
            "#1101535VI only realized it hadn't when I heard\x01",
            "Cecile's explanation.\x02\x03",
            "#1101536V#1508FI-I'm so sorry, everyone. If only I had\x01",
            "said something earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101537V#0002F#6PNo, it's fine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101538V#0104F#6PWe appreciate you telling us, Shizuku.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101539V#0203F#6PAnyway, this statement supports the clues we\x01",
            "found during our investigation of the roof, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101540V#0303F#12PSure does. And remember the sounds she heard\x01",
            "after Lytton screamed and fainted?\x02\x03",
            "#1101541V#0301FThose must've been the wolves breathin',\x01",
            "then their jumpin' on the boxes. That's\x01",
            "their escape route, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101542V#1501F#5PB-But there's more, I think...\x02\x03",
            "#1101543VThough, I might have just misheard it...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#1101544V#0000F#6PIt's okay, Shizuku. Even the smallest\x01",
            "detail might be an important clue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101545V#1501F#5PO-Okay.\x02\x03",
            "#1101546VUm, there was something else I heard\x01",
            "on top of what I already told you...\x02\x03",
            "#1101547VFor some reason, I feel like I heard\x01",
            "a faint whistling sound coming from\x01",
            "outside the hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x103,
        "#1101548V#0205F#6PWhistling...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101549V#0301F#12PHmm. Could it have been a cry unique\x01",
            "to this kinda monster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101550V#0101F#6PShizuku, have you heard that particular\x01",
            "sound before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101551V#1505F#5PNo. I've only ever heard it that night.\x02\x03",
            "#1101552V#1508FI must have misheard it after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101553V#0004F#6PI wouldn't be so sure. Anyway, thanks for\x01",
            "giving us your statement, Shizuku. It might\x01",
            "end up being the clue we need.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88B0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88B0)
    WaitChrThread(0x101, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1101554V#0001F#12PCecile, are you ready to hear our report?\x01",
            "I think our investigation here has helped\x01",
            "make the truth a little bit clearer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1101555V#1304F#5PYes, of course.\x02",
    )

    CloseMessageWindow()

    def lambda_897C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_897C)
    WaitChrThread(0xC, 1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#1101556V#1300F#6PWell, Shizuku, I'll see you around\x01",
            "dinnertime, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101557V#1502F#5POkay. I hope the rest of your shift\x01",
            "goes well, Cecile.\x02\x03",
            "#1101558VAnd good luck with your investigation,\x01",
            "Lloyd. To the rest of you, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A80():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A80)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#1101559V#0002F#6PThanks, Shizuku.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101560V#0102F#6PWe'll definitely come visit again, okay?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-22470, 1000, 30420, 0)
    MoveCamera(38, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27250, 0)
    SetChrPos(0xC, -22510, 0, 32970, 180)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -21910, 0, 29950, 0)
    SetChrPos(0x102, -23180, 0, 29950, 0)
    SetChrPos(0x103, -23180, 0, 28850, 0)
    SetChrPos(0x104, -21910, 0, 28850, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x3)
    FadeToBright(1000, 0)
    SetCameraDistance(26250, 2000)
    OP_6F(0x10)

    def lambda_8BBB():
        OP_95(0xFE, -22510, 0, 31530, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8BBB)

    def lambda_8BD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_8BD5)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xC, 2)

    def lambda_8BEE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8BEE)
    WaitChrThread(0xC, 1)
    Sleep(300)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    Sleep(500)

    ChrTalk(
        0x101,
        "#1101561V#0001F#12PCecile, was that girl...?\x02",
    )

    CloseMessageWindow()

    def lambda_8C52():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8C52)
    WaitChrThread(0xC, 1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#1101562V#1303F#5PBlind, yes. She lost her eyesight in an\x01",
            "accident several years back.\x02\x03",
            "#1101563V#1300FFortunately, it's not as if there isn't any\x01",
            "hope for her.\x02\x03",
            "#1101564VShe's been staying at St. Ursula and\x01",
            "undergoing treatment, recovering\x01",
            "little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101565V#0003F#12PWell, at least there's hope.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101566V#0206F#6PIt must be very difficult for her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1101567V#1304F#5PShe's a brave girl.\x02\x03",
            "#1101568VSince the Bracer Guild keeps her father busy,\x01",
            "she gets quite lonely here. Yet, despite that,\x01",
            "she still pretends to be happy...\x02\x03",
            "#1101569V#1302FYou don't have to, but would you four be her\x01",
            "friends from now on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101570V#0000F#12POf course, Cecile. We'd love to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101571V#0104F#6PShe seems like a lovely girl. I certainly wouldn't\x01",
            "mind spending more time with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101572V#0202F#6PI feel the same.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101573V#0309F#12PLeave it to me, Cecile! I never fail\x01",
            "at makin' the ladies smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1101574V#1309F#5PThank you, everyone.\x02\x03",
            "#1101575V#1300FNow, back to business. You figured out\x01",
            "something while she was talking, right?\x02\x03",
            "#1101576VMind filling me in?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    AddParty(0x35, 0xFF, 0xFF)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_6F98 end

    def Function_21_90D3(): pass

    label("Function_21_90D3")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-98750, 1100, 54900, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16000, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrSubChip(0x8, 0x2)
    OP_68(-98640, 1200, 56080, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x11,
        (
            "#0802F#6POh, wow! I knew they made braille\x01",
            "books, but braille PICTURE books?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0902F#6PThey're pretty impressive, aren't they? Even\x01",
            "the pictures themselves are three-dimensional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1500F#5PThey are. Though, it doesn't seem there are\x01",
            "very many of them.\x02\x03",
            "When I'm older, I'd like to author braille picture\x01",
            "books myself.\x02\x03",
            "#1510FStill, I can't help but wonder whether\x01",
            "someone like me can even do it in\x01",
            "the first place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#0808F#6PShizuku, sweetie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0901F#6PIsn't there still a possibility that you'll be\x01",
            "able to regain your eyesight, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1510F#5PThat's what the doctors say, but...\x02\x03",
            "I think it's important to consider what\x01",
            "I will do if it doesn't happen, too.\x02\x03",
            "#1508FS-Sorry. I must sound annoying, talking\x01",
            "about silly things like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#0801F#6PHey, now! No being shy around us!\x02",
    )

    CloseMessageWindow()
    OP_98(0x11, 0xFA, 0x0, 0xFA, 0x3E8, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle grabbed Shizuku's hands and held them close.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#1505F#5PE-Estelle...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0802F#6PI've got a great idea. Let's make picture\x01",
            "books that every kid can enjoy! Together!\x02\x03",
            "#0809FSo don't you worry about a thing, Shizuku!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0904F#6PIt's easy to see the author's devotion and\x01",
            "warmth shine through the pages...\x02\x03",
            "#0900FI think you should take your own, similar\x01",
            "feelings, hold them close, and never let go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1505F#5PEstelle, Joshua...\x02\x03",
            "#1510F*sniff* Thank you so much.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        "#0805F#6PSh-Shizuku, there's no need to cry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0902F#6PSorry for making you feel that way,\x01",
            "Shizuku.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_68(-22870, 1300, 33250, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -22180, 0, 32330, 315)
    SetChrPos(0x102, -23190, 0, 32030, 45)
    SetChrPos(0x103, -22730, 0, 31110, 0)
    SetChrPos(0x104, -24450, 0, 31390, 45)
    OP_71(0x3, 0x5, 0x5, 0x0, 0x0)
    OP_68(-22870, 1300, 32250, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#0002F(They probably wouldn't mind if we\x01",
            "stepped in, but maybe we shouldn't.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0109F(I agree. It sounds like they're having\x01",
            "a moment.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0304F#5P(Hey, there's always next time.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202F(Indeed there is.)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -22600, 0, 31500, 0)
    OP_71(0x3, 0x0, 0x0, 0x0, 0x0)
    SetScenarioFlags(0xB7, 1)
    EventEnd(0x5)
    Return()

    # Function_21_90D3 end

    def Function_22_98D5(): pass

    label("Function_22_98D5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Linen Room\x01",
            "Employees Only\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_98D5 end

    def Function_23_9924(): pass

    label("Function_23_9924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9ADF")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A80")
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("Doctor Belldine's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "So, how are you feeling today?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'm okay. Everything's the same as always.\x02\x03",
            "...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Doctor Belldine's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "What's wrong? You're missing that smile\x01",
            "of yours.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "N-No, nothing's wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#1303FShe must be in the middle of a checkup.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x68, 1)

    label("loc_9A80")


    ChrTalk(
        0x101,
        (
            "#0000FI'd like to ask her some questions regarding\x01",
            "the incident, but it can wait.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_A0A2")

    label("loc_9ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B80")
    TalkBegin(0xFF)
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You see...and then we...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Heehee...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(They must be busy with something...)\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_A0A2")

    label("loc_9B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CD1")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 1)), scpexpr(EXPR_END)), "loc_9CC6")
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("Shizuku's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I-I'm sorry! I don't know why I suddenly\x01",
            "started crying...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Estelle's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Don't sweat it!\x02\x03",
            "Now, Shizuku, prepare to get spoiled\x01",
            "rotten by your big sister today! No ifs,\x01",
            "ands, or buts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F(We shouldn't interrupt those three.\x01",
            "Let's go, everyone.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CC9")

    label("loc_9CC6")

    Call(0, 21)

    label("loc_9CC9")

    TalkEnd(0xFF)
    Jump("loc_A0A2")

    label("loc_9CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0A2")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A025")
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("Doctor Belldine's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "How are you feeling, Shizuku?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Shizuku's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'm doing well, Doctor Belldine.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Doctor Belldine's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hmm? Your complexion is looking\x01",
            "brighter than usual.\x02\x03",
            "Something good happen?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Shizuku's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "U-Umm... I guess you could say\x01",
            "I had a lot of fun today.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Doctor Belldine's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That so? Well, that's good to hear.\x02\x03",
            "Now, ready to start the examination?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Shizuku's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, of course. Thank you, Doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FIt sounds like Shizuku will be busy\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1111FHuh? Why'd you stop in front of this room?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FOh, right. KeA still hasn't met her yet.\x02\x03",
            "#0000FWell, let's just make sure to stop by later.\x02\x03",
            "We can introduce the two of them then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1106FHer...?\x02\x03",
            "#1110FI dunno what you're talking about, but\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 0)
    Jump("loc_A09F")

    label("loc_A025")


    ChrTalk(
        0x101,
        (
            "#0000FShizuku's in the middle of an exam.\x02\x03",
            "We should probably pay Doctor Guenter\x01",
            "a visit before we do anything else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A09F")

    TalkEnd(0xFF)

    label("loc_A0A2")

    SetChrName("")
    Return()

    # Function_23_9924 end

    def Function_24_A0A5(): pass

    label("Function_24_A0A5")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-98260, 800, 56110, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19530, 0)
    SetChrPos(0x101, -99650, 0, 54550, 45)
    SetChrPos(0x102, -100000, 0, 53550, 45)
    SetChrPos(0x103, -98500, 0, 53800, 0)
    SetChrPos(0x104, -97830, 0, 53030, 0)
    SetChrPos(0x109, -100480, 0, 55530, 89)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    TurnDirection(0xC, 0x101, 0)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    FadeToBright(500, 0)
    OP_0D()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#5P#1305FOh, that reminds me of something.\x02\x03",
            "#1300FEveryone, if you're free, would you mind\x01",
            "giving us a hand with something?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#11P#1505FH-Huh?! Cecile, you don't mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FWhat's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1505FP-Please, don't worry about it, Cecile!\x02\x03",
            "It's just a silly idea!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#1309FOh, you're the one being silly. There's\x01",
            "no need to be so shy.\x02\x03",
            "#1300FYou see, it's almost Shizuku's father's\x01",
            "birthday.\x02\x03",
            "So, of course, she wants to give him\x01",
            "a special present...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105FIt's almost Arios' birthday?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0309FSo he IS human, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203FObviously, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FI think I get it. You want our help to\x01",
            "figure out what present to get, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1505FN-No, not quite.\x02\x03",
            "#1500FYou see, I was thinking of making Father\x01",
            "something handmade this year, so...\x02\x03",
            "I was wanting to search for some things\x01",
            "I could use for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FOh, got'cha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0504FSo you want to collect a bunch of trinkets\x01",
            "around here to craft a special charm for\x01",
            "your dad?\x02\x03",
            "#0500FThat's been a Crossbellan tradition for\x01",
            "a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FWhoa, really? Never knew about that one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0102FI remember making cute things like that\x01",
            "for Grandfather when I was little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FSo, we're to search the hospital\x01",
            "for suitable materials for her gift?\x02\x03",
            "Does that summarize the request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#1502FI-If you could, yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#1304FIf it's the Special Support Section, I have\x01",
            "no doubt that you'll find some materials.\x02\x03",
            "#1300FWhen you do, would you mind bringing\x01",
            "them up to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FSure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FIt's not like we could refuse a request\x01",
            "from the adorable Shizuku, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#1500FI never meant to impose, but thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FThe next question would be: What do you\x01",
            "want to make? If we know that, we should be\x01",
            "able to put together a list of what to look for.\x02\x03",
            "#0000FAny ideas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1505FW-Well, let's see...\x02\x03",
            "#1502FThe truth is, I found this really pretty stone\x01",
            "when I was out walking with Cecile. It's all\x01",
            "smooth and feels nice to touch...\x02\x03",
            "Anyway, after talking to Cecile, we decided\x01",
            "that it should be the present. I just really love\x01",
            "how beautiful it is, so...\x02\x03",
            "...could you find something to put it in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#1300FI'm on board with the idea. I think it's cute.\x02\x03",
            "It's quite the mysterious little rock, though.\x01",
            "When I held it, I swear it was as if a warmth\x01",
            "coursed through my entire body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0305FWhew. That's pretty neat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0102FNow, if we're using this stone, we should\x01",
            "consider what kind of present would be\x01",
            "most suitable for Arios.\x02\x03",
            "#0104FAnd since it's a present, of course, we'll need\x01",
            "something to substitute as a gift box.\x02\x03",
            "#0100FSo let's put a box and ribbon down on\x01",
            "our list as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FGood call, Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1508FAgain, I'm sorry that you have to go\x01",
            "through all this trouble for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FIt's fine, Shizuku. Thanks to you, we\x01",
            "have a good idea of what to look for.\x01",
            "That makes this way easier for us.\x02\x03",
            "Well, guys, ready to start our search?\x02",
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
            "[A Present for Father]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50500, 1000, 57500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_29(0x2C, 0x4, 0x2)
    SetChrPos(0x0, -99300, 0, 54000, 0)
    SetChrPos(0x1, -99300, 0, 54000, 0)
    SetChrPos(0x2, -99300, 0, 54000, 0)
    SetChrPos(0x3, -99300, 0, 54000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    TurnDirection(0xC, 0x8, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_A0A5 end

    def Function_25_AE27(): pass

    label("Function_25_AE27")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-98260, 800, 56110, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19530, 0)
    SetChrPos(0x101, -99650, 0, 54550, 45)
    SetChrPos(0x102, -100000, 0, 53550, 45)
    SetChrPos(0x103, -98500, 0, 53800, 0)
    SetChrPos(0x104, -97830, 0, 53030, 0)
    SetChrPos(0x109, -100480, 0, 55530, 89)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    TurnDirection(0xC, 0x101, 0)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xC,
        "#5P#1305FBack already, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#1502FDoes that mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FThat's right. I think we've found enough\x01",
            "stuff to put together a good present.\x02",
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
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x342),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    AnonymousTalk(
        0xFF,
        (
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x343),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x342, 1)
    SubItemNumber(0x343, 1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#11P#1502FOh, is this...a pendant top?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FYep. We also found a box and ribbon.\x01",
            "Along with these other things, that should\x01",
            "be everything you need.\x02",
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
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x344),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    AnonymousTalk(
        0xFF,
        (
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x345),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x344, 1)
    SubItemNumber(0x345, 1)

    ChrTalk(
        0xC,
        (
            "#5P#1305FI'm honestly a little shocked. I believed in you,\x01",
            "but you really went above and beyond. Finding\x01",
            "all this in St. Ursula couldn't have been easy.\x02\x03",
            "#1300FWhat do you think, Shizuku? Can you make\x01",
            "Arios a present with this stuff?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1502FY-Yes, I can! This should be more than\x01",
            "enough.\x02\x03",
            "The pendant top is really sturdy, so I\x01",
            "doubt it will break...\x02\x03",
            "Also, I don't think that this string's\x01",
            "material will bother Father while he\x01",
            "wears it at work.\x02\x03",
            "Everyone, thank you so very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0009FYour smile made the whole thing\x01",
            "worth it, Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0304FWhat kinda men would we be if we\x01",
            "turned down a request from a cutie\x01",
            "like you?\x02\x03",
            "#0300FIt was high stakes for me and Lloyd,\x01",
            "believe me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0102FIt's going to be perfect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0204FIt certainly should be, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#1300FOh, Shizuku. Since we're all here,\x01",
            "should we go ahead and put\x01",
            "everything together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1505FY-Yes, of course.\x02\x03",
            "#1502FEveryone, would you like to stay for\x01",
            "a bit longer and see the final product?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FDefinitely. After all, we might still be\x01",
            "able to help you with something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0500FI may not be the best with arts and\x01",
            "crafts, but I'd love to help.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#1500FLet's see...\x02\x03",
            "Now, all that's left is to attach the\x01",
            "string and set the stone in the top...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11P#1505FI-It's done!\x02\x03",
            "#1502FWhat do you think, everyone? Do you\x01",
            "think it turned out okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FIt looks extremely well made, Shizuku.\x01",
            "Great job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#1302FI'm sure your father will be delighted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#1502FPhew... Thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FI was kinda skeptical at first, but\x01",
            "this stone really is something else.\x01",
            "Downright beautiful, to boot.\x02\x03",
            "#0304FLike, a little polish and it made a hell\x01",
            "of a pendant. I doubt even jewelers\x01",
            "can measure up to this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FIt's uncanny, really. It's as if the stone\x01",
            "was meant to sit inside that pendant.\x02\x03",
            "The string, too. It doesn't look a step\x01",
            "out of place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FIt is uncomplicated, but I think that, in\x01",
            "and of itself, adds to its elegance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0500FI agree with Randy. It doesn't look like\x01",
            "any less than what you would find in a\x01",
            "jewelry shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#1300FI feel the same way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1502FCecile, everyone...thank you. I would\x01",
            "have never been able to make this\x01",
            "amazing gift without you.\x02\x03",
            "Um, this is a token of my gratitude.\x01",
            "Please, take it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x62),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x62, 1)

    ChrTalk(
        0x101,
        (
            "#6P#0005FIt's beautiful... Wait, is this the same\x01",
            "kind of stone you put in the pendant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1502FYes. When I found the stone with\x01",
            "Cecile, I actually found two of them.\x02\x03",
            "For this one, though, I simply put it\x01",
            "inside my broken brooch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105FAre you sure you want us to have it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1500FYes, of course I am.\x02\x03",
            "Alone, I don't think I ever would have\x01",
            "been able to make my father the gift\x01",
            "I wanted to...\x02\x03",
            "That's why I told myself that I would\x01",
            "give this to whoever helped me.\x02\x03",
            "#1502FAt first, I thought Cecile would be the\x01",
            "one to get it, but after talking things\x01",
            "over with her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#1304F...we turned to all of you.\x02\x03",
            "#1300FAfter collecting such amazing pieces,\x01",
            "you have every right to have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0309FHaha! With all this flattery, it'd be rude\x01",
            "to not accept the thing, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI think we should accept it with\x01",
            "gratitude, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0004FYou make a good case.\x02\x03",
            "#0000FThank you, Shizuku. I promise that\x01",
            "we'll take good care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#1502FYes, please do.\x02\x03",
            "Thank you again, and have a great\x01",
            "rest of your day, everyone.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50500, 1000, 57500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[A Present for Father]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x2C, 0x1, 0x6)
    OP_29(0x2C, 0x4, 0x10)
    SetChrPos(0x0, -100060, 50, 50620, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    TurnDirection(0xC, 0x8, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_AE27 end

    def Function_26_BF95(): pass

    label("Function_26_BF95")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(5720, 1000, -48480, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19220, 0)
    SetChrPos(0x101, 5800, 0, -49500, 0)
    SetChrPos(0x102, 4500, 0, -49500, 45)
    SetChrPos(0x103, 5800, 0, -50800, 0)
    SetChrPos(0x104, 4500, 0, -50800, 45)
    SetChrPos(0x109, 3200, 0, -50150, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x9, 0x1)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#5PEarlier, I got a letter from my parents, all\x01",
            "the way from Leman. It even came with a\x01",
            "present, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThey got me the toy I've been telling them\x01",
            "about, which made me pretty happy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FHaha. Good for you, Michael.\x02\x03",
            "#0003F(If it was a gift, then maybe...)\x02\x03",
            "#0000FHey, do you still happen to have\x01",
            "the box your toy came in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PThe box?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PMiss Neues folded it up for me earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PShe said since I don't get presents\x01",
            "often, I shouldn't just throw it away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FWhew. Women are way more thoughtful\x01",
            "than men. I'd have thrown that sucker in\x01",
            "the trash right after I opened it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FThoughtful? I think it simply comes down\x01",
            "to you being inconsiderate, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PUmm, did you need it for something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FWell, actually...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that they were collecting materials\x01",
            "for a present Shizuku wanted to make.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12P#0000FSo, we're busy trying to find a gift box\x01",
            "and things like that for her, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PWait, so it's for Shizuku...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PWhy didn't you say that to start with?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PHere!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x345),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x345, 1)

    ChrTalk(
        0x102,
        (
            "#12P#0100FWow, isn't it lovely?\x02\x03",
            "A wonderful box for a wonderful gift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0500FAre you really okay with this? You made\x01",
            "it sound like it was pretty important to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PI'm definitely okay with it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI still have the toy it came with, and I was\x01",
            "going to throw it away until Miss Neues told\x01",
            "me not to, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PMore importantly, I wanna give something\x01",
            "to Shizuku, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FIf that's the case, we'll happily take it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0304FHaha, aren't you the ladies' man?\x02\x03",
            "#0300FKeep it up, kid. There's nowhere to go but up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PEhehe, thanks...\x02",
    )

    CloseMessageWindow()
    OP_29(0x2C, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C7F3")
    OP_29(0x2C, 0x1, 0x5)

    ChrTalk(
        0x101,
        (
            "#12P#0000F(We should have everything, now. I bet\x01",
            "the gift box and ribbon will go great with\x01",
            "the rest of the present, too.)\x02\x03",
            "(I think it's about time to show Shizuku\x01",
            "what we found.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7F3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(5800, 1000, -49500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 5800, 0, -49500, 0)
    SetChrPos(0x1, 5800, 0, -49500, 0)
    SetChrPos(0x2, 5800, 0, -49500, 0)
    SetChrPos(0x3, 5800, 0, -49500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x9, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_26_BF95 end

    SaveToFile()

Try(main)
