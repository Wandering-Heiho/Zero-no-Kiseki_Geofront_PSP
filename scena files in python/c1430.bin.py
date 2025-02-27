from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1430.bin",                # FileName
        "c1430",                    # MapName
        "c1430",                    # Location
        0x0032,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 50, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1430",                  # 0
        "Chief Guillaume",        # 1
        "Bracer Scott",           # 2
        "Bracer Wenzel",          # 3
        "Chief Roberts",          # 4
    ))

    AddCharChip((
        "chr/ch26400.itc",                   # 00
        "chr/ch27200.itc",                   # 01
        "chr/ch27300.itc",                   # 02
        "chr/ch29300.itc",                   # 03
    ))

    DeclNpc(5619,    0,       5329,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(550,     0,       4179,    90,   389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(709,     0,       5539,    135,  389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-51279,  0,       15350,   270,  389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)

    DeclActor(4150,    0,       4740,    1000,    5620,    1500,    5330,    0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_170",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_425",          # 02, 2
        "Function_3_5A5",          # 03, 3
        "Function_4_5C2",          # 04, 4
        "Function_5_1013",         # 05, 5
        "Function_6_38AE",         # 06, 6
        "Function_7_3D7F",         # 07, 7
        "Function_8_3EF5",         # 08, 8
        "Function_9_41A7",         # 09, 9
        "Function_10_4209",        # 0A, 10
        "Function_11_47B1",        # 0B, 11
        "Function_12_671B",        # 0C, 12
        "Function_13_88EF",        # 0D, 13
    ))


    def Function_0_170(): pass

    label("Function_0_170")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1B0"),
        (1, "loc_1BC"),
        (2, "loc_1C8"),
        (3, "loc_1D4"),
        (4, "loc_1E0"),
        (5, "loc_1EC"),
        (6, "loc_1F8"),
        (SWITCH_DEFAULT, "loc_204"),
    )


    label("loc_1B0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1BC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1C8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1D4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1E0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1EC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_204")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_210")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_227")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_227")

    Return()

    # Function_0_170 end

    def Function_1_228(): pass

    label("Function_1_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_253")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_2B8")

    label("loc_253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_28C")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    SetChrPos(0xB, 5620, 0, 5330, 270)
    Jump("loc_2B8")

    label("loc_28C")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 1040, 0, 7000, 270)
    SetChrPos(0xB, -490, 0, 7000, 90)
    SetChrFlags(0xB, 0x10)

    label("loc_2B8")

    Jump("loc_424")

    label("loc_2BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2CB")
    Jump("loc_424")

    label("loc_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2E3")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_424")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2F1")
    Jump("loc_424")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_310")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_424")

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_424")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_32C")
    Jump("loc_424")

    label("loc_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33A")
    Jump("loc_424")

    label("loc_33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_348")
    Jump("loc_424")

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_356")
    Jump("loc_424")

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_364")
    Jump("loc_424")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_383")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_424")

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_391")
    Jump("loc_424")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_END)), "loc_3CA")
    SetChrPos(0x8, 14820, 1000, 8970, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14820, 1000, 7170, 0)

    label("loc_3CA")

    Jump("loc_424")

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_424")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3EB")
    Jump("loc_424")

    label("loc_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_40A")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_424")

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_424")
    SetChrPos(0x8, 15240, 1000, 7610, 90)

    label("loc_424")

    Return()

    # Function_1_228 end

    def Function_2_425(): pass

    label("Function_2_425")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_444")

    label("loc_43E")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_444")

    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    ClearMapObjFlags(0x0, 0x4)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_49E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_483")
    OP_65(0x0, 0x1)
    Jump("loc_499")

    label("loc_483")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_495")
    Jump("loc_499")

    label("loc_495")

    OP_65(0x0, 0x1)

    label("loc_499")

    Jump("loc_5A4")

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4AC")
    Jump("loc_5A4")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4BA")
    Jump("loc_5A4")

    label("loc_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4C8")
    Jump("loc_5A4")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4DA")
    OP_65(0x0, 0x1)
    Jump("loc_5A4")

    label("loc_4DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4E8")
    Jump("loc_5A4")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4F6")
    Jump("loc_5A4")

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_504")
    Jump("loc_5A4")

    label("loc_504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_512")
    Jump("loc_5A4")

    label("loc_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_520")
    Jump("loc_5A4")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_52E")
    Jump("loc_5A4")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_540")
    OP_65(0x0, 0x1)
    Jump("loc_5A4")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_54E")
    Jump("loc_5A4")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_END)), "loc_564")
    OP_65(0x0, 0x1)

    label("loc_564")

    Jump("loc_5A4")

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_577")
    Jump("loc_5A4")

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_585")
    Jump("loc_5A4")

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_597")
    OP_65(0x0, 0x1)
    Jump("loc_5A4")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5A4")
    OP_65(0x0, 0x1)

    label("loc_5A4")

    Return()

    # Function_2_425 end

    def Function_3_5A5(): pass

    label("Function_3_5A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BE")
    Call(0, 10)
    Return()

    label("loc_5BE")

    Call(0, 4)
    Return()

    # Function_3_5A5 end

    def Function_4_5C2(): pass

    label("Function_4_5C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E3")
    Call(0, 11)
    Return()

    label("loc_5E3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_637")

    ChrTalk(
        0x8,
        (
            "Oh, you're all here?\x01",
            "Need some modifications done?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    SetScenarioFlags(0x4E, 4)
    Jump("loc_AF5")

    label("loc_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADF")

    ChrTalk(
        0x8,
        (
            "Hey, welcome.\x01",
            "What can I do ya for today?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_END)), "loc_6CF")

    ChrTalk(
        0x8,
        (
            "Ah, you folks are here.\x01",
            "You're those SSS guys from the CPD, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_752")

    label("loc_6CF")


    ChrTalk(
        0x8,
        (
            "Ah, you folks are here.\x01",
            "If my eyes aren't deceiving me, you're those cops\x01",
            "that were recently featured in the Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_752")


    ChrTalk(
        0x8,
        (
            "Well, whatever. As long as I'm making a buck, I don't care.\x01",
            "If you need me to spruce up your gear, let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I mainly dabble in orbment repairs, but I\x01",
            "can perk your weapons up, if you need it.\x01",
            "Just ask me to enhance your weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FYou can enhance weapons?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yep. Reinforcing weapons is child's play\x01",
            "if I have the right materials on hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I may not look the part anymore, but I was actually\x01",
            "a specialist at the Epstein Foundation's Materials\x01",
            "Engineering Division back in my prime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Just know that your gear's in good hands.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYou once worked at the foundation? Impressive.\x01",
            "That would explain your proficiency in modifications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FSweet. Sounds like we've got ourselves a nice hookup\x01",
            "for some decked out weapons we can't find elsewhere.\x02\x03",
            "If we run across any materials this old dude could\x01",
            "use, let's bring 'em over and get us some shiny\x01",
            "equipment.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    SetScenarioFlags(0x4E, 4)
    Jump("loc_AF5")

    label("loc_ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF5")
    Call(0, 6)
    TalkEnd(0x8)
    Return()

    label("loc_AF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE8")

    ChrTalk(
        0x8,
        (
            "Oh. Looks like ya managed to get your hands\x01",
            "on some T-Material, didja?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just say the word and I'll make that orbal\x01",
            "staff look brand spankin' new. I'm ready\x01",
            "to go any time ya need me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE8")

    SetScenarioFlags(0x0, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F04")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",               # 0
            "Customize\x01",          # 1
            "Upgrade Staff\x01",      # 2
            "Leave\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C59")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_C59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C78")
    OP_AF(0xAE)
    Jump("loc_CAA")

    label("loc_C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C88")
    OP_AF(0xAD)
    Jump("loc_CAA")

    label("loc_C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C98")
    OP_AF(0xAC)
    Jump("loc_CAA")

    label("loc_C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_CA8")
    OP_AF(0xAB)
    Jump("loc_CAA")

    label("loc_CA8")

    OP_AF(0xAA)

    label("loc_CAA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFF")

    label("loc_CB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECF")

    ChrTalk(
        0x8,
        (
            "I'll need to use that material you found\x01",
            "to upgrade the orbal staff. Should we\x01",
            "proceed with the upgrade?\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "[Please]\x01",       # 0
            "[Not Yet]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E43")

    ChrTalk(
        0x101,
        "#0000FYeah, please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Okay. Let's get this show on the road.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        "Everything good on your end, Roberts?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yep. I've got the materials, and I'm ready to go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Just hold on, I'm on my way!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 12)
    Return()

    label("loc_E43")


    ChrTalk(
        0x8,
        (
            "Oh, sure. Just let me know if you're itchin'\x01",
            "for an upgrade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm all prepped and ready to go. Just gimme the word.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EFF")

    label("loc_ECF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE3")
    Jump("loc_EFF")

    label("loc_EE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_EFF")

    Jump("loc_BF5")

    label("loc_F04")

    Jump("loc_100F")

    label("loc_F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_100C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1007")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",           # 0
            "Customize\x01",      # 1
            "Leave\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F72")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_F72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_F91")
    OP_AF(0xAE)
    Jump("loc_FC3")

    label("loc_F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_FA1")
    OP_AF(0xAD)
    Jump("loc_FC3")

    label("loc_FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_FB1")
    OP_AF(0xAC)
    Jump("loc_FC3")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_FC1")
    OP_AF(0xAB)
    Jump("loc_FC3")

    label("loc_FC1")

    OP_AF(0xAA)

    label("loc_FC3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1002")

    label("loc_FD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FE6")
    Jump("loc_1002")

    label("loc_FE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1002")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_1002")

    Jump("loc_F1C")

    label("loc_1007")

    Jump("loc_100F")

    label("loc_100C")

    Call(0, 5)

    label("loc_100F")

    TalkEnd(0x8)
    Return()

    # Function_4_5C2 end

    def Function_5_1013(): pass

    label("Function_5_1013")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110A")

    ChrTalk(
        0x8,
        (
            "The special material you'll need is called T-Material.\x01",
            "It's a bit of a rare one, or so I've heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll continue prepping things on our end, so give us a\x01",
            "shout when you've gathered everything you need!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38AD")

    label("loc_110A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_125C")

    ChrTalk(
        0x8,
        (
            "Don't worry about it. Didn't even break a sweat\x01",
            "performin' that upgrade. All I did was follow some\x01",
            "instructions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahahaha! Don't be a stranger! I'm not going to bite,\x01",
            "so come by and use my services whenever ya need!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FYes. We will be sure to do so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWe really appreciate you doing this for us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38AD")

    label("loc_125C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_153D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_130E")

    ChrTalk(
        0x8,
        "Oh, Aidios! It completely slipped my mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I bet if I could convince one of them guards\x01",
            "that I have authorization, he'd let me pass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14ED")

    label("loc_130E")


    ChrTalk(
        0x8,
        "Whoops. Evening already, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was planning on heading down to the foundation's branch\x01",
            "in Crossbell, but it completely slipped my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205FYou have business with the Epstein Foundation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah. I was thinkin' about talking to old\x01",
            "Roberts down there about a few things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Only problem is...the branch is located smack dab\x01",
            "in the middle of the IBC. Dangit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I figure the IBC building's already closed for\x01",
            "business at this time, so I'm outta luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 4)
    SetScenarioFlags(0x0, 0)

    label("loc_14ED")

    Jump("loc_1538")

    label("loc_14F2")


    ChrTalk(
        0x8,
        "H-Hey. You guys are here again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ya wanna upgrade somethin'?\x02",
    )

    CloseMessageWindow()

    label("loc_1538")

    Jump("loc_38AD")

    label("loc_153D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_162F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15F6")

    ChrTalk(
        0x8,
        (
            "Can't put my finger on it, but the town's\x01",
            "been givin' me the creeps all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Might just be 'cause I'm feeling woozy from\x01",
            "pullin' an all-nighter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_162A")

    label("loc_15F6")


    ChrTalk(
        0x8,
        "Hey, you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ya wanna upgrade somethin'?\x02",
    )

    CloseMessageWindow()

    label("loc_162A")

    Jump("loc_38AD")

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_17DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16CD")

    ChrTalk(
        0x8,
        (
            "There's no way an old coot like myself can\x01",
            "simply change the way I'm livin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "May as well run this factory until I keel over.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D5")

    label("loc_16CD")


    ChrTalk(
        0x8,
        (
            "I managed to meet up with that gal Wendy yesterday.\x01",
            "Been forever since I last saw her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Says she's used to workin' her job these days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh. Must be nice to still be young. I figure you can\x01",
            "probably adapt to anything life throws you pretty easily.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17D5")

    Jump("loc_38AD")

    label("loc_17DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 2)), scpexpr(EXPR_END)), "loc_191D")

    ChrTalk(
        0x8,
        (
            "Old Roberts down at the Epstein Foundation was a\x01",
            "buddy of mine back when I used to work there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Back in the day, all the brightest youngsters would\x01",
            "flock over to the Epstein Foundation to study\x01",
            "orbal technology and engineering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Of course, old Roberts and I were among\x01",
            "those youngsters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A55")

    label("loc_191D")


    ChrTalk(
        0x8,
        (
            "I was runnin' outta interesting ways to\x01",
            "spruce up weapons, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Figured I'd consult with my old friend, Roberts.\x01",
            "Started by draftin' up some nifty blueprints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's still some room for improvement, but hey,\x01",
            "somethin' is still better than nothin'!\x01",
            "Gimme a shout if you wanna give it a whirl.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 2)

    label("loc_1A55")

    Jump("loc_38AD")

    label("loc_1A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B25")

    ChrTalk(
        0x8,
        (
            "If there's anything ever troublin' you young folks,\x01",
            "don't be afraid to ask this old coot for advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it's within my power, I'll do my best to\x01",
            "help you fine folks out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D34")

    label("loc_1B25")


    ChrTalk(
        0x8,
        (
            "Oh. The famed Special Support Section has come\x01",
            "to pay me a visit? I'm honored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've heard all about your latest achievements,\x01",
            "y'know. Seems like you folks are really provin'\x01",
            "yourselves out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYou have? I feel like we've finally reached a point\x01",
            "where we can take a quick breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there's anything ever troublin' you young lads,\x01",
            "don't be afraid to ask this old coot for advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you ever need a place to lay low while you hide from\x01",
            "the bustle of the city, my door's always open to ya.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D34")

    Jump("loc_38AD")

    label("loc_1D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E0A")

    ChrTalk(
        0x8,
        (
            "I swear, bein' a perfectionist is going to end up killin' me.\x01",
            "How the hell am I ever going to meet my own standards?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, it's kinda fun tryin' to outdo myself, to be honest.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F28")

    label("loc_1E0A")


    ChrTalk(
        0x8,
        (
            "Been pretty busy tryin' to draft up some nifty new\x01",
            "blueprints for weapons upgrades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... No, not quite like that.\x01",
            "Not like this, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I usually come up with my best ideas outta nowhere.\x01",
            "Nothing I make when I'm actively thinking about it\x01",
            "seems to turn out well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F28")

    Jump("loc_38AD")

    label("loc_1F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1FEE")

    ChrTalk(
        0x8,
        (
            "You folks heading out somewhere? Better be careful!\x01",
            "These huge crowds tend to be merciless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Not a year passes by where there isn't a\x01",
            "ton of congestion after the parade.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38AD")

    label("loc_1FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2199")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2137")

    ChrTalk(
        0x8,
        (
            "Some guy had me repair one of them orbal-\x01",
            "powered kids' toys today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ya never know when work will come knockin' on\x01",
            "your door durin' the festival. You'd be kinda\x01",
            "surprised seein' how much work I get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've got a bunch of different material strengthening\x01",
            "tests I've been itchin' to try out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2194")

    label("loc_2137")


    ChrTalk(
        0x8,
        (
            "I don't got any plans to close up shop durin' the\x01",
            "festival. Stop by whenever ya'd like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2194")

    Jump("loc_38AD")

    label("loc_2199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2394")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_226C")

    ChrTalk(
        0x8,
        (
            "The orbal network and airships are what you'd\x01",
            "consider...sophisticated engineering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm a lil' interested in them, too. Though, look at\x01",
            "where this dingy shop of mine is located.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238F")

    label("loc_226C")


    ChrTalk(
        0x8,
        (
            "There's just some things ya can't get your\x01",
            "hands on in this dump.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Like the orbal network, for example.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ya think they'd ever lay down the cables\x01",
            "in a place like Downtown District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd be a lyin' old geezer if I said I wasn't\x01",
            "at least a little interested, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_238F")

    Jump("loc_38AD")

    label("loc_2394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2693")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 4)), scpexpr(EXPR_END)), "loc_246A")

    ChrTalk(
        0x8,
        (
            "Gotta say. I admire that proud and strong spirit\x01",
            "you folks seem to possess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ya better keep devotin' yourself to your duties, y'hear?!\x01",
            "This old man's excited to see what you can do!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268E")

    label("loc_246A")


    ChrTalk(
        0x8,
        (
            "Happy birthday, Crossbell! Ain't a happier time\x01",
            "in the year than right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if it isn't Crossbell's esteemed heroes! The gallant folks\x01",
            "that stopped the mayor from takin' a dirt nap!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FYou do realize how insanely embarrassing that is,\x01",
            "right? A little hyperbolic, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You'll have to forgive me. I'm a sucker for cheesy lines.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ya better keep devotin' yourself to your duties, y'hear?!\x01",
            "This old man's excited to see what you can do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYou got it, old man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWe appreciate the praise, Guillaume.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 4)

    label("loc_268E")

    Jump("loc_38AD")

    label("loc_2693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_27EA")

    ChrTalk(
        0x8,
        (
            "Supposedly, that U-Material I use for customizing\x01",
            "gear is dropped by monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Not only that, but they apparently like showin' up\x01",
            "in places where ya least expect it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if ya stumble across any unfamiliar materials,\x01",
            "I recommend hangin' on to 'em. Who knows?\x01",
            "I may even be able to use 'em for future upgrades.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38AD")

    label("loc_27EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_28E5")

    ChrTalk(
        0x8,
        (
            "Thanks to them fancy railways and airships that\x01",
            "pass through Crossbell, it feels like we're living\x01",
            "in some sorta fantasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Great Goddess. Are we the only nation blessed to\x01",
            "this extent when it comes to orbal technology?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2D")

    label("loc_28E5")


    ChrTalk(
        0x8,
        (
            "It's always out with the old, in with the new for us\x01",
            "Crossbellans. Ya folks ever realize how much\x01",
            "orbal technology is taken for granted here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Sheesh. Must be nice livin' a life so extravagant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I bet most folks 'round here don't even realize that most\x01",
            "of Zemuria is still stuck in the early days of orbal tech.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2A2D")

    Jump("loc_38AD")

    label("loc_2A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B0D")

    ChrTalk(
        0x8,
        (
            "Been experimentin' with some new ways to\x01",
            "upgrade your weapons. Interested?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This old coot can't wait to apply the finishin' touches.\x01",
            "I'll definitely show you the results, so don't worry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA6")

    label("loc_2B0D")


    ChrTalk(
        0x8,
        (
            "I'm just about finished experimentin' with some\x01",
            "new ways to upgrade your weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh. Ain't this a beauty? Believe it or not,\x01",
            "I made these blueprints from scratch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, actually... I kinda came up with it while I\x01",
            "was workin' on a bunch of other modifications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's still a prototype, but I'm excited to see\x01",
            "the final results. I'll definitely show you once\x01",
            "it's ready, so don't worry!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2CA6")

    Jump("loc_38AD")

    label("loc_2CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D5F")

    ChrTalk(
        0x8,
        "I'm glad Wendy seems to be chuggin' along.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wish she'd make some time for me every\x01",
            "once in a while, though. Oh, well...\x01",
            "I'm sure she's a busy lass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2D5F")


    ChrTalk(
        0x8,
        "How's Wendy doin' these days?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That girl could work her way around an orbment\x01",
            "when she was my apprentice, I'll tell ya what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If she ever gets bored of workin' at Genten,\x01",
            "I'd hire her faster than you can say 'orbment.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Been dealin' with a bunch of repair and upgrade jobs\x01",
            "lately... Startin' to think that I may need an extra set\x01",
            "of hands around here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2ED3")

    Jump("loc_38AD")

    label("loc_2ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3019")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_END)), "loc_2F85")

    ChrTalk(
        0x8,
        (
            "Old Roberts and I have been pals ever since\x01",
            "we worked together at the foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh. Twenty years and that nutjob hasn't\x01",
            "changed one bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3014")

    label("loc_2F85")


    ChrTalk(
        0x8,
        "Oh. You folks heading out somewhere this fine morning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Dunno where you're planning to go, but make sure\x01",
            "yer fully prepared, y'hear?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3014")

    Jump("loc_38AD")

    label("loc_3019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_30CD")

    ChrTalk(
        0x8,
        (
            "I had three more repair jobs come through\x01",
            "my door today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Dang. I really don't get enough help around here.\x01",
            "Should probably look into getting an apprentice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38AD")

    label("loc_30CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_33BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_END)), "loc_31FF")

    ChrTalk(
        0x8,
        (
            "I've been tinkerin' with orbal gadgets\x01",
            "ever since I was a wee lad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Been dabblin' with weapon upgrades in addition\x01",
            "to the usual repairs these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh. Feel free to give my services a whirl\x01",
            "if ya want, folks. I may not look the part,\x01",
            "but I get the job done. Trust me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B6")

    label("loc_31FF")


    ChrTalk(
        0x8,
        (
            "You folks have been rackin' up one achievement\x01",
            "after another, haven't ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Y'know those police officers that popped up\x01",
            "in the Crossbell Times?\x01",
            "That's you folks, yeah?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 5)), scpexpr(EXPR_END)), "loc_3349")

    ChrTalk(
        0x8,
        (
            "Heh. Just what I'd expect from Wendy's childhood pal.\x01",
            "Thanks for bein' a reliable young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha, thanks. I appreciate it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_33B3")

    label("loc_3349")


    ChrTalk(
        0x8,
        (
            "Heh. Thanks for givin' me back my quiet and peaceful\x01",
            "neighbood. Allow me to show some gratitude, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B3")

    SetScenarioFlags(0x6B, 4)

    label("loc_33B6")

    Jump("loc_38AD")

    label("loc_33BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3532")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3476")

    ChrTalk(
        0x8,
        (
            "Come by again if ya ever need somethin' from\x01",
            "me, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I may be outta spare parts for the day,\x01",
            "but I can still maintain your gear to\x01",
            "the usual standards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_352D")

    label("loc_3476")


    ChrTalk(
        0x8,
        (
            "Livin' downtown isn't nearly as bad as ya'd think.\x01",
            "Lotta spare parts lying around, waitin' to be discovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right. Think it's about time to see what I can\x01",
            "dig up today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_352D")

    Jump("loc_38AD")

    label("loc_3532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37FA")

    ChrTalk(
        0x8,
        "I used to work at the factory out in the city, y'know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Guess they converted it into an orbal store for\x01",
            "whatever reason as of last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, I figured...hey, what the hell?\x01",
            "Why not open up my own shop?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37F2")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005FOh, so you're the craftsman Wendy\x01",
            "was telling me about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh? Ya know that young lass, Wendy?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, I get it. You're that childhood friend\x01",
            "she'd always go on about! The one\x01",
            "who wanted to be a police officer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FSounds like Wendy's been telling\x01",
            "you a lot about me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, yeah. Wendy was my apprentice back when\x01",
            "Genten was still a factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Heh. Glad to hear she's still doin' well.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 5)

    label("loc_37F2")

    SetScenarioFlags(0x0, 0)
    Jump("loc_38AD")

    label("loc_37FA")


    ChrTalk(
        0x8,
        (
            "If you folks ever need somethin' repaired,\x01",
            "don't hesitate to stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I may be outta spare parts for the day,\x01",
            "but I can still maintain your gear to\x01",
            "the usual standards.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38AD")

    Return()

    # Function_5_1013 end

    def Function_6_38AE(): pass

    label("Function_6_38AE")

    EventBegin(0x0)
    Fade(500)
    OP_68(14750, 2250, 7600, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 13750, 1000, 7200, 90)
    SetChrPos(0x102, 13650, 1000, 8000, 90)
    SetChrPos(0x103, 12500, 1000, 7200, 90)
    SetChrPos(0x104, 12400, 1000, 8000, 90)
    OP_93(0x8, 0x10E, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        "Oh, you folks customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've already used up all of my spare parts\x01",
            "for the day. Sorry 'bout that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Come back another time if ya need anythin'.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHey, um... This is a factory, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(*click* *clack*)\x02\x03",
            "#0200FThere are no records of this business\x01",
            "in the database, either. He must not\x01",
            "be in possession of a permit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! A smart lass, you are. You'd be correct,\x01",
            "as I've yet to submit an application.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This isn't an official shop. I'm just runnin' it\x01",
            "for my own personal pleasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Like to use it to repair broken orbal devices.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FIt is essentially a repair shop, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FFigures you can count on Crossbell to find\x01",
            "anything you'd ever need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FIf I may respectfully comment, sir. It would be in\x01",
            "your best interest to apply for a business permit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Bwahaha. You may be right, missy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, I figure it's about time I closed up shop.\x01",
            "If ya folks ever need help, you know where to find me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It'll barely cost ya anythin' for some trivial repairs.\x01",
            "I can fix a broken orbal light for dirt cheap!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 13750, 1000, 7600, 90)
    SetScenarioFlags(0x4A, 3)
    EventEnd(0x5)
    Return()

    # Function_6_38AE end

    def Function_7_3D7F(): pass

    label("Function_7_3D7F")

    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By talking to Guillaume and selecting 'Customize,'\x01",
            "a list of possible upgrades will be displayed. If you\x01",
            "have the necessary materials, you can create it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Weapons and armor made by customizing are\x01",
            "stronger, cannot be bought at weapons shops,\x01",
            "and special effects may be added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters may drop the necessary materials.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Return()

    # Function_7_3D7F end

    def Function_8_3EF5(): pass

    label("Function_8_3EF5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_41A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B9")

    ChrTalk(
        0xFE,
        (
            "Yep, it's as good as new.\x01",
            "This place never fails to get the job done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh. Hey, Scott. Do you come here regularly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FW-Well, this store gives off the impression\x01",
            "that it's an illegally-run business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. No need to be as stiff as a board.\x01",
            "You guys come here often, too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A bracer has to take advantage of everything at\x01",
            "their disposal, or we'd have trouble making it in\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41A3")

    label("loc_40B9")


    ChrTalk(
        0xFE,
        (
            "I dropped off my rifle for repairs the other day,\x01",
            "so I just came back to pick it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Needed some tuning up, considering the recent\x01",
            "uptick of powerful monsters around Crossbell.\x01",
            "Remember, guys: You can never be too prepared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41A3")

    TalkEnd(0xFE)
    Return()

    # Function_8_3EF5 end

    def Function_9_41A7(): pass

    label("Function_9_41A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4205")

    ChrTalk(
        0xFE,
        (
            "Hmm...\x01",
            "Might be a good idea to bring my Enigma here\x01",
            "the next time it breaks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4205")

    TalkEnd(0xFE)
    Return()

    # Function_9_41A7 end

    def Function_10_4209(): pass

    label("Function_10_4209")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422A")
    Call(0, 11)
    Return()

    label("loc_422A")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4481")

    ChrTalk(
        0xB,
        (
            "I'll now begin the preparations to install\x01",
            "the new programming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's nothing more than a large update, but unpacking\x01",
            "the components takes a considerable amount of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FPeople will begin to think you are employed here\x01",
            "if you stand at the counter for too long, Chief.\x01",
            "Is that not misleading?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xB, 0x103, 500)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "I-I'm sorry, Tio! I can't help it. This place is\x01",
            "too dark for my poor old eyes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F(Can't you give the poor guy a break\x01",
            "every once in a while, Tio?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203F(My apologies. It comes naturally.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4590")

    label("loc_4481")


    ChrTalk(
        0xB,
        (
            "No need to worry. I'll begin preparations necessary\x01",
            "for implementing the supplemental programming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please speak with Guillaume once you've\x01",
            "gathered the required materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We'll be ready to implement the modifications\x01",
            "whenever you're ready to begin, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4590")

    Jump("loc_47AD")

    label("loc_4595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4618")

    ChrTalk(
        0xB,
        "Hahaha. I am completely prepared.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've moved all of the necessary tools for\x01",
            "the modification to this shop!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47AD")

    label("loc_4618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_46AF")

    ChrTalk(
        0xB,
        (
            "Guillaume is an old friend of mine.\x01",
            "We try to keep in touch...occasionally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I had no idea that he had opened up\x01",
            "a repair shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47AD")

    label("loc_46AF")


    ChrTalk(
        0xB,
        "Hello there, Tio. How is the analyzer functioning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Would you like me to calibrate it for you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThat is unnecessary, Chief. I can perform\x01",
            "the calibration more efficiently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "O-Oh. Really?\x01",
            "(*grumble* I just wanted to help you...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_47AD")

    TalkEnd(0xB)
    Return()

    # Function_10_4209 end

    def Function_11_47B1(): pass

    label("Function_11_47B1")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(510, 1000, 6090, 0)
    MoveCamera(42, 23, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(28680, 0)
    SetChrPos(0x101, 380, 0, 4670, 0)
    SetChrPos(0x102, -230, 0, 3500, 0)
    SetChrPos(0x103, -830, 0, 4330, 0)
    SetChrPos(0x104, 1200, 0, 4160, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4863")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 780, 0, 2600, 0)

    label("loc_4863")

    SetChrPos(0x8, 1000, 0, 7430, 270)
    SetChrPos(0xB, -400, 0, 7430, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        "#11PAh, you're all here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FHello, Guillaume. We saw your support request.\x01",
            "Mind telling us the details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FHey there, Mr. Fixer Upper. Appreciate\x01",
            "the help as always, old man.\x02\x03",
            "#0305FOh, uh...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x13B, 0x1F4)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(700)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    def lambda_49A8():
        OP_95(0xFE, -870, 0, 5820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_49A8)

    ChrTalk(
        0xB,
        "#5PTio, it's been too long!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PHow have you been doing?\x01",
            "Are you still in good health?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0205FAh. You are involved, Chief.\x02\x03",
            "#0211FAdditionally, it has only been a short period of\x01",
            "time since you last saw me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0109FAhaha...\x01",
            "(Tio's relationship with Chief Roberts seems\x01",
            "awfully complicated, doesn't it?)\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EAC")

    ChrTalk(
        0x10A,
        (
            "#12P#0603FMr. Roberts of the Epstein Foundation, and\x01",
            "former foundation engineer, Guillaume.\x02\x03",
            "#0600FI've read through the outline of your request already.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_4C0A():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C0A)

    def lambda_4C17():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4C17)

    def lambda_4C24():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C24)

    def lambda_4C31():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4C31)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#0005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#0600FI'll be waiting for you outside.\x01",
            "Let me know when you're finished.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x10A, 300, 0, -1400, 2000, 0x0)
    OP_95(0x10A, 300, 0, -3210, 2000, 0x0)

    ChrTalk(
        0xB,
        (
            "#5PIs he your division chief, Tio? He seems\x01",
            "like quite the sharp man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203F*sigh* He is Alex Dudley of the First Division.\x01",
            "Our circumstances are complicated, so we are\x01",
            "working together for the time being.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4DAC():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DAC)

    def lambda_4DB9():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DB9)

    def lambda_4DC6():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4DC6)

    def lambda_4DD3():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4DD3)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#0105FI believe we may have barged into\x01",
            "the middle of your conversation.\x01",
            "Are we interrupting something important?\x02\x03",
            "#0100FWe don't mind returning at a more\x01",
            "convenient time, if that's the case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F74")

    label("loc_4EAC")

    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#0105FOur apologies if we barged into the middle of\x01",
            "your conversation. Are we interrupting you?\x02\x03",
            "#0100FWe don't mind returning at a more\x01",
            "convenient time, if that's the case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F74")


    ChrTalk(
        0x8,
        (
            "#11PAh, no. Save your worrying for something that\x01",
            "needs it. In fact, I'll leave the explanation to\x01",
            "my old chum Roberts here...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0xB, 0x8, 500)
    Sleep(500)
    OP_95(0xB, -210, 0, 6430, 5000, 0x0)

    ChrTalk(
        0xB,
        (
            "#5PHuh? Guillaume?! I could have sworn I\x01",
            "begged you to keep quiet about--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0211F*staaaaaare*\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xB, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#5PI-It's not what you think, Tio. I swear!\x01",
            "I promise there's nothing suspicious\x01",
            "about this at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PEr, um... We've got a bit of a complex\x01",
            "situation on our hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FA complex situation? How so?\x02\x03",
            "#0001FI imagine it's related to the request.\x01",
            "Mind filling us in on the details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PR-Right, I'll tell you everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PThis request actually concerns the foundation.\x02",
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
        0xB,
        (
            "#5PI believe you're aware that the foundation has\x01",
            "been collecting Tio's combat data for the orbal\x01",
            "staff tests in Crossbell, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PWe're using Tio's data as a reference to\x01",
            "continuously improve the orbal staff's\x01",
            "potency and efficiency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PThis request was made with the intention of\x01",
            "unlocking a new function within the staff.\x01",
            "A function that is currently deactivated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FWhat does unlocking a new function entail?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FYou tellin' us that Tio Tot's gonna get a\x01",
            "sweet new ability?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#6P#0203FThe function is for the staff,\x01",
            "not me, Randy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5542():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5542)

    def lambda_554F():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_554F)

    def lambda_555C():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_555C)
    Sleep(400)

    ChrTalk(
        0x103,
        (
            "#6P#0200FMany complex functions already lay dormant\x01",
            "within the staff's code.\x02\x03",
            "#0203FHowever, there are no programs available that will\x01",
            "allow me to safely utilize them...\x02\x03",
            "#0200FThere is a strong possibility that a new program\x01",
            "has already been in development. At least, I\x01",
            "believe this to be the purpose of the request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105FWell, what kind of function is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PTo keep it simple, it's related to a new craft.\x02",
    )

    CloseMessageWindow()

    def lambda_5719():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5719)

    def lambda_5726():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5726)

    def lambda_5733():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5733)

    def lambda_5740():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5740)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#5PThrough the application of a new program, the orbal staff\x01",
            "will be able to activate a new, robust function.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI've already checked out the materials list, too.\x01",
            "This staff's going to become one heck of a beast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWe sadly can't activate the new function in the current\x01",
            "staff without puttin' Tio in harm's way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWe're goin' to need to improve the handle\x01",
            "so she can get a better grip on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FW-Wow. I don't really get it, but it sounds incredible.\x02\x03",
            "#0005FSo, will Tio be able to use this new function if\x01",
            "upgrades are made to the staff?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PShe sure will. Just a teensy bit of a problem, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe shipment carryin' the program and\x01",
            "required parts has been delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P'Cause of a silly mistake on their end,\x01",
            "we're going to have to wait another week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PIn fact, this is what the request is related to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIf things continue the way they have,\x01",
            "then it'll inconvenience Tio as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PWe couldn't stand here and wait, so\x01",
            "we wanted to give Tio a helping hand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FAh. So that's why the request was called\x01",
            "'Orbal Staff Enhancement,' eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FIt all makes sense now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FWhile a week-long delay is unfortunate,\x01",
            "I am not particularly irritated by it.\x02\x03",
            "#0200FI am interested in testing out the new function\x01",
            "as soon as possible, though. After all, I am partly\x01",
            "responsible for writing the program.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FIf Tio's combat prowess can increase after\x01",
            "the upgrade, it'd be a great help towards our\x01",
            "investigations.\x02\x03",
            "#0005FAre you implying there's something you can\x01",
            "do about the delayed shipment? Have you\x01",
            "come up with an alternative?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)
    OP_63(0xB, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    ChrTalk(
        0xB,
        (
            "#5PHaha. I'm glad you asked, Lloyd.\x01",
            "As a matter of fact, I have!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#5PThanks to the documents we received earlier,\x01",
            "we were able to reconstruct the program needed\x01",
            "for the upgrade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAll that's left is to procure the materials required\x01",
            "for the attachments to the orbal staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAnd that's where your old pal comes in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAs you all know, repairs and modifications are my forte.\x01",
            "Now that I've gone through those documents, the parts\x01",
            "are as good as yours...as long as ya get me the materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FOh, I see what you're saying. If we gather\x01",
            "you the materials, you'd be able to finish\x01",
            "up this project.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_605E():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_605E)

    def lambda_606B():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_606B)

    def lambda_6078():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6078)

    def lambda_6085():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6085)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#11P#0000FHey, guys. Why don't we pitch in and help\x01",
            "for Tio's sake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FYes, I was thinking the same thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FNo complaints from me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0205FIs this truly okay?\x01",
            "Our investigation may be delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0309FHaha. We're just gatherin' some materials.\x01",
            "It's no biggie, Tio Tot. I could do that in my sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FI agree with Randy. And much like Lloyd said,\x01",
            "increasing your combat prowess is sure to\x01",
            "make our investigations go more smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FYeah, there's really no reason not to do this.\x02\x03",
            "What do you think, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FAn acceptable idea. I will be relying on your\x01",
            "assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FSounds like a plan.\x02",
    )

    CloseMessageWindow()

    def lambda_633E():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_633E)

    def lambda_634B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_634B)

    def lambda_6358():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6358)

    def lambda_6365():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6365)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#6P#0200FWhich materials are necessary to apply the\x01",
            "modifications?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAh, it's a special material called T-Material.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI heard it might be kinda difficult to\x01",
            "find 'em in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FIs that so? Well, we'll search for it\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAh. Now's a good time to tell you that we only\x01",
            "need one of them. I hope you manage to find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PPlease speak with Guillaume once you've\x01",
            "gathered one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PWe'll proceed with preparations to modify\x01",
            "the orbal staff once you've done so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FI suppose I will be relying on you this time, Chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FShall we go, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FYeah. Let's go hunt this bad boy down!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Orbal Staff Enhancement]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115090, 1500, 58830, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -200, 0, 3820, 0)
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    SetChrPos(0xB, 5620, 0, 5330, 270)
    ClearChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66FA")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_66FA")

    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_29(0x31, 0x1, 0x0)
    SetScenarioFlags(0x4E, 4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_47B1 end

    def Function_12_671B(): pass

    label("Function_12_671B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0x8)
    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(13800, 2300, 7800, 0)
    MoveCamera(61, 26, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(24880, 0)
    SetChrPos(0x101, 12800, 1000, 7200, 90)
    SetChrPos(0x102, 12800, 1000, 8100, 90)
    SetChrPos(0x103, 12800, 1000, 9000, 90)
    SetChrPos(0x104, 12800, 1000, 6300, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67D0")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 12110, 1000, 9870, 90)

    label("loc_67D0")

    SetChrPos(0x8, 15200, 1000, 8900, 225)
    SetChrPos(0xB, 15240, 1000, 7610, 270)
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x0, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PI'm done verifyin' the required materials.\x01",
            "We're ready to roll.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F6F")

    ChrTalk(
        0x10A,
        (
            "#6P#0604FSo you're going to have a weapon modification done.\x01",
            "What an honor to witness such a spectacle.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_68E5():

        label("loc_68E5")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_68E5")

    QueueWorkItem2(0x104, 1, lambda_68E5)
    Sleep(50)

    def lambda_68FA():

        label("loc_68FA")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_68FA")

    QueueWorkItem2(0x101, 1, lambda_68FA)

    def lambda_690C():

        label("loc_690C")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_690C")

    QueueWorkItem2(0x102, 1, lambda_690C)

    def lambda_691E():

        label("loc_691E")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_691E")

    QueueWorkItem2(0x103, 1, lambda_691E)

    def lambda_6930():

        label("loc_6930")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_6930")

    QueueWorkItem2(0xB, 1, lambda_6930)

    def lambda_6942():

        label("loc_6942")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_6942")

    QueueWorkItem2(0x8, 1, lambda_6942)
    Sleep(400)

    ChrTalk(
        0x104,
        (
            "#12P#0300FHey, so you're getting into it after all.\x01",
            "I'm proud of ya, Glasses!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#6P#0601FYou idiot. I was being sarcastic! Why are we\x01",
            "humoring trivial requests when we're in the\x01",
            "middle of an important investigation?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#0103FW-We're sorry. You might be right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FI apologize for not realizing it sooner,\x01",
            "Detective Dudley.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x10A,
        (
            "#6P#0603FHmph... Don't misunderstand. I know your\x01",
            "circumstances are unique, Plato.\x02\x03",
            "#0601FI may have acted out of line. Finish this up\x01",
            "as quickly as you can so we can get back to\x01",
            "the investigation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FR-Right. Don't worry, we will.\x02",
    )

    CloseMessageWindow()
    OP_95(0x10A, 7200, 0, 9870, 2000, 0x0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#11PThat's what detectives from the First Division\x01",
            "are like, huh?\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0x8, 0x1)

    def lambda_6C99():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C99)

    def lambda_6CA6():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6CA6)

    def lambda_6CB3():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6CB3)

    def lambda_6CC0():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6CC0)
    OP_93(0x8, 0xE1, 0x190)
    Sleep(400)

    ChrTalk(
        0xB,
        (
            "#11PWould you like to postpone the upgrade, Tio?\x01",
            "Wouldn't want to make your friend wait now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FNot to worry, Chief. This behavior is\x01",
            "typical of Detective Dudley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FI think he understood the situation, anyway.\x01",
            "We may as well hurry and complete the\x01",
            "modifications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYeah, looks it. Ya wanna get started?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PSounds good. We'll try to complete the\x01",
            "modifications with record timing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0xB,
        (
            "#11PNow that I'm in the right mindset, I can really\x01",
            "feel the adrenaline pumping through my veins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PHahaha. I'm looking forward to this!\x01",
            "I can already picture Tio gallantly\x01",
            "brandishing her new orbal staff!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7024")

    label("loc_6F6F")


    ChrTalk(
        0xB,
        "#11PAll right, everything's ready.\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0xB,
        (
            "#11PHaha. I'm looking forward to this!\x01",
            "I can already picture Tio, gallantly\x01",
            "brandishing her new orbal staff!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7024")


    ChrTalk(
        0x103,
        (
            "#6P#0211FChief.\x02\x03",
            "If the orbal staff is rendered useless thanks to\x01",
            "a bug, you will be punished. Do you understand?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        "#11PN-No way... A-Anything but that, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PWhat have I done to deserve this?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FUh, Chief. Nothing's happened yet.\x01",
            "Take a deep breath and relax.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        "#5PCome back to us, Roberts.\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xB,
        "#11PH-Huh?!\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x190)
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#11PO-Oh, sorry. Let's go ahead and begin\x01",
            "the process, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PDo you mind waiting a little bit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FOf course not. We'll just sit here\x01",
            "and watch you, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(800)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others spent the next thirty\x01",
            "minutes observing the process.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They were unable to understand the details, but\x01",
            "the orbal staff upgrade proceeded smoothly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And then...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x103, 250, 0, 6400, 255)
    SetChrPos(0x8, -820, 0, 8210, 166)
    SetChrPos(0xB, 1100, 0, 8510, 211)
    SetChrPos(0x101, -2090, 0, 2600, 31)
    SetChrPos(0x102, -880, 0, 2190, 346)
    SetChrPos(0x104, -2730, 0, 3880, 31)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73EA")
    SetChrPos(0x10A, 230, 0, -1850, 38)
    SetChrFlags(0x10A, 0x80)

    label("loc_73EA")

    OP_68(-520, 1600, 5910, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16770, 0)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00257.itc", 0x1F)
    LoadChrToIndex("chr/ch0025A.itc", 0x20)
    LoadEffect(0x0, "battle\\cr002403.eff")
    LoadEffect(0x1, "battle\\cr002401.eff")
    SetChrChipByIndex(0x103, 0x1E)
    BeginChrThread(0x103, 0, 0, 13)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    OP_A0(0x103, 1500, 0x0, 0x2)
    Sleep(300)
    OP_A0(0x103, 1500, 0x2, 0x3)
    Sound(279, 0, 100, 0)
    SetChrSubChip(0x103, 0x4)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x103, 0xC0, 200, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(363, 0, 100, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x103, 0xC0, 200, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(274, 0, 100, 0)
    Sleep(100)
    Fade(300)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sleep(2500)
    PlayEffect(0x1, 0xFF, 0x103, 0xC0, 200, 550, 850, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(280, 0, 90, 0)
    Sound(323, 0, 90, 0)
    Sleep(4500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x103)
    Sleep(1000)
    Fade(300)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 0, 0, 13)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5PHow's it feel? I think I applied the adjustments\x01",
            "the way I was supposed to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FWell, then...\x02\x03",
            "#0200FI feel some discomfort due to the code having\x01",
            "been completely overwritten. It is not terrible,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PI bet it's due to the balance control. If anyone can\x01",
            "get used to it, it'd be you, Tio. I believe in you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PPlease copy over any programs utilized\x01",
            "by the Aeon system when you change to\x01",
            "a different orbal staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAlso, please don't forget to install any\x01",
            "of the attachments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_68(-630, 1000, 5470, 2200)
    MoveCamera(67, 26, 0, 2200)
    SetCameraDistance(20230, 2200)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#6P#0305FYo, Lloyd... Any idea if that went well?\x01",
            "'Cause I sure as hell couldn't tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FI'm not sure, either. I definitely wasn't expecting\x01",
            "the orbal staff to open like that, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FI wouldn't have expected your staff to\x01",
            "have so many different functions...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#0105FAh, right.\x01",
            "How does it handle now, Tio?\x02\x03",
            "#0100FAre you able to perform that new craft?\x02",
        )
    )

    CloseMessageWindow()
    Fade(300)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    OP_0D()
    Sleep(300)

    def lambda_799B():
        OP_95(0xFE, -990, 0, 4810, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_799B)
    Sleep(300)

    def lambda_79B8():
        OP_95(0xFE, -1390, 0, 6630, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_79B8)

    def lambda_79D2():
        OP_95(0xFE, 250, 0, 6400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_79D2)
    Sleep(2000)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#11P#0200FYes, the upgrade is complete. I should be\x01",
            "able to perform all of the new functions\x01",
            "efficiently and without error.\x02\x03",
            "#0203F'Absolute Zero' allows me to launch\x01",
            "anti-energy bullets at zero degrees.\x02\x03",
            "#0200FThough I cannot fire them excessively,\x01",
            "I imagine they will prove quite useful\x01",
            "in more intense fights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FReally? Well, that's reassuring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FHaha. Sounds like that thing'll be able to\x01",
            "bail us out if we're ever in a pickle.\x01",
            "I'm itchin' to see it in action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FWe'll definitely be counting on you\x01",
            "for your support, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0200FRoger.\x02",
    )

    CloseMessageWindow()

    def lambda_7C45():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7C45)

    def lambda_7C52():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C52)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#11P#0200FChief, Guillaume.\x01",
            "Thank you for your efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYeah, we appreciate the help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, that little thing was no big deal.\x01",
            "Don't worry about it at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PRight, no need to thank us. It was our\x01",
            "proposal, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PBesides, I'm glad we were able to complete\x01",
            "all of the intended modifications successfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PI was prepared for your rejection from the very beginning.\x01",
            "Putting Guillaume's name on the request was brilliant!\x01",
            "It must have opened you up to the idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(14)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x103, 0xB, 500)
    TurnDirection(0x101, 0xB, 500)
    Sleep(200)

    ChrTalk(
        0x103,
        "#6P#0211F*stare*...\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#11PN-No, never mind.\x01",
            "Don't worry about what I just said.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x1F4)
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#11PWhoops, would you look at the time?\x01",
            "I think I'll make my swift exit!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xE1, 0x1F4)
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#11PConduct combat tests with the staff, Tio. Okay?\x01",
            "Well, then... Until next time!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_800B():

        label("loc_800B")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_800B")

    QueueWorkItem2(0x101, 1, lambda_800B)

    def lambda_801D():

        label("loc_801D")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_801D")

    QueueWorkItem2(0x102, 1, lambda_801D)

    def lambda_802F():

        label("loc_802F")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_802F")

    QueueWorkItem2(0x104, 1, lambda_802F)

    def lambda_8041():

        label("loc_8041")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_8041")

    QueueWorkItem2(0x103, 1, lambda_8041)

    def lambda_8053():

        label("loc_8053")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_8053")

    QueueWorkItem2(0x8, 1, lambda_8053)

    def lambda_8065():
        OP_95(0xFE, 1200, 0, 1500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8065)
    WaitChrThread(0xB, 1)

    def lambda_8083():
        OP_95(0xFE, 0, 0, 1500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8083)
    WaitChrThread(0xB, 1)

    def lambda_80A1():
        OP_95(0xFE, 0, 0, -2000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_80A1)
    Sound(105, 0, 100, 0)

    def lambda_80C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_80C1)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xB, 0x80)
    Sleep(1100)

    ChrTalk(
        0x103,
        "#6P#0206F*sigh* Why must he be like this?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x1)

    ChrTalk(
        0x101,
        (
            "#12P#0000FI could at least tell that he was genuinely\x01",
            "worried for you, Tio. I'm sure he's only\x01",
            "like that because he cares for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThat old man hasn't become one bit less\x01",
            "overbearing, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86B2")
    ClearChrFlags(0x10A, 0x80)

    NpcTalk(
        0x10A,
        "Man's Voice",
        "#3PYou're all finished with it now?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(-380, 1000, 4920, 3000)
    MoveCamera(14, 20, 0, 3000)

    def lambda_82B1():

        label("loc_82B1")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_82B1")

    QueueWorkItem2(0x101, 1, lambda_82B1)

    def lambda_82C3():

        label("loc_82C3")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_82C3")

    QueueWorkItem2(0x102, 1, lambda_82C3)

    def lambda_82D5():

        label("loc_82D5")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_82D5")

    QueueWorkItem2(0x104, 1, lambda_82D5)

    def lambda_82E7():

        label("loc_82E7")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_82E7")

    QueueWorkItem2(0x103, 1, lambda_82E7)

    def lambda_82F9():

        label("loc_82F9")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_82F9")

    QueueWorkItem2(0x8, 1, lambda_82F9)
    OP_95(0x10A, 730, 0, 2370, 2000, 0x0)
    OP_93(0x10A, 0x13B, 0x1F4)
    Sleep(200)
    OP_6F(0x79)

    ChrTalk(
        0x10A,
        (
            "#12P#0600FI assume you've successfully\x01",
            "modified the orbal staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0200FYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FSorry it took so long, Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#0603FHmph. You've got that right. Imagine\x01",
            "going in for weapon maintenance in\x01",
            "the middle of an urgent situation.\x02\x03",
            "#0601FWell, no matter. Could we return to our\x01",
            "investigation if you're finished?\x02\x03",
            "We can't afford to put it off any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FUnderstood. Let's move, then.\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x1)

    def lambda_84F3():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84F3)

    def lambda_8500():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8500)

    def lambda_850D():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_850D)

    def lambda_851A():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_851A)
    Sleep(400)

    ChrTalk(
        0x101,
        "#12P#0000FWe'll be heading out now, Guillaume.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FWe owe you one, sir. You can always\x01",
            "count on us to help you, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSure. Don't really get what's happenin',\x01",
            "but keep hangin' in there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDudley, was it? Don't be a stranger.\x01",
            "Come to my factory any time you\x01",
            "need to maintain your weapon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#0604FHmph... Well, I'll consider it.\x02\x03",
            "#0600FUntil we meet again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_880B")

    label("loc_86B2")


    ChrTalk(
        0x8,
        (
            "#5PEh. Figure things are gonna die down\x01",
            "for a little bit.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_86F9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86F9)

    def lambda_8706():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8706)

    def lambda_8713():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8713)

    def lambda_8720():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8720)
    Sleep(300)

    ChrTalk(
        0x8,
        "#5P'Bout time I get back to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYa better put that staff to good use, y'hear?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FNaturally. I will use it to the best of my abilities.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FYou can always count on us to\x01",
            "help you, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_880B")

    AddCraft(0x2, 0xAE)
    SubItemNumber(0x397, 1)
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Orbal Staff Enhancement]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 0, 4190, 180)
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    OP_4C(0x8, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88DB")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_88DB")

    OP_29(0x31, 0x4, 0x10)
    OP_29(0x31, 0x1, 0x1)
    SetScenarioFlags(0x0, 4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_671B end

    def Function_13_88EF(): pass

    label("Function_13_88EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8906")
    OP_A0(0x103, 1200, 0x0, 0x4)
    Jump("Function_13_88EF")

    label("loc_8906")

    Return()

    # Function_13_88EF end

    SaveToFile()

Try(main)
