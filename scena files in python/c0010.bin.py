from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0010.bin",                # FileName
        "c0010",                    # MapName
        "c0010",                    # Location
        0x0003,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 3, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0010",                  # 0
        "Attendant Lux",          # 1
        "Attendant Lisa",         # 2
        "Attendant Heim",         # 3
        "Attendant Schenley",     # 4
        "Attendant Maggis",       # 5
        "Inspection Officer Quattro",# 6
        "Bracer Scott",           # 7
        "Bracer Wenzel",          # 8
        "Bracer Lynn",            # 9
        "Bracer Aeolia",          # 10
        "Passenger",              # 11
        "Passenger",              # 12
        "Passenger",              # 13
        "Passenger",              # 14
        "Passenger",              # 15
        "Passenger",              # 16
        "Passenger",              # 17
        "Passenger",              # 18
    ))

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch28400.itc",                   # 01
        "chr/ch28500.itc",                   # 02
        "chr/ch22002.itc",                   # 03
        "chr/ch22102.itc",                   # 04
        "chr/ch21202.itc",                   # 05
        "chr/ch20000.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch34200.itc",                   # 08
        "chr/ch21600.itc",                   # 09
        "chr/ch27200.itc",                   # 0A
        "chr/ch27300.itc",                   # 0B
        "chr/ch32000.itc",                   # 0C
        "chr/ch32100.itc",                   # 0D
    ))

    DeclNpc(4750,    0,       7500,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(9500,    0,       7500,    180,  257,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(33000,   4000,    8000,    270,  257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(33000,   4000,    -8000,   270,  257,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(18260,   0,       10229,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(28000,   4000,    10000,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(12439,   29,      -409,    180,  389,  0x0, 0,   10,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(12439,   29,      -2549,   0,    405,  0x0, 0,   11,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(6420,    29,      -2569,   180,  389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(6420,    0,       -4050,   0,    389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(14000,   100,     -8899,   0,    469,  0x0, 0,   3,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(13000,   100,     -8899,   0,    469,  0x0, 0,   4,   0,   255, 255, 0,   21,  255,  0)
    DeclNpc(5500,    100,     -5400,   0,    469,  0x0, 0,   5,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(28500,   4000,    1350,    90,   385,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(13500,   100,     -8899,   0,    469,  0x0, 0,   4,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(11000,   0,       0,       90,   385,  0x0, 0,   8,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(12000,   0,       0,       270,  385,  0x0, 0,   9,   0,   0,   0,   0,   27,  255,  0)

    DeclActor(4750,    0,       6500,    1000,    4750,    1500,    7500,    0x007E, 0,  5,  0x0000)
    DeclActor(9500,    0,       6500,    1000,    9500,    1500,    7500,    0x007E, 0,  7,  0x0000)
    DeclActor(32000,   4000,    8000,    1000,    33000,   5500,    8000,    0x007E, 0,  9,  0x0000)
    DeclActor(32000,   4000,    -8000,   1000,    33000,   5500,    -8000,   0x007E, 0,  11, 0x0000)
    DeclActor(20560,   0,       4090,    1000,    20560,   1500,    4090,    0x007C, 0,  35, 0x0000)
    DeclActor(20130,   0,       -4810,   1000,    20130,   1500,    -4810,   0x007C, 0,  36, 0x0000)
    DeclActor(31150,   4000,    1130,    1000,    31150,   5500,    1130,    0x007C, 0,  37, 0x0000)
    DeclActor(28100,   4000,    11510,   1000,    28100,   5500,    11510,   0x007C, 0,  38, 0x0000)
    DeclActor(30940,   4000,    -1900,   1000,    30940,   5500,    -1900,   0x007C, 0,  39, 0x0000)

    ScpFunction((
        "Function_0_4A8",          # 00, 0
        "Function_1_560",          # 01, 1
        "Function_2_58B",          # 02, 2
        "Function_3_600",          # 03, 3
        "Function_4_6F4",          # 04, 4
        "Function_5_781",          # 05, 5
        "Function_6_785",          # 06, 6
        "Function_7_C3D",          # 07, 7
        "Function_8_C41",          # 08, 8
        "Function_9_1460",         # 09, 9
        "Function_10_1464",        # 0A, 10
        "Function_11_16FB",        # 0B, 11
        "Function_12_16FF",        # 0C, 12
        "Function_13_1D42",        # 0D, 13
        "Function_14_25A0",        # 0E, 14
        "Function_15_2726",        # 0F, 15
        "Function_16_2BDC",        # 10, 16
        "Function_17_3007",        # 11, 17
        "Function_18_314D",        # 12, 18
        "Function_19_370C",        # 13, 19
        "Function_20_38DC",        # 14, 20
        "Function_21_3B25",        # 15, 21
        "Function_22_3D1F",        # 16, 22
        "Function_23_3F76",        # 17, 23
        "Function_24_408C",        # 18, 24
        "Function_25_4267",        # 19, 25
        "Function_26_451F",        # 1A, 26
        "Function_27_4605",        # 1B, 27
        "Function_28_4775",        # 1C, 28
        "Function_29_4AFE",        # 1D, 29
        "Function_30_4D46",        # 1E, 30
        "Function_31_4E2F",        # 1F, 31
        "Function_32_4FF4",        # 20, 32
        "Function_33_55D1",        # 21, 33
        "Function_34_59D4",        # 22, 34
        "Function_35_5A4D",        # 23, 35
        "Function_36_5ABA",        # 24, 36
        "Function_37_5B32",        # 25, 37
        "Function_38_5B74",        # 26, 38
        "Function_39_5BE3",        # 27, 39
    ))


    def Function_0_4A8(): pass

    label("Function_0_4A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4E8"),
        (1, "loc_4F4"),
        (2, "loc_500"),
        (3, "loc_50C"),
        (4, "loc_518"),
        (5, "loc_524"),
        (6, "loc_530"),
        (SWITCH_DEFAULT, "loc_53C"),
    )


    label("loc_4E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_4F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_500")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_50C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_518")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_524")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_530")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_53C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_55F")

    Return()

    # Function_0_4A8 end

    def Function_1_560(): pass

    label("Function_1_560")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58A")
    OP_94(0xFE, 0x4D12, 0x686, 0x3F6F, 0xFFFFF81C, 0x3E8)
    Sleep(300)
    Jump("Function_1_560")

    label("loc_58A")

    Return()

    # Function_1_560 end

    def Function_2_58B(): pass

    label("Function_2_58B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FF")
    OP_95(0xFE, 20920, 4000, -8210, 1000, 0x0)
    OP_95(0xFE, 20920, 4000, 760, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0xC8)
    Sleep(2500)
    OP_95(0xFE, 20920, 4000, -8210, 1000, 0x0)
    OP_95(0xFE, 18700, 4000, -8210, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0xC8)
    Sleep(4500)
    Jump("Function_2_58B")

    label("loc_5FF")

    Return()

    # Function_2_58B end

    def Function_3_600(): pass

    label("Function_3_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_614")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 33)
    Jump("loc_621")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_621")
    Event(0, 28)

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_668")
    SetChrPos(0xD, 18820, 0, 4500, 90)
    SetChrPos(0xC, 19970, 0, 4500, 270)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_679")

    label("loc_668")

    SetChrPos(0xD, 19970, 0, -4490, 90)

    label("loc_679")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_6F3")

    label("loc_6A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D0")
    SetChrFlags(0xD, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C6")
    Jump("loc_6CB")

    label("loc_6C6")

    SetChrFlags(0xD, 0x80)

    label("loc_6CB")

    Jump("loc_6DF")

    label("loc_6D0")

    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_6DF")

    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_6F3")

    Return()

    # Function_3_600 end

    def Function_4_6F4(): pass

    label("Function_4_6F4")

    ClearMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71D")
    SetMapObjFlags(0x2, 0x10)

    label("loc_71D")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_731")
    Jump("loc_769")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_769")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_751")
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_769")

    label("loc_751")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_769")
    SetMapObjFlags(0x1, 0x10)
    OP_1B(0x0, 0x0, 0x22)

    label("loc_769")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_780")
    SetMapObjFlags(0x1, 0x10)

    label("loc_780")

    Return()

    # Function_4_6F4 end

    def Function_5_781(): pass

    label("Function_5_781")

    Call(0, 6)
    Return()

    # Function_5_781 end

    def Function_6_785(): pass

    label("Function_6_785")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_AC7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_903")

    ChrTalk(
        0x8,
        (
            "You know how the relations between Erebonia\x01",
            "and Calvard were pretty bad around the time\x01",
            "of the Hundred Days War, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "During that period, railway operations\x01",
            "shut down and travelers lingering in\x01",
            "Crossbell were forced to stay put.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Afterwards, the system was revised to prevent\x01",
            "a similar situation from ever happening again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9D4")

    label("loc_903")


    ChrTalk(
        0x8,
        (
            "Train operations were temporarily shut down\x01",
            "during the Hundred Days War, leaving many\x01",
            "travelers stranded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Afterwards, the system was revised to prevent\x01",
            "a similar situation from ever happening again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D4")

    Jump("loc_AC2")

    label("loc_9D9")


    ChrTalk(
        0x8,
        (
            "Even Mayor MacDowell uses the railway\x01",
            "whenever he has appointments in the\x01",
            "Empire or Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sure, traveling by airship would be faster,\x01",
            "but the tickets are way more expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "We're blessed with such a frugal mayor!\x02",
    )

    CloseMessageWindow()

    label("loc_AC2")

    Jump("loc_C39")

    label("loc_AC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B64")

    ChrTalk(
        0x8,
        (
            "Thank you very much for your continued\x01",
            "patronage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The station gets crowded after the trains\x01",
            "arrive, so please try to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C39")

    label("loc_B64")


    ChrTalk(
        0x8,
        (
            "The railway is operated and maintained\x01",
            "by the Zemurian Railroad Corporation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way, Quattro was dispatched here by\x01",
            "the Empire for inspection purposes. He's not\x01",
            "actually employed by the corporation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C39")

    TalkEnd(0x8)
    Return()

    # Function_6_785 end

    def Function_7_C3D(): pass

    label("Function_7_C3D")

    Call(0, 8)
    Return()

    # Function_7_C3D end

    def Function_8_C41(): pass

    label("Function_8_C41")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_C9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_CBE")
    OP_AF(0x89)
    Jump("loc_D20")

    label("loc_CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_CCE")
    OP_AF(0x88)
    Jump("loc_D20")

    label("loc_CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_CDE")
    OP_AF(0x87)
    Jump("loc_D20")

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_CEE")
    OP_AF(0x86)
    Jump("loc_D20")

    label("loc_CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CFE")
    OP_AF(0x85)
    Jump("loc_D20")

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_D0E")
    OP_AF(0x84)
    Jump("loc_D20")

    label("loc_D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_D1E")
    OP_AF(0x83)
    Jump("loc_D20")

    label("loc_D1E")

    OP_AF(0x82)

    label("loc_D20")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1457")

    label("loc_D2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D43")
    Jump("loc_1457")

    label("loc_D43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1457")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_10D3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1B")

    ChrTalk(
        0x9,
        (
            "The Calvard-bound passenger train will soon\x01",
            "be departing from Platform 1.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you have yet to board, please hurry or wait\x01",
            "for the next train.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EC5")

    label("loc_E1B")


    ChrTalk(
        0x9,
        (
            "The Calvard-bound passenger train will soon\x01",
            "be departing from Platform 1.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please take your time while boarding. Rushing\x01",
            "is dangerous to your safety and others.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC5")

    Jump("loc_10CE")

    label("loc_ECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1015")

    ChrTalk(
        0x9,
        (
            "The bus service provides transportation to the\x01",
            "Erebonia and Calvard border gates, if you\x01",
            "would rather do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you have a minute, I can explain alternative\x01",
            "methods of transportation that can assist you\x01",
            "in your return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you happen to miss your train, please don't\x01",
            "hesitate to let me know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10CE")

    label("loc_1015")


    ChrTalk(
        0x9,
        (
            "If needed, I can even show you the optimal bus route\x01",
            "to take upon arriving at any of the border gates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you happen to miss your train, please don't\x01",
            "hesitate to let me know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10CE")

    Jump("loc_1457")

    label("loc_10D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1229")

    ChrTalk(
        0x9,
        "Oh. Excuse me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "I was distracted by the Crossbell Times\x01",
            "article I was reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Are you here about Quattro's request?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's waiting for you in front of his office.\x01",
            "It's upstairs and to the left.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12B5")

    label("loc_1229")


    ChrTalk(
        0x9,
        "So, are you here for Quattro's request?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's waiting for you in front of his office. Go\x01",
            "up the stairs, and it'll be on your left.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B5")

    Jump("loc_1457")

    label("loc_12BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139D")

    ChrTalk(
        0x9,
        (
            "Freight trains run from here to either of the\x01",
            "border gates, where the Guardian Force is\x01",
            "stationed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "CGF supplies are transported directly to the\x01",
            "gates, so these railways are crucial to their\x01",
            "success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1457")

    label("loc_139D")


    ChrTalk(
        0x9,
        (
            "Freight trains run from here to either of the\x01",
            "border gates, where the Guardian Force is\x01",
            "stationed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please note that ordinary passengers are not\x01",
            "allowed on these freight lines.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1457")

    Jump("loc_C4E")

    label("loc_145C")

    TalkEnd(0x9)
    Return()

    # Function_8_C41 end

    def Function_9_1460(): pass

    label("Function_9_1460")

    Call(0, 10)
    Return()

    # Function_9_1460 end

    def Function_10_1464(): pass

    label("Function_10_1464")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_15BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F8")

    ChrTalk(
        0xA,
        "Oh, excuse me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I understand you may be in a hurry, but\x01",
            "please try to refrain from running on the\x01",
            "platforms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15B8")

    label("loc_14F8")


    ChrTalk(
        0xA,
        (
            "There's been a lot of accidents lately. The last\x01",
            "thing we want is for you to get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "All I want is for passengers to pay attention to\x01",
            "their surroundings and have pleasant travels.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B8")

    Jump("loc_16F7")

    label("loc_15BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165A")

    ChrTalk(
        0xA,
        (
            "Beverages are sold on our trains for your\x01",
            "convenience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Feel free to take advantage of our services\x01",
            "during your long train rides.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F7")

    label("loc_165A")


    ChrTalk(
        0xA,
        (
            "Some businessmen take trains to the\x01",
            "Empire and Republic on a daily basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I deeply respect their contributions to\x01",
            "Crossbell's flourishing economy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F7")

    TalkEnd(0xA)
    Return()

    # Function_10_1464 end

    def Function_11_16FB(): pass

    label("Function_11_16FB")

    Call(0, 12)
    Return()

    # Function_11_16FB end

    def Function_12_16FF(): pass

    label("Function_12_16FF")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1874")

    ChrTalk(
        0xB,
        "Excuse me, could you wait a moment?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "Attention all passengers. Attention all\x01",
            "passengers.\x02\x03",
            "Please step back from the edge of the platform\x01",
            "once the departing train's bells begin to ring.\x02\x03",
            "Refrain from leaning forward at all times, as\x01",
            "high-speed trains pass through. Thank you\x01",
            "for understanding.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_18F3")

    label("loc_1874")


    ChrTalk(
        0xB,
        (
            "Ummm... Anyway, please don't lean forward\x01",
            "while on the platform. High-speed trains tend\x01",
            "to speed through without warning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F3")

    Jump("loc_19B3")

    label("loc_18F8")


    ChrTalk(
        0xB,
        (
            "I used to be really shy, but I managed to get\x01",
            "over it after I was put in charge of making\x01",
            "the announcements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm so glad they trusted me with\x01",
            "this. It's the perfect job for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B3")

    Jump("loc_1D3E")

    label("loc_19B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA6")

    ChrTalk(
        0xB,
        (
            "Thank you very much for your continued\x01",
            "patronage, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Apart from selling tickets, I can instruct\x01",
            "you on how to actually use them, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Feel free to talk to me if you have any\x01",
            "questions.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1B2D")

    label("loc_1AA6")


    ChrTalk(
        0xB,
        (
            "I'm in charge of the intercom\x01",
            "announcements, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you have any questions about the\x01",
            "railway, feel free to ask me anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2D")

    Jump("loc_1D3E")

    label("loc_1B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C97")

    ChrTalk(
        0xB,
        "Excuse me, could you wait a moment?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "Attention all passengers. Attention all\x01",
            "passengers.\x02\x03",
            "Calvard-bound passenger trains depart from\x01",
            "Platform 1, and Erebonia-bound ones leave\x01",
            "from Platform 2.\x02\x03",
            "Please refrain from standing near Platform 3.\x01",
            "That platform is reserved for freight transport and\x01",
            "special express lines.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D3E")

    label("loc_1C97")


    ChrTalk(
        0xB,
        (
            "Passengers are unauthorized to embark or\x01",
            "disembark from Platform 3.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's reserved for Crossbell Guardian Force\x01",
            "freight trains. Please refrain from entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3E")

    TalkEnd(0xB)
    Return()

    # Function_12_16FF end

    def Function_13_1D42(): pass

    label("Function_13_1D42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_21BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E57")
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Thanks for helping out with that Republican\x01",
            "train inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You look as busy as always, Quattro!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I wouldn't say that. Compared to the chaos\x01",
            "that was the Anniversary Festival, this has\x01",
            "been a walk in the park.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    Jump("loc_1F10")

    label("loc_1E57")


    ChrTalk(
        0xFE,
        (
            "By the way, I happened to run into a young lady who\x01",
            "seemed...a little out of it, for lack of a better term.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She struck me as wealthy, but I didn't see any\x01",
            "attendant with her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F10")

    Jump("loc_21B6")

    label("loc_1F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F27")
    Call(0, 14)
    Jump("loc_21B6")

    label("loc_1F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E9")

    ChrTalk(
        0xFE,
        (
            "Even with the hustle and bustle of the festival,\x01",
            "there always was one passenger in particular\x01",
            "that stood out to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was young--the playboy type of guy.\x01",
            "Let me tell you, he had Quattro completely\x01",
            "twisted around his little finger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, Quattro went haywire, but\x01",
            "witnessing it unfold from the sidelines\x01",
            "was entertaining, to say the least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(That description sounds suspiciously like\x01",
            "someone we know.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_21B6")

    label("loc_20E9")


    ChrTalk(
        0xFE,
        (
            "Even with the hustle and bustle of the festival,\x01",
            "there always was one passenger in particular\x01",
            "that stood out to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sure was something to see that redheaded\x01",
            "playboy drive Quattro up the wall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B6")

    Jump("loc_259C")

    label("loc_21BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F6")

    ChrTalk(
        0xFE,
        (
            "Loads of people from the Empire and Republic\x01",
            "visit Crossbell via this station daily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just take a look at our stores and architecture.\x01",
            "You could even call Crossbell City the cultural\x01",
            "melting pot of Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, I wonder what the city was like\x01",
            "when it was founded?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_23B8")

    label("loc_22F6")


    ChrTalk(
        0xFE,
        (
            "Just take a look at our stores and architecture.\x01",
            "You could even call Crossbell City the cultural\x01",
            "melting pot of Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, I wonder what the city was like\x01",
            "when it was founded?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B8")

    Jump("loc_259C")

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D5")

    ChrTalk(
        0xFE,
        (
            "It's been almost five years since I started\x01",
            "working here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At first, I tried memorizing the faces of all\x01",
            "the passengers I came across, but I gave\x01",
            "up on that a looong time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Powered by the ignorance of youth, I was\x01",
            "convinced I could do ANYTHING.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_259C")

    label("loc_24D5")


    ChrTalk(
        0xFE,
        (
            "At first, I tried memorizing the faces of all\x01",
            "the passengers I came across, but I gave\x01",
            "up on that a looong time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Powered by the ignorance of youth, I was\x01",
            "convinced I could do ANYTHING.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_259C")

    TalkEnd(0xFE)
    Return()

    # Function_13_1D42 end

    def Function_14_25A0(): pass

    label("Function_14_25A0")


    ChrTalk(
        0xFE,
        (
            "I remember you guys. Weren't you heading\x01",
            "to Calvard? Do you four travel for work or\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once I got adjusted to traveling by train, it\x01",
            "started to become dull. So, to kill the time,\x01",
            "I picked up reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, I finished this novel not too long\x01",
            "ago. You should give it a read some time.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2D2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D2, 1)
    SetScenarioFlags(0x9D, 4)
    Return()

    # Function_14_25A0 end

    def Function_15_2726(): pass

    label("Function_15_2726")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2B70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_280C")
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Heads-up. An Erebonia-bound train will be\x01",
            "making a short stop for inspection soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Stay sharp and keep your eyes peeled, got it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "(Oh, he's always so strict. I know what to do.)\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_2B6B")

    label("loc_280C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DD")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Well, if it isn't the Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FIt's been a while, Quattro.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed it has. Thank you again for\x01",
            "last time, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm on my way to perform a routine\x01",
            "inspection of Platform 2.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Weren't you on your way to Calvard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FY-Yeah. Let's call it a business trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh? Okay, then.\x01",
            "Those who put in the most effort are the\x01",
            "ones who'll find the most success in life.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2A91")

    label("loc_29DD")


    ChrTalk(
        0xFE,
        (
            "Those who put in the most effort are the\x01",
            "ones who'll find the most success in life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know you're probably busy, but continue\x01",
            "striving for excellence in all that you do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A91")

    Jump("loc_2B6B")

    label("loc_2A96")


    ChrTalk(
        0xFE,
        (
            "I'm on my way to perform a routine\x01",
            "inspection of Platform 2.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm obligated to verify the identity of everyone\x01",
            "wishing to enter the Erebonian Empire. If you\x01",
            "don't have your papers, you aren't getting in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B6B")

    Jump("loc_2BD8")

    label("loc_2B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B81")
    Jump("loc_2BD8")

    label("loc_2B81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2B96")
    Call(0, 30)
    Jump("loc_2BD8")

    label("loc_2B96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2BAA")
    Call(0, 29)
    Jump("loc_2BD8")

    label("loc_2BAA")


    ChrTalk(
        0xFE,
        "*sigh* Looks like we're behind schedule.\x02",
    )

    CloseMessageWindow()

    label("loc_2BD8")

    TalkEnd(0xFE)
    Return()

    # Function_15_2726 end

    def Function_16_2BDC(): pass

    label("Function_16_2BDC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3003")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F3F")
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xE, 0x0, 0)
    TurnDirection(0xF, 0x0, 0)

    ChrTalk(
        0xE,
        (
            "Hey, aren't you the new guys from\x01",
            "the CPD?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 7)), scpexpr(EXPR_END)), "loc_2C68")

    ChrTalk(
        0x101,
        "#0005FUh, yes. That's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2C68")


    ChrTalk(
        0x101,
        (
            "#0005FThat's right.\x02\x03",
            "#0003F(These guys are bracers, right? I think\x01",
            "their names were Scott and...Wenzel?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD6")


    ChrTalk(
        0x102,
        "#0100FAre you two coming back from a job?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Sure are. We just got back from Erebonia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "So, what brings you four over here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FNot much. Just workin' our way through\x01",
            "our pile of support requests.\x02\x03",
            "We were helpin' Quattro with his inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "That so? They actually gave you guys\x01",
            "a proper mission, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Good for you. Keep up the good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Just make sure not to interfere with\x01",
            "ours in the process.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I see they have yet to cease denying our\x01",
            "legitimacy.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Well, then, it's our mission to prove to\x01",
            "them that we are legitimate.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 7)
    Jump("loc_3003")

    label("loc_2F3F")


    ChrTalk(
        0xFE,
        (
            "Have you had the chance to meet\x01",
            "Estelle and Joshua yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So young, yet so incredible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think they're around your age, too.\x01",
            "Haha. You're probably compared to\x01",
            "them wherever you go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3003")

    TalkEnd(0xFE)
    Return()

    # Function_16_2BDC end

    def Function_17_3007(): pass

    label("Function_17_3007")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3025")
    Call(0, 16)
    Jump("loc_3149")

    label("loc_3025")


    ChrTalk(
        0xFE,
        (
            "Inspections, is that right?\x01",
            "Even us bracers have some trouble\x01",
            "trying to take on those requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure the guild would appreciate it if\x01",
            "you handled the ones that accidentally\x01",
            "fall through the cracks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just make sure not to be a burden on\x01",
            "us, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(What a snob.)\x02",
    )

    CloseMessageWindow()

    label("loc_3149")

    TalkEnd(0xFE)
    Return()

    # Function_17_3007 end

    def Function_18_314D(): pass

    label("Function_18_314D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3708")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D8")

    ChrTalk(
        0xFE,
        (
            "We're about to start investigating\x01",
            "that mess with the mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm? Are you in a hurry or something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3708")

    label("loc_31D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3613")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    ChrTalk(
        0x10,
        (
            "Wait. Didn't you just step off a train\x01",
            "that came from the Republic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If you have to make one-day trips out\x01",
            "of the state, you must be really busy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FHaha. Well, we didn't have much choice,\x01",
            "considering the support request.\x02\x03",
            "#0001FWhile you're here, have there been any\x01",
            "developments in the raid investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Well, actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "We found that, not too long ago, some really\x01",
            "dangerous stuff was smuggled into the state\x01",
            "from Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FHow dangerous are we talking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, it was some of those Reinford-made\x01",
            "heavy machine guns used in the raid. So...very.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Revache must have planned the raid well in\x01",
            "advance. They were ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301FFigures that's how they got those guns.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FBut despite their careful planning, Heiyue still\x01",
            "managed to drive them into a corner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Exactly. And that's what strikes me as odd.\x01",
            "For a supposedly premeditated raid, their\x01",
            "performance was rather lackluster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "We need to keep that inconsistency in mind\x01",
            "as we continue to investigate.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x0)
    OP_93(0x11, 0x0, 0x0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x1, 0)
    Jump("loc_3708")

    label("loc_3613")


    ChrTalk(
        0xFE,
        (
            "At any rate, my records show that some of the\x01",
            "freight trains that came from Erebonia weren't\x01",
            "inspected, for whatever reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They had one job! ONE job! Is it too much to\x01",
            "ask for a little thoroughness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(O-Ouch, my eardrums.)\x02",
    )

    CloseMessageWindow()

    label("loc_3708")

    TalkEnd(0xFE)
    Return()

    # Function_18_314D end

    def Function_19_370C(): pass

    label("Function_19_370C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_38D8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3824")

    ChrTalk(
        0xFE,
        (
            "We plan to split the workload with Wenzel and\x01",
            "the others, and then start our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let us know if you figure anything out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(We still don't have any concrete leads about\x01",
            "the pills, so let's not mention that to them yet.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D8")

    label("loc_3824")


    ChrTalk(
        0xFE,
        (
            "The fact that they got their hands on Reinford\x01",
            "Company weaponry rubs me the wrong way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How does Revache do it? Not even the CGF\x01",
            "are able to buy those heavy machine guns.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D8")

    TalkEnd(0xFE)
    Return()

    # Function_19_370C end

    def Function_20_38DC(): pass

    label("Function_20_38DC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3970")
    Jump("loc_39BA")

    label("loc_3970")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3990")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39BA")

    label("loc_3990")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39B0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39BA")

    label("loc_39B0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39BA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA3")

    ChrTalk(
        0xFE,
        (
            "There's a certain elegance in\x01",
            "leaving Erebonia by train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, but I've also taken an airship to Remiferia\x01",
            "before. Trains and airships both have their own\x01",
            "unique charms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B1D")

    label("loc_3AA3")


    ChrTalk(
        0xFE,
        "We'll go to the most splendid of places today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shall we start by visiting Mishelam's\x01",
            "famous Fortuna restaurant?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B1D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_38DC end

    def Function_21_3B25(): pass

    label("Function_21_3B25")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BB9")
    Jump("loc_3C03")

    label("loc_3BB9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BD9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C03")

    label("loc_3BD9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BF9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C03")

    label("loc_3BF9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C03")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF2")

    ChrTalk(
        0xFE,
        "I prefer airships over trains.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, they do run more frequently.\x01",
            "I'll give them that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love it if the airliner between Erebonia and\x01",
            "Crossbell flew more frequently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D17")

    label("loc_3CF2")


    ChrTalk(
        0xFE,
        "My boyfriend is so predictable.\x02",
    )

    CloseMessageWindow()

    label("loc_3D17")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_3B25 end

    def Function_22_3D1F(): pass

    label("Function_22_3D1F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DB3")
    Jump("loc_3DFD")

    label("loc_3DB3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3DD3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DFD")

    label("loc_3DD3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DF3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DFD")

    label("loc_3DF3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DFD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ECA")

    ChrTalk(
        0xFE,
        (
            "I, uh, lost my ticket while on the train\x01",
            "coming from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really hope the station attendants will\x01",
            "have mercy on my scatterbrain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F6E")

    label("loc_3ECA")


    ChrTalk(
        0xFE,
        (
            "The ticket I thought I lost had just fallen\x01",
            "between the seats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew, that was a close one. Now I can\x01",
            "enter Crossbell without security getting\x01",
            "on my case!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F6E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_3D1F end

    def Function_23_3F76(): pass

    label("Function_23_3F76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4047")

    ChrTalk(
        0xFE,
        (
            "I heard that hot springs work miracles\x01",
            "for the hips, so I've decided to go try\x01",
            "one out while I'm in Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My hips are looking forward to relaxing\x01",
            "in the warm, soothing water.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4088")

    label("loc_4047")


    ChrTalk(
        0xFE,
        (
            "Now, then, when does the next train for\x01",
            "the Republic leave?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4088")

    TalkEnd(0xFE)
    Return()

    # Function_23_3F76 end

    def Function_24_408C(): pass

    label("Function_24_408C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4170")

    ChrTalk(
        0xFE,
        (
            "I'm planning to visit Calvard's\x01",
            "Eastern Quarter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I could get tickets to see that Gambler Jack\x01",
            "stage play, that'd be great. It was based off\x01",
            "this bestselling novel of the same name.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_41BB")

    label("loc_4170")


    ChrTalk(
        0xFE,
        "I pre-purchased tickets for the next train.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, I'm so excited!\x02",
    )

    CloseMessageWindow()

    label("loc_41BB")

    Jump("loc_4263")

    label("loc_41C0")


    ChrTalk(
        0xFE,
        (
            "Actually, I'm still not too sure whether the\x01",
            "Eastern Quarter is even safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, what if it's full of rogues and crooks\x01",
            "like the ones in Gambler Jack?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4263")

    TalkEnd(0xFE)
    Return()

    # Function_24_408C end

    def Function_25_4267(): pass

    label("Function_25_4267")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42FB")
    Jump("loc_4345")

    label("loc_42FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_431B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4345")

    label("loc_431B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_433B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4345")

    label("loc_433B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4345")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4463")

    ChrTalk(
        0xFE,
        (
            "My boyfriend--well, ex-boyfriend--dumped me,\x01",
            "so I've decided to try to ease the heartbreak by\x01",
            "traveling abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This isn't the end for me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just watch! I'll find a foreign guy at least ten\x01",
            "times as cool as that jerk!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4517")

    label("loc_4463")


    ChrTalk(
        0xFE,
        (
            "I have to decide whether I want to\x01",
            "go to Erebonia or Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Might as well pick the one with the more\x01",
            "attractive men, but...I'm not exactly sure\x01",
            "how to figure that out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4517")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_4267 end

    def Function_26_451F(): pass

    label("Function_26_451F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A8")

    ChrTalk(
        0xFE,
        "Okay, Grandpa, we made it to the station.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish you didn't have to leave for work,\x01",
            "but have a safe trip!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4601")

    label("loc_45A8")


    ChrTalk(
        0xFE,
        (
            "I'm going to be lonely at home for a while,\x01",
            "but that's okay. Do your best, Grandpa!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4601")

    TalkEnd(0xFE)
    Return()

    # Function_26_451F end

    def Function_27_4605(): pass

    label("Function_27_4605")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46DA")

    ChrTalk(
        0xFE,
        (
            "The Imperial company I used to work for\x01",
            "when I was younger still contacts me for\x01",
            "advice fairly often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a demanding job, but it keeps me sharp.\x01",
            "At my age, it's more than welcome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4771")

    label("loc_46DA")


    ChrTalk(
        0xFE,
        (
            "The Empire-bound train is about to depart. I can't\x01",
            "help but feel rather reluctant about leaving again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Perhaps I should just stay this time.\x02",
    )

    CloseMessageWindow()

    label("loc_4771")

    TalkEnd(0xFE)
    Return()

    # Function_27_4605 end

    def Function_28_4775(): pass

    label("Function_28_4775")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(5300, 1500, 6460, 0)
    MoveCamera(44, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 2500, 0, -500, 90)
    SetChrPos(0x102, 2250, 0, 500, 90)
    SetChrPos(0x103, 1000, 0, -500, 90)
    SetChrPos(0x104, 750, 0, 500, 90)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_68(6300, 1500, 6460, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3900)
    Fade(500)
    OP_68(29620, 5500, -8119, 0)
    MoveCamera(42, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(29590, 5500, 9120, 7000)
    Sleep(6900)
    Fade(500)
    OP_68(12760, 3000, -8000, 0)
    MoveCamera(48, 8, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_68(5320, 1530, 440, 5000)
    Sleep(5000)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_49B8")

    ChrTalk(
        0x103,
        (
            "#5P#0200FThe representative's daughter must\x01",
            "be around here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FThe train heading for Calvard leaves\x01",
            "from Platform 1. Come on!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AC9")

    label("loc_49B8")


    ChrTalk(
        0x101,
        (
            "#11P#0005FThis station never fails to amaze me.\x02\x03",
            "#0004FHas it really already been a month since\x01",
            "I stepped off that train? Wow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FIt has. Anyway, I believe the inspection\x01",
            "officer submitted the request, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FYeah. Let's go ask him about it.\x02",
    )

    CloseMessageWindow()

    label("loc_4AC9")

    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    SetChrPos(0x0, 2500, 0, 0, 90)
    SetScenarioFlags(0x44, 3)
    EventEnd(0x5)
    Return()

    # Function_28_4775 end

    def Function_29_4AFE(): pass

    label("Function_29_4AFE")

    EventBegin(0x0)
    Fade(500)
    OP_68(27680, 5500, 8290, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 28500, 4000, 8500, 0)
    SetChrPos(0x102, 27500, 4000, 8250, 0)
    SetChrPos(0x103, 28500, 4000, 7000, 0)
    SetChrPos(0x104, 27500, 4000, 6750, 0)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    ChrTalk(
        0xD,
        "#5PHmph. They're late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FExcuse me, but are you the inspection officer?\x02\x03",
            "We're here regarding your support request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PAh, so you're the Special Support Section,\x01",
            "then? About time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PMy name's Quattro. I was transferred here\x01",
            "from the Imperial Army to work as the station's\x01",
            "inspection officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PIf you don't mind, I'd like to cut to the chase.\x01",
            "Will you accept my request?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0x0)
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D32")
    Call(0, 32)
    Jump("loc_4D45")

    label("loc_4D32")

    SetChrPos(0x0, 28000, 4000, 8500, 0)
    EventEnd(0x5)

    label("loc_4D45")

    Return()

    # Function_29_4AFE end

    def Function_30_4D46(): pass

    label("Function_30_4D46")

    EventBegin(0x0)
    Fade(500)
    OP_68(27680, 5500, 8290, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 28500, 4000, 8500, 0)
    SetChrPos(0x102, 27500, 4000, 8250, 0)
    SetChrPos(0x103, 28500, 4000, 7000, 0)
    SetChrPos(0x104, 27500, 4000, 6750, 0)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    ChrTalk(
        0xD,
        "#5PWhat do you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PWill you accept my request?\x02",
    )

    CloseMessageWindow()
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E1B")
    Call(0, 32)
    Jump("loc_4E2E")

    label("loc_4E1B")

    SetChrPos(0x0, 28000, 4000, 8500, 0)
    EventEnd(0x5)

    label("loc_4E2E")

    Return()

    # Function_30_4D46 end

    def Function_31_4E2F(): pass

    label("Function_31_4E2F")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EC3")

    ChrTalk(
        0x101,
        (
            "#11P#0000FYou can count on us, Quattro.\x02\x03",
            "Could you talk us through the specifics?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF3")

    label("loc_4EC3")


    ChrTalk(
        0x101,
        (
            "#11P#0006FWe're really sorry, but we have some\x01",
            "other business to attend to right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PThat right? Then I guess I'll have to\x01",
            "figure things out on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PIf you can finish whatever you have to\x01",
            "do soon, come on back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PAfter all, we're both short on time. Try\x01",
            "not to waste any.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4FF3")

    Return()

    # Function_31_4E2F end

    def Function_32_4FF4(): pass

    label("Function_32_4FF4")


    ChrTalk(
        0xD,
        "#5PVery well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PBut, then again...\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#0005FIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PNot really. Just not used to cooperating\x01",
            "with rookies like you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PI suppose it's better than if no one\x01",
            "showed up at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301F(Dude, what the hell? We're goin' out of\x01",
            "our way, and this is how he treats us?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PYou say something, Red?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FYou are better off ignoring anything he says.\x02\x03",
            "#0200FJust to clarify, you submitted a request\x01",
            "asking for assistance in an inspection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PThat's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PA train bound for Erebonia will be\x01",
            "arriving any second now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PAnd I want your help in inspecting the\x01",
            "interior of said train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0005FAnd that would entail...?\x02\x03",
            "#0000FWe'll be looking for any passengers\x01",
            "or luggage considered too dangerous\x01",
            "for Erebonian territory, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PPrecisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PI don't normally have to do this on my\x01",
            "own, but I woke up to a torrent of sick\x01",
            "leaves this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PThat's why I had to issue a request for\x01",
            "outside help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FThat makes sense. Conducting an inspection\x01",
            "like this alone would take way too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PGlad you understand. That makes things easier.\x02",
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Attendant's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Erebonia-bound passenger train will soon be\x01",
            "arriving at Platform 2.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We ask that all passengers wishing to board the\x01",
            "train make their way to the platform.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    SetScenarioFlags(0x5C, 1)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_4FF4 end

    def Function_33_55D1(): pass

    label("Function_33_55D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x1, 0x5, 0x5, 0x0, 0x0)
    OP_68(28050, 5500, 8960, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 28500, 4000, 8500, 0)
    SetChrPos(0x102, 27500, 4000, 8250, 0)
    SetChrPos(0x103, 28500, 4000, 7000, 0)
    SetChrPos(0x104, 27500, 4000, 6750, 0)
    SetChrPos(0xD, 28000, 4000, 10000, 180)
    OP_4B(0xD, 0xFF)
    SetChrSubChip(0xD, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        "#5PThere it is now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5POnce we're on the platform, I'll explain\x01",
            "the specifics of the job. Sorry about the\x01",
            "short notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PNow, follow me.\x02",
    )

    CloseMessageWindow()
    OP_97(0xD, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_5731():
        OP_93(0x101, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5731)

    def lambda_573E():
        OP_93(0x102, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_573E)

    def lambda_574B():
        OP_93(0x103, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_574B)

    def lambda_5758():
        OP_93(0x104, 0xFF79, 0x96)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5758)
    OP_97(0xD, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    Fade(500)
    SetChrPos(0xD, 18000, 0, -8000, 90)
    SetChrFlags(0xD, 0x8000)
    OP_68(19030, 1500, -9110, 0)
    MoveCamera(29, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    OP_68(20030, 1500, -9110, 3000)
    OP_97(0xD, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
    ClearChrFlags(0xD, 0x8000)
    OP_0D()
    Fade(500)
    OP_68(27830, 5500, 7060, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0006FOkay, then. Anyone else expect today\x01",
            "to turn out like this? Because I didn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FI can't stand this dude's high-and-mighty\x01",
            "attitude, but...\x02\x03",
            "#0300F...he's in a bind. Let's give him a hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FIt's settled, then. Shall we head down to\x01",
            "Platform 2?\x02",
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
            "[Inspection Assistance Wanted]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 28000, 4000, 8500, 180)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x10)
    OP_1B(0x0, 0x0, 0x22)
    OP_29(0x9, 0x1, 0x1)
    OP_4C(0xD, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_33_55D1 end

    def Function_34_59D4(): pass

    label("Function_34_59D4")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FThe inspection officer is waiting\x01",
            "for us at Platform 2.\x02\x03",
            "We should be heading there.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 500, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_34_59D4 end

    def Function_35_5A4D(): pass

    label("Function_35_5A4D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "← Calvard Republic - Platform 1\x01",
            "　 Altair (35 min.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_5A4D end

    def Function_36_5ABA(): pass

    label("Function_36_5ABA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Erebonian Empire - Platform 2 →\x01",
            "　 Garrelia Fortress (32 min.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_36_5ABA end

    def Function_37_5B32(): pass

    label("Function_37_5B32")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a timetable for the Crossbell State area.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_37_5B32 end

    def Function_38_5B74(): pass

    label("Function_38_5B74")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　  Inspection Office \x01",
            "   Authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_5B74 end

    def Function_39_5BE3(): pass

    label("Function_39_5BE3")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a route map for the Crossbell State area.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_39_5BE3 end

    SaveToFile()

Try(main)
