from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "a0000_2.bin",                # FileName
        "map1",                    # MapName
        "map1",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [324, 621, 916, 1121, 1471, 1595, 1755, 1894, 2051, 0, 2277, 0, 2323, 2516, 2688, 2824, 0, 2963, 0, 48, 12, 0, 0],
    )

    BuildStringList((
        "a0000_2",                # 0
    ))

    ScpFunction((
        "Function_0_184",          # 00, 0
        "Function_1_2DF",          # 01, 1
        "Function_2_43A",          # 02, 2
        "Function_3_521",          # 03, 3
        "Function_4_6B6",          # 04, 4
        "Function_5_732",          # 05, 5
        "Function_6_7D2",          # 06, 6
        "Function_7_85D",          # 07, 7
        "Function_8_8FA",          # 08, 8
        "Function_9_9DC",          # 09, 9
        "Function_10_A0A",         # 0A, 10
        "Function_11_ACB",         # 0B, 11
        "Function_12_B77",         # 0C, 12
        "Function_13_BFF",         # 0D, 13
        "Function_14_C8A",         # 0E, 14
        "Function_15_D27",         # 0F, 15
        "Function_16_E0C",         # 10, 16
        "Function_17_E3A",         # 11, 17
        "Function_18_EF2",         # 12, 18
        "Function_19_F9E",         # 13, 19
        "Function_20_1386",        # 14, 20
        "Function_21_17B2",        # 15, 21
        "Function_22_19AE",        # 16, 22
        "Function_23_1D1F",        # 17, 23
        "Function_24_211B",        # 18, 24
        "Function_25_24FD",        # 19, 25
        "Function_26_28C0",        # 1A, 26
        "Function_27_2CB4",        # 1B, 27
        "Function_28_30E0",        # 1C, 28
        "Function_29_34FF",        # 1D, 29
        "Function_30_397F",        # 1E, 30
        "Function_31_3DF3",        # 1F, 31
        "Function_32_3E8B",        # 20, 32
        "Function_33_42FB",        # 21, 33
        "Function_34_4763",        # 22, 34
        "Function_35_47FB",        # 23, 35
        "Function_36_4BA7",        # 24, 36
        "Function_37_4F4F",        # 25, 37
        "Function_38_5310",        # 26, 38
        "Function_39_5791",        # 27, 39
        "Function_40_5BA0",        # 28, 40
        "Function_41_5FF3",        # 29, 41
        "Function_42_63FF",        # 2A, 42
        "Function_43_681D",        # 2B, 43
        "Function_44_6A27",        # 2C, 44
        "Function_45_6BE8",        # 2D, 45
        "Function_46_6E6D",        # 2E, 46
        "Function_47_7088",        # 2F, 47
        "Function_48_737D",        # 30, 48
        "Function_49_7643",        # 31, 49
        "Function_50_7929",        # 32, 50
        "Function_51_7ABE",        # 33, 51
        "Function_52_7BCD",        # 34, 52
        "Function_53_7CA9",        # 35, 53
        "Function_54_7D85",        # 36, 54
        "Function_55_BBBB",        # 37, 55
        "Function_56_DB5E",        # 38, 56
        "Function_57_F185",        # 39, 57
        "Function_58_122E9",       # 3A, 58
        "Function_59_12AF9",       # 3B, 59
    ))


    def Function_0_184(): pass

    label("Function_0_184")

    Call(2, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_191")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D1")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼Chapter 0 ①\x01",      # 0
            "▼Chapter 0 ②\x01",      # 1
            "▼Chapter 0 ③\x01",      # 2
            "▼Chapter 1 ①\x01",      # 3
            "▼Chapter 1 ②\x01",      # 4
            "▼Chapter 1 ③\x01",      # 5
            "▼Chapter 2 ①\x01",      # 6
            "▼Chapter 2 ②\x01",      # 7
            "▼Chapter 2 ③\x01",      # 8
            "Cancel\x01",              # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27A"),
        (1, "loc_282"),
        (2, "loc_28A"),
        (3, "loc_292"),
        (4, "loc_29A"),
        (5, "loc_2A2"),
        (6, "loc_2AA"),
        (7, "loc_2B2"),
        (8, "loc_2BA"),
        (SWITCH_DEFAULT, "loc_2C2"),
    )


    label("loc_27A")

    Call(2, 19)
    Jump("loc_2CC")

    label("loc_282")

    Call(2, 20)
    Jump("loc_2CC")

    label("loc_28A")

    Call(2, 21)
    Jump("loc_2CC")

    label("loc_292")

    Call(2, 22)
    Jump("loc_2CC")

    label("loc_29A")

    Call(2, 23)
    Jump("loc_2CC")

    label("loc_2A2")

    Call(2, 24)
    Jump("loc_2CC")

    label("loc_2AA")

    Call(2, 25)
    Jump("loc_2CC")

    label("loc_2B2")

    Call(2, 26)
    Jump("loc_2CC")

    label("loc_2BA")

    Call(2, 27)
    Jump("loc_2CC")

    label("loc_2C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CC")

    Jump("loc_191")

    label("loc_2D1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_0_184 end

    def Function_1_2DF(): pass

    label("Function_1_2DF")

    Call(2, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42C")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼Chapter 3 ①\x01",      # 0
            "▼Chapter 3 ②\x01",      # 1
            "▼Chapter 3 ③\x01",      # 2
            "▼Chapter 3 ④\x01",      # 3
            "▼Chapter 3 ⑤\x01",      # 4
            "▼Intermission\x01",      # 5
            "▼Chapter 4 ①\x01",      # 6
            "▼Chapter 4 ②\x01",      # 7
            "▼Chapter 4 ③\x01",      # 8
            "Cancel\x01",              # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D5"),
        (1, "loc_3DD"),
        (2, "loc_3E5"),
        (3, "loc_3ED"),
        (4, "loc_3F5"),
        (5, "loc_3FD"),
        (6, "loc_405"),
        (7, "loc_40D"),
        (8, "loc_415"),
        (SWITCH_DEFAULT, "loc_41D"),
    )


    label("loc_3D5")

    Call(2, 28)
    Jump("loc_427")

    label("loc_3DD")

    Call(2, 29)
    Jump("loc_427")

    label("loc_3E5")

    Call(2, 30)
    Jump("loc_427")

    label("loc_3ED")

    Call(2, 32)
    Jump("loc_427")

    label("loc_3F5")

    Call(2, 33)
    Jump("loc_427")

    label("loc_3FD")

    Call(2, 35)
    Jump("loc_427")

    label("loc_405")

    Call(2, 36)
    Jump("loc_427")

    label("loc_40D")

    Call(2, 37)
    Jump("loc_427")

    label("loc_415")

    Call(2, 38)
    Jump("loc_427")

    label("loc_41D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_427")

    Jump("loc_2EC")

    label("loc_42C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_1_2DF end

    def Function_2_43A(): pass

    label("Function_2_43A")

    Call(2, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_447")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_513")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼Chapter 5 ①\x01",      # 0
            "▼Chapter 5 ②\x01",      # 1
            "▼Chapter 5 ③\x01",      # 2
            "▼Chapter 5 ④\x01",      # 3
            "▼Chapter 5 ⑤\x01",      # 4
            "Cancel\x01",              # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4DC"),
        (1, "loc_4E4"),
        (2, "loc_4EC"),
        (3, "loc_4F4"),
        (4, "loc_4FC"),
        (SWITCH_DEFAULT, "loc_504"),
    )


    label("loc_4DC")

    Call(2, 39)
    Jump("loc_50E")

    label("loc_4E4")

    Call(2, 40)
    Jump("loc_50E")

    label("loc_4EC")

    Call(2, 41)
    Jump("loc_50E")

    label("loc_4F4")

    Call(2, 42)
    Jump("loc_50E")

    label("loc_4FC")

    Call(2, 43)
    Jump("loc_50E")

    label("loc_504")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50E")

    Jump("loc_447")

    label("loc_513")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_2_43A end

    def Function_3_521(): pass

    label("Function_3_521")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A8")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼Prologue\x01",                         # 0
            "▼Chapter 1\x01",                        # 1
            "▼Chapter 2\x01",                        # 2
            "▼Chapter 3 ①\x01",                     # 3
            "▼Chapter 3 ② & Intermission\x01",      # 4
            "▼Chapter 4\x01",                        # 5
            "▼Finale\x01",                           # 6
            "Set Bonding Points\x01",                 # 7
            "Auction Companion\x01",                  # 8
            "Intermission Companion\x01",             # 9
            "Cancel\x01",                             # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_634"),
        (1, "loc_63F"),
        (2, "loc_64A"),
        (3, "loc_655"),
        (4, "loc_660"),
        (5, "loc_66B"),
        (6, "loc_676"),
        (7, "loc_681"),
        (8, "loc_689"),
        (9, "loc_691"),
        (SWITCH_DEFAULT, "loc_699"),
    )


    label("loc_634")

    Call(2, 4)
    Call(2, 44)
    Jump("loc_6A3")

    label("loc_63F")

    Call(2, 4)
    Call(2, 45)
    Jump("loc_6A3")

    label("loc_64A")

    Call(2, 4)
    Call(2, 46)
    Jump("loc_6A3")

    label("loc_655")

    Call(2, 4)
    Call(2, 47)
    Jump("loc_6A3")

    label("loc_660")

    Call(2, 4)
    Call(2, 48)
    Jump("loc_6A3")

    label("loc_66B")

    Call(2, 4)
    Call(2, 49)
    Jump("loc_6A3")

    label("loc_676")

    Call(2, 4)
    Call(2, 50)
    Jump("loc_6A3")

    label("loc_681")

    Call(2, 51)
    Jump("loc_6A3")

    label("loc_689")

    Call(2, 52)
    Jump("loc_6A3")

    label("loc_691")

    Call(2, 53)
    Jump("loc_6A3")

    label("loc_699")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A3")

    Jump("loc_52B")

    label("loc_6A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_3_521 end

    def Function_4_6B6(): pass

    label("Function_4_6B6")

    ClearScenarioFlags(0x5C, 0)
    ClearScenarioFlags(0x5C, 1)
    ClearScenarioFlags(0x5C, 2)
    ClearScenarioFlags(0x5C, 3)
    ClearScenarioFlags(0x5C, 4)
    ClearScenarioFlags(0x5C, 5)
    ClearScenarioFlags(0x5C, 6)
    ClearScenarioFlags(0x5C, 7)
    ClearScenarioFlags(0x5D, 1)
    ClearScenarioFlags(0x5D, 2)
    ClearScenarioFlags(0x5D, 3)
    ClearScenarioFlags(0x5D, 4)
    ClearScenarioFlags(0x5D, 5)
    ClearScenarioFlags(0x5D, 6)
    ClearScenarioFlags(0x5D, 7)
    ClearScenarioFlags(0x5E, 0)
    ClearScenarioFlags(0x5E, 1)
    ClearScenarioFlags(0x5E, 2)
    ClearScenarioFlags(0x5E, 3)
    ClearScenarioFlags(0x5E, 4)
    ClearScenarioFlags(0x5E, 5)
    ClearScenarioFlags(0x5E, 6)
    ClearScenarioFlags(0x5E, 7)
    ClearScenarioFlags(0x5F, 0)
    ClearScenarioFlags(0x5F, 1)
    Call(2, 12)
    Call(2, 13)
    Call(2, 14)
    Call(2, 15)
    Call(2, 16)
    Call(2, 17)
    Call(2, 18)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_6B6 end

    def Function_5_732(): pass

    label("Function_5_732")

    SetScenarioFlags(0x40, 0)
    SetScenarioFlags(0x40, 1)
    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 7)
    SetScenarioFlags(0x41, 0)
    SetScenarioFlags(0x41, 1)
    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)
    SetScenarioFlags(0x41, 4)
    SetScenarioFlags(0x41, 5)
    OP_29(0x1, 0x4, 0x2)
    OP_29(0x1, 0x4, 0x10)
    OP_29(0x1, 0x4, 0x20)
    SetScenarioFlags(0x41, 6)
    SetScenarioFlags(0x41, 7)
    SetScenarioFlags(0x42, 0)
    SetScenarioFlags(0x42, 1)
    SetScenarioFlags(0x42, 2)
    SetScenarioFlags(0x42, 3)
    SetScenarioFlags(0x42, 4)
    SetScenarioFlags(0x42, 5)
    SetScenarioFlags(0x42, 6)
    SetScenarioFlags(0x42, 7)
    SetScenarioFlags(0x43, 0)
    SetScenarioFlags(0x43, 1)
    SetScenarioFlags(0x43, 2)
    SetScenarioFlags(0x44, 0)
    SetScenarioFlags(0x44, 1)
    SetScenarioFlags(0x44, 2)
    SetScenarioFlags(0x44, 4)
    SetScenarioFlags(0x44, 5)
    SetScenarioFlags(0x44, 6)
    SetScenarioFlags(0x44, 7)
    SetScenarioFlags(0x45, 0)
    SetScenarioFlags(0x45, 1)
    SetScenarioFlags(0x45, 2)
    SetScenarioFlags(0x45, 3)
    SetScenarioFlags(0x47, 3)
    SetScenarioFlags(0x47, 4)
    SetScenarioFlags(0x45, 5)
    SetScenarioFlags(0x45, 6)
    SetScenarioFlags(0x45, 7)
    SetScenarioFlags(0x46, 0)
    SetScenarioFlags(0x47, 5)
    SetScenarioFlags(0x4C, 1)
    SetScenarioFlags(0x46, 1)
    SetScenarioFlags(0x4C, 2)
    Return()

    # Function_5_732 end

    def Function_6_7D2(): pass

    label("Function_6_7D2")

    SetScenarioFlags(0x60, 0)
    SetScenarioFlags(0x60, 1)
    SetScenarioFlags(0x60, 2)
    SetScenarioFlags(0x60, 3)
    SetScenarioFlags(0x60, 4)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)
    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x61, 0)
    SetScenarioFlags(0x61, 1)
    SetScenarioFlags(0x61, 2)
    SetScenarioFlags(0x61, 3)
    SetScenarioFlags(0x61, 4)
    SetScenarioFlags(0x61, 5)
    SetScenarioFlags(0x61, 6)
    SetScenarioFlags(0x61, 7)
    SetScenarioFlags(0x62, 0)
    SetScenarioFlags(0x62, 1)
    SetScenarioFlags(0x62, 2)
    SetScenarioFlags(0x62, 3)
    SetScenarioFlags(0x62, 4)
    SetScenarioFlags(0x62, 5)
    SetScenarioFlags(0x62, 6)
    SetScenarioFlags(0x62, 7)
    SetScenarioFlags(0x63, 0)
    SetScenarioFlags(0x63, 1)
    SetScenarioFlags(0x63, 2)
    SetScenarioFlags(0x63, 3)
    SetScenarioFlags(0x63, 4)
    SetScenarioFlags(0x63, 5)
    SetScenarioFlags(0x63, 6)
    SetScenarioFlags(0x63, 7)
    SetScenarioFlags(0x64, 0)
    SetScenarioFlags(0x64, 1)
    SetScenarioFlags(0x64, 2)
    SetScenarioFlags(0x64, 3)
    SetScenarioFlags(0x64, 4)
    SetScenarioFlags(0x64, 5)
    SetScenarioFlags(0x64, 6)
    SetScenarioFlags(0x64, 7)
    SetScenarioFlags(0x65, 0)
    SetScenarioFlags(0x65, 1)
    SetScenarioFlags(0x65, 2)
    SetScenarioFlags(0x65, 3)
    SetScenarioFlags(0x65, 4)
    SetScenarioFlags(0x65, 5)
    Return()

    # Function_6_7D2 end

    def Function_7_85D(): pass

    label("Function_7_85D")

    SetScenarioFlags(0x80, 0)
    SetScenarioFlags(0x80, 1)
    SetScenarioFlags(0x80, 2)
    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)
    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x80, 7)
    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)
    SetScenarioFlags(0x81, 2)
    SetScenarioFlags(0x81, 3)
    SetScenarioFlags(0x81, 4)
    SetScenarioFlags(0x81, 5)
    SetScenarioFlags(0x81, 6)
    SetScenarioFlags(0x81, 7)
    SetScenarioFlags(0x82, 0)
    SetScenarioFlags(0x82, 1)
    SetScenarioFlags(0x82, 2)
    SetScenarioFlags(0x82, 3)
    SetScenarioFlags(0x82, 4)
    SetScenarioFlags(0x82, 5)
    SetScenarioFlags(0x82, 6)
    SetScenarioFlags(0x82, 7)
    SetScenarioFlags(0x83, 0)
    SetScenarioFlags(0x83, 1)
    SetScenarioFlags(0x83, 2)
    SetScenarioFlags(0x83, 3)
    SetScenarioFlags(0x83, 4)
    SetScenarioFlags(0x83, 5)
    SetScenarioFlags(0x83, 6)
    SetScenarioFlags(0x83, 7)
    SetScenarioFlags(0x84, 0)
    SetScenarioFlags(0x84, 1)
    SetScenarioFlags(0x84, 2)
    SetScenarioFlags(0x84, 3)
    SetScenarioFlags(0x84, 4)
    SetScenarioFlags(0x84, 5)
    SetScenarioFlags(0x84, 6)
    SetScenarioFlags(0x84, 7)
    SetScenarioFlags(0x85, 0)
    SetScenarioFlags(0x85, 1)
    SetScenarioFlags(0x85, 2)
    SetScenarioFlags(0x85, 3)
    SetScenarioFlags(0x85, 4)
    SetScenarioFlags(0x85, 5)
    SetScenarioFlags(0x85, 6)
    SetScenarioFlags(0x85, 7)
    SetScenarioFlags(0x86, 0)
    SetScenarioFlags(0x86, 1)
    SetScenarioFlags(0x87, 3)
    SetScenarioFlags(0x87, 5)
    Return()

    # Function_7_85D end

    def Function_8_8FA(): pass

    label("Function_8_8FA")

    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xB9, 3)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xB9, 4)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xB9, 5)
    SetScenarioFlags(0xA2, 4)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xAC, 5)
    SetScenarioFlags(0xAC, 6)
    SetScenarioFlags(0xB9, 6)
    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xB9, 7)
    SetScenarioFlags(0xA2, 7)
    SetScenarioFlags(0xA3, 0)
    SetScenarioFlags(0xA3, 1)
    SetScenarioFlags(0xA3, 2)
    SetScenarioFlags(0xA3, 3)
    SetScenarioFlags(0xA3, 4)
    SetScenarioFlags(0xA3, 5)
    SetScenarioFlags(0xA3, 6)
    SetScenarioFlags(0xA3, 7)
    SetScenarioFlags(0xA4, 0)
    SetScenarioFlags(0xA4, 1)
    SetScenarioFlags(0xA4, 2)
    SetScenarioFlags(0xA4, 3)
    SetScenarioFlags(0xA4, 4)
    SetScenarioFlags(0xA4, 5)
    SetScenarioFlags(0xA4, 6)
    SetScenarioFlags(0xA4, 7)
    SetScenarioFlags(0xA5, 0)
    SetScenarioFlags(0xA5, 1)
    SetScenarioFlags(0xA5, 2)
    SetScenarioFlags(0xA5, 3)
    SetScenarioFlags(0xA5, 4)
    SetScenarioFlags(0xA5, 5)
    SetScenarioFlags(0xA5, 6)
    SetScenarioFlags(0xA5, 7)
    SetScenarioFlags(0xA6, 0)
    SetScenarioFlags(0xA6, 1)
    SetScenarioFlags(0xA6, 2)
    SetScenarioFlags(0xA6, 3)
    SetScenarioFlags(0xA6, 4)
    SetScenarioFlags(0xA6, 5)
    SetScenarioFlags(0xA6, 6)
    SetScenarioFlags(0xA6, 7)
    SetScenarioFlags(0xA7, 0)
    SetScenarioFlags(0xA7, 1)
    SetScenarioFlags(0xA7, 2)
    SetScenarioFlags(0xA7, 3)
    SetScenarioFlags(0xA7, 4)
    SetScenarioFlags(0xA7, 5)
    SetScenarioFlags(0xA9, 1)
    SetScenarioFlags(0xA9, 2)
    SetScenarioFlags(0xA9, 3)
    SetScenarioFlags(0xAA, 0)
    SetScenarioFlags(0xAA, 1)
    SetScenarioFlags(0xAA, 2)
    Return()

    # Function_8_8FA end

    def Function_9_9DC(): pass

    label("Function_9_9DC")

    SetScenarioFlags(0xA7, 6)
    SetScenarioFlags(0xA7, 7)
    SetScenarioFlags(0xA8, 0)
    SetScenarioFlags(0xA8, 1)
    SetScenarioFlags(0xA8, 2)
    SetScenarioFlags(0xA8, 3)
    SetScenarioFlags(0xA8, 4)
    SetScenarioFlags(0xA8, 5)
    SetScenarioFlags(0xA8, 6)
    SetScenarioFlags(0xA8, 7)
    SetScenarioFlags(0xA9, 0)
    SetScenarioFlags(0xA9, 4)
    SetScenarioFlags(0xA9, 5)
    SetScenarioFlags(0xA9, 6)
    SetScenarioFlags(0xA9, 7)
    Return()

    # Function_9_9DC end

    def Function_10_A0A(): pass

    label("Function_10_A0A")

    SetScenarioFlags(0xC0, 0)
    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)
    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 5)
    SetScenarioFlags(0xC1, 6)
    SetScenarioFlags(0xC1, 7)
    SetScenarioFlags(0xC2, 0)
    SetScenarioFlags(0xC2, 1)
    SetScenarioFlags(0xC2, 2)
    SetScenarioFlags(0xC2, 3)
    SetScenarioFlags(0xC2, 4)
    SetScenarioFlags(0xC2, 5)
    SetScenarioFlags(0xC2, 6)
    SetScenarioFlags(0xC2, 7)
    SetScenarioFlags(0xC3, 0)
    SetScenarioFlags(0xC3, 1)
    SetScenarioFlags(0xC3, 2)
    SetScenarioFlags(0xC3, 3)
    SetScenarioFlags(0xC3, 4)
    SetScenarioFlags(0xC3, 5)
    SetScenarioFlags(0xC3, 6)
    SetScenarioFlags(0xC3, 7)
    SetScenarioFlags(0xC4, 0)
    SetScenarioFlags(0xC4, 1)
    SetScenarioFlags(0xC4, 2)
    SetScenarioFlags(0xC4, 3)
    SetScenarioFlags(0xC4, 4)
    SetScenarioFlags(0xC4, 5)
    SetScenarioFlags(0xC4, 6)
    SetScenarioFlags(0xC4, 7)
    SetScenarioFlags(0xC5, 0)
    SetScenarioFlags(0xC5, 1)
    SetScenarioFlags(0xC5, 2)
    SetScenarioFlags(0xC5, 3)
    SetScenarioFlags(0xC6, 5)
    SetScenarioFlags(0xC5, 4)
    SetScenarioFlags(0xC5, 5)
    SetScenarioFlags(0xC5, 6)
    SetScenarioFlags(0xC5, 7)
    SetScenarioFlags(0xC6, 0)
    SetScenarioFlags(0xC6, 1)
    SetScenarioFlags(0xC6, 2)
    SetScenarioFlags(0xC6, 3)
    SetScenarioFlags(0xC6, 4)
    SetScenarioFlags(0xC6, 6)
    SetScenarioFlags(0xC6, 7)
    SetScenarioFlags(0xC8, 0)
    SetScenarioFlags(0xC8, 1)
    SetScenarioFlags(0xC8, 2)
    SetScenarioFlags(0xC8, 3)
    SetScenarioFlags(0xC8, 4)
    Return()

    # Function_10_A0A end

    def Function_11_ACB(): pass

    label("Function_11_ACB")

    SetScenarioFlags(0xE0, 0)
    SetScenarioFlags(0xE0, 1)
    SetScenarioFlags(0xE0, 2)
    SetScenarioFlags(0xE0, 3)
    SetScenarioFlags(0xE0, 4)
    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)
    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)
    SetScenarioFlags(0xE1, 1)
    SetScenarioFlags(0xE1, 2)
    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)
    SetScenarioFlags(0xE1, 5)
    SetScenarioFlags(0xE1, 6)
    SetScenarioFlags(0xE1, 7)
    SetScenarioFlags(0xE2, 0)
    SetScenarioFlags(0xE2, 1)
    SetScenarioFlags(0xE2, 2)
    SetScenarioFlags(0xE2, 3)
    SetScenarioFlags(0xE2, 4)
    SetScenarioFlags(0xE2, 5)
    SetScenarioFlags(0xE2, 6)
    SetScenarioFlags(0xE2, 7)
    SetScenarioFlags(0xE3, 0)
    SetScenarioFlags(0xE3, 1)
    SetScenarioFlags(0xE3, 2)
    SetScenarioFlags(0xE3, 3)
    SetScenarioFlags(0xE3, 4)
    SetScenarioFlags(0xE3, 5)
    SetScenarioFlags(0xE3, 6)
    SetScenarioFlags(0xE3, 7)
    SetScenarioFlags(0xE4, 0)
    SetScenarioFlags(0xE4, 1)
    SetScenarioFlags(0xE4, 2)
    SetScenarioFlags(0xE4, 3)
    SetScenarioFlags(0xE4, 4)
    SetScenarioFlags(0xE7, 5)
    SetScenarioFlags(0xE4, 5)
    SetScenarioFlags(0xE4, 6)
    SetScenarioFlags(0xE4, 7)
    SetScenarioFlags(0xE5, 0)
    SetScenarioFlags(0xE5, 1)
    SetScenarioFlags(0xE5, 2)
    SetScenarioFlags(0xE5, 3)
    SetScenarioFlags(0xE5, 4)
    SetScenarioFlags(0xE5, 5)
    SetScenarioFlags(0xE5, 6)
    SetScenarioFlags(0xE5, 7)
    SetScenarioFlags(0xE6, 0)
    SetScenarioFlags(0xE6, 1)
    SetScenarioFlags(0xE6, 2)
    SetScenarioFlags(0xE6, 3)
    SetScenarioFlags(0xE6, 4)
    SetScenarioFlags(0xE6, 5)
    SetScenarioFlags(0xE6, 6)
    SetScenarioFlags(0xE6, 7)
    Return()

    # Function_11_ACB end

    def Function_12_B77(): pass

    label("Function_12_B77")

    ClearScenarioFlags(0x40, 0)
    ClearScenarioFlags(0x40, 1)
    ClearScenarioFlags(0x40, 2)
    ClearScenarioFlags(0x40, 3)
    ClearScenarioFlags(0x40, 4)
    ClearScenarioFlags(0x40, 5)
    ClearScenarioFlags(0x40, 6)
    ClearScenarioFlags(0x40, 7)
    ClearScenarioFlags(0x41, 0)
    ClearScenarioFlags(0x41, 1)
    ClearScenarioFlags(0x41, 2)
    ClearScenarioFlags(0x41, 3)
    ClearScenarioFlags(0x41, 4)
    ClearScenarioFlags(0x41, 5)
    OP_29(0x1, 0x3, 0x2)
    OP_29(0x1, 0x3, 0x10)
    OP_29(0x1, 0x3, 0x20)
    ClearScenarioFlags(0x41, 6)
    ClearScenarioFlags(0x41, 7)
    ClearScenarioFlags(0x42, 0)
    ClearScenarioFlags(0x42, 1)
    ClearScenarioFlags(0x42, 2)
    ClearScenarioFlags(0x42, 3)
    ClearScenarioFlags(0x42, 4)
    ClearScenarioFlags(0x42, 5)
    ClearScenarioFlags(0x42, 6)
    ClearScenarioFlags(0x42, 7)
    ClearScenarioFlags(0x43, 0)
    ClearScenarioFlags(0x43, 1)
    ClearScenarioFlags(0x43, 2)
    ClearScenarioFlags(0x44, 0)
    ClearScenarioFlags(0x44, 1)
    ClearScenarioFlags(0x44, 2)
    ClearScenarioFlags(0x45, 5)
    ClearScenarioFlags(0x45, 6)
    ClearScenarioFlags(0x45, 7)
    ClearScenarioFlags(0x46, 0)
    ClearScenarioFlags(0x47, 5)
    ClearScenarioFlags(0x4C, 1)
    ClearScenarioFlags(0x46, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_B77 end

    def Function_13_BFF(): pass

    label("Function_13_BFF")

    ClearScenarioFlags(0x60, 0)
    ClearScenarioFlags(0x60, 1)
    ClearScenarioFlags(0x60, 2)
    ClearScenarioFlags(0x60, 3)
    ClearScenarioFlags(0x60, 4)
    ClearScenarioFlags(0x60, 5)
    ClearScenarioFlags(0x60, 6)
    ClearScenarioFlags(0x60, 7)
    ClearScenarioFlags(0x61, 0)
    ClearScenarioFlags(0x61, 1)
    ClearScenarioFlags(0x61, 2)
    ClearScenarioFlags(0x61, 3)
    ClearScenarioFlags(0x61, 4)
    ClearScenarioFlags(0x61, 5)
    ClearScenarioFlags(0x61, 6)
    ClearScenarioFlags(0x61, 7)
    ClearScenarioFlags(0x62, 0)
    ClearScenarioFlags(0x62, 1)
    ClearScenarioFlags(0x62, 2)
    ClearScenarioFlags(0x62, 3)
    ClearScenarioFlags(0x62, 4)
    ClearScenarioFlags(0x62, 5)
    ClearScenarioFlags(0x62, 6)
    ClearScenarioFlags(0x62, 7)
    ClearScenarioFlags(0x63, 0)
    ClearScenarioFlags(0x63, 1)
    ClearScenarioFlags(0x63, 2)
    ClearScenarioFlags(0x63, 3)
    ClearScenarioFlags(0x63, 4)
    ClearScenarioFlags(0x63, 5)
    ClearScenarioFlags(0x63, 6)
    ClearScenarioFlags(0x63, 7)
    ClearScenarioFlags(0x64, 0)
    ClearScenarioFlags(0x64, 1)
    ClearScenarioFlags(0x64, 2)
    ClearScenarioFlags(0x64, 3)
    ClearScenarioFlags(0x64, 4)
    ClearScenarioFlags(0x64, 5)
    ClearScenarioFlags(0x64, 6)
    ClearScenarioFlags(0x64, 7)
    ClearScenarioFlags(0x65, 0)
    ClearScenarioFlags(0x65, 1)
    ClearScenarioFlags(0x65, 2)
    ClearScenarioFlags(0x65, 3)
    ClearScenarioFlags(0x65, 4)
    ClearScenarioFlags(0x65, 5)
    Return()

    # Function_13_BFF end

    def Function_14_C8A(): pass

    label("Function_14_C8A")

    ClearScenarioFlags(0x80, 0)
    ClearScenarioFlags(0x80, 1)
    ClearScenarioFlags(0x80, 2)
    ClearScenarioFlags(0x80, 3)
    ClearScenarioFlags(0x80, 4)
    ClearScenarioFlags(0x80, 5)
    ClearScenarioFlags(0x80, 6)
    ClearScenarioFlags(0x80, 7)
    ClearScenarioFlags(0x81, 0)
    ClearScenarioFlags(0x81, 1)
    ClearScenarioFlags(0x81, 2)
    ClearScenarioFlags(0x81, 3)
    ClearScenarioFlags(0x81, 4)
    ClearScenarioFlags(0x81, 5)
    ClearScenarioFlags(0x81, 6)
    ClearScenarioFlags(0x81, 7)
    ClearScenarioFlags(0x82, 0)
    ClearScenarioFlags(0x82, 1)
    ClearScenarioFlags(0x82, 2)
    ClearScenarioFlags(0x82, 3)
    ClearScenarioFlags(0x82, 4)
    ClearScenarioFlags(0x82, 5)
    ClearScenarioFlags(0x82, 6)
    ClearScenarioFlags(0x82, 7)
    ClearScenarioFlags(0x83, 0)
    ClearScenarioFlags(0x83, 1)
    ClearScenarioFlags(0x83, 2)
    ClearScenarioFlags(0x83, 3)
    ClearScenarioFlags(0x83, 4)
    ClearScenarioFlags(0x83, 5)
    ClearScenarioFlags(0x83, 6)
    ClearScenarioFlags(0x83, 7)
    ClearScenarioFlags(0x84, 0)
    ClearScenarioFlags(0x84, 1)
    ClearScenarioFlags(0x84, 2)
    ClearScenarioFlags(0x84, 3)
    ClearScenarioFlags(0x84, 4)
    ClearScenarioFlags(0x84, 5)
    ClearScenarioFlags(0x84, 6)
    ClearScenarioFlags(0x84, 7)
    ClearScenarioFlags(0x85, 0)
    ClearScenarioFlags(0x85, 1)
    ClearScenarioFlags(0x85, 2)
    ClearScenarioFlags(0x85, 3)
    ClearScenarioFlags(0x85, 4)
    ClearScenarioFlags(0x85, 5)
    ClearScenarioFlags(0x85, 6)
    ClearScenarioFlags(0x85, 7)
    ClearScenarioFlags(0x86, 0)
    ClearScenarioFlags(0x86, 1)
    ClearScenarioFlags(0x87, 3)
    ClearScenarioFlags(0x87, 5)
    Return()

    # Function_14_C8A end

    def Function_15_D27(): pass

    label("Function_15_D27")

    ClearScenarioFlags(0xA0, 0)
    ClearScenarioFlags(0xA0, 1)
    ClearScenarioFlags(0xA0, 2)
    ClearScenarioFlags(0xA0, 3)
    ClearScenarioFlags(0xA0, 4)
    ClearScenarioFlags(0xA0, 5)
    ClearScenarioFlags(0xA0, 6)
    ClearScenarioFlags(0xA0, 7)
    ClearScenarioFlags(0xA1, 0)
    ClearScenarioFlags(0xA1, 1)
    ClearScenarioFlags(0xA1, 2)
    ClearScenarioFlags(0xA1, 3)
    ClearScenarioFlags(0xA1, 4)
    ClearScenarioFlags(0xA1, 5)
    ClearScenarioFlags(0xA1, 6)
    ClearScenarioFlags(0xA1, 7)
    ClearScenarioFlags(0xB9, 3)
    ClearScenarioFlags(0xA2, 0)
    ClearScenarioFlags(0xB9, 4)
    ClearScenarioFlags(0xA2, 1)
    ClearScenarioFlags(0xA2, 2)
    ClearScenarioFlags(0xA2, 3)
    ClearScenarioFlags(0xB9, 5)
    ClearScenarioFlags(0xA2, 4)
    ClearScenarioFlags(0xA2, 5)
    ClearScenarioFlags(0xAC, 5)
    ClearScenarioFlags(0xB1, 0)
    ClearScenarioFlags(0xAC, 6)
    ClearScenarioFlags(0xB9, 6)
    ClearScenarioFlags(0xA2, 6)
    ClearScenarioFlags(0xB9, 7)
    ClearScenarioFlags(0xA2, 7)
    ClearScenarioFlags(0xA3, 0)
    ClearScenarioFlags(0xA3, 1)
    ClearScenarioFlags(0xA3, 2)
    ClearScenarioFlags(0xA3, 3)
    ClearScenarioFlags(0xA3, 4)
    ClearScenarioFlags(0xA3, 5)
    ClearScenarioFlags(0xA3, 6)
    ClearScenarioFlags(0xA3, 7)
    ClearScenarioFlags(0xA4, 0)
    ClearScenarioFlags(0xA4, 1)
    ClearScenarioFlags(0xA4, 2)
    ClearScenarioFlags(0xA4, 3)
    ClearScenarioFlags(0xA4, 4)
    ClearScenarioFlags(0xA4, 5)
    ClearScenarioFlags(0xA4, 6)
    ClearScenarioFlags(0xA4, 7)
    ClearScenarioFlags(0xA5, 0)
    ClearScenarioFlags(0xA5, 1)
    ClearScenarioFlags(0xA5, 2)
    ClearScenarioFlags(0xA5, 3)
    ClearScenarioFlags(0xA5, 4)
    ClearScenarioFlags(0xA5, 5)
    ClearScenarioFlags(0xA5, 6)
    ClearScenarioFlags(0xA5, 7)
    ClearScenarioFlags(0xA6, 0)
    ClearScenarioFlags(0xA6, 1)
    ClearScenarioFlags(0xA6, 2)
    ClearScenarioFlags(0xA6, 3)
    ClearScenarioFlags(0xA6, 4)
    ClearScenarioFlags(0xA6, 5)
    ClearScenarioFlags(0xA6, 6)
    ClearScenarioFlags(0xA6, 7)
    ClearScenarioFlags(0xA7, 0)
    ClearScenarioFlags(0xA7, 1)
    ClearScenarioFlags(0xA7, 2)
    ClearScenarioFlags(0xA7, 3)
    ClearScenarioFlags(0xA7, 4)
    ClearScenarioFlags(0xA7, 5)
    ClearScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 2)
    ClearScenarioFlags(0xA9, 3)
    ClearScenarioFlags(0xAA, 0)
    ClearScenarioFlags(0xAA, 1)
    ClearScenarioFlags(0xAA, 2)
    Return()

    # Function_15_D27 end

    def Function_16_E0C(): pass

    label("Function_16_E0C")

    ClearScenarioFlags(0xA7, 6)
    ClearScenarioFlags(0xA7, 7)
    ClearScenarioFlags(0xA8, 0)
    ClearScenarioFlags(0xA8, 1)
    ClearScenarioFlags(0xA8, 2)
    ClearScenarioFlags(0xA8, 3)
    ClearScenarioFlags(0xA8, 4)
    ClearScenarioFlags(0xA8, 5)
    ClearScenarioFlags(0xA8, 6)
    ClearScenarioFlags(0xA8, 7)
    ClearScenarioFlags(0xA9, 0)
    ClearScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 5)
    ClearScenarioFlags(0xA9, 6)
    ClearScenarioFlags(0xA9, 7)
    Return()

    # Function_16_E0C end

    def Function_17_E3A(): pass

    label("Function_17_E3A")

    ClearScenarioFlags(0xC0, 0)
    ClearScenarioFlags(0xC0, 1)
    ClearScenarioFlags(0xC0, 2)
    ClearScenarioFlags(0xC0, 3)
    ClearScenarioFlags(0xC0, 4)
    ClearScenarioFlags(0xC0, 5)
    ClearScenarioFlags(0xC0, 6)
    ClearScenarioFlags(0xC0, 7)
    ClearScenarioFlags(0xC1, 0)
    ClearScenarioFlags(0xC1, 1)
    ClearScenarioFlags(0xC1, 2)
    ClearScenarioFlags(0xC1, 3)
    ClearScenarioFlags(0xC1, 4)
    ClearScenarioFlags(0xC1, 5)
    ClearScenarioFlags(0xC1, 6)
    ClearScenarioFlags(0xC1, 7)
    ClearScenarioFlags(0xC2, 0)
    ClearScenarioFlags(0xC2, 1)
    ClearScenarioFlags(0xC2, 2)
    ClearScenarioFlags(0xC2, 3)
    ClearScenarioFlags(0xC2, 4)
    ClearScenarioFlags(0xC2, 5)
    ClearScenarioFlags(0xC2, 6)
    ClearScenarioFlags(0xC2, 7)
    ClearScenarioFlags(0xC3, 0)
    ClearScenarioFlags(0xC3, 1)
    ClearScenarioFlags(0xC3, 2)
    ClearScenarioFlags(0xC3, 3)
    ClearScenarioFlags(0xC3, 4)
    ClearScenarioFlags(0xC3, 5)
    ClearScenarioFlags(0xC3, 6)
    ClearScenarioFlags(0xC3, 7)
    ClearScenarioFlags(0xC4, 0)
    ClearScenarioFlags(0xC4, 1)
    ClearScenarioFlags(0xC4, 2)
    ClearScenarioFlags(0xC4, 3)
    ClearScenarioFlags(0xC4, 4)
    ClearScenarioFlags(0xC4, 5)
    ClearScenarioFlags(0xC4, 6)
    ClearScenarioFlags(0xC4, 7)
    ClearScenarioFlags(0xC5, 0)
    ClearScenarioFlags(0xC5, 1)
    ClearScenarioFlags(0xC5, 2)
    ClearScenarioFlags(0xC5, 3)
    ClearScenarioFlags(0xC6, 5)
    ClearScenarioFlags(0xC5, 4)
    ClearScenarioFlags(0xC5, 5)
    ClearScenarioFlags(0xC5, 6)
    ClearScenarioFlags(0xC5, 7)
    ClearScenarioFlags(0xC6, 0)
    ClearScenarioFlags(0xC6, 1)
    ClearScenarioFlags(0xC6, 2)
    ClearScenarioFlags(0xC6, 3)
    ClearScenarioFlags(0xC6, 4)
    ClearScenarioFlags(0xC6, 6)
    ClearScenarioFlags(0xC6, 7)
    ClearScenarioFlags(0xC8, 0)
    ClearScenarioFlags(0xC8, 1)
    ClearScenarioFlags(0xC8, 2)
    ClearScenarioFlags(0xC8, 3)
    ClearScenarioFlags(0xC8, 4)
    Return()

    # Function_17_E3A end

    def Function_18_EF2(): pass

    label("Function_18_EF2")

    ClearScenarioFlags(0xE0, 0)
    ClearScenarioFlags(0xE0, 1)
    ClearScenarioFlags(0xE0, 2)
    ClearScenarioFlags(0xE0, 3)
    ClearScenarioFlags(0xE0, 4)
    ClearScenarioFlags(0xE0, 5)
    ClearScenarioFlags(0xE0, 6)
    ClearScenarioFlags(0xE0, 7)
    ClearScenarioFlags(0xE1, 0)
    ClearScenarioFlags(0xE1, 1)
    ClearScenarioFlags(0xE1, 2)
    ClearScenarioFlags(0xE1, 3)
    ClearScenarioFlags(0xE1, 4)
    ClearScenarioFlags(0xE1, 5)
    ClearScenarioFlags(0xE1, 6)
    ClearScenarioFlags(0xE1, 7)
    ClearScenarioFlags(0xE2, 0)
    ClearScenarioFlags(0xE2, 1)
    ClearScenarioFlags(0xE2, 2)
    ClearScenarioFlags(0xE2, 3)
    ClearScenarioFlags(0xE2, 4)
    ClearScenarioFlags(0xE2, 5)
    ClearScenarioFlags(0xE2, 6)
    ClearScenarioFlags(0xE2, 7)
    ClearScenarioFlags(0xE3, 0)
    ClearScenarioFlags(0xE3, 1)
    ClearScenarioFlags(0xE3, 2)
    ClearScenarioFlags(0xE3, 3)
    ClearScenarioFlags(0xE3, 4)
    ClearScenarioFlags(0xE3, 5)
    ClearScenarioFlags(0xE3, 6)
    ClearScenarioFlags(0xE3, 7)
    ClearScenarioFlags(0xE4, 0)
    ClearScenarioFlags(0xE4, 1)
    ClearScenarioFlags(0xE4, 2)
    ClearScenarioFlags(0xE4, 3)
    ClearScenarioFlags(0xE4, 4)
    ClearScenarioFlags(0xE7, 5)
    ClearScenarioFlags(0xE4, 5)
    ClearScenarioFlags(0xE4, 6)
    ClearScenarioFlags(0xE4, 7)
    ClearScenarioFlags(0xE5, 0)
    ClearScenarioFlags(0xE5, 1)
    ClearScenarioFlags(0xE5, 2)
    ClearScenarioFlags(0xE5, 3)
    ClearScenarioFlags(0xE5, 4)
    ClearScenarioFlags(0xE5, 5)
    ClearScenarioFlags(0xE5, 6)
    ClearScenarioFlags(0xE5, 7)
    ClearScenarioFlags(0xE6, 0)
    ClearScenarioFlags(0xE6, 1)
    ClearScenarioFlags(0xE6, 2)
    ClearScenarioFlags(0xE6, 3)
    ClearScenarioFlags(0xE6, 4)
    ClearScenarioFlags(0xE6, 5)
    ClearScenarioFlags(0xE6, 6)
    ClearScenarioFlags(0xE6, 7)
    Return()

    # Function_18_EF2 end

    def Function_19_F9E(): pass

    label("Function_19_F9E")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1378")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Prologue\x01",                                # 0
            "②▼In Transcontinental Railroad Train\x01",      # 1
            "③▼Arrive at Crossbell Station\x01",             # 2
            "④▼Talk to Police Reception\x01",                # 3
            "⑤▼In Front of Geofront\x01",                    # 4
            "⑥▼Hear Child Crying\x01",                       # 5
            "⑦▼Find Another Child\x01",                      # 6
            "⑧▼Arios Appears After Battle\x01",              # 7
            "⑨▼Reporter Grace Appears\x01",                  # 8
            "⑩▼Vice Commissioner Reprimand\x01",             # 9
            "⑪▼Arrive at SSS\x01",                           # 10
            "⑫▼Visit Members' Rooms\x01",                    # 11
            "⑬▼Talk With Tio\x01",                           # 12
            "⑭▼Children Come to Visit\x01",                  # 13
            "Cancel\x01",                                      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_1196"),
        (12, "loc_1199"),
        (11, "loc_119F"),
        (10, "loc_11A2"),
        (9, "loc_11A2"),
        (8, "loc_11A2"),
        (7, "loc_11A2"),
        (6, "loc_11A5"),
        (5, "loc_11AB"),
        (4, "loc_11B7"),
        (3, "loc_11B7"),
        (2, "loc_11BA"),
        (1, "loc_11BA"),
        (0, "loc_11BD"),
        (SWITCH_DEFAULT, "loc_11D1"),
    )


    label("loc_1196")

    SetScenarioFlags(0x41, 4)

    label("loc_1199")

    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)

    label("loc_119F")

    SetScenarioFlags(0x41, 1)

    label("loc_11A2")

    SetScenarioFlags(0x41, 0)

    label("loc_11A5")

    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 7)

    label("loc_11AB")

    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)

    label("loc_11B7")

    SetScenarioFlags(0x40, 1)

    label("loc_11BA")

    SetScenarioFlags(0x40, 0)

    label("loc_11BD")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 46)
    Jump("loc_11D6")

    label("loc_11D1")

    Jump("loc_11D6")

    label("loc_11D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11FB")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)

    label("loc_11FB")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1259"),
        (1, "loc_126A"),
        (2, "loc_127B"),
        (3, "loc_128C"),
        (4, "loc_129A"),
        (5, "loc_12AB"),
        (6, "loc_12B9"),
        (7, "loc_12CB"),
        (8, "loc_12E4"),
        (9, "loc_12FD"),
        (10, "loc_130E"),
        (11, "loc_131F"),
        (12, "loc_1336"),
        (13, "loc_134D"),
        (SWITCH_DEFAULT, "loc_1364"),
    )


    label("loc_1259")

    SetScenarioFlags(0x5C, 1)
    NewScene("m3000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_126A")

    SetScenarioFlags(0x5C, 0)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_127B")

    SetScenarioFlags(0x5C, 0)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_128C")

    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_129A")

    SetScenarioFlags(0x5C, 1)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_12AB")

    NewScene("m0001", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_12B9")

    AddParty(0x96, 0xFF, 0xFF)
    NewScene("m0002", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_12CB")

    AddParty(0x96, 0xFF, 0xFF)
    AddParty(0x97, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("m0002", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_12E4")

    AddParty(0x96, 0xFF, 0xFF)
    AddParty(0x97, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_12FD")

    SetScenarioFlags(0x5C, 0)
    NewScene("c1160", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_130E")

    SetScenarioFlags(0x5C, 0)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_131F")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_1336")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_134D")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c010B", 105, 0, 0)
    IdleLoop()
    Jump("loc_1373")

    label("loc_1364")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1373")

    label("loc_1373")

    Jump("loc_FAD")

    label("loc_1378")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_19_F9E end

    def Function_20_1386(): pass

    label("Function_20_1386")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17A4")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Memory - Lloyd at Grave\x01",                # 0
            "②▼Hear SSS Explanation\x01",                   # 1
            "③▼Receive First Support Requests\x01",         # 2
            "④▼Arbitrating a Quarrel\x01",                  # 3
            "⑤▼Wazy and Wald Appear After Battle\x01",      # 4
            "⑥▼Dialogue With Wazy\x01",                     # 5
            "⑦▼Exchange Before Ignis\x01",                  # 6
            "⑧▼Dialogue With Wald\x01",                     # 7
            "⑨▼Dialogue With Wald After Battle\x01",        # 8
            "⑩▼Leave Ignis\x01",                            # 9
            "⑪▼Dialogue With Grace\x01",                    # 10
            "⑫▼Dialogue With Sergei\x01",                   # 11
            "⑬▼Dudley Passes By\x01",                       # 12
            "⑭▼Dialogue With Lawyer Ian\x01",               # 13
            "Cancel\x01",                                     # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_1598"),
        (12, "loc_159B"),
        (11, "loc_159E"),
        (10, "loc_15A1"),
        (9, "loc_15A4"),
        (8, "loc_15A7"),
        (7, "loc_15A7"),
        (6, "loc_15AA"),
        (5, "loc_15AD"),
        (4, "loc_15B0"),
        (3, "loc_15B0"),
        (2, "loc_15B3"),
        (1, "loc_15CB"),
        (0, "loc_15CB"),
        (SWITCH_DEFAULT, "loc_1606"),
    )


    label("loc_1598")

    SetScenarioFlags(0x42, 7)

    label("loc_159B")

    SetScenarioFlags(0x42, 6)

    label("loc_159E")

    SetScenarioFlags(0x42, 5)

    label("loc_15A1")

    SetScenarioFlags(0x42, 4)

    label("loc_15A4")

    SetScenarioFlags(0x42, 3)

    label("loc_15A7")

    SetScenarioFlags(0x42, 2)

    label("loc_15AA")

    SetScenarioFlags(0x42, 1)

    label("loc_15AD")

    SetScenarioFlags(0x42, 0)

    label("loc_15B0")

    SetScenarioFlags(0x41, 7)

    label("loc_15B3")

    SetScenarioFlags(0x41, 6)
    SetScenarioFlags(0x41, 5)
    SetScenarioFlags(0x4C, 1)
    OP_29(0x1, 0x4, 0x2)
    OP_29(0x1, 0x4, 0x10)
    OP_29(0x1, 0x4, 0x20)

    label("loc_15CB")

    SetScenarioFlags(0x41, 4)
    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)
    SetScenarioFlags(0x41, 1)
    SetScenarioFlags(0x41, 0)
    SetScenarioFlags(0x40, 7)
    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x40, 1)
    SetScenarioFlags(0x40, 0)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 47)
    Jump("loc_160B")

    label("loc_1606")

    Jump("loc_160B")

    label("loc_160B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1669"),
        (1, "loc_167A"),
        (2, "loc_168B"),
        (3, "loc_169C"),
        (4, "loc_16AA"),
        (5, "loc_16C4"),
        (6, "loc_16DC"),
        (7, "loc_16F4"),
        (8, "loc_170C"),
        (9, "loc_1727"),
        (10, "loc_173F"),
        (11, "loc_1757"),
        (12, "loc_176A"),
        (13, "loc_177D"),
        (SWITCH_DEFAULT, "loc_1790"),
    )


    label("loc_1669")

    SetScenarioFlags(0x5C, 0)
    NewScene("t4100", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_167A")

    SetScenarioFlags(0x5C, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_168B")

    SetScenarioFlags(0x5C, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_169C")

    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_16AA")

    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x205), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_16C4")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("c1410", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_16DC")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_16F4")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("c1420", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_170C")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    SetScenarioFlags(0x5C, 0)
    NewScene("c1420", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_1727")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_173F")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("c1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_1757")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_176A")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0200", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_177D")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0220", 0, 0, 0)
    IdleLoop()
    Jump("loc_179F")

    label("loc_1790")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_179F")

    label("loc_179F")

    Jump("loc_13A1")

    label("loc_17A4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_20_1386 end

    def Function_21_17B2(): pass

    label("Function_21_17B2")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A0")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Return to SSS\x01",                         # 0
            "②▼Truth About Wazy and Wald\x01",             # 1
            "③▼Trap for Mafia\x01",                        # 2
            "④▼Mafia Escape After Battle\x01",             # 3
            "⑤▼Report Support Mission Completed\x01",      # 4
            "Cancel\x01",                                    # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (4, "loc_189D"),
        (3, "loc_189D"),
        (2, "loc_189D"),
        (1, "loc_189D"),
        (0, "loc_18A3"),
        (SWITCH_DEFAULT, "loc_1905"),
    )


    label("loc_189D")

    SetScenarioFlags(0x43, 1)
    SetScenarioFlags(0x43, 2)

    label("loc_18A3")

    SetScenarioFlags(0x46, 1)
    SetScenarioFlags(0x43, 0)
    SetScenarioFlags(0x42, 7)
    SetScenarioFlags(0x42, 6)
    SetScenarioFlags(0x42, 5)
    SetScenarioFlags(0x42, 4)
    SetScenarioFlags(0x42, 3)
    SetScenarioFlags(0x42, 2)
    SetScenarioFlags(0x42, 1)
    SetScenarioFlags(0x42, 0)
    SetScenarioFlags(0x41, 7)
    SetScenarioFlags(0x41, 6)
    SetScenarioFlags(0x41, 5)
    SetScenarioFlags(0x41, 4)
    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)
    SetScenarioFlags(0x41, 1)
    SetScenarioFlags(0x41, 0)
    SetScenarioFlags(0x40, 7)
    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x40, 1)
    SetScenarioFlags(0x40, 0)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 48)
    Jump("loc_190A")

    label("loc_1905")

    Jump("loc_190A")

    label("loc_190A")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1932"),
        (1, "loc_1945"),
        (2, "loc_1956"),
        (3, "loc_1967"),
        (4, "loc_197B"),
        (SWITCH_DEFAULT, "loc_198C"),
    )


    label("loc_1932")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_199B")

    label("loc_1945")

    SetScenarioFlags(0x5C, 0)
    NewScene("c000B", 0, 0, 0)
    IdleLoop()
    Jump("loc_199B")

    label("loc_1956")

    SetScenarioFlags(0x5C, 0)
    NewScene("c140B", 0, 0, 0)
    IdleLoop()
    Jump("loc_199B")

    label("loc_1967")

    SetScenarioFlags(0x45, 5)
    SetScenarioFlags(0x5C, 1)
    NewScene("c140B", 0, 0, 0)
    IdleLoop()
    Jump("loc_199B")

    label("loc_197B")

    SetScenarioFlags(0x5C, 3)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_199B")

    label("loc_198C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_199B")

    label("loc_199B")

    Jump("loc_17CD")

    label("loc_19A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_21_17B2 end

    def Function_22_19AE(): pass

    label("Function_22_19AE")

    Call(2, 5)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D11")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Prologue\x01",                             # 0
            "②▼Morning in Crossbell\x01",                 # 1
            "③▼Police HQ\x01",                            # 2
            "④▼Look Over the Details\x01",                # 3
            "⑤▼Miss the Orbal Bus\x01",                   # 4
            "⑥▼Arrive at Fork\x01",                       # 5
            "⑦▼Arrive at Rest Area\x01",                  # 6
            "⑧▼Arrive at Armorica Village\x01",           # 7
            "⑨▼Visit the Village Chief's House\x01",      # 8
            "⑩▼Later at Armorica Village\x01",            # 9
            "⑪▼Harold to Escort\x01",                     # 10
            "⑫▼Return to Crossbell\x01",                  # 11
            "⑬▼Wait for Bus\x01",                         # 12
            "⑭▼Find Bus\x01",                             # 13
            "Cancel\x01",                                   # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_1B88"),
        (12, "loc_1B8B"),
        (11, "loc_1B8E"),
        (10, "loc_1B8E"),
        (9, "loc_1B91"),
        (8, "loc_1B9A"),
        (7, "loc_1B9D"),
        (6, "loc_1BA0"),
        (5, "loc_1BA3"),
        (4, "loc_1BA6"),
        (3, "loc_1BA9"),
        (2, "loc_1BA9"),
        (1, "loc_1BA9"),
        (0, "loc_1BA9"),
        (SWITCH_DEFAULT, "loc_1BBD"),
    )


    label("loc_1B88")

    SetScenarioFlags(0x61, 2)

    label("loc_1B8B")

    SetScenarioFlags(0x61, 1)

    label("loc_1B8E")

    SetScenarioFlags(0x61, 0)

    label("loc_1B91")

    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)

    label("loc_1B9A")

    SetScenarioFlags(0x60, 4)

    label("loc_1B9D")

    SetScenarioFlags(0x60, 3)

    label("loc_1BA0")

    SetScenarioFlags(0x60, 2)

    label("loc_1BA3")

    SetScenarioFlags(0x60, 1)

    label("loc_1BA6")

    SetScenarioFlags(0x60, 0)

    label("loc_1BA9")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 49)
    Jump("loc_1BC2")

    label("loc_1BBD")

    Jump("loc_1BC2")

    label("loc_1BC2")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C20"),
        (1, "loc_1C31"),
        (2, "loc_1C42"),
        (3, "loc_1C53"),
        (4, "loc_1C64"),
        (5, "loc_1C72"),
        (6, "loc_1C80"),
        (7, "loc_1C8E"),
        (8, "loc_1C9C"),
        (9, "loc_1CAA"),
        (10, "loc_1CB8"),
        (11, "loc_1CC6"),
        (12, "loc_1CDC"),
        (13, "loc_1CEF"),
        (SWITCH_DEFAULT, "loc_1D02"),
    )


    label("loc_1C20")

    SetScenarioFlags(0x5C, 0)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1C31")

    SetScenarioFlags(0x5C, 3)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1C42")

    SetScenarioFlags(0x5C, 1)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1C53")

    SetScenarioFlags(0x5C, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1C64")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1C72")

    NewScene("r0030", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1C80")

    NewScene("r0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1C8E")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1C9C")

    NewScene("t0010", 103, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1CAA")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1CB8")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1CC6")

    SetScenarioFlags(0x5C, 3)
    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1CDC")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r1500", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1CEF")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r1520", 0, 0, 0)
    IdleLoop()
    Jump("loc_1D0C")

    label("loc_1D02")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D0C")

    Jump("loc_19CC")

    label("loc_1D11")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_22_19AE end

    def Function_23_1D1F(): pass

    label("Function_23_1D1F")

    Call(2, 5)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210D")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Estelle Arrives After Battle\x01",       # 0
            "②▼Estelle Event\x01",                      # 1
            "③▼Arrive at Medical College\x01",          # 2
            "④▼Reunion With Cecile\x01",                # 3
            "⑤▼Dialogue With Residents\x01",            # 4
            "⑥▼Examine Location of Attack\x01",         # 5
            "⑦▼Hear Cecile's Whereabouts\x01",          # 6
            "⑧▼Meet Shizuku\x01",                       # 7
            "⑨▼Report to Cecile\x01",                   # 8
            "⑩▼Return on Orbal Bus\x01",                # 9
            "⑪▼Flashback\x01",                          # 10
            "⑫▼Hear Howling at North Exit\x01",         # 11
            "⑬▼Hear Howling on Mountain Path\x01",      # 12
            "⑭▼Arrive at Fork\x01",                     # 13
            "Cancel\x01",                                 # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_1F1F"),
        (12, "loc_1F22"),
        (11, "loc_1F25"),
        (10, "loc_1F28"),
        (9, "loc_1F2B"),
        (8, "loc_1F2E"),
        (7, "loc_1F2E"),
        (6, "loc_1F37"),
        (5, "loc_1F52"),
        (4, "loc_1F58"),
        (3, "loc_1F5B"),
        (2, "loc_1F61"),
        (1, "loc_1F67"),
        (0, "loc_1F6A"),
        (SWITCH_DEFAULT, "loc_1F9F"),
    )


    label("loc_1F1F")

    SetScenarioFlags(0x64, 3)

    label("loc_1F22")

    SetScenarioFlags(0x64, 2)

    label("loc_1F25")

    SetScenarioFlags(0x64, 1)

    label("loc_1F28")

    SetScenarioFlags(0x64, 0)

    label("loc_1F2B")

    SetScenarioFlags(0x63, 7)

    label("loc_1F2E")

    SetScenarioFlags(0x63, 4)
    SetScenarioFlags(0x63, 5)
    SetScenarioFlags(0x63, 6)

    label("loc_1F37")

    SetScenarioFlags(0x62, 3)
    SetScenarioFlags(0x62, 4)
    SetScenarioFlags(0x62, 5)
    SetScenarioFlags(0x62, 6)
    SetScenarioFlags(0x62, 7)
    SetScenarioFlags(0x63, 0)
    SetScenarioFlags(0x63, 1)
    SetScenarioFlags(0x63, 2)
    SetScenarioFlags(0x63, 3)

    label("loc_1F52")

    SetScenarioFlags(0x62, 1)
    SetScenarioFlags(0x62, 2)

    label("loc_1F58")

    SetScenarioFlags(0x62, 0)

    label("loc_1F5B")

    SetScenarioFlags(0x61, 6)
    SetScenarioFlags(0x61, 7)

    label("loc_1F61")

    SetScenarioFlags(0x61, 4)
    SetScenarioFlags(0x61, 5)

    label("loc_1F67")

    SetScenarioFlags(0x61, 3)

    label("loc_1F6A")

    SetScenarioFlags(0x60, 0)
    SetScenarioFlags(0x60, 1)
    SetScenarioFlags(0x60, 2)
    SetScenarioFlags(0x60, 3)
    SetScenarioFlags(0x60, 4)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)
    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x61, 0)
    SetScenarioFlags(0x61, 1)
    SetScenarioFlags(0x61, 2)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 50)
    Jump("loc_1FA4")

    label("loc_1F9F")

    Jump("loc_1FA4")

    label("loc_1FA4")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2002"),
        (1, "loc_2018"),
        (2, "loc_202B"),
        (3, "loc_203E"),
        (4, "loc_2051"),
        (5, "loc_2063"),
        (6, "loc_2075"),
        (7, "loc_2083"),
        (8, "loc_2091"),
        (9, "loc_20A6"),
        (10, "loc_20B4"),
        (11, "loc_20C5"),
        (12, "loc_20D8"),
        (13, "loc_20EB"),
        (SWITCH_DEFAULT, "loc_20FE"),
    )


    label("loc_2002")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7102")
    NewScene("r1520", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_2018")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r1520", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_202B")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("t1500", 100, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_203E")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_2051")

    AddParty(0x35, 0xFF, 0xFF)
    NewScene("t1540", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_2063")

    AddParty(0x35, 0xFF, 0xFF)
    NewScene("t1600", 103, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_2075")

    NewScene("t1540", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_2083")

    NewScene("t1550", 107, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_2091")

    SetScenarioFlags(0x5C, 0)
    AddParty(0x35, 0xFF, 0xFF)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_20A6")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_20B4")

    SetScenarioFlags(0x5C, 4)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_20C5")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_20D8")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_20EB")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_20FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2108")

    Jump("loc_1D3D")

    label("loc_210D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_23_1D1F end

    def Function_24_211B(): pass

    label("Function_24_211B")

    Call(2, 5)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2139")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24EF")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Encounter Renne\x01",                                   # 0
            "②▼Enter Tunnel Path\x01",                                 # 1
            "③▼Encounter Zeit\x01",                                    # 2
            "④▼Arrive at Mainz\x01",                                   # 3
            "⑤▼Mafia Henchmen Appear\x01",                             # 4
            "⑥▼Dialogue With Mayor\x01",                               # 5
            "⑦▼Begin Meeting\x01",                                     # 6
            "⑧▼Repel Wolves\x01",                                      # 7
            "⑨▼Find Mafia After Battle\x01",                           # 8
            "⑩▼Zeit Rescues After Battle\x01",                         # 9
            "⑪▼Apprehend Mafia\x01",                                   # 10
            "⑫▼Return to Crossbell\x01",                               # 11
            "⑬★Hospital at Night (Flashback - Personal Use)\x01",      # 12
            "Cancel\x01",                                                # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_22F0"),
        (11, "loc_22F0"),
        (10, "loc_22F0"),
        (9, "loc_22F0"),
        (8, "loc_22F0"),
        (7, "loc_22F0"),
        (6, "loc_22F3"),
        (5, "loc_22F6"),
        (4, "loc_22F9"),
        (3, "loc_22FF"),
        (2, "loc_2302"),
        (1, "loc_2308"),
        (0, "loc_230B"),
        (SWITCH_DEFAULT, "loc_238E"),
    )


    label("loc_22F0")

    SetScenarioFlags(0x65, 5)

    label("loc_22F3")

    SetScenarioFlags(0x65, 4)

    label("loc_22F6")

    SetScenarioFlags(0x65, 3)

    label("loc_22F9")

    SetScenarioFlags(0x65, 1)
    SetScenarioFlags(0x65, 2)

    label("loc_22FF")

    SetScenarioFlags(0x65, 0)

    label("loc_2302")

    SetScenarioFlags(0x64, 6)
    SetScenarioFlags(0x64, 7)

    label("loc_2308")

    SetScenarioFlags(0x64, 5)

    label("loc_230B")

    SetScenarioFlags(0x60, 0)
    SetScenarioFlags(0x60, 1)
    SetScenarioFlags(0x60, 2)
    SetScenarioFlags(0x60, 3)
    SetScenarioFlags(0x60, 4)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)
    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x61, 0)
    SetScenarioFlags(0x61, 1)
    SetScenarioFlags(0x61, 2)
    SetScenarioFlags(0x61, 3)
    SetScenarioFlags(0x61, 4)
    SetScenarioFlags(0x61, 5)
    SetScenarioFlags(0x61, 6)
    SetScenarioFlags(0x61, 7)
    SetScenarioFlags(0x62, 0)
    SetScenarioFlags(0x62, 1)
    SetScenarioFlags(0x62, 2)
    SetScenarioFlags(0x62, 3)
    SetScenarioFlags(0x62, 4)
    SetScenarioFlags(0x62, 5)
    SetScenarioFlags(0x62, 6)
    SetScenarioFlags(0x62, 7)
    SetScenarioFlags(0x63, 0)
    SetScenarioFlags(0x63, 1)
    SetScenarioFlags(0x63, 2)
    SetScenarioFlags(0x63, 3)
    SetScenarioFlags(0x63, 4)
    SetScenarioFlags(0x63, 5)
    SetScenarioFlags(0x63, 6)
    SetScenarioFlags(0x63, 7)
    SetScenarioFlags(0x64, 0)
    SetScenarioFlags(0x64, 1)
    SetScenarioFlags(0x64, 2)
    SetScenarioFlags(0x64, 3)
    SetScenarioFlags(0x64, 4)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 51)
    Jump("loc_2393")

    label("loc_238E")

    Jump("loc_2393")

    label("loc_2393")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23EB"),
        (1, "loc_23FE"),
        (2, "loc_2411"),
        (3, "loc_2424"),
        (4, "loc_2437"),
        (5, "loc_2445"),
        (6, "loc_245D"),
        (7, "loc_246B"),
        (8, "loc_2479"),
        (9, "loc_2493"),
        (10, "loc_24A4"),
        (11, "loc_24B5"),
        (12, "loc_24CF"),
        (SWITCH_DEFAULT, "loc_24E0"),
    )


    label("loc_23EB")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("t3000", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_23FE")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_2411")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_2424")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_2437")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_2445")

    ReplaceBGM("ed7121", "ed7302")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_245D")

    NewScene("t0520", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_246B")

    NewScene("t052B", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_2479")

    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r206B", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_2493")

    SetScenarioFlags(0x5C, 1)
    NewScene("r206B", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_24A4")

    SetScenarioFlags(0x5C, 1)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_24B5")

    SetScenarioFlags(0x5C, 4)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_24CF")

    SetScenarioFlags(0x5C, 5)
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Jump("loc_24EA")

    label("loc_24E0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24EA")

    Jump("loc_2139")

    label("loc_24EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_24_211B end

    def Function_25_24FD(): pass

    label("Function_25_24FD")

    Call(2, 5)
    Call(2, 6)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_251E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28B2")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Prologue 1\x01",                          # 0
            "②▼Prologue 2\x01",                          # 1
            "③▼Prologue 3\x01",                          # 2
            "④▼Review Support Requests\x01",             # 3
            "⑤▼Contact by Fran\x01",                     # 4
            "⑥▼Meet With Rixia\x01",                     # 5
            "⑦▼Before Arriving at Arc en Ciel\x01",      # 6
            "⑧▼See Ilya Training\x01",                   # 7
            "⑨▼Before Going to Revache & Co.\x01",       # 8
            "⑩▼Dialogue With Lawyer Ian\x01",            # 9
            "⑪▼Visit Heiyue Trading, Ltd.\x01",          # 10
            "⑫▼First Interview With Cao\x01",            # 11
            "⑬▼Meet With Mayor MacDowell\x01",           # 12
            "⑭▼Report to Ilya and Rixia\x01",            # 13
            "Cancel\x01",                                  # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_26FE"),
        (12, "loc_2701"),
        (11, "loc_2704"),
        (10, "loc_2707"),
        (9, "loc_270D"),
        (8, "loc_2710"),
        (7, "loc_2719"),
        (6, "loc_271F"),
        (5, "loc_2722"),
        (4, "loc_2725"),
        (3, "loc_2728"),
        (2, "loc_2728"),
        (1, "loc_2728"),
        (0, "loc_2728"),
        (SWITCH_DEFAULT, "loc_273C"),
    )


    label("loc_26FE")

    SetScenarioFlags(0x81, 4)

    label("loc_2701")

    SetScenarioFlags(0x81, 3)

    label("loc_2704")

    SetScenarioFlags(0x81, 2)

    label("loc_2707")

    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)

    label("loc_270D")

    SetScenarioFlags(0x80, 7)

    label("loc_2710")

    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x87, 3)

    label("loc_2719")

    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)

    label("loc_271F")

    SetScenarioFlags(0x80, 2)

    label("loc_2722")

    SetScenarioFlags(0x80, 1)

    label("loc_2725")

    SetScenarioFlags(0x80, 0)

    label("loc_2728")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 52)
    Jump("loc_2741")

    label("loc_273C")

    Jump("loc_2741")

    label("loc_2741")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_279F"),
        (1, "loc_27B9"),
        (2, "loc_27CA"),
        (3, "loc_27DB"),
        (4, "loc_27EC"),
        (5, "loc_27FD"),
        (6, "loc_280B"),
        (7, "loc_2819"),
        (8, "loc_2827"),
        (9, "loc_2835"),
        (10, "loc_284D"),
        (11, "loc_2865"),
        (12, "loc_287D"),
        (13, "loc_2895"),
        (SWITCH_DEFAULT, "loc_28A3"),
    )


    label("loc_279F")

    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c050B", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_27B9")

    SetScenarioFlags(0x5C, 0)
    NewScene("c0420", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_27CA")

    SetScenarioFlags(0x5C, 0)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_27DB")

    SetScenarioFlags(0x5C, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_27EC")

    SetScenarioFlags(0x5C, 6)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_27FD")

    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_280B")

    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_2819")

    NewScene("c0420", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_2827")

    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_2835")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0220", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_284D")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_2865")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c1210", 102, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_287D")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_2895")

    NewScene("c0420", 0, 0, 0)
    IdleLoop()
    Jump("loc_28AD")

    label("loc_28A3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28AD")

    Jump("loc_251E")

    label("loc_28B2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_25_24FD end

    def Function_26_28C0(): pass

    label("Function_26_28C0")

    Call(2, 5)
    Call(2, 6)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CA6")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Visit from Ernest\x01",                      # 0
            "②▼Conversation With Elie on Rooftop\x01",      # 1
            "③▼Request from Yin\x01",                       # 2
            "④▼In Front of IBC Building\x01",               # 3
            "⑤▼Inquire at Reception\x01",                   # 4
            "⑥▼Board Elevator\x01",                         # 5
            "⑦▼Dieter & Mariabell\x01",                     # 6
            "⑧▼To Terminal Room\x01",                       # 7
            "⑨▼Enter Terminal Room\x01",                    # 8
            "⑩▼Conversation With Mariabell\x01",            # 9
            "⑪▼Leave IBC Building\x01",                     # 10
            "⑫▼Borrow Key from City Hall\x01",              # 11
            "⑬▼Enter Geofront Sector B\x01",                # 12
            "⑭▼Find Jona's Hideout\x01",                    # 13
            "Cancel\x01",                                     # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_2AC8"),
        (12, "loc_2AD1"),
        (11, "loc_2AD4"),
        (10, "loc_2AD7"),
        (9, "loc_2ADA"),
        (8, "loc_2ADD"),
        (7, "loc_2AE0"),
        (6, "loc_2AE3"),
        (5, "loc_2AE9"),
        (4, "loc_2AEC"),
        (3, "loc_2AEF"),
        (2, "loc_2AF2"),
        (1, "loc_2AF2"),
        (0, "loc_2AF5"),
        (SWITCH_DEFAULT, "loc_2B36"),
    )


    label("loc_2AC8")

    SetScenarioFlags(0x86, 1)
    SetScenarioFlags(0x83, 3)
    SetScenarioFlags(0x83, 4)

    label("loc_2AD1")

    SetScenarioFlags(0x83, 2)

    label("loc_2AD4")

    SetScenarioFlags(0x83, 1)

    label("loc_2AD7")

    SetScenarioFlags(0x83, 0)

    label("loc_2ADA")

    SetScenarioFlags(0x82, 7)

    label("loc_2ADD")

    SetScenarioFlags(0x82, 6)

    label("loc_2AE0")

    SetScenarioFlags(0x82, 5)

    label("loc_2AE3")

    SetScenarioFlags(0x82, 3)
    SetScenarioFlags(0x82, 4)

    label("loc_2AE9")

    SetScenarioFlags(0x82, 2)

    label("loc_2AEC")

    SetScenarioFlags(0x82, 1)

    label("loc_2AEF")

    SetScenarioFlags(0x82, 0)

    label("loc_2AF2")

    SetScenarioFlags(0x81, 6)

    label("loc_2AF5")

    SetScenarioFlags(0x80, 0)
    SetScenarioFlags(0x80, 1)
    SetScenarioFlags(0x80, 2)
    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)
    SetScenarioFlags(0x87, 3)
    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x80, 7)
    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)
    SetScenarioFlags(0x81, 2)
    SetScenarioFlags(0x81, 3)
    SetScenarioFlags(0x81, 4)
    SetScenarioFlags(0x81, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 53)
    Jump("loc_2B3B")

    label("loc_2B36")

    Jump("loc_2B3B")

    label("loc_2B3B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B99"),
        (1, "loc_2BAC"),
        (2, "loc_2BCC"),
        (3, "loc_2BE6"),
        (4, "loc_2BF4"),
        (5, "loc_2C02"),
        (6, "loc_2C10"),
        (7, "loc_2C1E"),
        (8, "loc_2C30"),
        (9, "loc_2C42"),
        (10, "loc_2C50"),
        (11, "loc_2C63"),
        (12, "loc_2C76"),
        (13, "loc_2C89"),
        (SWITCH_DEFAULT, "loc_2C97"),
    )


    label("loc_2B99")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2BAC")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c010B", 110, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2BCC")

    SetScenarioFlags(0x5C, 7)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2BE6")

    NewScene("c1300", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2BF4")

    NewScene("c1310", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2C02")

    NewScene("c1310", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2C10")

    NewScene("c1340", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2C1E")

    AddParty(0x37, 0xFF, 0xFF)
    NewScene("c1330", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2C30")

    AddParty(0x37, 0xFF, 0xFF)
    NewScene("c1320", 100, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2C42")

    NewScene("c1320", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2C50")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c1300", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2C63")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2C76")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0300", 0, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2C89")

    NewScene("m0101", 133, 0, 0)
    IdleLoop()
    Jump("loc_2CA1")

    label("loc_2C97")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CA1")

    Jump("loc_28E1")

    label("loc_2CA6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_26_28C0 end

    def Function_27_2CB4(): pass

    label("Function_27_2CB4")

    Call(2, 5)
    Call(2, 6)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30D2")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼To Stargazer's Tower\x01",                          # 0
            "②▼Get to Offshoot\x01",                               # 1
            "③▼Enter Stargazer's Tower\x01",                       # 2
            "④▼After Battle With Golem\x01",                       # 3
            "⑤▼Battle With Yin on Tower's Highest Floor\x01",      # 4
            "⑥▼After Battle With Yin\x01",                         # 5
            "⑦▼Gather Invited Guests\x01",                         # 6
            "⑧▼Begin Play; Start Patrol\x01",                      # 7
            "⑨▼Begin Act 2\x01",                                   # 8
            "⑩▼Begin Act 3\x01",                                   # 9
            "⑪▼Begin Finale\x01",                                  # 10
            "⑫▼Find Grace\x01",                                    # 11
            "⑬▼Epilogue 1\x01",                                    # 12
            "⑭▼Epilogue 2\x01",                                    # 13
            "Cancel\x01",                                            # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_2E96"),
        (12, "loc_2E96"),
        (11, "loc_2E96"),
        (10, "loc_2E99"),
        (9, "loc_2EA5"),
        (8, "loc_2EB1"),
        (7, "loc_2EBD"),
        (6, "loc_2EBD"),
        (5, "loc_2EBD"),
        (4, "loc_2EBD"),
        (3, "loc_2EC0"),
        (2, "loc_2EC0"),
        (1, "loc_2EC9"),
        (0, "loc_2ECC"),
        (SWITCH_DEFAULT, "loc_2F40"),
    )


    label("loc_2E96")

    SetScenarioFlags(0x86, 0)

    label("loc_2E99")

    SetScenarioFlags(0x85, 4)
    SetScenarioFlags(0x85, 5)
    SetScenarioFlags(0x85, 6)
    SetScenarioFlags(0x85, 7)

    label("loc_2EA5")

    SetScenarioFlags(0x85, 0)
    SetScenarioFlags(0x85, 1)
    SetScenarioFlags(0x85, 2)
    SetScenarioFlags(0x85, 3)

    label("loc_2EB1")

    SetScenarioFlags(0x84, 4)
    SetScenarioFlags(0x84, 5)
    SetScenarioFlags(0x84, 6)
    SetScenarioFlags(0x84, 7)

    label("loc_2EBD")

    SetScenarioFlags(0x84, 3)

    label("loc_2EC0")

    SetScenarioFlags(0x84, 0)
    SetScenarioFlags(0x84, 1)
    SetScenarioFlags(0x84, 2)

    label("loc_2EC9")

    SetScenarioFlags(0x83, 7)

    label("loc_2ECC")

    SetScenarioFlags(0x80, 0)
    SetScenarioFlags(0x80, 1)
    SetScenarioFlags(0x80, 2)
    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)
    SetScenarioFlags(0x87, 3)
    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x80, 7)
    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)
    SetScenarioFlags(0x81, 2)
    SetScenarioFlags(0x81, 3)
    SetScenarioFlags(0x81, 4)
    SetScenarioFlags(0x81, 5)
    SetScenarioFlags(0x81, 6)
    SetScenarioFlags(0x81, 7)
    SetScenarioFlags(0x82, 0)
    SetScenarioFlags(0x82, 1)
    SetScenarioFlags(0x82, 2)
    SetScenarioFlags(0x82, 3)
    SetScenarioFlags(0x82, 4)
    SetScenarioFlags(0x82, 5)
    SetScenarioFlags(0x82, 6)
    SetScenarioFlags(0x82, 7)
    SetScenarioFlags(0x83, 0)
    SetScenarioFlags(0x83, 1)
    SetScenarioFlags(0x83, 2)
    SetScenarioFlags(0x83, 3)
    SetScenarioFlags(0x83, 4)
    SetScenarioFlags(0x83, 5)
    SetScenarioFlags(0x83, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 54)
    Jump("loc_2F45")

    label("loc_2F40")

    Jump("loc_2F45")

    label("loc_2F45")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FA3"),
        (1, "loc_2FB6"),
        (2, "loc_2FC4"),
        (3, "loc_2FD6"),
        (4, "loc_2FEB"),
        (5, "loc_2FFD"),
        (6, "loc_3017"),
        (7, "loc_3028"),
        (8, "loc_303F"),
        (9, "loc_3053"),
        (10, "loc_3067"),
        (11, "loc_307B"),
        (12, "loc_3098"),
        (13, "loc_30A9"),
        (SWITCH_DEFAULT, "loc_30C3"),
    )


    label("loc_2FA3")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0300", 0, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_2FB6")

    NewScene("r1520", 0, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_2FC4")

    AddParty(0x8, 0xFF, 0xFF)
    NewScene("m1020", 0, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_2FD6")

    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("m1020", 0, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_2FEB")

    AddParty(0x8, 0xFF, 0xFF)
    NewScene("m1099", 0, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_2FFD")

    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7102")
    NewScene("m1099", 0, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_3017")

    SetScenarioFlags(0x5C, 0)
    NewScene("c040B", 0, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_3028")

    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    SetScenarioFlags(0x5C, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_303F")

    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_3053")

    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_3067")

    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_307B")

    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x213), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0410", 105, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_3098")

    SetScenarioFlags(0x5D, 2)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_30A9")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Jump("loc_30CD")

    label("loc_30C3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30CD")

    Jump("loc_2CD5")

    label("loc_30D2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_27_2CB4 end

    def Function_28_30E0(): pass

    label("Function_28_30E0")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3104")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34F1")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼City Hall Assembly\x01",                 # 0
            "②▼Anniversary Festival\x01",               # 1
            "③▼In Front of Arc en Ciel\x01",            # 2
            "④▼Second Day Morning\x01",                 # 3
            "⑤▼Contact by Fran\x01",                    # 4
            "⑥▼Gang Brawl\x01",                         # 5
            "⑦▼Downtown District Chase 1\x01",          # 6
            "⑧▼Downtown District Chase 2\x01",          # 7
            "⑨▼Downtown District Chase 3\x01",          # 8
            "⑩▼Third Day Morning\x01",                  # 9
            "⑪▼Contact by Jona\x01",                    # 10
            "⑫▼Request Description from Jona\x01",      # 11
            "⑬▼Arrive at Geofront A\x01",               # 12
            "⑭▼Arrive at Geofront A - 2\x01",           # 13
            "Cancel\x01",                                 # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_32E6"),
        (12, "loc_32EC"),
        (11, "loc_32F2"),
        (10, "loc_32F5"),
        (9, "loc_32F8"),
        (8, "loc_32F8"),
        (7, "loc_32F8"),
        (6, "loc_32F8"),
        (5, "loc_32F8"),
        (4, "loc_32FB"),
        (3, "loc_32FE"),
        (2, "loc_32FE"),
        (1, "loc_32FE"),
        (0, "loc_32FE"),
        (SWITCH_DEFAULT, "loc_3312"),
    )


    label("loc_32E6")

    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)

    label("loc_32EC")

    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 4)

    label("loc_32F2")

    SetScenarioFlags(0xA0, 3)

    label("loc_32F5")

    SetScenarioFlags(0xA0, 2)

    label("loc_32F8")

    SetScenarioFlags(0xA0, 1)

    label("loc_32FB")

    SetScenarioFlags(0xA0, 0)

    label("loc_32FE")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 55)
    Jump("loc_3317")

    label("loc_3312")

    Jump("loc_3317")

    label("loc_3317")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3375"),
        (1, "loc_3386"),
        (2, "loc_33A5"),
        (3, "loc_33BB"),
        (4, "loc_33D6"),
        (5, "loc_33F1"),
        (6, "loc_3409"),
        (7, "loc_342D"),
        (8, "loc_3451"),
        (9, "loc_346C"),
        (10, "loc_3487"),
        (11, "loc_34A2"),
        (12, "loc_34BA"),
        (13, "loc_34CE"),
        (SWITCH_DEFAULT, "loc_34E2"),
    )


    label("loc_3375")

    SetScenarioFlags(0x5C, 1)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_3386")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7106")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_33A5")

    SetScenarioFlags(0x5C, 1)
    ReplaceBGM("ed7100", "ed7106")
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_33BB")

    SetScenarioFlags(0x5C, 6)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_33D6")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c000C", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_33F1")

    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_3409")

    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c140C", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_342D")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c140C", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_3451")

    SetScenarioFlags(0x5C, 2)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c140C", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_346C")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_3487")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_34A2")

    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("m0101", 135, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_34BA")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("m0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_34CE")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("m0010", 103, 0, 0)
    IdleLoop()
    Jump("loc_34EC")

    label("loc_34E2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_34EC")

    Jump("loc_3104")

    label("loc_34F1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_28_30E0 end

    def Function_29_34FF(): pass

    label("Function_29_34FF")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3523")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3971")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Encounter Mid Boss\x01",               # 0
            "②▼After Battle With Mid Boss\x01",       # 1
            "③▼Third Control Terminal Room\x01",      # 2
            "④▼Leave Geofront A\x01",                 # 3
            "⑤▼Review Mafia Intel\x01",               # 4
            "⑥▼Fourth Day Morning (Elie)\x01",        # 5
            "⑦▼Fourth Day Morning (Tio)\x01",         # 6
            "⑧▼Fourth Day Morning (Randy)\x01",       # 7
            "⑨▼Contact by Fran - 2\x01",              # 8
            "⑩▼Dialogue With Hayworths\x01",          # 9
            "⑪▼Check Arc en Ciel\x01",                # 10
            "⑫▼Contact by Randy\x01",                 # 11
            "⑬▼Renne Appears\x01",                    # 12
            "⑭▼Contact by Elie\x01",                  # 13
            "Cancel\x01",                               # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_3704"),
        (12, "loc_370A"),
        (11, "loc_3710"),
        (10, "loc_3713"),
        (9, "loc_3716"),
        (8, "loc_371C"),
        (7, "loc_371F"),
        (6, "loc_371F"),
        (5, "loc_371F"),
        (4, "loc_371F"),
        (3, "loc_371F"),
        (2, "loc_3722"),
        (1, "loc_3725"),
        (0, "loc_3725"),
        (SWITCH_DEFAULT, "loc_3757"),
    )


    label("loc_3704")

    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xB9, 4)

    label("loc_370A")

    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xB9, 3)

    label("loc_3710")

    SetScenarioFlags(0xA1, 7)

    label("loc_3713")

    SetScenarioFlags(0xA1, 6)

    label("loc_3716")

    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xAA, 2)

    label("loc_371C")

    SetScenarioFlags(0xA1, 4)

    label("loc_371F")

    SetScenarioFlags(0xA1, 3)

    label("loc_3722")

    SetScenarioFlags(0xA1, 2)

    label("loc_3725")

    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 56)
    Jump("loc_375C")

    label("loc_3757")

    Jump("loc_375C")

    label("loc_375C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_377B")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)

    label("loc_377B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_379D")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)

    label("loc_379D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_37FB"),
        (1, "loc_3809"),
        (2, "loc_381A"),
        (3, "loc_3828"),
        (4, "loc_3840"),
        (5, "loc_3851"),
        (6, "loc_387D"),
        (7, "loc_38A9"),
        (8, "loc_38D5"),
        (9, "loc_38E6"),
        (10, "loc_38FE"),
        (11, "loc_3916"),
        (12, "loc_392E"),
        (13, "loc_3946"),
        (SWITCH_DEFAULT, "loc_3962"),
    )


    label("loc_37FB")

    NewScene("m0013", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_3809")

    SetScenarioFlags(0x5C, 0)
    NewScene("m0013", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_381A")

    NewScene("m0013", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_3828")

    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c000C", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_3840")

    SetScenarioFlags(0x5C, 5)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_3851")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_387D")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_38A9")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_38D5")

    SetScenarioFlags(0x5C, 1)
    NewScene("c100C", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_38E6")

    ReplaceBGM("ed7100", "ed7104")
    ReplaceBGM("ed7101", "ed7104")
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_38FE")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c041C", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_3916")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c050C", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_392E")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c050C", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_3946")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_396C")

    label("loc_3962")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_396C")

    Jump("loc_3523")

    label("loc_3971")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_29_34FF end

    def Function_30_397F(): pass

    label("Function_30_397F")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DE5")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Entered Department Store\x01",             # 0
            "②▼Contact by Tio\x01",                       # 1
            "③▼Check Door\x01",                           # 2
            "④▼Contact by R & T\x01",                     # 3
            "⑤▼Contact by E & T\x01",                     # 4
            "⑥▼Renne Operates Terminal\x01",              # 5
            "⑦▼Leave from West Exit on Highway\x01",      # 6
            "⑧▼Find Truck\x01",                           # 7
            "⑨▼Hear Delightful Child\x01",                # 8
            "⑩▼Find Colin\x01",                           # 9
            "⑪▼Find Colin, After Battle\x01",             # 10
            "⑫▼Lloyd's Room\x01",                         # 11
            "⑬▼Lloyd's Room - 2\x01",                     # 12
            "⑭▼Final Day Morning\x01",                    # 13
            "Cancel\x01",                                   # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_3B5D"),
        (12, "loc_3B5D"),
        (11, "loc_3B5D"),
        (10, "loc_3B5D"),
        (9, "loc_3B5D"),
        (8, "loc_3B60"),
        (7, "loc_3B63"),
        (6, "loc_3B66"),
        (5, "loc_3B69"),
        (4, "loc_3B69"),
        (3, "loc_3B6F"),
        (2, "loc_3B75"),
        (1, "loc_3B78"),
        (0, "loc_3B7E"),
        (SWITCH_DEFAULT, "loc_3BD4"),
    )


    label("loc_3B5D")

    SetScenarioFlags(0xA3, 2)

    label("loc_3B60")

    SetScenarioFlags(0xA3, 1)

    label("loc_3B63")

    SetScenarioFlags(0xA3, 0)

    label("loc_3B66")

    SetScenarioFlags(0xA2, 7)

    label("loc_3B69")

    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xB9, 7)

    label("loc_3B6F")

    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xB9, 6)

    label("loc_3B75")

    SetScenarioFlags(0xA2, 4)

    label("loc_3B78")

    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xB9, 5)

    label("loc_3B7E")

    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xAA, 2)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xB9, 3)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xB9, 4)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 57)
    Jump("loc_3BD9")

    label("loc_3BD4")

    Jump("loc_3BD9")

    label("loc_3BD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BFB")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)

    label("loc_3BFB")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3C59"),
        (1, "loc_3C75"),
        (2, "loc_3C91"),
        (3, "loc_3CAD"),
        (4, "loc_3CC9"),
        (5, "loc_3CE5"),
        (6, "loc_3D04"),
        (7, "loc_3D20"),
        (8, "loc_3D3C"),
        (9, "loc_3D58"),
        (10, "loc_3D6A"),
        (11, "loc_3D7F"),
        (12, "loc_3D9D"),
        (13, "loc_3DBB"),
        (SWITCH_DEFAULT, "loc_3DD6"),
    )


    label("loc_3C59")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c017C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3C75")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c000C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3C91")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c000C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3CAD")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3CC9")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c020C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3CE5")

    AddParty(0x5F, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 3)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3D04")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3D20")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("r1020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3D3C")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("r1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3D58")

    AddParty(0x5F, 0xFF, 0xFF)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3D6A")

    AddParty(0x5F, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3D7F")

    AddParty(0x5F, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3D9D")

    AddParty(0x5F, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 5)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x202), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3DBB")

    SetScenarioFlags(0x5C, 1)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DE0")

    label("loc_3DD6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DE0")

    Jump("loc_39A3")

    label("loc_3DE5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_30_397F end

    def Function_31_3DF3(): pass

    label("Function_31_3DF3")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "☆Partner: Elie\x01",       # 0
            "☆Partner: Tio\x01",        # 1
            "☆Partner: Randy\x01",      # 2
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3E54"),
        (1, "loc_3E66"),
        (2, "loc_3E78"),
        (SWITCH_DEFAULT, "loc_3E8A"),
    )


    label("loc_3E54")

    SetScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 2)
    ClearScenarioFlags(0xA9, 3)
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_3E8A")

    label("loc_3E66")

    ClearScenarioFlags(0xA9, 1)
    SetScenarioFlags(0xA9, 2)
    ClearScenarioFlags(0xA9, 3)
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_3E8A")

    label("loc_3E78")

    ClearScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 2)
    SetScenarioFlags(0xA9, 3)
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_3E8A")

    label("loc_3E8A")

    Return()

    # Function_31_3DF3 end

    def Function_32_3E8B(): pass

    label("Function_32_3E8B")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42ED")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Board Cruise Ship\x01",            # 0
            "②▼Dialogue in Cruise Ship\x01",      # 1
            "③▼Arrive at Mishelam\x01",           # 2
            "④▼Check Speaker's Mansion\x01",      # 3
            "⑤▼Check Theme Park\x01",             # 4
            "⑥▼Sort Information\x01",             # 5
            "⑦▼Wazy's Room\x01",                  # 6
            "⑧▼Enter Boutique\x01",               # 7
            "⑨▼To Auction\x01",                   # 8
            "⑩▼Arrive at Auction\x01",            # 9
            "⑪▼Check Venue\x01",                  # 10
            "⑫▼Mariabell Appears\x01",            # 11
            "⑬▼Auction Start\x01",                # 12
            "⑭▼Encounter Yin\x01",                # 13
            "Cancel\x01",                           # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_4050"),
        (12, "loc_4053"),
        (11, "loc_4056"),
        (10, "loc_406E"),
        (9, "loc_4071"),
        (8, "loc_4074"),
        (7, "loc_4074"),
        (6, "loc_4077"),
        (5, "loc_407D"),
        (4, "loc_4086"),
        (3, "loc_4086"),
        (2, "loc_4089"),
        (1, "loc_408F"),
        (0, "loc_4095"),
        (SWITCH_DEFAULT, "loc_410F"),
    )


    label("loc_4050")

    SetScenarioFlags(0xA6, 2)

    label("loc_4053")

    SetScenarioFlags(0xA6, 1)

    label("loc_4056")

    SetScenarioFlags(0xA5, 1)
    SetScenarioFlags(0xA5, 2)
    SetScenarioFlags(0xA5, 3)
    SetScenarioFlags(0xA5, 4)
    SetScenarioFlags(0xA5, 5)
    SetScenarioFlags(0xA5, 6)
    SetScenarioFlags(0xA5, 7)
    SetScenarioFlags(0xA6, 0)

    label("loc_406E")

    SetScenarioFlags(0xA5, 0)

    label("loc_4071")

    SetScenarioFlags(0xA4, 7)

    label("loc_4074")

    SetScenarioFlags(0xA4, 6)

    label("loc_4077")

    SetScenarioFlags(0xA4, 4)
    SetScenarioFlags(0xA4, 5)

    label("loc_407D")

    SetScenarioFlags(0xA4, 1)
    SetScenarioFlags(0xA4, 2)
    SetScenarioFlags(0xA4, 3)

    label("loc_4086")

    SetScenarioFlags(0xA4, 0)

    label("loc_4089")

    SetScenarioFlags(0xA3, 6)
    SetScenarioFlags(0xA3, 7)

    label("loc_408F")

    SetScenarioFlags(0xA3, 4)
    SetScenarioFlags(0xA3, 5)

    label("loc_4095")

    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xAA, 2)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xB9, 3)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xB9, 4)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xB9, 5)
    SetScenarioFlags(0xA2, 4)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xB9, 6)
    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xB9, 7)
    SetScenarioFlags(0xA2, 7)
    SetScenarioFlags(0xA3, 0)
    SetScenarioFlags(0xA3, 1)
    SetScenarioFlags(0xA3, 2)
    SetScenarioFlags(0xA3, 3)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 58)
    Jump("loc_4114")

    label("loc_410F")

    Jump("loc_4114")

    label("loc_4114")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4172"),
        (1, "loc_418A"),
        (2, "loc_4198"),
        (3, "loc_41A9"),
        (4, "loc_41B7"),
        (5, "loc_41C5"),
        (6, "loc_41D3"),
        (7, "loc_41E1"),
        (8, "loc_41F3"),
        (9, "loc_4244"),
        (10, "loc_4292"),
        (11, "loc_42A3"),
        (12, "loc_42B4"),
        (13, "loc_42C9"),
        (SWITCH_DEFAULT, "loc_42DE"),
    )


    label("loc_4172")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_418A")

    NewScene("e0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_4198")

    SetScenarioFlags(0x5C, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_41A9")

    NewScene("t1100", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_41B7")

    NewScene("t1030", 100, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_41C5")

    NewScene("t1020", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_41D3")

    NewScene("t1050", 107, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_41E1")

    AddParty(0x50, 0xFF, 0xFF)
    NewScene("t1040", 100, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_41F3")

    Call(2, 31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_420C")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_4233")

    label("loc_420C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4222")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_4233")

    label("loc_4222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4233")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_4233")

    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_4244")

    Call(2, 31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_425D")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_4284")

    label("loc_425D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4273")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_4284")

    label("loc_4273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4284")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_4284")

    NewScene("t110B", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_4292")

    Call(2, 31)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_42A3")

    Call(2, 31)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_42B4")

    Call(2, 31)
    AddParty(0x37, 0xFF, 0xFF)
    NewScene("t112B", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_42C9")

    Call(2, 31)
    AddParty(0x50, 0xFF, 0xFF)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Jump("loc_42E8")

    label("loc_42DE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_42E8")

    Jump("loc_3EAF")

    label("loc_42ED")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_32_3E8B end

    def Function_33_42FB(): pass

    label("Function_33_42FB")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_431F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4755")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Enter Treasure Room\x01",             # 0
            "②▼Begin Escape\x01",                    # 1
            "③▼Entrance Hall Blockade R\x01",        # 2
            "④▼Entrance Hall Blockade L\x01",        # 3
            "⑤▼Enter Speaker's Bedroom\x01",         # 4
            "⑥▼Entrance Hall Breakthrough\x01",      # 5
            "⑦▼Breakthrough, After Battle\x01",      # 6
            "⑧▼Fight at Residences Block\x01",       # 7
            "⑨▼Fight at Mishelam Center\x01",        # 8
            "⑩▼Fight With Garcia\x01",               # 9
            "⑪▼After Fight With Garcia\x01",         # 10
            "Cancel\x01",                              # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (10, "loc_44B7"),
        (9, "loc_44B7"),
        (8, "loc_44BA"),
        (7, "loc_44BD"),
        (6, "loc_44C3"),
        (5, "loc_44C3"),
        (4, "loc_44C6"),
        (3, "loc_44C9"),
        (2, "loc_44CF"),
        (1, "loc_44D2"),
        (0, "loc_44D8"),
        (SWITCH_DEFAULT, "loc_458B"),
    )


    label("loc_44B7")

    SetScenarioFlags(0xA7, 5)

    label("loc_44BA")

    SetScenarioFlags(0xA7, 4)

    label("loc_44BD")

    SetScenarioFlags(0xA7, 3)
    SetScenarioFlags(0x5A, 3)

    label("loc_44C3")

    SetScenarioFlags(0xA7, 2)

    label("loc_44C6")

    SetScenarioFlags(0xA7, 1)

    label("loc_44C9")

    SetScenarioFlags(0xA6, 7)
    SetScenarioFlags(0xA7, 0)

    label("loc_44CF")

    SetScenarioFlags(0xA6, 6)

    label("loc_44D2")

    SetScenarioFlags(0xA6, 4)
    SetScenarioFlags(0xA6, 5)

    label("loc_44D8")

    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xAA, 2)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xA2, 4)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xA2, 7)
    SetScenarioFlags(0xA3, 0)
    SetScenarioFlags(0xA3, 1)
    SetScenarioFlags(0xA3, 2)
    SetScenarioFlags(0xA3, 3)
    SetScenarioFlags(0xA3, 4)
    SetScenarioFlags(0xA3, 5)
    SetScenarioFlags(0xA3, 6)
    SetScenarioFlags(0xA3, 7)
    SetScenarioFlags(0xA4, 0)
    SetScenarioFlags(0xA4, 1)
    SetScenarioFlags(0xA4, 2)
    SetScenarioFlags(0xA4, 3)
    SetScenarioFlags(0xA4, 4)
    SetScenarioFlags(0xA4, 5)
    SetScenarioFlags(0xA4, 6)
    SetScenarioFlags(0xA4, 7)
    SetScenarioFlags(0xA5, 0)
    SetScenarioFlags(0xA5, 1)
    SetScenarioFlags(0xA5, 2)
    SetScenarioFlags(0xA5, 3)
    SetScenarioFlags(0xA5, 4)
    SetScenarioFlags(0xA5, 5)
    SetScenarioFlags(0xA5, 6)
    SetScenarioFlags(0xA5, 7)
    SetScenarioFlags(0xA6, 0)
    SetScenarioFlags(0xA6, 1)
    SetScenarioFlags(0xA6, 2)
    SetScenarioFlags(0xA6, 3)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 59)
    Jump("loc_4590")

    label("loc_458B")

    Jump("loc_4590")

    label("loc_4590")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45AC")
    Call(2, 31)

    label("loc_45AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45CD")
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x32, 0xFF, 0xFF)

    label("loc_45CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45EE")
    SetChrChipPat(0x0, 0x1, 0x9A)
    LoadChrChipPat()

    label("loc_45EE")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_463A"),
        (1, "loc_4655"),
        (2, "loc_466D"),
        (3, "loc_4685"),
        (4, "loc_469D"),
        (5, "loc_46B5"),
        (6, "loc_46CD"),
        (7, "loc_46E8"),
        (8, "loc_4700"),
        (9, "loc_4718"),
        (10, "loc_4730"),
        (SWITCH_DEFAULT, "loc_4746"),
    )


    label("loc_463A")

    AddParty(0x50, 0xFF, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t116B", 0, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_4655")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t116B", 0, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_466D")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t119B", 102, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_4685")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t119B", 103, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_469D")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t121B", 106, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_46B5")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_46CD")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    SetScenarioFlags(0x5C, 4)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_46E8")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t101B", 0, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_4700")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t102B", 0, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_4718")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t100B", 0, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_4730")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7513", "ed7509")
    NewScene("t100B", 0, 0, 0)
    IdleLoop()
    Jump("loc_4750")

    label("loc_4746")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4750")

    Jump("loc_431F")

    label("loc_4755")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_33_42FB end

    def Function_34_4763(): pass

    label("Function_34_4763")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "☆Partner: Elie\x01",       # 0
            "☆Partner: Tio\x01",        # 1
            "☆Partner: Randy\x01",      # 2
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_47C4"),
        (1, "loc_47D6"),
        (2, "loc_47E8"),
        (SWITCH_DEFAULT, "loc_47FA"),
    )


    label("loc_47C4")

    SetScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 5)
    ClearScenarioFlags(0xA9, 6)
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_47FA")

    label("loc_47D6")

    ClearScenarioFlags(0xA9, 4)
    SetScenarioFlags(0xA9, 5)
    ClearScenarioFlags(0xA9, 6)
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_47FA")

    label("loc_47E8")

    ClearScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 5)
    SetScenarioFlags(0xA9, 6)
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_47FA")

    label("loc_47FA")

    Return()

    # Function_34_4763 end

    def Function_35_47FB(): pass

    label("Function_35_47FB")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4822")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B99")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Sort Situation\x01",              # 0
            "②▼Leave Central Square\x01",        # 1
            "③▼Visit Bracer Guild\x01",          # 2
            "④▼Arrive at Cathedral\x01",         # 3
            "⑤▼Consult Sister\x01",              # 4
            "⑥▼Leave Cathedral\x01",             # 5
            "⑦▼Board Bus\x01",                   # 6
            "⑧▼Arrive at Hospital\x01",          # 7
            "⑨▼Reunite With Cecile\x01",         # 8
            "⑩▼Joachim's Lab\x01",               # 9
            "⑪▼KeA and Shizuku Meet\x01",        # 10
            "⑫▼Rejoin KeA and Shizuku\x01",      # 11
            "⑬▼Scene at Revache\x01",            # 12
            "Cancel\x01",                          # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_49B6"),
        (11, "loc_49B6"),
        (10, "loc_49B9"),
        (9, "loc_49BF"),
        (8, "loc_49C2"),
        (7, "loc_49C5"),
        (6, "loc_49C5"),
        (5, "loc_49C8"),
        (4, "loc_49CB"),
        (3, "loc_49CE"),
        (2, "loc_49D1"),
        (1, "loc_49D4"),
        (0, "loc_49D7"),
        (SWITCH_DEFAULT, "loc_49EB"),
    )


    label("loc_49B6")

    SetScenarioFlags(0xA9, 0)

    label("loc_49B9")

    SetScenarioFlags(0xA8, 6)
    SetScenarioFlags(0xA8, 7)

    label("loc_49BF")

    SetScenarioFlags(0xA8, 5)

    label("loc_49C2")

    SetScenarioFlags(0xA8, 4)

    label("loc_49C5")

    SetScenarioFlags(0xA8, 3)

    label("loc_49C8")

    SetScenarioFlags(0xA8, 2)

    label("loc_49CB")

    SetScenarioFlags(0xA8, 1)

    label("loc_49CE")

    SetScenarioFlags(0xA8, 0)

    label("loc_49D1")

    SetScenarioFlags(0xA7, 7)

    label("loc_49D4")

    SetScenarioFlags(0xA7, 6)

    label("loc_49D7")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 59)
    Jump("loc_49F0")

    label("loc_49EB")

    Jump("loc_49F0")

    label("loc_49F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A0D")
    AddParty(0x52, 0xFF, 0xFF)

    label("loc_4A0D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4A65"),
        (1, "loc_4A76"),
        (2, "loc_4A91"),
        (3, "loc_4AAC"),
        (4, "loc_4AC7"),
        (5, "loc_4AE2"),
        (6, "loc_4AFD"),
        (7, "loc_4B18"),
        (8, "loc_4B2C"),
        (9, "loc_4B3D"),
        (10, "loc_4B4E"),
        (11, "loc_4B5F"),
        (12, "loc_4B70"),
        (SWITCH_DEFAULT, "loc_4B8A"),
    )


    label("loc_4A65")

    SetScenarioFlags(0x5D, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4A76")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4A91")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4AAC")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("t4000", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4AC7")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("t4010", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4AE2")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("t4000", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4AFD")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("r1500", 100, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4B18")

    Call(2, 34)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4B2C")

    Call(2, 34)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4B3D")

    Call(2, 34)
    NewScene("t1650", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4B4E")

    Call(2, 34)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4B5F")

    Call(2, 34)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4B70")

    SetScenarioFlags(0x5C, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B94")

    label("loc_4B8A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B94")

    Jump("loc_4822")

    label("loc_4B99")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_35_47FB end

    def Function_36_4BA7(): pass

    label("Function_36_4BA7")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F41")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼KeA Helps With Cooking\x01",              # 0
            "②▼Car Parked at North Exit\x01",            # 1
            "③▼Fork in Tunnel\x01",                      # 2
            "④▼Arrive in Front of Moon Temple\x01",      # 3
            "⑤▼Arrive at Chapel\x01",                    # 4
            "⑥▼After Battle in Chapel\x01",              # 5
            "⑦▼Arrive During Ritual\x01",                # 6
            "⑧▼After Battle in Ritual Area\x01",         # 7
            "⑨▼Stop Bell Resonance\x01",                 # 8
            "⑩▼Return to Chapel\x01",                    # 9
            "⑪▼Contact by Fran\x01",                     # 10
            "⑫▼Arrive at Mainz\x01",                     # 11
            "⑬▼Visit Mayor's Residence\x01",             # 12
            "Cancel\x01",                                  # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_4D93"),
        (11, "loc_4D96"),
        (10, "loc_4D99"),
        (9, "loc_4D9C"),
        (8, "loc_4D9F"),
        (7, "loc_4DA2"),
        (6, "loc_4DA2"),
        (5, "loc_4DA5"),
        (4, "loc_4DA5"),
        (3, "loc_4DA8"),
        (2, "loc_4DAB"),
        (1, "loc_4DAE"),
        (0, "loc_4DBA"),
        (SWITCH_DEFAULT, "loc_4DCE"),
    )


    label("loc_4D93")

    SetScenarioFlags(0xC1, 1)

    label("loc_4D96")

    SetScenarioFlags(0xC1, 0)

    label("loc_4D99")

    SetScenarioFlags(0xC0, 7)

    label("loc_4D9C")

    SetScenarioFlags(0xC0, 6)

    label("loc_4D9F")

    SetScenarioFlags(0xC0, 5)

    label("loc_4DA2")

    SetScenarioFlags(0xC0, 4)

    label("loc_4DA5")

    SetScenarioFlags(0xC0, 3)

    label("loc_4DA8")

    SetScenarioFlags(0xC0, 2)

    label("loc_4DAB")

    SetScenarioFlags(0xC0, 1)

    label("loc_4DAE")

    SetScenarioFlags(0xC0, 0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DBA")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 60)
    Jump("loc_4DD3")

    label("loc_4DCE")

    Jump("loc_4DD3")

    label("loc_4DD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DF0")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_4DF0")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4E48"),
        (1, "loc_4E59"),
        (2, "loc_4E6C"),
        (3, "loc_4E7F"),
        (4, "loc_4E92"),
        (5, "loc_4EA5"),
        (6, "loc_4EBB"),
        (7, "loc_4ECE"),
        (8, "loc_4EE4"),
        (9, "loc_4EF7"),
        (10, "loc_4F05"),
        (11, "loc_4F13"),
        (12, "loc_4F24"),
        (SWITCH_DEFAULT, "loc_4F32"),
    )


    label("loc_4E48")

    SetScenarioFlags(0x5D, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4E59")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4E6C")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4E7F")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r2070", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4E92")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("m2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4EA5")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7102")
    NewScene("m2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4EBB")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("m2099", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4ECE")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7102")
    NewScene("m2099", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4EE4")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("m2060", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4EF7")

    NewScene("m2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4F05")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4F13")

    SetScenarioFlags(0x5C, 2)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4F24")

    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F3C")

    label("loc_4F32")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F3C")

    Jump("loc_4BD1")

    label("loc_4F41")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_36_4BA7 end

    def Function_37_4F4F(): pass

    label("Function_37_4F4F")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5302")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Return to Square\x01",              # 0
            "②▼Visit Casino\x01",                  # 1
            "③▼Dialogue With Drake\x01",           # 2
            "④▼Investigate Gantz's Luck\x01",      # 3
            "⑤▼Return to SSS\x01",                 # 4
            "⑥▼Dialogue With Lawyer Ian\x01",      # 5
            "⑦▼Raid on Heiyue\x01",                # 6
            "⑧▼Contact by Jona\x01",               # 7
            "⑨▼Question Heiyue\x01",               # 8
            "⑩▼Dialogue With Cao\x01",             # 9
            "⑪▼Dialogue With Garcia\x01",          # 10
            "⑫▼Exchange With Grace\x01",           # 11
            "⑬▼Match at Casino\x01",               # 12
            "Cancel\x01",                            # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_5113"),
        (11, "loc_5116"),
        (10, "loc_5119"),
        (9, "loc_511C"),
        (8, "loc_511F"),
        (7, "loc_5122"),
        (6, "loc_5122"),
        (5, "loc_5122"),
        (4, "loc_5125"),
        (3, "loc_5128"),
        (2, "loc_512E"),
        (1, "loc_5131"),
        (0, "loc_513D"),
        (SWITCH_DEFAULT, "loc_517E"),
    )


    label("loc_5113")

    SetScenarioFlags(0xC2, 6)

    label("loc_5116")

    SetScenarioFlags(0xC2, 5)

    label("loc_5119")

    SetScenarioFlags(0xC2, 4)

    label("loc_511C")

    SetScenarioFlags(0xC2, 3)

    label("loc_511F")

    SetScenarioFlags(0xC2, 2)

    label("loc_5122")

    SetScenarioFlags(0xC2, 1)

    label("loc_5125")

    SetScenarioFlags(0xC2, 0)

    label("loc_5128")

    SetScenarioFlags(0xC1, 6)
    SetScenarioFlags(0xC1, 7)

    label("loc_512E")

    SetScenarioFlags(0xC1, 5)

    label("loc_5131")

    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_513D")

    SetScenarioFlags(0xC0, 0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 61)
    Jump("loc_5183")

    label("loc_517E")

    Jump("loc_5183")

    label("loc_5183")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_51DB"),
        (1, "loc_51F9"),
        (2, "loc_5207"),
        (3, "loc_5215"),
        (4, "loc_5223"),
        (5, "loc_5231"),
        (6, "loc_5242"),
        (7, "loc_525C"),
        (8, "loc_5277"),
        (9, "loc_528F"),
        (10, "loc_52A7"),
        (11, "loc_52BF"),
        (12, "loc_52D7"),
        (SWITCH_DEFAULT, "loc_52F3"),
    )


    label("loc_51DB")

    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_51F9")

    NewScene("c0470", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_5207")

    NewScene("c0470", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_5215")

    NewScene("c045B", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_5223")

    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_5231")

    RemoveParty(0x2, 0x0)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_5242")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_525C")

    SetScenarioFlags(0x5D, 4)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_5277")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_528F")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c1210", 102, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_52A7")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_52BF")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0570", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_52D7")

    AddParty(0x3C, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0470", 0, 0, 0)
    IdleLoop()
    Jump("loc_52FD")

    label("loc_52F3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52FD")

    Jump("loc_4F79")

    label("loc_5302")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_37_4F4F end

    def Function_38_5310(): pass

    label("Function_38_5310")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_533A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5783")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Find Pills\x01",                          # 0
            "②▼Report to Sergei\x01",                    # 1
            "③▼Arrive at Hospital\x01",                  # 2
            "④▼Contact Lab from Reception\x01",          # 3
            "⑤▼Show Pills to Joachim\x01",               # 4
            "⑥▼Tio Collapses\x01",                       # 5
            "⑦▼Intel About D∴G Cult\x01",               # 6
            "⑧▼Disappearance of Miners\x01",             # 7
            "⑨▼Contact by Dudley\x01",                   # 8
            "⑩▼Dudley Joins In\x01",                     # 9
            "⑪▼Before Don's Room\x01",                   # 10
            "⑫▼After Battle Before Don's Room\x01",      # 11
            "⑬▼Begin Search of Don's Room\x01",          # 12
            "Cancel\x01",                                  # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_54F2"),
        (11, "loc_54F5"),
        (10, "loc_54F5"),
        (9, "loc_5531"),
        (8, "loc_5534"),
        (7, "loc_5537"),
        (6, "loc_5537"),
        (5, "loc_5537"),
        (4, "loc_553D"),
        (3, "loc_5540"),
        (2, "loc_5543"),
        (1, "loc_5549"),
        (0, "loc_554C"),
        (SWITCH_DEFAULT, "loc_55B7"),
    )


    label("loc_54F2")

    SetScenarioFlags(0xC6, 1)

    label("loc_54F5")

    SetScenarioFlags(0xC4, 0)
    SetScenarioFlags(0xC4, 1)
    SetScenarioFlags(0xC4, 2)
    SetScenarioFlags(0xC4, 3)
    SetScenarioFlags(0xC4, 4)
    SetScenarioFlags(0xC4, 5)
    SetScenarioFlags(0xC4, 6)
    SetScenarioFlags(0xC4, 7)
    SetScenarioFlags(0xC5, 0)
    SetScenarioFlags(0xC5, 1)
    SetScenarioFlags(0xC5, 2)
    SetScenarioFlags(0xC5, 3)
    SetScenarioFlags(0xC6, 5)
    SetScenarioFlags(0xC5, 4)
    SetScenarioFlags(0xC5, 5)
    SetScenarioFlags(0xC5, 6)
    SetScenarioFlags(0xC5, 7)
    SetScenarioFlags(0xC6, 0)
    SetScenarioFlags(0xC6, 6)
    SetScenarioFlags(0xC6, 7)

    label("loc_5531")

    SetScenarioFlags(0xC3, 7)

    label("loc_5534")

    SetScenarioFlags(0xC3, 6)

    label("loc_5537")

    SetScenarioFlags(0xC3, 4)
    SetScenarioFlags(0xC3, 5)

    label("loc_553D")

    SetScenarioFlags(0xC3, 3)

    label("loc_5540")

    SetScenarioFlags(0xC3, 2)

    label("loc_5543")

    SetScenarioFlags(0xC3, 0)
    SetScenarioFlags(0xC3, 1)

    label("loc_5549")

    SetScenarioFlags(0xC2, 7)

    label("loc_554C")

    SetScenarioFlags(0xC0, 0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)
    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 5)
    SetScenarioFlags(0xC1, 6)
    SetScenarioFlags(0xC1, 7)
    SetScenarioFlags(0xC2, 0)
    SetScenarioFlags(0xC2, 1)
    SetScenarioFlags(0xC2, 2)
    SetScenarioFlags(0xC2, 3)
    SetScenarioFlags(0xC2, 4)
    SetScenarioFlags(0xC2, 5)
    SetScenarioFlags(0xC2, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 62)
    Jump("loc_55BC")

    label("loc_55B7")

    Jump("loc_55BC")

    label("loc_55BC")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5614"),
        (1, "loc_563C"),
        (2, "loc_5654"),
        (3, "loc_566C"),
        (4, "loc_5684"),
        (5, "loc_569C"),
        (6, "loc_56B4"),
        (7, "loc_56CF"),
        (8, "loc_56EA"),
        (9, "loc_5705"),
        (10, "loc_571D"),
        (11, "loc_5739"),
        (12, "loc_5758"),
        (SWITCH_DEFAULT, "loc_5774"),
    )


    label("loc_5614")

    AddParty(0x3C, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0450", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_563C")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_5654")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("t1500", 100, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_566C")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_5684")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("t1650", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_569C")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_56B4")

    SetScenarioFlags(0x5C, 6)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_56CF")

    SetScenarioFlags(0x5D, 5)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_56EA")

    SetScenarioFlags(0x5D, 6)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_5705")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_571D")

    AddParty(0x9, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0597", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_5739")

    AddParty(0x9, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 2)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0597", 0, 0, 0)
    IdleLoop()
    Jump("loc_577E")

    label("loc_5758")

    AddParty(0x9, 0xFF, 0xFF)
    NewScene("c0597", 0, 0, 0)
    IdleLoop()
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    Jump("loc_577E")

    label("loc_5774")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_577E")

    Jump("loc_533A")

    label("loc_5783")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_38_5310 end

    def Function_39_5791(): pass

    label("Function_39_5791")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B92")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Doll Studio\x01",                          # 0
            "②▼Cooperation With Bracer Guild\x01",        # 1
            "③▼To the Hospital\x01",                      # 2
            "④▼Contact by Dudley\x01",                    # 3
            "⑤▼Find Abandoned Bus\x01",                   # 4
            "⑥▼Arrive at Hospital at Night\x01",          # 5
            "⑦▼After Battle, Hospital at Night\x01",      # 6
            "⑧▼Dormitory 1F - Entrance\x01",              # 7
            "⑨▼Investigate Dormitory 1F\x01",             # 8
            "⑩▼Dormitory 2F - Terrace\x01",               # 9
            "⑪▼Open With Hospital Key\x01",               # 10
            "⑫▼Hospital 2F - Passage ①\x01",             # 11
            "⑬▼Hospital 2F - Passage ②\x01",             # 12
            "Cancel\x01",                                   # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_5998"),
        (11, "loc_599B"),
        (10, "loc_59A1"),
        (9, "loc_59A7"),
        (8, "loc_59AD"),
        (7, "loc_59B0"),
        (6, "loc_59B3"),
        (5, "loc_59B3"),
        (4, "loc_59B6"),
        (3, "loc_59B9"),
        (2, "loc_59BC"),
        (1, "loc_59BC"),
        (0, "loc_59BC"),
        (SWITCH_DEFAULT, "loc_59D0"),
    )


    label("loc_5998")

    SetScenarioFlags(0xE1, 7)

    label("loc_599B")

    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)

    label("loc_59A1")

    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)

    label("loc_59A7")

    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)

    label("loc_59AD")

    SetScenarioFlags(0xE0, 4)

    label("loc_59B0")

    SetScenarioFlags(0xE0, 3)

    label("loc_59B3")

    SetScenarioFlags(0xE0, 2)

    label("loc_59B6")

    SetScenarioFlags(0xE0, 1)

    label("loc_59B9")

    SetScenarioFlags(0xE0, 0)

    label("loc_59BC")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 63)
    Jump("loc_59D5")

    label("loc_59D0")

    Jump("loc_59D5")

    label("loc_59D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59F2")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_59F2")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A4A"),
        (1, "loc_5A5B"),
        (2, "loc_5A6C"),
        (3, "loc_5A7D"),
        (4, "loc_5A8B"),
        (5, "loc_5AC1"),
        (6, "loc_5AF7"),
        (7, "loc_5B11"),
        (8, "loc_5B24"),
        (9, "loc_5B37"),
        (10, "loc_5B4A"),
        (11, "loc_5B5D"),
        (12, "loc_5B70"),
        (SWITCH_DEFAULT, "loc_5B83"),
    )


    label("loc_5A4A")

    SetScenarioFlags(0x5C, 0)
    NewScene("t3010", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5A5B")

    SetScenarioFlags(0x5C, 0)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5A6C")

    SetScenarioFlags(0x5D, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5A7D")

    NewScene("r1500", 100, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5A8B")

    ReplaceBGM("ed7200", "ed7203")
    ReplaceBGM("ed7202", "ed7203")
    ReplaceBGM("ed7100", "ed7203")
    ReplaceBGM("ed7101", "ed7203")
    ReplaceBGM("ed7111", "ed7203")
    ReplaceBGM("ed7116", "ed7203")
    ReplaceBGM("ed7117", "ed7203")
    ReplaceBGM("ed7124", "ed7203")
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5AC1")

    ReplaceBGM("ed7200", "ed7203")
    ReplaceBGM("ed7202", "ed7203")
    ReplaceBGM("ed7100", "ed7203")
    ReplaceBGM("ed7101", "ed7203")
    ReplaceBGM("ed7111", "ed7203")
    ReplaceBGM("ed7116", "ed7203")
    ReplaceBGM("ed7117", "ed7203")
    ReplaceBGM("ed7124", "ed7203")
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5AF7")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5B11")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t151B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5B24")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t151B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5B37")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t150B", 105, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5B4A")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5B5D")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t154B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5B70")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t154B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5B8D")

    label("loc_5B83")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B8D")

    Jump("loc_57BE")

    label("loc_5B92")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_39_5791 end

    def Function_40_5BA0(): pass

    label("Function_40_5BA0")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FE5")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Hospital 3F - Passage\x01",             # 0
            "②▼Check Nurses, Philia\x01",              # 1
            "③▼Rescue Cecile\x01",                     # 2
            "④▼Rescue Cecile After Battle\x01",        # 3
            "⑤▼Research Ward 1F - Entrance\x01",       # 4
            "⑥▼Find Doctors\x01",                      # 5
            "⑦▼Get Card Key\x01",                      # 6
            "⑧▼Fight Ernest\x01",                      # 7
            "⑨▼After Ernest Fight\x01",                # 8
            "⑩▼Joachim's Lab\x01",                     # 9
            "⑪▼Guards Came Along\x01",                 # 10
            "⑫▼SSS Raid\x01",                          # 11
            "⑬▼SSS Raid - 2\x01",                      # 12
            "⑭★Ernest, Flying Dragon Escape\x01",      # 13
            "⑮★Renne, Pater-Mater Escape\x01",         # 14
            "Cancel\x01",                                # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_5DA6"),
        (13, "loc_5DA6"),
        (12, "loc_5DA6"),
        (11, "loc_5DA6"),
        (10, "loc_5DA6"),
        (9, "loc_5DA9"),
        (8, "loc_5DAC"),
        (7, "loc_5DAC"),
        (6, "loc_5DB2"),
        (5, "loc_5DB5"),
        (4, "loc_5DB8"),
        (3, "loc_5DBB"),
        (2, "loc_5DBB"),
        (1, "loc_5DBE"),
        (0, "loc_5DC1"),
        (SWITCH_DEFAULT, "loc_5DFC"),
    )


    label("loc_5DA6")

    SetScenarioFlags(0xE3, 6)

    label("loc_5DA9")

    SetScenarioFlags(0xE3, 5)

    label("loc_5DAC")

    SetScenarioFlags(0xE3, 3)
    SetScenarioFlags(0xE3, 4)

    label("loc_5DB2")

    SetScenarioFlags(0xE3, 2)

    label("loc_5DB5")

    SetScenarioFlags(0xE3, 0)

    label("loc_5DB8")

    SetScenarioFlags(0xE2, 7)

    label("loc_5DBB")

    SetScenarioFlags(0xE2, 4)

    label("loc_5DBE")

    SetScenarioFlags(0xE2, 3)

    label("loc_5DC1")

    SetScenarioFlags(0xE0, 0)
    SetScenarioFlags(0xE0, 1)
    SetScenarioFlags(0xE0, 2)
    SetScenarioFlags(0xE0, 3)
    SetScenarioFlags(0xE0, 4)
    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)
    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)
    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)
    SetScenarioFlags(0xE1, 7)
    SetScenarioFlags(0xE2, 1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 63)
    Jump("loc_5E01")

    label("loc_5DFC")

    Jump("loc_5E01")

    label("loc_5E01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E1E")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_5E1E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5E82"),
        (1, "loc_5E95"),
        (2, "loc_5EA8"),
        (3, "loc_5EBB"),
        (4, "loc_5ED1"),
        (5, "loc_5EE4"),
        (6, "loc_5EF7"),
        (7, "loc_5F0A"),
        (8, "loc_5F1D"),
        (9, "loc_5F33"),
        (10, "loc_5F4A"),
        (11, "loc_5F64"),
        (12, "loc_5F7B"),
        (13, "loc_5FAE"),
        (14, "loc_5FC5"),
        (SWITCH_DEFAULT, "loc_5FD6"),
    )


    label("loc_5E82")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t155B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5E95")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t155B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5EA8")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t160B", 103, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5EBB")

    SetScenarioFlags(0x5C, 1)
    ReplaceBGM("ed7123", "ed7510")
    NewScene("t160B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5ED1")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t162B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5EE4")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t163B", 102, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5EF7")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t164B", 116, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5F0A")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t165B", 101, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5F1D")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7123", "ed7510")
    NewScene("t165B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5F33")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t165B", 101, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5F4A")

    SetScenarioFlags(0x5C, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5F64")

    Call(1, 29)
    Call(1, 64)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5F7B")

    AddParty(0x9, 0xFF, 0xFF)
    Call(1, 29)
    Call(1, 64)
    SetChrChipPat(0x0, 0x1, 0x9B)
    SetChrChipPat(0x3, 0x1, 0x9C)
    LoadChrChipPat()
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c020B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5FAE")

    Call(1, 29)
    Call(1, 64)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3300", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5FC5")

    SetScenarioFlags(0x5C, 1)
    NewScene("e3300", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FE0")

    label("loc_5FD6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FE0")

    Jump("loc_5BCD")

    label("loc_5FE5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_40_5BA0 end

    def Function_41_5FF3(): pass

    label("Function_41_5FF3")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6020")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63F1")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼East Exit Bridge\x01",                     # 0
            "②▼East Exit Bridge After Battle\x01",        # 1
            "③▼In Limosine\x01",                          # 2
            "④▼Explain Situation at IBC\x01",             # 3
            "⑤▼Break at IBC\x01",                         # 4
            "⑥▼Contact by President Room\x01",            # 5
            "⑦▼Report from Guards\x01",                   # 6
            "⑧▼Start Battles\x01",                        # 7
            "⑨▼End Battles\x01",                          # 8
            "⑩▼Vipers and Testaments Join In\x01",        # 9
            "⑪▼Joachim Escapes\x01",                      # 10
            "⑫▼Breaking Through With Limousine\x01",      # 11
            "⑬▼In Limosine\x01",                          # 12
            "Cancel\x01",                                   # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_61D0"),
        (11, "loc_61D0"),
        (10, "loc_61D0"),
        (9, "loc_61D0"),
        (8, "loc_61D0"),
        (7, "loc_61D0"),
        (6, "loc_61D3"),
        (5, "loc_61D6"),
        (4, "loc_61E2"),
        (3, "loc_61E8"),
        (2, "loc_61E8"),
        (1, "loc_61E8"),
        (0, "loc_61E8"),
        (SWITCH_DEFAULT, "loc_623E"),
    )


    label("loc_61D0")

    SetScenarioFlags(0xE7, 5)

    label("loc_61D3")

    SetScenarioFlags(0xE4, 4)

    label("loc_61D6")

    SetScenarioFlags(0xE4, 0)
    SetScenarioFlags(0xE4, 1)
    SetScenarioFlags(0xE4, 2)
    SetScenarioFlags(0xE4, 3)

    label("loc_61E2")

    Call(2, 51)
    SetScenarioFlags(0xE3, 7)

    label("loc_61E8")

    SetScenarioFlags(0xE0, 0)
    SetScenarioFlags(0xE0, 1)
    SetScenarioFlags(0xE0, 2)
    SetScenarioFlags(0xE0, 3)
    SetScenarioFlags(0xE0, 4)
    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)
    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)
    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)
    SetScenarioFlags(0xE1, 7)
    SetScenarioFlags(0xE2, 1)
    SetScenarioFlags(0xE2, 3)
    SetScenarioFlags(0xE2, 4)
    SetScenarioFlags(0xE2, 7)
    SetScenarioFlags(0xE3, 0)
    SetScenarioFlags(0xE3, 2)
    SetScenarioFlags(0xE3, 3)
    SetScenarioFlags(0xE3, 4)
    SetScenarioFlags(0xE3, 5)
    SetScenarioFlags(0xE3, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 64)
    Jump("loc_6243")

    label("loc_623E")

    Jump("loc_6243")

    label("loc_6243")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_629B"),
        (1, "loc_62C4"),
        (2, "loc_62F5"),
        (3, "loc_630E"),
        (4, "loc_631F"),
        (5, "loc_6336"),
        (6, "loc_634D"),
        (7, "loc_6364"),
        (8, "loc_6372"),
        (9, "loc_6383"),
        (10, "loc_639D"),
        (11, "loc_63B7"),
        (12, "loc_63C8"),
        (SWITCH_DEFAULT, "loc_63E2"),
    )


    label("loc_629B")

    SetChrChipPat(0x0, 0x1, 0x9B)
    SetChrChipPat(0x3, 0x1, 0x9C)
    LoadChrChipPat()
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r000B", 0, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_62C4")

    AddParty(0x9F, 0xFF, 0xFF)
    AddParty(0x57, 0xFF, 0xFF)
    SetChrChipPat(0x0, 0x1, 0x9B)
    SetChrChipPat(0x3, 0x1, 0x9C)
    LoadChrChipPat()
    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r000B", 0, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_62F5")

    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x57, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_630E")

    SetScenarioFlags(0x5C, 0)
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_631F")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c134B", 101, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_6336")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c134B", 101, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_634D")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c134B", 101, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_6364")

    NewScene("c131B", 0, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_6372")

    SetScenarioFlags(0x5C, 2)
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_6383")

    SetScenarioFlags(0x5C, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_639D")

    SetScenarioFlags(0x5C, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_63B7")

    SetScenarioFlags(0x5C, 2)
    NewScene("r000B", 0, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_63C8")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Jump("loc_63EC")

    label("loc_63E2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63EC")

    Jump("loc_6020")

    label("loc_63F1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_41_5FF3 end

    def Function_42_63FF(): pass

    label("Function_42_63FF")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_642C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_680F")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Arrive at Sun Fort\x01",            # 0
            "②▼Find Cult Mark\x01",                # 1
            "③▼Find Vertical Shaft\x01",           # 2
            "④▼Demon Mafiosos\x01",                # 3
            "⑤▼Blood Pond Area\x01",               # 4
            "⑥▼Find Missing People\x01",           # 5
            "⑦▼Find Marconi\x01",                  # 6
            "⑧▼Fight Demon Ernest\x01",            # 7
            "⑨▼After Demon Ernest Fight\x01",      # 8
            "⑩▼Fight Garcia\x01",                  # 9
            "⑪▼After Garcia Fight\x01",            # 10
            "⑫▼Showdown With Joachim\x01",         # 11
            "⑬▼Fight Demon Joachim\x01",           # 12
            "Cancel\x01",                            # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_65C6"),
        (11, "loc_65C6"),
        (10, "loc_65C9"),
        (9, "loc_65C9"),
        (8, "loc_65CC"),
        (7, "loc_65CC"),
        (6, "loc_65CF"),
        (5, "loc_65DB"),
        (4, "loc_65DE"),
        (3, "loc_65ED"),
        (2, "loc_65F0"),
        (1, "loc_65F3"),
        (0, "loc_65F6"),
        (SWITCH_DEFAULT, "loc_665B"),
    )


    label("loc_65C6")

    SetScenarioFlags(0xE6, 4)

    label("loc_65C9")

    SetScenarioFlags(0xE6, 3)

    label("loc_65CC")

    SetScenarioFlags(0xE6, 2)

    label("loc_65CF")

    SetScenarioFlags(0xE5, 6)
    SetScenarioFlags(0xE5, 7)
    SetScenarioFlags(0xE6, 0)
    SetScenarioFlags(0xE6, 1)

    label("loc_65DB")

    SetScenarioFlags(0xE5, 5)

    label("loc_65DE")

    SetScenarioFlags(0xE5, 0)
    SetScenarioFlags(0xE5, 1)
    SetScenarioFlags(0xE5, 2)
    SetScenarioFlags(0xE5, 3)
    SetScenarioFlags(0xE5, 4)

    label("loc_65ED")

    SetScenarioFlags(0xE4, 7)

    label("loc_65F0")

    SetScenarioFlags(0xE4, 6)

    label("loc_65F3")

    SetScenarioFlags(0xE4, 5)

    label("loc_65F6")

    SetScenarioFlags(0xE0, 0)
    SetScenarioFlags(0xE0, 1)
    SetScenarioFlags(0xE0, 2)
    SetScenarioFlags(0xE0, 3)
    SetScenarioFlags(0xE0, 4)
    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)
    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)
    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)
    SetScenarioFlags(0xE1, 7)
    SetScenarioFlags(0xE2, 1)
    SetScenarioFlags(0xE2, 3)
    SetScenarioFlags(0xE2, 4)
    SetScenarioFlags(0xE2, 7)
    SetScenarioFlags(0xE3, 0)
    SetScenarioFlags(0xE3, 2)
    SetScenarioFlags(0xE3, 3)
    SetScenarioFlags(0xE3, 4)
    SetScenarioFlags(0xE3, 5)
    SetScenarioFlags(0xE3, 6)
    SetScenarioFlags(0xE3, 7)
    SetScenarioFlags(0xE4, 0)
    SetScenarioFlags(0xE4, 1)
    SetScenarioFlags(0xE4, 2)
    SetScenarioFlags(0xE4, 3)
    SetScenarioFlags(0xE4, 4)
    SetScenarioFlags(0xE7, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6660")

    label("loc_665B")

    Jump("loc_6660")

    label("loc_6660")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6681")
    AddParty(0x6, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)

    label("loc_6681")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_66D9"),
        (1, "loc_66F0"),
        (2, "loc_6709"),
        (3, "loc_671D"),
        (4, "loc_6731"),
        (5, "loc_6745"),
        (6, "loc_6759"),
        (7, "loc_676D"),
        (8, "loc_6781"),
        (9, "loc_6798"),
        (10, "loc_67AC"),
        (11, "loc_67CC"),
        (12, "loc_67E0"),
        (SWITCH_DEFAULT, "loc_6800"),
    )


    label("loc_66D9")

    Call(1, 29)
    Call(1, 65)
    SetScenarioFlags(0x5C, 0)
    NewScene("r307B", 0, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_66F0")

    Call(1, 29)
    Call(1, 65)
    ReplaceBGM("ed7510", "ed7305")
    NewScene("m3000", 108, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_6709")

    Call(1, 29)
    Call(1, 65)
    NewScene("m3002", 0, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_671D")

    Call(1, 29)
    Call(1, 66)
    NewScene("m3012", 0, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_6731")

    Call(1, 29)
    Call(1, 66)
    NewScene("m3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_6745")

    Call(1, 29)
    Call(1, 66)
    NewScene("m3021", 0, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_6759")

    Call(1, 29)
    Call(1, 66)
    NewScene("m3023", 104, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_676D")

    Call(1, 29)
    Call(1, 66)
    NewScene("m3021", 105, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_6781")

    Call(1, 29)
    Call(1, 66)
    SetScenarioFlags(0x5C, 0)
    NewScene("m3021", 0, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_6798")

    Call(1, 29)
    Call(1, 67)
    NewScene("m3034", 0, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_67AC")

    Call(1, 29)
    Call(1, 67)
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m3034", 0, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_67CC")

    Call(1, 29)
    Call(1, 68)
    NewScene("m3099", 0, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_67E0")

    Call(1, 29)
    Call(1, 68)
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m3099", 0, 0, 0)
    IdleLoop()
    Jump("loc_680A")

    label("loc_6800")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_680A")

    Jump("loc_642C")

    label("loc_680F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_42_63FF end

    def Function_43_681D(): pass

    label("Function_43_681D")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_684A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A19")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼Pater-Mater Joins In\x01",                   # 0
            "②▼After Demon Joachim Fight\x01",              # 1
            "③▼Daybreak over Ancient Battlefield\x01",      # 2
            "④▼Staff Roll\x01",                             # 3
            "⑤▼Epilogue\x01",                               # 4
            "⑥▼Epilogue - 2\x01",                           # 5
            "Cancel\x01",                                     # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (5, "loc_6924"),
        (4, "loc_6924"),
        (3, "loc_6924"),
        (2, "loc_6924"),
        (1, "loc_6924"),
        (0, "loc_6924"),
        (SWITCH_DEFAULT, "loc_6935"),
    )


    label("loc_6924")

    Call(2, 11)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_693A")

    label("loc_6935")

    Jump("loc_693A")

    label("loc_693A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_695B")
    AddParty(0x6, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)

    label("loc_695B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6989"),
        (1, "loc_69A3"),
        (2, "loc_69BD"),
        (3, "loc_69D7"),
        (4, "loc_69E8"),
        (5, "loc_69F9"),
        (SWITCH_DEFAULT, "loc_6A0A"),
    )


    label("loc_6989")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x196), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m3099", 0, 0, 0)
    IdleLoop()
    Jump("loc_6A14")

    label("loc_69A3")

    SetScenarioFlags(0x5C, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x196), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m3099", 0, 0, 0)
    IdleLoop()
    Jump("loc_6A14")

    label("loc_69BD")

    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x208), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Jump("loc_6A14")

    label("loc_69D7")

    SetScenarioFlags(0x5C, 1)
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Jump("loc_6A14")

    label("loc_69E8")

    SetScenarioFlags(0x5C, 0)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Jump("loc_6A14")

    label("loc_69F9")

    SetScenarioFlags(0x5E, 0)
    NewScene("e3500", 0, 0, 0)
    IdleLoop()
    Jump("loc_6A14")

    label("loc_6A0A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A14")

    Jump("loc_684A")

    label("loc_6A19")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_43_681D end

    def Function_44_6A27(): pass

    label("Function_44_6A27")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BDA")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "★'Arrived at Crossbell Police'\x01",          # 0
            "★'Arrived at SSS'\x01",                       # 1
            "★'Talked With Tio'\x01",                      # 2
            "★'Heard SSS Explanation'\x01",                # 3
            "▼①Start Prologue\x01",                       # 4
            "★'Received First Support Requests'\x01",      # 5
            "▼②Heard from Grace\x01",                     # 6
            "★'Had Dialogue With Mr. Grimwood'\x01",       # 7
            "Cancel\x01",                                   # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (7, "loc_6B66"),
        (6, "loc_6B6F"),
        (5, "loc_6B81"),
        (4, "loc_6B8F"),
        (3, "loc_6B92"),
        (2, "loc_6B95"),
        (1, "loc_6B9E"),
        (0, "loc_6BB6"),
        (SWITCH_DEFAULT, "loc_6BCB"),
    )


    label("loc_6B66")

    SetScenarioFlags(0x42, 6)
    SetScenarioFlags(0x42, 7)
    SetScenarioFlags(0x43, 0)

    label("loc_6B6F")

    SetScenarioFlags(0x42, 0)
    SetScenarioFlags(0x42, 1)
    SetScenarioFlags(0x42, 2)
    SetScenarioFlags(0x42, 3)
    SetScenarioFlags(0x42, 4)
    SetScenarioFlags(0x42, 5)

    label("loc_6B81")

    SetScenarioFlags(0x41, 7)
    OP_29(0x3E, 0x4, 0x2)
    OP_29(0x3E, 0x1, 0x0)

    label("loc_6B8F")

    SetScenarioFlags(0x41, 6)

    label("loc_6B92")

    SetScenarioFlags(0x41, 5)

    label("loc_6B95")

    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)
    SetScenarioFlags(0x41, 4)

    label("loc_6B9E")

    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 7)
    SetScenarioFlags(0x41, 0)
    SetScenarioFlags(0x41, 1)

    label("loc_6BB6")

    SetScenarioFlags(0x40, 0)
    SetScenarioFlags(0x40, 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6BD5")

    label("loc_6BCB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6BD5")

    Jump("loc_6A3A")

    label("loc_6BDA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_44_6A27 end

    def Function_45_6BE8(): pass

    label("Function_45_6BE8")

    Call(2, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6BFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E5F")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼③Start First Chapter\x01",                 # 0
            "★'Left Village Chief's Residence'\x01",      # 1
            "★'Finished Listening'\x01",                  # 2
            "▼④Return from Armorica Village\x01",        # 3
            "★'Search for Bus'\x01",                      # 4
            "★'Reunited With Cecile'\x01",                # 5
            "★'Had Dialogue With Resident'\x01",          # 6
            "★'Found Monsters' Footprints'\x01",          # 7
            "★'Took Measures Against Monsters'\x01",      # 8
            "▼⑤Second Day, to Mainz\x01",                # 9
            "★'Had Dialogue With Mayor'\x01",             # 10
            "★'Had Meeting'\x01",                         # 11
            "Cancel\x01",                                  # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (11, "loc_6DB7"),
        (10, "loc_6DBA"),
        (9, "loc_6DDB"),
        (8, "loc_6DE1"),
        (7, "loc_6DF3"),
        (6, "loc_6E0B"),
        (5, "loc_6E0E"),
        (4, "loc_6E20"),
        (3, "loc_6E23"),
        (2, "loc_6E26"),
        (1, "loc_6E2C"),
        (0, "loc_6E3E"),
        (SWITCH_DEFAULT, "loc_6E50"),
    )


    label("loc_6DB7")

    SetScenarioFlags(0x65, 5)

    label("loc_6DBA")

    SetScenarioFlags(0x64, 2)
    SetScenarioFlags(0x64, 3)
    SetScenarioFlags(0x64, 4)
    SetScenarioFlags(0x64, 5)
    SetScenarioFlags(0x64, 6)
    SetScenarioFlags(0x64, 7)
    SetScenarioFlags(0x65, 0)
    SetScenarioFlags(0x65, 1)
    SetScenarioFlags(0x65, 2)
    SetScenarioFlags(0x65, 3)
    SetScenarioFlags(0x65, 4)

    label("loc_6DDB")

    SetScenarioFlags(0x64, 0)
    SetScenarioFlags(0x64, 1)

    label("loc_6DE1")

    SetScenarioFlags(0x63, 2)
    SetScenarioFlags(0x63, 3)
    SetScenarioFlags(0x63, 4)
    SetScenarioFlags(0x63, 5)
    SetScenarioFlags(0x63, 6)
    SetScenarioFlags(0x63, 7)

    label("loc_6DF3")

    SetScenarioFlags(0x62, 2)
    SetScenarioFlags(0x62, 3)
    SetScenarioFlags(0x62, 4)
    SetScenarioFlags(0x62, 5)
    SetScenarioFlags(0x62, 6)
    SetScenarioFlags(0x62, 7)
    SetScenarioFlags(0x63, 0)
    SetScenarioFlags(0x63, 1)

    label("loc_6E0B")

    SetScenarioFlags(0x62, 1)

    label("loc_6E0E")

    SetScenarioFlags(0x61, 3)
    SetScenarioFlags(0x61, 4)
    SetScenarioFlags(0x61, 5)
    SetScenarioFlags(0x61, 6)
    SetScenarioFlags(0x61, 7)
    SetScenarioFlags(0x62, 0)

    label("loc_6E20")

    SetScenarioFlags(0x61, 2)

    label("loc_6E23")

    SetScenarioFlags(0x61, 1)

    label("loc_6E26")

    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x61, 0)

    label("loc_6E2C")

    SetScenarioFlags(0x60, 1)
    SetScenarioFlags(0x60, 2)
    SetScenarioFlags(0x60, 3)
    SetScenarioFlags(0x60, 4)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)

    label("loc_6E3E")

    SetScenarioFlags(0x60, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E5A")

    label("loc_6E50")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E5A")

    Jump("loc_6BFE")

    label("loc_6E5F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_45_6BE8 end

    def Function_46_6E6D(): pass

    label("Function_46_6E6D")

    Call(2, 5)
    Call(2, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_707A")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼⑥Start Second Chapter\x01",             # 0
            "▼⑦Start Gathering Information\x01",      # 1
            "★'Reviewed Support Requests'\x01",        # 2
            "★'Seek Elie'\x01",                        # 3
            "▼⑧To IBC Building\x01",                  # 4
            "▼⑨To Stargazer's Tower\x01",             # 5
            "★'Started Patrol'\x01",                   # 6
            "★'Act 2 Begun'\x01",                      # 7
            "★'Act 3 Begun'\x01",                      # 8
            "★'Finale Begun'\x01",                     # 9
            "Cancel\x01",                               # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (9, "loc_6FC4"),
        (8, "loc_6FD0"),
        (7, "loc_6FDC"),
        (6, "loc_6FE8"),
        (5, "loc_6FF7"),
        (4, "loc_7024"),
        (3, "loc_702A"),
        (2, "loc_702D"),
        (1, "loc_703F"),
        (0, "loc_7054"),
        (SWITCH_DEFAULT, "loc_7066"),
    )


    label("loc_6FC4")

    SetScenarioFlags(0x85, 5)
    SetScenarioFlags(0x85, 6)
    SetScenarioFlags(0x85, 7)
    SetScenarioFlags(0x86, 0)

    label("loc_6FD0")

    SetScenarioFlags(0x85, 1)
    SetScenarioFlags(0x85, 2)
    SetScenarioFlags(0x85, 3)
    SetScenarioFlags(0x85, 4)

    label("loc_6FDC")

    SetScenarioFlags(0x84, 5)
    SetScenarioFlags(0x84, 6)
    SetScenarioFlags(0x84, 7)
    SetScenarioFlags(0x85, 0)

    label("loc_6FE8")

    SetScenarioFlags(0x84, 0)
    SetScenarioFlags(0x84, 1)
    SetScenarioFlags(0x84, 2)
    SetScenarioFlags(0x84, 3)
    SetScenarioFlags(0x84, 4)

    label("loc_6FF7")

    SetScenarioFlags(0x82, 1)
    SetScenarioFlags(0x82, 2)
    SetScenarioFlags(0x82, 3)
    SetScenarioFlags(0x82, 4)
    SetScenarioFlags(0x82, 5)
    SetScenarioFlags(0x82, 6)
    SetScenarioFlags(0x82, 7)
    SetScenarioFlags(0x83, 0)
    SetScenarioFlags(0x83, 1)
    SetScenarioFlags(0x83, 2)
    SetScenarioFlags(0x83, 3)
    SetScenarioFlags(0x83, 4)
    SetScenarioFlags(0x83, 5)
    SetScenarioFlags(0x83, 6)
    SetScenarioFlags(0x83, 7)

    label("loc_7024")

    SetScenarioFlags(0x81, 7)
    SetScenarioFlags(0x82, 0)

    label("loc_702A")

    SetScenarioFlags(0x81, 6)

    label("loc_702D")

    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)
    SetScenarioFlags(0x81, 2)
    SetScenarioFlags(0x81, 3)
    SetScenarioFlags(0x81, 4)
    SetScenarioFlags(0x81, 5)

    label("loc_703F")

    SetScenarioFlags(0x80, 1)
    SetScenarioFlags(0x80, 2)
    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)
    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x80, 7)

    label("loc_7054")

    SetScenarioFlags(0x80, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7075")

    label("loc_7066")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7075")

    label("loc_7075")

    Jump("loc_6E86")

    label("loc_707A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_46_6E6D end

    def Function_47_7088(): pass

    label("Function_47_7088")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_736F")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼⑩Festival Second Day Start\x01",                         # 0
            "★'Contacted by Fran' (3-1)\x01",                           # 1
            "▼⑪Festival Third Day Start\x01",                          # 2
            "▼⑫Festival Third Day Return After Key Quest\x01",         # 3
            "★'Arrived at Geofront A'\x01",                             # 4
            "▼⑬Festival Fourth Day Start\x01",                         # 5
            "▼⑭Festival Fourth Day Return After Key Quest\x01",        # 6
            "★'Contacted by Fran' (3-3)\x01",                           # 7
            "★'Begun Search for Colin'\x01",                            # 8
            "★'Contacted by Randy ①'\x01",                             # 9
            "★'Renne Has Tagged Along'\x01",                            # 10
            "★'Contacted by Elie ①'\x01",                              # 11
            "★'Contacted by Tio ①'\x01",                               # 12
            "★'Contacted by Randy & Tio'\x01",                          # 13
            "★'Left on West Crossbell Highway to Find Colin'\x01",      # 14
            "Cancel\x01",                                                # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_7301"),
        (13, "loc_7304"),
        (12, "loc_730A"),
        (11, "loc_7310"),
        (10, "loc_7313"),
        (9, "loc_7316"),
        (8, "loc_731C"),
        (7, "loc_731F"),
        (6, "loc_7322"),
        (5, "loc_7325"),
        (4, "loc_7337"),
        (3, "loc_7340"),
        (2, "loc_7343"),
        (1, "loc_7346"),
        (0, "loc_7349"),
        (SWITCH_DEFAULT, "loc_735B"),
    )


    label("loc_7301")

    SetScenarioFlags(0xA2, 7)

    label("loc_7304")

    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xA2, 6)

    label("loc_730A")

    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xA2, 4)

    label("loc_7310")

    SetScenarioFlags(0xA2, 2)

    label("loc_7313")

    SetScenarioFlags(0xA2, 1)

    label("loc_7316")

    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xA2, 0)

    label("loc_731C")

    SetScenarioFlags(0xA1, 6)

    label("loc_731F")

    SetScenarioFlags(0xA1, 5)

    label("loc_7322")

    SetScenarioFlags(0xAA, 2)

    label("loc_7325")

    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)

    label("loc_7337")

    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)

    label("loc_7340")

    SetScenarioFlags(0xA0, 3)

    label("loc_7343")

    SetScenarioFlags(0xA0, 2)

    label("loc_7346")

    SetScenarioFlags(0xA0, 1)

    label("loc_7349")

    SetScenarioFlags(0xA0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_736A")

    label("loc_735B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_736A")

    label("loc_736A")

    Jump("loc_70A4")

    label("loc_736F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_47_7088 end

    def Function_48_737D(): pass

    label("Function_48_737D")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xAA, 2)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xA2, 4)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xA2, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7635")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼⑮Festival Final Day Start\x01",            # 0
            "★'Arrived at Mishelam'\x01",                 # 1
            "★'Headed to Boutique'\x01",                  # 2
            "★'Headed to Auction'\x01",                   # 3
            "★'Arrived at Auction'\x01",                  # 4
            "★'Joined With Mariabell'\x01",               # 5
            "★'Incident Occurred in Mansion'\x01",        # 6
            "★'Found KeA'\x01",                           # 7
            "▼⑯Intermission\x01",                        # 8
            "★'Consulted Sister Marble'\x01",             # 9
            "★'Arrived at St. Ursula Hospital'\x01",      # 10
            "★'Chased After KeA'\x01",                    # 11
            "Cancel\x01",                                  # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (7, "loc_7576"),
        (6, "loc_757F"),
        (5, "loc_7582"),
        (4, "loc_759D"),
        (3, "loc_75A0"),
        (2, "loc_75A3"),
        (1, "loc_75B5"),
        (0, "loc_75C4"),
        (11, "loc_75E8"),
        (10, "loc_75F1"),
        (9, "loc_75F7"),
        (8, "loc_7603"),
        (SWITCH_DEFAULT, "loc_7621"),
    )


    label("loc_7576")

    SetScenarioFlags(0xA6, 3)
    SetScenarioFlags(0xA6, 4)
    SetScenarioFlags(0xA6, 5)

    label("loc_757F")

    SetScenarioFlags(0xA6, 2)

    label("loc_7582")

    SetScenarioFlags(0xA5, 1)
    SetScenarioFlags(0xA5, 2)
    SetScenarioFlags(0xA5, 3)
    SetScenarioFlags(0xA5, 4)
    SetScenarioFlags(0xA5, 5)
    SetScenarioFlags(0xA5, 6)
    SetScenarioFlags(0xA5, 7)
    SetScenarioFlags(0xA6, 0)
    SetScenarioFlags(0xA6, 1)

    label("loc_759D")

    SetScenarioFlags(0xA5, 0)

    label("loc_75A0")

    SetScenarioFlags(0xA4, 7)

    label("loc_75A3")

    SetScenarioFlags(0xA4, 1)
    SetScenarioFlags(0xA4, 2)
    SetScenarioFlags(0xA4, 3)
    SetScenarioFlags(0xA4, 4)
    SetScenarioFlags(0xA4, 5)
    SetScenarioFlags(0xA4, 6)

    label("loc_75B5")

    SetScenarioFlags(0xA3, 4)
    SetScenarioFlags(0xA3, 5)
    SetScenarioFlags(0xA3, 6)
    SetScenarioFlags(0xA3, 7)
    SetScenarioFlags(0xA4, 0)

    label("loc_75C4")

    SetScenarioFlags(0xA3, 0)
    SetScenarioFlags(0xA3, 1)
    SetScenarioFlags(0xA3, 2)
    SetScenarioFlags(0xA3, 3)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7630")

    label("loc_75E8")

    SetScenarioFlags(0xA8, 5)
    SetScenarioFlags(0xA8, 6)
    SetScenarioFlags(0xA8, 7)

    label("loc_75F1")

    SetScenarioFlags(0xA8, 3)
    SetScenarioFlags(0xA8, 4)

    label("loc_75F7")

    SetScenarioFlags(0xA7, 7)
    SetScenarioFlags(0xA8, 0)
    SetScenarioFlags(0xA8, 1)
    SetScenarioFlags(0xA8, 2)

    label("loc_7603")

    SetScenarioFlags(0xA7, 6)
    Call(2, 8)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7630")

    label("loc_7621")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7630")

    label("loc_7630")

    Jump("loc_73DB")

    label("loc_7635")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_48_737D end

    def Function_49_7643(): pass

    label("Function_49_7643")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7665")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_791B")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼⑰Start Fourth Chapter (First Day)\x01",                             # 0
            "★'Returned to Crossbell City by Car'\x01",                            # 1
            "★'Had Dialogue With Drake'\x01",                                      # 2
            "▼⑲Second Day (Heiyue Raid)\x01",                                     # 3
            "★'Begun Drug Investigation With First Division'\x01",                 # 4
            "★'Returned to Crossbell'\x01",                                        # 5
            "▼⑳Third Day (Missing Person)\x01",                                   # 6
            "★'Disappearance of Securities Man at Residential District'\x01",      # 7
            "★'Had Discussion With Dudley'\x01",                                   # 8
            "★'Begun Search of Don's Room'\x01",                                   # 9
            "Cancel\x01",                                                           # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (9, "loc_7835"),
        (8, "loc_7877"),
        (7, "loc_7886"),
        (6, "loc_7889"),
        (5, "loc_788C"),
        (4, "loc_789B"),
        (3, "loc_78AD"),
        (2, "loc_78B9"),
        (1, "loc_78CB"),
        (0, "loc_78EC"),
        (SWITCH_DEFAULT, "loc_7907"),
    )


    label("loc_7835")

    SetScenarioFlags(0xC4, 0)
    SetScenarioFlags(0xC4, 1)
    SetScenarioFlags(0xC4, 2)
    SetScenarioFlags(0xC4, 3)
    SetScenarioFlags(0xC4, 4)
    SetScenarioFlags(0xC4, 5)
    SetScenarioFlags(0xC4, 6)
    SetScenarioFlags(0xC4, 7)
    SetScenarioFlags(0xC5, 0)
    SetScenarioFlags(0xC5, 1)
    SetScenarioFlags(0xC5, 2)
    SetScenarioFlags(0xC5, 3)
    SetScenarioFlags(0xC6, 5)
    SetScenarioFlags(0xC5, 4)
    SetScenarioFlags(0xC5, 5)
    SetScenarioFlags(0xC5, 6)
    SetScenarioFlags(0xC5, 7)
    SetScenarioFlags(0xC6, 0)
    SetScenarioFlags(0xC6, 1)
    SetScenarioFlags(0xC6, 2)
    SetScenarioFlags(0xC6, 6)
    SetScenarioFlags(0xC6, 7)

    label("loc_7877")

    SetScenarioFlags(0xC3, 7)
    SetScenarioFlags(0xC8, 0)
    SetScenarioFlags(0xC8, 1)
    SetScenarioFlags(0xC8, 2)
    SetScenarioFlags(0xC8, 4)

    label("loc_7886")

    SetScenarioFlags(0xC8, 3)

    label("loc_7889")

    SetScenarioFlags(0xC3, 6)

    label("loc_788C")

    SetScenarioFlags(0xC3, 1)
    SetScenarioFlags(0xC3, 2)
    SetScenarioFlags(0xC3, 3)
    SetScenarioFlags(0xC3, 4)
    SetScenarioFlags(0xC3, 5)

    label("loc_789B")

    SetScenarioFlags(0xC2, 3)
    SetScenarioFlags(0xC2, 4)
    SetScenarioFlags(0xC2, 5)
    SetScenarioFlags(0xC2, 6)
    SetScenarioFlags(0xC2, 7)
    SetScenarioFlags(0xC3, 0)

    label("loc_78AD")

    SetScenarioFlags(0xC1, 7)
    SetScenarioFlags(0xC2, 0)
    SetScenarioFlags(0xC2, 1)
    SetScenarioFlags(0xC2, 2)

    label("loc_78B9")

    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 5)
    SetScenarioFlags(0xC1, 6)

    label("loc_78CB")

    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)

    label("loc_78EC")

    SetScenarioFlags(0xC0, 0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7916")

    label("loc_7907")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7916")

    label("loc_7916")

    Jump("loc_7665")

    label("loc_791B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_49_7643 end

    def Function_50_7929(): pass

    label("Function_50_7929")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_794E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AB0")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼(21)Crossbell City at Dusk\x01",        # 0
            "★'Had Discussion With Dudley'\x01",      # 1
            "★'Found Abandoned Bus'\x01",             # 2
            "★'Took a Break'\x01",                    # 3
            "★'Contacted by CEO's Office'\x01",       # 4
            "Cancel\x01",                              # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (4, "loc_7A1B"),
        (3, "loc_7A2D"),
        (2, "loc_7A84"),
        (1, "loc_7A87"),
        (0, "loc_7A8A"),
        (SWITCH_DEFAULT, "loc_7A9C"),
    )


    label("loc_7A1B")

    SetScenarioFlags(0xE4, 0)
    SetScenarioFlags(0xE4, 1)
    SetScenarioFlags(0xE4, 2)
    SetScenarioFlags(0xE4, 3)
    SetScenarioFlags(0xE4, 4)
    SetScenarioFlags(0xE7, 5)

    label("loc_7A2D")

    SetScenarioFlags(0xE0, 3)
    SetScenarioFlags(0xE0, 4)
    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)
    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)
    SetScenarioFlags(0xE1, 1)
    SetScenarioFlags(0xE1, 2)
    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)
    SetScenarioFlags(0xE1, 5)
    SetScenarioFlags(0xE1, 6)
    SetScenarioFlags(0xE1, 7)
    SetScenarioFlags(0xE2, 0)
    SetScenarioFlags(0xE2, 1)
    SetScenarioFlags(0xE2, 2)
    SetScenarioFlags(0xE2, 3)
    SetScenarioFlags(0xE2, 4)
    SetScenarioFlags(0xE2, 5)
    SetScenarioFlags(0xE2, 6)
    SetScenarioFlags(0xE2, 7)
    SetScenarioFlags(0xE3, 0)
    SetScenarioFlags(0xE3, 1)
    SetScenarioFlags(0xE3, 2)
    SetScenarioFlags(0xE3, 3)
    SetScenarioFlags(0xE3, 4)
    SetScenarioFlags(0xE3, 5)
    SetScenarioFlags(0xE3, 6)
    SetScenarioFlags(0xE3, 7)

    label("loc_7A84")

    SetScenarioFlags(0xE0, 2)

    label("loc_7A87")

    SetScenarioFlags(0xE0, 1)

    label("loc_7A8A")

    SetScenarioFlags(0xE0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AAB")

    label("loc_7A9C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AAB")

    label("loc_7AAB")

    Jump("loc_794E")

    label("loc_7AB0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_50_7929 end

    def Function_51_7ABE(): pass

    label("Function_51_7ABE")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BBF")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "★Like: Elie\x01",       # 0
            "★Like: Tio\x01",        # 1
            "★Like: Randy\x01",      # 2
            "Cancel\x01",             # 3
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_7B2D"),
        (1, "loc_7B57"),
        (2, "loc_7B81"),
        (SWITCH_DEFAULT, "loc_7BAB"),
    )


    label("loc_7B2D")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x41), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7BBA")

    label("loc_7B57")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x41), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7BBA")

    label("loc_7B81")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x41), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7BBA")

    label("loc_7BAB")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7BBA")

    label("loc_7BBA")

    Jump("loc_7AC8")

    label("loc_7BBF")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_51_7ABE end

    def Function_52_7BCD(): pass

    label("Function_52_7BCD")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7BD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C9B")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "★Chose: Elie\x01",       # 0
            "★Chose: Tio\x01",        # 1
            "★Chose: Randy\x01",      # 2
            "Cancel\x01",              # 3
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_7C3F"),
        (1, "loc_7C57"),
        (2, "loc_7C6F"),
        (SWITCH_DEFAULT, "loc_7C87"),
    )


    label("loc_7C3F")

    SetScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 2)
    ClearScenarioFlags(0xA9, 3)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C96")

    label("loc_7C57")

    SetScenarioFlags(0xA9, 2)
    ClearScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 3)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C96")

    label("loc_7C6F")

    SetScenarioFlags(0xA9, 3)
    ClearScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 2)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C96")

    label("loc_7C87")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C96")

    label("loc_7C96")

    Jump("loc_7BD7")

    label("loc_7C9B")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_52_7BCD end

    def Function_53_7CA9(): pass

    label("Function_53_7CA9")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7CB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D77")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "★Chose: Elie\x01",       # 0
            "★Chose: Tio\x01",        # 1
            "★Chose: Randy\x01",      # 2
            "Cancel\x01",              # 3
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_7D1B"),
        (1, "loc_7D33"),
        (2, "loc_7D4B"),
        (SWITCH_DEFAULT, "loc_7D63"),
    )


    label("loc_7D1B")

    SetScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 5)
    ClearScenarioFlags(0xA9, 6)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D72")

    label("loc_7D33")

    SetScenarioFlags(0xA9, 5)
    ClearScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 6)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D72")

    label("loc_7D4B")

    SetScenarioFlags(0xA9, 6)
    ClearScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 5)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D72")

    label("loc_7D63")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D72")

    label("loc_7D72")

    Jump("loc_7CB3")

    label("loc_7D77")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_53_7CA9 end

    def Function_54_7D85(): pass

    label("Function_54_7D85")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7D8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBAD")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼Quests - Prologue, Ch. 1\x01",      # 0
            "▼Quests - Ch. 2\x01",                # 1
            "▼Quests - Ch. 3\x01",                # 2
            "▼Quests - Intermission\x01",         # 3
            "▼Quests - Ch. 4, Finale\x01",        # 4
            "▼Arranged Monster Fights\x01",       # 5
            "▼Check All Contents\x01",            # 6
            "Cancel\x01",                          # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7E82"),
        (1, "loc_7E8A"),
        (2, "loc_7E92"),
        (3, "loc_7E9A"),
        (4, "loc_7EA2"),
        (5, "loc_7EAA"),
        (6, "loc_8EA7"),
        (SWITCH_DEFAULT, "loc_BB99"),
    )


    label("loc_7E82")

    Call(2, 55)
    Jump("loc_BBA8")

    label("loc_7E8A")

    Call(2, 56)
    Jump("loc_BBA8")

    label("loc_7E92")

    Call(2, 57)
    Jump("loc_BBA8")

    label("loc_7E9A")

    Call(2, 58)
    Jump("loc_BBA8")

    label("loc_7EA2")

    Call(2, 59)
    Jump("loc_BBA8")

    label("loc_7EAA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7EB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E95")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "P  ① Megalo Bat x1 + Add\x01",        # 0
            "1  ② Fall Eagle x2\x01",              # 1
            "2  ③ Nepenthes G x3\x01",             # 2
            "2  ④ Savage Horn x2\x01",             # 3
            "3  ⑤ Megalo Queen x1 + Add\x01",      # 4
            "3  ⑥ Sepith Demon x2\x01",            # 5
            "3  ⑦ Cannibalya G x2\x01",            # 6
            "3  ⑧ Steel Drew x1 + Add\x01",        # 7
            "I  ⑨ Gord Chaba Nei x1\x01",          # 8
            "4  ⑩ Bijo x2\x01",                    # 9
            "4  ⑪ Quetzalcoatl x2\x01",            # 10
            "4  ⑫ Org Virage x2\x01",              # 11
            "4  ⑬ Dark Legend x2\x01",             # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8046"),
        (1, "loc_8170"),
        (2, "loc_82D1"),
        (3, "loc_83D2"),
        (4, "loc_8503"),
        (5, "loc_8607"),
        (6, "loc_8714"),
        (7, "loc_883C"),
        (8, "loc_8994"),
        (9, "loc_8A9B"),
        (10, "loc_8BAE"),
        (11, "loc_8CF7"),
        (12, "loc_8CF7"),
        (SWITCH_DEFAULT, "loc_8E81"),
    )


    label("loc_8046")

    OP_29(0x35, 0x3, 0x0)
    OP_29(0x35, 0x3, 0x1)
    OP_29(0x35, 0x3, 0x2)
    OP_29(0x35, 0x3, 0x10)
    OP_29(0x35, 0x3, 0x20)
    OP_29(0x35, 0x3, 0x40)
    OP_29(0x35, 0x2, 0x0)
    OP_29(0x35, 0x2, 0x1)
    OP_29(0x35, 0x2, 0x2)
    OP_29(0x35, 0x2, 0x3)
    OP_29(0x35, 0x2, 0x4)
    OP_29(0x35, 0x2, 0x5)
    OP_29(0x35, 0x2, 0x6)
    OP_29(0x35, 0x2, 0x7)
    OP_29(0x35, 0x2, 0x8)
    OP_29(0x35, 0x2, 0x9)
    OP_29(0x35, 0x2, 0xA)
    OP_29(0x35, 0x2, 0xB)
    OP_29(0x35, 0x2, 0xC)
    OP_29(0x35, 0x2, 0xD)
    OP_29(0x35, 0x2, 0xE)
    OP_29(0x35, 0x2, 0xF)
    OP_29(0x35, 0x2, 0x10)
    OP_29(0x35, 0x2, 0x11)
    OP_29(0x35, 0x2, 0x12)
    OP_29(0x35, 0x2, 0x13)
    OP_29(0x35, 0x2, 0x14)
    OP_29(0x35, 0x2, 0x15)
    OP_29(0x35, 0x2, 0x16)
    OP_29(0x35, 0x2, 0x17)
    OP_29(0x35, 0x2, 0x18)
    OP_29(0x35, 0x2, 0x19)
    OP_29(0x35, 0x2, 0x1A)
    OP_29(0x35, 0x2, 0x1B)
    OP_29(0x35, 0x2, 0x1C)
    OP_29(0x35, 0x2, 0x1D)
    OP_29(0x35, 0x2, 0x1E)
    OP_29(0x35, 0x2, 0x1F)
    Call(2, 4)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x41, 6)
    SetScenarioFlags(0x41, 5)
    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)
    SetScenarioFlags(0x41, 4)
    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 7)
    SetScenarioFlags(0x41, 0)
    SetScenarioFlags(0x41, 1)
    SetScenarioFlags(0x40, 0)
    SetScenarioFlags(0x40, 1)
    OP_29(0x35, 0x4, 0x2)
    NewScene("m0002", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_8170")

    OP_29(0xB, 0x3, 0x0)
    OP_29(0xB, 0x3, 0x1)
    OP_29(0xB, 0x3, 0x2)
    OP_29(0xB, 0x3, 0x10)
    OP_29(0xB, 0x3, 0x20)
    OP_29(0xB, 0x3, 0x40)
    OP_29(0xB, 0x2, 0x0)
    OP_29(0xB, 0x2, 0x1)
    OP_29(0xB, 0x2, 0x2)
    OP_29(0xB, 0x2, 0x3)
    OP_29(0xB, 0x2, 0x4)
    OP_29(0xB, 0x2, 0x5)
    OP_29(0xB, 0x2, 0x6)
    OP_29(0xB, 0x2, 0x7)
    OP_29(0xB, 0x2, 0x8)
    OP_29(0xB, 0x2, 0x9)
    OP_29(0xB, 0x2, 0xA)
    OP_29(0xB, 0x2, 0xB)
    OP_29(0xB, 0x2, 0xC)
    OP_29(0xB, 0x2, 0xD)
    OP_29(0xB, 0x2, 0xE)
    OP_29(0xB, 0x2, 0xF)
    OP_29(0xB, 0x2, 0x10)
    OP_29(0xB, 0x2, 0x11)
    OP_29(0xB, 0x2, 0x12)
    OP_29(0xB, 0x2, 0x13)
    OP_29(0xB, 0x2, 0x14)
    OP_29(0xB, 0x2, 0x15)
    OP_29(0xB, 0x2, 0x16)
    OP_29(0xB, 0x2, 0x17)
    OP_29(0xB, 0x2, 0x18)
    OP_29(0xB, 0x2, 0x19)
    OP_29(0xB, 0x2, 0x1A)
    OP_29(0xB, 0x2, 0x1B)
    OP_29(0xB, 0x2, 0x1C)
    OP_29(0xB, 0x2, 0x1D)
    OP_29(0xB, 0x2, 0x1E)
    OP_29(0xB, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x64, 0)
    SetScenarioFlags(0x64, 1)
    SetScenarioFlags(0x63, 2)
    SetScenarioFlags(0x63, 3)
    SetScenarioFlags(0x63, 4)
    SetScenarioFlags(0x63, 5)
    SetScenarioFlags(0x63, 6)
    SetScenarioFlags(0x63, 7)
    SetScenarioFlags(0x62, 2)
    SetScenarioFlags(0x62, 3)
    SetScenarioFlags(0x62, 4)
    SetScenarioFlags(0x62, 5)
    SetScenarioFlags(0x62, 6)
    SetScenarioFlags(0x62, 7)
    SetScenarioFlags(0x63, 0)
    SetScenarioFlags(0x63, 1)
    SetScenarioFlags(0x62, 1)
    SetScenarioFlags(0x61, 3)
    SetScenarioFlags(0x61, 4)
    SetScenarioFlags(0x61, 5)
    SetScenarioFlags(0x61, 6)
    SetScenarioFlags(0x61, 7)
    SetScenarioFlags(0x62, 0)
    SetScenarioFlags(0x61, 2)
    SetScenarioFlags(0x61, 1)
    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x61, 0)
    SetScenarioFlags(0x60, 1)
    SetScenarioFlags(0x60, 2)
    SetScenarioFlags(0x60, 3)
    SetScenarioFlags(0x60, 4)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)
    SetScenarioFlags(0x60, 0)
    NewScene("r2040", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_82D1")

    OP_29(0x10, 0x3, 0x0)
    OP_29(0x10, 0x3, 0x1)
    OP_29(0x10, 0x3, 0x2)
    OP_29(0x10, 0x3, 0x10)
    OP_29(0x10, 0x3, 0x20)
    OP_29(0x10, 0x3, 0x40)
    OP_29(0x10, 0x2, 0x0)
    OP_29(0x10, 0x2, 0x1)
    OP_29(0x10, 0x2, 0x2)
    OP_29(0x10, 0x2, 0x3)
    OP_29(0x10, 0x2, 0x4)
    OP_29(0x10, 0x2, 0x5)
    OP_29(0x10, 0x2, 0x6)
    OP_29(0x10, 0x2, 0x7)
    OP_29(0x10, 0x2, 0x8)
    OP_29(0x10, 0x2, 0x9)
    OP_29(0x10, 0x2, 0xA)
    OP_29(0x10, 0x2, 0xB)
    OP_29(0x10, 0x2, 0xC)
    OP_29(0x10, 0x2, 0xD)
    OP_29(0x10, 0x2, 0xE)
    OP_29(0x10, 0x2, 0xF)
    OP_29(0x10, 0x2, 0x10)
    OP_29(0x10, 0x2, 0x11)
    OP_29(0x10, 0x2, 0x12)
    OP_29(0x10, 0x2, 0x13)
    OP_29(0x10, 0x2, 0x14)
    OP_29(0x10, 0x2, 0x15)
    OP_29(0x10, 0x2, 0x16)
    OP_29(0x10, 0x2, 0x17)
    OP_29(0x10, 0x2, 0x18)
    OP_29(0x10, 0x2, 0x19)
    OP_29(0x10, 0x2, 0x1A)
    OP_29(0x10, 0x2, 0x1B)
    OP_29(0x10, 0x2, 0x1C)
    OP_29(0x10, 0x2, 0x1D)
    OP_29(0x10, 0x2, 0x1E)
    OP_29(0x10, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x80, 0)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_83D2")

    OP_29(0x14, 0x3, 0x0)
    OP_29(0x14, 0x3, 0x1)
    OP_29(0x14, 0x3, 0x2)
    OP_29(0x14, 0x3, 0x10)
    OP_29(0x14, 0x3, 0x20)
    OP_29(0x14, 0x3, 0x40)
    OP_29(0x14, 0x2, 0x0)
    OP_29(0x14, 0x2, 0x1)
    OP_29(0x14, 0x2, 0x2)
    OP_29(0x14, 0x2, 0x3)
    OP_29(0x14, 0x2, 0x4)
    OP_29(0x14, 0x2, 0x5)
    OP_29(0x14, 0x2, 0x6)
    OP_29(0x14, 0x2, 0x7)
    OP_29(0x14, 0x2, 0x8)
    OP_29(0x14, 0x2, 0x9)
    OP_29(0x14, 0x2, 0xA)
    OP_29(0x14, 0x2, 0xB)
    OP_29(0x14, 0x2, 0xC)
    OP_29(0x14, 0x2, 0xD)
    OP_29(0x14, 0x2, 0xE)
    OP_29(0x14, 0x2, 0xF)
    OP_29(0x14, 0x2, 0x10)
    OP_29(0x14, 0x2, 0x11)
    OP_29(0x14, 0x2, 0x12)
    OP_29(0x14, 0x2, 0x13)
    OP_29(0x14, 0x2, 0x14)
    OP_29(0x14, 0x2, 0x15)
    OP_29(0x14, 0x2, 0x16)
    OP_29(0x14, 0x2, 0x17)
    OP_29(0x14, 0x2, 0x18)
    OP_29(0x14, 0x2, 0x19)
    OP_29(0x14, 0x2, 0x1A)
    OP_29(0x14, 0x2, 0x1B)
    OP_29(0x14, 0x2, 0x1C)
    OP_29(0x14, 0x2, 0x1D)
    OP_29(0x14, 0x2, 0x1E)
    OP_29(0x14, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x81, 7)
    SetScenarioFlags(0x82, 0)
    SetScenarioFlags(0x81, 6)
    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)
    SetScenarioFlags(0x81, 2)
    SetScenarioFlags(0x81, 3)
    SetScenarioFlags(0x81, 4)
    SetScenarioFlags(0x81, 5)
    SetScenarioFlags(0x80, 1)
    SetScenarioFlags(0x80, 2)
    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)
    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x80, 7)
    SetScenarioFlags(0x80, 0)
    NewScene("r0040", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_8503")

    OP_29(0x1A, 0x3, 0x0)
    OP_29(0x1A, 0x3, 0x1)
    OP_29(0x1A, 0x3, 0x2)
    OP_29(0x1A, 0x3, 0x10)
    OP_29(0x1A, 0x3, 0x20)
    OP_29(0x1A, 0x3, 0x40)
    OP_29(0x1A, 0x2, 0x0)
    OP_29(0x1A, 0x2, 0x1)
    OP_29(0x1A, 0x2, 0x2)
    OP_29(0x1A, 0x2, 0x3)
    OP_29(0x1A, 0x2, 0x4)
    OP_29(0x1A, 0x2, 0x5)
    OP_29(0x1A, 0x2, 0x6)
    OP_29(0x1A, 0x2, 0x7)
    OP_29(0x1A, 0x2, 0x8)
    OP_29(0x1A, 0x2, 0x9)
    OP_29(0x1A, 0x2, 0xA)
    OP_29(0x1A, 0x2, 0xB)
    OP_29(0x1A, 0x2, 0xC)
    OP_29(0x1A, 0x2, 0xD)
    OP_29(0x1A, 0x2, 0xE)
    OP_29(0x1A, 0x2, 0xF)
    OP_29(0x1A, 0x2, 0x10)
    OP_29(0x1A, 0x2, 0x11)
    OP_29(0x1A, 0x2, 0x12)
    OP_29(0x1A, 0x2, 0x13)
    OP_29(0x1A, 0x2, 0x14)
    OP_29(0x1A, 0x2, 0x15)
    OP_29(0x1A, 0x2, 0x16)
    OP_29(0x1A, 0x2, 0x17)
    OP_29(0x1A, 0x2, 0x18)
    OP_29(0x1A, 0x2, 0x19)
    OP_29(0x1A, 0x2, 0x1A)
    OP_29(0x1A, 0x2, 0x1B)
    OP_29(0x1A, 0x2, 0x1C)
    OP_29(0x1A, 0x2, 0x1D)
    OP_29(0x1A, 0x2, 0x1E)
    OP_29(0x1A, 0x2, 0x1F)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    SetScenarioFlags(0xA0, 0)
    NewScene("m0102", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_8607")

    OP_29(0x1E, 0x3, 0x0)
    OP_29(0x1E, 0x3, 0x1)
    OP_29(0x1E, 0x3, 0x2)
    OP_29(0x1E, 0x3, 0x10)
    OP_29(0x1E, 0x3, 0x20)
    OP_29(0x1E, 0x3, 0x40)
    OP_29(0x1E, 0x2, 0x0)
    OP_29(0x1E, 0x2, 0x1)
    OP_29(0x1E, 0x2, 0x2)
    OP_29(0x1E, 0x2, 0x3)
    OP_29(0x1E, 0x2, 0x4)
    OP_29(0x1E, 0x2, 0x5)
    OP_29(0x1E, 0x2, 0x6)
    OP_29(0x1E, 0x2, 0x7)
    OP_29(0x1E, 0x2, 0x8)
    OP_29(0x1E, 0x2, 0x9)
    OP_29(0x1E, 0x2, 0xA)
    OP_29(0x1E, 0x2, 0xB)
    OP_29(0x1E, 0x2, 0xC)
    OP_29(0x1E, 0x2, 0xD)
    OP_29(0x1E, 0x2, 0xE)
    OP_29(0x1E, 0x2, 0xF)
    OP_29(0x1E, 0x2, 0x10)
    OP_29(0x1E, 0x2, 0x11)
    OP_29(0x1E, 0x2, 0x12)
    OP_29(0x1E, 0x2, 0x13)
    OP_29(0x1E, 0x2, 0x14)
    OP_29(0x1E, 0x2, 0x15)
    OP_29(0x1E, 0x2, 0x16)
    OP_29(0x1E, 0x2, 0x17)
    OP_29(0x1E, 0x2, 0x18)
    OP_29(0x1E, 0x2, 0x19)
    OP_29(0x1E, 0x2, 0x1A)
    OP_29(0x1E, 0x2, 0x1B)
    OP_29(0x1E, 0x2, 0x1C)
    OP_29(0x1E, 0x2, 0x1D)
    OP_29(0x1E, 0x2, 0x1E)
    OP_29(0x1E, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 0)
    NewScene("r0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_8714")

    OP_29(0x21, 0x3, 0x0)
    OP_29(0x21, 0x3, 0x1)
    OP_29(0x21, 0x3, 0x2)
    OP_29(0x21, 0x3, 0x10)
    OP_29(0x21, 0x3, 0x20)
    OP_29(0x21, 0x3, 0x40)
    OP_29(0x21, 0x2, 0x0)
    OP_29(0x21, 0x2, 0x1)
    OP_29(0x21, 0x2, 0x2)
    OP_29(0x21, 0x2, 0x3)
    OP_29(0x21, 0x2, 0x4)
    OP_29(0x21, 0x2, 0x5)
    OP_29(0x21, 0x2, 0x6)
    OP_29(0x21, 0x2, 0x7)
    OP_29(0x21, 0x2, 0x8)
    OP_29(0x21, 0x2, 0x9)
    OP_29(0x21, 0x2, 0xA)
    OP_29(0x21, 0x2, 0xB)
    OP_29(0x21, 0x2, 0xC)
    OP_29(0x21, 0x2, 0xD)
    OP_29(0x21, 0x2, 0xE)
    OP_29(0x21, 0x2, 0xF)
    OP_29(0x21, 0x2, 0x10)
    OP_29(0x21, 0x2, 0x11)
    OP_29(0x21, 0x2, 0x12)
    OP_29(0x21, 0x2, 0x13)
    OP_29(0x21, 0x2, 0x14)
    OP_29(0x21, 0x2, 0x15)
    OP_29(0x21, 0x2, 0x16)
    OP_29(0x21, 0x2, 0x17)
    OP_29(0x21, 0x2, 0x18)
    OP_29(0x21, 0x2, 0x19)
    OP_29(0x21, 0x2, 0x1A)
    OP_29(0x21, 0x2, 0x1B)
    OP_29(0x21, 0x2, 0x1C)
    OP_29(0x21, 0x2, 0x1D)
    OP_29(0x21, 0x2, 0x1E)
    OP_29(0x21, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 0)
    NewScene("r0020", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_883C")

    OP_29(0x23, 0x3, 0x0)
    OP_29(0x23, 0x3, 0x1)
    OP_29(0x23, 0x3, 0x2)
    OP_29(0x23, 0x3, 0x10)
    OP_29(0x23, 0x3, 0x20)
    OP_29(0x23, 0x3, 0x40)
    OP_29(0x23, 0x2, 0x0)
    OP_29(0x23, 0x2, 0x1)
    OP_29(0x23, 0x2, 0x2)
    OP_29(0x23, 0x2, 0x3)
    OP_29(0x23, 0x2, 0x4)
    OP_29(0x23, 0x2, 0x5)
    OP_29(0x23, 0x2, 0x6)
    OP_29(0x23, 0x2, 0x7)
    OP_29(0x23, 0x2, 0x8)
    OP_29(0x23, 0x2, 0x9)
    OP_29(0x23, 0x2, 0xA)
    OP_29(0x23, 0x2, 0xB)
    OP_29(0x23, 0x2, 0xC)
    OP_29(0x23, 0x2, 0xD)
    OP_29(0x23, 0x2, 0xE)
    OP_29(0x23, 0x2, 0xF)
    OP_29(0x23, 0x2, 0x10)
    OP_29(0x23, 0x2, 0x11)
    OP_29(0x23, 0x2, 0x12)
    OP_29(0x23, 0x2, 0x13)
    OP_29(0x23, 0x2, 0x14)
    OP_29(0x23, 0x2, 0x15)
    OP_29(0x23, 0x2, 0x16)
    OP_29(0x23, 0x2, 0x17)
    OP_29(0x23, 0x2, 0x18)
    OP_29(0x23, 0x2, 0x19)
    OP_29(0x23, 0x2, 0x1A)
    OP_29(0x23, 0x2, 0x1B)
    OP_29(0x23, 0x2, 0x1C)
    OP_29(0x23, 0x2, 0x1D)
    OP_29(0x23, 0x2, 0x1E)
    OP_29(0x23, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xAA, 2)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xA2, 4)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xA2, 7)
    SetScenarioFlags(0xA3, 0)
    SetScenarioFlags(0xA3, 1)
    SetScenarioFlags(0xA3, 2)
    SetScenarioFlags(0xA3, 3)
    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_8994")

    OP_29(0x25, 0x3, 0x0)
    OP_29(0x25, 0x3, 0x1)
    OP_29(0x25, 0x3, 0x2)
    OP_29(0x25, 0x3, 0x10)
    OP_29(0x25, 0x3, 0x20)
    OP_29(0x25, 0x3, 0x40)
    OP_29(0x25, 0x2, 0x0)
    OP_29(0x25, 0x2, 0x1)
    OP_29(0x25, 0x2, 0x2)
    OP_29(0x25, 0x2, 0x3)
    OP_29(0x25, 0x2, 0x4)
    OP_29(0x25, 0x2, 0x5)
    OP_29(0x25, 0x2, 0x6)
    OP_29(0x25, 0x2, 0x7)
    OP_29(0x25, 0x2, 0x8)
    OP_29(0x25, 0x2, 0x9)
    OP_29(0x25, 0x2, 0xA)
    OP_29(0x25, 0x2, 0xB)
    OP_29(0x25, 0x2, 0xC)
    OP_29(0x25, 0x2, 0xD)
    OP_29(0x25, 0x2, 0xE)
    OP_29(0x25, 0x2, 0xF)
    OP_29(0x25, 0x2, 0x10)
    OP_29(0x25, 0x2, 0x11)
    OP_29(0x25, 0x2, 0x12)
    OP_29(0x25, 0x2, 0x13)
    OP_29(0x25, 0x2, 0x14)
    OP_29(0x25, 0x2, 0x15)
    OP_29(0x25, 0x2, 0x16)
    OP_29(0x25, 0x2, 0x17)
    OP_29(0x25, 0x2, 0x18)
    OP_29(0x25, 0x2, 0x19)
    OP_29(0x25, 0x2, 0x1A)
    OP_29(0x25, 0x2, 0x1B)
    OP_29(0x25, 0x2, 0x1C)
    OP_29(0x25, 0x2, 0x1D)
    OP_29(0x25, 0x2, 0x1E)
    OP_29(0x25, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA7, 6)
    NewScene("m0013", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_8A9B")

    OP_29(0x2B, 0x3, 0x0)
    OP_29(0x2B, 0x3, 0x1)
    OP_29(0x2B, 0x3, 0x2)
    OP_29(0x2B, 0x3, 0x10)
    OP_29(0x2B, 0x3, 0x20)
    OP_29(0x2B, 0x3, 0x40)
    OP_29(0x2B, 0x2, 0x0)
    OP_29(0x2B, 0x2, 0x1)
    OP_29(0x2B, 0x2, 0x2)
    OP_29(0x2B, 0x2, 0x3)
    OP_29(0x2B, 0x2, 0x4)
    OP_29(0x2B, 0x2, 0x5)
    OP_29(0x2B, 0x2, 0x6)
    OP_29(0x2B, 0x2, 0x7)
    OP_29(0x2B, 0x2, 0x8)
    OP_29(0x2B, 0x2, 0x9)
    OP_29(0x2B, 0x2, 0xA)
    OP_29(0x2B, 0x2, 0xB)
    OP_29(0x2B, 0x2, 0xC)
    OP_29(0x2B, 0x2, 0xD)
    OP_29(0x2B, 0x2, 0xE)
    OP_29(0x2B, 0x2, 0xF)
    OP_29(0x2B, 0x2, 0x10)
    OP_29(0x2B, 0x2, 0x11)
    OP_29(0x2B, 0x2, 0x12)
    OP_29(0x2B, 0x2, 0x13)
    OP_29(0x2B, 0x2, 0x14)
    OP_29(0x2B, 0x2, 0x15)
    OP_29(0x2B, 0x2, 0x16)
    OP_29(0x2B, 0x2, 0x17)
    OP_29(0x2B, 0x2, 0x18)
    OP_29(0x2B, 0x2, 0x19)
    OP_29(0x2B, 0x2, 0x1A)
    OP_29(0x2B, 0x2, 0x1B)
    OP_29(0x2B, 0x2, 0x1C)
    OP_29(0x2B, 0x2, 0x1D)
    OP_29(0x2B, 0x2, 0x1E)
    OP_29(0x2B, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC0, 0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_8BAE")

    OP_29(0x2F, 0x3, 0x0)
    OP_29(0x2F, 0x3, 0x1)
    OP_29(0x2F, 0x3, 0x2)
    OP_29(0x2F, 0x3, 0x10)
    OP_29(0x2F, 0x3, 0x20)
    OP_29(0x2F, 0x3, 0x40)
    OP_29(0x2F, 0x2, 0x0)
    OP_29(0x2F, 0x2, 0x1)
    OP_29(0x2F, 0x2, 0x2)
    OP_29(0x2F, 0x2, 0x3)
    OP_29(0x2F, 0x2, 0x4)
    OP_29(0x2F, 0x2, 0x5)
    OP_29(0x2F, 0x2, 0x6)
    OP_29(0x2F, 0x2, 0x7)
    OP_29(0x2F, 0x2, 0x8)
    OP_29(0x2F, 0x2, 0x9)
    OP_29(0x2F, 0x2, 0xA)
    OP_29(0x2F, 0x2, 0xB)
    OP_29(0x2F, 0x2, 0xC)
    OP_29(0x2F, 0x2, 0xD)
    OP_29(0x2F, 0x2, 0xE)
    OP_29(0x2F, 0x2, 0xF)
    OP_29(0x2F, 0x2, 0x10)
    OP_29(0x2F, 0x2, 0x11)
    OP_29(0x2F, 0x2, 0x12)
    OP_29(0x2F, 0x2, 0x13)
    OP_29(0x2F, 0x2, 0x14)
    OP_29(0x2F, 0x2, 0x15)
    OP_29(0x2F, 0x2, 0x16)
    OP_29(0x2F, 0x2, 0x17)
    OP_29(0x2F, 0x2, 0x18)
    OP_29(0x2F, 0x2, 0x19)
    OP_29(0x2F, 0x2, 0x1A)
    OP_29(0x2F, 0x2, 0x1B)
    OP_29(0x2F, 0x2, 0x1C)
    OP_29(0x2F, 0x2, 0x1D)
    OP_29(0x2F, 0x2, 0x1E)
    OP_29(0x2F, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 7)
    SetScenarioFlags(0xC2, 0)
    SetScenarioFlags(0xC2, 1)
    SetScenarioFlags(0xC2, 2)
    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 5)
    SetScenarioFlags(0xC1, 6)
    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)
    SetScenarioFlags(0xC0, 0)
    NewScene("r1020", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E90")

    label("loc_8CF7")

    OP_29(0x32, 0x3, 0x0)
    OP_29(0x32, 0x3, 0x1)
    OP_29(0x32, 0x3, 0x2)
    OP_29(0x32, 0x3, 0x10)
    OP_29(0x32, 0x3, 0x20)
    OP_29(0x32, 0x3, 0x40)
    OP_29(0x32, 0x2, 0x0)
    OP_29(0x32, 0x2, 0x1)
    OP_29(0x32, 0x2, 0x2)
    OP_29(0x32, 0x2, 0x3)
    OP_29(0x32, 0x2, 0x4)
    OP_29(0x32, 0x2, 0x5)
    OP_29(0x32, 0x2, 0x6)
    OP_29(0x32, 0x2, 0x7)
    OP_29(0x32, 0x2, 0x8)
    OP_29(0x32, 0x2, 0x9)
    OP_29(0x32, 0x2, 0xA)
    OP_29(0x32, 0x2, 0xB)
    OP_29(0x32, 0x2, 0xC)
    OP_29(0x32, 0x2, 0xD)
    OP_29(0x32, 0x2, 0xE)
    OP_29(0x32, 0x2, 0xF)
    OP_29(0x32, 0x2, 0x10)
    OP_29(0x32, 0x2, 0x11)
    OP_29(0x32, 0x2, 0x12)
    OP_29(0x32, 0x2, 0x13)
    OP_29(0x32, 0x2, 0x14)
    OP_29(0x32, 0x2, 0x15)
    OP_29(0x32, 0x2, 0x16)
    OP_29(0x32, 0x2, 0x17)
    OP_29(0x32, 0x2, 0x18)
    OP_29(0x32, 0x2, 0x19)
    OP_29(0x32, 0x2, 0x1A)
    OP_29(0x32, 0x2, 0x1B)
    OP_29(0x32, 0x2, 0x1C)
    OP_29(0x32, 0x2, 0x1D)
    OP_29(0x32, 0x2, 0x1E)
    OP_29(0x32, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC3, 6)
    SetScenarioFlags(0xC3, 1)
    SetScenarioFlags(0xC3, 2)
    SetScenarioFlags(0xC3, 3)
    SetScenarioFlags(0xC3, 4)
    SetScenarioFlags(0xC3, 5)
    SetScenarioFlags(0xC2, 3)
    SetScenarioFlags(0xC2, 4)
    SetScenarioFlags(0xC2, 5)
    SetScenarioFlags(0xC2, 6)
    SetScenarioFlags(0xC2, 7)
    SetScenarioFlags(0xC3, 0)
    SetScenarioFlags(0xC1, 7)
    SetScenarioFlags(0xC2, 0)
    SetScenarioFlags(0xC2, 1)
    SetScenarioFlags(0xC2, 2)
    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 5)
    SetScenarioFlags(0xC1, 6)
    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)
    SetScenarioFlags(0xC0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E73")
    NewScene("m1090", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E7C")

    label("loc_8E73")

    NewScene("r3080", 0, 0, 0)
    IdleLoop()

    label("loc_8E7C")

    Jump("loc_8E90")

    label("loc_8E81")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E90")

    label("loc_8E90")

    Jump("loc_7EB4")

    label("loc_8E95")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Jump("loc_BBA8")

    label("loc_8EA7")

    OP_29(0x1, 0x4, 0x0)
    OP_29(0x1, 0x4, 0x1)
    OP_29(0x1, 0x4, 0x2)
    OP_29(0x1, 0x4, 0x10)
    OP_29(0x1, 0x4, 0x20)
    OP_29(0x2, 0x4, 0x0)
    OP_29(0x2, 0x4, 0x1)
    OP_29(0x2, 0x4, 0x2)
    OP_29(0x2, 0x4, 0x10)
    OP_29(0x2, 0x4, 0x20)
    OP_29(0x3, 0x4, 0x0)
    OP_29(0x3, 0x4, 0x1)
    OP_29(0x3, 0x4, 0x2)
    OP_29(0x3, 0x4, 0x10)
    OP_29(0x3, 0x4, 0x20)
    OP_29(0x4, 0x4, 0x0)
    OP_29(0x4, 0x4, 0x1)
    OP_29(0x4, 0x4, 0x2)
    OP_29(0x4, 0x4, 0x10)
    OP_29(0x4, 0x4, 0x20)
    OP_29(0x35, 0x4, 0x0)
    OP_29(0x35, 0x4, 0x1)
    OP_29(0x35, 0x4, 0x2)
    OP_29(0x35, 0x4, 0x10)
    OP_29(0x35, 0x4, 0x20)
    OP_29(0x5, 0x4, 0x0)
    OP_29(0x5, 0x4, 0x1)
    OP_29(0x5, 0x4, 0x2)
    OP_29(0x5, 0x4, 0x10)
    OP_29(0x5, 0x4, 0x20)
    OP_29(0x6, 0x4, 0x0)
    OP_29(0x6, 0x4, 0x1)
    OP_29(0x6, 0x4, 0x2)
    OP_29(0x6, 0x4, 0x10)
    OP_29(0x6, 0x4, 0x20)
    OP_29(0x7, 0x4, 0x0)
    OP_29(0x7, 0x4, 0x1)
    OP_29(0x7, 0x4, 0x2)
    OP_29(0x7, 0x4, 0x10)
    OP_29(0x7, 0x4, 0x20)
    OP_29(0x8, 0x4, 0x0)
    OP_29(0x8, 0x4, 0x1)
    OP_29(0x8, 0x4, 0x2)
    OP_29(0x8, 0x4, 0x10)
    OP_29(0x8, 0x4, 0x20)
    OP_29(0x9, 0x4, 0x0)
    OP_29(0x9, 0x4, 0x1)
    OP_29(0x9, 0x4, 0x2)
    OP_29(0x9, 0x4, 0x10)
    OP_29(0x9, 0x4, 0x20)
    OP_29(0xA, 0x4, 0x0)
    OP_29(0xA, 0x4, 0x1)
    OP_29(0xA, 0x4, 0x2)
    OP_29(0xA, 0x4, 0x10)
    OP_29(0xA, 0x4, 0x20)
    OP_29(0xB, 0x4, 0x0)
    OP_29(0xB, 0x4, 0x1)
    OP_29(0xB, 0x4, 0x2)
    OP_29(0xB, 0x4, 0x10)
    OP_29(0xB, 0x4, 0x20)
    OP_29(0xC, 0x4, 0x0)
    OP_29(0xC, 0x4, 0x1)
    OP_29(0xC, 0x4, 0x2)
    OP_29(0xC, 0x4, 0x10)
    OP_29(0xC, 0x4, 0x20)
    OP_29(0xD, 0x4, 0x0)
    OP_29(0xD, 0x4, 0x1)
    OP_29(0xD, 0x4, 0x2)
    OP_29(0xD, 0x4, 0x10)
    OP_29(0xD, 0x4, 0x20)
    OP_29(0xE, 0x4, 0x0)
    OP_29(0xE, 0x4, 0x1)
    OP_29(0xE, 0x4, 0x2)
    OP_29(0xE, 0x4, 0x10)
    OP_29(0xE, 0x4, 0x20)
    OP_29(0xF, 0x4, 0x0)
    OP_29(0xF, 0x4, 0x1)
    OP_29(0xF, 0x4, 0x2)
    OP_29(0xF, 0x4, 0x10)
    OP_29(0xF, 0x4, 0x20)
    OP_29(0x10, 0x4, 0x0)
    OP_29(0x10, 0x4, 0x1)
    OP_29(0x10, 0x4, 0x2)
    OP_29(0x10, 0x4, 0x10)
    OP_29(0x10, 0x4, 0x20)
    OP_29(0x11, 0x4, 0x0)
    OP_29(0x11, 0x4, 0x1)
    OP_29(0x11, 0x4, 0x2)
    OP_29(0x11, 0x4, 0x10)
    OP_29(0x11, 0x4, 0x20)
    OP_29(0x12, 0x4, 0x0)
    OP_29(0x12, 0x4, 0x1)
    OP_29(0x12, 0x4, 0x2)
    OP_29(0x12, 0x4, 0x10)
    OP_29(0x12, 0x4, 0x20)
    OP_29(0x13, 0x4, 0x0)
    OP_29(0x13, 0x4, 0x1)
    OP_29(0x13, 0x4, 0x2)
    OP_29(0x13, 0x4, 0x10)
    OP_29(0x13, 0x4, 0x20)
    OP_29(0x14, 0x4, 0x0)
    OP_29(0x14, 0x4, 0x1)
    OP_29(0x14, 0x4, 0x2)
    OP_29(0x14, 0x4, 0x10)
    OP_29(0x14, 0x4, 0x20)
    OP_29(0x15, 0x4, 0x0)
    OP_29(0x15, 0x4, 0x1)
    OP_29(0x15, 0x4, 0x2)
    OP_29(0x15, 0x4, 0x10)
    OP_29(0x15, 0x4, 0x20)
    OP_29(0x16, 0x4, 0x0)
    OP_29(0x16, 0x4, 0x1)
    OP_29(0x16, 0x4, 0x2)
    OP_29(0x16, 0x4, 0x10)
    OP_29(0x16, 0x4, 0x20)
    OP_29(0x17, 0x4, 0x0)
    OP_29(0x17, 0x4, 0x1)
    OP_29(0x17, 0x4, 0x2)
    OP_29(0x17, 0x4, 0x10)
    OP_29(0x17, 0x4, 0x20)
    OP_29(0x18, 0x4, 0x0)
    OP_29(0x18, 0x4, 0x1)
    OP_29(0x18, 0x4, 0x2)
    OP_29(0x18, 0x4, 0x10)
    OP_29(0x18, 0x4, 0x20)
    OP_29(0x19, 0x4, 0x0)
    OP_29(0x19, 0x4, 0x1)
    OP_29(0x19, 0x4, 0x2)
    OP_29(0x19, 0x4, 0x10)
    OP_29(0x19, 0x4, 0x20)
    OP_29(0x1A, 0x4, 0x0)
    OP_29(0x1A, 0x4, 0x1)
    OP_29(0x1A, 0x4, 0x2)
    OP_29(0x1A, 0x4, 0x10)
    OP_29(0x1A, 0x4, 0x20)
    OP_29(0x1B, 0x4, 0x0)
    OP_29(0x1B, 0x4, 0x1)
    OP_29(0x1B, 0x4, 0x2)
    OP_29(0x1B, 0x4, 0x10)
    OP_29(0x1B, 0x4, 0x20)
    OP_29(0x1C, 0x4, 0x0)
    OP_29(0x1C, 0x4, 0x1)
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x4, 0x10)
    OP_29(0x1C, 0x4, 0x20)
    OP_29(0x1D, 0x4, 0x0)
    OP_29(0x1D, 0x4, 0x1)
    OP_29(0x1D, 0x4, 0x2)
    OP_29(0x1D, 0x4, 0x10)
    OP_29(0x1D, 0x4, 0x20)
    OP_29(0x1E, 0x4, 0x0)
    OP_29(0x1E, 0x4, 0x1)
    OP_29(0x1E, 0x4, 0x2)
    OP_29(0x1E, 0x4, 0x10)
    OP_29(0x1E, 0x4, 0x20)
    OP_29(0x1F, 0x4, 0x0)
    OP_29(0x1F, 0x4, 0x1)
    OP_29(0x1F, 0x4, 0x2)
    OP_29(0x1F, 0x4, 0x10)
    OP_29(0x1F, 0x4, 0x20)
    OP_29(0x20, 0x4, 0x0)
    OP_29(0x20, 0x4, 0x1)
    OP_29(0x20, 0x4, 0x2)
    OP_29(0x20, 0x4, 0x10)
    OP_29(0x20, 0x4, 0x20)
    OP_29(0x21, 0x4, 0x0)
    OP_29(0x21, 0x4, 0x1)
    OP_29(0x21, 0x4, 0x2)
    OP_29(0x21, 0x4, 0x10)
    OP_29(0x21, 0x4, 0x20)
    OP_29(0x22, 0x4, 0x0)
    OP_29(0x22, 0x4, 0x1)
    OP_29(0x22, 0x4, 0x2)
    OP_29(0x22, 0x4, 0x10)
    OP_29(0x22, 0x4, 0x20)
    OP_29(0x23, 0x4, 0x0)
    OP_29(0x23, 0x4, 0x1)
    OP_29(0x23, 0x4, 0x2)
    OP_29(0x23, 0x4, 0x10)
    OP_29(0x23, 0x4, 0x20)
    OP_29(0x24, 0x4, 0x0)
    OP_29(0x24, 0x4, 0x1)
    OP_29(0x24, 0x4, 0x2)
    OP_29(0x24, 0x4, 0x10)
    OP_29(0x24, 0x4, 0x20)
    OP_29(0x25, 0x4, 0x0)
    OP_29(0x25, 0x4, 0x1)
    OP_29(0x25, 0x4, 0x2)
    OP_29(0x25, 0x4, 0x10)
    OP_29(0x25, 0x4, 0x20)
    OP_29(0x26, 0x4, 0x0)
    OP_29(0x26, 0x4, 0x1)
    OP_29(0x26, 0x4, 0x2)
    OP_29(0x26, 0x4, 0x10)
    OP_29(0x26, 0x4, 0x20)
    OP_29(0x27, 0x4, 0x0)
    OP_29(0x27, 0x4, 0x1)
    OP_29(0x27, 0x4, 0x2)
    OP_29(0x27, 0x4, 0x10)
    OP_29(0x27, 0x4, 0x20)
    OP_29(0x28, 0x4, 0x0)
    OP_29(0x28, 0x4, 0x1)
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x4, 0x10)
    OP_29(0x28, 0x4, 0x20)
    OP_29(0x29, 0x4, 0x0)
    OP_29(0x29, 0x4, 0x1)
    OP_29(0x29, 0x4, 0x2)
    OP_29(0x29, 0x4, 0x10)
    OP_29(0x29, 0x4, 0x20)
    OP_29(0x2A, 0x4, 0x0)
    OP_29(0x2A, 0x4, 0x1)
    OP_29(0x2A, 0x4, 0x2)
    OP_29(0x2A, 0x4, 0x10)
    OP_29(0x2A, 0x4, 0x20)
    OP_29(0x2B, 0x4, 0x0)
    OP_29(0x2B, 0x4, 0x1)
    OP_29(0x2B, 0x4, 0x2)
    OP_29(0x2B, 0x4, 0x10)
    OP_29(0x2B, 0x4, 0x20)
    OP_29(0x2C, 0x4, 0x0)
    OP_29(0x2C, 0x4, 0x1)
    OP_29(0x2C, 0x4, 0x2)
    OP_29(0x2C, 0x4, 0x10)
    OP_29(0x2C, 0x4, 0x20)
    OP_29(0x2D, 0x4, 0x0)
    OP_29(0x2D, 0x4, 0x1)
    OP_29(0x2D, 0x4, 0x2)
    OP_29(0x2D, 0x4, 0x10)
    OP_29(0x2D, 0x4, 0x20)
    OP_29(0x2E, 0x4, 0x0)
    OP_29(0x2E, 0x4, 0x1)
    OP_29(0x2E, 0x4, 0x2)
    OP_29(0x2E, 0x4, 0x10)
    OP_29(0x2E, 0x4, 0x20)
    OP_29(0x2F, 0x4, 0x0)
    OP_29(0x2F, 0x4, 0x1)
    OP_29(0x2F, 0x4, 0x2)
    OP_29(0x2F, 0x4, 0x10)
    OP_29(0x2F, 0x4, 0x20)
    OP_29(0x30, 0x4, 0x0)
    OP_29(0x30, 0x4, 0x1)
    OP_29(0x30, 0x4, 0x2)
    OP_29(0x30, 0x4, 0x10)
    OP_29(0x30, 0x4, 0x20)
    OP_29(0x31, 0x4, 0x0)
    OP_29(0x31, 0x4, 0x1)
    OP_29(0x31, 0x4, 0x2)
    OP_29(0x31, 0x4, 0x10)
    OP_29(0x31, 0x4, 0x20)
    OP_29(0x32, 0x4, 0x0)
    OP_29(0x32, 0x4, 0x1)
    OP_29(0x32, 0x4, 0x2)
    OP_29(0x32, 0x4, 0x10)
    OP_29(0x32, 0x4, 0x20)
    OP_29(0x33, 0x4, 0x0)
    OP_29(0x33, 0x4, 0x1)
    OP_29(0x33, 0x4, 0x2)
    OP_29(0x33, 0x4, 0x10)
    OP_29(0x33, 0x4, 0x20)
    OP_29(0x34, 0x4, 0x0)
    OP_29(0x34, 0x4, 0x1)
    OP_29(0x34, 0x4, 0x2)
    OP_29(0x34, 0x4, 0x10)
    OP_29(0x34, 0x4, 0x20)
    OP_29(0x1, 0x1, 0x0)
    OP_29(0x1, 0x1, 0x1)
    OP_29(0x1, 0x1, 0x2)
    OP_29(0x1, 0x1, 0x3)
    OP_29(0x1, 0x1, 0x4)
    OP_29(0x1, 0x1, 0x5)
    OP_29(0x1, 0x1, 0x6)
    OP_29(0x1, 0x1, 0x7)
    OP_29(0x1, 0x1, 0x8)
    OP_29(0x1, 0x1, 0x9)
    OP_29(0x1, 0x1, 0xA)
    OP_29(0x1, 0x1, 0xB)
    OP_29(0x1, 0x1, 0xC)
    OP_29(0x1, 0x1, 0xD)
    OP_29(0x1, 0x1, 0xE)
    OP_29(0x1, 0x1, 0xF)
    OP_29(0x1, 0x1, 0x10)
    OP_29(0x1, 0x1, 0x11)
    OP_29(0x1, 0x1, 0x12)
    OP_29(0x1, 0x1, 0x13)
    OP_29(0x1, 0x1, 0x14)
    OP_29(0x1, 0x1, 0x15)
    OP_29(0x1, 0x1, 0x16)
    OP_29(0x1, 0x1, 0x17)
    OP_29(0x1, 0x1, 0x18)
    OP_29(0x1, 0x1, 0x19)
    OP_29(0x1, 0x1, 0x1A)
    OP_29(0x1, 0x1, 0x1B)
    OP_29(0x1, 0x1, 0x1C)
    OP_29(0x1, 0x1, 0x1D)
    OP_29(0x1, 0x1, 0x1E)
    OP_29(0x1, 0x1, 0x1F)
    OP_29(0x2, 0x1, 0x0)
    OP_29(0x2, 0x1, 0x1)
    OP_29(0x2, 0x1, 0x2)
    OP_29(0x2, 0x1, 0x3)
    OP_29(0x2, 0x1, 0x4)
    OP_29(0x2, 0x1, 0x5)
    OP_29(0x2, 0x1, 0x6)
    OP_29(0x2, 0x1, 0x7)
    OP_29(0x2, 0x1, 0x8)
    OP_29(0x2, 0x1, 0x9)
    OP_29(0x2, 0x1, 0xA)
    OP_29(0x2, 0x1, 0xB)
    OP_29(0x2, 0x1, 0xC)
    OP_29(0x2, 0x1, 0xD)
    OP_29(0x2, 0x1, 0xE)
    OP_29(0x2, 0x1, 0xF)
    OP_29(0x2, 0x1, 0x10)
    OP_29(0x2, 0x1, 0x11)
    OP_29(0x2, 0x1, 0x12)
    OP_29(0x2, 0x1, 0x13)
    OP_29(0x2, 0x1, 0x14)
    OP_29(0x2, 0x1, 0x15)
    OP_29(0x2, 0x1, 0x16)
    OP_29(0x2, 0x1, 0x17)
    OP_29(0x2, 0x1, 0x18)
    OP_29(0x2, 0x1, 0x19)
    OP_29(0x2, 0x1, 0x1A)
    OP_29(0x2, 0x1, 0x1B)
    OP_29(0x2, 0x1, 0x1C)
    OP_29(0x2, 0x1, 0x1D)
    OP_29(0x2, 0x1, 0x1E)
    OP_29(0x2, 0x1, 0x1F)
    OP_29(0x3, 0x1, 0x0)
    OP_29(0x3, 0x1, 0x1)
    OP_29(0x3, 0x1, 0x2)
    OP_29(0x3, 0x1, 0x3)
    OP_29(0x3, 0x1, 0x4)
    OP_29(0x3, 0x1, 0x5)
    OP_29(0x3, 0x1, 0x6)
    OP_29(0x3, 0x1, 0x7)
    OP_29(0x3, 0x1, 0x8)
    OP_29(0x3, 0x1, 0x9)
    OP_29(0x3, 0x1, 0xA)
    OP_29(0x3, 0x1, 0xB)
    OP_29(0x3, 0x1, 0xC)
    OP_29(0x3, 0x1, 0xD)
    OP_29(0x3, 0x1, 0xE)
    OP_29(0x3, 0x1, 0xF)
    OP_29(0x3, 0x1, 0x10)
    OP_29(0x3, 0x1, 0x11)
    OP_29(0x3, 0x1, 0x12)
    OP_29(0x3, 0x1, 0x13)
    OP_29(0x3, 0x1, 0x14)
    OP_29(0x3, 0x1, 0x15)
    OP_29(0x3, 0x1, 0x16)
    OP_29(0x3, 0x1, 0x17)
    OP_29(0x3, 0x1, 0x18)
    OP_29(0x3, 0x1, 0x19)
    OP_29(0x3, 0x1, 0x1A)
    OP_29(0x3, 0x1, 0x1B)
    OP_29(0x3, 0x1, 0x1C)
    OP_29(0x3, 0x1, 0x1D)
    OP_29(0x3, 0x1, 0x1E)
    OP_29(0x3, 0x1, 0x1F)
    OP_29(0x4, 0x1, 0x0)
    OP_29(0x4, 0x1, 0x1)
    OP_29(0x4, 0x1, 0x2)
    OP_29(0x4, 0x1, 0x3)
    OP_29(0x4, 0x1, 0x4)
    OP_29(0x4, 0x1, 0x5)
    OP_29(0x4, 0x1, 0x6)
    OP_29(0x4, 0x1, 0x7)
    OP_29(0x4, 0x1, 0x8)
    OP_29(0x4, 0x1, 0x9)
    OP_29(0x4, 0x1, 0xA)
    OP_29(0x4, 0x1, 0xB)
    OP_29(0x4, 0x1, 0xC)
    OP_29(0x4, 0x1, 0xD)
    OP_29(0x4, 0x1, 0xE)
    OP_29(0x4, 0x1, 0xF)
    OP_29(0x4, 0x1, 0x10)
    OP_29(0x4, 0x1, 0x11)
    OP_29(0x4, 0x1, 0x12)
    OP_29(0x4, 0x1, 0x13)
    OP_29(0x4, 0x1, 0x14)
    OP_29(0x4, 0x1, 0x15)
    OP_29(0x4, 0x1, 0x16)
    OP_29(0x4, 0x1, 0x17)
    OP_29(0x4, 0x1, 0x18)
    OP_29(0x4, 0x1, 0x19)
    OP_29(0x4, 0x1, 0x1A)
    OP_29(0x4, 0x1, 0x1B)
    OP_29(0x4, 0x1, 0x1C)
    OP_29(0x4, 0x1, 0x1D)
    OP_29(0x4, 0x1, 0x1E)
    OP_29(0x4, 0x1, 0x1F)
    OP_29(0x35, 0x1, 0x0)
    OP_29(0x35, 0x1, 0x1)
    OP_29(0x35, 0x1, 0x2)
    OP_29(0x35, 0x1, 0x3)
    OP_29(0x35, 0x1, 0x4)
    OP_29(0x35, 0x1, 0x5)
    OP_29(0x35, 0x1, 0x6)
    OP_29(0x35, 0x1, 0x7)
    OP_29(0x35, 0x1, 0x8)
    OP_29(0x35, 0x1, 0x9)
    OP_29(0x35, 0x1, 0xA)
    OP_29(0x35, 0x1, 0xB)
    OP_29(0x35, 0x1, 0xC)
    OP_29(0x35, 0x1, 0xD)
    OP_29(0x35, 0x1, 0xE)
    OP_29(0x35, 0x1, 0xF)
    OP_29(0x35, 0x1, 0x10)
    OP_29(0x35, 0x1, 0x11)
    OP_29(0x35, 0x1, 0x12)
    OP_29(0x35, 0x1, 0x13)
    OP_29(0x35, 0x1, 0x14)
    OP_29(0x35, 0x1, 0x15)
    OP_29(0x35, 0x1, 0x16)
    OP_29(0x35, 0x1, 0x17)
    OP_29(0x35, 0x1, 0x18)
    OP_29(0x35, 0x1, 0x19)
    OP_29(0x35, 0x1, 0x1A)
    OP_29(0x35, 0x1, 0x1B)
    OP_29(0x35, 0x1, 0x1C)
    OP_29(0x35, 0x1, 0x1D)
    OP_29(0x35, 0x1, 0x1E)
    OP_29(0x35, 0x1, 0x1F)
    OP_29(0x5, 0x1, 0x0)
    OP_29(0x5, 0x1, 0x1)
    OP_29(0x5, 0x1, 0x2)
    OP_29(0x5, 0x1, 0x3)
    OP_29(0x5, 0x1, 0x4)
    OP_29(0x5, 0x1, 0x5)
    OP_29(0x5, 0x1, 0x6)
    OP_29(0x5, 0x1, 0x7)
    OP_29(0x5, 0x1, 0x8)
    OP_29(0x5, 0x1, 0x9)
    OP_29(0x5, 0x1, 0xA)
    OP_29(0x5, 0x1, 0xB)
    OP_29(0x5, 0x1, 0xC)
    OP_29(0x5, 0x1, 0xD)
    OP_29(0x5, 0x1, 0xE)
    OP_29(0x5, 0x1, 0xF)
    OP_29(0x5, 0x1, 0x10)
    OP_29(0x5, 0x1, 0x11)
    OP_29(0x5, 0x1, 0x12)
    OP_29(0x5, 0x1, 0x13)
    OP_29(0x5, 0x1, 0x14)
    OP_29(0x5, 0x1, 0x15)
    OP_29(0x5, 0x1, 0x16)
    OP_29(0x5, 0x1, 0x17)
    OP_29(0x5, 0x1, 0x18)
    OP_29(0x5, 0x1, 0x19)
    OP_29(0x5, 0x1, 0x1A)
    OP_29(0x5, 0x1, 0x1B)
    OP_29(0x5, 0x1, 0x1C)
    OP_29(0x5, 0x1, 0x1D)
    OP_29(0x5, 0x1, 0x1E)
    OP_29(0x5, 0x1, 0x1F)
    OP_29(0x6, 0x1, 0x0)
    OP_29(0x6, 0x1, 0x1)
    OP_29(0x6, 0x1, 0x2)
    OP_29(0x6, 0x1, 0x3)
    OP_29(0x6, 0x1, 0x4)
    OP_29(0x6, 0x1, 0x5)
    OP_29(0x6, 0x1, 0x6)
    OP_29(0x6, 0x1, 0x7)
    OP_29(0x6, 0x1, 0x8)
    OP_29(0x6, 0x1, 0x9)
    OP_29(0x6, 0x1, 0xA)
    OP_29(0x6, 0x1, 0xB)
    OP_29(0x6, 0x1, 0xC)
    OP_29(0x6, 0x1, 0xD)
    OP_29(0x6, 0x1, 0xE)
    OP_29(0x6, 0x1, 0xF)
    OP_29(0x6, 0x1, 0x10)
    OP_29(0x6, 0x1, 0x11)
    OP_29(0x6, 0x1, 0x12)
    OP_29(0x6, 0x1, 0x13)
    OP_29(0x6, 0x1, 0x14)
    OP_29(0x6, 0x1, 0x15)
    OP_29(0x6, 0x1, 0x16)
    OP_29(0x6, 0x1, 0x17)
    OP_29(0x6, 0x1, 0x18)
    OP_29(0x6, 0x1, 0x19)
    OP_29(0x6, 0x1, 0x1A)
    OP_29(0x6, 0x1, 0x1B)
    OP_29(0x6, 0x1, 0x1C)
    OP_29(0x6, 0x1, 0x1D)
    OP_29(0x6, 0x1, 0x1E)
    OP_29(0x6, 0x1, 0x1F)
    OP_29(0x7, 0x1, 0x0)
    OP_29(0x7, 0x1, 0x1)
    OP_29(0x7, 0x1, 0x2)
    OP_29(0x7, 0x1, 0x3)
    OP_29(0x7, 0x1, 0x4)
    OP_29(0x7, 0x1, 0x5)
    OP_29(0x7, 0x1, 0x6)
    OP_29(0x7, 0x1, 0x7)
    OP_29(0x7, 0x1, 0x8)
    OP_29(0x7, 0x1, 0x9)
    OP_29(0x7, 0x1, 0xA)
    OP_29(0x7, 0x1, 0xB)
    OP_29(0x7, 0x1, 0xC)
    OP_29(0x7, 0x1, 0xD)
    OP_29(0x7, 0x1, 0xE)
    OP_29(0x7, 0x1, 0xF)
    OP_29(0x7, 0x1, 0x10)
    OP_29(0x7, 0x1, 0x11)
    OP_29(0x7, 0x1, 0x12)
    OP_29(0x7, 0x1, 0x13)
    OP_29(0x7, 0x1, 0x14)
    OP_29(0x7, 0x1, 0x15)
    OP_29(0x7, 0x1, 0x16)
    OP_29(0x7, 0x1, 0x17)
    OP_29(0x7, 0x1, 0x18)
    OP_29(0x7, 0x1, 0x19)
    OP_29(0x7, 0x1, 0x1A)
    OP_29(0x7, 0x1, 0x1B)
    OP_29(0x7, 0x1, 0x1C)
    OP_29(0x7, 0x1, 0x1D)
    OP_29(0x7, 0x1, 0x1E)
    OP_29(0x7, 0x1, 0x1F)
    OP_29(0x8, 0x1, 0x0)
    OP_29(0x8, 0x1, 0x1)
    OP_29(0x8, 0x1, 0x2)
    OP_29(0x8, 0x1, 0x3)
    OP_29(0x8, 0x1, 0x4)
    OP_29(0x8, 0x1, 0x5)
    OP_29(0x8, 0x1, 0x6)
    OP_29(0x8, 0x1, 0x7)
    OP_29(0x8, 0x1, 0x8)
    OP_29(0x8, 0x1, 0x9)
    OP_29(0x8, 0x1, 0xA)
    OP_29(0x8, 0x1, 0xB)
    OP_29(0x8, 0x1, 0xC)
    OP_29(0x8, 0x1, 0xD)
    OP_29(0x8, 0x1, 0xE)
    OP_29(0x8, 0x1, 0xF)
    OP_29(0x8, 0x1, 0x10)
    OP_29(0x8, 0x1, 0x11)
    OP_29(0x8, 0x1, 0x12)
    OP_29(0x8, 0x1, 0x13)
    OP_29(0x8, 0x1, 0x14)
    OP_29(0x8, 0x1, 0x15)
    OP_29(0x8, 0x1, 0x16)
    OP_29(0x8, 0x1, 0x17)
    OP_29(0x8, 0x1, 0x18)
    OP_29(0x8, 0x1, 0x19)
    OP_29(0x8, 0x1, 0x1A)
    OP_29(0x8, 0x1, 0x1B)
    OP_29(0x8, 0x1, 0x1C)
    OP_29(0x8, 0x1, 0x1D)
    OP_29(0x8, 0x1, 0x1E)
    OP_29(0x8, 0x1, 0x1F)
    OP_29(0x9, 0x1, 0x0)
    OP_29(0x9, 0x1, 0x1)
    OP_29(0x9, 0x1, 0x2)
    OP_29(0x9, 0x1, 0x3)
    OP_29(0x9, 0x1, 0x4)
    OP_29(0x9, 0x1, 0x5)
    OP_29(0x9, 0x1, 0x6)
    OP_29(0x9, 0x1, 0x7)
    OP_29(0x9, 0x1, 0x8)
    OP_29(0x9, 0x1, 0x9)
    OP_29(0x9, 0x1, 0xA)
    OP_29(0x9, 0x1, 0xB)
    OP_29(0x9, 0x1, 0xC)
    OP_29(0x9, 0x1, 0xD)
    OP_29(0x9, 0x1, 0xE)
    OP_29(0x9, 0x1, 0xF)
    OP_29(0x9, 0x1, 0x10)
    OP_29(0x9, 0x1, 0x11)
    OP_29(0x9, 0x1, 0x12)
    OP_29(0x9, 0x1, 0x13)
    OP_29(0x9, 0x1, 0x14)
    OP_29(0x9, 0x1, 0x15)
    OP_29(0x9, 0x1, 0x16)
    OP_29(0x9, 0x1, 0x17)
    OP_29(0x9, 0x1, 0x18)
    OP_29(0x9, 0x1, 0x19)
    OP_29(0x9, 0x1, 0x1A)
    OP_29(0x9, 0x1, 0x1B)
    OP_29(0x9, 0x1, 0x1C)
    OP_29(0x9, 0x1, 0x1D)
    OP_29(0x9, 0x1, 0x1E)
    OP_29(0x9, 0x1, 0x1F)
    OP_29(0xA, 0x1, 0x0)
    OP_29(0xA, 0x1, 0x1)
    OP_29(0xA, 0x1, 0x2)
    OP_29(0xA, 0x1, 0x3)
    OP_29(0xA, 0x1, 0x4)
    OP_29(0xA, 0x1, 0x5)
    OP_29(0xA, 0x1, 0x6)
    OP_29(0xA, 0x1, 0x7)
    OP_29(0xA, 0x1, 0x8)
    OP_29(0xA, 0x1, 0x9)
    OP_29(0xA, 0x1, 0xA)
    OP_29(0xA, 0x1, 0xB)
    OP_29(0xA, 0x1, 0xC)
    OP_29(0xA, 0x1, 0xD)
    OP_29(0xA, 0x1, 0xE)
    OP_29(0xA, 0x1, 0xF)
    OP_29(0xA, 0x1, 0x10)
    OP_29(0xA, 0x1, 0x11)
    OP_29(0xA, 0x1, 0x12)
    OP_29(0xA, 0x1, 0x13)
    OP_29(0xA, 0x1, 0x14)
    OP_29(0xA, 0x1, 0x15)
    OP_29(0xA, 0x1, 0x16)
    OP_29(0xA, 0x1, 0x17)
    OP_29(0xA, 0x1, 0x18)
    OP_29(0xA, 0x1, 0x19)
    OP_29(0xA, 0x1, 0x1A)
    OP_29(0xA, 0x1, 0x1B)
    OP_29(0xA, 0x1, 0x1C)
    OP_29(0xA, 0x1, 0x1D)
    OP_29(0xA, 0x1, 0x1E)
    OP_29(0xA, 0x1, 0x1F)
    OP_29(0xB, 0x1, 0x0)
    OP_29(0xB, 0x1, 0x1)
    OP_29(0xB, 0x1, 0x2)
    OP_29(0xB, 0x1, 0x3)
    OP_29(0xB, 0x1, 0x4)
    OP_29(0xB, 0x1, 0x5)
    OP_29(0xB, 0x1, 0x6)
    OP_29(0xB, 0x1, 0x7)
    OP_29(0xB, 0x1, 0x8)
    OP_29(0xB, 0x1, 0x9)
    OP_29(0xB, 0x1, 0xA)
    OP_29(0xB, 0x1, 0xB)
    OP_29(0xB, 0x1, 0xC)
    OP_29(0xB, 0x1, 0xD)
    OP_29(0xB, 0x1, 0xE)
    OP_29(0xB, 0x1, 0xF)
    OP_29(0xB, 0x1, 0x10)
    OP_29(0xB, 0x1, 0x11)
    OP_29(0xB, 0x1, 0x12)
    OP_29(0xB, 0x1, 0x13)
    OP_29(0xB, 0x1, 0x14)
    OP_29(0xB, 0x1, 0x15)
    OP_29(0xB, 0x1, 0x16)
    OP_29(0xB, 0x1, 0x17)
    OP_29(0xB, 0x1, 0x18)
    OP_29(0xB, 0x1, 0x19)
    OP_29(0xB, 0x1, 0x1A)
    OP_29(0xB, 0x1, 0x1B)
    OP_29(0xB, 0x1, 0x1C)
    OP_29(0xB, 0x1, 0x1D)
    OP_29(0xB, 0x1, 0x1E)
    OP_29(0xB, 0x1, 0x1F)
    OP_29(0xC, 0x1, 0x0)
    OP_29(0xC, 0x1, 0x1)
    OP_29(0xC, 0x1, 0x2)
    OP_29(0xC, 0x1, 0x3)
    OP_29(0xC, 0x1, 0x4)
    OP_29(0xC, 0x1, 0x5)
    OP_29(0xC, 0x1, 0x6)
    OP_29(0xC, 0x1, 0x7)
    OP_29(0xC, 0x1, 0x8)
    OP_29(0xC, 0x1, 0x9)
    OP_29(0xC, 0x1, 0xA)
    OP_29(0xC, 0x1, 0xB)
    OP_29(0xC, 0x1, 0xC)
    OP_29(0xC, 0x1, 0xD)
    OP_29(0xC, 0x1, 0xE)
    OP_29(0xC, 0x1, 0xF)
    OP_29(0xC, 0x1, 0x10)
    OP_29(0xC, 0x1, 0x11)
    OP_29(0xC, 0x1, 0x12)
    OP_29(0xC, 0x1, 0x13)
    OP_29(0xC, 0x1, 0x14)
    OP_29(0xC, 0x1, 0x15)
    OP_29(0xC, 0x1, 0x16)
    OP_29(0xC, 0x1, 0x17)
    OP_29(0xC, 0x1, 0x18)
    OP_29(0xC, 0x1, 0x19)
    OP_29(0xC, 0x1, 0x1A)
    OP_29(0xC, 0x1, 0x1B)
    OP_29(0xC, 0x1, 0x1C)
    OP_29(0xC, 0x1, 0x1D)
    OP_29(0xC, 0x1, 0x1E)
    OP_29(0xC, 0x1, 0x1F)
    OP_29(0xD, 0x1, 0x0)
    OP_29(0xD, 0x1, 0x1)
    OP_29(0xD, 0x1, 0x2)
    OP_29(0xD, 0x1, 0x3)
    OP_29(0xD, 0x1, 0x4)
    OP_29(0xD, 0x1, 0x5)
    OP_29(0xD, 0x1, 0x6)
    OP_29(0xD, 0x1, 0x7)
    OP_29(0xD, 0x1, 0x8)
    OP_29(0xD, 0x1, 0x9)
    OP_29(0xD, 0x1, 0xA)
    OP_29(0xD, 0x1, 0xB)
    OP_29(0xD, 0x1, 0xC)
    OP_29(0xD, 0x1, 0xD)
    OP_29(0xD, 0x1, 0xE)
    OP_29(0xD, 0x1, 0xF)
    OP_29(0xD, 0x1, 0x10)
    OP_29(0xD, 0x1, 0x11)
    OP_29(0xD, 0x1, 0x12)
    OP_29(0xD, 0x1, 0x13)
    OP_29(0xD, 0x1, 0x14)
    OP_29(0xD, 0x1, 0x15)
    OP_29(0xD, 0x1, 0x16)
    OP_29(0xD, 0x1, 0x17)
    OP_29(0xD, 0x1, 0x18)
    OP_29(0xD, 0x1, 0x19)
    OP_29(0xD, 0x1, 0x1A)
    OP_29(0xD, 0x1, 0x1B)
    OP_29(0xD, 0x1, 0x1C)
    OP_29(0xD, 0x1, 0x1D)
    OP_29(0xD, 0x1, 0x1E)
    OP_29(0xD, 0x1, 0x1F)
    OP_29(0xE, 0x1, 0x0)
    OP_29(0xE, 0x1, 0x1)
    OP_29(0xE, 0x1, 0x2)
    OP_29(0xE, 0x1, 0x3)
    OP_29(0xE, 0x1, 0x4)
    OP_29(0xE, 0x1, 0x5)
    OP_29(0xE, 0x1, 0x6)
    OP_29(0xE, 0x1, 0x7)
    OP_29(0xE, 0x1, 0x8)
    OP_29(0xE, 0x1, 0x9)
    OP_29(0xE, 0x1, 0xA)
    OP_29(0xE, 0x1, 0xB)
    OP_29(0xE, 0x1, 0xC)
    OP_29(0xE, 0x1, 0xD)
    OP_29(0xE, 0x1, 0xE)
    OP_29(0xE, 0x1, 0xF)
    OP_29(0xE, 0x1, 0x10)
    OP_29(0xE, 0x1, 0x11)
    OP_29(0xE, 0x1, 0x12)
    OP_29(0xE, 0x1, 0x13)
    OP_29(0xE, 0x1, 0x14)
    OP_29(0xE, 0x1, 0x15)
    OP_29(0xE, 0x1, 0x16)
    OP_29(0xE, 0x1, 0x17)
    OP_29(0xE, 0x1, 0x18)
    OP_29(0xE, 0x1, 0x19)
    OP_29(0xE, 0x1, 0x1A)
    OP_29(0xE, 0x1, 0x1B)
    OP_29(0xE, 0x1, 0x1C)
    OP_29(0xE, 0x1, 0x1D)
    OP_29(0xE, 0x1, 0x1E)
    OP_29(0xE, 0x1, 0x1F)
    OP_29(0xF, 0x1, 0x0)
    OP_29(0xF, 0x1, 0x1)
    OP_29(0xF, 0x1, 0x2)
    OP_29(0xF, 0x1, 0x3)
    OP_29(0xF, 0x1, 0x4)
    OP_29(0xF, 0x1, 0x5)
    OP_29(0xF, 0x1, 0x6)
    OP_29(0xF, 0x1, 0x7)
    OP_29(0xF, 0x1, 0x8)
    OP_29(0xF, 0x1, 0x9)
    OP_29(0xF, 0x1, 0xA)
    OP_29(0xF, 0x1, 0xB)
    OP_29(0xF, 0x1, 0xC)
    OP_29(0xF, 0x1, 0xD)
    OP_29(0xF, 0x1, 0xE)
    OP_29(0xF, 0x1, 0xF)
    OP_29(0xF, 0x1, 0x10)
    OP_29(0xF, 0x1, 0x11)
    OP_29(0xF, 0x1, 0x12)
    OP_29(0xF, 0x1, 0x13)
    OP_29(0xF, 0x1, 0x14)
    OP_29(0xF, 0x1, 0x15)
    OP_29(0xF, 0x1, 0x16)
    OP_29(0xF, 0x1, 0x17)
    OP_29(0xF, 0x1, 0x18)
    OP_29(0xF, 0x1, 0x19)
    OP_29(0xF, 0x1, 0x1A)
    OP_29(0xF, 0x1, 0x1B)
    OP_29(0xF, 0x1, 0x1C)
    OP_29(0xF, 0x1, 0x1D)
    OP_29(0xF, 0x1, 0x1E)
    OP_29(0xF, 0x1, 0x1F)
    OP_29(0x10, 0x1, 0x0)
    OP_29(0x10, 0x1, 0x1)
    OP_29(0x10, 0x1, 0x2)
    OP_29(0x10, 0x1, 0x3)
    OP_29(0x10, 0x1, 0x4)
    OP_29(0x10, 0x1, 0x5)
    OP_29(0x10, 0x1, 0x6)
    OP_29(0x10, 0x1, 0x7)
    OP_29(0x10, 0x1, 0x8)
    OP_29(0x10, 0x1, 0x9)
    OP_29(0x10, 0x1, 0xA)
    OP_29(0x10, 0x1, 0xB)
    OP_29(0x10, 0x1, 0xC)
    OP_29(0x10, 0x1, 0xD)
    OP_29(0x10, 0x1, 0xE)
    OP_29(0x10, 0x1, 0xF)
    OP_29(0x10, 0x1, 0x10)
    OP_29(0x10, 0x1, 0x11)
    OP_29(0x10, 0x1, 0x12)
    OP_29(0x10, 0x1, 0x13)
    OP_29(0x10, 0x1, 0x14)
    OP_29(0x10, 0x1, 0x15)
    OP_29(0x10, 0x1, 0x16)
    OP_29(0x10, 0x1, 0x17)
    OP_29(0x10, 0x1, 0x18)
    OP_29(0x10, 0x1, 0x19)
    OP_29(0x10, 0x1, 0x1A)
    OP_29(0x10, 0x1, 0x1B)
    OP_29(0x10, 0x1, 0x1C)
    OP_29(0x10, 0x1, 0x1D)
    OP_29(0x10, 0x1, 0x1E)
    OP_29(0x10, 0x1, 0x1F)
    OP_29(0x11, 0x1, 0x0)
    OP_29(0x11, 0x1, 0x1)
    OP_29(0x11, 0x1, 0x2)
    OP_29(0x11, 0x1, 0x3)
    OP_29(0x11, 0x1, 0x4)
    OP_29(0x11, 0x1, 0x5)
    OP_29(0x11, 0x1, 0x6)
    OP_29(0x11, 0x1, 0x7)
    OP_29(0x11, 0x1, 0x8)
    OP_29(0x11, 0x1, 0x9)
    OP_29(0x11, 0x1, 0xA)
    OP_29(0x11, 0x1, 0xB)
    OP_29(0x11, 0x1, 0xC)
    OP_29(0x11, 0x1, 0xD)
    OP_29(0x11, 0x1, 0xE)
    OP_29(0x11, 0x1, 0xF)
    OP_29(0x11, 0x1, 0x10)
    OP_29(0x11, 0x1, 0x11)
    OP_29(0x11, 0x1, 0x12)
    OP_29(0x11, 0x1, 0x13)
    OP_29(0x11, 0x1, 0x14)
    OP_29(0x11, 0x1, 0x15)
    OP_29(0x11, 0x1, 0x16)
    OP_29(0x11, 0x1, 0x17)
    OP_29(0x11, 0x1, 0x18)
    OP_29(0x11, 0x1, 0x19)
    OP_29(0x11, 0x1, 0x1A)
    OP_29(0x11, 0x1, 0x1B)
    OP_29(0x11, 0x1, 0x1C)
    OP_29(0x11, 0x1, 0x1D)
    OP_29(0x11, 0x1, 0x1E)
    OP_29(0x11, 0x1, 0x1F)
    OP_29(0x12, 0x1, 0x0)
    OP_29(0x12, 0x1, 0x1)
    OP_29(0x12, 0x1, 0x2)
    OP_29(0x12, 0x1, 0x3)
    OP_29(0x12, 0x1, 0x4)
    OP_29(0x12, 0x1, 0x5)
    OP_29(0x12, 0x1, 0x6)
    OP_29(0x12, 0x1, 0x7)
    OP_29(0x12, 0x1, 0x8)
    OP_29(0x12, 0x1, 0x9)
    OP_29(0x12, 0x1, 0xA)
    OP_29(0x12, 0x1, 0xB)
    OP_29(0x12, 0x1, 0xC)
    OP_29(0x12, 0x1, 0xD)
    OP_29(0x12, 0x1, 0xE)
    OP_29(0x12, 0x1, 0xF)
    OP_29(0x12, 0x1, 0x10)
    OP_29(0x12, 0x1, 0x11)
    OP_29(0x12, 0x1, 0x12)
    OP_29(0x12, 0x1, 0x13)
    OP_29(0x12, 0x1, 0x14)
    OP_29(0x12, 0x1, 0x15)
    OP_29(0x12, 0x1, 0x16)
    OP_29(0x12, 0x1, 0x17)
    OP_29(0x12, 0x1, 0x18)
    OP_29(0x12, 0x1, 0x19)
    OP_29(0x12, 0x1, 0x1A)
    OP_29(0x12, 0x1, 0x1B)
    OP_29(0x12, 0x1, 0x1C)
    OP_29(0x12, 0x1, 0x1D)
    OP_29(0x12, 0x1, 0x1E)
    OP_29(0x12, 0x1, 0x1F)
    OP_29(0x13, 0x1, 0x0)
    OP_29(0x13, 0x1, 0x1)
    OP_29(0x13, 0x1, 0x2)
    OP_29(0x13, 0x1, 0x3)
    OP_29(0x13, 0x1, 0x4)
    OP_29(0x13, 0x1, 0x5)
    OP_29(0x13, 0x1, 0x6)
    OP_29(0x13, 0x1, 0x7)
    OP_29(0x13, 0x1, 0x8)
    OP_29(0x13, 0x1, 0x9)
    OP_29(0x13, 0x1, 0xA)
    OP_29(0x13, 0x1, 0xB)
    OP_29(0x13, 0x1, 0xC)
    OP_29(0x13, 0x1, 0xD)
    OP_29(0x13, 0x1, 0xE)
    OP_29(0x13, 0x1, 0xF)
    OP_29(0x13, 0x1, 0x10)
    OP_29(0x13, 0x1, 0x11)
    OP_29(0x13, 0x1, 0x12)
    OP_29(0x13, 0x1, 0x13)
    OP_29(0x13, 0x1, 0x14)
    OP_29(0x13, 0x1, 0x15)
    OP_29(0x13, 0x1, 0x16)
    OP_29(0x13, 0x1, 0x17)
    OP_29(0x13, 0x1, 0x18)
    OP_29(0x13, 0x1, 0x19)
    OP_29(0x13, 0x1, 0x1A)
    OP_29(0x13, 0x1, 0x1B)
    OP_29(0x13, 0x1, 0x1C)
    OP_29(0x13, 0x1, 0x1D)
    OP_29(0x13, 0x1, 0x1E)
    OP_29(0x13, 0x1, 0x1F)
    OP_29(0x14, 0x1, 0x0)
    OP_29(0x14, 0x1, 0x1)
    OP_29(0x14, 0x1, 0x2)
    OP_29(0x14, 0x1, 0x3)
    OP_29(0x14, 0x1, 0x4)
    OP_29(0x14, 0x1, 0x5)
    OP_29(0x14, 0x1, 0x6)
    OP_29(0x14, 0x1, 0x7)
    OP_29(0x14, 0x1, 0x8)
    OP_29(0x14, 0x1, 0x9)
    OP_29(0x14, 0x1, 0xA)
    OP_29(0x14, 0x1, 0xB)
    OP_29(0x14, 0x1, 0xC)
    OP_29(0x14, 0x1, 0xD)
    OP_29(0x14, 0x1, 0xE)
    OP_29(0x14, 0x1, 0xF)
    OP_29(0x14, 0x1, 0x10)
    OP_29(0x14, 0x1, 0x11)
    OP_29(0x14, 0x1, 0x12)
    OP_29(0x14, 0x1, 0x13)
    OP_29(0x14, 0x1, 0x14)
    OP_29(0x14, 0x1, 0x15)
    OP_29(0x14, 0x1, 0x16)
    OP_29(0x14, 0x1, 0x17)
    OP_29(0x14, 0x1, 0x18)
    OP_29(0x14, 0x1, 0x19)
    OP_29(0x14, 0x1, 0x1A)
    OP_29(0x14, 0x1, 0x1B)
    OP_29(0x14, 0x1, 0x1C)
    OP_29(0x14, 0x1, 0x1D)
    OP_29(0x14, 0x1, 0x1E)
    OP_29(0x14, 0x1, 0x1F)
    OP_29(0x15, 0x1, 0x0)
    OP_29(0x15, 0x1, 0x1)
    OP_29(0x15, 0x1, 0x2)
    OP_29(0x15, 0x1, 0x3)
    OP_29(0x15, 0x1, 0x4)
    OP_29(0x15, 0x1, 0x5)
    OP_29(0x15, 0x1, 0x6)
    OP_29(0x15, 0x1, 0x7)
    OP_29(0x15, 0x1, 0x8)
    OP_29(0x15, 0x1, 0x9)
    OP_29(0x15, 0x1, 0xA)
    OP_29(0x15, 0x1, 0xB)
    OP_29(0x15, 0x1, 0xC)
    OP_29(0x15, 0x1, 0xD)
    OP_29(0x15, 0x1, 0xE)
    OP_29(0x15, 0x1, 0xF)
    OP_29(0x15, 0x1, 0x10)
    OP_29(0x15, 0x1, 0x11)
    OP_29(0x15, 0x1, 0x12)
    OP_29(0x15, 0x1, 0x13)
    OP_29(0x15, 0x1, 0x14)
    OP_29(0x15, 0x1, 0x15)
    OP_29(0x15, 0x1, 0x16)
    OP_29(0x15, 0x1, 0x17)
    OP_29(0x15, 0x1, 0x18)
    OP_29(0x15, 0x1, 0x19)
    OP_29(0x15, 0x1, 0x1A)
    OP_29(0x15, 0x1, 0x1B)
    OP_29(0x15, 0x1, 0x1C)
    OP_29(0x15, 0x1, 0x1D)
    OP_29(0x15, 0x1, 0x1E)
    OP_29(0x15, 0x1, 0x1F)
    OP_29(0x16, 0x1, 0x0)
    OP_29(0x16, 0x1, 0x1)
    OP_29(0x16, 0x1, 0x2)
    OP_29(0x16, 0x1, 0x3)
    OP_29(0x16, 0x1, 0x4)
    OP_29(0x16, 0x1, 0x5)
    OP_29(0x16, 0x1, 0x6)
    OP_29(0x16, 0x1, 0x7)
    OP_29(0x16, 0x1, 0x8)
    OP_29(0x16, 0x1, 0x9)
    OP_29(0x16, 0x1, 0xA)
    OP_29(0x16, 0x1, 0xB)
    OP_29(0x16, 0x1, 0xC)
    OP_29(0x16, 0x1, 0xD)
    OP_29(0x16, 0x1, 0xE)
    OP_29(0x16, 0x1, 0xF)
    OP_29(0x16, 0x1, 0x10)
    OP_29(0x16, 0x1, 0x11)
    OP_29(0x16, 0x1, 0x12)
    OP_29(0x16, 0x1, 0x13)
    OP_29(0x16, 0x1, 0x14)
    OP_29(0x16, 0x1, 0x15)
    OP_29(0x16, 0x1, 0x16)
    OP_29(0x16, 0x1, 0x17)
    OP_29(0x16, 0x1, 0x18)
    OP_29(0x16, 0x1, 0x19)
    OP_29(0x16, 0x1, 0x1A)
    OP_29(0x16, 0x1, 0x1B)
    OP_29(0x16, 0x1, 0x1C)
    OP_29(0x16, 0x1, 0x1D)
    OP_29(0x16, 0x1, 0x1E)
    OP_29(0x16, 0x1, 0x1F)
    OP_29(0x17, 0x1, 0x0)
    OP_29(0x17, 0x1, 0x1)
    OP_29(0x17, 0x1, 0x2)
    OP_29(0x17, 0x1, 0x3)
    OP_29(0x17, 0x1, 0x4)
    OP_29(0x17, 0x1, 0x5)
    OP_29(0x17, 0x1, 0x6)
    OP_29(0x17, 0x1, 0x7)
    OP_29(0x17, 0x1, 0x8)
    OP_29(0x17, 0x1, 0x9)
    OP_29(0x17, 0x1, 0xA)
    OP_29(0x17, 0x1, 0xB)
    OP_29(0x17, 0x1, 0xC)
    OP_29(0x17, 0x1, 0xD)
    OP_29(0x17, 0x1, 0xE)
    OP_29(0x17, 0x1, 0xF)
    OP_29(0x17, 0x1, 0x10)
    OP_29(0x17, 0x1, 0x11)
    OP_29(0x17, 0x1, 0x12)
    OP_29(0x17, 0x1, 0x13)
    OP_29(0x17, 0x1, 0x14)
    OP_29(0x17, 0x1, 0x15)
    OP_29(0x17, 0x1, 0x16)
    OP_29(0x17, 0x1, 0x17)
    OP_29(0x17, 0x1, 0x18)
    OP_29(0x17, 0x1, 0x19)
    OP_29(0x17, 0x1, 0x1A)
    OP_29(0x17, 0x1, 0x1B)
    OP_29(0x17, 0x1, 0x1C)
    OP_29(0x17, 0x1, 0x1D)
    OP_29(0x17, 0x1, 0x1E)
    OP_29(0x17, 0x1, 0x1F)
    OP_29(0x18, 0x1, 0x0)
    OP_29(0x18, 0x1, 0x1)
    OP_29(0x18, 0x1, 0x2)
    OP_29(0x18, 0x1, 0x3)
    OP_29(0x18, 0x1, 0x4)
    OP_29(0x18, 0x1, 0x5)
    OP_29(0x18, 0x1, 0x6)
    OP_29(0x18, 0x1, 0x7)
    OP_29(0x18, 0x1, 0x8)
    OP_29(0x18, 0x1, 0x9)
    OP_29(0x18, 0x1, 0xA)
    OP_29(0x18, 0x1, 0xB)
    OP_29(0x18, 0x1, 0xC)
    OP_29(0x18, 0x1, 0xD)
    OP_29(0x18, 0x1, 0xE)
    OP_29(0x18, 0x1, 0xF)
    OP_29(0x18, 0x1, 0x10)
    OP_29(0x18, 0x1, 0x11)
    OP_29(0x18, 0x1, 0x12)
    OP_29(0x18, 0x1, 0x13)
    OP_29(0x18, 0x1, 0x14)
    OP_29(0x18, 0x1, 0x15)
    OP_29(0x18, 0x1, 0x16)
    OP_29(0x18, 0x1, 0x17)
    OP_29(0x18, 0x1, 0x18)
    OP_29(0x18, 0x1, 0x19)
    OP_29(0x18, 0x1, 0x1A)
    OP_29(0x18, 0x1, 0x1B)
    OP_29(0x18, 0x1, 0x1C)
    OP_29(0x18, 0x1, 0x1D)
    OP_29(0x18, 0x1, 0x1E)
    OP_29(0x18, 0x1, 0x1F)
    OP_29(0x19, 0x1, 0x0)
    OP_29(0x19, 0x1, 0x1)
    OP_29(0x19, 0x1, 0x2)
    OP_29(0x19, 0x1, 0x3)
    OP_29(0x19, 0x1, 0x4)
    OP_29(0x19, 0x1, 0x5)
    OP_29(0x19, 0x1, 0x6)
    OP_29(0x19, 0x1, 0x7)
    OP_29(0x19, 0x1, 0x8)
    OP_29(0x19, 0x1, 0x9)
    OP_29(0x19, 0x1, 0xA)
    OP_29(0x19, 0x1, 0xB)
    OP_29(0x19, 0x1, 0xC)
    OP_29(0x19, 0x1, 0xD)
    OP_29(0x19, 0x1, 0xE)
    OP_29(0x19, 0x1, 0xF)
    OP_29(0x19, 0x1, 0x10)
    OP_29(0x19, 0x1, 0x11)
    OP_29(0x19, 0x1, 0x12)
    OP_29(0x19, 0x1, 0x13)
    OP_29(0x19, 0x1, 0x14)
    OP_29(0x19, 0x1, 0x15)
    OP_29(0x19, 0x1, 0x16)
    OP_29(0x19, 0x1, 0x17)
    OP_29(0x19, 0x1, 0x18)
    OP_29(0x19, 0x1, 0x19)
    OP_29(0x19, 0x1, 0x1A)
    OP_29(0x19, 0x1, 0x1B)
    OP_29(0x19, 0x1, 0x1C)
    OP_29(0x19, 0x1, 0x1D)
    OP_29(0x19, 0x1, 0x1E)
    OP_29(0x19, 0x1, 0x1F)
    OP_29(0x1A, 0x1, 0x0)
    OP_29(0x1A, 0x1, 0x1)
    OP_29(0x1A, 0x1, 0x2)
    OP_29(0x1A, 0x1, 0x3)
    OP_29(0x1A, 0x1, 0x4)
    OP_29(0x1A, 0x1, 0x5)
    OP_29(0x1A, 0x1, 0x6)
    OP_29(0x1A, 0x1, 0x7)
    OP_29(0x1A, 0x1, 0x8)
    OP_29(0x1A, 0x1, 0x9)
    OP_29(0x1A, 0x1, 0xA)
    OP_29(0x1A, 0x1, 0xB)
    OP_29(0x1A, 0x1, 0xC)
    OP_29(0x1A, 0x1, 0xD)
    OP_29(0x1A, 0x1, 0xE)
    OP_29(0x1A, 0x1, 0xF)
    OP_29(0x1A, 0x1, 0x10)
    OP_29(0x1A, 0x1, 0x11)
    OP_29(0x1A, 0x1, 0x12)
    OP_29(0x1A, 0x1, 0x13)
    OP_29(0x1A, 0x1, 0x14)
    OP_29(0x1A, 0x1, 0x15)
    OP_29(0x1A, 0x1, 0x16)
    OP_29(0x1A, 0x1, 0x17)
    OP_29(0x1A, 0x1, 0x18)
    OP_29(0x1A, 0x1, 0x19)
    OP_29(0x1A, 0x1, 0x1A)
    OP_29(0x1A, 0x1, 0x1B)
    OP_29(0x1A, 0x1, 0x1C)
    OP_29(0x1A, 0x1, 0x1D)
    OP_29(0x1A, 0x1, 0x1E)
    OP_29(0x1A, 0x1, 0x1F)
    OP_29(0x1B, 0x1, 0x0)
    OP_29(0x1B, 0x1, 0x1)
    OP_29(0x1B, 0x1, 0x2)
    OP_29(0x1B, 0x1, 0x3)
    OP_29(0x1B, 0x1, 0x4)
    OP_29(0x1B, 0x1, 0x5)
    OP_29(0x1B, 0x1, 0x6)
    OP_29(0x1B, 0x1, 0x7)
    OP_29(0x1B, 0x1, 0x8)
    OP_29(0x1B, 0x1, 0x9)
    OP_29(0x1B, 0x1, 0xA)
    OP_29(0x1B, 0x1, 0xB)
    OP_29(0x1B, 0x1, 0xC)
    OP_29(0x1B, 0x1, 0xD)
    OP_29(0x1B, 0x1, 0xE)
    OP_29(0x1B, 0x1, 0xF)
    OP_29(0x1B, 0x1, 0x10)
    OP_29(0x1B, 0x1, 0x11)
    OP_29(0x1B, 0x1, 0x12)
    OP_29(0x1B, 0x1, 0x13)
    OP_29(0x1B, 0x1, 0x14)
    OP_29(0x1B, 0x1, 0x15)
    OP_29(0x1B, 0x1, 0x16)
    OP_29(0x1B, 0x1, 0x17)
    OP_29(0x1B, 0x1, 0x18)
    OP_29(0x1B, 0x1, 0x19)
    OP_29(0x1B, 0x1, 0x1A)
    OP_29(0x1B, 0x1, 0x1B)
    OP_29(0x1B, 0x1, 0x1C)
    OP_29(0x1B, 0x1, 0x1D)
    OP_29(0x1B, 0x1, 0x1E)
    OP_29(0x1B, 0x1, 0x1F)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)
    OP_29(0x1C, 0x1, 0x4)
    OP_29(0x1C, 0x1, 0x5)
    OP_29(0x1C, 0x1, 0x6)
    OP_29(0x1C, 0x1, 0x7)
    OP_29(0x1C, 0x1, 0x8)
    OP_29(0x1C, 0x1, 0x9)
    OP_29(0x1C, 0x1, 0xA)
    OP_29(0x1C, 0x1, 0xB)
    OP_29(0x1C, 0x1, 0xC)
    OP_29(0x1C, 0x1, 0xD)
    OP_29(0x1C, 0x1, 0xE)
    OP_29(0x1C, 0x1, 0xF)
    OP_29(0x1C, 0x1, 0x10)
    OP_29(0x1C, 0x1, 0x11)
    OP_29(0x1C, 0x1, 0x12)
    OP_29(0x1C, 0x1, 0x13)
    OP_29(0x1C, 0x1, 0x14)
    OP_29(0x1C, 0x1, 0x15)
    OP_29(0x1C, 0x1, 0x16)
    OP_29(0x1C, 0x1, 0x17)
    OP_29(0x1C, 0x1, 0x18)
    OP_29(0x1C, 0x1, 0x19)
    OP_29(0x1C, 0x1, 0x1A)
    OP_29(0x1C, 0x1, 0x1B)
    OP_29(0x1C, 0x1, 0x1C)
    OP_29(0x1C, 0x1, 0x1D)
    OP_29(0x1C, 0x1, 0x1E)
    OP_29(0x1C, 0x1, 0x1F)
    OP_29(0x1D, 0x1, 0x0)
    OP_29(0x1D, 0x1, 0x1)
    OP_29(0x1D, 0x1, 0x2)
    OP_29(0x1D, 0x1, 0x3)
    OP_29(0x1D, 0x1, 0x4)
    OP_29(0x1D, 0x1, 0x5)
    OP_29(0x1D, 0x1, 0x6)
    OP_29(0x1D, 0x1, 0x7)
    OP_29(0x1D, 0x1, 0x8)
    OP_29(0x1D, 0x1, 0x9)
    OP_29(0x1D, 0x1, 0xA)
    OP_29(0x1D, 0x1, 0xB)
    OP_29(0x1D, 0x1, 0xC)
    OP_29(0x1D, 0x1, 0xD)
    OP_29(0x1D, 0x1, 0xE)
    OP_29(0x1D, 0x1, 0xF)
    OP_29(0x1D, 0x1, 0x10)
    OP_29(0x1D, 0x1, 0x11)
    OP_29(0x1D, 0x1, 0x12)
    OP_29(0x1D, 0x1, 0x13)
    OP_29(0x1D, 0x1, 0x14)
    OP_29(0x1D, 0x1, 0x15)
    OP_29(0x1D, 0x1, 0x16)
    OP_29(0x1D, 0x1, 0x17)
    OP_29(0x1D, 0x1, 0x18)
    OP_29(0x1D, 0x1, 0x19)
    OP_29(0x1D, 0x1, 0x1A)
    OP_29(0x1D, 0x1, 0x1B)
    OP_29(0x1D, 0x1, 0x1C)
    OP_29(0x1D, 0x1, 0x1D)
    OP_29(0x1D, 0x1, 0x1E)
    OP_29(0x1D, 0x1, 0x1F)
    OP_29(0x1E, 0x1, 0x0)
    OP_29(0x1E, 0x1, 0x1)
    OP_29(0x1E, 0x1, 0x2)
    OP_29(0x1E, 0x1, 0x3)
    OP_29(0x1E, 0x1, 0x4)
    OP_29(0x1E, 0x1, 0x5)
    OP_29(0x1E, 0x1, 0x6)
    OP_29(0x1E, 0x1, 0x7)
    OP_29(0x1E, 0x1, 0x8)
    OP_29(0x1E, 0x1, 0x9)
    OP_29(0x1E, 0x1, 0xA)
    OP_29(0x1E, 0x1, 0xB)
    OP_29(0x1E, 0x1, 0xC)
    OP_29(0x1E, 0x1, 0xD)
    OP_29(0x1E, 0x1, 0xE)
    OP_29(0x1E, 0x1, 0xF)
    OP_29(0x1E, 0x1, 0x10)
    OP_29(0x1E, 0x1, 0x11)
    OP_29(0x1E, 0x1, 0x12)
    OP_29(0x1E, 0x1, 0x13)
    OP_29(0x1E, 0x1, 0x14)
    OP_29(0x1E, 0x1, 0x15)
    OP_29(0x1E, 0x1, 0x16)
    OP_29(0x1E, 0x1, 0x17)
    OP_29(0x1E, 0x1, 0x18)
    OP_29(0x1E, 0x1, 0x19)
    OP_29(0x1E, 0x1, 0x1A)
    OP_29(0x1E, 0x1, 0x1B)
    OP_29(0x1E, 0x1, 0x1C)
    OP_29(0x1E, 0x1, 0x1D)
    OP_29(0x1E, 0x1, 0x1E)
    OP_29(0x1E, 0x1, 0x1F)
    OP_29(0x1F, 0x1, 0x0)
    OP_29(0x1F, 0x1, 0x1)
    OP_29(0x1F, 0x1, 0x2)
    OP_29(0x1F, 0x1, 0x3)
    OP_29(0x1F, 0x1, 0x4)
    OP_29(0x1F, 0x1, 0x5)
    OP_29(0x1F, 0x1, 0x6)
    OP_29(0x1F, 0x1, 0x7)
    OP_29(0x1F, 0x1, 0x8)
    OP_29(0x1F, 0x1, 0x9)
    OP_29(0x1F, 0x1, 0xA)
    OP_29(0x1F, 0x1, 0xB)
    OP_29(0x1F, 0x1, 0xC)
    OP_29(0x1F, 0x1, 0xD)
    OP_29(0x1F, 0x1, 0xE)
    OP_29(0x1F, 0x1, 0xF)
    OP_29(0x1F, 0x1, 0x10)
    OP_29(0x1F, 0x1, 0x11)
    OP_29(0x1F, 0x1, 0x12)
    OP_29(0x1F, 0x1, 0x13)
    OP_29(0x1F, 0x1, 0x14)
    OP_29(0x1F, 0x1, 0x15)
    OP_29(0x1F, 0x1, 0x16)
    OP_29(0x1F, 0x1, 0x17)
    OP_29(0x1F, 0x1, 0x18)
    OP_29(0x1F, 0x1, 0x19)
    OP_29(0x1F, 0x1, 0x1A)
    OP_29(0x1F, 0x1, 0x1B)
    OP_29(0x1F, 0x1, 0x1C)
    OP_29(0x1F, 0x1, 0x1D)
    OP_29(0x1F, 0x1, 0x1E)
    OP_29(0x1F, 0x1, 0x1F)
    OP_29(0x20, 0x1, 0x0)
    OP_29(0x20, 0x1, 0x1)
    OP_29(0x20, 0x1, 0x2)
    OP_29(0x20, 0x1, 0x3)
    OP_29(0x20, 0x1, 0x4)
    OP_29(0x20, 0x1, 0x5)
    OP_29(0x20, 0x1, 0x6)
    OP_29(0x20, 0x1, 0x7)
    OP_29(0x20, 0x1, 0x8)
    OP_29(0x20, 0x1, 0x9)
    OP_29(0x20, 0x1, 0xA)
    OP_29(0x20, 0x1, 0xB)
    OP_29(0x20, 0x1, 0xC)
    OP_29(0x20, 0x1, 0xD)
    OP_29(0x20, 0x1, 0xE)
    OP_29(0x20, 0x1, 0xF)
    OP_29(0x20, 0x1, 0x10)
    OP_29(0x20, 0x1, 0x11)
    OP_29(0x20, 0x1, 0x12)
    OP_29(0x20, 0x1, 0x13)
    OP_29(0x20, 0x1, 0x14)
    OP_29(0x20, 0x1, 0x15)
    OP_29(0x20, 0x1, 0x16)
    OP_29(0x20, 0x1, 0x17)
    OP_29(0x20, 0x1, 0x18)
    OP_29(0x20, 0x1, 0x19)
    OP_29(0x20, 0x1, 0x1A)
    OP_29(0x20, 0x1, 0x1B)
    OP_29(0x20, 0x1, 0x1C)
    OP_29(0x20, 0x1, 0x1D)
    OP_29(0x20, 0x1, 0x1E)
    OP_29(0x20, 0x1, 0x1F)
    OP_29(0x21, 0x1, 0x0)
    OP_29(0x21, 0x1, 0x1)
    OP_29(0x21, 0x1, 0x2)
    OP_29(0x21, 0x1, 0x3)
    OP_29(0x21, 0x1, 0x4)
    OP_29(0x21, 0x1, 0x5)
    OP_29(0x21, 0x1, 0x6)
    OP_29(0x21, 0x1, 0x7)
    OP_29(0x21, 0x1, 0x8)
    OP_29(0x21, 0x1, 0x9)
    OP_29(0x21, 0x1, 0xA)
    OP_29(0x21, 0x1, 0xB)
    OP_29(0x21, 0x1, 0xC)
    OP_29(0x21, 0x1, 0xD)
    OP_29(0x21, 0x1, 0xE)
    OP_29(0x21, 0x1, 0xF)
    OP_29(0x21, 0x1, 0x10)
    OP_29(0x21, 0x1, 0x11)
    OP_29(0x21, 0x1, 0x12)
    OP_29(0x21, 0x1, 0x13)
    OP_29(0x21, 0x1, 0x14)
    OP_29(0x21, 0x1, 0x15)
    OP_29(0x21, 0x1, 0x16)
    OP_29(0x21, 0x1, 0x17)
    OP_29(0x21, 0x1, 0x18)
    OP_29(0x21, 0x1, 0x19)
    OP_29(0x21, 0x1, 0x1A)
    OP_29(0x21, 0x1, 0x1B)
    OP_29(0x21, 0x1, 0x1C)
    OP_29(0x21, 0x1, 0x1D)
    OP_29(0x21, 0x1, 0x1E)
    OP_29(0x21, 0x1, 0x1F)
    OP_29(0x22, 0x1, 0x0)
    OP_29(0x22, 0x1, 0x1)
    OP_29(0x22, 0x1, 0x2)
    OP_29(0x22, 0x1, 0x3)
    OP_29(0x22, 0x1, 0x4)
    OP_29(0x22, 0x1, 0x5)
    OP_29(0x22, 0x1, 0x6)
    OP_29(0x22, 0x1, 0x7)
    OP_29(0x22, 0x1, 0x8)
    OP_29(0x22, 0x1, 0x9)
    OP_29(0x22, 0x1, 0xA)
    OP_29(0x22, 0x1, 0xB)
    OP_29(0x22, 0x1, 0xC)
    OP_29(0x22, 0x1, 0xD)
    OP_29(0x22, 0x1, 0xE)
    OP_29(0x22, 0x1, 0xF)
    OP_29(0x22, 0x1, 0x10)
    OP_29(0x22, 0x1, 0x11)
    OP_29(0x22, 0x1, 0x12)
    OP_29(0x22, 0x1, 0x13)
    OP_29(0x22, 0x1, 0x14)
    OP_29(0x22, 0x1, 0x15)
    OP_29(0x22, 0x1, 0x16)
    OP_29(0x22, 0x1, 0x17)
    OP_29(0x22, 0x1, 0x18)
    OP_29(0x22, 0x1, 0x19)
    OP_29(0x22, 0x1, 0x1A)
    OP_29(0x22, 0x1, 0x1B)
    OP_29(0x22, 0x1, 0x1C)
    OP_29(0x22, 0x1, 0x1D)
    OP_29(0x22, 0x1, 0x1E)
    OP_29(0x22, 0x1, 0x1F)
    OP_29(0x23, 0x1, 0x0)
    OP_29(0x23, 0x1, 0x1)
    OP_29(0x23, 0x1, 0x2)
    OP_29(0x23, 0x1, 0x3)
    OP_29(0x23, 0x1, 0x4)
    OP_29(0x23, 0x1, 0x5)
    OP_29(0x23, 0x1, 0x6)
    OP_29(0x23, 0x1, 0x7)
    OP_29(0x23, 0x1, 0x8)
    OP_29(0x23, 0x1, 0x9)
    OP_29(0x23, 0x1, 0xA)
    OP_29(0x23, 0x1, 0xB)
    OP_29(0x23, 0x1, 0xC)
    OP_29(0x23, 0x1, 0xD)
    OP_29(0x23, 0x1, 0xE)
    OP_29(0x23, 0x1, 0xF)
    OP_29(0x23, 0x1, 0x10)
    OP_29(0x23, 0x1, 0x11)
    OP_29(0x23, 0x1, 0x12)
    OP_29(0x23, 0x1, 0x13)
    OP_29(0x23, 0x1, 0x14)
    OP_29(0x23, 0x1, 0x15)
    OP_29(0x23, 0x1, 0x16)
    OP_29(0x23, 0x1, 0x17)
    OP_29(0x23, 0x1, 0x18)
    OP_29(0x23, 0x1, 0x19)
    OP_29(0x23, 0x1, 0x1A)
    OP_29(0x23, 0x1, 0x1B)
    OP_29(0x23, 0x1, 0x1C)
    OP_29(0x23, 0x1, 0x1D)
    OP_29(0x23, 0x1, 0x1E)
    OP_29(0x23, 0x1, 0x1F)
    OP_29(0x24, 0x1, 0x0)
    OP_29(0x24, 0x1, 0x1)
    OP_29(0x24, 0x1, 0x2)
    OP_29(0x24, 0x1, 0x3)
    OP_29(0x24, 0x1, 0x4)
    OP_29(0x24, 0x1, 0x5)
    OP_29(0x24, 0x1, 0x6)
    OP_29(0x24, 0x1, 0x7)
    OP_29(0x24, 0x1, 0x8)
    OP_29(0x24, 0x1, 0x9)
    OP_29(0x24, 0x1, 0xA)
    OP_29(0x24, 0x1, 0xB)
    OP_29(0x24, 0x1, 0xC)
    OP_29(0x24, 0x1, 0xD)
    OP_29(0x24, 0x1, 0xE)
    OP_29(0x24, 0x1, 0xF)
    OP_29(0x24, 0x1, 0x10)
    OP_29(0x24, 0x1, 0x11)
    OP_29(0x24, 0x1, 0x12)
    OP_29(0x24, 0x1, 0x13)
    OP_29(0x24, 0x1, 0x14)
    OP_29(0x24, 0x1, 0x15)
    OP_29(0x24, 0x1, 0x16)
    OP_29(0x24, 0x1, 0x17)
    OP_29(0x24, 0x1, 0x18)
    OP_29(0x24, 0x1, 0x19)
    OP_29(0x24, 0x1, 0x1A)
    OP_29(0x24, 0x1, 0x1B)
    OP_29(0x24, 0x1, 0x1C)
    OP_29(0x24, 0x1, 0x1D)
    OP_29(0x24, 0x1, 0x1E)
    OP_29(0x24, 0x1, 0x1F)
    OP_29(0x25, 0x1, 0x0)
    OP_29(0x25, 0x1, 0x1)
    OP_29(0x25, 0x1, 0x2)
    OP_29(0x25, 0x1, 0x3)
    OP_29(0x25, 0x1, 0x4)
    OP_29(0x25, 0x1, 0x5)
    OP_29(0x25, 0x1, 0x6)
    OP_29(0x25, 0x1, 0x7)
    OP_29(0x25, 0x1, 0x8)
    OP_29(0x25, 0x1, 0x9)
    OP_29(0x25, 0x1, 0xA)
    OP_29(0x25, 0x1, 0xB)
    OP_29(0x25, 0x1, 0xC)
    OP_29(0x25, 0x1, 0xD)
    OP_29(0x25, 0x1, 0xE)
    OP_29(0x25, 0x1, 0xF)
    OP_29(0x25, 0x1, 0x10)
    OP_29(0x25, 0x1, 0x11)
    OP_29(0x25, 0x1, 0x12)
    OP_29(0x25, 0x1, 0x13)
    OP_29(0x25, 0x1, 0x14)
    OP_29(0x25, 0x1, 0x15)
    OP_29(0x25, 0x1, 0x16)
    OP_29(0x25, 0x1, 0x17)
    OP_29(0x25, 0x1, 0x18)
    OP_29(0x25, 0x1, 0x19)
    OP_29(0x25, 0x1, 0x1A)
    OP_29(0x25, 0x1, 0x1B)
    OP_29(0x25, 0x1, 0x1C)
    OP_29(0x25, 0x1, 0x1D)
    OP_29(0x25, 0x1, 0x1E)
    OP_29(0x25, 0x1, 0x1F)
    OP_29(0x26, 0x1, 0x0)
    OP_29(0x26, 0x1, 0x1)
    OP_29(0x26, 0x1, 0x2)
    OP_29(0x26, 0x1, 0x3)
    OP_29(0x26, 0x1, 0x4)
    OP_29(0x26, 0x1, 0x5)
    OP_29(0x26, 0x1, 0x6)
    OP_29(0x26, 0x1, 0x7)
    OP_29(0x26, 0x1, 0x8)
    OP_29(0x26, 0x1, 0x9)
    OP_29(0x26, 0x1, 0xA)
    OP_29(0x26, 0x1, 0xB)
    OP_29(0x26, 0x1, 0xC)
    OP_29(0x26, 0x1, 0xD)
    OP_29(0x26, 0x1, 0xE)
    OP_29(0x26, 0x1, 0xF)
    OP_29(0x26, 0x1, 0x10)
    OP_29(0x26, 0x1, 0x11)
    OP_29(0x26, 0x1, 0x12)
    OP_29(0x26, 0x1, 0x13)
    OP_29(0x26, 0x1, 0x14)
    OP_29(0x26, 0x1, 0x15)
    OP_29(0x26, 0x1, 0x16)
    OP_29(0x26, 0x1, 0x17)
    OP_29(0x26, 0x1, 0x18)
    OP_29(0x26, 0x1, 0x19)
    OP_29(0x26, 0x1, 0x1A)
    OP_29(0x26, 0x1, 0x1B)
    OP_29(0x26, 0x1, 0x1C)
    OP_29(0x26, 0x1, 0x1D)
    OP_29(0x26, 0x1, 0x1E)
    OP_29(0x26, 0x1, 0x1F)
    OP_29(0x27, 0x1, 0x0)
    OP_29(0x27, 0x1, 0x1)
    OP_29(0x27, 0x1, 0x2)
    OP_29(0x27, 0x1, 0x3)
    OP_29(0x27, 0x1, 0x4)
    OP_29(0x27, 0x1, 0x5)
    OP_29(0x27, 0x1, 0x6)
    OP_29(0x27, 0x1, 0x7)
    OP_29(0x27, 0x1, 0x8)
    OP_29(0x27, 0x1, 0x9)
    OP_29(0x27, 0x1, 0xA)
    OP_29(0x27, 0x1, 0xB)
    OP_29(0x27, 0x1, 0xC)
    OP_29(0x27, 0x1, 0xD)
    OP_29(0x27, 0x1, 0xE)
    OP_29(0x27, 0x1, 0xF)
    OP_29(0x27, 0x1, 0x10)
    OP_29(0x27, 0x1, 0x11)
    OP_29(0x27, 0x1, 0x12)
    OP_29(0x27, 0x1, 0x13)
    OP_29(0x27, 0x1, 0x14)
    OP_29(0x27, 0x1, 0x15)
    OP_29(0x27, 0x1, 0x16)
    OP_29(0x27, 0x1, 0x17)
    OP_29(0x27, 0x1, 0x18)
    OP_29(0x27, 0x1, 0x19)
    OP_29(0x27, 0x1, 0x1A)
    OP_29(0x27, 0x1, 0x1B)
    OP_29(0x27, 0x1, 0x1C)
    OP_29(0x27, 0x1, 0x1D)
    OP_29(0x27, 0x1, 0x1E)
    OP_29(0x27, 0x1, 0x1F)
    OP_29(0x28, 0x1, 0x0)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x3)
    OP_29(0x28, 0x1, 0x4)
    OP_29(0x28, 0x1, 0x5)
    OP_29(0x28, 0x1, 0x6)
    OP_29(0x28, 0x1, 0x7)
    OP_29(0x28, 0x1, 0x8)
    OP_29(0x28, 0x1, 0x9)
    OP_29(0x28, 0x1, 0xA)
    OP_29(0x28, 0x1, 0xB)
    OP_29(0x28, 0x1, 0xC)
    OP_29(0x28, 0x1, 0xD)
    OP_29(0x28, 0x1, 0xE)
    OP_29(0x28, 0x1, 0xF)
    OP_29(0x28, 0x1, 0x10)
    OP_29(0x28, 0x1, 0x11)
    OP_29(0x28, 0x1, 0x12)
    OP_29(0x28, 0x1, 0x13)
    OP_29(0x28, 0x1, 0x14)
    OP_29(0x28, 0x1, 0x15)
    OP_29(0x28, 0x1, 0x16)
    OP_29(0x28, 0x1, 0x17)
    OP_29(0x28, 0x1, 0x18)
    OP_29(0x28, 0x1, 0x19)
    OP_29(0x28, 0x1, 0x1A)
    OP_29(0x28, 0x1, 0x1B)
    OP_29(0x28, 0x1, 0x1C)
    OP_29(0x28, 0x1, 0x1D)
    OP_29(0x28, 0x1, 0x1E)
    OP_29(0x28, 0x1, 0x1F)
    OP_29(0x29, 0x1, 0x0)
    OP_29(0x29, 0x1, 0x1)
    OP_29(0x29, 0x1, 0x2)
    OP_29(0x29, 0x1, 0x3)
    OP_29(0x29, 0x1, 0x4)
    OP_29(0x29, 0x1, 0x5)
    OP_29(0x29, 0x1, 0x6)
    OP_29(0x29, 0x1, 0x7)
    OP_29(0x29, 0x1, 0x8)
    OP_29(0x29, 0x1, 0x9)
    OP_29(0x29, 0x1, 0xA)
    OP_29(0x29, 0x1, 0xB)
    OP_29(0x29, 0x1, 0xC)
    OP_29(0x29, 0x1, 0xD)
    OP_29(0x29, 0x1, 0xE)
    OP_29(0x29, 0x1, 0xF)
    OP_29(0x29, 0x1, 0x10)
    OP_29(0x29, 0x1, 0x11)
    OP_29(0x29, 0x1, 0x12)
    OP_29(0x29, 0x1, 0x13)
    OP_29(0x29, 0x1, 0x14)
    OP_29(0x29, 0x1, 0x15)
    OP_29(0x29, 0x1, 0x16)
    OP_29(0x29, 0x1, 0x17)
    OP_29(0x29, 0x1, 0x18)
    OP_29(0x29, 0x1, 0x19)
    OP_29(0x29, 0x1, 0x1A)
    OP_29(0x29, 0x1, 0x1B)
    OP_29(0x29, 0x1, 0x1C)
    OP_29(0x29, 0x1, 0x1D)
    OP_29(0x29, 0x1, 0x1E)
    OP_29(0x29, 0x1, 0x1F)
    OP_29(0x2A, 0x1, 0x0)
    OP_29(0x2A, 0x1, 0x1)
    OP_29(0x2A, 0x1, 0x2)
    OP_29(0x2A, 0x1, 0x3)
    OP_29(0x2A, 0x1, 0x4)
    OP_29(0x2A, 0x1, 0x5)
    OP_29(0x2A, 0x1, 0x6)
    OP_29(0x2A, 0x1, 0x7)
    OP_29(0x2A, 0x1, 0x8)
    OP_29(0x2A, 0x1, 0x9)
    OP_29(0x2A, 0x1, 0xA)
    OP_29(0x2A, 0x1, 0xB)
    OP_29(0x2A, 0x1, 0xC)
    OP_29(0x2A, 0x1, 0xD)
    OP_29(0x2A, 0x1, 0xE)
    OP_29(0x2A, 0x1, 0xF)
    OP_29(0x2A, 0x1, 0x10)
    OP_29(0x2A, 0x1, 0x11)
    OP_29(0x2A, 0x1, 0x12)
    OP_29(0x2A, 0x1, 0x13)
    OP_29(0x2A, 0x1, 0x14)
    OP_29(0x2A, 0x1, 0x15)
    OP_29(0x2A, 0x1, 0x16)
    OP_29(0x2A, 0x1, 0x17)
    OP_29(0x2A, 0x1, 0x18)
    OP_29(0x2A, 0x1, 0x19)
    OP_29(0x2A, 0x1, 0x1A)
    OP_29(0x2A, 0x1, 0x1B)
    OP_29(0x2A, 0x1, 0x1C)
    OP_29(0x2A, 0x1, 0x1D)
    OP_29(0x2A, 0x1, 0x1E)
    OP_29(0x2A, 0x1, 0x1F)
    OP_29(0x2B, 0x1, 0x0)
    OP_29(0x2B, 0x1, 0x1)
    OP_29(0x2B, 0x1, 0x2)
    OP_29(0x2B, 0x1, 0x3)
    OP_29(0x2B, 0x1, 0x4)
    OP_29(0x2B, 0x1, 0x5)
    OP_29(0x2B, 0x1, 0x6)
    OP_29(0x2B, 0x1, 0x7)
    OP_29(0x2B, 0x1, 0x8)
    OP_29(0x2B, 0x1, 0x9)
    OP_29(0x2B, 0x1, 0xA)
    OP_29(0x2B, 0x1, 0xB)
    OP_29(0x2B, 0x1, 0xC)
    OP_29(0x2B, 0x1, 0xD)
    OP_29(0x2B, 0x1, 0xE)
    OP_29(0x2B, 0x1, 0xF)
    OP_29(0x2B, 0x1, 0x10)
    OP_29(0x2B, 0x1, 0x11)
    OP_29(0x2B, 0x1, 0x12)
    OP_29(0x2B, 0x1, 0x13)
    OP_29(0x2B, 0x1, 0x14)
    OP_29(0x2B, 0x1, 0x15)
    OP_29(0x2B, 0x1, 0x16)
    OP_29(0x2B, 0x1, 0x17)
    OP_29(0x2B, 0x1, 0x18)
    OP_29(0x2B, 0x1, 0x19)
    OP_29(0x2B, 0x1, 0x1A)
    OP_29(0x2B, 0x1, 0x1B)
    OP_29(0x2B, 0x1, 0x1C)
    OP_29(0x2B, 0x1, 0x1D)
    OP_29(0x2B, 0x1, 0x1E)
    OP_29(0x2B, 0x1, 0x1F)
    OP_29(0x2C, 0x1, 0x0)
    OP_29(0x2C, 0x1, 0x1)
    OP_29(0x2C, 0x1, 0x2)
    OP_29(0x2C, 0x1, 0x3)
    OP_29(0x2C, 0x1, 0x4)
    OP_29(0x2C, 0x1, 0x5)
    OP_29(0x2C, 0x1, 0x6)
    OP_29(0x2C, 0x1, 0x7)
    OP_29(0x2C, 0x1, 0x8)
    OP_29(0x2C, 0x1, 0x9)
    OP_29(0x2C, 0x1, 0xA)
    OP_29(0x2C, 0x1, 0xB)
    OP_29(0x2C, 0x1, 0xC)
    OP_29(0x2C, 0x1, 0xD)
    OP_29(0x2C, 0x1, 0xE)
    OP_29(0x2C, 0x1, 0xF)
    OP_29(0x2C, 0x1, 0x10)
    OP_29(0x2C, 0x1, 0x11)
    OP_29(0x2C, 0x1, 0x12)
    OP_29(0x2C, 0x1, 0x13)
    OP_29(0x2C, 0x1, 0x14)
    OP_29(0x2C, 0x1, 0x15)
    OP_29(0x2C, 0x1, 0x16)
    OP_29(0x2C, 0x1, 0x17)
    OP_29(0x2C, 0x1, 0x18)
    OP_29(0x2C, 0x1, 0x19)
    OP_29(0x2C, 0x1, 0x1A)
    OP_29(0x2C, 0x1, 0x1B)
    OP_29(0x2C, 0x1, 0x1C)
    OP_29(0x2C, 0x1, 0x1D)
    OP_29(0x2C, 0x1, 0x1E)
    OP_29(0x2C, 0x1, 0x1F)
    OP_29(0x2D, 0x1, 0x0)
    OP_29(0x2D, 0x1, 0x1)
    OP_29(0x2D, 0x1, 0x2)
    OP_29(0x2D, 0x1, 0x3)
    OP_29(0x2D, 0x1, 0x4)
    OP_29(0x2D, 0x1, 0x5)
    OP_29(0x2D, 0x1, 0x6)
    OP_29(0x2D, 0x1, 0x7)
    OP_29(0x2D, 0x1, 0x8)
    OP_29(0x2D, 0x1, 0x9)
    OP_29(0x2D, 0x1, 0xA)
    OP_29(0x2D, 0x1, 0xB)
    OP_29(0x2D, 0x1, 0xC)
    OP_29(0x2D, 0x1, 0xD)
    OP_29(0x2D, 0x1, 0xE)
    OP_29(0x2D, 0x1, 0xF)
    OP_29(0x2D, 0x1, 0x10)
    OP_29(0x2D, 0x1, 0x11)
    OP_29(0x2D, 0x1, 0x12)
    OP_29(0x2D, 0x1, 0x13)
    OP_29(0x2D, 0x1, 0x14)
    OP_29(0x2D, 0x1, 0x15)
    OP_29(0x2D, 0x1, 0x16)
    OP_29(0x2D, 0x1, 0x17)
    OP_29(0x2D, 0x1, 0x18)
    OP_29(0x2D, 0x1, 0x19)
    OP_29(0x2D, 0x1, 0x1A)
    OP_29(0x2D, 0x1, 0x1B)
    OP_29(0x2D, 0x1, 0x1C)
    OP_29(0x2D, 0x1, 0x1D)
    OP_29(0x2D, 0x1, 0x1E)
    OP_29(0x2D, 0x1, 0x1F)
    OP_29(0x2E, 0x1, 0x0)
    OP_29(0x2E, 0x1, 0x1)
    OP_29(0x2E, 0x1, 0x2)
    OP_29(0x2E, 0x1, 0x3)
    OP_29(0x2E, 0x1, 0x4)
    OP_29(0x2E, 0x1, 0x5)
    OP_29(0x2E, 0x1, 0x6)
    OP_29(0x2E, 0x1, 0x7)
    OP_29(0x2E, 0x1, 0x8)
    OP_29(0x2E, 0x1, 0x9)
    OP_29(0x2E, 0x1, 0xA)
    OP_29(0x2E, 0x1, 0xB)
    OP_29(0x2E, 0x1, 0xC)
    OP_29(0x2E, 0x1, 0xD)
    OP_29(0x2E, 0x1, 0xE)
    OP_29(0x2E, 0x1, 0xF)
    OP_29(0x2E, 0x1, 0x10)
    OP_29(0x2E, 0x1, 0x11)
    OP_29(0x2E, 0x1, 0x12)
    OP_29(0x2E, 0x1, 0x13)
    OP_29(0x2E, 0x1, 0x14)
    OP_29(0x2E, 0x1, 0x15)
    OP_29(0x2E, 0x1, 0x16)
    OP_29(0x2E, 0x1, 0x17)
    OP_29(0x2E, 0x1, 0x18)
    OP_29(0x2E, 0x1, 0x19)
    OP_29(0x2E, 0x1, 0x1A)
    OP_29(0x2E, 0x1, 0x1B)
    OP_29(0x2E, 0x1, 0x1C)
    OP_29(0x2E, 0x1, 0x1D)
    OP_29(0x2E, 0x1, 0x1E)
    OP_29(0x2E, 0x1, 0x1F)
    OP_29(0x2F, 0x1, 0x0)
    OP_29(0x2F, 0x1, 0x1)
    OP_29(0x2F, 0x1, 0x2)
    OP_29(0x2F, 0x1, 0x3)
    OP_29(0x2F, 0x1, 0x4)
    OP_29(0x2F, 0x1, 0x5)
    OP_29(0x2F, 0x1, 0x6)
    OP_29(0x2F, 0x1, 0x7)
    OP_29(0x2F, 0x1, 0x8)
    OP_29(0x2F, 0x1, 0x9)
    OP_29(0x2F, 0x1, 0xA)
    OP_29(0x2F, 0x1, 0xB)
    OP_29(0x2F, 0x1, 0xC)
    OP_29(0x2F, 0x1, 0xD)
    OP_29(0x2F, 0x1, 0xE)
    OP_29(0x2F, 0x1, 0xF)
    OP_29(0x2F, 0x1, 0x10)
    OP_29(0x2F, 0x1, 0x11)
    OP_29(0x2F, 0x1, 0x12)
    OP_29(0x2F, 0x1, 0x13)
    OP_29(0x2F, 0x1, 0x14)
    OP_29(0x2F, 0x1, 0x15)
    OP_29(0x2F, 0x1, 0x16)
    OP_29(0x2F, 0x1, 0x17)
    OP_29(0x2F, 0x1, 0x18)
    OP_29(0x2F, 0x1, 0x19)
    OP_29(0x2F, 0x1, 0x1A)
    OP_29(0x2F, 0x1, 0x1B)
    OP_29(0x2F, 0x1, 0x1C)
    OP_29(0x2F, 0x1, 0x1D)
    OP_29(0x2F, 0x1, 0x1E)
    OP_29(0x2F, 0x1, 0x1F)
    OP_29(0x30, 0x1, 0x0)
    OP_29(0x30, 0x1, 0x1)
    OP_29(0x30, 0x1, 0x2)
    OP_29(0x30, 0x1, 0x3)
    OP_29(0x30, 0x1, 0x4)
    OP_29(0x30, 0x1, 0x5)
    OP_29(0x30, 0x1, 0x6)
    OP_29(0x30, 0x1, 0x7)
    OP_29(0x30, 0x1, 0x8)
    OP_29(0x30, 0x1, 0x9)
    OP_29(0x30, 0x1, 0xA)
    OP_29(0x30, 0x1, 0xB)
    OP_29(0x30, 0x1, 0xC)
    OP_29(0x30, 0x1, 0xD)
    OP_29(0x30, 0x1, 0xE)
    OP_29(0x30, 0x1, 0xF)
    OP_29(0x30, 0x1, 0x10)
    OP_29(0x30, 0x1, 0x11)
    OP_29(0x30, 0x1, 0x12)
    OP_29(0x30, 0x1, 0x13)
    OP_29(0x30, 0x1, 0x14)
    OP_29(0x30, 0x1, 0x15)
    OP_29(0x30, 0x1, 0x16)
    OP_29(0x30, 0x1, 0x17)
    OP_29(0x30, 0x1, 0x18)
    OP_29(0x30, 0x1, 0x19)
    OP_29(0x30, 0x1, 0x1A)
    OP_29(0x30, 0x1, 0x1B)
    OP_29(0x30, 0x1, 0x1C)
    OP_29(0x30, 0x1, 0x1D)
    OP_29(0x30, 0x1, 0x1E)
    OP_29(0x30, 0x1, 0x1F)
    OP_29(0x31, 0x1, 0x0)
    OP_29(0x31, 0x1, 0x1)
    OP_29(0x31, 0x1, 0x2)
    OP_29(0x31, 0x1, 0x3)
    OP_29(0x31, 0x1, 0x4)
    OP_29(0x31, 0x1, 0x5)
    OP_29(0x31, 0x1, 0x6)
    OP_29(0x31, 0x1, 0x7)
    OP_29(0x31, 0x1, 0x8)
    OP_29(0x31, 0x1, 0x9)
    OP_29(0x31, 0x1, 0xA)
    OP_29(0x31, 0x1, 0xB)
    OP_29(0x31, 0x1, 0xC)
    OP_29(0x31, 0x1, 0xD)
    OP_29(0x31, 0x1, 0xE)
    OP_29(0x31, 0x1, 0xF)
    OP_29(0x31, 0x1, 0x10)
    OP_29(0x31, 0x1, 0x11)
    OP_29(0x31, 0x1, 0x12)
    OP_29(0x31, 0x1, 0x13)
    OP_29(0x31, 0x1, 0x14)
    OP_29(0x31, 0x1, 0x15)
    OP_29(0x31, 0x1, 0x16)
    OP_29(0x31, 0x1, 0x17)
    OP_29(0x31, 0x1, 0x18)
    OP_29(0x31, 0x1, 0x19)
    OP_29(0x31, 0x1, 0x1A)
    OP_29(0x31, 0x1, 0x1B)
    OP_29(0x31, 0x1, 0x1C)
    OP_29(0x31, 0x1, 0x1D)
    OP_29(0x31, 0x1, 0x1E)
    OP_29(0x31, 0x1, 0x1F)
    OP_29(0x32, 0x1, 0x0)
    OP_29(0x32, 0x1, 0x1)
    OP_29(0x32, 0x1, 0x2)
    OP_29(0x32, 0x1, 0x3)
    OP_29(0x32, 0x1, 0x4)
    OP_29(0x32, 0x1, 0x5)
    OP_29(0x32, 0x1, 0x6)
    OP_29(0x32, 0x1, 0x7)
    OP_29(0x32, 0x1, 0x8)
    OP_29(0x32, 0x1, 0x9)
    OP_29(0x32, 0x1, 0xA)
    OP_29(0x32, 0x1, 0xB)
    OP_29(0x32, 0x1, 0xC)
    OP_29(0x32, 0x1, 0xD)
    OP_29(0x32, 0x1, 0xE)
    OP_29(0x32, 0x1, 0xF)
    OP_29(0x32, 0x1, 0x10)
    OP_29(0x32, 0x1, 0x11)
    OP_29(0x32, 0x1, 0x12)
    OP_29(0x32, 0x1, 0x13)
    OP_29(0x32, 0x1, 0x14)
    OP_29(0x32, 0x1, 0x15)
    OP_29(0x32, 0x1, 0x16)
    OP_29(0x32, 0x1, 0x17)
    OP_29(0x32, 0x1, 0x18)
    OP_29(0x32, 0x1, 0x19)
    OP_29(0x32, 0x1, 0x1A)
    OP_29(0x32, 0x1, 0x1B)
    OP_29(0x32, 0x1, 0x1C)
    OP_29(0x32, 0x1, 0x1D)
    OP_29(0x32, 0x1, 0x1E)
    OP_29(0x32, 0x1, 0x1F)
    OP_29(0x33, 0x1, 0x0)
    OP_29(0x33, 0x1, 0x1)
    OP_29(0x33, 0x1, 0x2)
    OP_29(0x33, 0x1, 0x3)
    OP_29(0x33, 0x1, 0x4)
    OP_29(0x33, 0x1, 0x5)
    OP_29(0x33, 0x1, 0x6)
    OP_29(0x33, 0x1, 0x7)
    OP_29(0x33, 0x1, 0x8)
    OP_29(0x33, 0x1, 0x9)
    OP_29(0x33, 0x1, 0xA)
    OP_29(0x33, 0x1, 0xB)
    OP_29(0x33, 0x1, 0xC)
    OP_29(0x33, 0x1, 0xD)
    OP_29(0x33, 0x1, 0xE)
    OP_29(0x33, 0x1, 0xF)
    OP_29(0x33, 0x1, 0x10)
    OP_29(0x33, 0x1, 0x11)
    OP_29(0x33, 0x1, 0x12)
    OP_29(0x33, 0x1, 0x13)
    OP_29(0x33, 0x1, 0x14)
    OP_29(0x33, 0x1, 0x15)
    OP_29(0x33, 0x1, 0x16)
    OP_29(0x33, 0x1, 0x17)
    OP_29(0x33, 0x1, 0x18)
    OP_29(0x33, 0x1, 0x19)
    OP_29(0x33, 0x1, 0x1A)
    OP_29(0x33, 0x1, 0x1B)
    OP_29(0x33, 0x1, 0x1C)
    OP_29(0x33, 0x1, 0x1D)
    OP_29(0x33, 0x1, 0x1E)
    OP_29(0x33, 0x1, 0x1F)
    OP_29(0x34, 0x1, 0x0)
    OP_29(0x34, 0x1, 0x1)
    OP_29(0x34, 0x1, 0x2)
    OP_29(0x34, 0x1, 0x3)
    OP_29(0x34, 0x1, 0x4)
    OP_29(0x34, 0x1, 0x5)
    OP_29(0x34, 0x1, 0x6)
    OP_29(0x34, 0x1, 0x7)
    OP_29(0x34, 0x1, 0x8)
    OP_29(0x34, 0x1, 0x9)
    OP_29(0x34, 0x1, 0xA)
    OP_29(0x34, 0x1, 0xB)
    OP_29(0x34, 0x1, 0xC)
    OP_29(0x34, 0x1, 0xD)
    OP_29(0x34, 0x1, 0xE)
    OP_29(0x34, 0x1, 0xF)
    OP_29(0x34, 0x1, 0x10)
    OP_29(0x34, 0x1, 0x11)
    OP_29(0x34, 0x1, 0x12)
    OP_29(0x34, 0x1, 0x13)
    OP_29(0x34, 0x1, 0x14)
    OP_29(0x34, 0x1, 0x15)
    OP_29(0x34, 0x1, 0x16)
    OP_29(0x34, 0x1, 0x17)
    OP_29(0x34, 0x1, 0x18)
    OP_29(0x34, 0x1, 0x19)
    OP_29(0x34, 0x1, 0x1A)
    OP_29(0x34, 0x1, 0x1B)
    OP_29(0x34, 0x1, 0x1C)
    OP_29(0x34, 0x1, 0x1D)
    OP_29(0x34, 0x1, 0x1E)
    OP_29(0x34, 0x1, 0x1F)
    Jump("loc_BBA8")

    label("loc_BB99")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BBA8")

    label("loc_BBA8")

    Jump("loc_7D8F")

    label("loc_BBAD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_54_7D85 end

    def Function_55_BBBB(): pass

    label("Function_55_BBBB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BBC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB46")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "-- Prologue --\x01",                                     # 0
            "QS_0001 - Get Combat Notebook\x01",                      # 1
            "QS_0002 - Search for Lost Item\x01",                     # 2
            "QS_0003 - Confirm Absent Resident\x01",                  # 3
            "QS_0004 - Michel's Challenge\x01",                       # 4
            "QS_0005 - Prepare Monsters ①\x01",                      # 5
            "-- Chapter 1 --\x01",                                    # 6
            "QS_0101 - Overdue Book Retrieval\x01",                   # 7
            "QS_0102 - Hunting for Ingredients\x01",                  # 8
            "QS_0103 - Assistance With New Service\x01",              # 9
            "QS_0104 - Search for the Kitten's Owner\x01",            # 10
            "QS_0105 - Assistance With Imperial Inspection\x01",      # 11
            "QS_0106 - Abandoned Apartment Monster Cleanup\x01",      # 12
            "QS_0107 - Prepare Monsters ②\x01",                      # 13
            "QS_0108 - We Long for Mishy\x01",                        # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_BE18"),
        (2, "loc_BE18"),
        (3, "loc_BE18"),
        (4, "loc_BE18"),
        (5, "loc_BE18"),
        (7, "loc_BE18"),
        (8, "loc_BE18"),
        (9, "loc_BE18"),
        (10, "loc_BE18"),
        (11, "loc_BE18"),
        (12, "loc_BE18"),
        (13, "loc_BE18"),
        (14, "loc_BE18"),
        (SWITCH_DEFAULT, "loc_BE97"),
    )


    label("loc_BE18")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",         # 0
            "Start\x01",         # 1
            "QF_01\x01",         # 2
            "QF_02\x01",         # 3
            "QF_03\x01",         # 4
            "QF_04\x01",         # 5
            "QF_05\x01",         # 6
            "QF_06\x01",         # 7
            "QF_07\x01",         # 8
            "QF_08\x01",         # 9
            "QF_09\x01",         # 10
            "QF_10\x01",         # 11
            "QF_11\x01",         # 12
            "QF_12\x01",         # 13
            "Complete\x01",      # 14
            "Report\x01",        # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_BEA6")

    label("loc_BE97")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BEA6")

    label("loc_BEA6")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB41")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_BF10"),
        (2, "loc_C149"),
        (3, "loc_C373"),
        (4, "loc_C59D"),
        (5, "loc_C7C7"),
        (7, "loc_C9F1"),
        (8, "loc_CC1B"),
        (9, "loc_CE45"),
        (10, "loc_D06F"),
        (11, "loc_D299"),
        (12, "loc_D4C3"),
        (13, "loc_D6ED"),
        (14, "loc_D917"),
        (SWITCH_DEFAULT, "loc_DB41"),
    )


    label("loc_BF10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C000")
    OP_29(0x1, 0x3, 0x0)
    OP_29(0x1, 0x3, 0x1)
    OP_29(0x1, 0x3, 0x2)
    OP_29(0x1, 0x3, 0x10)
    OP_29(0x1, 0x3, 0x20)
    OP_29(0x1, 0x3, 0x40)
    OP_29(0x1, 0x2, 0x0)
    OP_29(0x1, 0x2, 0x1)
    OP_29(0x1, 0x2, 0x2)
    OP_29(0x1, 0x2, 0x3)
    OP_29(0x1, 0x2, 0x4)
    OP_29(0x1, 0x2, 0x5)
    OP_29(0x1, 0x2, 0x6)
    OP_29(0x1, 0x2, 0x7)
    OP_29(0x1, 0x2, 0x8)
    OP_29(0x1, 0x2, 0x9)
    OP_29(0x1, 0x2, 0xA)
    OP_29(0x1, 0x2, 0xB)
    OP_29(0x1, 0x2, 0xC)
    OP_29(0x1, 0x2, 0xD)
    OP_29(0x1, 0x2, 0xE)
    OP_29(0x1, 0x2, 0xF)
    OP_29(0x1, 0x2, 0x10)
    OP_29(0x1, 0x2, 0x11)
    OP_29(0x1, 0x2, 0x12)
    OP_29(0x1, 0x2, 0x13)
    OP_29(0x1, 0x2, 0x14)
    OP_29(0x1, 0x2, 0x15)
    OP_29(0x1, 0x2, 0x16)
    OP_29(0x1, 0x2, 0x17)
    OP_29(0x1, 0x2, 0x18)
    OP_29(0x1, 0x2, 0x19)
    OP_29(0x1, 0x2, 0x1A)
    OP_29(0x1, 0x2, 0x1B)
    OP_29(0x1, 0x2, 0x1C)
    OP_29(0x1, 0x2, 0x1D)
    OP_29(0x1, 0x2, 0x1E)
    OP_29(0x1, 0x2, 0x1F)
    ClearScenarioFlags(0x50, 1)

    label("loc_C000")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C014")
    OP_29(0x1, 0x4, 0x2)

    label("loc_C014")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C029")
    OP_29(0x1, 0x1, 0x0)

    label("loc_C029")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C03E")
    OP_29(0x1, 0x1, 0x1)

    label("loc_C03E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C053")
    OP_29(0x1, 0x1, 0x2)

    label("loc_C053")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C068")
    OP_29(0x1, 0x1, 0x3)

    label("loc_C068")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C07D")
    OP_29(0x1, 0x1, 0x4)

    label("loc_C07D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C092")
    OP_29(0x1, 0x1, 0x5)

    label("loc_C092")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0A7")
    OP_29(0x1, 0x1, 0x6)

    label("loc_C0A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0BC")
    OP_29(0x1, 0x1, 0x7)

    label("loc_C0BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0D1")
    OP_29(0x1, 0x1, 0x8)

    label("loc_C0D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0E6")
    OP_29(0x1, 0x1, 0x9)

    label("loc_C0E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0FB")
    OP_29(0x1, 0x1, 0xA)

    label("loc_C0FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C110")
    OP_29(0x1, 0x1, 0xB)

    label("loc_C110")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C130")
    OP_29(0x1, 0x2, 0x0)
    OP_29(0x1, 0x2, 0x1)
    OP_29(0x1, 0x4, 0x10)

    label("loc_C130")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C144")
    OP_29(0x1, 0x4, 0x20)

    label("loc_C144")

    Jump("loc_DB41")

    label("loc_C149")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C236")
    OP_29(0x2, 0x3, 0x0)
    OP_29(0x2, 0x3, 0x1)
    OP_29(0x2, 0x3, 0x2)
    OP_29(0x2, 0x3, 0x10)
    OP_29(0x2, 0x3, 0x20)
    OP_29(0x2, 0x3, 0x40)
    OP_29(0x2, 0x2, 0x0)
    OP_29(0x2, 0x2, 0x1)
    OP_29(0x2, 0x2, 0x2)
    OP_29(0x2, 0x2, 0x3)
    OP_29(0x2, 0x2, 0x4)
    OP_29(0x2, 0x2, 0x5)
    OP_29(0x2, 0x2, 0x6)
    OP_29(0x2, 0x2, 0x7)
    OP_29(0x2, 0x2, 0x8)
    OP_29(0x2, 0x2, 0x9)
    OP_29(0x2, 0x2, 0xA)
    OP_29(0x2, 0x2, 0xB)
    OP_29(0x2, 0x2, 0xC)
    OP_29(0x2, 0x2, 0xD)
    OP_29(0x2, 0x2, 0xE)
    OP_29(0x2, 0x2, 0xF)
    OP_29(0x2, 0x2, 0x10)
    OP_29(0x2, 0x2, 0x11)
    OP_29(0x2, 0x2, 0x12)
    OP_29(0x2, 0x2, 0x13)
    OP_29(0x2, 0x2, 0x14)
    OP_29(0x2, 0x2, 0x15)
    OP_29(0x2, 0x2, 0x16)
    OP_29(0x2, 0x2, 0x17)
    OP_29(0x2, 0x2, 0x18)
    OP_29(0x2, 0x2, 0x19)
    OP_29(0x2, 0x2, 0x1A)
    OP_29(0x2, 0x2, 0x1B)
    OP_29(0x2, 0x2, 0x1C)
    OP_29(0x2, 0x2, 0x1D)
    OP_29(0x2, 0x2, 0x1E)
    OP_29(0x2, 0x2, 0x1F)

    label("loc_C236")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C24A")
    OP_29(0x2, 0x4, 0x2)

    label("loc_C24A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C25F")
    OP_29(0x2, 0x1, 0x0)

    label("loc_C25F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C274")
    OP_29(0x2, 0x1, 0x1)

    label("loc_C274")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C289")
    OP_29(0x2, 0x1, 0x2)

    label("loc_C289")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C29E")
    OP_29(0x2, 0x1, 0x3)

    label("loc_C29E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C2B3")
    OP_29(0x2, 0x1, 0x4)

    label("loc_C2B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C2C8")
    OP_29(0x2, 0x1, 0x5)

    label("loc_C2C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C2DD")
    OP_29(0x2, 0x1, 0x6)

    label("loc_C2DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C2F2")
    OP_29(0x2, 0x1, 0x7)

    label("loc_C2F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C307")
    OP_29(0x2, 0x1, 0x8)

    label("loc_C307")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C31C")
    OP_29(0x2, 0x1, 0x9)

    label("loc_C31C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C331")
    OP_29(0x2, 0x1, 0xA)

    label("loc_C331")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C346")
    OP_29(0x2, 0x1, 0xB)

    label("loc_C346")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C35A")
    OP_29(0x2, 0x4, 0x10)

    label("loc_C35A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C36E")
    OP_29(0x2, 0x4, 0x20)

    label("loc_C36E")

    Jump("loc_DB41")

    label("loc_C373")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C460")
    OP_29(0x3, 0x3, 0x0)
    OP_29(0x3, 0x3, 0x1)
    OP_29(0x3, 0x3, 0x2)
    OP_29(0x3, 0x3, 0x10)
    OP_29(0x3, 0x3, 0x20)
    OP_29(0x3, 0x3, 0x40)
    OP_29(0x3, 0x2, 0x0)
    OP_29(0x3, 0x2, 0x1)
    OP_29(0x3, 0x2, 0x2)
    OP_29(0x3, 0x2, 0x3)
    OP_29(0x3, 0x2, 0x4)
    OP_29(0x3, 0x2, 0x5)
    OP_29(0x3, 0x2, 0x6)
    OP_29(0x3, 0x2, 0x7)
    OP_29(0x3, 0x2, 0x8)
    OP_29(0x3, 0x2, 0x9)
    OP_29(0x3, 0x2, 0xA)
    OP_29(0x3, 0x2, 0xB)
    OP_29(0x3, 0x2, 0xC)
    OP_29(0x3, 0x2, 0xD)
    OP_29(0x3, 0x2, 0xE)
    OP_29(0x3, 0x2, 0xF)
    OP_29(0x3, 0x2, 0x10)
    OP_29(0x3, 0x2, 0x11)
    OP_29(0x3, 0x2, 0x12)
    OP_29(0x3, 0x2, 0x13)
    OP_29(0x3, 0x2, 0x14)
    OP_29(0x3, 0x2, 0x15)
    OP_29(0x3, 0x2, 0x16)
    OP_29(0x3, 0x2, 0x17)
    OP_29(0x3, 0x2, 0x18)
    OP_29(0x3, 0x2, 0x19)
    OP_29(0x3, 0x2, 0x1A)
    OP_29(0x3, 0x2, 0x1B)
    OP_29(0x3, 0x2, 0x1C)
    OP_29(0x3, 0x2, 0x1D)
    OP_29(0x3, 0x2, 0x1E)
    OP_29(0x3, 0x2, 0x1F)

    label("loc_C460")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C474")
    OP_29(0x3, 0x4, 0x2)

    label("loc_C474")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C489")
    OP_29(0x3, 0x1, 0x0)

    label("loc_C489")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C49E")
    OP_29(0x3, 0x1, 0x1)

    label("loc_C49E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C4B3")
    OP_29(0x3, 0x1, 0x2)

    label("loc_C4B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C4C8")
    OP_29(0x3, 0x1, 0x3)

    label("loc_C4C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C4DD")
    OP_29(0x3, 0x1, 0x4)

    label("loc_C4DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C4F2")
    OP_29(0x3, 0x1, 0x5)

    label("loc_C4F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C507")
    OP_29(0x3, 0x1, 0x6)

    label("loc_C507")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C51C")
    OP_29(0x3, 0x1, 0x7)

    label("loc_C51C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C531")
    OP_29(0x3, 0x1, 0x8)

    label("loc_C531")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C546")
    OP_29(0x3, 0x1, 0x9)

    label("loc_C546")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C55B")
    OP_29(0x3, 0x1, 0xA)

    label("loc_C55B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C570")
    OP_29(0x3, 0x1, 0xB)

    label("loc_C570")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C584")
    OP_29(0x3, 0x4, 0x10)

    label("loc_C584")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C598")
    OP_29(0x3, 0x4, 0x20)

    label("loc_C598")

    Jump("loc_DB41")

    label("loc_C59D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C68A")
    OP_29(0x4, 0x3, 0x0)
    OP_29(0x4, 0x3, 0x1)
    OP_29(0x4, 0x3, 0x2)
    OP_29(0x4, 0x3, 0x10)
    OP_29(0x4, 0x3, 0x20)
    OP_29(0x4, 0x3, 0x40)
    OP_29(0x4, 0x2, 0x0)
    OP_29(0x4, 0x2, 0x1)
    OP_29(0x4, 0x2, 0x2)
    OP_29(0x4, 0x2, 0x3)
    OP_29(0x4, 0x2, 0x4)
    OP_29(0x4, 0x2, 0x5)
    OP_29(0x4, 0x2, 0x6)
    OP_29(0x4, 0x2, 0x7)
    OP_29(0x4, 0x2, 0x8)
    OP_29(0x4, 0x2, 0x9)
    OP_29(0x4, 0x2, 0xA)
    OP_29(0x4, 0x2, 0xB)
    OP_29(0x4, 0x2, 0xC)
    OP_29(0x4, 0x2, 0xD)
    OP_29(0x4, 0x2, 0xE)
    OP_29(0x4, 0x2, 0xF)
    OP_29(0x4, 0x2, 0x10)
    OP_29(0x4, 0x2, 0x11)
    OP_29(0x4, 0x2, 0x12)
    OP_29(0x4, 0x2, 0x13)
    OP_29(0x4, 0x2, 0x14)
    OP_29(0x4, 0x2, 0x15)
    OP_29(0x4, 0x2, 0x16)
    OP_29(0x4, 0x2, 0x17)
    OP_29(0x4, 0x2, 0x18)
    OP_29(0x4, 0x2, 0x19)
    OP_29(0x4, 0x2, 0x1A)
    OP_29(0x4, 0x2, 0x1B)
    OP_29(0x4, 0x2, 0x1C)
    OP_29(0x4, 0x2, 0x1D)
    OP_29(0x4, 0x2, 0x1E)
    OP_29(0x4, 0x2, 0x1F)

    label("loc_C68A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C69E")
    OP_29(0x4, 0x4, 0x2)

    label("loc_C69E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C6B3")
    OP_29(0x4, 0x1, 0x0)

    label("loc_C6B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C6C8")
    OP_29(0x4, 0x1, 0x1)

    label("loc_C6C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C6DD")
    OP_29(0x4, 0x1, 0x2)

    label("loc_C6DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C6F2")
    OP_29(0x4, 0x1, 0x3)

    label("loc_C6F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C707")
    OP_29(0x4, 0x1, 0x4)

    label("loc_C707")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C71C")
    OP_29(0x4, 0x1, 0x5)

    label("loc_C71C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C731")
    OP_29(0x4, 0x1, 0x6)

    label("loc_C731")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C746")
    OP_29(0x4, 0x1, 0x7)

    label("loc_C746")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C75B")
    OP_29(0x4, 0x1, 0x8)

    label("loc_C75B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C770")
    OP_29(0x4, 0x1, 0x9)

    label("loc_C770")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C785")
    OP_29(0x4, 0x1, 0xA)

    label("loc_C785")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C79A")
    OP_29(0x4, 0x1, 0xB)

    label("loc_C79A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C7AE")
    OP_29(0x4, 0x4, 0x10)

    label("loc_C7AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C7C2")
    OP_29(0x4, 0x4, 0x20)

    label("loc_C7C2")

    Jump("loc_DB41")

    label("loc_C7C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8B4")
    OP_29(0x35, 0x3, 0x0)
    OP_29(0x35, 0x3, 0x1)
    OP_29(0x35, 0x3, 0x2)
    OP_29(0x35, 0x3, 0x10)
    OP_29(0x35, 0x3, 0x20)
    OP_29(0x35, 0x3, 0x40)
    OP_29(0x35, 0x2, 0x0)
    OP_29(0x35, 0x2, 0x1)
    OP_29(0x35, 0x2, 0x2)
    OP_29(0x35, 0x2, 0x3)
    OP_29(0x35, 0x2, 0x4)
    OP_29(0x35, 0x2, 0x5)
    OP_29(0x35, 0x2, 0x6)
    OP_29(0x35, 0x2, 0x7)
    OP_29(0x35, 0x2, 0x8)
    OP_29(0x35, 0x2, 0x9)
    OP_29(0x35, 0x2, 0xA)
    OP_29(0x35, 0x2, 0xB)
    OP_29(0x35, 0x2, 0xC)
    OP_29(0x35, 0x2, 0xD)
    OP_29(0x35, 0x2, 0xE)
    OP_29(0x35, 0x2, 0xF)
    OP_29(0x35, 0x2, 0x10)
    OP_29(0x35, 0x2, 0x11)
    OP_29(0x35, 0x2, 0x12)
    OP_29(0x35, 0x2, 0x13)
    OP_29(0x35, 0x2, 0x14)
    OP_29(0x35, 0x2, 0x15)
    OP_29(0x35, 0x2, 0x16)
    OP_29(0x35, 0x2, 0x17)
    OP_29(0x35, 0x2, 0x18)
    OP_29(0x35, 0x2, 0x19)
    OP_29(0x35, 0x2, 0x1A)
    OP_29(0x35, 0x2, 0x1B)
    OP_29(0x35, 0x2, 0x1C)
    OP_29(0x35, 0x2, 0x1D)
    OP_29(0x35, 0x2, 0x1E)
    OP_29(0x35, 0x2, 0x1F)

    label("loc_C8B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C8C8")
    OP_29(0x35, 0x4, 0x2)

    label("loc_C8C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C8DD")
    OP_29(0x35, 0x1, 0x0)

    label("loc_C8DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C8F2")
    OP_29(0x35, 0x1, 0x1)

    label("loc_C8F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C907")
    OP_29(0x35, 0x1, 0x2)

    label("loc_C907")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C91C")
    OP_29(0x35, 0x1, 0x3)

    label("loc_C91C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C931")
    OP_29(0x35, 0x1, 0x4)

    label("loc_C931")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C946")
    OP_29(0x35, 0x1, 0x5)

    label("loc_C946")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C95B")
    OP_29(0x35, 0x1, 0x6)

    label("loc_C95B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C970")
    OP_29(0x35, 0x1, 0x7)

    label("loc_C970")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C985")
    OP_29(0x35, 0x1, 0x8)

    label("loc_C985")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C99A")
    OP_29(0x35, 0x1, 0x9)

    label("loc_C99A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C9AF")
    OP_29(0x35, 0x1, 0xA)

    label("loc_C9AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C9C4")
    OP_29(0x35, 0x1, 0xB)

    label("loc_C9C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C9D8")
    OP_29(0x35, 0x4, 0x10)

    label("loc_C9D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C9EC")
    OP_29(0x35, 0x4, 0x20)

    label("loc_C9EC")

    Jump("loc_DB41")

    label("loc_C9F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CADE")
    OP_29(0x5, 0x3, 0x0)
    OP_29(0x5, 0x3, 0x1)
    OP_29(0x5, 0x3, 0x2)
    OP_29(0x5, 0x3, 0x10)
    OP_29(0x5, 0x3, 0x20)
    OP_29(0x5, 0x3, 0x40)
    OP_29(0x5, 0x2, 0x0)
    OP_29(0x5, 0x2, 0x1)
    OP_29(0x5, 0x2, 0x2)
    OP_29(0x5, 0x2, 0x3)
    OP_29(0x5, 0x2, 0x4)
    OP_29(0x5, 0x2, 0x5)
    OP_29(0x5, 0x2, 0x6)
    OP_29(0x5, 0x2, 0x7)
    OP_29(0x5, 0x2, 0x8)
    OP_29(0x5, 0x2, 0x9)
    OP_29(0x5, 0x2, 0xA)
    OP_29(0x5, 0x2, 0xB)
    OP_29(0x5, 0x2, 0xC)
    OP_29(0x5, 0x2, 0xD)
    OP_29(0x5, 0x2, 0xE)
    OP_29(0x5, 0x2, 0xF)
    OP_29(0x5, 0x2, 0x10)
    OP_29(0x5, 0x2, 0x11)
    OP_29(0x5, 0x2, 0x12)
    OP_29(0x5, 0x2, 0x13)
    OP_29(0x5, 0x2, 0x14)
    OP_29(0x5, 0x2, 0x15)
    OP_29(0x5, 0x2, 0x16)
    OP_29(0x5, 0x2, 0x17)
    OP_29(0x5, 0x2, 0x18)
    OP_29(0x5, 0x2, 0x19)
    OP_29(0x5, 0x2, 0x1A)
    OP_29(0x5, 0x2, 0x1B)
    OP_29(0x5, 0x2, 0x1C)
    OP_29(0x5, 0x2, 0x1D)
    OP_29(0x5, 0x2, 0x1E)
    OP_29(0x5, 0x2, 0x1F)

    label("loc_CADE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CAF2")
    OP_29(0x5, 0x4, 0x2)

    label("loc_CAF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB07")
    OP_29(0x5, 0x1, 0x0)

    label("loc_CB07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB1C")
    OP_29(0x5, 0x1, 0x1)

    label("loc_CB1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB31")
    OP_29(0x5, 0x1, 0x2)

    label("loc_CB31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB46")
    OP_29(0x5, 0x1, 0x3)

    label("loc_CB46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB5B")
    OP_29(0x5, 0x1, 0x4)

    label("loc_CB5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB70")
    OP_29(0x5, 0x1, 0x5)

    label("loc_CB70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB85")
    OP_29(0x5, 0x1, 0x6)

    label("loc_CB85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB9A")
    OP_29(0x5, 0x1, 0x7)

    label("loc_CB9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CBAF")
    OP_29(0x5, 0x1, 0x8)

    label("loc_CBAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CBC4")
    OP_29(0x5, 0x1, 0x9)

    label("loc_CBC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CBD9")
    OP_29(0x5, 0x1, 0xA)

    label("loc_CBD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CBEE")
    OP_29(0x5, 0x1, 0xB)

    label("loc_CBEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC02")
    OP_29(0x5, 0x4, 0x10)

    label("loc_CC02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC16")
    OP_29(0x5, 0x4, 0x20)

    label("loc_CC16")

    Jump("loc_DB41")

    label("loc_CC1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD08")
    OP_29(0x6, 0x3, 0x0)
    OP_29(0x6, 0x3, 0x1)
    OP_29(0x6, 0x3, 0x2)
    OP_29(0x6, 0x3, 0x10)
    OP_29(0x6, 0x3, 0x20)
    OP_29(0x6, 0x3, 0x40)
    OP_29(0x6, 0x2, 0x0)
    OP_29(0x6, 0x2, 0x1)
    OP_29(0x6, 0x2, 0x2)
    OP_29(0x6, 0x2, 0x3)
    OP_29(0x6, 0x2, 0x4)
    OP_29(0x6, 0x2, 0x5)
    OP_29(0x6, 0x2, 0x6)
    OP_29(0x6, 0x2, 0x7)
    OP_29(0x6, 0x2, 0x8)
    OP_29(0x6, 0x2, 0x9)
    OP_29(0x6, 0x2, 0xA)
    OP_29(0x6, 0x2, 0xB)
    OP_29(0x6, 0x2, 0xC)
    OP_29(0x6, 0x2, 0xD)
    OP_29(0x6, 0x2, 0xE)
    OP_29(0x6, 0x2, 0xF)
    OP_29(0x6, 0x2, 0x10)
    OP_29(0x6, 0x2, 0x11)
    OP_29(0x6, 0x2, 0x12)
    OP_29(0x6, 0x2, 0x13)
    OP_29(0x6, 0x2, 0x14)
    OP_29(0x6, 0x2, 0x15)
    OP_29(0x6, 0x2, 0x16)
    OP_29(0x6, 0x2, 0x17)
    OP_29(0x6, 0x2, 0x18)
    OP_29(0x6, 0x2, 0x19)
    OP_29(0x6, 0x2, 0x1A)
    OP_29(0x6, 0x2, 0x1B)
    OP_29(0x6, 0x2, 0x1C)
    OP_29(0x6, 0x2, 0x1D)
    OP_29(0x6, 0x2, 0x1E)
    OP_29(0x6, 0x2, 0x1F)

    label("loc_CD08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CD1C")
    OP_29(0x6, 0x4, 0x2)

    label("loc_CD1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CD31")
    OP_29(0x6, 0x1, 0x0)

    label("loc_CD31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CD46")
    OP_29(0x6, 0x1, 0x1)

    label("loc_CD46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CD5B")
    OP_29(0x6, 0x1, 0x2)

    label("loc_CD5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CD70")
    OP_29(0x6, 0x1, 0x3)

    label("loc_CD70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CD85")
    OP_29(0x6, 0x1, 0x4)

    label("loc_CD85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CD9A")
    OP_29(0x6, 0x1, 0x5)

    label("loc_CD9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDAF")
    OP_29(0x6, 0x1, 0x6)

    label("loc_CDAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDC4")
    OP_29(0x6, 0x1, 0x7)

    label("loc_CDC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDD9")
    OP_29(0x6, 0x1, 0x8)

    label("loc_CDD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDEE")
    OP_29(0x6, 0x1, 0x9)

    label("loc_CDEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE03")
    OP_29(0x6, 0x1, 0xA)

    label("loc_CE03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE18")
    OP_29(0x6, 0x1, 0xB)

    label("loc_CE18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE2C")
    OP_29(0x6, 0x4, 0x10)

    label("loc_CE2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE40")
    OP_29(0x6, 0x4, 0x20)

    label("loc_CE40")

    Jump("loc_DB41")

    label("loc_CE45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF32")
    OP_29(0x7, 0x3, 0x0)
    OP_29(0x7, 0x3, 0x1)
    OP_29(0x7, 0x3, 0x2)
    OP_29(0x7, 0x3, 0x10)
    OP_29(0x7, 0x3, 0x20)
    OP_29(0x7, 0x3, 0x40)
    OP_29(0x7, 0x2, 0x0)
    OP_29(0x7, 0x2, 0x1)
    OP_29(0x7, 0x2, 0x2)
    OP_29(0x7, 0x2, 0x3)
    OP_29(0x7, 0x2, 0x4)
    OP_29(0x7, 0x2, 0x5)
    OP_29(0x7, 0x2, 0x6)
    OP_29(0x7, 0x2, 0x7)
    OP_29(0x7, 0x2, 0x8)
    OP_29(0x7, 0x2, 0x9)
    OP_29(0x7, 0x2, 0xA)
    OP_29(0x7, 0x2, 0xB)
    OP_29(0x7, 0x2, 0xC)
    OP_29(0x7, 0x2, 0xD)
    OP_29(0x7, 0x2, 0xE)
    OP_29(0x7, 0x2, 0xF)
    OP_29(0x7, 0x2, 0x10)
    OP_29(0x7, 0x2, 0x11)
    OP_29(0x7, 0x2, 0x12)
    OP_29(0x7, 0x2, 0x13)
    OP_29(0x7, 0x2, 0x14)
    OP_29(0x7, 0x2, 0x15)
    OP_29(0x7, 0x2, 0x16)
    OP_29(0x7, 0x2, 0x17)
    OP_29(0x7, 0x2, 0x18)
    OP_29(0x7, 0x2, 0x19)
    OP_29(0x7, 0x2, 0x1A)
    OP_29(0x7, 0x2, 0x1B)
    OP_29(0x7, 0x2, 0x1C)
    OP_29(0x7, 0x2, 0x1D)
    OP_29(0x7, 0x2, 0x1E)
    OP_29(0x7, 0x2, 0x1F)

    label("loc_CF32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CF46")
    OP_29(0x7, 0x4, 0x2)

    label("loc_CF46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CF5B")
    OP_29(0x7, 0x1, 0x0)

    label("loc_CF5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CF70")
    OP_29(0x7, 0x1, 0x1)

    label("loc_CF70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CF85")
    OP_29(0x7, 0x1, 0x2)

    label("loc_CF85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CF9A")
    OP_29(0x7, 0x1, 0x3)

    label("loc_CF9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFAF")
    OP_29(0x7, 0x1, 0x4)

    label("loc_CFAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFC4")
    OP_29(0x7, 0x1, 0x5)

    label("loc_CFC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFD9")
    OP_29(0x7, 0x1, 0x6)

    label("loc_CFD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFEE")
    OP_29(0x7, 0x1, 0x7)

    label("loc_CFEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D003")
    OP_29(0x7, 0x1, 0x8)

    label("loc_D003")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D018")
    OP_29(0x7, 0x1, 0x9)

    label("loc_D018")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D02D")
    OP_29(0x7, 0x1, 0xA)

    label("loc_D02D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D042")
    OP_29(0x7, 0x1, 0xB)

    label("loc_D042")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D056")
    OP_29(0x7, 0x4, 0x10)

    label("loc_D056")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D06A")
    OP_29(0x7, 0x4, 0x20)

    label("loc_D06A")

    Jump("loc_DB41")

    label("loc_D06F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D15C")
    OP_29(0x8, 0x3, 0x0)
    OP_29(0x8, 0x3, 0x1)
    OP_29(0x8, 0x3, 0x2)
    OP_29(0x8, 0x3, 0x10)
    OP_29(0x8, 0x3, 0x20)
    OP_29(0x8, 0x3, 0x40)
    OP_29(0x8, 0x2, 0x0)
    OP_29(0x8, 0x2, 0x1)
    OP_29(0x8, 0x2, 0x2)
    OP_29(0x8, 0x2, 0x3)
    OP_29(0x8, 0x2, 0x4)
    OP_29(0x8, 0x2, 0x5)
    OP_29(0x8, 0x2, 0x6)
    OP_29(0x8, 0x2, 0x7)
    OP_29(0x8, 0x2, 0x8)
    OP_29(0x8, 0x2, 0x9)
    OP_29(0x8, 0x2, 0xA)
    OP_29(0x8, 0x2, 0xB)
    OP_29(0x8, 0x2, 0xC)
    OP_29(0x8, 0x2, 0xD)
    OP_29(0x8, 0x2, 0xE)
    OP_29(0x8, 0x2, 0xF)
    OP_29(0x8, 0x2, 0x10)
    OP_29(0x8, 0x2, 0x11)
    OP_29(0x8, 0x2, 0x12)
    OP_29(0x8, 0x2, 0x13)
    OP_29(0x8, 0x2, 0x14)
    OP_29(0x8, 0x2, 0x15)
    OP_29(0x8, 0x2, 0x16)
    OP_29(0x8, 0x2, 0x17)
    OP_29(0x8, 0x2, 0x18)
    OP_29(0x8, 0x2, 0x19)
    OP_29(0x8, 0x2, 0x1A)
    OP_29(0x8, 0x2, 0x1B)
    OP_29(0x8, 0x2, 0x1C)
    OP_29(0x8, 0x2, 0x1D)
    OP_29(0x8, 0x2, 0x1E)
    OP_29(0x8, 0x2, 0x1F)

    label("loc_D15C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D170")
    OP_29(0x8, 0x4, 0x2)

    label("loc_D170")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D185")
    OP_29(0x8, 0x1, 0x0)

    label("loc_D185")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D19A")
    OP_29(0x8, 0x1, 0x1)

    label("loc_D19A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D1AF")
    OP_29(0x8, 0x1, 0x2)

    label("loc_D1AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D1C4")
    OP_29(0x8, 0x1, 0x3)

    label("loc_D1C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D1D9")
    OP_29(0x8, 0x1, 0x4)

    label("loc_D1D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D1EE")
    OP_29(0x8, 0x1, 0x5)

    label("loc_D1EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D203")
    OP_29(0x8, 0x1, 0x6)

    label("loc_D203")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D218")
    OP_29(0x8, 0x1, 0x7)

    label("loc_D218")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D22D")
    OP_29(0x8, 0x1, 0x8)

    label("loc_D22D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D242")
    OP_29(0x8, 0x1, 0x9)

    label("loc_D242")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D257")
    OP_29(0x8, 0x1, 0xA)

    label("loc_D257")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D26C")
    OP_29(0x8, 0x1, 0xB)

    label("loc_D26C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D280")
    OP_29(0x8, 0x4, 0x10)

    label("loc_D280")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D294")
    OP_29(0x8, 0x4, 0x20)

    label("loc_D294")

    Jump("loc_DB41")

    label("loc_D299")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D386")
    OP_29(0x9, 0x3, 0x0)
    OP_29(0x9, 0x3, 0x1)
    OP_29(0x9, 0x3, 0x2)
    OP_29(0x9, 0x3, 0x10)
    OP_29(0x9, 0x3, 0x20)
    OP_29(0x9, 0x3, 0x40)
    OP_29(0x9, 0x2, 0x0)
    OP_29(0x9, 0x2, 0x1)
    OP_29(0x9, 0x2, 0x2)
    OP_29(0x9, 0x2, 0x3)
    OP_29(0x9, 0x2, 0x4)
    OP_29(0x9, 0x2, 0x5)
    OP_29(0x9, 0x2, 0x6)
    OP_29(0x9, 0x2, 0x7)
    OP_29(0x9, 0x2, 0x8)
    OP_29(0x9, 0x2, 0x9)
    OP_29(0x9, 0x2, 0xA)
    OP_29(0x9, 0x2, 0xB)
    OP_29(0x9, 0x2, 0xC)
    OP_29(0x9, 0x2, 0xD)
    OP_29(0x9, 0x2, 0xE)
    OP_29(0x9, 0x2, 0xF)
    OP_29(0x9, 0x2, 0x10)
    OP_29(0x9, 0x2, 0x11)
    OP_29(0x9, 0x2, 0x12)
    OP_29(0x9, 0x2, 0x13)
    OP_29(0x9, 0x2, 0x14)
    OP_29(0x9, 0x2, 0x15)
    OP_29(0x9, 0x2, 0x16)
    OP_29(0x9, 0x2, 0x17)
    OP_29(0x9, 0x2, 0x18)
    OP_29(0x9, 0x2, 0x19)
    OP_29(0x9, 0x2, 0x1A)
    OP_29(0x9, 0x2, 0x1B)
    OP_29(0x9, 0x2, 0x1C)
    OP_29(0x9, 0x2, 0x1D)
    OP_29(0x9, 0x2, 0x1E)
    OP_29(0x9, 0x2, 0x1F)

    label("loc_D386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D39A")
    OP_29(0x9, 0x4, 0x2)

    label("loc_D39A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D3AF")
    OP_29(0x9, 0x1, 0x0)

    label("loc_D3AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D3C4")
    OP_29(0x9, 0x1, 0x1)

    label("loc_D3C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D3D9")
    OP_29(0x9, 0x1, 0x2)

    label("loc_D3D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D3EE")
    OP_29(0x9, 0x1, 0x3)

    label("loc_D3EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D403")
    OP_29(0x9, 0x1, 0x4)

    label("loc_D403")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D418")
    OP_29(0x9, 0x1, 0x5)

    label("loc_D418")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D42D")
    OP_29(0x9, 0x1, 0x6)

    label("loc_D42D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D442")
    OP_29(0x9, 0x1, 0x7)

    label("loc_D442")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D457")
    OP_29(0x9, 0x1, 0x8)

    label("loc_D457")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D46C")
    OP_29(0x9, 0x1, 0x9)

    label("loc_D46C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D481")
    OP_29(0x9, 0x1, 0xA)

    label("loc_D481")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D496")
    OP_29(0x9, 0x1, 0xB)

    label("loc_D496")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D4AA")
    OP_29(0x9, 0x4, 0x10)

    label("loc_D4AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D4BE")
    OP_29(0x9, 0x4, 0x20)

    label("loc_D4BE")

    Jump("loc_DB41")

    label("loc_D4C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5B0")
    OP_29(0xA, 0x3, 0x0)
    OP_29(0xA, 0x3, 0x1)
    OP_29(0xA, 0x3, 0x2)
    OP_29(0xA, 0x3, 0x10)
    OP_29(0xA, 0x3, 0x20)
    OP_29(0xA, 0x3, 0x40)
    OP_29(0xA, 0x2, 0x0)
    OP_29(0xA, 0x2, 0x1)
    OP_29(0xA, 0x2, 0x2)
    OP_29(0xA, 0x2, 0x3)
    OP_29(0xA, 0x2, 0x4)
    OP_29(0xA, 0x2, 0x5)
    OP_29(0xA, 0x2, 0x6)
    OP_29(0xA, 0x2, 0x7)
    OP_29(0xA, 0x2, 0x8)
    OP_29(0xA, 0x2, 0x9)
    OP_29(0xA, 0x2, 0xA)
    OP_29(0xA, 0x2, 0xB)
    OP_29(0xA, 0x2, 0xC)
    OP_29(0xA, 0x2, 0xD)
    OP_29(0xA, 0x2, 0xE)
    OP_29(0xA, 0x2, 0xF)
    OP_29(0xA, 0x2, 0x10)
    OP_29(0xA, 0x2, 0x11)
    OP_29(0xA, 0x2, 0x12)
    OP_29(0xA, 0x2, 0x13)
    OP_29(0xA, 0x2, 0x14)
    OP_29(0xA, 0x2, 0x15)
    OP_29(0xA, 0x2, 0x16)
    OP_29(0xA, 0x2, 0x17)
    OP_29(0xA, 0x2, 0x18)
    OP_29(0xA, 0x2, 0x19)
    OP_29(0xA, 0x2, 0x1A)
    OP_29(0xA, 0x2, 0x1B)
    OP_29(0xA, 0x2, 0x1C)
    OP_29(0xA, 0x2, 0x1D)
    OP_29(0xA, 0x2, 0x1E)
    OP_29(0xA, 0x2, 0x1F)

    label("loc_D5B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D5C4")
    OP_29(0xA, 0x4, 0x2)

    label("loc_D5C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D5D9")
    OP_29(0xA, 0x1, 0x0)

    label("loc_D5D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D5EE")
    OP_29(0xA, 0x1, 0x1)

    label("loc_D5EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D603")
    OP_29(0xA, 0x1, 0x2)

    label("loc_D603")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D618")
    OP_29(0xA, 0x1, 0x3)

    label("loc_D618")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D62D")
    OP_29(0xA, 0x1, 0x4)

    label("loc_D62D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D642")
    OP_29(0xA, 0x1, 0x5)

    label("loc_D642")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D657")
    OP_29(0xA, 0x1, 0x6)

    label("loc_D657")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D66C")
    OP_29(0xA, 0x1, 0x7)

    label("loc_D66C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D681")
    OP_29(0xA, 0x1, 0x8)

    label("loc_D681")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D696")
    OP_29(0xA, 0x1, 0x9)

    label("loc_D696")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D6AB")
    OP_29(0xA, 0x1, 0xA)

    label("loc_D6AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D6C0")
    OP_29(0xA, 0x1, 0xB)

    label("loc_D6C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D6D4")
    OP_29(0xA, 0x4, 0x10)

    label("loc_D6D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D6E8")
    OP_29(0xA, 0x4, 0x20)

    label("loc_D6E8")

    Jump("loc_DB41")

    label("loc_D6ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7DA")
    OP_29(0xB, 0x3, 0x0)
    OP_29(0xB, 0x3, 0x1)
    OP_29(0xB, 0x3, 0x2)
    OP_29(0xB, 0x3, 0x10)
    OP_29(0xB, 0x3, 0x20)
    OP_29(0xB, 0x3, 0x40)
    OP_29(0xB, 0x2, 0x0)
    OP_29(0xB, 0x2, 0x1)
    OP_29(0xB, 0x2, 0x2)
    OP_29(0xB, 0x2, 0x3)
    OP_29(0xB, 0x2, 0x4)
    OP_29(0xB, 0x2, 0x5)
    OP_29(0xB, 0x2, 0x6)
    OP_29(0xB, 0x2, 0x7)
    OP_29(0xB, 0x2, 0x8)
    OP_29(0xB, 0x2, 0x9)
    OP_29(0xB, 0x2, 0xA)
    OP_29(0xB, 0x2, 0xB)
    OP_29(0xB, 0x2, 0xC)
    OP_29(0xB, 0x2, 0xD)
    OP_29(0xB, 0x2, 0xE)
    OP_29(0xB, 0x2, 0xF)
    OP_29(0xB, 0x2, 0x10)
    OP_29(0xB, 0x2, 0x11)
    OP_29(0xB, 0x2, 0x12)
    OP_29(0xB, 0x2, 0x13)
    OP_29(0xB, 0x2, 0x14)
    OP_29(0xB, 0x2, 0x15)
    OP_29(0xB, 0x2, 0x16)
    OP_29(0xB, 0x2, 0x17)
    OP_29(0xB, 0x2, 0x18)
    OP_29(0xB, 0x2, 0x19)
    OP_29(0xB, 0x2, 0x1A)
    OP_29(0xB, 0x2, 0x1B)
    OP_29(0xB, 0x2, 0x1C)
    OP_29(0xB, 0x2, 0x1D)
    OP_29(0xB, 0x2, 0x1E)
    OP_29(0xB, 0x2, 0x1F)

    label("loc_D7DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D7EE")
    OP_29(0xB, 0x4, 0x2)

    label("loc_D7EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D803")
    OP_29(0xB, 0x1, 0x0)

    label("loc_D803")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D818")
    OP_29(0xB, 0x1, 0x1)

    label("loc_D818")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D82D")
    OP_29(0xB, 0x1, 0x2)

    label("loc_D82D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D842")
    OP_29(0xB, 0x1, 0x3)

    label("loc_D842")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D857")
    OP_29(0xB, 0x1, 0x4)

    label("loc_D857")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D86C")
    OP_29(0xB, 0x1, 0x5)

    label("loc_D86C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D881")
    OP_29(0xB, 0x1, 0x6)

    label("loc_D881")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D896")
    OP_29(0xB, 0x1, 0x7)

    label("loc_D896")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D8AB")
    OP_29(0xB, 0x1, 0x8)

    label("loc_D8AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D8C0")
    OP_29(0xB, 0x1, 0x9)

    label("loc_D8C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D8D5")
    OP_29(0xB, 0x1, 0xA)

    label("loc_D8D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D8EA")
    OP_29(0xB, 0x1, 0xB)

    label("loc_D8EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D8FE")
    OP_29(0xB, 0x4, 0x10)

    label("loc_D8FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D912")
    OP_29(0xB, 0x4, 0x20)

    label("loc_D912")

    Jump("loc_DB41")

    label("loc_D917")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA04")
    OP_29(0xC, 0x3, 0x0)
    OP_29(0xC, 0x3, 0x1)
    OP_29(0xC, 0x3, 0x2)
    OP_29(0xC, 0x3, 0x10)
    OP_29(0xC, 0x3, 0x20)
    OP_29(0xC, 0x3, 0x40)
    OP_29(0xC, 0x2, 0x0)
    OP_29(0xC, 0x2, 0x1)
    OP_29(0xC, 0x2, 0x2)
    OP_29(0xC, 0x2, 0x3)
    OP_29(0xC, 0x2, 0x4)
    OP_29(0xC, 0x2, 0x5)
    OP_29(0xC, 0x2, 0x6)
    OP_29(0xC, 0x2, 0x7)
    OP_29(0xC, 0x2, 0x8)
    OP_29(0xC, 0x2, 0x9)
    OP_29(0xC, 0x2, 0xA)
    OP_29(0xC, 0x2, 0xB)
    OP_29(0xC, 0x2, 0xC)
    OP_29(0xC, 0x2, 0xD)
    OP_29(0xC, 0x2, 0xE)
    OP_29(0xC, 0x2, 0xF)
    OP_29(0xC, 0x2, 0x10)
    OP_29(0xC, 0x2, 0x11)
    OP_29(0xC, 0x2, 0x12)
    OP_29(0xC, 0x2, 0x13)
    OP_29(0xC, 0x2, 0x14)
    OP_29(0xC, 0x2, 0x15)
    OP_29(0xC, 0x2, 0x16)
    OP_29(0xC, 0x2, 0x17)
    OP_29(0xC, 0x2, 0x18)
    OP_29(0xC, 0x2, 0x19)
    OP_29(0xC, 0x2, 0x1A)
    OP_29(0xC, 0x2, 0x1B)
    OP_29(0xC, 0x2, 0x1C)
    OP_29(0xC, 0x2, 0x1D)
    OP_29(0xC, 0x2, 0x1E)
    OP_29(0xC, 0x2, 0x1F)

    label("loc_DA04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA18")
    OP_29(0xC, 0x4, 0x2)

    label("loc_DA18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA2D")
    OP_29(0xC, 0x1, 0x0)

    label("loc_DA2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA42")
    OP_29(0xC, 0x1, 0x1)

    label("loc_DA42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA57")
    OP_29(0xC, 0x1, 0x2)

    label("loc_DA57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA6C")
    OP_29(0xC, 0x1, 0x3)

    label("loc_DA6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA81")
    OP_29(0xC, 0x1, 0x4)

    label("loc_DA81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA96")
    OP_29(0xC, 0x1, 0x5)

    label("loc_DA96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DAAB")
    OP_29(0xC, 0x1, 0x6)

    label("loc_DAAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DAC0")
    OP_29(0xC, 0x1, 0x7)

    label("loc_DAC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DAD5")
    OP_29(0xC, 0x1, 0x8)

    label("loc_DAD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DAEA")
    OP_29(0xC, 0x1, 0x9)

    label("loc_DAEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DAFF")
    OP_29(0xC, 0x1, 0xA)

    label("loc_DAFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DB14")
    OP_29(0xC, 0x1, 0xB)

    label("loc_DB14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DB28")
    OP_29(0xC, 0x4, 0x10)

    label("loc_DB28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DB3C")
    OP_29(0xC, 0x4, 0x20)

    label("loc_DB3C")

    Jump("loc_DB41")

    label("loc_DB41")

    Jump("loc_BBC5")

    label("loc_DB46")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_55_BBBB end

    def Function_56_DB5E(): pass

    label("Function_56_DB5E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DB68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F16D")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "-- Chapter 2 --\x01",                                        # 0
            "QS_0201 - Old Road Property Monster Extermination\x01",      # 1
            "QS_0202 - Enigma Combat Test\x01",                           # 2
            "QS_0203 - Tangram Gate Drill\x01",                           # 3
            "QS_0204 - Prepare Monsters ③\x01",                          # 4
            "QS_0205 - Fishing for Ingredients\x01",                      # 5
            "QS_0206 - Bout With Delinquents\x01",                        # 6
            "QS_0207 - Helping Doctor Lago\x01",                          # 7
            "QS_0208 - Prepare Monsters ④\x01",                          # 8
            "QS_0209 - Lost Wedding Ring\x01",                            # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (3, "loc_DCF7"),
        (7, "loc_DDA3"),
        (1, "loc_DE49"),
        (2, "loc_DE49"),
        (4, "loc_DE49"),
        (5, "loc_DE49"),
        (6, "loc_DE49"),
        (8, "loc_DE49"),
        (9, "loc_DE49"),
        (SWITCH_DEFAULT, "loc_DEC8"),
    )


    label("loc_DCF7")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                             # 0
            "Start\x01",                             # 1
            "QF_01 - Read Request Details\x01",      # 2
            "QF_02 - Lost 1 time\x01",               # 3
            "QF_03 - Lost 2 times\x01",              # 4
            "QF_04 - Won all times\x01",             # 5
            "QF_05 - Event Completion\x01",          # 6
            "Complete\x01",                          # 7
            "Report\x01",                            # 8
        )
    )

    MenuEnd(0x5)
    Jump("loc_DED7")

    label("loc_DDA3")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                               # 0
            "Start\x01",                               # 1
            "QF_01 - Read Request Details\x01",        # 2
            "QF_02 - Talked With Archbishop\x01",      # 3
            "QF_03 - Got Lupinus Grass\x01",           # 4
            "QF_04 - Event Completion\x01",            # 5
            "Complete\x01",                            # 6
            "Report\x01",                              # 7
        )
    )

    MenuEnd(0x5)
    Jump("loc_DED7")

    label("loc_DE49")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",         # 0
            "Start\x01",         # 1
            "QF_01\x01",         # 2
            "QF_02\x01",         # 3
            "QF_03\x01",         # 4
            "QF_04\x01",         # 5
            "QF_05\x01",         # 6
            "QF_06\x01",         # 7
            "QF_07\x01",         # 8
            "QF_08\x01",         # 9
            "QF_09\x01",         # 10
            "QF_10\x01",         # 11
            "QF_11\x01",         # 12
            "QF_12\x01",         # 13
            "Complete\x01",      # 14
            "Report\x01",        # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_DED7")

    label("loc_DEC8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DED7")

    label("loc_DED7")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F168")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_DF29"),
        (2, "loc_E153"),
        (3, "loc_E37D"),
        (4, "loc_E514"),
        (5, "loc_E73E"),
        (6, "loc_E968"),
        (7, "loc_EB92"),
        (8, "loc_ED14"),
        (9, "loc_EF3E"),
        (SWITCH_DEFAULT, "loc_F168"),
    )


    label("loc_DF29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E016")
    OP_29(0xD, 0x3, 0x0)
    OP_29(0xD, 0x3, 0x1)
    OP_29(0xD, 0x3, 0x2)
    OP_29(0xD, 0x3, 0x10)
    OP_29(0xD, 0x3, 0x20)
    OP_29(0xD, 0x3, 0x40)
    OP_29(0xD, 0x2, 0x0)
    OP_29(0xD, 0x2, 0x1)
    OP_29(0xD, 0x2, 0x2)
    OP_29(0xD, 0x2, 0x3)
    OP_29(0xD, 0x2, 0x4)
    OP_29(0xD, 0x2, 0x5)
    OP_29(0xD, 0x2, 0x6)
    OP_29(0xD, 0x2, 0x7)
    OP_29(0xD, 0x2, 0x8)
    OP_29(0xD, 0x2, 0x9)
    OP_29(0xD, 0x2, 0xA)
    OP_29(0xD, 0x2, 0xB)
    OP_29(0xD, 0x2, 0xC)
    OP_29(0xD, 0x2, 0xD)
    OP_29(0xD, 0x2, 0xE)
    OP_29(0xD, 0x2, 0xF)
    OP_29(0xD, 0x2, 0x10)
    OP_29(0xD, 0x2, 0x11)
    OP_29(0xD, 0x2, 0x12)
    OP_29(0xD, 0x2, 0x13)
    OP_29(0xD, 0x2, 0x14)
    OP_29(0xD, 0x2, 0x15)
    OP_29(0xD, 0x2, 0x16)
    OP_29(0xD, 0x2, 0x17)
    OP_29(0xD, 0x2, 0x18)
    OP_29(0xD, 0x2, 0x19)
    OP_29(0xD, 0x2, 0x1A)
    OP_29(0xD, 0x2, 0x1B)
    OP_29(0xD, 0x2, 0x1C)
    OP_29(0xD, 0x2, 0x1D)
    OP_29(0xD, 0x2, 0x1E)
    OP_29(0xD, 0x2, 0x1F)

    label("loc_E016")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E02A")
    OP_29(0xD, 0x4, 0x2)

    label("loc_E02A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E03F")
    OP_29(0xD, 0x1, 0x0)

    label("loc_E03F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E054")
    OP_29(0xD, 0x1, 0x1)

    label("loc_E054")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E069")
    OP_29(0xD, 0x1, 0x2)

    label("loc_E069")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E07E")
    OP_29(0xD, 0x1, 0x3)

    label("loc_E07E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E093")
    OP_29(0xD, 0x1, 0x4)

    label("loc_E093")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0A8")
    OP_29(0xD, 0x1, 0x5)

    label("loc_E0A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0BD")
    OP_29(0xD, 0x1, 0x6)

    label("loc_E0BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0D2")
    OP_29(0xD, 0x1, 0x7)

    label("loc_E0D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0E7")
    OP_29(0xD, 0x1, 0x8)

    label("loc_E0E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0FC")
    OP_29(0xD, 0x1, 0x9)

    label("loc_E0FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E111")
    OP_29(0xD, 0x1, 0xA)

    label("loc_E111")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E126")
    OP_29(0xD, 0x1, 0xB)

    label("loc_E126")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E13A")
    OP_29(0xD, 0x4, 0x10)

    label("loc_E13A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E14E")
    OP_29(0xD, 0x4, 0x20)

    label("loc_E14E")

    Jump("loc_F168")

    label("loc_E153")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E240")
    OP_29(0xE, 0x3, 0x0)
    OP_29(0xE, 0x3, 0x1)
    OP_29(0xE, 0x3, 0x2)
    OP_29(0xE, 0x3, 0x10)
    OP_29(0xE, 0x3, 0x20)
    OP_29(0xE, 0x3, 0x40)
    OP_29(0xE, 0x2, 0x0)
    OP_29(0xE, 0x2, 0x1)
    OP_29(0xE, 0x2, 0x2)
    OP_29(0xE, 0x2, 0x3)
    OP_29(0xE, 0x2, 0x4)
    OP_29(0xE, 0x2, 0x5)
    OP_29(0xE, 0x2, 0x6)
    OP_29(0xE, 0x2, 0x7)
    OP_29(0xE, 0x2, 0x8)
    OP_29(0xE, 0x2, 0x9)
    OP_29(0xE, 0x2, 0xA)
    OP_29(0xE, 0x2, 0xB)
    OP_29(0xE, 0x2, 0xC)
    OP_29(0xE, 0x2, 0xD)
    OP_29(0xE, 0x2, 0xE)
    OP_29(0xE, 0x2, 0xF)
    OP_29(0xE, 0x2, 0x10)
    OP_29(0xE, 0x2, 0x11)
    OP_29(0xE, 0x2, 0x12)
    OP_29(0xE, 0x2, 0x13)
    OP_29(0xE, 0x2, 0x14)
    OP_29(0xE, 0x2, 0x15)
    OP_29(0xE, 0x2, 0x16)
    OP_29(0xE, 0x2, 0x17)
    OP_29(0xE, 0x2, 0x18)
    OP_29(0xE, 0x2, 0x19)
    OP_29(0xE, 0x2, 0x1A)
    OP_29(0xE, 0x2, 0x1B)
    OP_29(0xE, 0x2, 0x1C)
    OP_29(0xE, 0x2, 0x1D)
    OP_29(0xE, 0x2, 0x1E)
    OP_29(0xE, 0x2, 0x1F)

    label("loc_E240")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E254")
    OP_29(0xE, 0x4, 0x2)

    label("loc_E254")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E269")
    OP_29(0xE, 0x1, 0x0)

    label("loc_E269")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E27E")
    OP_29(0xE, 0x1, 0x1)

    label("loc_E27E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E293")
    OP_29(0xE, 0x1, 0x2)

    label("loc_E293")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2A8")
    OP_29(0xE, 0x1, 0x3)

    label("loc_E2A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2BD")
    OP_29(0xE, 0x1, 0x4)

    label("loc_E2BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2D2")
    OP_29(0xE, 0x1, 0x5)

    label("loc_E2D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2E7")
    OP_29(0xE, 0x1, 0x6)

    label("loc_E2E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2FC")
    OP_29(0xE, 0x1, 0x7)

    label("loc_E2FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E311")
    OP_29(0xE, 0x1, 0x8)

    label("loc_E311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E326")
    OP_29(0xE, 0x1, 0x9)

    label("loc_E326")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E33B")
    OP_29(0xE, 0x1, 0xA)

    label("loc_E33B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E350")
    OP_29(0xE, 0x1, 0xB)

    label("loc_E350")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E364")
    OP_29(0xE, 0x4, 0x10)

    label("loc_E364")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E378")
    OP_29(0xE, 0x4, 0x20)

    label("loc_E378")

    Jump("loc_F168")

    label("loc_E37D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E46A")
    OP_29(0xF, 0x3, 0x0)
    OP_29(0xF, 0x3, 0x1)
    OP_29(0xF, 0x3, 0x2)
    OP_29(0xF, 0x3, 0x10)
    OP_29(0xF, 0x3, 0x20)
    OP_29(0xF, 0x3, 0x40)
    OP_29(0xF, 0x2, 0x0)
    OP_29(0xF, 0x2, 0x1)
    OP_29(0xF, 0x2, 0x2)
    OP_29(0xF, 0x2, 0x3)
    OP_29(0xF, 0x2, 0x4)
    OP_29(0xF, 0x2, 0x5)
    OP_29(0xF, 0x2, 0x6)
    OP_29(0xF, 0x2, 0x7)
    OP_29(0xF, 0x2, 0x8)
    OP_29(0xF, 0x2, 0x9)
    OP_29(0xF, 0x2, 0xA)
    OP_29(0xF, 0x2, 0xB)
    OP_29(0xF, 0x2, 0xC)
    OP_29(0xF, 0x2, 0xD)
    OP_29(0xF, 0x2, 0xE)
    OP_29(0xF, 0x2, 0xF)
    OP_29(0xF, 0x2, 0x10)
    OP_29(0xF, 0x2, 0x11)
    OP_29(0xF, 0x2, 0x12)
    OP_29(0xF, 0x2, 0x13)
    OP_29(0xF, 0x2, 0x14)
    OP_29(0xF, 0x2, 0x15)
    OP_29(0xF, 0x2, 0x16)
    OP_29(0xF, 0x2, 0x17)
    OP_29(0xF, 0x2, 0x18)
    OP_29(0xF, 0x2, 0x19)
    OP_29(0xF, 0x2, 0x1A)
    OP_29(0xF, 0x2, 0x1B)
    OP_29(0xF, 0x2, 0x1C)
    OP_29(0xF, 0x2, 0x1D)
    OP_29(0xF, 0x2, 0x1E)
    OP_29(0xF, 0x2, 0x1F)

    label("loc_E46A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E47E")
    OP_29(0xF, 0x4, 0x2)

    label("loc_E47E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E493")
    OP_29(0xF, 0x1, 0x0)

    label("loc_E493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4A8")
    OP_29(0xF, 0x1, 0x1)

    label("loc_E4A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4BD")
    OP_29(0xF, 0x1, 0x2)

    label("loc_E4BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4D2")
    OP_29(0xF, 0x1, 0x3)

    label("loc_E4D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4E7")
    OP_29(0xF, 0x1, 0x4)

    label("loc_E4E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4FB")
    OP_29(0xF, 0x4, 0x10)

    label("loc_E4FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E50F")
    OP_29(0xF, 0x4, 0x20)

    label("loc_E50F")

    Jump("loc_F168")

    label("loc_E514")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E601")
    OP_29(0x10, 0x3, 0x0)
    OP_29(0x10, 0x3, 0x1)
    OP_29(0x10, 0x3, 0x2)
    OP_29(0x10, 0x3, 0x10)
    OP_29(0x10, 0x3, 0x20)
    OP_29(0x10, 0x3, 0x40)
    OP_29(0x10, 0x2, 0x0)
    OP_29(0x10, 0x2, 0x1)
    OP_29(0x10, 0x2, 0x2)
    OP_29(0x10, 0x2, 0x3)
    OP_29(0x10, 0x2, 0x4)
    OP_29(0x10, 0x2, 0x5)
    OP_29(0x10, 0x2, 0x6)
    OP_29(0x10, 0x2, 0x7)
    OP_29(0x10, 0x2, 0x8)
    OP_29(0x10, 0x2, 0x9)
    OP_29(0x10, 0x2, 0xA)
    OP_29(0x10, 0x2, 0xB)
    OP_29(0x10, 0x2, 0xC)
    OP_29(0x10, 0x2, 0xD)
    OP_29(0x10, 0x2, 0xE)
    OP_29(0x10, 0x2, 0xF)
    OP_29(0x10, 0x2, 0x10)
    OP_29(0x10, 0x2, 0x11)
    OP_29(0x10, 0x2, 0x12)
    OP_29(0x10, 0x2, 0x13)
    OP_29(0x10, 0x2, 0x14)
    OP_29(0x10, 0x2, 0x15)
    OP_29(0x10, 0x2, 0x16)
    OP_29(0x10, 0x2, 0x17)
    OP_29(0x10, 0x2, 0x18)
    OP_29(0x10, 0x2, 0x19)
    OP_29(0x10, 0x2, 0x1A)
    OP_29(0x10, 0x2, 0x1B)
    OP_29(0x10, 0x2, 0x1C)
    OP_29(0x10, 0x2, 0x1D)
    OP_29(0x10, 0x2, 0x1E)
    OP_29(0x10, 0x2, 0x1F)

    label("loc_E601")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E615")
    OP_29(0x10, 0x4, 0x2)

    label("loc_E615")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E62A")
    OP_29(0x10, 0x1, 0x0)

    label("loc_E62A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E63F")
    OP_29(0x10, 0x1, 0x1)

    label("loc_E63F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E654")
    OP_29(0x10, 0x1, 0x2)

    label("loc_E654")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E669")
    OP_29(0x10, 0x1, 0x3)

    label("loc_E669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E67E")
    OP_29(0x10, 0x1, 0x4)

    label("loc_E67E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E693")
    OP_29(0x10, 0x1, 0x5)

    label("loc_E693")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6A8")
    OP_29(0x10, 0x1, 0x6)

    label("loc_E6A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6BD")
    OP_29(0x10, 0x1, 0x7)

    label("loc_E6BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6D2")
    OP_29(0x10, 0x1, 0x8)

    label("loc_E6D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6E7")
    OP_29(0x10, 0x1, 0x9)

    label("loc_E6E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6FC")
    OP_29(0x10, 0x1, 0xA)

    label("loc_E6FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E711")
    OP_29(0x10, 0x1, 0xB)

    label("loc_E711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E725")
    OP_29(0x10, 0x4, 0x10)

    label("loc_E725")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E739")
    OP_29(0x10, 0x4, 0x20)

    label("loc_E739")

    Jump("loc_F168")

    label("loc_E73E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E82B")
    OP_29(0x11, 0x3, 0x0)
    OP_29(0x11, 0x3, 0x1)
    OP_29(0x11, 0x3, 0x2)
    OP_29(0x11, 0x3, 0x10)
    OP_29(0x11, 0x3, 0x20)
    OP_29(0x11, 0x3, 0x40)
    OP_29(0x11, 0x2, 0x0)
    OP_29(0x11, 0x2, 0x1)
    OP_29(0x11, 0x2, 0x2)
    OP_29(0x11, 0x2, 0x3)
    OP_29(0x11, 0x2, 0x4)
    OP_29(0x11, 0x2, 0x5)
    OP_29(0x11, 0x2, 0x6)
    OP_29(0x11, 0x2, 0x7)
    OP_29(0x11, 0x2, 0x8)
    OP_29(0x11, 0x2, 0x9)
    OP_29(0x11, 0x2, 0xA)
    OP_29(0x11, 0x2, 0xB)
    OP_29(0x11, 0x2, 0xC)
    OP_29(0x11, 0x2, 0xD)
    OP_29(0x11, 0x2, 0xE)
    OP_29(0x11, 0x2, 0xF)
    OP_29(0x11, 0x2, 0x10)
    OP_29(0x11, 0x2, 0x11)
    OP_29(0x11, 0x2, 0x12)
    OP_29(0x11, 0x2, 0x13)
    OP_29(0x11, 0x2, 0x14)
    OP_29(0x11, 0x2, 0x15)
    OP_29(0x11, 0x2, 0x16)
    OP_29(0x11, 0x2, 0x17)
    OP_29(0x11, 0x2, 0x18)
    OP_29(0x11, 0x2, 0x19)
    OP_29(0x11, 0x2, 0x1A)
    OP_29(0x11, 0x2, 0x1B)
    OP_29(0x11, 0x2, 0x1C)
    OP_29(0x11, 0x2, 0x1D)
    OP_29(0x11, 0x2, 0x1E)
    OP_29(0x11, 0x2, 0x1F)

    label("loc_E82B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E83F")
    OP_29(0x11, 0x4, 0x2)

    label("loc_E83F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E854")
    OP_29(0x11, 0x1, 0x0)

    label("loc_E854")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E869")
    OP_29(0x11, 0x1, 0x1)

    label("loc_E869")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E87E")
    OP_29(0x11, 0x1, 0x2)

    label("loc_E87E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E893")
    OP_29(0x11, 0x1, 0x3)

    label("loc_E893")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8A8")
    OP_29(0x11, 0x1, 0x4)

    label("loc_E8A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8BD")
    OP_29(0x11, 0x1, 0x5)

    label("loc_E8BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8D2")
    OP_29(0x11, 0x1, 0x6)

    label("loc_E8D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8E7")
    OP_29(0x11, 0x1, 0x7)

    label("loc_E8E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8FC")
    OP_29(0x11, 0x1, 0x8)

    label("loc_E8FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E911")
    OP_29(0x11, 0x1, 0x9)

    label("loc_E911")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E926")
    OP_29(0x11, 0x1, 0xA)

    label("loc_E926")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E93B")
    OP_29(0x11, 0x1, 0xB)

    label("loc_E93B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E94F")
    OP_29(0x11, 0x4, 0x10)

    label("loc_E94F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E963")
    OP_29(0x11, 0x4, 0x20)

    label("loc_E963")

    Jump("loc_F168")

    label("loc_E968")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA55")
    OP_29(0x12, 0x3, 0x0)
    OP_29(0x12, 0x3, 0x1)
    OP_29(0x12, 0x3, 0x2)
    OP_29(0x12, 0x3, 0x10)
    OP_29(0x12, 0x3, 0x20)
    OP_29(0x12, 0x3, 0x40)
    OP_29(0x12, 0x2, 0x0)
    OP_29(0x12, 0x2, 0x1)
    OP_29(0x12, 0x2, 0x2)
    OP_29(0x12, 0x2, 0x3)
    OP_29(0x12, 0x2, 0x4)
    OP_29(0x12, 0x2, 0x5)
    OP_29(0x12, 0x2, 0x6)
    OP_29(0x12, 0x2, 0x7)
    OP_29(0x12, 0x2, 0x8)
    OP_29(0x12, 0x2, 0x9)
    OP_29(0x12, 0x2, 0xA)
    OP_29(0x12, 0x2, 0xB)
    OP_29(0x12, 0x2, 0xC)
    OP_29(0x12, 0x2, 0xD)
    OP_29(0x12, 0x2, 0xE)
    OP_29(0x12, 0x2, 0xF)
    OP_29(0x12, 0x2, 0x10)
    OP_29(0x12, 0x2, 0x11)
    OP_29(0x12, 0x2, 0x12)
    OP_29(0x12, 0x2, 0x13)
    OP_29(0x12, 0x2, 0x14)
    OP_29(0x12, 0x2, 0x15)
    OP_29(0x12, 0x2, 0x16)
    OP_29(0x12, 0x2, 0x17)
    OP_29(0x12, 0x2, 0x18)
    OP_29(0x12, 0x2, 0x19)
    OP_29(0x12, 0x2, 0x1A)
    OP_29(0x12, 0x2, 0x1B)
    OP_29(0x12, 0x2, 0x1C)
    OP_29(0x12, 0x2, 0x1D)
    OP_29(0x12, 0x2, 0x1E)
    OP_29(0x12, 0x2, 0x1F)

    label("loc_EA55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EA69")
    OP_29(0x12, 0x4, 0x2)

    label("loc_EA69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EA7E")
    OP_29(0x12, 0x1, 0x0)

    label("loc_EA7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EA93")
    OP_29(0x12, 0x1, 0x1)

    label("loc_EA93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAA8")
    OP_29(0x12, 0x1, 0x2)

    label("loc_EAA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EABD")
    OP_29(0x12, 0x1, 0x3)

    label("loc_EABD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAD2")
    OP_29(0x12, 0x1, 0x4)

    label("loc_EAD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAE7")
    OP_29(0x12, 0x1, 0x5)

    label("loc_EAE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAFC")
    OP_29(0x12, 0x1, 0x6)

    label("loc_EAFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB11")
    OP_29(0x12, 0x1, 0x7)

    label("loc_EB11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB26")
    OP_29(0x12, 0x1, 0x8)

    label("loc_EB26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB3B")
    OP_29(0x12, 0x1, 0x9)

    label("loc_EB3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB50")
    OP_29(0x12, 0x1, 0xA)

    label("loc_EB50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB65")
    OP_29(0x12, 0x1, 0xB)

    label("loc_EB65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB79")
    OP_29(0x12, 0x4, 0x10)

    label("loc_EB79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB8D")
    OP_29(0x12, 0x4, 0x20)

    label("loc_EB8D")

    Jump("loc_F168")

    label("loc_EB92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC7F")
    OP_29(0x13, 0x3, 0x0)
    OP_29(0x13, 0x3, 0x1)
    OP_29(0x13, 0x3, 0x2)
    OP_29(0x13, 0x3, 0x10)
    OP_29(0x13, 0x3, 0x20)
    OP_29(0x13, 0x3, 0x40)
    OP_29(0x13, 0x2, 0x0)
    OP_29(0x13, 0x2, 0x1)
    OP_29(0x13, 0x2, 0x2)
    OP_29(0x13, 0x2, 0x3)
    OP_29(0x13, 0x2, 0x4)
    OP_29(0x13, 0x2, 0x5)
    OP_29(0x13, 0x2, 0x6)
    OP_29(0x13, 0x2, 0x7)
    OP_29(0x13, 0x2, 0x8)
    OP_29(0x13, 0x2, 0x9)
    OP_29(0x13, 0x2, 0xA)
    OP_29(0x13, 0x2, 0xB)
    OP_29(0x13, 0x2, 0xC)
    OP_29(0x13, 0x2, 0xD)
    OP_29(0x13, 0x2, 0xE)
    OP_29(0x13, 0x2, 0xF)
    OP_29(0x13, 0x2, 0x10)
    OP_29(0x13, 0x2, 0x11)
    OP_29(0x13, 0x2, 0x12)
    OP_29(0x13, 0x2, 0x13)
    OP_29(0x13, 0x2, 0x14)
    OP_29(0x13, 0x2, 0x15)
    OP_29(0x13, 0x2, 0x16)
    OP_29(0x13, 0x2, 0x17)
    OP_29(0x13, 0x2, 0x18)
    OP_29(0x13, 0x2, 0x19)
    OP_29(0x13, 0x2, 0x1A)
    OP_29(0x13, 0x2, 0x1B)
    OP_29(0x13, 0x2, 0x1C)
    OP_29(0x13, 0x2, 0x1D)
    OP_29(0x13, 0x2, 0x1E)
    OP_29(0x13, 0x2, 0x1F)

    label("loc_EC7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EC93")
    OP_29(0x13, 0x4, 0x2)

    label("loc_EC93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECA8")
    OP_29(0x13, 0x1, 0x0)

    label("loc_ECA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECBD")
    OP_29(0x13, 0x1, 0x1)

    label("loc_ECBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECD2")
    OP_29(0x13, 0x1, 0x2)

    label("loc_ECD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECE7")
    OP_29(0x13, 0x1, 0x3)

    label("loc_ECE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECFB")
    OP_29(0x13, 0x4, 0x10)

    label("loc_ECFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED0F")
    OP_29(0x13, 0x4, 0x20)

    label("loc_ED0F")

    Jump("loc_F168")

    label("loc_ED14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE01")
    OP_29(0x14, 0x3, 0x0)
    OP_29(0x14, 0x3, 0x1)
    OP_29(0x14, 0x3, 0x2)
    OP_29(0x14, 0x3, 0x10)
    OP_29(0x14, 0x3, 0x20)
    OP_29(0x14, 0x3, 0x40)
    OP_29(0x14, 0x2, 0x0)
    OP_29(0x14, 0x2, 0x1)
    OP_29(0x14, 0x2, 0x2)
    OP_29(0x14, 0x2, 0x3)
    OP_29(0x14, 0x2, 0x4)
    OP_29(0x14, 0x2, 0x5)
    OP_29(0x14, 0x2, 0x6)
    OP_29(0x14, 0x2, 0x7)
    OP_29(0x14, 0x2, 0x8)
    OP_29(0x14, 0x2, 0x9)
    OP_29(0x14, 0x2, 0xA)
    OP_29(0x14, 0x2, 0xB)
    OP_29(0x14, 0x2, 0xC)
    OP_29(0x14, 0x2, 0xD)
    OP_29(0x14, 0x2, 0xE)
    OP_29(0x14, 0x2, 0xF)
    OP_29(0x14, 0x2, 0x10)
    OP_29(0x14, 0x2, 0x11)
    OP_29(0x14, 0x2, 0x12)
    OP_29(0x14, 0x2, 0x13)
    OP_29(0x14, 0x2, 0x14)
    OP_29(0x14, 0x2, 0x15)
    OP_29(0x14, 0x2, 0x16)
    OP_29(0x14, 0x2, 0x17)
    OP_29(0x14, 0x2, 0x18)
    OP_29(0x14, 0x2, 0x19)
    OP_29(0x14, 0x2, 0x1A)
    OP_29(0x14, 0x2, 0x1B)
    OP_29(0x14, 0x2, 0x1C)
    OP_29(0x14, 0x2, 0x1D)
    OP_29(0x14, 0x2, 0x1E)
    OP_29(0x14, 0x2, 0x1F)

    label("loc_EE01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EE15")
    OP_29(0x14, 0x4, 0x2)

    label("loc_EE15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EE2A")
    OP_29(0x14, 0x1, 0x0)

    label("loc_EE2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EE3F")
    OP_29(0x14, 0x1, 0x1)

    label("loc_EE3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EE54")
    OP_29(0x14, 0x1, 0x2)

    label("loc_EE54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EE69")
    OP_29(0x14, 0x1, 0x3)

    label("loc_EE69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EE7E")
    OP_29(0x14, 0x1, 0x4)

    label("loc_EE7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EE93")
    OP_29(0x14, 0x1, 0x5)

    label("loc_EE93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EEA8")
    OP_29(0x14, 0x1, 0x6)

    label("loc_EEA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EEBD")
    OP_29(0x14, 0x1, 0x7)

    label("loc_EEBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EED2")
    OP_29(0x14, 0x1, 0x8)

    label("loc_EED2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EEE7")
    OP_29(0x14, 0x1, 0x9)

    label("loc_EEE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EEFC")
    OP_29(0x14, 0x1, 0xA)

    label("loc_EEFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EF11")
    OP_29(0x14, 0x1, 0xB)

    label("loc_EF11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EF25")
    OP_29(0x14, 0x4, 0x10)

    label("loc_EF25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EF39")
    OP_29(0x14, 0x4, 0x20)

    label("loc_EF39")

    Jump("loc_F168")

    label("loc_EF3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F02B")
    OP_29(0x15, 0x3, 0x0)
    OP_29(0x15, 0x3, 0x1)
    OP_29(0x15, 0x3, 0x2)
    OP_29(0x15, 0x3, 0x10)
    OP_29(0x15, 0x3, 0x20)
    OP_29(0x15, 0x3, 0x40)
    OP_29(0x15, 0x2, 0x0)
    OP_29(0x15, 0x2, 0x1)
    OP_29(0x15, 0x2, 0x2)
    OP_29(0x15, 0x2, 0x3)
    OP_29(0x15, 0x2, 0x4)
    OP_29(0x15, 0x2, 0x5)
    OP_29(0x15, 0x2, 0x6)
    OP_29(0x15, 0x2, 0x7)
    OP_29(0x15, 0x2, 0x8)
    OP_29(0x15, 0x2, 0x9)
    OP_29(0x15, 0x2, 0xA)
    OP_29(0x15, 0x2, 0xB)
    OP_29(0x15, 0x2, 0xC)
    OP_29(0x15, 0x2, 0xD)
    OP_29(0x15, 0x2, 0xE)
    OP_29(0x15, 0x2, 0xF)
    OP_29(0x15, 0x2, 0x10)
    OP_29(0x15, 0x2, 0x11)
    OP_29(0x15, 0x2, 0x12)
    OP_29(0x15, 0x2, 0x13)
    OP_29(0x15, 0x2, 0x14)
    OP_29(0x15, 0x2, 0x15)
    OP_29(0x15, 0x2, 0x16)
    OP_29(0x15, 0x2, 0x17)
    OP_29(0x15, 0x2, 0x18)
    OP_29(0x15, 0x2, 0x19)
    OP_29(0x15, 0x2, 0x1A)
    OP_29(0x15, 0x2, 0x1B)
    OP_29(0x15, 0x2, 0x1C)
    OP_29(0x15, 0x2, 0x1D)
    OP_29(0x15, 0x2, 0x1E)
    OP_29(0x15, 0x2, 0x1F)

    label("loc_F02B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F03F")
    OP_29(0x15, 0x4, 0x2)

    label("loc_F03F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F054")
    OP_29(0x15, 0x1, 0x0)

    label("loc_F054")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F069")
    OP_29(0x15, 0x1, 0x1)

    label("loc_F069")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F07E")
    OP_29(0x15, 0x1, 0x2)

    label("loc_F07E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F093")
    OP_29(0x15, 0x1, 0x3)

    label("loc_F093")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F0A8")
    OP_29(0x15, 0x1, 0x4)

    label("loc_F0A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F0BD")
    OP_29(0x15, 0x1, 0x5)

    label("loc_F0BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F0D2")
    OP_29(0x15, 0x1, 0x6)

    label("loc_F0D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F0E7")
    OP_29(0x15, 0x1, 0x7)

    label("loc_F0E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F0FC")
    OP_29(0x15, 0x1, 0x8)

    label("loc_F0FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F111")
    OP_29(0x15, 0x1, 0x9)

    label("loc_F111")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F126")
    OP_29(0x15, 0x1, 0xA)

    label("loc_F126")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F13B")
    OP_29(0x15, 0x1, 0xB)

    label("loc_F13B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F14F")
    OP_29(0x15, 0x4, 0x10)

    label("loc_F14F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F163")
    OP_29(0x15, 0x4, 0x20)

    label("loc_F163")

    Jump("loc_F168")

    label("loc_F168")

    Jump("loc_DB68")

    label("loc_F16D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_56_DB5E end

    def Function_57_F185(): pass

    label("Function_57_F185")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F18F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_122D1")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "-- Chapter 3 --\x01",                                   # 0
            "QS_0301 - Search for Missing Doctor\x01",               # 1
            "QS_0302 - Illegal Parking Crackdown\x01",               # 2
            "QS_0303 - The Many Famous Views of Crossbell\x01",      # 3
            "QS_0304 - Bellguard Gate Lost Item\x01",                # 4
            "QS_0305 - Prepare Monsters ⑤\x01",                     # 5
            "QS_0306 - Assistance from Second Division\x01",         # 6
            "QS_0307 - Mine Monster Cleanup\x01",                    # 7
            "QS_0308 - Stalker Investigation\x01",                   # 8
            "QS_0309 - Prepare Monsters ⑥\x01",                     # 9
            "QS_0310 - Tourists Are Missing\x01",                    # 10
            "QS_0311 - Serial Theft Investigation\x01",              # 11
            "QS_0312 - Prepare Monsters ⑦\x01",                     # 12
            "QS_0313 - Phantom Thief B Challenge\x01",               # 13
            "QS_0314 - Prepare Monsters ⑧\x01",                     # 14
            "QS_0315 - Lost Engagement Ring\x01",                    # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_F41E"),
        (2, "loc_F561"),
        (3, "loc_F7C7"),
        (4, "loc_FA25"),
        (6, "loc_FB05"),
        (7, "loc_FBE0"),
        (11, "loc_FCB3"),
        (13, "loc_FE10"),
        (5, "loc_FF86"),
        (8, "loc_FF86"),
        (9, "loc_FF86"),
        (10, "loc_FF86"),
        (12, "loc_FF86"),
        (15, "loc_FF86"),
        (14, "loc_FF86"),
        (SWITCH_DEFAULT, "loc_10005"),
    )


    label("loc_F41E")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                                                 # 0
            "Start\x01",                                                 # 1
            "QF_01 - Heard Situation at Hospital\x01",                   # 2
            "QF_02 - Visited Fisherman's Guild\x01",                     # 3
            "GF   - Heard About Fishing Tournament at Sandbar\x01",      # 4
            "QF_03 - Started Fishing Duel\x01",                          # 5
            "QF_04 - Lost\x01",                                          # 6
            "QF_05 - Drew\x01",                                          # 7
            "QF_06 - Won\x01",                                           # 8
            "QF_07 - Cleared Quest\x01",                                 # 9
            "QF_08 (Unused)\x01",                                        # 10
            "QF_09 (Unused)\x01",                                        # 11
            "QF_10 (Unused)\x01",                                        # 12
            "QF_11 (Unused)\x01",                                        # 13
            "Complete\x01",                                              # 14
            "Report\x01",                                                # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_10014")

    label("loc_F561")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                                         # 0
            "Start\x01",                                         # 1
            "QF_01 - Start\x01",                                 # 2
            "QF_03 - West Exit - Sticker on Vehicle 1\x01",      # 3
            "QF_05 - West Exit - Sticker on Vehicle 2\x01",      # 4
            "QF_07 - West Exit - Sticker on Vehicle 3\x01",      # 5
            "QF_09 - West Exit - Sticker on Vehicle 4\x01",      # 6
            "QF_11 - East Exit - Sticker on Vehicle 5\x01",      # 7
            "QF_13 - East Exit - Sticker on Vehicle 6\x01",      # 8
            "QF_15 - East Exit - Sticker on Vehicle 7\x01",      # 9
            "QF_17 - East Exit - Sticker on Vehicle 8\x01",      # 10
            "QF_19 - East Exit - Sticker on Vehicle 9\x01",      # 11
            "QF_20 - Saw All Vehicle Numbers\x01",               # 12
            "QF_21 - Noticed Duplicate Number\x01",              # 13
            "[→next]\x01",                                      # 14
        )
    )

    MenuEnd(0x5)
    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7C2")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "QF_22 - Fail End\x01",         # 0
            "QF_23 - Success End\x01",      # 1
            "Complete\x01",                 # 2
            "Report\x01",                   # 3
        )
    )

    MenuEnd(0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7C2")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F7C2")

    Jump("loc_10014")

    label("loc_F7C7")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                                          # 0
            "Start\x01",                                          # 1
            "QF_01 - Talked With Receptionist Tria\x01",          # 2
            "QF_02 - Read Request Details\x01",                   # 3
            "QF_03 - Old Road Rural Landscape\x01",               # 4
            "QF_04 - Armorica Village Flower Garden\x01",         # 5
            "QF_05 - Ursula Road Lookout Platform\x01",           # 6
            "QF_06 - View From Cathedral Graveyard\x01",          # 7
            "QF_07 - Mainz Mountain Path Waterfall\x01",          # 8
            "QF_08 - West Crossbell Highway Rail\x01",            # 9
            "QF_09 - Distant View of Stargazer's Tower\x01",      # 10
            "QF_10 - Distant View of Moon Temple\x01",            # 11
            "QF_11 - Distant View of Sun Fort\x01",               # 12
            "[→next]\x01",                                       # 13
        )
    )

    MenuEnd(0x5)
    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA20")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "QF_12 - Presented Photos - Fully Satisfied\x01",      # 0
            "QF_13 - Presented Photos - Several\x01",              # 1
            "Complete\x01",                                        # 2
            "Report\x01",                                          # 3
        )
    )

    MenuEnd(0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA20")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FA20")

    Jump("loc_10014")

    label("loc_FA25")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                                   # 0
            "Start\x01",                                   # 1
            "QF_01 - Inspected Covered Tank\x01",          # 2
            "QF_02 - Read Request Details\x01",            # 3
            "QF_03 - Take on Request\x01",                 # 4
            "QF_04 - Talked to Dieter\x01",                # 5
            "QF_05 - Talked to Stella\x01",                # 6
            "QF_06 - Started Searching the Roof\x01",      # 7
            "Complete\x01",                                # 8
            "Report\x01",                                  # 9
        )
    )

    MenuEnd(0x5)
    Jump("loc_10014")

    label("loc_FB05")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                                     # 0
            "Start\x01",                                     # 1
            "QF_01 - Requested by Second Division\x01",      # 2
            "QF_02 - Had Meeting\x01",                       # 3
            "QF_03 - Talked to Sonya\x01",                   # 4
            "QF_04 - Investigation Started\x01",             # 5
            "QF_05 - Started Listening\x01",                 # 6
            "QF_14 - Finished Listening\x01",                # 7
            "Complete\x01",                                  # 8
            "Report\x01",                                    # 9
        )
    )

    MenuEnd(0x5)
    Jump("loc_10014")

    label("loc_FBE0")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                                # 0
            "Start\x01",                                # 1
            "QF_01 - Read Request Details\x01",         # 2
            "QF_02 - Take on Request\x01",              # 3
            "QF_03 - Used Abandoned Mine Key\x01",      # 4
            "QF_04 - Entered Mine\x01",                 # 5
            "QF_05 - Eliminated Monsters\x01",          # 6
            "- One More Eliminated\x01",                # 7
            "Complete\x01",                             # 8
            "Report\x01",                               # 9
        )
    )

    MenuEnd(0x5)
    Jump("loc_10014")

    label("loc_FCB3")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",         # 0
            "Start\x01",         # 1
            "QF_01\x01",         # 2
            "QF_02\x01",         # 3
            "QF_03\x01",         # 4
            "QF_04\x01",         # 5
            "QF_05\x01",         # 6
            "QF_06\x01",         # 7
            "QF_07\x01",         # 8
            "QF_08\x01",         # 9
            "QF_09\x01",         # 10
            "QF_10\x01",         # 11
            "QF_11\x01",         # 12
            "QF_12\x01",         # 13
            "QF_13\x01",         # 14
            "[→next]\x01",      # 15
        )
    )

    MenuEnd(0x5)
    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE0B")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "QF_14\x01",                 # 0
            "QF_15\x01",                 # 1
            "QF_16\x01",                 # 2
            "QF_17\x01",                 # 3
            "QF_18\x01",                 # 4
            "QF_19\x01",                 # 5
            "QF_20\x01",                 # 6
            "QF_21\x01",                 # 7
            "QF_22\x01",                 # 8
            "[C010C Stakeout]\x01",      # 9
            "[C110C Stakeout]\x01",      # 10
            "[C040C Stakeout]\x01",      # 11
            "[C120C Stakeout]\x01",      # 12
            "[Stakeout Fail]\x01",       # 13
            "[Resolution]\x01",          # 14
            "Report\x01",                # 15
        )
    )

    MenuEnd(0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FE0B")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FE0B")

    Jump("loc_10014")

    label("loc_FE10")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                                               # 0
            "Start\x01",                                               # 1
            "QF_01 - Heard Situation, Started Investigation\x01",      # 2
            "QF_02 - Checked Bell in Central Square\x01",              # 3
            "QF_03 - Checked Aquarium in Fisherman's Guild\x01",       # 4
            "QF_04 - Checked Speaker in Ignis\x01",                    # 5
            "QF_05 - Saw Event in Library\x01",                        # 6
            "QF_06 - Found Card in Airport\x01",                       # 7
            "QF_07 - Checked CNS\x01",                                 # 8
            "QF_08 (Unused)\x01",                                      # 9
            "QF_09 (Unused)\x01",                                      # 10
            "QF_10 (Unused)\x01",                                      # 11
            "QF_11 (Unused)\x01",                                      # 12
            "QF_12 (Unused)\x01",                                      # 13
            "Complete\x01",                                            # 14
            "Report\x01",                                              # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_10014")

    label("loc_FF86")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",         # 0
            "Start\x01",         # 1
            "QF_01\x01",         # 2
            "QF_02\x01",         # 3
            "QF_03\x01",         # 4
            "QF_04\x01",         # 5
            "QF_05\x01",         # 6
            "QF_06\x01",         # 7
            "QF_07\x01",         # 8
            "QF_08\x01",         # 9
            "QF_09\x01",         # 10
            "QF_10\x01",         # 11
            "QF_11\x01",         # 12
            "QF_12\x01",         # 13
            "Complete\x01",      # 14
            "Report\x01",        # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_10014")

    label("loc_10005")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10014")

    label("loc_10014")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_122CC")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1008A"),
        (2, "loc_102B1"),
        (3, "loc_10505"),
        (4, "loc_10744"),
        (5, "loc_108F0"),
        (6, "loc_10B1A"),
        (7, "loc_10CC6"),
        (8, "loc_10FFE"),
        (9, "loc_11228"),
        (10, "loc_11452"),
        (11, "loc_1167C"),
        (12, "loc_11A24"),
        (13, "loc_11C4E"),
        (14, "loc_11E78"),
        (15, "loc_120A2"),
        (SWITCH_DEFAULT, "loc_122CC"),
    )


    label("loc_1008A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10177")
    OP_29(0x16, 0x3, 0x0)
    OP_29(0x16, 0x3, 0x1)
    OP_29(0x16, 0x3, 0x2)
    OP_29(0x16, 0x3, 0x10)
    OP_29(0x16, 0x3, 0x20)
    OP_29(0x16, 0x3, 0x40)
    OP_29(0x16, 0x2, 0x0)
    OP_29(0x16, 0x2, 0x1)
    OP_29(0x16, 0x2, 0x2)
    OP_29(0x16, 0x2, 0x3)
    OP_29(0x16, 0x2, 0x4)
    OP_29(0x16, 0x2, 0x5)
    OP_29(0x16, 0x2, 0x6)
    OP_29(0x16, 0x2, 0x7)
    OP_29(0x16, 0x2, 0x8)
    OP_29(0x16, 0x2, 0x9)
    OP_29(0x16, 0x2, 0xA)
    OP_29(0x16, 0x2, 0xB)
    OP_29(0x16, 0x2, 0xC)
    OP_29(0x16, 0x2, 0xD)
    OP_29(0x16, 0x2, 0xE)
    OP_29(0x16, 0x2, 0xF)
    OP_29(0x16, 0x2, 0x10)
    OP_29(0x16, 0x2, 0x11)
    OP_29(0x16, 0x2, 0x12)
    OP_29(0x16, 0x2, 0x13)
    OP_29(0x16, 0x2, 0x14)
    OP_29(0x16, 0x2, 0x15)
    OP_29(0x16, 0x2, 0x16)
    OP_29(0x16, 0x2, 0x17)
    OP_29(0x16, 0x2, 0x18)
    OP_29(0x16, 0x2, 0x19)
    OP_29(0x16, 0x2, 0x1A)
    OP_29(0x16, 0x2, 0x1B)
    OP_29(0x16, 0x2, 0x1C)
    OP_29(0x16, 0x2, 0x1D)
    OP_29(0x16, 0x2, 0x1E)
    OP_29(0x16, 0x2, 0x1F)

    label("loc_10177")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1018B")
    OP_29(0x16, 0x4, 0x2)

    label("loc_1018B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_101A0")
    OP_29(0x16, 0x1, 0x0)

    label("loc_101A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_101B5")
    OP_29(0x16, 0x1, 0x1)

    label("loc_101B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_101C7")
    SetScenarioFlags(0xBD, 3)

    label("loc_101C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_101DC")
    OP_29(0x16, 0x1, 0x2)

    label("loc_101DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101F1")
    OP_29(0x16, 0x1, 0x3)

    label("loc_101F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10206")
    OP_29(0x16, 0x1, 0x4)

    label("loc_10206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1021B")
    OP_29(0x16, 0x1, 0x5)

    label("loc_1021B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10230")
    OP_29(0x16, 0x1, 0x6)

    label("loc_10230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10245")
    OP_29(0x16, 0x1, 0x7)

    label("loc_10245")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1025A")
    OP_29(0x16, 0x1, 0x8)

    label("loc_1025A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1026F")
    OP_29(0x16, 0x1, 0x9)

    label("loc_1026F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10284")
    OP_29(0x16, 0x1, 0xA)

    label("loc_10284")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10298")
    OP_29(0x16, 0x4, 0x10)

    label("loc_10298")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_102AC")
    OP_29(0x16, 0x4, 0x20)

    label("loc_102AC")

    Jump("loc_122CC")

    label("loc_102B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1039E")
    OP_29(0x17, 0x3, 0x0)
    OP_29(0x17, 0x3, 0x1)
    OP_29(0x17, 0x3, 0x2)
    OP_29(0x17, 0x3, 0x10)
    OP_29(0x17, 0x3, 0x20)
    OP_29(0x17, 0x3, 0x40)
    OP_29(0x17, 0x2, 0x0)
    OP_29(0x17, 0x2, 0x1)
    OP_29(0x17, 0x2, 0x2)
    OP_29(0x17, 0x2, 0x3)
    OP_29(0x17, 0x2, 0x4)
    OP_29(0x17, 0x2, 0x5)
    OP_29(0x17, 0x2, 0x6)
    OP_29(0x17, 0x2, 0x7)
    OP_29(0x17, 0x2, 0x8)
    OP_29(0x17, 0x2, 0x9)
    OP_29(0x17, 0x2, 0xA)
    OP_29(0x17, 0x2, 0xB)
    OP_29(0x17, 0x2, 0xC)
    OP_29(0x17, 0x2, 0xD)
    OP_29(0x17, 0x2, 0xE)
    OP_29(0x17, 0x2, 0xF)
    OP_29(0x17, 0x2, 0x10)
    OP_29(0x17, 0x2, 0x11)
    OP_29(0x17, 0x2, 0x12)
    OP_29(0x17, 0x2, 0x13)
    OP_29(0x17, 0x2, 0x14)
    OP_29(0x17, 0x2, 0x15)
    OP_29(0x17, 0x2, 0x16)
    OP_29(0x17, 0x2, 0x17)
    OP_29(0x17, 0x2, 0x18)
    OP_29(0x17, 0x2, 0x19)
    OP_29(0x17, 0x2, 0x1A)
    OP_29(0x17, 0x2, 0x1B)
    OP_29(0x17, 0x2, 0x1C)
    OP_29(0x17, 0x2, 0x1D)
    OP_29(0x17, 0x2, 0x1E)
    OP_29(0x17, 0x2, 0x1F)

    label("loc_1039E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_103B2")
    OP_29(0x17, 0x4, 0x2)

    label("loc_103B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_103C7")
    OP_29(0x17, 0x1, 0x0)

    label("loc_103C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_103DC")
    OP_29(0x17, 0x1, 0x2)

    label("loc_103DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_103F1")
    OP_29(0x17, 0x1, 0x4)

    label("loc_103F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10406")
    OP_29(0x17, 0x1, 0x6)

    label("loc_10406")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1041B")
    OP_29(0x17, 0x1, 0x8)

    label("loc_1041B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10430")
    OP_29(0x17, 0x1, 0xA)

    label("loc_10430")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10445")
    OP_29(0x17, 0x1, 0xC)

    label("loc_10445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1045A")
    OP_29(0x17, 0x1, 0xE)

    label("loc_1045A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1046F")
    OP_29(0x17, 0x1, 0x10)

    label("loc_1046F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10484")
    OP_29(0x17, 0x1, 0x12)

    label("loc_10484")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10499")
    OP_29(0x17, 0x1, 0x13)

    label("loc_10499")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104AE")
    OP_29(0x17, 0x1, 0x14)

    label("loc_104AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104C3")
    OP_29(0x17, 0x1, 0x15)

    label("loc_104C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104D8")
    OP_29(0x17, 0x1, 0x16)

    label("loc_104D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104EC")
    OP_29(0x17, 0x4, 0x10)

    label("loc_104EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10500")
    OP_29(0x17, 0x4, 0x20)

    label("loc_10500")

    Jump("loc_122CC")

    label("loc_10505")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105F2")
    OP_29(0x18, 0x3, 0x0)
    OP_29(0x18, 0x3, 0x1)
    OP_29(0x18, 0x3, 0x2)
    OP_29(0x18, 0x3, 0x10)
    OP_29(0x18, 0x3, 0x20)
    OP_29(0x18, 0x3, 0x40)
    OP_29(0x18, 0x2, 0x0)
    OP_29(0x18, 0x2, 0x1)
    OP_29(0x18, 0x2, 0x2)
    OP_29(0x18, 0x2, 0x3)
    OP_29(0x18, 0x2, 0x4)
    OP_29(0x18, 0x2, 0x5)
    OP_29(0x18, 0x2, 0x6)
    OP_29(0x18, 0x2, 0x7)
    OP_29(0x18, 0x2, 0x8)
    OP_29(0x18, 0x2, 0x9)
    OP_29(0x18, 0x2, 0xA)
    OP_29(0x18, 0x2, 0xB)
    OP_29(0x18, 0x2, 0xC)
    OP_29(0x18, 0x2, 0xD)
    OP_29(0x18, 0x2, 0xE)
    OP_29(0x18, 0x2, 0xF)
    OP_29(0x18, 0x2, 0x10)
    OP_29(0x18, 0x2, 0x11)
    OP_29(0x18, 0x2, 0x12)
    OP_29(0x18, 0x2, 0x13)
    OP_29(0x18, 0x2, 0x14)
    OP_29(0x18, 0x2, 0x15)
    OP_29(0x18, 0x2, 0x16)
    OP_29(0x18, 0x2, 0x17)
    OP_29(0x18, 0x2, 0x18)
    OP_29(0x18, 0x2, 0x19)
    OP_29(0x18, 0x2, 0x1A)
    OP_29(0x18, 0x2, 0x1B)
    OP_29(0x18, 0x2, 0x1C)
    OP_29(0x18, 0x2, 0x1D)
    OP_29(0x18, 0x2, 0x1E)
    OP_29(0x18, 0x2, 0x1F)

    label("loc_105F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10606")
    OP_29(0x18, 0x4, 0x2)

    label("loc_10606")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1061B")
    OP_29(0x18, 0x1, 0x0)

    label("loc_1061B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10630")
    OP_29(0x18, 0x1, 0x1)

    label("loc_10630")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10645")
    OP_29(0x18, 0x1, 0x2)

    label("loc_10645")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1065A")
    OP_29(0x18, 0x1, 0x3)

    label("loc_1065A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1066F")
    OP_29(0x18, 0x1, 0x4)

    label("loc_1066F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10684")
    OP_29(0x18, 0x1, 0x5)

    label("loc_10684")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10699")
    OP_29(0x18, 0x1, 0x6)

    label("loc_10699")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_106AE")
    OP_29(0x18, 0x1, 0x7)

    label("loc_106AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_106C3")
    OP_29(0x18, 0x1, 0x8)

    label("loc_106C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_106D8")
    OP_29(0x18, 0x1, 0x9)

    label("loc_106D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_106ED")
    OP_29(0x18, 0x1, 0xA)

    label("loc_106ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10702")
    OP_29(0x18, 0x1, 0xB)

    label("loc_10702")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10717")
    OP_29(0x18, 0x1, 0xC)

    label("loc_10717")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1072B")
    OP_29(0x18, 0x4, 0x10)

    label("loc_1072B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1073F")
    OP_29(0x18, 0x4, 0x20)

    label("loc_1073F")

    Jump("loc_122CC")

    label("loc_10744")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10831")
    OP_29(0x19, 0x3, 0x0)
    OP_29(0x19, 0x3, 0x1)
    OP_29(0x19, 0x3, 0x2)
    OP_29(0x19, 0x3, 0x10)
    OP_29(0x19, 0x3, 0x20)
    OP_29(0x19, 0x3, 0x40)
    OP_29(0x19, 0x2, 0x0)
    OP_29(0x19, 0x2, 0x1)
    OP_29(0x19, 0x2, 0x2)
    OP_29(0x19, 0x2, 0x3)
    OP_29(0x19, 0x2, 0x4)
    OP_29(0x19, 0x2, 0x5)
    OP_29(0x19, 0x2, 0x6)
    OP_29(0x19, 0x2, 0x7)
    OP_29(0x19, 0x2, 0x8)
    OP_29(0x19, 0x2, 0x9)
    OP_29(0x19, 0x2, 0xA)
    OP_29(0x19, 0x2, 0xB)
    OP_29(0x19, 0x2, 0xC)
    OP_29(0x19, 0x2, 0xD)
    OP_29(0x19, 0x2, 0xE)
    OP_29(0x19, 0x2, 0xF)
    OP_29(0x19, 0x2, 0x10)
    OP_29(0x19, 0x2, 0x11)
    OP_29(0x19, 0x2, 0x12)
    OP_29(0x19, 0x2, 0x13)
    OP_29(0x19, 0x2, 0x14)
    OP_29(0x19, 0x2, 0x15)
    OP_29(0x19, 0x2, 0x16)
    OP_29(0x19, 0x2, 0x17)
    OP_29(0x19, 0x2, 0x18)
    OP_29(0x19, 0x2, 0x19)
    OP_29(0x19, 0x2, 0x1A)
    OP_29(0x19, 0x2, 0x1B)
    OP_29(0x19, 0x2, 0x1C)
    OP_29(0x19, 0x2, 0x1D)
    OP_29(0x19, 0x2, 0x1E)
    OP_29(0x19, 0x2, 0x1F)

    label("loc_10831")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10845")
    OP_29(0x19, 0x4, 0x2)

    label("loc_10845")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1085A")
    OP_29(0x19, 0x1, 0x0)

    label("loc_1085A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1086F")
    OP_29(0x19, 0x1, 0x1)

    label("loc_1086F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10884")
    OP_29(0x19, 0x1, 0x2)

    label("loc_10884")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10899")
    OP_29(0x19, 0x1, 0x3)

    label("loc_10899")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_108AE")
    OP_29(0x19, 0x1, 0x4)

    label("loc_108AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_108C3")
    OP_29(0x19, 0x1, 0x5)

    label("loc_108C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_108D7")
    OP_29(0x19, 0x4, 0x10)

    label("loc_108D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_108EB")
    OP_29(0x19, 0x4, 0x20)

    label("loc_108EB")

    Jump("loc_122CC")

    label("loc_108F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109DD")
    OP_29(0x1A, 0x3, 0x0)
    OP_29(0x1A, 0x3, 0x1)
    OP_29(0x1A, 0x3, 0x2)
    OP_29(0x1A, 0x3, 0x10)
    OP_29(0x1A, 0x3, 0x20)
    OP_29(0x1A, 0x3, 0x40)
    OP_29(0x1A, 0x2, 0x0)
    OP_29(0x1A, 0x2, 0x1)
    OP_29(0x1A, 0x2, 0x2)
    OP_29(0x1A, 0x2, 0x3)
    OP_29(0x1A, 0x2, 0x4)
    OP_29(0x1A, 0x2, 0x5)
    OP_29(0x1A, 0x2, 0x6)
    OP_29(0x1A, 0x2, 0x7)
    OP_29(0x1A, 0x2, 0x8)
    OP_29(0x1A, 0x2, 0x9)
    OP_29(0x1A, 0x2, 0xA)
    OP_29(0x1A, 0x2, 0xB)
    OP_29(0x1A, 0x2, 0xC)
    OP_29(0x1A, 0x2, 0xD)
    OP_29(0x1A, 0x2, 0xE)
    OP_29(0x1A, 0x2, 0xF)
    OP_29(0x1A, 0x2, 0x10)
    OP_29(0x1A, 0x2, 0x11)
    OP_29(0x1A, 0x2, 0x12)
    OP_29(0x1A, 0x2, 0x13)
    OP_29(0x1A, 0x2, 0x14)
    OP_29(0x1A, 0x2, 0x15)
    OP_29(0x1A, 0x2, 0x16)
    OP_29(0x1A, 0x2, 0x17)
    OP_29(0x1A, 0x2, 0x18)
    OP_29(0x1A, 0x2, 0x19)
    OP_29(0x1A, 0x2, 0x1A)
    OP_29(0x1A, 0x2, 0x1B)
    OP_29(0x1A, 0x2, 0x1C)
    OP_29(0x1A, 0x2, 0x1D)
    OP_29(0x1A, 0x2, 0x1E)
    OP_29(0x1A, 0x2, 0x1F)

    label("loc_109DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_109F1")
    OP_29(0x1A, 0x4, 0x2)

    label("loc_109F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10A06")
    OP_29(0x1A, 0x1, 0x0)

    label("loc_10A06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10A1B")
    OP_29(0x1A, 0x1, 0x1)

    label("loc_10A1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10A30")
    OP_29(0x1A, 0x1, 0x2)

    label("loc_10A30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10A45")
    OP_29(0x1A, 0x1, 0x3)

    label("loc_10A45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10A5A")
    OP_29(0x1A, 0x1, 0x4)

    label("loc_10A5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10A6F")
    OP_29(0x1A, 0x1, 0x5)

    label("loc_10A6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10A84")
    OP_29(0x1A, 0x1, 0x6)

    label("loc_10A84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10A99")
    OP_29(0x1A, 0x1, 0x7)

    label("loc_10A99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10AAE")
    OP_29(0x1A, 0x1, 0x8)

    label("loc_10AAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10AC3")
    OP_29(0x1A, 0x1, 0x9)

    label("loc_10AC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10AD8")
    OP_29(0x1A, 0x1, 0xA)

    label("loc_10AD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10AED")
    OP_29(0x1A, 0x1, 0xB)

    label("loc_10AED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10B01")
    OP_29(0x1A, 0x4, 0x10)

    label("loc_10B01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10B15")
    OP_29(0x1A, 0x4, 0x20)

    label("loc_10B15")

    Jump("loc_122CC")

    label("loc_10B1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C07")
    OP_29(0x1B, 0x3, 0x0)
    OP_29(0x1B, 0x3, 0x1)
    OP_29(0x1B, 0x3, 0x2)
    OP_29(0x1B, 0x3, 0x10)
    OP_29(0x1B, 0x3, 0x20)
    OP_29(0x1B, 0x3, 0x40)
    OP_29(0x1B, 0x2, 0x0)
    OP_29(0x1B, 0x2, 0x1)
    OP_29(0x1B, 0x2, 0x2)
    OP_29(0x1B, 0x2, 0x3)
    OP_29(0x1B, 0x2, 0x4)
    OP_29(0x1B, 0x2, 0x5)
    OP_29(0x1B, 0x2, 0x6)
    OP_29(0x1B, 0x2, 0x7)
    OP_29(0x1B, 0x2, 0x8)
    OP_29(0x1B, 0x2, 0x9)
    OP_29(0x1B, 0x2, 0xA)
    OP_29(0x1B, 0x2, 0xB)
    OP_29(0x1B, 0x2, 0xC)
    OP_29(0x1B, 0x2, 0xD)
    OP_29(0x1B, 0x2, 0xE)
    OP_29(0x1B, 0x2, 0xF)
    OP_29(0x1B, 0x2, 0x10)
    OP_29(0x1B, 0x2, 0x11)
    OP_29(0x1B, 0x2, 0x12)
    OP_29(0x1B, 0x2, 0x13)
    OP_29(0x1B, 0x2, 0x14)
    OP_29(0x1B, 0x2, 0x15)
    OP_29(0x1B, 0x2, 0x16)
    OP_29(0x1B, 0x2, 0x17)
    OP_29(0x1B, 0x2, 0x18)
    OP_29(0x1B, 0x2, 0x19)
    OP_29(0x1B, 0x2, 0x1A)
    OP_29(0x1B, 0x2, 0x1B)
    OP_29(0x1B, 0x2, 0x1C)
    OP_29(0x1B, 0x2, 0x1D)
    OP_29(0x1B, 0x2, 0x1E)
    OP_29(0x1B, 0x2, 0x1F)

    label("loc_10C07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C1B")
    OP_29(0x1B, 0x4, 0x2)

    label("loc_10C1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C30")
    OP_29(0x1B, 0x1, 0x0)

    label("loc_10C30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C45")
    OP_29(0x1B, 0x1, 0x1)

    label("loc_10C45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C5A")
    OP_29(0x1B, 0x1, 0x2)

    label("loc_10C5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C6F")
    OP_29(0x1B, 0x1, 0x3)

    label("loc_10C6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C84")
    OP_29(0x1B, 0x1, 0x4)

    label("loc_10C84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C99")
    OP_29(0x1A, 0x1, 0xD)

    label("loc_10C99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10CAD")
    OP_29(0x1B, 0x4, 0x10)

    label("loc_10CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10CC1")
    OP_29(0x1B, 0x4, 0x20)

    label("loc_10CC1")

    Jump("loc_122CC")

    label("loc_10CC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DB3")
    OP_29(0x1C, 0x3, 0x0)
    OP_29(0x1C, 0x3, 0x1)
    OP_29(0x1C, 0x3, 0x2)
    OP_29(0x1C, 0x3, 0x10)
    OP_29(0x1C, 0x3, 0x20)
    OP_29(0x1C, 0x3, 0x40)
    OP_29(0x1C, 0x2, 0x0)
    OP_29(0x1C, 0x2, 0x1)
    OP_29(0x1C, 0x2, 0x2)
    OP_29(0x1C, 0x2, 0x3)
    OP_29(0x1C, 0x2, 0x4)
    OP_29(0x1C, 0x2, 0x5)
    OP_29(0x1C, 0x2, 0x6)
    OP_29(0x1C, 0x2, 0x7)
    OP_29(0x1C, 0x2, 0x8)
    OP_29(0x1C, 0x2, 0x9)
    OP_29(0x1C, 0x2, 0xA)
    OP_29(0x1C, 0x2, 0xB)
    OP_29(0x1C, 0x2, 0xC)
    OP_29(0x1C, 0x2, 0xD)
    OP_29(0x1C, 0x2, 0xE)
    OP_29(0x1C, 0x2, 0xF)
    OP_29(0x1C, 0x2, 0x10)
    OP_29(0x1C, 0x2, 0x11)
    OP_29(0x1C, 0x2, 0x12)
    OP_29(0x1C, 0x2, 0x13)
    OP_29(0x1C, 0x2, 0x14)
    OP_29(0x1C, 0x2, 0x15)
    OP_29(0x1C, 0x2, 0x16)
    OP_29(0x1C, 0x2, 0x17)
    OP_29(0x1C, 0x2, 0x18)
    OP_29(0x1C, 0x2, 0x19)
    OP_29(0x1C, 0x2, 0x1A)
    OP_29(0x1C, 0x2, 0x1B)
    OP_29(0x1C, 0x2, 0x1C)
    OP_29(0x1C, 0x2, 0x1D)
    OP_29(0x1C, 0x2, 0x1E)
    OP_29(0x1C, 0x2, 0x1F)

    label("loc_10DB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10DC7")
    OP_29(0x1C, 0x4, 0x2)

    label("loc_10DC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10DE1")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)

    label("loc_10DE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E01")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)

    label("loc_10E01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E27")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)

    label("loc_10E27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E53")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)

    label("loc_10E53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10EB2")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)
    SetScenarioFlags(0xBA, 3)
    SetScenarioFlags(0xBA, 4)
    SetScenarioFlags(0xBA, 5)
    SetScenarioFlags(0xBA, 6)
    SetScenarioFlags(0xBA, 7)
    SetScenarioFlags(0xBB, 0)
    SetScenarioFlags(0xBB, 1)
    SetScenarioFlags(0xBB, 2)
    SetScenarioFlags(0xBB, 3)
    SetScenarioFlags(0xBB, 4)
    SetScenarioFlags(0xBB, 5)
    SetScenarioFlags(0xBB, 6)
    SetScenarioFlags(0xBB, 7)
    SetScenarioFlags(0xBC, 0)
    SetScenarioFlags(0xBC, 1)
    SetScenarioFlags(0xBC, 2)
    SetScenarioFlags(0xBC, 3)

    label("loc_10EB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10F1A")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)
    OP_29(0x1C, 0x1, 0x4)
    SetScenarioFlags(0xBA, 2)
    SetScenarioFlags(0xBA, 3)
    SetScenarioFlags(0xBA, 4)
    SetScenarioFlags(0xBA, 5)
    SetScenarioFlags(0xBA, 6)
    SetScenarioFlags(0xBA, 7)
    SetScenarioFlags(0xBB, 0)
    SetScenarioFlags(0xBB, 1)
    SetScenarioFlags(0xBB, 2)
    SetScenarioFlags(0xBB, 3)
    SetScenarioFlags(0xBB, 4)
    SetScenarioFlags(0xBB, 5)
    SetScenarioFlags(0xBB, 6)
    SetScenarioFlags(0xBB, 7)
    SetScenarioFlags(0xBC, 0)
    SetScenarioFlags(0xBC, 1)
    SetScenarioFlags(0xBC, 2)
    SetScenarioFlags(0xBC, 3)

    label("loc_10F1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10F87")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)
    OP_29(0x1C, 0x1, 0x4)
    SetScenarioFlags(0xBA, 2)
    SetScenarioFlags(0xBA, 3)
    SetScenarioFlags(0xBA, 4)
    SetScenarioFlags(0xBA, 5)
    SetScenarioFlags(0xBA, 6)
    SetScenarioFlags(0xBA, 7)
    SetScenarioFlags(0xBB, 0)
    SetScenarioFlags(0xBB, 1)
    SetScenarioFlags(0xBB, 2)
    SetScenarioFlags(0xBB, 3)
    SetScenarioFlags(0xBB, 4)
    SetScenarioFlags(0xBB, 5)
    SetScenarioFlags(0xBB, 6)
    SetScenarioFlags(0xBB, 7)
    SetScenarioFlags(0xBC, 0)
    SetScenarioFlags(0xBC, 1)
    SetScenarioFlags(0xBC, 2)
    SetScenarioFlags(0xBC, 3)
    OP_29(0x1C, 0x4, 0x10)

    label("loc_10F87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10FF9")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)
    OP_29(0x1C, 0x1, 0x4)
    SetScenarioFlags(0xBA, 2)
    SetScenarioFlags(0xBA, 3)
    SetScenarioFlags(0xBA, 4)
    SetScenarioFlags(0xBA, 5)
    SetScenarioFlags(0xBA, 6)
    SetScenarioFlags(0xBA, 7)
    SetScenarioFlags(0xBB, 0)
    SetScenarioFlags(0xBB, 1)
    SetScenarioFlags(0xBB, 2)
    SetScenarioFlags(0xBB, 3)
    SetScenarioFlags(0xBB, 4)
    SetScenarioFlags(0xBB, 5)
    SetScenarioFlags(0xBB, 6)
    SetScenarioFlags(0xBB, 7)
    SetScenarioFlags(0xBC, 0)
    SetScenarioFlags(0xBC, 1)
    SetScenarioFlags(0xBC, 2)
    SetScenarioFlags(0xBC, 3)
    OP_29(0x1C, 0x4, 0x10)
    OP_29(0x1C, 0x4, 0x20)

    label("loc_10FF9")

    Jump("loc_122CC")

    label("loc_10FFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110EB")
    OP_29(0x1D, 0x3, 0x0)
    OP_29(0x1D, 0x3, 0x1)
    OP_29(0x1D, 0x3, 0x2)
    OP_29(0x1D, 0x3, 0x10)
    OP_29(0x1D, 0x3, 0x20)
    OP_29(0x1D, 0x3, 0x40)
    OP_29(0x1D, 0x2, 0x0)
    OP_29(0x1D, 0x2, 0x1)
    OP_29(0x1D, 0x2, 0x2)
    OP_29(0x1D, 0x2, 0x3)
    OP_29(0x1D, 0x2, 0x4)
    OP_29(0x1D, 0x2, 0x5)
    OP_29(0x1D, 0x2, 0x6)
    OP_29(0x1D, 0x2, 0x7)
    OP_29(0x1D, 0x2, 0x8)
    OP_29(0x1D, 0x2, 0x9)
    OP_29(0x1D, 0x2, 0xA)
    OP_29(0x1D, 0x2, 0xB)
    OP_29(0x1D, 0x2, 0xC)
    OP_29(0x1D, 0x2, 0xD)
    OP_29(0x1D, 0x2, 0xE)
    OP_29(0x1D, 0x2, 0xF)
    OP_29(0x1D, 0x2, 0x10)
    OP_29(0x1D, 0x2, 0x11)
    OP_29(0x1D, 0x2, 0x12)
    OP_29(0x1D, 0x2, 0x13)
    OP_29(0x1D, 0x2, 0x14)
    OP_29(0x1D, 0x2, 0x15)
    OP_29(0x1D, 0x2, 0x16)
    OP_29(0x1D, 0x2, 0x17)
    OP_29(0x1D, 0x2, 0x18)
    OP_29(0x1D, 0x2, 0x19)
    OP_29(0x1D, 0x2, 0x1A)
    OP_29(0x1D, 0x2, 0x1B)
    OP_29(0x1D, 0x2, 0x1C)
    OP_29(0x1D, 0x2, 0x1D)
    OP_29(0x1D, 0x2, 0x1E)
    OP_29(0x1D, 0x2, 0x1F)

    label("loc_110EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_110FF")
    OP_29(0x1D, 0x4, 0x2)

    label("loc_110FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11114")
    OP_29(0x1D, 0x1, 0x0)

    label("loc_11114")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11129")
    OP_29(0x1D, 0x1, 0x1)

    label("loc_11129")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1113E")
    OP_29(0x1D, 0x1, 0x2)

    label("loc_1113E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11153")
    OP_29(0x1D, 0x1, 0x3)

    label("loc_11153")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11168")
    OP_29(0x1D, 0x1, 0x4)

    label("loc_11168")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1117D")
    OP_29(0x1D, 0x1, 0x5)

    label("loc_1117D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11192")
    OP_29(0x1D, 0x1, 0x6)

    label("loc_11192")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_111A7")
    OP_29(0x1D, 0x1, 0x7)

    label("loc_111A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_111BC")
    OP_29(0x1D, 0x1, 0x8)

    label("loc_111BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_111D1")
    OP_29(0x1D, 0x1, 0x9)

    label("loc_111D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_111E6")
    OP_29(0x1D, 0x1, 0xA)

    label("loc_111E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_111FB")
    OP_29(0x1D, 0x1, 0xB)

    label("loc_111FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1120F")
    OP_29(0x1D, 0x4, 0x10)

    label("loc_1120F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11223")
    OP_29(0x1D, 0x4, 0x20)

    label("loc_11223")

    Jump("loc_122CC")

    label("loc_11228")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11315")
    OP_29(0x1E, 0x3, 0x0)
    OP_29(0x1E, 0x3, 0x1)
    OP_29(0x1E, 0x3, 0x2)
    OP_29(0x1E, 0x3, 0x10)
    OP_29(0x1E, 0x3, 0x20)
    OP_29(0x1E, 0x3, 0x40)
    OP_29(0x1E, 0x2, 0x0)
    OP_29(0x1E, 0x2, 0x1)
    OP_29(0x1E, 0x2, 0x2)
    OP_29(0x1E, 0x2, 0x3)
    OP_29(0x1E, 0x2, 0x4)
    OP_29(0x1E, 0x2, 0x5)
    OP_29(0x1E, 0x2, 0x6)
    OP_29(0x1E, 0x2, 0x7)
    OP_29(0x1E, 0x2, 0x8)
    OP_29(0x1E, 0x2, 0x9)
    OP_29(0x1E, 0x2, 0xA)
    OP_29(0x1E, 0x2, 0xB)
    OP_29(0x1E, 0x2, 0xC)
    OP_29(0x1E, 0x2, 0xD)
    OP_29(0x1E, 0x2, 0xE)
    OP_29(0x1E, 0x2, 0xF)
    OP_29(0x1E, 0x2, 0x10)
    OP_29(0x1E, 0x2, 0x11)
    OP_29(0x1E, 0x2, 0x12)
    OP_29(0x1E, 0x2, 0x13)
    OP_29(0x1E, 0x2, 0x14)
    OP_29(0x1E, 0x2, 0x15)
    OP_29(0x1E, 0x2, 0x16)
    OP_29(0x1E, 0x2, 0x17)
    OP_29(0x1E, 0x2, 0x18)
    OP_29(0x1E, 0x2, 0x19)
    OP_29(0x1E, 0x2, 0x1A)
    OP_29(0x1E, 0x2, 0x1B)
    OP_29(0x1E, 0x2, 0x1C)
    OP_29(0x1E, 0x2, 0x1D)
    OP_29(0x1E, 0x2, 0x1E)
    OP_29(0x1E, 0x2, 0x1F)

    label("loc_11315")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11329")
    OP_29(0x1E, 0x4, 0x2)

    label("loc_11329")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1133E")
    OP_29(0x1E, 0x1, 0x0)

    label("loc_1133E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11353")
    OP_29(0x1E, 0x1, 0x1)

    label("loc_11353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11368")
    OP_29(0x1E, 0x1, 0x2)

    label("loc_11368")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1137D")
    OP_29(0x1E, 0x1, 0x3)

    label("loc_1137D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11392")
    OP_29(0x1E, 0x1, 0x4)

    label("loc_11392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_113A7")
    OP_29(0x1E, 0x1, 0x5)

    label("loc_113A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_113BC")
    OP_29(0x1E, 0x1, 0x6)

    label("loc_113BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_113D1")
    OP_29(0x1E, 0x1, 0x7)

    label("loc_113D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_113E6")
    OP_29(0x1E, 0x1, 0x8)

    label("loc_113E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_113FB")
    OP_29(0x1E, 0x1, 0x9)

    label("loc_113FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11410")
    OP_29(0x1E, 0x1, 0xA)

    label("loc_11410")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11425")
    OP_29(0x1E, 0x1, 0xB)

    label("loc_11425")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11439")
    OP_29(0x1E, 0x4, 0x10)

    label("loc_11439")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1144D")
    OP_29(0x1E, 0x4, 0x20)

    label("loc_1144D")

    Jump("loc_122CC")

    label("loc_11452")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1153F")
    OP_29(0x1F, 0x3, 0x0)
    OP_29(0x1F, 0x3, 0x1)
    OP_29(0x1F, 0x3, 0x2)
    OP_29(0x1F, 0x3, 0x10)
    OP_29(0x1F, 0x3, 0x20)
    OP_29(0x1F, 0x3, 0x40)
    OP_29(0x1F, 0x2, 0x0)
    OP_29(0x1F, 0x2, 0x1)
    OP_29(0x1F, 0x2, 0x2)
    OP_29(0x1F, 0x2, 0x3)
    OP_29(0x1F, 0x2, 0x4)
    OP_29(0x1F, 0x2, 0x5)
    OP_29(0x1F, 0x2, 0x6)
    OP_29(0x1F, 0x2, 0x7)
    OP_29(0x1F, 0x2, 0x8)
    OP_29(0x1F, 0x2, 0x9)
    OP_29(0x1F, 0x2, 0xA)
    OP_29(0x1F, 0x2, 0xB)
    OP_29(0x1F, 0x2, 0xC)
    OP_29(0x1F, 0x2, 0xD)
    OP_29(0x1F, 0x2, 0xE)
    OP_29(0x1F, 0x2, 0xF)
    OP_29(0x1F, 0x2, 0x10)
    OP_29(0x1F, 0x2, 0x11)
    OP_29(0x1F, 0x2, 0x12)
    OP_29(0x1F, 0x2, 0x13)
    OP_29(0x1F, 0x2, 0x14)
    OP_29(0x1F, 0x2, 0x15)
    OP_29(0x1F, 0x2, 0x16)
    OP_29(0x1F, 0x2, 0x17)
    OP_29(0x1F, 0x2, 0x18)
    OP_29(0x1F, 0x2, 0x19)
    OP_29(0x1F, 0x2, 0x1A)
    OP_29(0x1F, 0x2, 0x1B)
    OP_29(0x1F, 0x2, 0x1C)
    OP_29(0x1F, 0x2, 0x1D)
    OP_29(0x1F, 0x2, 0x1E)
    OP_29(0x1F, 0x2, 0x1F)

    label("loc_1153F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11553")
    OP_29(0x1F, 0x4, 0x2)

    label("loc_11553")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11568")
    OP_29(0x1F, 0x1, 0x0)

    label("loc_11568")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1157D")
    OP_29(0x1F, 0x1, 0x1)

    label("loc_1157D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11592")
    OP_29(0x1F, 0x1, 0x2)

    label("loc_11592")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_115A7")
    OP_29(0x1F, 0x1, 0x3)

    label("loc_115A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_115BC")
    OP_29(0x1F, 0x1, 0x4)

    label("loc_115BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_115D1")
    OP_29(0x1F, 0x1, 0x5)

    label("loc_115D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_115E6")
    OP_29(0x1F, 0x1, 0x6)

    label("loc_115E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_115FB")
    OP_29(0x1F, 0x1, 0x7)

    label("loc_115FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11610")
    OP_29(0x1F, 0x1, 0x8)

    label("loc_11610")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11625")
    OP_29(0x1F, 0x1, 0x9)

    label("loc_11625")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1163A")
    OP_29(0x1F, 0x1, 0xA)

    label("loc_1163A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1164F")
    OP_29(0x1F, 0x1, 0xB)

    label("loc_1164F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11663")
    OP_29(0x1F, 0x4, 0x10)

    label("loc_11663")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11677")
    OP_29(0x1F, 0x4, 0x20)

    label("loc_11677")

    Jump("loc_122CC")

    label("loc_1167C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11769")
    OP_29(0x20, 0x3, 0x0)
    OP_29(0x20, 0x3, 0x1)
    OP_29(0x20, 0x3, 0x2)
    OP_29(0x20, 0x3, 0x10)
    OP_29(0x20, 0x3, 0x20)
    OP_29(0x20, 0x3, 0x40)
    OP_29(0x20, 0x2, 0x0)
    OP_29(0x20, 0x2, 0x1)
    OP_29(0x20, 0x2, 0x2)
    OP_29(0x20, 0x2, 0x3)
    OP_29(0x20, 0x2, 0x4)
    OP_29(0x20, 0x2, 0x5)
    OP_29(0x20, 0x2, 0x6)
    OP_29(0x20, 0x2, 0x7)
    OP_29(0x20, 0x2, 0x8)
    OP_29(0x20, 0x2, 0x9)
    OP_29(0x20, 0x2, 0xA)
    OP_29(0x20, 0x2, 0xB)
    OP_29(0x20, 0x2, 0xC)
    OP_29(0x20, 0x2, 0xD)
    OP_29(0x20, 0x2, 0xE)
    OP_29(0x20, 0x2, 0xF)
    OP_29(0x20, 0x2, 0x10)
    OP_29(0x20, 0x2, 0x11)
    OP_29(0x20, 0x2, 0x12)
    OP_29(0x20, 0x2, 0x13)
    OP_29(0x20, 0x2, 0x14)
    OP_29(0x20, 0x2, 0x15)
    OP_29(0x20, 0x2, 0x16)
    OP_29(0x20, 0x2, 0x17)
    OP_29(0x20, 0x2, 0x18)
    OP_29(0x20, 0x2, 0x19)
    OP_29(0x20, 0x2, 0x1A)
    OP_29(0x20, 0x2, 0x1B)
    OP_29(0x20, 0x2, 0x1C)
    OP_29(0x20, 0x2, 0x1D)
    OP_29(0x20, 0x2, 0x1E)
    OP_29(0x20, 0x2, 0x1F)

    label("loc_11769")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1177D")
    OP_29(0x20, 0x4, 0x2)

    label("loc_1177D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11792")
    OP_29(0x20, 0x1, 0x0)

    label("loc_11792")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_117A7")
    OP_29(0x20, 0x1, 0x1)

    label("loc_117A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_117BC")
    OP_29(0x20, 0x1, 0x2)

    label("loc_117BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_117D1")
    OP_29(0x20, 0x1, 0x3)

    label("loc_117D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_117E6")
    OP_29(0x20, 0x1, 0x4)

    label("loc_117E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_117FB")
    OP_29(0x20, 0x1, 0x5)

    label("loc_117FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11810")
    OP_29(0x20, 0x1, 0x6)

    label("loc_11810")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11825")
    OP_29(0x20, 0x1, 0x7)

    label("loc_11825")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1183A")
    OP_29(0x20, 0x1, 0x8)

    label("loc_1183A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1184F")
    OP_29(0x20, 0x1, 0x9)

    label("loc_1184F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11864")
    OP_29(0x20, 0x1, 0xA)

    label("loc_11864")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11879")
    OP_29(0x20, 0x1, 0xB)

    label("loc_11879")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1188E")
    OP_29(0x20, 0x1, 0xC)

    label("loc_1188E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_118A3")
    OP_29(0x20, 0x1, 0xD)

    label("loc_118A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_118B8")
    OP_29(0x20, 0x1, 0xE)

    label("loc_118B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_118CD")
    OP_29(0x20, 0x1, 0xF)

    label("loc_118CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_118E2")
    OP_29(0x20, 0x1, 0x10)

    label("loc_118E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_118F7")
    OP_29(0x20, 0x1, 0x11)

    label("loc_118F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1190C")
    OP_29(0x20, 0x1, 0x12)

    label("loc_1190C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11921")
    OP_29(0x20, 0x1, 0x13)

    label("loc_11921")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11936")
    OP_29(0x20, 0x1, 0x14)

    label("loc_11936")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1194B")
    OP_29(0x20, 0x1, 0x15)

    label("loc_1194B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1196B")
    SetScenarioFlags(0x5C, 4)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_11A06")

    label("loc_1196B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1198B")
    SetScenarioFlags(0x5C, 1)
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Jump("loc_11A06")

    label("loc_1198B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119AB")
    SetScenarioFlags(0x5C, 3)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Jump("loc_11A06")

    label("loc_119AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119CB")
    SetScenarioFlags(0x5C, 2)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Jump("loc_11A06")

    label("loc_119CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119EB")
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_11A06")

    label("loc_119EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A06")
    SetScenarioFlags(0x5C, 1)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()

    label("loc_11A06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11A1F")
    OP_29(0x20, 0x4, 0x10)
    OP_29(0x20, 0x4, 0x20)

    label("loc_11A1F")

    Jump("loc_122CC")

    label("loc_11A24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B11")
    OP_29(0x21, 0x3, 0x0)
    OP_29(0x21, 0x3, 0x1)
    OP_29(0x21, 0x3, 0x2)
    OP_29(0x21, 0x3, 0x10)
    OP_29(0x21, 0x3, 0x20)
    OP_29(0x21, 0x3, 0x40)
    OP_29(0x21, 0x2, 0x0)
    OP_29(0x21, 0x2, 0x1)
    OP_29(0x21, 0x2, 0x2)
    OP_29(0x21, 0x2, 0x3)
    OP_29(0x21, 0x2, 0x4)
    OP_29(0x21, 0x2, 0x5)
    OP_29(0x21, 0x2, 0x6)
    OP_29(0x21, 0x2, 0x7)
    OP_29(0x21, 0x2, 0x8)
    OP_29(0x21, 0x2, 0x9)
    OP_29(0x21, 0x2, 0xA)
    OP_29(0x21, 0x2, 0xB)
    OP_29(0x21, 0x2, 0xC)
    OP_29(0x21, 0x2, 0xD)
    OP_29(0x21, 0x2, 0xE)
    OP_29(0x21, 0x2, 0xF)
    OP_29(0x21, 0x2, 0x10)
    OP_29(0x21, 0x2, 0x11)
    OP_29(0x21, 0x2, 0x12)
    OP_29(0x21, 0x2, 0x13)
    OP_29(0x21, 0x2, 0x14)
    OP_29(0x21, 0x2, 0x15)
    OP_29(0x21, 0x2, 0x16)
    OP_29(0x21, 0x2, 0x17)
    OP_29(0x21, 0x2, 0x18)
    OP_29(0x21, 0x2, 0x19)
    OP_29(0x21, 0x2, 0x1A)
    OP_29(0x21, 0x2, 0x1B)
    OP_29(0x21, 0x2, 0x1C)
    OP_29(0x21, 0x2, 0x1D)
    OP_29(0x21, 0x2, 0x1E)
    OP_29(0x21, 0x2, 0x1F)

    label("loc_11B11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B25")
    OP_29(0x21, 0x4, 0x2)

    label("loc_11B25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B3A")
    OP_29(0x21, 0x1, 0x0)

    label("loc_11B3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B4F")
    OP_29(0x21, 0x1, 0x1)

    label("loc_11B4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B64")
    OP_29(0x21, 0x1, 0x2)

    label("loc_11B64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B79")
    OP_29(0x21, 0x1, 0x3)

    label("loc_11B79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B8E")
    OP_29(0x21, 0x1, 0x4)

    label("loc_11B8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11BA3")
    OP_29(0x21, 0x1, 0x5)

    label("loc_11BA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11BB8")
    OP_29(0x21, 0x1, 0x6)

    label("loc_11BB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11BCD")
    OP_29(0x21, 0x1, 0x7)

    label("loc_11BCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11BE2")
    OP_29(0x21, 0x1, 0x8)

    label("loc_11BE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11BF7")
    OP_29(0x21, 0x1, 0x9)

    label("loc_11BF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11C0C")
    OP_29(0x21, 0x1, 0xA)

    label("loc_11C0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11C21")
    OP_29(0x21, 0x1, 0xB)

    label("loc_11C21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11C35")
    OP_29(0x21, 0x4, 0x10)

    label("loc_11C35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11C49")
    OP_29(0x21, 0x4, 0x20)

    label("loc_11C49")

    Jump("loc_122CC")

    label("loc_11C4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D3B")
    OP_29(0x22, 0x3, 0x0)
    OP_29(0x22, 0x3, 0x1)
    OP_29(0x22, 0x3, 0x2)
    OP_29(0x22, 0x3, 0x10)
    OP_29(0x22, 0x3, 0x20)
    OP_29(0x22, 0x3, 0x40)
    OP_29(0x22, 0x2, 0x0)
    OP_29(0x22, 0x2, 0x1)
    OP_29(0x22, 0x2, 0x2)
    OP_29(0x22, 0x2, 0x3)
    OP_29(0x22, 0x2, 0x4)
    OP_29(0x22, 0x2, 0x5)
    OP_29(0x22, 0x2, 0x6)
    OP_29(0x22, 0x2, 0x7)
    OP_29(0x22, 0x2, 0x8)
    OP_29(0x22, 0x2, 0x9)
    OP_29(0x22, 0x2, 0xA)
    OP_29(0x22, 0x2, 0xB)
    OP_29(0x22, 0x2, 0xC)
    OP_29(0x22, 0x2, 0xD)
    OP_29(0x22, 0x2, 0xE)
    OP_29(0x22, 0x2, 0xF)
    OP_29(0x22, 0x2, 0x10)
    OP_29(0x22, 0x2, 0x11)
    OP_29(0x22, 0x2, 0x12)
    OP_29(0x22, 0x2, 0x13)
    OP_29(0x22, 0x2, 0x14)
    OP_29(0x22, 0x2, 0x15)
    OP_29(0x22, 0x2, 0x16)
    OP_29(0x22, 0x2, 0x17)
    OP_29(0x22, 0x2, 0x18)
    OP_29(0x22, 0x2, 0x19)
    OP_29(0x22, 0x2, 0x1A)
    OP_29(0x22, 0x2, 0x1B)
    OP_29(0x22, 0x2, 0x1C)
    OP_29(0x22, 0x2, 0x1D)
    OP_29(0x22, 0x2, 0x1E)
    OP_29(0x22, 0x2, 0x1F)

    label("loc_11D3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D4F")
    OP_29(0x22, 0x4, 0x2)

    label("loc_11D4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D64")
    OP_29(0x22, 0x1, 0x0)

    label("loc_11D64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D79")
    OP_29(0x22, 0x1, 0x1)

    label("loc_11D79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D8E")
    OP_29(0x22, 0x1, 0x2)

    label("loc_11D8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11DA3")
    OP_29(0x22, 0x1, 0x3)

    label("loc_11DA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11DB8")
    OP_29(0x22, 0x1, 0x4)

    label("loc_11DB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11DCD")
    OP_29(0x22, 0x1, 0x5)

    label("loc_11DCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11DE2")
    OP_29(0x22, 0x1, 0x6)

    label("loc_11DE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11DF7")
    OP_29(0x22, 0x1, 0x7)

    label("loc_11DF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11E0C")
    OP_29(0x22, 0x1, 0x8)

    label("loc_11E0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11E21")
    OP_29(0x22, 0x1, 0x9)

    label("loc_11E21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11E36")
    OP_29(0x22, 0x1, 0xA)

    label("loc_11E36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11E4B")
    OP_29(0x22, 0x1, 0xB)

    label("loc_11E4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11E5F")
    OP_29(0x22, 0x4, 0x10)

    label("loc_11E5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11E73")
    OP_29(0x22, 0x4, 0x20)

    label("loc_11E73")

    Jump("loc_122CC")

    label("loc_11E78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F65")
    OP_29(0x23, 0x3, 0x0)
    OP_29(0x23, 0x3, 0x1)
    OP_29(0x23, 0x3, 0x2)
    OP_29(0x23, 0x3, 0x10)
    OP_29(0x23, 0x3, 0x20)
    OP_29(0x23, 0x3, 0x40)
    OP_29(0x23, 0x2, 0x0)
    OP_29(0x23, 0x2, 0x1)
    OP_29(0x23, 0x2, 0x2)
    OP_29(0x23, 0x2, 0x3)
    OP_29(0x23, 0x2, 0x4)
    OP_29(0x23, 0x2, 0x5)
    OP_29(0x23, 0x2, 0x6)
    OP_29(0x23, 0x2, 0x7)
    OP_29(0x23, 0x2, 0x8)
    OP_29(0x23, 0x2, 0x9)
    OP_29(0x23, 0x2, 0xA)
    OP_29(0x23, 0x2, 0xB)
    OP_29(0x23, 0x2, 0xC)
    OP_29(0x23, 0x2, 0xD)
    OP_29(0x23, 0x2, 0xE)
    OP_29(0x23, 0x2, 0xF)
    OP_29(0x23, 0x2, 0x10)
    OP_29(0x23, 0x2, 0x11)
    OP_29(0x23, 0x2, 0x12)
    OP_29(0x23, 0x2, 0x13)
    OP_29(0x23, 0x2, 0x14)
    OP_29(0x23, 0x2, 0x15)
    OP_29(0x23, 0x2, 0x16)
    OP_29(0x23, 0x2, 0x17)
    OP_29(0x23, 0x2, 0x18)
    OP_29(0x23, 0x2, 0x19)
    OP_29(0x23, 0x2, 0x1A)
    OP_29(0x23, 0x2, 0x1B)
    OP_29(0x23, 0x2, 0x1C)
    OP_29(0x23, 0x2, 0x1D)
    OP_29(0x23, 0x2, 0x1E)
    OP_29(0x23, 0x2, 0x1F)

    label("loc_11F65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11F79")
    OP_29(0x23, 0x4, 0x2)

    label("loc_11F79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11F8E")
    OP_29(0x23, 0x1, 0x0)

    label("loc_11F8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11FA3")
    OP_29(0x23, 0x1, 0x1)

    label("loc_11FA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11FB8")
    OP_29(0x23, 0x1, 0x2)

    label("loc_11FB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11FCD")
    OP_29(0x23, 0x1, 0x3)

    label("loc_11FCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11FE2")
    OP_29(0x23, 0x1, 0x4)

    label("loc_11FE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11FF7")
    OP_29(0x23, 0x1, 0x5)

    label("loc_11FF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1200C")
    OP_29(0x23, 0x1, 0x6)

    label("loc_1200C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12021")
    OP_29(0x23, 0x1, 0x7)

    label("loc_12021")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12036")
    OP_29(0x23, 0x1, 0x8)

    label("loc_12036")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1204B")
    OP_29(0x23, 0x1, 0x9)

    label("loc_1204B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12060")
    OP_29(0x23, 0x1, 0xA)

    label("loc_12060")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12075")
    OP_29(0x23, 0x1, 0xB)

    label("loc_12075")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12089")
    OP_29(0x23, 0x4, 0x10)

    label("loc_12089")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1209D")
    OP_29(0x23, 0x4, 0x20)

    label("loc_1209D")

    Jump("loc_122CC")

    label("loc_120A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1218F")
    OP_29(0x24, 0x3, 0x0)
    OP_29(0x24, 0x3, 0x1)
    OP_29(0x24, 0x3, 0x2)
    OP_29(0x24, 0x3, 0x10)
    OP_29(0x24, 0x3, 0x20)
    OP_29(0x24, 0x3, 0x40)
    OP_29(0x24, 0x2, 0x0)
    OP_29(0x24, 0x2, 0x1)
    OP_29(0x24, 0x2, 0x2)
    OP_29(0x24, 0x2, 0x3)
    OP_29(0x24, 0x2, 0x4)
    OP_29(0x24, 0x2, 0x5)
    OP_29(0x24, 0x2, 0x6)
    OP_29(0x24, 0x2, 0x7)
    OP_29(0x24, 0x2, 0x8)
    OP_29(0x24, 0x2, 0x9)
    OP_29(0x24, 0x2, 0xA)
    OP_29(0x24, 0x2, 0xB)
    OP_29(0x24, 0x2, 0xC)
    OP_29(0x24, 0x2, 0xD)
    OP_29(0x24, 0x2, 0xE)
    OP_29(0x24, 0x2, 0xF)
    OP_29(0x24, 0x2, 0x10)
    OP_29(0x24, 0x2, 0x11)
    OP_29(0x24, 0x2, 0x12)
    OP_29(0x24, 0x2, 0x13)
    OP_29(0x24, 0x2, 0x14)
    OP_29(0x24, 0x2, 0x15)
    OP_29(0x24, 0x2, 0x16)
    OP_29(0x24, 0x2, 0x17)
    OP_29(0x24, 0x2, 0x18)
    OP_29(0x24, 0x2, 0x19)
    OP_29(0x24, 0x2, 0x1A)
    OP_29(0x24, 0x2, 0x1B)
    OP_29(0x24, 0x2, 0x1C)
    OP_29(0x24, 0x2, 0x1D)
    OP_29(0x24, 0x2, 0x1E)
    OP_29(0x24, 0x2, 0x1F)

    label("loc_1218F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_121A3")
    OP_29(0x24, 0x4, 0x2)

    label("loc_121A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_121B8")
    OP_29(0x24, 0x1, 0x0)

    label("loc_121B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_121CD")
    OP_29(0x24, 0x1, 0x1)

    label("loc_121CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_121E2")
    OP_29(0x24, 0x1, 0x2)

    label("loc_121E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_121F7")
    OP_29(0x24, 0x1, 0x3)

    label("loc_121F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1220C")
    OP_29(0x24, 0x1, 0x4)

    label("loc_1220C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12221")
    OP_29(0x24, 0x1, 0x5)

    label("loc_12221")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12236")
    OP_29(0x24, 0x1, 0x6)

    label("loc_12236")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1224B")
    OP_29(0x24, 0x1, 0x7)

    label("loc_1224B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12260")
    OP_29(0x24, 0x1, 0x8)

    label("loc_12260")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12275")
    OP_29(0x24, 0x1, 0x9)

    label("loc_12275")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1228A")
    OP_29(0x24, 0x1, 0xA)

    label("loc_1228A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1229F")
    OP_29(0x24, 0x1, 0xB)

    label("loc_1229F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_122B3")
    OP_29(0x24, 0x4, 0x10)

    label("loc_122B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_122C7")
    OP_29(0x24, 0x4, 0x20)

    label("loc_122C7")

    Jump("loc_122CC")

    label("loc_122CC")

    Jump("loc_F18F")

    label("loc_122D1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_57_F185 end

    def Function_58_122E9(): pass

    label("Function_58_122E9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_122F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12AE1")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "-- Intermission --\x01",                              # 0
            "QS_0401 - Prepare Monsters ⑨\x01",                   # 1
            "QS_0402 - Request for Mayor\x01",                     # 2
            "QS_0403 - Temporary Sunday School Lecturer\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_123A2"),
        (2, "loc_123A2"),
        (3, "loc_123A2"),
        (SWITCH_DEFAULT, "loc_12421"),
    )


    label("loc_123A2")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",         # 0
            "Start\x01",         # 1
            "QF_01\x01",         # 2
            "QF_02\x01",         # 3
            "QF_03\x01",         # 4
            "QF_04\x01",         # 5
            "QF_05\x01",         # 6
            "QF_06\x01",         # 7
            "QF_07\x01",         # 8
            "QF_08\x01",         # 9
            "QF_09\x01",         # 10
            "QF_10\x01",         # 11
            "QF_11\x01",         # 12
            "QF_12\x01",         # 13
            "Complete\x01",      # 14
            "Report\x01",        # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_12430")

    label("loc_12421")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12430")

    label("loc_12430")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12ADC")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1245E"),
        (2, "loc_12688"),
        (3, "loc_128B2"),
        (SWITCH_DEFAULT, "loc_12ADC"),
    )


    label("loc_1245E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1254B")
    OP_29(0x25, 0x3, 0x0)
    OP_29(0x25, 0x3, 0x1)
    OP_29(0x25, 0x3, 0x2)
    OP_29(0x25, 0x3, 0x10)
    OP_29(0x25, 0x3, 0x20)
    OP_29(0x25, 0x3, 0x40)
    OP_29(0x25, 0x2, 0x0)
    OP_29(0x25, 0x2, 0x1)
    OP_29(0x25, 0x2, 0x2)
    OP_29(0x25, 0x2, 0x3)
    OP_29(0x25, 0x2, 0x4)
    OP_29(0x25, 0x2, 0x5)
    OP_29(0x25, 0x2, 0x6)
    OP_29(0x25, 0x2, 0x7)
    OP_29(0x25, 0x2, 0x8)
    OP_29(0x25, 0x2, 0x9)
    OP_29(0x25, 0x2, 0xA)
    OP_29(0x25, 0x2, 0xB)
    OP_29(0x25, 0x2, 0xC)
    OP_29(0x25, 0x2, 0xD)
    OP_29(0x25, 0x2, 0xE)
    OP_29(0x25, 0x2, 0xF)
    OP_29(0x25, 0x2, 0x10)
    OP_29(0x25, 0x2, 0x11)
    OP_29(0x25, 0x2, 0x12)
    OP_29(0x25, 0x2, 0x13)
    OP_29(0x25, 0x2, 0x14)
    OP_29(0x25, 0x2, 0x15)
    OP_29(0x25, 0x2, 0x16)
    OP_29(0x25, 0x2, 0x17)
    OP_29(0x25, 0x2, 0x18)
    OP_29(0x25, 0x2, 0x19)
    OP_29(0x25, 0x2, 0x1A)
    OP_29(0x25, 0x2, 0x1B)
    OP_29(0x25, 0x2, 0x1C)
    OP_29(0x25, 0x2, 0x1D)
    OP_29(0x25, 0x2, 0x1E)
    OP_29(0x25, 0x2, 0x1F)

    label("loc_1254B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1255F")
    OP_29(0x25, 0x4, 0x2)

    label("loc_1255F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12574")
    OP_29(0x25, 0x1, 0x0)

    label("loc_12574")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12589")
    OP_29(0x25, 0x1, 0x1)

    label("loc_12589")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1259E")
    OP_29(0x25, 0x1, 0x2)

    label("loc_1259E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_125B3")
    OP_29(0x25, 0x1, 0x3)

    label("loc_125B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_125C8")
    OP_29(0x25, 0x1, 0x4)

    label("loc_125C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_125DD")
    OP_29(0x25, 0x1, 0x5)

    label("loc_125DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_125F2")
    OP_29(0x25, 0x1, 0x6)

    label("loc_125F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12607")
    OP_29(0x25, 0x1, 0x7)

    label("loc_12607")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1261C")
    OP_29(0x25, 0x1, 0x8)

    label("loc_1261C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12631")
    OP_29(0x25, 0x1, 0x9)

    label("loc_12631")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12646")
    OP_29(0x25, 0x1, 0xA)

    label("loc_12646")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1265B")
    OP_29(0x25, 0x1, 0xB)

    label("loc_1265B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1266F")
    OP_29(0x25, 0x4, 0x10)

    label("loc_1266F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12683")
    OP_29(0x25, 0x4, 0x20)

    label("loc_12683")

    Jump("loc_12ADC")

    label("loc_12688")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12775")
    OP_29(0x26, 0x3, 0x0)
    OP_29(0x26, 0x3, 0x1)
    OP_29(0x26, 0x3, 0x2)
    OP_29(0x26, 0x3, 0x10)
    OP_29(0x26, 0x3, 0x20)
    OP_29(0x26, 0x3, 0x40)
    OP_29(0x26, 0x2, 0x0)
    OP_29(0x26, 0x2, 0x1)
    OP_29(0x26, 0x2, 0x2)
    OP_29(0x26, 0x2, 0x3)
    OP_29(0x26, 0x2, 0x4)
    OP_29(0x26, 0x2, 0x5)
    OP_29(0x26, 0x2, 0x6)
    OP_29(0x26, 0x2, 0x7)
    OP_29(0x26, 0x2, 0x8)
    OP_29(0x26, 0x2, 0x9)
    OP_29(0x26, 0x2, 0xA)
    OP_29(0x26, 0x2, 0xB)
    OP_29(0x26, 0x2, 0xC)
    OP_29(0x26, 0x2, 0xD)
    OP_29(0x26, 0x2, 0xE)
    OP_29(0x26, 0x2, 0xF)
    OP_29(0x26, 0x2, 0x10)
    OP_29(0x26, 0x2, 0x11)
    OP_29(0x26, 0x2, 0x12)
    OP_29(0x26, 0x2, 0x13)
    OP_29(0x26, 0x2, 0x14)
    OP_29(0x26, 0x2, 0x15)
    OP_29(0x26, 0x2, 0x16)
    OP_29(0x26, 0x2, 0x17)
    OP_29(0x26, 0x2, 0x18)
    OP_29(0x26, 0x2, 0x19)
    OP_29(0x26, 0x2, 0x1A)
    OP_29(0x26, 0x2, 0x1B)
    OP_29(0x26, 0x2, 0x1C)
    OP_29(0x26, 0x2, 0x1D)
    OP_29(0x26, 0x2, 0x1E)
    OP_29(0x26, 0x2, 0x1F)

    label("loc_12775")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12789")
    OP_29(0x26, 0x4, 0x2)

    label("loc_12789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1279E")
    OP_29(0x26, 0x1, 0x0)

    label("loc_1279E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_127B3")
    OP_29(0x26, 0x1, 0x1)

    label("loc_127B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_127C8")
    OP_29(0x26, 0x1, 0x2)

    label("loc_127C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_127DD")
    OP_29(0x26, 0x1, 0x3)

    label("loc_127DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_127F2")
    OP_29(0x26, 0x1, 0x4)

    label("loc_127F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12807")
    OP_29(0x26, 0x1, 0x5)

    label("loc_12807")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1281C")
    OP_29(0x26, 0x1, 0x6)

    label("loc_1281C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12831")
    OP_29(0x26, 0x1, 0x7)

    label("loc_12831")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12846")
    OP_29(0x26, 0x1, 0x8)

    label("loc_12846")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1285B")
    OP_29(0x26, 0x1, 0x9)

    label("loc_1285B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12870")
    OP_29(0x26, 0x1, 0xA)

    label("loc_12870")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12885")
    OP_29(0x26, 0x1, 0xB)

    label("loc_12885")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12899")
    OP_29(0x26, 0x4, 0x10)

    label("loc_12899")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_128AD")
    OP_29(0x26, 0x4, 0x20)

    label("loc_128AD")

    Jump("loc_12ADC")

    label("loc_128B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1299F")
    OP_29(0x27, 0x3, 0x0)
    OP_29(0x27, 0x3, 0x1)
    OP_29(0x27, 0x3, 0x2)
    OP_29(0x27, 0x3, 0x10)
    OP_29(0x27, 0x3, 0x20)
    OP_29(0x27, 0x3, 0x40)
    OP_29(0x27, 0x2, 0x0)
    OP_29(0x27, 0x2, 0x1)
    OP_29(0x27, 0x2, 0x2)
    OP_29(0x27, 0x2, 0x3)
    OP_29(0x27, 0x2, 0x4)
    OP_29(0x27, 0x2, 0x5)
    OP_29(0x27, 0x2, 0x6)
    OP_29(0x27, 0x2, 0x7)
    OP_29(0x27, 0x2, 0x8)
    OP_29(0x27, 0x2, 0x9)
    OP_29(0x27, 0x2, 0xA)
    OP_29(0x27, 0x2, 0xB)
    OP_29(0x27, 0x2, 0xC)
    OP_29(0x27, 0x2, 0xD)
    OP_29(0x27, 0x2, 0xE)
    OP_29(0x27, 0x2, 0xF)
    OP_29(0x27, 0x2, 0x10)
    OP_29(0x27, 0x2, 0x11)
    OP_29(0x27, 0x2, 0x12)
    OP_29(0x27, 0x2, 0x13)
    OP_29(0x27, 0x2, 0x14)
    OP_29(0x27, 0x2, 0x15)
    OP_29(0x27, 0x2, 0x16)
    OP_29(0x27, 0x2, 0x17)
    OP_29(0x27, 0x2, 0x18)
    OP_29(0x27, 0x2, 0x19)
    OP_29(0x27, 0x2, 0x1A)
    OP_29(0x27, 0x2, 0x1B)
    OP_29(0x27, 0x2, 0x1C)
    OP_29(0x27, 0x2, 0x1D)
    OP_29(0x27, 0x2, 0x1E)
    OP_29(0x27, 0x2, 0x1F)

    label("loc_1299F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_129B3")
    OP_29(0x27, 0x4, 0x2)

    label("loc_129B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_129C8")
    OP_29(0x27, 0x1, 0x0)

    label("loc_129C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_129DD")
    OP_29(0x27, 0x1, 0x1)

    label("loc_129DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_129F2")
    OP_29(0x27, 0x1, 0x2)

    label("loc_129F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12A07")
    OP_29(0x27, 0x1, 0x3)

    label("loc_12A07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12A1C")
    OP_29(0x27, 0x1, 0x4)

    label("loc_12A1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12A31")
    OP_29(0x27, 0x1, 0x5)

    label("loc_12A31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12A46")
    OP_29(0x27, 0x1, 0x6)

    label("loc_12A46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12A5B")
    OP_29(0x27, 0x1, 0x7)

    label("loc_12A5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12A70")
    OP_29(0x27, 0x1, 0x8)

    label("loc_12A70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12A85")
    OP_29(0x27, 0x1, 0x9)

    label("loc_12A85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12A9A")
    OP_29(0x27, 0x1, 0xA)

    label("loc_12A9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12AAF")
    OP_29(0x27, 0x1, 0xB)

    label("loc_12AAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12AC3")
    OP_29(0x27, 0x4, 0x10)

    label("loc_12AC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12AD7")
    OP_29(0x27, 0x4, 0x20)

    label("loc_12AD7")

    Jump("loc_12ADC")

    label("loc_12ADC")

    Jump("loc_122F3")

    label("loc_12AE1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_58_122E9 end

    def Function_59_12AF9(): pass

    label("Function_59_12AF9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12B03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_150B7")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "-- Chapter 4 --\x01",                                      # 0
            "QS_0501 - Collecting Overdue Books 2\x01",                 # 1
            "QS_0502 - Craving Creative Cuisine\x01",                   # 2
            "QS_0503 - Childhood Love at First Sight\x01",              # 3
            "QS_0504 - Prepare Monsters ⑩\x01",                        # 4
            "QS_0505 - Present to Father\x01",                          # 5
            "QS_0506 - Search for Diet Member's Daughter\x01",          # 6
            "QS_0507 - Finding Flowers for Remembrance\x01",            # 7
            "QS_0508 - Prepare Monsters ⑪\x01",                        # 8
            "QS_0509 - Receiving Custom Doll\x01",                      # 9
            "QS_0510 - Developing Orbal Staff Feature\x01",             # 10
            "QS_0511 - Prepare Monsters ⑫\x01",                        # 11
            "QS_0512 - Prepare Monsters ⑬\x01",                        # 12
            "-- Finale --\x01",                                         # 13
            "QS_0601 - Investigate Abnormality in Geofront B\x01",      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_12D66"),
        (5, "loc_12ED3"),
        (6, "loc_12FBA"),
        (7, "loc_13205"),
        (2, "loc_132F3"),
        (3, "loc_132F3"),
        (4, "loc_132F3"),
        (8, "loc_132F3"),
        (9, "loc_132F3"),
        (10, "loc_132F3"),
        (11, "loc_132F3"),
        (12, "loc_132F3"),
        (14, "loc_132F3"),
        (SWITCH_DEFAULT, "loc_13372"),
    )


    label("loc_12D66")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                              # 0
            "Start\x01",                              # 1
            "QF_01 - Read Request Details\x01",       # 2
            "QF_02 - Take on Request\x01",            # 3
            "QF_03 - Talk With Alfred\x01",           # 4
            "QF_04 - Talk With Elkin\x01",            # 5
            "QF_05 - Talk With Donald\x01",           # 6
            "QF_06 - Collect Alfred's Book\x01",      # 7
            "QF_07 - Talk With Logy\x01",             # 8
            "QF_08 - Collect Logy's Book\x01",        # 9
            "QF_09 - Talk With Flora\x01",            # 10
            "QF_10 - Enter Reference Room\x01",       # 11
            "QF_11 - Collect Flora's Book\x01",       # 12
            "Collected All Books\x01",                # 13
            "Complete\x01",                           # 14
            "Report\x01",                             # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_13381")

    label("loc_12ED3")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                                      # 0
            "Start (Talked With Cecile or Shizuku)\x01",      # 1
            "QF_01 - Talked With Michael\x01",                # 2
            "QF_02 - Talked With Meifa\x01",                  # 3
            "QF_03 - Talked With Ursuline\x01",               # 4
            "QF_04 - Talked With Doctor Gailey\x01",          # 5
            "QF_05 - Examined Container\x01",                 # 6
            "Complete\x01",                                   # 7
            "Report\x01",                                     # 8
        )
    )

    MenuEnd(0x5)
    Jump("loc_13381")

    label("loc_12FBA")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                                     # 0
            "Start\x01",                                     # 1
            "QF_01 - Went to Campbell's Residence\x01",      # 2
            "QF_02 - Checked Note\x01",                      # 3
            "QF_03 - Listened to Details\x01",               # 4
            "QF_04 - Listened to Details\x01",               # 5
            "QF_05 - Talked\x01",                            # 6
            "QF_06 - To IBC!\x01",                           # 7
            "QF_07 - Talk to Lanfei\x01",                    # 8
            "QF_08 - Go to CEO's Room\x01",                  # 9
            "QF_09 - Hurry to Airport!\x01",                 # 10
            "QF_10 - Hurry to Station!\x01",                 # 11
            "[→next]\x01",                                  # 12
        )
    )

    MenuEnd(0x5)
    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13200")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "QF_13 - Found Carla on Train\x01",             # 0
            "QF_14 - Let's Convince Carla!\x01",            # 1
            "QF_15 - Succeeded!\x01",                       # 2
            "QF_16 - Failed...\x01",                        # 3
            "[C0800 Board Train]\x01",                      # 4
            "[R0040 Train Passing Scene]\x01",              # 5
            "[C0800 Return - Successful Variant]\x01",      # 6
            "[C0800 Return - Failure Variant]\x01",         # 7
            "Complete\x01",                                 # 8
            "Report\x01",                                   # 9
        )
    )

    MenuEnd(0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13200")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13200")

    Jump("loc_13381")

    label("loc_13205")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",                             # 0
            "Start\x01",                             # 1
            "QF_01 - Read Request Details\x01",      # 2
            "QF_02 - Take on Request\x01",           # 3
            "QF_03 - Get Leevus Flower\x01",         # 4
            "QF_04 - Talk to Tallys\x01",            # 5
            "QF_05 - Get Requium Flower\x01",        # 6
            "QF_06 - Get Fainel Flower\x01",         # 7
            "QF_07 - Return With Flowers\x01",       # 8
            "Complete\x01",                          # 9
            "Report\x01",                            # 10
        )
    )

    MenuEnd(0x5)
    Jump("loc_13381")

    label("loc_132F3")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Reset\x01",         # 0
            "Start\x01",         # 1
            "QF_01\x01",         # 2
            "QF_02\x01",         # 3
            "QF_03\x01",         # 4
            "QF_04\x01",         # 5
            "QF_05\x01",         # 6
            "QF_06\x01",         # 7
            "QF_07\x01",         # 8
            "QF_08\x01",         # 9
            "QF_09\x01",         # 10
            "QF_10\x01",         # 11
            "QF_11\x01",         # 12
            "QF_12\x01",         # 13
            "Complete\x01",      # 14
            "Report\x01",        # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_13381")

    label("loc_13372")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13381")

    label("loc_13381")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_150B2")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_133EB"),
        (2, "loc_136FF"),
        (3, "loc_13929"),
        (4, "loc_13B53"),
        (5, "loc_13D7D"),
        (6, "loc_13F14"),
        (7, "loc_141F5"),
        (8, "loc_143B6"),
        (9, "loc_145E0"),
        (10, "loc_1480A"),
        (11, "loc_14A34"),
        (12, "loc_14C5E"),
        (14, "loc_14E88"),
        (SWITCH_DEFAULT, "loc_150B2"),
    )


    label("loc_133EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_134D8")
    OP_29(0x28, 0x3, 0x0)
    OP_29(0x28, 0x3, 0x1)
    OP_29(0x28, 0x3, 0x2)
    OP_29(0x28, 0x3, 0x10)
    OP_29(0x28, 0x3, 0x20)
    OP_29(0x28, 0x3, 0x40)
    OP_29(0x28, 0x2, 0x0)
    OP_29(0x28, 0x2, 0x1)
    OP_29(0x28, 0x2, 0x2)
    OP_29(0x28, 0x2, 0x3)
    OP_29(0x28, 0x2, 0x4)
    OP_29(0x28, 0x2, 0x5)
    OP_29(0x28, 0x2, 0x6)
    OP_29(0x28, 0x2, 0x7)
    OP_29(0x28, 0x2, 0x8)
    OP_29(0x28, 0x2, 0x9)
    OP_29(0x28, 0x2, 0xA)
    OP_29(0x28, 0x2, 0xB)
    OP_29(0x28, 0x2, 0xC)
    OP_29(0x28, 0x2, 0xD)
    OP_29(0x28, 0x2, 0xE)
    OP_29(0x28, 0x2, 0xF)
    OP_29(0x28, 0x2, 0x10)
    OP_29(0x28, 0x2, 0x11)
    OP_29(0x28, 0x2, 0x12)
    OP_29(0x28, 0x2, 0x13)
    OP_29(0x28, 0x2, 0x14)
    OP_29(0x28, 0x2, 0x15)
    OP_29(0x28, 0x2, 0x16)
    OP_29(0x28, 0x2, 0x17)
    OP_29(0x28, 0x2, 0x18)
    OP_29(0x28, 0x2, 0x19)
    OP_29(0x28, 0x2, 0x1A)
    OP_29(0x28, 0x2, 0x1B)
    OP_29(0x28, 0x2, 0x1C)
    OP_29(0x28, 0x2, 0x1D)
    OP_29(0x28, 0x2, 0x1E)
    OP_29(0x28, 0x2, 0x1F)

    label("loc_134D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_134EC")
    OP_29(0x28, 0x4, 0x2)

    label("loc_134EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13506")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x0)

    label("loc_13506")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13520")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)

    label("loc_13520")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13540")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)

    label("loc_13540")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13566")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x3)

    label("loc_13566")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13592")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x3)
    OP_29(0x28, 0x1, 0x4)

    label("loc_13592")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_135C4")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x3)
    OP_29(0x28, 0x1, 0x4)
    OP_29(0x28, 0x1, 0x5)

    label("loc_135C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_135E4")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x6)

    label("loc_135E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1360A")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x6)
    OP_29(0x28, 0x1, 0x7)

    label("loc_1360A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1362A")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x8)

    label("loc_1362A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13650")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x8)
    OP_29(0x28, 0x1, 0x9)

    label("loc_13650")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1367C")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x8)
    OP_29(0x28, 0x1, 0x9)
    OP_29(0x28, 0x1, 0xA)

    label("loc_1367C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_136CC")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x3)
    OP_29(0x28, 0x1, 0x4)
    OP_29(0x28, 0x1, 0x5)
    OP_29(0x28, 0x1, 0x6)
    OP_29(0x28, 0x1, 0x7)
    OP_29(0x28, 0x1, 0x8)
    OP_29(0x28, 0x1, 0x9)
    OP_29(0x28, 0x1, 0xA)

    label("loc_136CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_136E6")
    OP_29(0x28, 0x1, 0xB)
    OP_29(0x28, 0x4, 0x10)

    label("loc_136E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_136FA")
    OP_29(0x28, 0x4, 0x20)

    label("loc_136FA")

    Jump("loc_150B2")

    label("loc_136FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137EC")
    OP_29(0x29, 0x3, 0x0)
    OP_29(0x29, 0x3, 0x1)
    OP_29(0x29, 0x3, 0x2)
    OP_29(0x29, 0x3, 0x10)
    OP_29(0x29, 0x3, 0x20)
    OP_29(0x29, 0x3, 0x40)
    OP_29(0x29, 0x2, 0x0)
    OP_29(0x29, 0x2, 0x1)
    OP_29(0x29, 0x2, 0x2)
    OP_29(0x29, 0x2, 0x3)
    OP_29(0x29, 0x2, 0x4)
    OP_29(0x29, 0x2, 0x5)
    OP_29(0x29, 0x2, 0x6)
    OP_29(0x29, 0x2, 0x7)
    OP_29(0x29, 0x2, 0x8)
    OP_29(0x29, 0x2, 0x9)
    OP_29(0x29, 0x2, 0xA)
    OP_29(0x29, 0x2, 0xB)
    OP_29(0x29, 0x2, 0xC)
    OP_29(0x29, 0x2, 0xD)
    OP_29(0x29, 0x2, 0xE)
    OP_29(0x29, 0x2, 0xF)
    OP_29(0x29, 0x2, 0x10)
    OP_29(0x29, 0x2, 0x11)
    OP_29(0x29, 0x2, 0x12)
    OP_29(0x29, 0x2, 0x13)
    OP_29(0x29, 0x2, 0x14)
    OP_29(0x29, 0x2, 0x15)
    OP_29(0x29, 0x2, 0x16)
    OP_29(0x29, 0x2, 0x17)
    OP_29(0x29, 0x2, 0x18)
    OP_29(0x29, 0x2, 0x19)
    OP_29(0x29, 0x2, 0x1A)
    OP_29(0x29, 0x2, 0x1B)
    OP_29(0x29, 0x2, 0x1C)
    OP_29(0x29, 0x2, 0x1D)
    OP_29(0x29, 0x2, 0x1E)
    OP_29(0x29, 0x2, 0x1F)

    label("loc_137EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13800")
    OP_29(0x29, 0x4, 0x2)

    label("loc_13800")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13815")
    OP_29(0x29, 0x1, 0x0)

    label("loc_13815")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1382A")
    OP_29(0x29, 0x1, 0x1)

    label("loc_1382A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1383F")
    OP_29(0x29, 0x1, 0x2)

    label("loc_1383F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13854")
    OP_29(0x29, 0x1, 0x3)

    label("loc_13854")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13869")
    OP_29(0x29, 0x1, 0x4)

    label("loc_13869")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1387E")
    OP_29(0x29, 0x1, 0x5)

    label("loc_1387E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13893")
    OP_29(0x29, 0x1, 0x6)

    label("loc_13893")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_138A8")
    OP_29(0x29, 0x1, 0x7)

    label("loc_138A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_138BD")
    OP_29(0x29, 0x1, 0x8)

    label("loc_138BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_138D2")
    OP_29(0x29, 0x1, 0x9)

    label("loc_138D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_138E7")
    OP_29(0x29, 0x1, 0xA)

    label("loc_138E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_138FC")
    OP_29(0x29, 0x1, 0xB)

    label("loc_138FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13910")
    OP_29(0x29, 0x4, 0x10)

    label("loc_13910")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13924")
    OP_29(0x29, 0x4, 0x20)

    label("loc_13924")

    Jump("loc_150B2")

    label("loc_13929")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A16")
    OP_29(0x2A, 0x3, 0x0)
    OP_29(0x2A, 0x3, 0x1)
    OP_29(0x2A, 0x3, 0x2)
    OP_29(0x2A, 0x3, 0x10)
    OP_29(0x2A, 0x3, 0x20)
    OP_29(0x2A, 0x3, 0x40)
    OP_29(0x2A, 0x2, 0x0)
    OP_29(0x2A, 0x2, 0x1)
    OP_29(0x2A, 0x2, 0x2)
    OP_29(0x2A, 0x2, 0x3)
    OP_29(0x2A, 0x2, 0x4)
    OP_29(0x2A, 0x2, 0x5)
    OP_29(0x2A, 0x2, 0x6)
    OP_29(0x2A, 0x2, 0x7)
    OP_29(0x2A, 0x2, 0x8)
    OP_29(0x2A, 0x2, 0x9)
    OP_29(0x2A, 0x2, 0xA)
    OP_29(0x2A, 0x2, 0xB)
    OP_29(0x2A, 0x2, 0xC)
    OP_29(0x2A, 0x2, 0xD)
    OP_29(0x2A, 0x2, 0xE)
    OP_29(0x2A, 0x2, 0xF)
    OP_29(0x2A, 0x2, 0x10)
    OP_29(0x2A, 0x2, 0x11)
    OP_29(0x2A, 0x2, 0x12)
    OP_29(0x2A, 0x2, 0x13)
    OP_29(0x2A, 0x2, 0x14)
    OP_29(0x2A, 0x2, 0x15)
    OP_29(0x2A, 0x2, 0x16)
    OP_29(0x2A, 0x2, 0x17)
    OP_29(0x2A, 0x2, 0x18)
    OP_29(0x2A, 0x2, 0x19)
    OP_29(0x2A, 0x2, 0x1A)
    OP_29(0x2A, 0x2, 0x1B)
    OP_29(0x2A, 0x2, 0x1C)
    OP_29(0x2A, 0x2, 0x1D)
    OP_29(0x2A, 0x2, 0x1E)
    OP_29(0x2A, 0x2, 0x1F)

    label("loc_13A16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A2A")
    OP_29(0x2A, 0x4, 0x2)

    label("loc_13A2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A3F")
    OP_29(0x2A, 0x1, 0x0)

    label("loc_13A3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A54")
    OP_29(0x2A, 0x1, 0x1)

    label("loc_13A54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A69")
    OP_29(0x2A, 0x1, 0x2)

    label("loc_13A69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A7E")
    OP_29(0x2A, 0x1, 0x3)

    label("loc_13A7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A93")
    OP_29(0x2A, 0x1, 0x4)

    label("loc_13A93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13AA8")
    OP_29(0x2A, 0x1, 0x5)

    label("loc_13AA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13ABD")
    OP_29(0x2A, 0x1, 0x6)

    label("loc_13ABD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13AD2")
    OP_29(0x2A, 0x1, 0x7)

    label("loc_13AD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13AE7")
    OP_29(0x2A, 0x1, 0x8)

    label("loc_13AE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13AFC")
    OP_29(0x2A, 0x1, 0x9)

    label("loc_13AFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13B11")
    OP_29(0x2A, 0x1, 0xA)

    label("loc_13B11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13B26")
    OP_29(0x2A, 0x1, 0xB)

    label("loc_13B26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13B3A")
    OP_29(0x2A, 0x4, 0x10)

    label("loc_13B3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13B4E")
    OP_29(0x2A, 0x4, 0x20)

    label("loc_13B4E")

    Jump("loc_150B2")

    label("loc_13B53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C40")
    OP_29(0x2B, 0x3, 0x0)
    OP_29(0x2B, 0x3, 0x1)
    OP_29(0x2B, 0x3, 0x2)
    OP_29(0x2B, 0x3, 0x10)
    OP_29(0x2B, 0x3, 0x20)
    OP_29(0x2B, 0x3, 0x40)
    OP_29(0x2B, 0x2, 0x0)
    OP_29(0x2B, 0x2, 0x1)
    OP_29(0x2B, 0x2, 0x2)
    OP_29(0x2B, 0x2, 0x3)
    OP_29(0x2B, 0x2, 0x4)
    OP_29(0x2B, 0x2, 0x5)
    OP_29(0x2B, 0x2, 0x6)
    OP_29(0x2B, 0x2, 0x7)
    OP_29(0x2B, 0x2, 0x8)
    OP_29(0x2B, 0x2, 0x9)
    OP_29(0x2B, 0x2, 0xA)
    OP_29(0x2B, 0x2, 0xB)
    OP_29(0x2B, 0x2, 0xC)
    OP_29(0x2B, 0x2, 0xD)
    OP_29(0x2B, 0x2, 0xE)
    OP_29(0x2B, 0x2, 0xF)
    OP_29(0x2B, 0x2, 0x10)
    OP_29(0x2B, 0x2, 0x11)
    OP_29(0x2B, 0x2, 0x12)
    OP_29(0x2B, 0x2, 0x13)
    OP_29(0x2B, 0x2, 0x14)
    OP_29(0x2B, 0x2, 0x15)
    OP_29(0x2B, 0x2, 0x16)
    OP_29(0x2B, 0x2, 0x17)
    OP_29(0x2B, 0x2, 0x18)
    OP_29(0x2B, 0x2, 0x19)
    OP_29(0x2B, 0x2, 0x1A)
    OP_29(0x2B, 0x2, 0x1B)
    OP_29(0x2B, 0x2, 0x1C)
    OP_29(0x2B, 0x2, 0x1D)
    OP_29(0x2B, 0x2, 0x1E)
    OP_29(0x2B, 0x2, 0x1F)

    label("loc_13C40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13C54")
    OP_29(0x2B, 0x4, 0x2)

    label("loc_13C54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13C69")
    OP_29(0x2B, 0x1, 0x0)

    label("loc_13C69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13C7E")
    OP_29(0x2B, 0x1, 0x1)

    label("loc_13C7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13C93")
    OP_29(0x2B, 0x1, 0x2)

    label("loc_13C93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13CA8")
    OP_29(0x2B, 0x1, 0x3)

    label("loc_13CA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13CBD")
    OP_29(0x2B, 0x1, 0x4)

    label("loc_13CBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13CD2")
    OP_29(0x2B, 0x1, 0x5)

    label("loc_13CD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13CE7")
    OP_29(0x2B, 0x1, 0x6)

    label("loc_13CE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13CFC")
    OP_29(0x2B, 0x1, 0x7)

    label("loc_13CFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D11")
    OP_29(0x2B, 0x1, 0x8)

    label("loc_13D11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D26")
    OP_29(0x2B, 0x1, 0x9)

    label("loc_13D26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D3B")
    OP_29(0x2B, 0x1, 0xA)

    label("loc_13D3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D50")
    OP_29(0x2B, 0x1, 0xB)

    label("loc_13D50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D64")
    OP_29(0x2B, 0x4, 0x10)

    label("loc_13D64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D78")
    OP_29(0x2B, 0x4, 0x20)

    label("loc_13D78")

    Jump("loc_150B2")

    label("loc_13D7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E6A")
    OP_29(0x2C, 0x3, 0x0)
    OP_29(0x2C, 0x3, 0x1)
    OP_29(0x2C, 0x3, 0x2)
    OP_29(0x2C, 0x3, 0x10)
    OP_29(0x2C, 0x3, 0x20)
    OP_29(0x2C, 0x3, 0x40)
    OP_29(0x2C, 0x2, 0x0)
    OP_29(0x2C, 0x2, 0x1)
    OP_29(0x2C, 0x2, 0x2)
    OP_29(0x2C, 0x2, 0x3)
    OP_29(0x2C, 0x2, 0x4)
    OP_29(0x2C, 0x2, 0x5)
    OP_29(0x2C, 0x2, 0x6)
    OP_29(0x2C, 0x2, 0x7)
    OP_29(0x2C, 0x2, 0x8)
    OP_29(0x2C, 0x2, 0x9)
    OP_29(0x2C, 0x2, 0xA)
    OP_29(0x2C, 0x2, 0xB)
    OP_29(0x2C, 0x2, 0xC)
    OP_29(0x2C, 0x2, 0xD)
    OP_29(0x2C, 0x2, 0xE)
    OP_29(0x2C, 0x2, 0xF)
    OP_29(0x2C, 0x2, 0x10)
    OP_29(0x2C, 0x2, 0x11)
    OP_29(0x2C, 0x2, 0x12)
    OP_29(0x2C, 0x2, 0x13)
    OP_29(0x2C, 0x2, 0x14)
    OP_29(0x2C, 0x2, 0x15)
    OP_29(0x2C, 0x2, 0x16)
    OP_29(0x2C, 0x2, 0x17)
    OP_29(0x2C, 0x2, 0x18)
    OP_29(0x2C, 0x2, 0x19)
    OP_29(0x2C, 0x2, 0x1A)
    OP_29(0x2C, 0x2, 0x1B)
    OP_29(0x2C, 0x2, 0x1C)
    OP_29(0x2C, 0x2, 0x1D)
    OP_29(0x2C, 0x2, 0x1E)
    OP_29(0x2C, 0x2, 0x1F)

    label("loc_13E6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13E7E")
    OP_29(0x2C, 0x4, 0x2)

    label("loc_13E7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13E93")
    OP_29(0x2C, 0x1, 0x0)

    label("loc_13E93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13EA8")
    OP_29(0x2C, 0x1, 0x1)

    label("loc_13EA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13EBD")
    OP_29(0x2C, 0x1, 0x2)

    label("loc_13EBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13ED2")
    OP_29(0x2C, 0x1, 0x3)

    label("loc_13ED2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13EE7")
    OP_29(0x2C, 0x1, 0x4)

    label("loc_13EE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13EFB")
    OP_29(0x2C, 0x4, 0x10)

    label("loc_13EFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13F0F")
    OP_29(0x2C, 0x4, 0x20)

    label("loc_13F0F")

    Jump("loc_150B2")

    label("loc_13F14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14001")
    OP_29(0x2D, 0x3, 0x0)
    OP_29(0x2D, 0x3, 0x1)
    OP_29(0x2D, 0x3, 0x2)
    OP_29(0x2D, 0x3, 0x10)
    OP_29(0x2D, 0x3, 0x20)
    OP_29(0x2D, 0x3, 0x40)
    OP_29(0x2D, 0x2, 0x0)
    OP_29(0x2D, 0x2, 0x1)
    OP_29(0x2D, 0x2, 0x2)
    OP_29(0x2D, 0x2, 0x3)
    OP_29(0x2D, 0x2, 0x4)
    OP_29(0x2D, 0x2, 0x5)
    OP_29(0x2D, 0x2, 0x6)
    OP_29(0x2D, 0x2, 0x7)
    OP_29(0x2D, 0x2, 0x8)
    OP_29(0x2D, 0x2, 0x9)
    OP_29(0x2D, 0x2, 0xA)
    OP_29(0x2D, 0x2, 0xB)
    OP_29(0x2D, 0x2, 0xC)
    OP_29(0x2D, 0x2, 0xD)
    OP_29(0x2D, 0x2, 0xE)
    OP_29(0x2D, 0x2, 0xF)
    OP_29(0x2D, 0x2, 0x10)
    OP_29(0x2D, 0x2, 0x11)
    OP_29(0x2D, 0x2, 0x12)
    OP_29(0x2D, 0x2, 0x13)
    OP_29(0x2D, 0x2, 0x14)
    OP_29(0x2D, 0x2, 0x15)
    OP_29(0x2D, 0x2, 0x16)
    OP_29(0x2D, 0x2, 0x17)
    OP_29(0x2D, 0x2, 0x18)
    OP_29(0x2D, 0x2, 0x19)
    OP_29(0x2D, 0x2, 0x1A)
    OP_29(0x2D, 0x2, 0x1B)
    OP_29(0x2D, 0x2, 0x1C)
    OP_29(0x2D, 0x2, 0x1D)
    OP_29(0x2D, 0x2, 0x1E)
    OP_29(0x2D, 0x2, 0x1F)

    label("loc_14001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14015")
    OP_29(0x2D, 0x4, 0x2)

    label("loc_14015")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1402A")
    OP_29(0x2D, 0x1, 0x0)

    label("loc_1402A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1403F")
    OP_29(0x2D, 0x1, 0x1)

    label("loc_1403F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14054")
    OP_29(0x2D, 0x1, 0x2)

    label("loc_14054")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14069")
    OP_29(0x2D, 0x1, 0x3)

    label("loc_14069")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1407E")
    OP_29(0x2D, 0x1, 0x4)

    label("loc_1407E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14093")
    OP_29(0x2D, 0x1, 0x5)

    label("loc_14093")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_140A8")
    OP_29(0x2D, 0x1, 0x6)

    label("loc_140A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_140BD")
    OP_29(0x2D, 0x1, 0x7)

    label("loc_140BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_140D2")
    OP_29(0x2D, 0x1, 0x8)

    label("loc_140D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_140E7")
    OP_29(0x2D, 0x1, 0x9)

    label("loc_140E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_140FC")
    OP_29(0x2D, 0x1, 0xC)

    label("loc_140FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14111")
    OP_29(0x2D, 0x1, 0xD)

    label("loc_14111")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14126")
    OP_29(0x2D, 0x1, 0xE)

    label("loc_14126")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1413B")
    OP_29(0x2D, 0x1, 0xF)

    label("loc_1413B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1415D")
    OP_29(0x2D, 0x3, 0x10)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_141C8")

    label("loc_1415D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14182")
    SetScenarioFlags(0x5C, 0)
    OP_29(0x2D, 0x3, 0x10)
    NewScene("r0040", 0, 0, 0)
    IdleLoop()
    Jump("loc_141C8")

    label("loc_14182")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141A7")
    SetScenarioFlags(0x5C, 3)
    OP_29(0x2D, 0x3, 0x10)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_141C8")

    label("loc_141A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141C8")
    SetScenarioFlags(0x5C, 3)
    OP_29(0x2D, 0x2, 0xE)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()

    label("loc_141C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_141DC")
    OP_29(0x2D, 0x4, 0x10)

    label("loc_141DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_141F0")
    OP_29(0x2D, 0x4, 0x20)

    label("loc_141F0")

    Jump("loc_150B2")

    label("loc_141F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142E2")
    OP_29(0x2E, 0x3, 0x0)
    OP_29(0x2E, 0x3, 0x1)
    OP_29(0x2E, 0x3, 0x2)
    OP_29(0x2E, 0x3, 0x10)
    OP_29(0x2E, 0x3, 0x20)
    OP_29(0x2E, 0x3, 0x40)
    OP_29(0x2E, 0x2, 0x0)
    OP_29(0x2E, 0x2, 0x1)
    OP_29(0x2E, 0x2, 0x2)
    OP_29(0x2E, 0x2, 0x3)
    OP_29(0x2E, 0x2, 0x4)
    OP_29(0x2E, 0x2, 0x5)
    OP_29(0x2E, 0x2, 0x6)
    OP_29(0x2E, 0x2, 0x7)
    OP_29(0x2E, 0x2, 0x8)
    OP_29(0x2E, 0x2, 0x9)
    OP_29(0x2E, 0x2, 0xA)
    OP_29(0x2E, 0x2, 0xB)
    OP_29(0x2E, 0x2, 0xC)
    OP_29(0x2E, 0x2, 0xD)
    OP_29(0x2E, 0x2, 0xE)
    OP_29(0x2E, 0x2, 0xF)
    OP_29(0x2E, 0x2, 0x10)
    OP_29(0x2E, 0x2, 0x11)
    OP_29(0x2E, 0x2, 0x12)
    OP_29(0x2E, 0x2, 0x13)
    OP_29(0x2E, 0x2, 0x14)
    OP_29(0x2E, 0x2, 0x15)
    OP_29(0x2E, 0x2, 0x16)
    OP_29(0x2E, 0x2, 0x17)
    OP_29(0x2E, 0x2, 0x18)
    OP_29(0x2E, 0x2, 0x19)
    OP_29(0x2E, 0x2, 0x1A)
    OP_29(0x2E, 0x2, 0x1B)
    OP_29(0x2E, 0x2, 0x1C)
    OP_29(0x2E, 0x2, 0x1D)
    OP_29(0x2E, 0x2, 0x1E)
    OP_29(0x2E, 0x2, 0x1F)

    label("loc_142E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_142F6")
    OP_29(0x2E, 0x4, 0x2)

    label("loc_142F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1430B")
    OP_29(0x2E, 0x1, 0x0)

    label("loc_1430B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14320")
    OP_29(0x2E, 0x1, 0x1)

    label("loc_14320")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14335")
    OP_29(0x2E, 0x1, 0x2)

    label("loc_14335")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1434A")
    OP_29(0x2E, 0x1, 0x3)

    label("loc_1434A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1435F")
    OP_29(0x2E, 0x1, 0x4)

    label("loc_1435F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14374")
    OP_29(0x2E, 0x1, 0x5)

    label("loc_14374")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14389")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_14389")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1439D")
    OP_29(0x2E, 0x4, 0x10)

    label("loc_1439D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_143B1")
    OP_29(0x2E, 0x4, 0x20)

    label("loc_143B1")

    Jump("loc_150B2")

    label("loc_143B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144A3")
    OP_29(0x2F, 0x3, 0x0)
    OP_29(0x2F, 0x3, 0x1)
    OP_29(0x2F, 0x3, 0x2)
    OP_29(0x2F, 0x3, 0x10)
    OP_29(0x2F, 0x3, 0x20)
    OP_29(0x2F, 0x3, 0x40)
    OP_29(0x2F, 0x2, 0x0)
    OP_29(0x2F, 0x2, 0x1)
    OP_29(0x2F, 0x2, 0x2)
    OP_29(0x2F, 0x2, 0x3)
    OP_29(0x2F, 0x2, 0x4)
    OP_29(0x2F, 0x2, 0x5)
    OP_29(0x2F, 0x2, 0x6)
    OP_29(0x2F, 0x2, 0x7)
    OP_29(0x2F, 0x2, 0x8)
    OP_29(0x2F, 0x2, 0x9)
    OP_29(0x2F, 0x2, 0xA)
    OP_29(0x2F, 0x2, 0xB)
    OP_29(0x2F, 0x2, 0xC)
    OP_29(0x2F, 0x2, 0xD)
    OP_29(0x2F, 0x2, 0xE)
    OP_29(0x2F, 0x2, 0xF)
    OP_29(0x2F, 0x2, 0x10)
    OP_29(0x2F, 0x2, 0x11)
    OP_29(0x2F, 0x2, 0x12)
    OP_29(0x2F, 0x2, 0x13)
    OP_29(0x2F, 0x2, 0x14)
    OP_29(0x2F, 0x2, 0x15)
    OP_29(0x2F, 0x2, 0x16)
    OP_29(0x2F, 0x2, 0x17)
    OP_29(0x2F, 0x2, 0x18)
    OP_29(0x2F, 0x2, 0x19)
    OP_29(0x2F, 0x2, 0x1A)
    OP_29(0x2F, 0x2, 0x1B)
    OP_29(0x2F, 0x2, 0x1C)
    OP_29(0x2F, 0x2, 0x1D)
    OP_29(0x2F, 0x2, 0x1E)
    OP_29(0x2F, 0x2, 0x1F)

    label("loc_144A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_144B7")
    OP_29(0x2F, 0x4, 0x2)

    label("loc_144B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_144CC")
    OP_29(0x2F, 0x1, 0x0)

    label("loc_144CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_144E1")
    OP_29(0x2F, 0x1, 0x1)

    label("loc_144E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_144F6")
    OP_29(0x2F, 0x1, 0x2)

    label("loc_144F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1450B")
    OP_29(0x2F, 0x1, 0x3)

    label("loc_1450B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14520")
    OP_29(0x2F, 0x1, 0x4)

    label("loc_14520")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14535")
    OP_29(0x2F, 0x1, 0x5)

    label("loc_14535")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1454A")
    OP_29(0x2F, 0x1, 0x6)

    label("loc_1454A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1455F")
    OP_29(0x2F, 0x1, 0x7)

    label("loc_1455F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14574")
    OP_29(0x2F, 0x1, 0x8)

    label("loc_14574")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14589")
    OP_29(0x2F, 0x1, 0x9)

    label("loc_14589")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1459E")
    OP_29(0x2F, 0x1, 0xA)

    label("loc_1459E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_145B3")
    OP_29(0x2F, 0x1, 0xB)

    label("loc_145B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_145C7")
    OP_29(0x2F, 0x4, 0x10)

    label("loc_145C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_145DB")
    OP_29(0x2F, 0x4, 0x20)

    label("loc_145DB")

    Jump("loc_150B2")

    label("loc_145E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_146CD")
    OP_29(0x30, 0x3, 0x0)
    OP_29(0x30, 0x3, 0x1)
    OP_29(0x30, 0x3, 0x2)
    OP_29(0x30, 0x3, 0x10)
    OP_29(0x30, 0x3, 0x20)
    OP_29(0x30, 0x3, 0x40)
    OP_29(0x30, 0x2, 0x0)
    OP_29(0x30, 0x2, 0x1)
    OP_29(0x30, 0x2, 0x2)
    OP_29(0x30, 0x2, 0x3)
    OP_29(0x30, 0x2, 0x4)
    OP_29(0x30, 0x2, 0x5)
    OP_29(0x30, 0x2, 0x6)
    OP_29(0x30, 0x2, 0x7)
    OP_29(0x30, 0x2, 0x8)
    OP_29(0x30, 0x2, 0x9)
    OP_29(0x30, 0x2, 0xA)
    OP_29(0x30, 0x2, 0xB)
    OP_29(0x30, 0x2, 0xC)
    OP_29(0x30, 0x2, 0xD)
    OP_29(0x30, 0x2, 0xE)
    OP_29(0x30, 0x2, 0xF)
    OP_29(0x30, 0x2, 0x10)
    OP_29(0x30, 0x2, 0x11)
    OP_29(0x30, 0x2, 0x12)
    OP_29(0x30, 0x2, 0x13)
    OP_29(0x30, 0x2, 0x14)
    OP_29(0x30, 0x2, 0x15)
    OP_29(0x30, 0x2, 0x16)
    OP_29(0x30, 0x2, 0x17)
    OP_29(0x30, 0x2, 0x18)
    OP_29(0x30, 0x2, 0x19)
    OP_29(0x30, 0x2, 0x1A)
    OP_29(0x30, 0x2, 0x1B)
    OP_29(0x30, 0x2, 0x1C)
    OP_29(0x30, 0x2, 0x1D)
    OP_29(0x30, 0x2, 0x1E)
    OP_29(0x30, 0x2, 0x1F)

    label("loc_146CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_146E1")
    OP_29(0x30, 0x4, 0x2)

    label("loc_146E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_146F6")
    OP_29(0x30, 0x1, 0x0)

    label("loc_146F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1470B")
    OP_29(0x30, 0x1, 0x1)

    label("loc_1470B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14720")
    OP_29(0x30, 0x1, 0x2)

    label("loc_14720")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14735")
    OP_29(0x30, 0x1, 0x3)

    label("loc_14735")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1474A")
    OP_29(0x30, 0x1, 0x4)

    label("loc_1474A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1475F")
    OP_29(0x30, 0x1, 0x5)

    label("loc_1475F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14774")
    OP_29(0x30, 0x1, 0x6)

    label("loc_14774")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14789")
    OP_29(0x30, 0x1, 0x7)

    label("loc_14789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1479E")
    OP_29(0x30, 0x1, 0x8)

    label("loc_1479E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_147B3")
    OP_29(0x30, 0x1, 0x9)

    label("loc_147B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_147C8")
    OP_29(0x30, 0x1, 0xA)

    label("loc_147C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_147DD")
    OP_29(0x30, 0x1, 0xB)

    label("loc_147DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_147F1")
    OP_29(0x30, 0x4, 0x10)

    label("loc_147F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14805")
    OP_29(0x30, 0x4, 0x20)

    label("loc_14805")

    Jump("loc_150B2")

    label("loc_1480A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148F7")
    OP_29(0x31, 0x3, 0x0)
    OP_29(0x31, 0x3, 0x1)
    OP_29(0x31, 0x3, 0x2)
    OP_29(0x31, 0x3, 0x10)
    OP_29(0x31, 0x3, 0x20)
    OP_29(0x31, 0x3, 0x40)
    OP_29(0x31, 0x2, 0x0)
    OP_29(0x31, 0x2, 0x1)
    OP_29(0x31, 0x2, 0x2)
    OP_29(0x31, 0x2, 0x3)
    OP_29(0x31, 0x2, 0x4)
    OP_29(0x31, 0x2, 0x5)
    OP_29(0x31, 0x2, 0x6)
    OP_29(0x31, 0x2, 0x7)
    OP_29(0x31, 0x2, 0x8)
    OP_29(0x31, 0x2, 0x9)
    OP_29(0x31, 0x2, 0xA)
    OP_29(0x31, 0x2, 0xB)
    OP_29(0x31, 0x2, 0xC)
    OP_29(0x31, 0x2, 0xD)
    OP_29(0x31, 0x2, 0xE)
    OP_29(0x31, 0x2, 0xF)
    OP_29(0x31, 0x2, 0x10)
    OP_29(0x31, 0x2, 0x11)
    OP_29(0x31, 0x2, 0x12)
    OP_29(0x31, 0x2, 0x13)
    OP_29(0x31, 0x2, 0x14)
    OP_29(0x31, 0x2, 0x15)
    OP_29(0x31, 0x2, 0x16)
    OP_29(0x31, 0x2, 0x17)
    OP_29(0x31, 0x2, 0x18)
    OP_29(0x31, 0x2, 0x19)
    OP_29(0x31, 0x2, 0x1A)
    OP_29(0x31, 0x2, 0x1B)
    OP_29(0x31, 0x2, 0x1C)
    OP_29(0x31, 0x2, 0x1D)
    OP_29(0x31, 0x2, 0x1E)
    OP_29(0x31, 0x2, 0x1F)

    label("loc_148F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1490B")
    OP_29(0x31, 0x4, 0x2)

    label("loc_1490B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14920")
    OP_29(0x31, 0x1, 0x0)

    label("loc_14920")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14935")
    OP_29(0x31, 0x1, 0x1)

    label("loc_14935")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1494A")
    OP_29(0x31, 0x1, 0x2)

    label("loc_1494A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1495F")
    OP_29(0x31, 0x1, 0x3)

    label("loc_1495F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14974")
    OP_29(0x31, 0x1, 0x4)

    label("loc_14974")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14989")
    OP_29(0x31, 0x1, 0x5)

    label("loc_14989")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1499E")
    OP_29(0x31, 0x1, 0x6)

    label("loc_1499E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_149B3")
    OP_29(0x31, 0x1, 0x7)

    label("loc_149B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_149C8")
    OP_29(0x31, 0x1, 0x8)

    label("loc_149C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_149DD")
    OP_29(0x31, 0x1, 0x9)

    label("loc_149DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_149F2")
    OP_29(0x31, 0x1, 0xA)

    label("loc_149F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14A07")
    OP_29(0x31, 0x1, 0xB)

    label("loc_14A07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14A1B")
    OP_29(0x31, 0x4, 0x10)

    label("loc_14A1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14A2F")
    OP_29(0x31, 0x4, 0x20)

    label("loc_14A2F")

    Jump("loc_150B2")

    label("loc_14A34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B21")
    OP_29(0x32, 0x3, 0x0)
    OP_29(0x32, 0x3, 0x1)
    OP_29(0x32, 0x3, 0x2)
    OP_29(0x32, 0x3, 0x10)
    OP_29(0x32, 0x3, 0x20)
    OP_29(0x32, 0x3, 0x40)
    OP_29(0x32, 0x2, 0x0)
    OP_29(0x32, 0x2, 0x1)
    OP_29(0x32, 0x2, 0x2)
    OP_29(0x32, 0x2, 0x3)
    OP_29(0x32, 0x2, 0x4)
    OP_29(0x32, 0x2, 0x5)
    OP_29(0x32, 0x2, 0x6)
    OP_29(0x32, 0x2, 0x7)
    OP_29(0x32, 0x2, 0x8)
    OP_29(0x32, 0x2, 0x9)
    OP_29(0x32, 0x2, 0xA)
    OP_29(0x32, 0x2, 0xB)
    OP_29(0x32, 0x2, 0xC)
    OP_29(0x32, 0x2, 0xD)
    OP_29(0x32, 0x2, 0xE)
    OP_29(0x32, 0x2, 0xF)
    OP_29(0x32, 0x2, 0x10)
    OP_29(0x32, 0x2, 0x11)
    OP_29(0x32, 0x2, 0x12)
    OP_29(0x32, 0x2, 0x13)
    OP_29(0x32, 0x2, 0x14)
    OP_29(0x32, 0x2, 0x15)
    OP_29(0x32, 0x2, 0x16)
    OP_29(0x32, 0x2, 0x17)
    OP_29(0x32, 0x2, 0x18)
    OP_29(0x32, 0x2, 0x19)
    OP_29(0x32, 0x2, 0x1A)
    OP_29(0x32, 0x2, 0x1B)
    OP_29(0x32, 0x2, 0x1C)
    OP_29(0x32, 0x2, 0x1D)
    OP_29(0x32, 0x2, 0x1E)
    OP_29(0x32, 0x2, 0x1F)

    label("loc_14B21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14B35")
    OP_29(0x32, 0x4, 0x2)

    label("loc_14B35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14B4A")
    OP_29(0x32, 0x1, 0x0)

    label("loc_14B4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14B5F")
    OP_29(0x32, 0x1, 0x1)

    label("loc_14B5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14B74")
    OP_29(0x32, 0x1, 0x2)

    label("loc_14B74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14B89")
    OP_29(0x32, 0x1, 0x3)

    label("loc_14B89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14B9E")
    OP_29(0x32, 0x1, 0x4)

    label("loc_14B9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14BB3")
    OP_29(0x32, 0x1, 0x5)

    label("loc_14BB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14BC8")
    OP_29(0x32, 0x1, 0x6)

    label("loc_14BC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14BDD")
    OP_29(0x32, 0x1, 0x7)

    label("loc_14BDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14BF2")
    OP_29(0x32, 0x1, 0x8)

    label("loc_14BF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14C07")
    OP_29(0x32, 0x1, 0x9)

    label("loc_14C07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14C1C")
    OP_29(0x32, 0x1, 0xA)

    label("loc_14C1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14C31")
    OP_29(0x32, 0x1, 0xB)

    label("loc_14C31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14C45")
    OP_29(0x32, 0x4, 0x10)

    label("loc_14C45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14C59")
    OP_29(0x32, 0x4, 0x20)

    label("loc_14C59")

    Jump("loc_150B2")

    label("loc_14C5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D4B")
    OP_29(0x33, 0x3, 0x0)
    OP_29(0x33, 0x3, 0x1)
    OP_29(0x33, 0x3, 0x2)
    OP_29(0x33, 0x3, 0x10)
    OP_29(0x33, 0x3, 0x20)
    OP_29(0x33, 0x3, 0x40)
    OP_29(0x33, 0x2, 0x0)
    OP_29(0x33, 0x2, 0x1)
    OP_29(0x33, 0x2, 0x2)
    OP_29(0x33, 0x2, 0x3)
    OP_29(0x33, 0x2, 0x4)
    OP_29(0x33, 0x2, 0x5)
    OP_29(0x33, 0x2, 0x6)
    OP_29(0x33, 0x2, 0x7)
    OP_29(0x33, 0x2, 0x8)
    OP_29(0x33, 0x2, 0x9)
    OP_29(0x33, 0x2, 0xA)
    OP_29(0x33, 0x2, 0xB)
    OP_29(0x33, 0x2, 0xC)
    OP_29(0x33, 0x2, 0xD)
    OP_29(0x33, 0x2, 0xE)
    OP_29(0x33, 0x2, 0xF)
    OP_29(0x33, 0x2, 0x10)
    OP_29(0x33, 0x2, 0x11)
    OP_29(0x33, 0x2, 0x12)
    OP_29(0x33, 0x2, 0x13)
    OP_29(0x33, 0x2, 0x14)
    OP_29(0x33, 0x2, 0x15)
    OP_29(0x33, 0x2, 0x16)
    OP_29(0x33, 0x2, 0x17)
    OP_29(0x33, 0x2, 0x18)
    OP_29(0x33, 0x2, 0x19)
    OP_29(0x33, 0x2, 0x1A)
    OP_29(0x33, 0x2, 0x1B)
    OP_29(0x33, 0x2, 0x1C)
    OP_29(0x33, 0x2, 0x1D)
    OP_29(0x33, 0x2, 0x1E)
    OP_29(0x33, 0x2, 0x1F)

    label("loc_14D4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14D5F")
    OP_29(0x33, 0x4, 0x2)

    label("loc_14D5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14D74")
    OP_29(0x33, 0x1, 0x0)

    label("loc_14D74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14D89")
    OP_29(0x33, 0x1, 0x1)

    label("loc_14D89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14D9E")
    OP_29(0x33, 0x1, 0x2)

    label("loc_14D9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14DB3")
    OP_29(0x33, 0x1, 0x3)

    label("loc_14DB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14DC8")
    OP_29(0x33, 0x1, 0x4)

    label("loc_14DC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14DDD")
    OP_29(0x33, 0x1, 0x5)

    label("loc_14DDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14DF2")
    OP_29(0x33, 0x1, 0x6)

    label("loc_14DF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14E07")
    OP_29(0x33, 0x1, 0x7)

    label("loc_14E07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14E1C")
    OP_29(0x33, 0x1, 0x8)

    label("loc_14E1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14E31")
    OP_29(0x33, 0x1, 0x9)

    label("loc_14E31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14E46")
    OP_29(0x33, 0x1, 0xA)

    label("loc_14E46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14E5B")
    OP_29(0x33, 0x1, 0xB)

    label("loc_14E5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14E6F")
    OP_29(0x33, 0x4, 0x10)

    label("loc_14E6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14E83")
    OP_29(0x33, 0x4, 0x20)

    label("loc_14E83")

    Jump("loc_150B2")

    label("loc_14E88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F75")
    OP_29(0x34, 0x3, 0x0)
    OP_29(0x34, 0x3, 0x1)
    OP_29(0x34, 0x3, 0x2)
    OP_29(0x34, 0x3, 0x10)
    OP_29(0x34, 0x3, 0x20)
    OP_29(0x34, 0x3, 0x40)
    OP_29(0x34, 0x2, 0x0)
    OP_29(0x34, 0x2, 0x1)
    OP_29(0x34, 0x2, 0x2)
    OP_29(0x34, 0x2, 0x3)
    OP_29(0x34, 0x2, 0x4)
    OP_29(0x34, 0x2, 0x5)
    OP_29(0x34, 0x2, 0x6)
    OP_29(0x34, 0x2, 0x7)
    OP_29(0x34, 0x2, 0x8)
    OP_29(0x34, 0x2, 0x9)
    OP_29(0x34, 0x2, 0xA)
    OP_29(0x34, 0x2, 0xB)
    OP_29(0x34, 0x2, 0xC)
    OP_29(0x34, 0x2, 0xD)
    OP_29(0x34, 0x2, 0xE)
    OP_29(0x34, 0x2, 0xF)
    OP_29(0x34, 0x2, 0x10)
    OP_29(0x34, 0x2, 0x11)
    OP_29(0x34, 0x2, 0x12)
    OP_29(0x34, 0x2, 0x13)
    OP_29(0x34, 0x2, 0x14)
    OP_29(0x34, 0x2, 0x15)
    OP_29(0x34, 0x2, 0x16)
    OP_29(0x34, 0x2, 0x17)
    OP_29(0x34, 0x2, 0x18)
    OP_29(0x34, 0x2, 0x19)
    OP_29(0x34, 0x2, 0x1A)
    OP_29(0x34, 0x2, 0x1B)
    OP_29(0x34, 0x2, 0x1C)
    OP_29(0x34, 0x2, 0x1D)
    OP_29(0x34, 0x2, 0x1E)
    OP_29(0x34, 0x2, 0x1F)

    label("loc_14F75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14F89")
    OP_29(0x34, 0x4, 0x2)

    label("loc_14F89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14F9E")
    OP_29(0x34, 0x1, 0x0)

    label("loc_14F9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14FB3")
    OP_29(0x34, 0x1, 0x1)

    label("loc_14FB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14FC8")
    OP_29(0x34, 0x1, 0x2)

    label("loc_14FC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14FDD")
    OP_29(0x34, 0x1, 0x3)

    label("loc_14FDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14FF2")
    OP_29(0x34, 0x1, 0x4)

    label("loc_14FF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15007")
    OP_29(0x34, 0x1, 0x5)

    label("loc_15007")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1501C")
    OP_29(0x34, 0x1, 0x6)

    label("loc_1501C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15031")
    OP_29(0x34, 0x1, 0x7)

    label("loc_15031")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15046")
    OP_29(0x34, 0x1, 0x8)

    label("loc_15046")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1505B")
    OP_29(0x34, 0x1, 0x9)

    label("loc_1505B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15070")
    OP_29(0x34, 0x1, 0xA)

    label("loc_15070")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15085")
    OP_29(0x34, 0x1, 0xB)

    label("loc_15085")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15099")
    OP_29(0x34, 0x4, 0x10)

    label("loc_15099")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_150AD")
    OP_29(0x34, 0x4, 0x20)

    label("loc_150AD")

    Jump("loc_150B2")

    label("loc_150B2")

    Jump("loc_12B03")

    label("loc_150B7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_59_12AF9 end

    SaveToFile()

Try(main)
