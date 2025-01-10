from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1600.bin",                # FileName
        "t1600",                    # MapName
        "t1600",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1600",                  # 0
        "Head Nurse Martha",      # 1
        "Nurse Cirone",           # 2
        "Doctor Guenter",         # 3
        "Medical Intern Lytton",  # 4
        "Janitor Dyson",          # 5
        "Nurse Meifa",            # 6
        "Tourist Totti",          # 7
        "Ursula Road",            # 8
    ))

    AddCharChip((
        "chr/ch29600.itc",                   # 00
        "chr/ch29900.itc",                   # 01
        "chr/ch07100.itc",                   # 02
        "chr/ch29400.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch34200.itc",                   # 06
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

    DeclNpc(-26559,  6000,    14199,   0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-26559,  6000,    14199,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4039,    7000,    2160,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4019,    7000,    3849,    180,  389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3430,    7000,    -9159,   178,  389,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-25850,  6000,    14149,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(13619,   7000,    280,     135,  385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 20,  -4.5,                  19.5,                  6.0,                   56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.5,                   -3.9000000953674316,   -1.2000000476837158,   1.0])
    DeclEvent(0x0000, 0, 23,  15.0,                  -14.300000190734863,   6.0,                   729.0,                 [0.23570217192173004,  0.03928372263908386,   -0.0,                  0.0,                   -0.23570233583450317,  0.039283692836761475,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -6.906075954437256,    -0.02749902382493019,  -1.1999999284744263,   1.0])
    DeclEvent(0x0000, 0, 24,  -13.5,                 20.0,                  5.5,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.75,                  -10.0,                 -1.100000023841858,    1.0])
    DeclEvent(0x0000, 0, 25,  -1.5,                  23.5,                  6.5,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.75,                  -11.75,                -1.3000000715255737,   1.0])
    DeclEvent(0x0000, 0, 26,  -22.5,                 23.5,                  5.5,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   11.25,                 -11.75,                -1.100000023841858,    1.0])

    DeclActor(28100,   7000,    -16700,  2000,    28100,   8000,    -16700,  0x007C, 0,  15, 0x0000)
    DeclActor(3300,    7000,    0,       2000,    3300,    8000,    0,       0x007C, 0,  16, 0x0000)
    DeclActor(22500,   7000,    13500,   2000,    22500,   8000,    13500,   0x007C, 0,  17, 0x0000)
    DeclActor(-9300,   7000,    18100,   2000,    -9300,   8000,    18100,   0x007C, 0,  18, 0x0000)
    DeclActor(-30000,  6000,    17000,   2000,    -30000,  7000,    17000,   0x007C, 0,  19, 0x0000)
    DeclActor(17500,   7000,    -3000,   2000,    18000,   8000,    -3000,   0x007C, 0,  14, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "Ursula Road")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ScpFunction((
        "Function_0_534",          # 00, 0
        "Function_1_5EC",          # 01, 1
        "Function_2_617",          # 02, 2
        "Function_3_642",          # 03, 3
        "Function_4_818",          # 04, 4
        "Function_5_9C2",          # 05, 5
        "Function_6_BFA",          # 06, 6
        "Function_7_16D4",         # 07, 7
        "Function_8_18F8",         # 08, 8
        "Function_9_1AF8",         # 09, 9
        "Function_10_2420",        # 0A, 10
        "Function_11_2599",        # 0B, 11
        "Function_12_2AD5",        # 0C, 12
        "Function_13_2B46",        # 0D, 13
        "Function_14_2C85",        # 0E, 14
        "Function_15_3321",        # 0F, 15
        "Function_16_354C",        # 10, 16
        "Function_17_37C5",        # 11, 17
        "Function_18_39C5",        # 12, 18
        "Function_19_3B64",        # 13, 19
        "Function_20_3D78",        # 14, 20
        "Function_21_4084",        # 15, 21
        "Function_22_40F4",        # 16, 22
        "Function_23_4149",        # 17, 23
        "Function_24_4B56",        # 18, 24
        "Function_25_4E62",        # 19, 25
        "Function_26_4E7E",        # 1A, 26
        "Function_27_4E9A",        # 1B, 27
    ))


    def Function_0_534(): pass

    label("Function_0_534")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_574"),
        (1, "loc_580"),
        (2, "loc_58C"),
        (3, "loc_598"),
        (4, "loc_5A4"),
        (5, "loc_5B0"),
        (6, "loc_5BC"),
        (SWITCH_DEFAULT, "loc_5C8"),
    )


    label("loc_574")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_580")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_58C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_598")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5EB")

    Return()

    # Function_0_534 end

    def Function_1_5EC(): pass

    label("Function_1_5EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_616")
    OP_94(0xFE, 0xFFFFF4A2, 0x49DE, 0xFFFFFD58, 0x5172, 0x3E8)
    Sleep(500)
    Jump("Function_1_5EC")

    label("loc_616")

    Return()

    # Function_1_5EC end

    def Function_2_617(): pass

    label("Function_2_617")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_641")
    OP_94(0xFE, 0x1FF4, 0xFFFFEB2E, 0x2EEA, 0xFFFFFE84, 0x3E8)
    Sleep(500)
    Jump("Function_2_617")

    label("loc_641")

    Return()

    # Function_2_617 end

    def Function_3_642(): pass

    label("Function_3_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_650")
    Jump("loc_804")

    label("loc_650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_679")
    SetChrPos(0x9, -27540, 6000, 14130, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_804")

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_691")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6A9")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_804")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6D3")
    SetChrPos(0x9, -1790, 7000, 19910, 180)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_804")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6FC")
    SetChrPos(0x9, -27200, 6000, 20220, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_714")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_722")
    Jump("loc_804")

    label("loc_722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_73A")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_79C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_76F")
    SetChrPos(0xA, 4040, 7000, 2160, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_797")

    label("loc_76F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_797")
    SetChrPos(0xB, 10930, 7000, -2350, 180)
    BeginChrThread(0xB, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)

    label("loc_797")

    Jump("loc_804")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7AF")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_7AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7C2")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_7C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_7DA")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_804")

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_7E8")
    Jump("loc_804")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_7F6")
    Jump("loc_804")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_804")
    ClearChrFlags(0x8, 0x80)

    label("loc_804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_817")
    ClearChrFlags(0xE, 0x80)

    label("loc_817")

    Return()

    # Function_3_642 end

    def Function_4_818(): pass

    label("Function_4_818")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_835")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_848")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_848")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87E")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_87E")

    ClearMapObjFlags(0x5, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B0")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    Jump("loc_903")

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DC")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    Jump("loc_903")

    label("loc_8DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_903")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)

    label("loc_903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_945")
    SetMapObjFrame(0xFF, "model6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    Jump("loc_979")

    label("loc_945")

    SetMapObjFrame(0xFF, "model6", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x2)

    label("loc_979")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_991")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_991")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A9")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_9A9")

    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C1")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_9C1")

    Return()

    # Function_4_818 end

    def Function_5_9C2(): pass

    label("Function_5_9C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B92")
    OP_93(0xFE, 0x0, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Oh, hello. Are you looking for\x01",
            "someone, by chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FY-Yeah. We wanted to see if we could meet\x01",
            "a friend who works here, so we're heading\x01",
            "to the front desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is that right? Well, in that case, you're\x01",
            "going in the completely wrong direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll find it in the lobby, on the first floor. Go\x01",
            "on, that should get you where you need to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, really? Thank you, ma'am.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BF6")

    label("loc_B92")


    ChrTalk(
        0xFE,
        (
            "The front desk is in the lobby, on the first floor.\x01",
            "Go on, I'm sure you'll be able to find it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF6")

    TalkEnd(0xFE)
    Return()

    # Function_5_9C2 end

    def Function_6_BFA(): pass

    label("Function_6_BFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C0B")
    Jump("loc_16D0")

    label("loc_C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_CA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C26")
    Call(0, 7)
    Jump("loc_C9C")

    label("loc_C26")


    ChrTalk(
        0xFE,
        (
            "Despite what Meifa tells you, she always\x01",
            "covers for my dumb mistakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm lucky to have such a good friend.\x02",
    )

    CloseMessageWindow()

    label("loc_C9C")

    Jump("loc_16D0")

    label("loc_CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_EA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0F")

    ChrTalk(
        0xFE,
        (
            "I accidentally bought a taaaad too many bed\x01",
            "sheets when filling out the purchase forms,\x01",
            "and Meifa got really mad at me. Again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You see, I thought 50 sheets weren't enough,\x01",
            "so I added one more zero to the order...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever. I've decided not to freak out\x01",
            "over every little mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't worry about little ol' me!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E9B")

    label("loc_E0F")


    ChrTalk(
        0xFE,
        (
            "Meifa is really heated right now, but I\x01",
            "decided not to let it bother me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not going to worry about every\x01",
            "little thing anymore!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9B")

    Jump("loc_16D0")

    label("loc_EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F3F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBC")
    Call(0, 8)
    Jump("loc_F3A")

    label("loc_EBC")


    ChrTalk(
        0xFE,
        "Darn it. Meifa got mad at me again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I was storing the deliveries right, too!\x01",
            "Why did she have to yell at me...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3A")

    Jump("loc_16D0")

    label("loc_F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_10C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104F")

    ChrTalk(
        0xFE,
        (
            "Geez... A kid ran into me, and now my\x01",
            "head's spinning round and round.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FS-Sorry. Sounds like it was our kid,\x01",
            "if I were to guess.\x02\x03",
            "#0005FAre you, uh, going to be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I-I think so? My vision's just a little topsy-turvy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10C3")

    label("loc_104F")


    ChrTalk(
        0xFE,
        "Everything won't stop spinninnnng...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, that little girl who bumped into me\x01",
            "came back into the hospital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C3")

    Jump("loc_16D0")

    label("loc_10C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_127E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BA")

    ChrTalk(
        0xFE,
        (
            "Meifa may be a nurse, but, wowie,\x01",
            "does she have a short fuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Trust me, I've seen it firsthand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, Meifa has to check on Mr. Gable\x01",
            "today. You know, the INFAMOUS Mr. Gable.\x01",
            "Will she be okay...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1279")

    label("loc_11BA")


    ChrTalk(
        0xFE,
        (
            "Meifa may be a nurse, but, wowie,\x01",
            "does she have a short fuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Gable is as pigheaded as they come,\x01",
            "you see. I can't help but wonder if Meifa\x01",
            "has the patience to deal with him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1279")

    Jump("loc_16D0")

    label("loc_127E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1412")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1365")

    ChrTalk(
        0xFE,
        (
            "Perfect weather! The sheets\x01",
            "should dry super quick today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I'm a genius!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could go ahead and dry Meifa's clothes\x01",
            "that I accidentally stained. Maybe that\x01",
            "would make her a bit happier...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_140D")

    label("loc_1365")


    ChrTalk(
        0xFE,
        (
            "Recently, I messed up and spilt some really\x01",
            "weird medicine on a few of Meifa's dresses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since the weather is THIS nice, it'd be\x01",
            "a waste to not dry them, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140D")

    Jump("loc_16D0")

    label("loc_1412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1420")
    Jump("loc_16D0")

    label("loc_1420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14E3")

    ChrTalk(
        0xFE,
        (
            "Yesterday, Cecile and the other nurses\x01",
            "took over our shifts, so we got the day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, I got to walk around Crossbell City\x01",
            "with Meifa all day. Heehee, it was a blast! ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D0")

    label("loc_14E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_14F1")
    Jump("loc_16D0")

    label("loc_14F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_14FF")
    Jump("loc_16D0")

    label("loc_14FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_150D")
    Jump("loc_16D0")

    label("loc_150D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_16AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FC")

    ChrTalk(
        0xFE,
        (
            "This is the prettiest sunset I've ever seen.\x01",
            "Nice and refreshing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Achoo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "N-No! I got snot on the sheets!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Qu-Quick, Cirone, what do you do?! If Meifa\x01",
            "finds out, she's going to lose her mind!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16A6")

    label("loc_15FC")


    ChrTalk(
        0xFE,
        (
            "C-C'mon, Cirone, what do you do? If Meifa\x01",
            "finds out, she's going to lose her mind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Mr. Dyson would wash them for\x01",
            "me in secret if I asked nicely...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A6")

    Jump("loc_16D0")

    label("loc_16AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_16B9")
    Jump("loc_16D0")

    label("loc_16B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_16C7")
    Jump("loc_16D0")

    label("loc_16C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_16D0")

    label("loc_16D0")

    TalkEnd(0xFE)
    Return()

    # Function_6_BFA end

    def Function_7_16D4(): pass

    label("Function_7_16D4")

    TurnDirection(0x9, 0xD, 0)
    TurnDirection(0xD, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "Ciroooone...! How long does it take\x01",
            "someone to dry bedsheets?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, hey, Meifa! Wait just a second, okay?\x01",
            "I've almost found out the perfect angle to\x01",
            "dry sheets at. It'll be super helpful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "P-Perfect angle? That's what you've been\x01",
            "doing all this time...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "While you were messing around, the rest\x01",
            "of your work was pushed onto me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huh? You did everything else? Thank you,\x01",
            "thank you! You're the best, Meifa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*sigh* And with that, I've lost the will to argue.\x01",
            "You win this battle, Cirone.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_7_16D4 end

    def Function_8_18F8(): pass

    label("Function_8_18F8")


    ChrTalk(
        0xFE,
        (
            "Aw, Meifa got mad at me again. She\x01",
            "should see one of the doctors about\x01",
            "that temper of hers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, I bet she's so angry\x01",
            "because she never gets to eat\x01",
            "lunch on time. I'd be mad, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I tried making the hamburger I saw at a\x01",
            "festival food stall, guess what? It was a piece\x01",
            "of cake! I should teach Meifa how to make it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh! If you want, I can teach you, too!\x02",
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
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1AF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1AF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xB)
    Return()

    # Function_8_18F8 end

    def Function_9_1AF8(): pass

    label("Function_9_1AF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B09")
    Jump("loc_241C")

    label("loc_1B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1B17")
    Jump("loc_241C")

    label("loc_1B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B25")
    Jump("loc_241C")

    label("loc_1B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1F35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEA")

    ChrTalk(
        0xA,
        (
            "#2401FAbout KeA's condition... I've looked into\x01",
            "everything I could find, but I have bad news.\x02\x03",
            "#2406FNothing is a perfect fit for her particular symptoms.\x01",
            "There's also a possibility that she's developed a new,\x01",
            "never-before-seen form of amnesia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2400FOn the bright side, it doesn't look like there\x01",
            "are any serious abnormalities with her. I say\x01",
            "just wait and monitor the situation.\x02\x03",
            "#2406FBesides, I'm no sadist. I don't want to trap her\x01",
            "somewhere she's obviously uncomfortable\x01",
            "with, you know?\x02\x03",
            "#2409FIf I had to say, I'm more of a masochist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106FWh-What are you talking about...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FMan, you don't make a lick of sense.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F30")

    label("loc_1DEA")


    ChrTalk(
        0xA,
        (
            "#2400FWell, whatever. You don't have anything\x01",
            "to worry about in the immediate future,\x01",
            "but try to keep an eye on it, okay?\x02\x03",
            "#2409FOh, yeah, get a load of this. When I went\x01",
            "fishing this morning, I hooked a real monster.\x02\x03",
            "You should've seen the look on Cerdan's face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FHe really does just live in his own world...\x02",
    )

    CloseMessageWindow()

    label("loc_1F30")

    Jump("loc_241C")

    label("loc_1F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1F43")
    Jump("loc_241C")

    label("loc_1F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1F51")
    Jump("loc_241C")

    label("loc_1F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F5F")
    Jump("loc_241C")

    label("loc_1F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1F6D")
    Jump("loc_241C")

    label("loc_1F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1F7B")
    Jump("loc_241C")

    label("loc_1F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_21A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CD")

    ChrTalk(
        0xA,
        (
            "#2406FWhat a shame. I was planning on sneaking\x01",
            "out of this place for the whole day.\x02\x03",
            "I wish you hadn't found me so quickly. I'd be in the\x01",
            "city enjoying the Anniversary Festival right now.\x02\x03",
            "#2400FWell, at least I got to take part in that fishing\x01",
            "tournament the guild threw, so I suppose\x01",
            "that'll have to do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_219C")

    label("loc_20CD")


    ChrTalk(
        0xA,
        (
            "#2406FWhat a shame. I was planning on sneaking\x01",
            "out of this place for the whole day.\x02\x03",
            "#2400FWell, at least I got to take part in that fishing\x01",
            "tournament the guild threw, so I suppose\x01",
            "that'll have to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219C")

    Jump("loc_241C")

    label("loc_21A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_21AF")
    Jump("loc_241C")

    label("loc_21AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_21BD")
    Jump("loc_241C")

    label("loc_21BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_23F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232D")

    ChrTalk(
        0xA,
        (
            "#2404FLet's see here... I have some time before\x01",
            "anything important, so I could go fishing...\x02\x03",
            "#2405FThough, I'd rather not get caught by\x01",
            "Doctor Lago again. It's always the\x01",
            "first floor where he stops me.\x02\x03",
            "#2406F*sigh* Cruel universe. Fine, I'll give up for\x01",
            "today and hole up in my lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012F(This doctor has a few screws loose...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_23F2")

    label("loc_232D")


    ChrTalk(
        0xA,
        (
            "#2403FFishing is a real blessing. I always turn to\x01",
            "it when I'm looking for a change of pace.\x02\x03",
            "#2400FIf I had time away from this limbo, I'd love\x01",
            "to scour Crossbell for the best fishing holes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F2")

    Jump("loc_241C")

    label("loc_23F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2405")
    Jump("loc_241C")

    label("loc_2405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2413")
    Jump("loc_241C")

    label("loc_2413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_241C")

    label("loc_241C")

    TalkEnd(0xFE)
    Return()

    # Function_9_1AF8 end

    def Function_10_2420(): pass

    label("Function_10_2420")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_24E3")

    ChrTalk(
        0xFE,
        "*sigh* Thanks for finding Doctor Guenter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, is it so much to ask him to get his\x01",
            "work done, rather than dump it all on me?\x01",
            "I can only handle so much, y'know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2595")

    label("loc_24E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2595")

    ChrTalk(
        0xFE,
        (
            "Are you kidding me?! Where the heck did the\x01",
            "doctor sneak off to?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm just an intern! I'm not qualified to deal with\x01",
            "EVERYTHING that comes across his desk!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2595")

    TalkEnd(0xFE)
    Return()

    # Function_10_2420 end

    def Function_11_2599(): pass

    label("Function_11_2599")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_25AA")
    Jump("loc_2AD1")

    label("loc_25AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_25B8")
    Jump("loc_2AD1")

    label("loc_25B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2668")

    ChrTalk(
        0xFE,
        (
            "Doctor Guenter and the others just ran\x01",
            "back into the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't get a good look, but it seemed that\x01",
            "they had a seriously wounded man with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD1")

    label("loc_2668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2676")
    Jump("loc_2AD1")

    label("loc_2676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2710")

    ChrTalk(
        0xFE,
        (
            "Wow. Some random girl just ran through here,\x01",
            "and I swear she was going at the speed of\x01",
            "light. I felt the wind kick as she passed me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD1")

    label("loc_2710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2779")

    ChrTalk(
        0xFE,
        "Hmm. You don't LOOK sick...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You have business in the research ward\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD1")

    label("loc_2779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2845")

    ChrTalk(
        0xFE,
        (
            "I'm pretty sure all the doctors are\x01",
            "in the middle of a faculty meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot goes into running\x01",
            "a hospital like St. Ursula.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, I'm perfectly okay with\x01",
            "being a janitor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD1")

    label("loc_2845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2853")
    Jump("loc_2AD1")

    label("loc_2853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28D1")

    ChrTalk(
        0xFE,
        (
            "The staff here works their hardest,\x01",
            "so I should, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Besides, this place would be a mess without me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AD1")

    label("loc_28D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_28DF")
    Jump("loc_2AD1")

    label("loc_28DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_29BA")

    ChrTalk(
        0xFE,
        (
            "Studies say that the color green is quite\x01",
            "soothing to people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, in order to bring a little peace of mind\x01",
            "to our patients, we had a lot of flowers and\x01",
            "greenery planted in and around St. Ursula.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD1")

    label("loc_29BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A9E")

    ChrTalk(
        0xFE,
        (
            "Recently, we put up a fence around the\x01",
            "hospital to keep monsters away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess it was more of a precaution\x01",
            "than anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If monsters broke in and hurt ANOTHER\x01",
            "intern, we'd be in real trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD1")

    label("loc_2A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2AAC")
    Jump("loc_2AD1")

    label("loc_2AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2ABA")
    Jump("loc_2AD1")

    label("loc_2ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2AC8")
    Jump("loc_2AD1")

    label("loc_2AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2AD1")

    label("loc_2AD1")

    TalkEnd(0xFE)
    Return()

    # Function_11_2599 end

    def Function_12_2AD5(): pass

    label("Function_12_2AD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEA")
    Call(0, 7)
    Jump("loc_2B42")

    label("loc_2AEA")


    ChrTalk(
        0xFE,
        "Have I been too soft on Cirone...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm always cleaning up after her messes...\x02",
    )

    CloseMessageWindow()

    label("loc_2B42")

    TalkEnd(0xFE)
    Return()

    # Function_12_2AD5 end

    def Function_13_2B46(): pass

    label("Function_13_2B46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0E")

    ChrTalk(
        0xFE,
        (
            "The roof is so big that they put\x01",
            "another building on top of it.\x01",
            "That's amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you climbed to the top of the research ward,\x01",
            "would you be able to see Crossbell City?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2C81")

    label("loc_2C0E")


    ChrTalk(
        0xFE,
        "I bet the view from the top floor is something else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Would they get mad if I went in without permission?\x02",
    )

    CloseMessageWindow()

    label("loc_2C81")

    TalkEnd(0xFE)
    Return()

    # Function_13_2B46 end

    def Function_14_2C85(): pass

    label("Function_14_2C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CFC")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#0006F(So she wasn't in the research ward, after all...)\x02\x03",
            "#0008F(Where did you go, KeA?)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_3320")

    label("loc_2CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA5")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2C")

    ChrTalk(
        0x101,
        "#0005FThis leads to the research ward, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FWhat should we do? Go in and get\x01",
            "the staff's statements?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FNo need. We've already decided on where\x01",
            "we want to investigate.\x02\x03",
            "#0001FLet's give the roof a quick sweep and see if\x01",
            "we can find any clues.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2E9D")

    label("loc_2E2C")


    ChrTalk(
        0x101,
        (
            "#0003FLet's keep searching the roof. If we want to\x01",
            "find clues about the monsters, this is where\x01",
            "they'll be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E9D")

    TalkEnd(0xFF)
    Jump("loc_3320")

    label("loc_2EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_32A1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F07")
    MenuCmd(1, 0, "[4F - Neurology / Pharmacology Lab]")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F44")
    MenuCmd(1, 0, "[1F - Reference Room]")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_321D")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(1, 0, "Cancel")
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KSelect Floor\x07\x00\x02",
        )
    )

    MenuCmd(2, 0, 132, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_DB()
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FCF"),
        (1, "loc_3015"),
        (2, "loc_305B"),
        (SWITCH_DEFAULT, "loc_306A"),
    )


    label("loc_2FCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2FF7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3010")

    label("loc_2FF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3010")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3010")

    Jump("loc_306A")

    label("loc_3015")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_303D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3056")

    label("loc_303D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3056")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3056")

    Jump("loc_306A")

    label("loc_305B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_306A")

    label("loc_306A")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3086"),
        (1, "loc_31E1"),
        (2, "loc_3211"),
        (SWITCH_DEFAULT, "loc_3218"),
    )


    label("loc_3086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3173")

    ChrTalk(
        0x101,
        (
            "#0005FWe still don't know whether Doctor Guenter\x01",
            "is here or not, but the receptionist should be\x01",
            "able to tell us.\x02\x03",
            "#0003FBesides, we aren't hospital staff, so it wouldn't\x01",
            "be a good idea to go barging in on them.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x5)
    Jump("loc_31DC")

    label("loc_3173")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31B2")
    SetScenarioFlags(0x5C, 0)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_31DC")

    label("loc_31B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31D1")
    SetScenarioFlags(0x5C, 1)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_31DC")

    label("loc_31D1")

    EventEnd(0x5)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_31DC")

    Jump("loc_3218")

    label("loc_31E1")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1620", 114, 0, 0)
    IdleLoop()
    Jump("loc_3218")

    label("loc_3211")

    EventEnd(0x3)
    Jump("loc_3218")

    label("loc_3218")

    Jump("loc_329C")

    label("loc_321D")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This is the St. Ursula research ward. The Special Support\x01",
            "Section doesn't have any business there as of now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_329C")

    Jump("loc_3320")

    label("loc_32A1")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This is the St. Ursula research ward. The Special Support\x01",
            "Section doesn't have any business there as of now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_3320")

    Return()

    # Function_14_2C85 end

    def Function_15_3321(): pass

    label("Function_15_3321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34BE")
    EventBegin(0x0)
    Fade(1000)
    OP_68(22460, 8000, -25140, 0)
    MoveCamera(53, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25970, 0)
    SetChrPos(0x101, 26480, 7000, -16960, 180)
    SetChrPos(0x102, 27690, 7000, -14290, 180)
    SetChrPos(0x103, 26160, 7000, -15280, 180)
    SetChrPos(0x104, 28420, 7000, -15270, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x104,
        "#1101305V#3P#0306FDefinitely wasn't here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101306V#0001FYeah, not with all that water below.\x02\x03",
            "#1101307VIf they really are canine, climbing up from\x01",
            "here would be near impossible for them.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 26480, 7000, -16960, 0)
    OP_68(26480, 8000, -16960, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetScenarioFlags(0x62, 4)
    OP_29(0x3F, 0x1, 0xB)
    EventEnd(0x5)
    Jump("loc_354B")

    label("loc_34BE")

    TalkBegin(0xFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a huge drop-off to the next floor and the\x01",
            "stream below. It seems unlikely that the monsters\x01",
            "trespassed from here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_354B")

    Return()

    # Function_15_3321 end

    def Function_16_354C(): pass

    label("Function_16_354C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376C")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-2220, 8000, -4870, 0)
    MoveCamera(41, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16280, 0)
    SetChrPos(0x101, 3970, 7000, 110, 270)
    SetChrPos(0x102, 5190, 7000, -250, 270)
    SetChrPos(0x103, 4160, 7000, 1920, 270)
    SetChrPos(0x104, 5500, 7000, 1650, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#1101308V#0200F#6PThis is quite the distance, but I suppose\x01",
            "the portico could serve as a stepping stone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101309V#0006F#4PHmm, but that's only about as high as the\x01",
            "first floor ceiling. Could they have really\x01",
            "jumped up from there?\x02\x03",
            "#1101310V#0001FEither way, I think it'd be pretty difficult for\x01",
            "them to get up that way, so let's put it on\x01",
            "the back burner for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 3970, 7000, 110, 90)
    SetScenarioFlags(0x62, 5)
    OP_29(0x3F, 0x1, 0xC)
    EventEnd(0x5)
    Jump("loc_37C4")

    label("loc_376C")

    TalkBegin(0xFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The front entrance portico is visible, but it is still\x01",
            "quite high up.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_37C4")

    Return()

    # Function_16_354C end

    def Function_17_37C5(): pass

    label("Function_17_37C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3941")
    EventBegin(0x0)
    Fade(1000)
    OP_68(23090, 8000, 14140, 0)
    MoveCamera(45, 41, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 21870, 7000, 12850, 45)
    SetChrPos(0x102, 21970, 7000, 11830, 45)
    SetChrPos(0x103, 20710, 7000, 11420, 45)
    SetChrPos(0x104, 20470, 7000, 13080, 45)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x102,
        "#1101311V#0101F#12P#NLloyd, what about here?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#1101312V#0003F#6PHmm. It's definitely not impossible for\x01",
            "this to be the infiltration route, but...\x02\x03",
            "#1101313V#0001F...even then, the drop is pretty high.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 21200, 7000, 12090, 225)
    SetScenarioFlags(0x62, 6)
    OP_29(0x3F, 0x1, 0xD)
    EventEnd(0x5)
    Jump("loc_39C4")

    label("loc_3941")

    TalkBegin(0xFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The surrounding terrain is a potential infiltration route\x01",
            "that the monsters used.\x02\x03",
            "However, it's quite the drop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_39C4")

    Return()

    # Function_17_37C5 end

    def Function_18_39C5(): pass

    label("Function_18_39C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B13")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-8530, 8000, 17450, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24400, 0)
    SetChrPos(0x101, -8770, 7000, 18960, 180)
    SetChrPos(0x102, -10030, 7000, 19500, 180)
    SetChrPos(0x103, -6950, 7000, 19010, 180)
    SetChrPos(0x104, -7950, 7000, 20200, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#1101314V#0006F#5PIt seems unlikely they came in\x01",
            "from this direction.\x02\x03",
            "#1101315V#0001FIf they had wings, that would explain\x01",
            "a lot, but I doubt that's the case.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -8770, 7000, 18960, 270)
    SetScenarioFlags(0x62, 7)
    OP_29(0x3F, 0x1, 0xE)
    EventEnd(0x5)
    Jump("loc_3B63")

    label("loc_3B13")

    TalkBegin(0xFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The drop from the walkway to the floor is incredibly\x01",
            "high up.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_3B63")

    Return()

    # Function_18_39C5 end

    def Function_19_3B64(): pass

    label("Function_19_3B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0B")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-30100, 7000, 16720, 0)
    MoveCamera(37, 43, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22550, 0)
    SetChrPos(0x101, -29060, 6000, 17010, 270)
    SetChrPos(0x102, -28050, 6000, 16180, 270)
    SetChrPos(0x103, -28460, 6000, 14890, 270)
    SetChrPos(0x104, -28620, 6000, 19420, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#1101316V#0005F#11PTake a look at this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101317V#0100F#11PDo you think the monsters might\x01",
            "have infiltrated through here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101318V#0000F#11PNormally, you wouldn't be able to jump\x01",
            "up here from that floor.\x02\x03",
            "#1101319V#0008FHowever...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -29060, 6000, 17010, 0)
    SetScenarioFlags(0x63, 0)
    OP_29(0x3F, 0x1, 0xF)
    ModifyEventFlags(0, 4, 0x80)
    EventEnd(0x5)
    Jump("loc_3D77")

    label("loc_3D0B")

    TalkBegin(0xFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Below the handrail, there are multiple boxes and\x01",
            "containers stacked on top of each other.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_3D77")

    Return()

    # Function_19_3B64 end

    def Function_20_3D78(): pass

    label("Function_20_3D78")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-4500, 8000, 19000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25250, 0)
    SetChrPos(0x101, -3800, 7000, 18900, 90)
    SetChrPos(0x102, -3800, 7000, 20100, 90)
    SetChrPos(0x103, -4900, 7000, 18900, 90)
    SetChrPos(0x104, -4900, 7000, 20100, 90)
    SetChrPos(0x136, -1600, 7000, 19500, 270)
    OP_68(-3000, 8000, 19000, 2500)
    OP_6F(0x1)
    OP_0D()
    OP_93(0x101, 0xB4, 0x12C)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1101177V#0001F#6PHmm... Is this where the victim was\x01",
            "attacked, Cecile?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101178V#1303F#11PI'm afraid so.\x02\x03",
            "#1101179V#1300FWhat's your plan, Lloyd? Search\x01",
            "the surrounding area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101180V#0000F#6PNo, actually. Before we do that, I want\x01",
            "to ask the victim a few questions.\x02\x03",
            "#1101181VWould you mind taking us to him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101182V#1300F#11PSure thing.\x02\x03",
            "#1101183VHe's being treated on the second\x01",
            "floor of the hospital. Follow me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101184V#0000F#6PThanks, Cecile.\x02",
    )

    CloseMessageWindow()
    OP_93(0x136, 0x0, 0x1F4)
    BeginChrThread(0x136, 3, 0, 21)
    Sleep(1300)
    BeginChrThread(0x101, 3, 0, 22)
    Sleep(1200)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 22)
    Sleep(1200)
    BeginChrThread(0x104, 3, 0, 22)
    WaitChrThread(0x136, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_71(0x4, 0xA, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x65, 7)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_3D78 end

    def Function_21_4084(): pass

    label("Function_21_4084")


    def lambda_4089():
        OP_95(0xFE, -1680, 7000, 22860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4089)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x4)

    def lambda_40C2():
        OP_95(0xFE, -1550, 7000, 25460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40C2)
    Sleep(500)

    def lambda_40DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40DF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_4084 end

    def Function_22_40F4(): pass

    label("Function_22_40F4")


    def lambda_40F9():
        OP_95(0xFE, -1680, 7000, 22860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40F9)
    WaitChrThread(0xFE, 1)

    def lambda_4117():
        OP_95(0xFE, -1550, 7000, 25460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4117)
    Sleep(500)

    def lambda_4134():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4134)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_40F4 end

    def Function_23_4149(): pass

    label("Function_23_4149")

    EventBegin(0x0)
    Fade(1000)
    OP_68(15000, 8000, -13430, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    OP_68(15000, 8000, -15500, 3000)
    SetChrPos(0x101, 15700, 7000, -14680, 180)
    SetChrPos(0x102, 14280, 7000, -14560, 180)
    SetChrPos(0x103, 14260, 7000, -13000, 180)
    SetChrPos(0x104, 15640, 7000, -13120, 180)
    SetChrPos(0x136, 15040, 7000, -16780, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#1101283V#0005F#5PJudging by everything we've heard, the scene\x01",
            "of the crime is right around here, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_425A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_425A)
    WaitChrThread(0x136, 1)
    Sleep(300)

    ChrTalk(
        0x136,
        (
            "#1101284V#1301F#5PYes. Supposedly, Lytton was found collapsed\x01",
            "in front of this bench.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101285V#0001F#5PThat matches the report, too.\x02",
    )

    CloseMessageWindow()

    def lambda_42FE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42FE)
    WaitChrThread(0x101, 1)
    Sleep(500)

    def lambda_4312():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_4312)
    Sleep(100)

    def lambda_4322():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4322)
    Sleep(100)

    def lambda_4332():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4332)
    Sleep(400)

    def lambda_4342():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4342)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    MoveCamera(45, 13, 0, 2000)
    OP_68(15000, 8500, -15500, 2000)
    OP_6F(0x51)

    ChrTalk(
        0x101,
        "#1101286V#6P#0005FOh. That's the research ward, isn't it?\x02",
    )

    CloseMessageWindow()

    def lambda_43CD():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43CD)
    Sleep(50)

    def lambda_43DD():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43DD)
    Sleep(50)

    def lambda_43ED():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43ED)
    Sleep(50)

    def lambda_43FD():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_43FD)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x136, 1)

    ChrTalk(
        0x136,
        (
            "#1101287V#12P#1300FThat's right. All of our doctors and interns\x01",
            "do their work there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101288V#0200F#6PDo they perform experiments on dangerous\x01",
            "monsters in there, by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101289V#12P#1304FOf course not, silly.\x02\x03",
            "#1101290V#1300FThe most exotic thing in there is a greenhouse\x01",
            "where plants used for research are grown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101291V#6P#0100FHow interesting.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_68(15000, 8000, -15500, 1200)
    MoveCamera(45, 18, 0, 1200)

    def lambda_45C9():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45C9)
    Sleep(50)

    def lambda_45D9():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_45D9)
    Sleep(50)

    def lambda_45E9():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_45E9)
    Sleep(50)

    def lambda_45F9():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_45F9)
    Sleep(50)

    def lambda_4609():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4609)
    OP_6F(0x51)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#1101292V#0004F#5PThanks for taking the time to show us\x01",
            "around, Cecile.\x02\x03",
            "#1101293V#0000FFor now, I'd like to perform a sweep of\x01",
            "the area until we figure something out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101294V#1300F#12PSure. I'm always happy to help.\x02\x03",
            "#1101295V#1309FWell, good luck, everyone. Investigate\x01",
            "until you can't investigate anymore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101296V#0102F#5PWe will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101297V#0202F#5PThank you for showing us around.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101298V#0309F#5PWe'll have this solved in no time! Look\x01",
            "forward to the good news, okay?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_481C():

        label("loc_481C")

        TurnDirection(0x101, 0x136, 500)
        Yield()
        Jump("loc_481C")

    QueueWorkItem2(0x101, 1, lambda_481C)

    def lambda_482E():

        label("loc_482E")

        TurnDirection(0x102, 0x136, 500)
        Yield()
        Jump("loc_482E")

    QueueWorkItem2(0x102, 1, lambda_482E)

    def lambda_4840():

        label("loc_4840")

        TurnDirection(0x103, 0x136, 500)
        Yield()
        Jump("loc_4840")

    QueueWorkItem2(0x103, 1, lambda_4840)

    def lambda_4852():

        label("loc_4852")

        TurnDirection(0x104, 0x136, 500)
        Yield()
        Jump("loc_4852")

    QueueWorkItem2(0x104, 1, lambda_4852)
    OP_93(0x136, 0x13B, 0x1F4)
    OP_68(13760, 8000, -12780, 3000)

    def lambda_487C():
        OP_95(0xFE, 11170, 7000, -14900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_487C)
    WaitChrThread(0x136, 1)

    def lambda_489A():
        OP_95(0xFE, 10070, 7000, -2850, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_489A)
    Sleep(3000)
    StopBGM(0xBB8)
    WaitChrThread(0x136, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_68(15390, 8000, -13910, 1500)

    def lambda_48E1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48E1)
    WaitChrThread(0x101, 1)

    def lambda_48F2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_48F2)
    Sleep(100)

    def lambda_4902():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4902)

    def lambda_490F():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_490F)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#1101299V#11P#0003FOkay, guys. Like I said, I think we should\x01",
            "conduct a quick sweep before anything else.\x02\x03",
            "#1101300V#0001F'The canine monsters appeared on the roof.'\x02\x03",
            "#1101301VWith that assumption in mind, I want us to\x01",
            "focus on pinning down their infiltration route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101302V#6P#0100FThat's a smart plan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101303V#0202F#1PAh, narrowing down the possibilities. That seems\x01",
            "to be your favorite method of investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101304V#5P#0300FWell, let's get to it.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RemoveParty(0x35, 0x0)
    SetChrPos(0x0, 15500, 7000, -13700, 180)
    ModifyEventFlags(0, 1, 0x80)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    SetScenarioFlags(0x62, 3)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)
    EventEnd(0x5)
    Return()

    # Function_23_4149 end

    def Function_24_4B56(): pass

    label("Function_24_4B56")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-20770, 7000, 15490, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D87")
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        "Oh? Are you four lost?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This isn't exactly the place for visitors.\x01",
            "Please ask the front desk about whatever\x01",
            "you need, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C53():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4C53)
    Sleep(50)

    def lambda_4C63():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4C63)
    Sleep(50)

    def lambda_4C73():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4C73)
    Sleep(50)

    def lambda_4C83():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4C83)
    WaitChrThread(0x0, 1)

    ChrTalk(
        0x101,
        (
            "#0005FSorry about that, ma'am.\x02\x03",
            "#0006F(It'd probably be best to wait until we\x01",
            "meet with Cecile. Otherwise people are\x01",
            "going to keep giving us confused looks.)\x02\x03",
            "(The front desk should be in the lobby.\x01",
            "I'm sure they can find her for us.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E40")

    label("loc_4D87")

    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "Outpatients aren't supposed to be here.\x01",
            "Try asking the front desk for whatever\x01",
            "you need, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's in the lobby, on the first floor of the\x01",
            "hospital. Go on, shoo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E40")

    Sleep(50)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -16660, 6000, 19210, 270)
    EventEnd(0x4)
    Return()

    # Function_24_4B56 end

    def Function_25_4E62(): pass

    label("Function_25_4E62")

    EventBegin(0x1)
    Call(0, 27)
    Sleep(50)
    SetChrPos(0x0, -1500, 6500, 21500, 180)
    EventEnd(0x4)
    Return()

    # Function_25_4E62 end

    def Function_26_4E7E(): pass

    label("Function_26_4E7E")

    EventBegin(0x1)
    Call(0, 27)
    Sleep(50)
    SetChrPos(0x0, -22500, 6000, 21500, 182)
    EventEnd(0x4)
    Return()

    # Function_26_4E7E end

    def Function_27_4E9A(): pass

    label("Function_27_4E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA0")

    ChrTalk(
        0x104,
        (
            "#0305FWe don't want to head back inside\x01",
            "just yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FLet's search for a little longer. Who knows\x01",
            "what might turn up?\x02\x03",
            "If monsters actually appeared on the roof,\x01",
            "there should be evidence substantiating\x01",
            "that claim somewhere up here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_500B")

    label("loc_4FA0")


    ChrTalk(
        0x101,
        (
            "#0001FWe still haven't found anything conclusive.\x01",
            "If we keep searching, something's bound\x01",
            "to turn up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_500B")

    Return()

    # Function_27_4E9A end

    SaveToFile()

Try(main)
