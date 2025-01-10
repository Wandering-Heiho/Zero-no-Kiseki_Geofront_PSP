from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1450.bin",                # FileName
        "c1450",                    # MapName
        "c1450",                    # Location
        0x0033,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 51, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1450",                  # 0
        "Old Man Tantz",          # 1
        "Geithner",               # 2
        "Corona",                 # 3
        "Lima",                   # 4
        "Melson",                 # 5
        "Old Man Tantz",          # 6
        "Michaud",                # 7
        "Geithner",               # 8
        "Rixia",                  # 9
        "Politician",             # 10
        "Man in Suit",            # 11
        "Man's Voice",            # 12
    ))

    AddCharChip((
        "chr/ch24000.itc",                   # 00
        "chr/ch24002.itc",                   # 01
        "chr/ch21000.itc",                   # 02
        "chr/ch21002.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch24402.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch27700.itc",                   # 09
        "chr/ch27600.itc",                   # 0A
        "chr/ch23000.itc",                   # 0B
        "chr/ch24700.itc",                   # 0C
        "chr/ch05200.itc",                   # 0D
    ))

    DeclNpc(4269,    0,       -52159,  90,   261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(52340,   29,      959,     180,  261,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(51200,   0,       54049,   0,    261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10270,   3500,    11050,   135,  261,  0x0, 0,   7,   0,   0,   2,   0,   13,  255,  0)
    DeclNpc(9609,    3500,    13869,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1399,   200,     -55000,  90,   389,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-46349,  200,     1899,    180,  261,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(1549,    200,     -55159,  270,  389,  0x0, 0,   3,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-1639,   29,      56029,   0,    389,  0x0, 0,   13,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(3809,    0,       1059,    135,  389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(2700,    0,       1490,    135,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(17899,   3500,    -39,     0,    126,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)

    DeclActor(17900,   3500,    -40,     1500,    17900,   4800,    -40,     0x007C, 0,  16, 0x0000)
    DeclActor(-140,    3500,    21470,   1500,    -140,    5000,    21470,   0x007C, 0,  29, 0x0000)

    ScpFunction((
        "Function_0_2DC",          # 00, 0
        "Function_1_394",          # 01, 1
        "Function_2_3BF",          # 02, 2
        "Function_3_3EA",          # 03, 3
        "Function_4_415",          # 04, 4
        "Function_5_6F2",          # 05, 5
        "Function_6_76D",          # 06, 6
        "Function_7_20A1",         # 07, 7
        "Function_8_2230",         # 08, 8
        "Function_9_235D",         # 09, 9
        "Function_10_3992",        # 0A, 10
        "Function_11_3B65",        # 0B, 11
        "Function_12_5433",        # 0C, 12
        "Function_13_6A72",        # 0D, 13
        "Function_14_772E",        # 0E, 14
        "Function_15_77BE",        # 0F, 15
        "Function_16_7886",        # 10, 16
        "Function_17_8337",        # 11, 17
        "Function_18_8379",        # 12, 18
        "Function_19_850B",        # 13, 19
        "Function_20_86A8",        # 14, 20
        "Function_21_8D3C",        # 15, 21
        "Function_22_8F76",        # 16, 22
        "Function_23_94AB",        # 17, 23
        "Function_24_9C75",        # 18, 24
        "Function_25_9C9D",        # 19, 25
        "Function_26_9CD9",        # 1A, 26
        "Function_27_9D0B",        # 1B, 27
        "Function_28_9D3D",        # 1C, 28
        "Function_29_A160",        # 1D, 29
    ))


    def Function_0_2DC(): pass

    label("Function_0_2DC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_31C"),
        (1, "loc_328"),
        (2, "loc_334"),
        (3, "loc_340"),
        (4, "loc_34C"),
        (5, "loc_358"),
        (6, "loc_364"),
        (SWITCH_DEFAULT, "loc_370"),
    )


    label("loc_31C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_328")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_334")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_340")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_34C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_358")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_364")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_370")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_37C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_393")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_37C")

    label("loc_393")

    Return()

    # Function_0_2DC end

    def Function_1_394(): pass

    label("Function_1_394")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BE")
    OP_94(0xFE, 0xC602, 0xFFFFF538, 0xCFDA, 0xF50, 0x3E8)
    Sleep(300)
    Jump("Function_1_394")

    label("loc_3BE")

    Return()

    # Function_1_394 end

    def Function_2_3BF(): pass

    label("Function_2_3BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E9")
    OP_94(0xFE, 0x1CFC, 0x208A, 0x2FBC, 0x337C, 0x3E8)
    Sleep(300)
    Jump("Function_2_3BF")

    label("loc_3E9")

    Return()

    # Function_2_3BF end

    def Function_3_3EA(): pass

    label("Function_3_3EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_414")
    OP_94(0xFE, 0xCC74, 0xBCCA, 0xD8C2, 0xC4C2, 0x3E8)
    Sleep(300)
    Jump("Function_3_3EA")

    label("loc_414")

    Return()

    # Function_3_3EA end

    def Function_4_415(): pass

    label("Function_4_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_453")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 10270, 3500, 13330, 315)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_44E")

    Jump("loc_6D0")

    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_466")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_6D0")

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_474")
    Jump("loc_6D0")

    label("loc_474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_499")
    SetChrPos(0xB, 53980, 30, 49050, 135)
    BeginChrThread(0xB, 0, 0, 3)
    Jump("loc_6D0")

    label("loc_499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4AC")
    SetChrFlags(0xE, 0x80)
    Jump("loc_6D0")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_4D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")
    SetChrFlags(0x10, 0x10)

    label("loc_4D3")

    Jump("loc_6D0")

    label("loc_4D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_50B")
    SetChrPos(0xE, -48650, 200, 4460, 270)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506")
    SetChrFlags(0x10, 0x10)

    label("loc_506")

    Jump("loc_6D0")

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_528")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_6D0")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_540")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_6D0")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_56C")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_6D0")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_57A")
    Jump("loc_6D0")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5B4")
    SetChrPos(0x8, 10280, 3500, 14670, 180)
    SetChrPos(0xA, 10270, 3500, 13330, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_6D0")

    label("loc_5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_636")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x8, 3880, 0, -500, 45)
    SetChrPos(0xA, 10270, 3500, 13330, 315)
    SetChrPos(0xB, 53980, 30, 49050, 135)
    SetChrPos(0x11, 9270, 3500, 14320, 135)
    SetChrPos(0x12, 8210, 3500, 14680, 135)
    BeginChrThread(0xB, 0, 0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_631")
    SetChrFlags(0xA, 0x10)

    label("loc_631")

    Jump("loc_6D0")

    label("loc_636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_65F")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x8, 5020, 0, -150, 315)
    Jump("loc_6D0")

    label("loc_65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_66D")
    Jump("loc_6D0")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6A0")
    SetChrPos(0xB, 51970, 0, 53350, 315)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_69B")
    SetChrFlags(0xA, 0x10)

    label("loc_69B")

    Jump("loc_6D0")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_6BF")
    SetChrPos(0xA, 10060, 3500, 14220, 180)
    Jump("loc_6D0")

    label("loc_6BF")

    SetChrPos(0xA, 10060, 3500, 14220, 180)

    label("loc_6D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F1")
    Event(0, 23)

    label("loc_6F1")

    Return()

    # Function_4_415 end

    def Function_5_6F2(): pass

    label("Function_5_6F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70B")
    OP_10(0x0, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_711")

    label("loc_70B")

    OP_10(0x0, 0x1)
    OP_10(0xD, 0x0)

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_744")

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_744")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_744")

    label("loc_744")

    ClearMapObjFlags(0x4, 0x10)
    OP_65(0x1, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76C")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_76C")

    Return()

    # Function_5_6F2 end

    def Function_6_76D(): pass

    label("Function_6_76D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_81A")

    ChrTalk(
        0xFE,
        (
            "I reckon there's only one vacant\x01",
            "apartment at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Second floor, to the left of the stairs as\x01",
            "you go up. Take a look if you're interested.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209D")

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_891")

    ChrTalk(
        0x8,
        "Hmm... What's for dinner tonight?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter what happens, you should always\x01",
            "keep yourself fed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209D")

    label("loc_891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_934")

    ChrTalk(
        0x8,
        (
            "Those delinquents have been searching\x01",
            "for their friend all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even though it's not my problem, I feel\x01",
            "for those sonny boys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1F")

    label("loc_934")


    ChrTalk(
        0x8,
        (
            "Those delinquents have been searching\x01",
            "for their friend all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, it's possible that the lad is simply out\x01",
            "somewhere relaxing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In that case, he should have notified his\x01",
            "little friends about his whereabouts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A1F")

    Jump("loc_209D")

    label("loc_A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B35")

    ChrTalk(
        0x8,
        (
            "I was minding my own gosh darn business taking\x01",
            "a walk, when I had a bit of a run-in with a delinquent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I believe that blue-haired lad was that new rookie.\x01",
            "Either way, he had a bit of a dangerous look in\x01",
            "his eyes. Scared the heck out of poor old me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209D")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BB9")

    ChrTalk(
        0x8,
        (
            "Those lads with anger issues seemed to have\x01",
            "calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Have they finally let bygones be bygones?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D38")

    label("loc_BB9")


    ChrTalk(
        0x8,
        (
            "Those lads with anger issues seemed to have\x01",
            "calmed down for the past month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's hardly any uproars, brawls, or petty\x01",
            "squabbles breaking out on the streets these\x01",
            "days. Some much-needed quiet, if I might add.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though, I suppose they have been engaging\x01",
            "each other with their mouths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You lads and lasses better be careful walking\x01",
            "through the Downtown District.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D38")

    Jump("loc_209D")

    label("loc_D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_ED0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DDA")

    ChrTalk(
        0x8,
        (
            "Polite, good-natured youths like Rixia are few\x01",
            "and far between around these parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hoho. She's a charming girl, I tell you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_DDA")


    ChrTalk(
        0x8,
        (
            "I stumbled into Rixia in the lobby this\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After exchanging pleasantries, she told me\x01",
            "she was going to hang out with her friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hoho. What a cheerful girl that Rixia is.\x01",
            "The city could use more youngsters like her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_ECB")

    Jump("loc_209D")

    label("loc_ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_100A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F7D")

    ChrTalk(
        0x8,
        (
            "I think I'll drag myself out to listen to the\x01",
            "mayor's address today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hoho. Only because I doubt many will\x01",
            "show up for the closing ceremony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1005")

    label("loc_F7D")


    ChrTalk(
        0x8,
        (
            "Now, then, I think I'll stretch my legs and\x01",
            "attend the closing ceremony later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It's become an annual tradition for myself.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1005")

    Jump("loc_209D")

    label("loc_100A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_108C")

    ChrTalk(
        0x8,
        (
            "Relaxing at home always calms me down\x01",
            "the most, even if it's a dingy apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Funny, isn't it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1134")

    label("loc_108C")


    ChrTalk(
        0x8,
        (
            "I went out to watch the parade and, boy,\x01",
            "did all that walking wear me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Relaxing at home always calms me down\x01",
            "the most, even if it's a dingy apartment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1134")

    Jump("loc_209D")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1281")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_119B")

    ChrTalk(
        0x8,
        (
            "Even us downtown folk acknowledge that\x01",
            "Mayor MacDowell is a fine man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127C")

    label("loc_119B")


    ChrTalk(
        0x8,
        "Mayor MacDowell is a fine man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Despite that incident at the theater, he kept\x01",
            "working with the diet and made certain that\x01",
            "the Anniversary Festival was safely held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Boy, let me tell you. He's a man among men.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_127C")

    Jump("loc_209D")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_132B")

    ChrTalk(
        0x8,
        (
            "I think I'll give some snacks to that sonny\x01",
            "who's always studying so hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not in my nature to abandon my fellow\x01",
            "neighbors in need.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1480")

    label("loc_132B")


    ChrTalk(
        0x8,
        (
            "Everyone here in Lotus Heights seems to\x01",
            "be enjoying themselves. Hoho, splendid.\x01",
            "That brings a smile to my face, it does.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "Hmm. Am I forgetting someone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You know what? That kid who's been\x01",
            "busy studying for his exams must be\x01",
            "feeling lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, well. It won't hurt to bring him some\x01",
            "snacks later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1480")

    Jump("loc_209D")

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_15CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_153C")

    ChrTalk(
        0x8,
        (
            "Just because I live downtown doesn't\x01",
            "mean I can't appreciate SOME luxury.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll have to scrape together whatever's\x01",
            "in my hidden savings sometime soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15CA")

    label("loc_153C")


    ChrTalk(
        0x8,
        "I thought I stashed it around here somewhere...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hoho. With the festival almost upon us,\x01",
            "I'll need to scrape together my savings.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_15CA")

    Jump("loc_209D")

    label("loc_15CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1724")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EA")
    Call(0, 12)
    Jump("loc_171F")

    label("loc_15EA")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "It honestly baffles me why a girl like Rixia\x01",
            "would want to stay in a neighborhood as\x01",
            "run-down as this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those nefarious diet members got what was\x01",
            "coming to them! After all their posturing, they\x01",
            "just turned tail and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose we owe it to that saint of a girl, too,\x01",
            "don't we?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    label("loc_171F")

    Jump("loc_209D")

    label("loc_1724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_18A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F3")

    ChrTalk(
        0xFE,
        (
            "Those diet members went to Corona's\x01",
            "apartment, didn't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're used to their incessant behavior\x01",
            "by now, so we'll get by... I do hope that\x01",
            "Corona is all right, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18A2")

    label("loc_17F3")


    ChrTalk(
        0xFE,
        (
            "There's been plans to redevelop downtown for\x01",
            "who knows how long now. Diet members tend\x01",
            "to harass us about it regularly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I only hope that Corona doesn't overdo it...\x02",
    )

    CloseMessageWindow()

    label("loc_18A2")

    Jump("loc_209D")

    label("loc_18A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1962")

    ChrTalk(
        0xFE,
        (
            "(Is it already time for these blasted\x01",
            "diet members to pester us again?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(They keep bothering us from time to time.\x01",
            "I need to figure out how to chase them away...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209D")

    label("loc_1962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_19E8")

    ChrTalk(
        0x8,
        "Nice weather we're having, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I'll head to East Street and pick\x01",
            "up some leftover grub at the market.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209D")

    label("loc_19E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1A84")

    ChrTalk(
        0x8,
        (
            "Apparently, a young lady moved into\x01",
            "one of the apartments by herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Who knows? Maybe she doesn't have\x01",
            "any relatives, like myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209D")

    label("loc_1A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B1E")

    ChrTalk(
        0x8,
        (
            "I've been living in the Downtown District going\x01",
            "on 60 years now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And despite that, I've no desire to live\x01",
            "anywhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C35")

    label("loc_1B1E")


    ChrTalk(
        0x8,
        (
            "I've been living in the Downtown District going\x01",
            "on 60 years now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. It used to be quite lively here until the\x01",
            "new business and entertainment districts\x01",
            "were built.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even though it feels as if the government has\x01",
            "forsaken this district, I've no desire to leave.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C35")

    Jump("loc_209D")

    label("loc_1C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1E2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D15")

    ChrTalk(
        0x8,
        (
            "Everyone has their own circumstances for\x01",
            "living here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, the Downtown District accepts everyone\x01",
            "with open arms. Allowing every bum into the area\x01",
            "can lead to a hostile environment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E26")

    label("loc_1D15")


    ChrTalk(
        0x8,
        "Between the jobless and the penniless, we have it all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Downtown District is home to many of those\x01",
            "rejected by society far and wide across the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We all live as one, though. Each one of us must do\x01",
            "our part in order to help one another survive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E26")

    Jump("loc_209D")

    label("loc_1E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_1F4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E91")

    ChrTalk(
        0x8,
        (
            "We're all living in the same area, so can't\x01",
            "these folks just make amends?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F47")

    label("loc_1E91")


    ChrTalk(
        0x8,
        (
            "Good grief, those whippersnappers are\x01",
            "back at it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was a lad full of energy back in my day, too, but they\x01",
            "should spend it on something more useful than fighting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F47")

    Jump("loc_209D")

    label("loc_1F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FED")

    ChrTalk(
        0x8,
        (
            "This dingy old apartment gets a draft going due\x01",
            "to how spacious it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "See? Doesn't it feel like you're enjoying\x01",
            "a nice, outdoor breeze?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209D")

    label("loc_1FED")


    ChrTalk(
        0x8,
        (
            "Oh, we sure do have a fine day on our hands.\x01",
            "An old man could get used to this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I love how fresh the air near the Lupinus River\x01",
            "feels. It's really quite pleasant!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_209D")

    TalkEnd(0xFE)
    Return()

    # Function_6_76D end

    def Function_7_20A1(): pass

    label("Function_7_20A1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2135")
    Jump("loc_217F")

    label("loc_2135")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2155")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_217F")

    label("loc_2155")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2175")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_217F")

    label("loc_2175")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_217F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2225")

    ChrTalk(
        0xD,
        "You folks interested in this fine drink?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hoho. Curious, are we? This liquor\x01",
            "is made from sweet potatoes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2228")

    label("loc_2225")

    Call(0, 8)

    label("loc_2228")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_20A1 end

    def Function_8_2230(): pass

    label("Function_8_2230")

    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xD,
        "And now we toast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It is unfortunate that the lovely\x01",
            "Rixia is unable to join us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She's co-starring in Arc en Ciel's new play, right?\x01",
            "Isn't that kind of a huge deal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I had no idea she was that popular. Our interactions\x01",
            "have been so tame this entire time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_8_2230 end

    def Function_9_235D(): pass

    label("Function_9_235D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2538")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2468")

    ChrTalk(
        0x9,
        (
            "At any rate, Rixia's been working harder than\x01",
            "I would have guessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This'll serve as motivation to get my life in order\x01",
            "and make my big comeback!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, enough of a comeback that I can buy a ticket\x01",
            "to her show and support her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2533")

    label("loc_2468")


    ChrTalk(
        0x9,
        (
            "Rixia stormed out of her room sometime around noon.\x01",
            "She looked like she was in a bit of a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think she might have been late for the daytime\x01",
            "performance. You think she made it on time?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2533")

    Jump("loc_398E")

    label("loc_2538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2679")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25C4")

    ChrTalk(
        0x9,
        (
            "Yeeeep. I sure love reading about business.\x01",
            "I'd like to become a merchant again...if I can\x01",
            "get my act together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2674")

    label("loc_25C4")


    ChrTalk(
        0x9,
        "I picked up a business magazine at the store today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heh. Saw Mariabell Crois featured in the top story in\x01",
            "this issue, so I figured it'd be worth giving it a read.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2674")

    Jump("loc_398E")

    label("loc_2679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_27D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26EC")

    ChrTalk(
        0x9,
        (
            "Hmm. I think I'll take my first trip out to the department\x01",
            "store in a long, long time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27CE")

    label("loc_26EC")


    ChrTalk(
        0x9,
        (
            "Oh, yeah. Don't they usually publish the newest\x01",
            "issue for that business magazine today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I used to subscribe to it a long time ago,\x01",
            "but...my business has long since folded.\x01",
            "I'm in complete shambles, so why bother?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_27CE")

    Jump("loc_398E")

    label("loc_27D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_293D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2868")

    ChrTalk(
        0x9,
        (
            "I just recently became closely acquainted\x01",
            "with Michaud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm pretty worried about him.\x01",
            "What if he ruined his health?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2938")

    label("loc_2868")


    ChrTalk(
        0x9,
        (
            "I won't be able to talk to my neighbor Michaud today\x01",
            "'cause he's heading to St. Ursula for a checkup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's been studying his butt off, so I imagine\x01",
            "the strain isn't doing wonders for his health.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2938")

    Jump("loc_398E")

    label("loc_293D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_29F6")

    ChrTalk(
        0x9,
        (
            "While I don't think this is necessarily the worst place\x01",
            "to live, it's certainly difficult for children to handle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Can't you guys do something about it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAD")

    label("loc_29F6")


    ChrTalk(
        0x9,
        (
            "Huh...? What's a kid doing straying off\x01",
            "into the Downtown District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Not good, guys. Not good at all.\x02\x03",
            "You should probably take her to\x01",
            "the guild or the cathedral, pronto.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2AAD")

    Jump("loc_398E")

    label("loc_2AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2CA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B68")

    ChrTalk(
        0x9,
        (
            "Those guys were making one heck of a ruckus.\x01",
            "Oddly enough, it was kind of refreshing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I was feeding off of their energy, and now I feel rejuvenated.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C9F")

    label("loc_2B68")


    ChrTalk(
        0x9,
        (
            "We had all gathered together to enjoy some hotpot\x01",
            "when, all of a sudden, those delinquents broke out\x01",
            "into an intense race.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That race was so close! They totally had\x01",
            "me white-knuckling toward the end!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. I definitely enjoyed that more than I\x01",
            "should have! I'm a sucker for that kind of stuff.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C9F")

    Jump("loc_398E")

    label("loc_2CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2E18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D46")

    ChrTalk(
        0x9,
        (
            "Anyway, this is my first Anniversary Festival since\x01",
            "moving to the Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I wonder how I'll celebrate it this year...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E13")

    label("loc_2D46")


    ChrTalk(
        0x9,
        "Hmm... How should I celebrate it this year?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Old Man Tantz invited me over to enjoy some\x01",
            "hotpot with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You know, when I think about our financial\x01",
            "situations, it doesn't sound half bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E13")

    Jump("loc_398E")

    label("loc_2E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2EB9")

    ChrTalk(
        0x9,
        (
            "All I used to do was trade stock, well, up until\x01",
            "I lost it all, that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Tantz is far more honest than I could ever\x01",
            "hope to be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F89")

    label("loc_2EB9")


    ChrTalk(
        0x9,
        "I have to admit, Tantz is a caring old man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I definitely had a negative perception of anyone\x01",
            "raised here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've seen the error of my ways, though. He's twice\x01",
            "the man I could ever hope to be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2F89")

    Jump("loc_398E")

    label("loc_2F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_30AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3021")

    ChrTalk(
        0x9,
        (
            "Living downtown has truly opened my eyes\x01",
            "to the deceit of our government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "They need to be cast off their thrones.\x02",
    )

    CloseMessageWindow()
    Jump("loc_30A5")

    label("loc_3021")


    ChrTalk(
        0x9,
        (
            "Our politicians talk a big game, but their\x01",
            "actions never follow suit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "They're too scared to approach a dump like this.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_30A5")

    Jump("loc_398E")

    label("loc_30AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_331A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3187")

    ChrTalk(
        0x9,
        (
            "How many years has it been since I last saw Harold?\x01",
            "I've lost everything, yet he still talked to me\x01",
            "like we just saw each other yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hahaha... I was almost moved to tears, honestly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_3187")


    ChrTalk(
        0x9,
        (
            "I met up with an old business acquaintance of\x01",
            "mine by the name of Harold yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I remember when people used to make fun of him\x01",
            "for being a timid, short man back in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's been a long time since we last saw each other,\x01",
            "but he was still the same carefree guy I knew.\x01",
            "We ended up drinking together for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hahaha... I was almost moved to tears, honestly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3315")

    Jump("loc_398E")

    label("loc_331A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_349E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_33C3")

    ChrTalk(
        0x9,
        (
            "I almost had a bit of a close call with those\x01",
            "delinquents earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*shudder* Why could they possibly have\x01",
            "been lying in wait like that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3499")

    label("loc_33C3")


    ChrTalk(
        0x9,
        (
            "I almost had a bit of a close call with those\x01",
            "delinquents earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*shudder* This is why I hate\x01",
            "lawless neighborhoods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The real question is, why were they lying in\x01",
            "wait in front of the apartment?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3499")

    Jump("loc_398E")

    label("loc_349E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3643")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_355E")

    ChrTalk(
        0x9,
        (
            "I may be in shambles, but that won't stop me from\x01",
            "indulging in the occasional business magazine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hahaha... I know it's shameful,\x01",
            "but I just can't help myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_363E")

    label("loc_355E")


    ChrTalk(
        0x9,
        "Hmm... This week's stock prices, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I know it's shameful of me to do this, but I still\x01",
            "indulge in the occasional business magazine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I can't seem to shake some of the habits\x01",
            "I had from my days as a trader.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_363E")

    Jump("loc_398E")

    label("loc_3643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3736")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_36C2")

    ChrTalk(
        0x9,
        "You know, I used to be a trader...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As you can now see, I am completely\x01",
            "in shambles. Hahaha...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3731")

    label("loc_36C2")


    ChrTalk(
        0x9,
        "The rent for this apartment is really cheap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even a bum like me can manage to\x01",
            "afford living here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3731")

    Jump("loc_398E")

    label("loc_3736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3795")

    ChrTalk(
        0x9,
        (
            "Damn it... How could someone like myself\x01",
            "be stuck living downtown?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3804")

    label("loc_3795")


    ChrTalk(
        0x9,
        "I-I used to be a well-renowned trader.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't lump me in with the rest of the crazies\x01",
            "living here!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3804")

    Jump("loc_398E")

    label("loc_3809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_384E")

    ChrTalk(
        0x9,
        (
            "What's with all the ruckus? Did something\x01",
            "happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_398E")

    label("loc_384E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_38AF")

    ChrTalk(
        0x9,
        (
            "Goddamn it...\x01",
            "Why'd it have to be like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It's not like I screwed up!\x02",
    )

    CloseMessageWindow()
    Jump("loc_398E")

    label("loc_38AF")


    ChrTalk(
        0x9,
        (
            "Goddamn it...\x01",
            "Why'd it have to be like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Those stocks were supposed to be safe!\x01",
            "It's not like I screwed up!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "Wh-Who are you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Are you friends with those delinquents?\x01",
            "Get lost!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_398E")

    TalkEnd(0xFE)
    Return()

    # Function_9_235D end

    def Function_10_3992(): pass

    label("Function_10_3992")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A26")
    Jump("loc_3A70")

    label("loc_3A26")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A46")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A70")

    label("loc_3A46")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A66")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A70")

    label("loc_3A66")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A70")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3B5A")

    ChrTalk(
        0xF,
        (
            "I don't have any mira to waste fooling around.\x01",
            "I'll spend it wisely by buying hotpot to celebrate\x01",
            "with me and the other tenants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I have to admit, Tantz is a caring old man.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B5D")

    label("loc_3B5A")

    Call(0, 8)

    label("loc_3B5D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_3992 end

    def Function_11_3B65(): pass

    label("Function_11_3B65")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BF9")
    Jump("loc_3C43")

    label("loc_3BF9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C19")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C43")

    label("loc_3C19")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C39")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C43")

    label("loc_3C39")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C43")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3CDE")

    ChrTalk(
        0xE,
        (
            "I can't do anything about this evening sleepiness...\x01",
            "Damn it. I've gotta get it together!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D78")

    label("loc_3CDE")

    SetChrSubChip(0xE, 0x0)

    ChrTalk(
        0xE,
        "Zzz... Zzz...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "Wh-Whoa, crap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm pretty sure this time of the day is cursed!\x01",
            "Why else would I always doze off?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3D78")

    Jump("loc_542B")

    label("loc_3D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3EAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3E00")

    ChrTalk(
        0xE,
        "I absolutely have to pass the exam this year.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Those goons better not distract me\x01",
            "from my studies!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAA")

    label("loc_3E00")


    ChrTalk(
        0xE,
        "Huh. Those goons have been oddly quiet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, whatever. Less distractions for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As long as my study sessions aren't being\x01",
            "interrupted, it's all good!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3EAA")

    Jump("loc_542B")

    label("loc_3EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3F7A")

    ChrTalk(
        0xE,
        (
            "My doctor and I had a long discussion when I\x01",
            "went to St. Ursula Medical College yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What a valuable experience that was.\x01",
            "Now I'm even more motivated to get\x01",
            "accepted there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542B")

    label("loc_3F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4052")

    ChrTalk(
        0xE,
        (
            "I managed to get a perfect score on the practice exam.\x01",
            "I have a solid eighty percent chance of getting in\x01",
            "if I keep up with my studies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Just have to keep at it and continue grinding!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4112")

    label("loc_4052")

    SetChrSubChip(0xE, 0x0)

    ChrTalk(
        0xE,
        (
            "And now, a toast! To my success\x01",
            "on the practice exam!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "*munch* *munch* *chew*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As long as I keep grinding through my studies\x01",
            "until the real deal, I've got this in the bag!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4112")

    Jump("loc_542B")

    label("loc_4117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4194")

    ChrTalk(
        0xE,
        (
            "Can't you guys cut it out already?! Is it too much\x01",
            "to ask for peace and quiet for just ONE day?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4230")

    label("loc_4194")


    ChrTalk(
        0xE,
        "What's with all the noise outside?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please, stop...\x01",
            "I have to take the practice entrance exam for\x01",
            "St. Ursula tomorrow. I can't deal with this!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4230")

    Jump("loc_542B")

    label("loc_4235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_437D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_42C0")

    ChrTalk(
        0xE,
        (
            "Just two more days till the practice exam... I'm not\x01",
            "going to cut corners just 'cause it's not the real thing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4378")

    label("loc_42C0")


    ChrTalk(
        0xE,
        (
            "I got swept into the crowd trying to\x01",
            "grab myself some lunch today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I barely managed to get out of there in one piece.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hurray. What a colossal waste of time that was.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4378")

    Jump("loc_542B")

    label("loc_437D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4473")

    ChrTalk(
        0xE,
        (
            "Old Man Tantz offered me some grilled fish\x01",
            "while I was studying yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm appreciative, because it supposedly\x01",
            "improves your memory!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha...hahaha... This secret weapon is\x01",
            "going to bolster my memorization skills!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542B")

    label("loc_4473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4608")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_454D")

    ChrTalk(
        0xE,
        (
            "I'll use the results of the practice exams to figure\x01",
            "out what my chances for getting into college are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I-I think I'll be too shocked to bother continuing\x01",
            "if I score poorly on the exam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4603")

    label("loc_454D")


    ChrTalk(
        0xE,
        "Ugh. Those obnoxious goons...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I couldn't get any studying in yesterday!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "This is bad. Real bad! The practice exam is\x01",
            "basically right after the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4603")

    Jump("loc_542B")

    label("loc_4608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_46F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4681")

    ChrTalk(
        0xE,
        "Damn you all and your festivities...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I wanna go out and have some fun, too...\x01",
            "*grumble*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46EB")

    label("loc_4681")


    ChrTalk(
        0xE,
        "Students like myself don't get to enjoy breaks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Do you have any idea what I'm going through?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_46EB")

    Jump("loc_542B")

    label("loc_46F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_485C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4780")

    ChrTalk(
        0xE,
        (
            "Sh-Shoot... I keep dozing off every time I try\x01",
            "to memorize something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Man, my memorization skills are garbage.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4857")

    label("loc_4780")

    SetChrSubChip(0xE, 0x0)

    ChrTalk(
        0xE,
        "Zzz... Zzz...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "Wh-Whoa, crap! I fell asleep\x01",
            "without realizing it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can't even afford to lose a half hour!\x01",
            "Don't even think about falling asleep\x01",
            "mid-studying, Michaud!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_4857")

    Jump("loc_542B")

    label("loc_485C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_490F")

    ChrTalk(
        0xE,
        (
            "While St. Ursula may be a medical college,\x01",
            "they still administer general education exams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Gee, there sure are a lot of things I need to memorize!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A28")

    label("loc_490F")


    ChrTalk(
        0xE,
        (
            "So, Giliath Osborne is the Erebonian Empire's chancellor\x01",
            "and rose through the ranks of the military...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "His main achievement so far is the expansion of\x01",
            "the railway network through the entire nation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "He then declared his 'Blood and Iron Policy...'\x01",
            "Uh. Excuse me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4A28")

    Jump("loc_542B")

    label("loc_4A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4B5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4A73")

    ChrTalk(
        0xE,
        "Please don't distract me from my studies.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B56")

    label("loc_4A73")


    ChrTalk(
        0xE,
        (
            "One of those government officials came by to\x01",
            "check up on my residency registration...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The heck? Isn't it obvious that I have\x01",
            "a registration? I'm no criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I wonder what prompted him to come\x01",
            "check up on me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4B56")

    Jump("loc_542B")

    label("loc_4B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4D9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4C30")

    ChrTalk(
        0xE,
        (
            "St. Ursula's practice entrance exam is\x01",
            "right after the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm going to try my hardest on it this time around.\x01",
            "Once that's over with, I'll take on the real exam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D98")

    label("loc_4C30")


    ChrTalk(
        0xE,
        (
            "St. Ursula's practice entrance exam is\x01",
            "right after the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Passing it will help boost my confidence.\x01",
            "I know I can trust in my own abilities to\x01",
            "get me through the real exam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I made the mistake of not taking the practice\x01",
            "exam last year. I sure made a fool of myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I promised myself I wouldn't repeat the same mistake.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4D98")

    Jump("loc_542B")

    label("loc_4D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4F71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC4")

    ChrTalk(
        0xFE,
        (
            "Those goons have set their sights on the girl\x01",
            "living above me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't blame them, though. Who wouldn't fall for a\x01",
            "total cutie who happily greets them everyday?\x01",
            "She's so lovely... ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xFE,
        (
            "No! Stop, Michaud! Rid yourself\x01",
            "of earthly desires!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4F6C")

    label("loc_4EC4")


    ChrTalk(
        0xFE,
        (
            "*sigh* I need to purge these useless thoughts\x01",
            "and concentrate on studying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those goons get to live the good life.\x01",
            "They've got all the free time in the world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F6C")

    Jump("loc_542B")

    label("loc_4F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5044")

    ChrTalk(
        0xE,
        (
            "It's difficult being a student like myself.\x01",
            "I don't get any free time, and my only\x01",
            "source of income is my allowance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*gulp* What am I going to do?\x01",
            "This month is looking tight...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_5044")


    ChrTalk(
        0xE,
        (
            "Ugh. This reference book is ruthless!\x01",
            "How hard can this thing get?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I want to buy a book that's easier to understand,\x01",
            "but I'm strapped for mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*gulp* What am I going to do?\x01",
            "This month is looking tight...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5123")

    Jump("loc_542B")

    label("loc_5128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5167")

    ChrTalk(
        0xE,
        "I have to pass the exam next year.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5214")

    label("loc_5167")


    ChrTalk(
        0xE,
        (
            "I came here from the countryside hoping to\x01",
            "get admitted into St. Ursula Medical College.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I failed this year's exam, as well...\x01",
            "Guess I'm retaking it next year.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5214")

    Jump("loc_542B")

    label("loc_5219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_52CC")

    ChrTalk(
        0xE,
        (
            "Will those goons EVER get tired\x01",
            "of fighting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "It'd be fantastic if they did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'd finally get the peace and quiet needed\x01",
            "to study for this damned exam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542B")

    label("loc_52CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_530D")

    ChrTalk(
        0xE,
        "Huh? Is it just me, or did it get more quiet?\x02",
    )

    CloseMessageWindow()
    Jump("loc_542B")

    label("loc_530D")


    ChrTalk(
        0xE,
        (
            "There are two different groups of goons around here.\x01",
            "One of them is known as the Testaments, while the\x01",
            "other one calls themselves the Saber Vipers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "They're the noisiest people I've ever had the\x01",
            "displeasure of knowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What am I going to do if I fail the exam\x01",
            "yet again?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_542B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_3B65 end

    def Function_12_5433(): pass

    label("Function_12_5433")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5548")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_54C2")

    ChrTalk(
        0xA,
        (
            "We haven't had a chance to enjoy a meal\x01",
            "together for far too long. I feel much\x01",
            "happier on these rare occasions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5543")

    label("loc_54C2")


    ChrTalk(
        0xA,
        "Looks like my husband just got home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, thank Aidios. We'll be able to happily\x01",
            "enjoy our meal as a family tonight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5543")

    Jump("loc_6A6E")

    label("loc_5548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5609")

    ChrTalk(
        0xA,
        (
            "They adjusted the construction schedule for today,\x01",
            "so my husband might be coming home early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "He just called me to tell me about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "This calls for a feast tonight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A6E")

    label("loc_5609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_571C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5675")

    ChrTalk(
        0xA,
        (
            "Rixia's job is difficult, yet she manages to\x01",
            "get up bright and early every day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5717")

    label("loc_5675")


    ChrTalk(
        0xA,
        (
            "Rixia appeared to have left the apartment\x01",
            "ridiculously early this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think she may have woken up two or three\x01",
            "hours before my husband, even.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5717")

    Jump("loc_6A6E")

    label("loc_571C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_58C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_57C5")

    ChrTalk(
        0xA,
        (
            "It doesn't sound like they've gotten much\x01",
            "work done at the construction site lately.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFF)

    ChrTalk(
        0xA,
        "In that case, why don't they give him time off?\x02",
    )

    CloseMessageWindow()
    Jump("loc_58C4")

    label("loc_57C5")


    ChrTalk(
        0xA,
        (
            "They've halted construction for the duration\x01",
            "of the diet sessions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They're waiting to see if their budget is\x01",
            "approved before resuming progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "My husband's been spending so much time at\x01",
            "the construction site that I hardly ever see him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_58C4")

    Jump("loc_6A6E")

    label("loc_58C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_59C1")

    ChrTalk(
        0xA,
        (
            "My husband was given time off for the Anniversary\x01",
            "Festival, but his job is still going to be just as busy\x01",
            "when he goes back to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think Lima would be a lot happier if he was\x01",
            "given a few extra vacation days, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A6E")

    label("loc_59C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5B0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5A71")

    ChrTalk(
        0xA,
        (
            "My husband hasn't taken a day off in quite some time.\x01",
            "Now we can enjoy the festival together as a family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm looking forward to it, actually.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B08")

    label("loc_5A71")


    ChrTalk(
        0xA,
        "Lima's already ecstatic for the festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "My husband hasn't taken a day off\x01",
            "in quite some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm looking forward to it, actually.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5B08")

    Jump("loc_6A6E")

    label("loc_5B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF9")
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0xA, 0x0, 0)
    TurnDirection(0x8, 0x0, 0)

    ChrTalk(
        0xA,
        (
            "Some diet members came to visit our apartment\x01",
            "today and behaved very rudely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Poor Rixia walked by in the middle of\x01",
            "their verbal onslaught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She gave her signature energetic greeting,\x01",
            "and their jaws dropped. They were utterly\x01",
            "speechless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, yes! They were wearing an amusing\x01",
            "flabbergasted look on their faces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was surprised to find out that Rixia\x01",
            "was a member of Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "At least they stopped their verbal abuse\x01",
            "and left us alone for the rest of the day.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Those bickering diet members tucked their tails\x01",
            "between their legs and ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hahaha. That was most amusing!\x01",
            "That lovely girl's smile saved our behinds.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_5EDE")

    label("loc_5DF9")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "Those diet members come and harass us\x01",
            "every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think we'll manage as long as we've got\x01",
            "Rixia on our side, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to bring her some food later as a\x01",
            "token of my appreciation.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)

    label("loc_5EDE")

    Jump("loc_6A6E")

    label("loc_5EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6153")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60C8")
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Residence permit...\x01",
            "Residency registration...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Excuse me, but I've been living in Crossbell for\x01",
            "five years already. I'm not sure why you're\x01",
            "asking for them now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Oh? Not being able to produce the proper\x01",
            "documentation will spell trouble for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "In accordance with state law, we will have to\x01",
            "issue an order to evict you. Unless...you plan\x01",
            "to leave of your own volition.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh, no... What am I supposed to do?\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_614E")

    label("loc_60C8")

    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xFE,
        "This doesn't look good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I can't get those permits submitted,\x01",
            "I might be evicted for illegal residency...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x13B, 0x0)

    label("loc_614E")

    Jump("loc_6A6E")

    label("loc_6153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_621A")

    ChrTalk(
        0xA,
        (
            "The girl living next door seems a little\x01",
            "down these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't want to pry into someone else's\x01",
            "life, but I can't help worrying about a girl\x01",
            "so young living alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6301")

    label("loc_621A")


    ChrTalk(
        0xA,
        (
            "The girl living next door is usually\x01",
            "bright and energetic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She's been nothing but a sweetheart\x01",
            "to Lima, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Still, I get the impression that she\x01",
            "feels a little down these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "What worries are on her mind?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_6301")

    Jump("loc_6A6E")

    label("loc_6306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_648E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_63DB")

    ChrTalk(
        0xA,
        "Lima loves her father a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Sadly for her, my husband works construction,\x01",
            "so he's hardly ever home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You know, I never really noticed when\x01",
            "she became Daddy's little princess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6489")

    label("loc_63DB")


    ChrTalk(
        0xA,
        "Oh, my dear Lima is being so unreasonable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I absolutely have to take an afternoon nap.\x01",
            "I'm completely spent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Not before I finish doing the laundry, though.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_6489")

    Jump("loc_6A6E")

    label("loc_648E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6680")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6564")

    ChrTalk(
        0xA,
        (
            "The cheap rent here allows us to earn\x01",
            "a decent living.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, if they decide to tear this place down\x01",
            "and replace it with luxury highrises, then we'll\x01",
            "have no choice but to leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667B")

    label("loc_6564")


    ChrTalk(
        0xA,
        "One of the diet members came by earlier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There were mentions of demolishing the Downtown\x01",
            "District in order to redevelop it, I think.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "The Downtown District will cease to exist, won't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "If that happens, then we'll have to move...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_667B")

    Jump("loc_6A6E")

    label("loc_6680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6700")

    ChrTalk(
        0xA,
        (
            "I can't help but worry about a young girl\x01",
            "living on her own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "We have to help take care of her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6783")

    label("loc_6700")


    ChrTalk(
        0xA,
        (
            "We recently had a young girl move in\x01",
            "next door to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To my surprise, I found out that she\x01",
            "was living all by herself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_6783")

    Jump("loc_6A6E")

    label("loc_6788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6887")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_67F0")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        "Hold your horses, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm making a delicious stew right now!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_6882")

    label("loc_67F0")


    ChrTalk(
        0xA,
        (
            "It's all thanks to my husband's hard work\x01",
            "that I can cook warm meals for my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm grateful for everything he does.\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 3)

    label("loc_6882")

    Jump("loc_6A6E")

    label("loc_6887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_69C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_68F5")

    ChrTalk(
        0xA,
        (
            "The utter lack of police intervention is\x01",
            "one of the biggest flaws of living here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69C0")

    label("loc_68F5")


    ChrTalk(
        0xA,
        (
            "The utter lack of police intervention is\x01",
            "one of the biggest flaws of living here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, but don't get me wrong.\x01",
            "We don't intend to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "And besides, we wouldn't have any place to go...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_69C0")

    Jump("loc_6A6E")

    label("loc_69C5")


    ChrTalk(
        0xA,
        (
            "My daughter ran out the door looking\x01",
            "very excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh* I'm a bit of a worrywart, so I have to occasionally\x01",
            "leave the cooking unattended to check up on her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A6E")

    TalkEnd(0xFE)
    Return()

    # Function_12_5433 end

    def Function_13_6A72(): pass

    label("Function_13_6A72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6B04")
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "Daddy came home early today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yaaay! We're going to play together\x01",
            "lots and lots today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B07")

    label("loc_6B04")

    Call(0, 14)

    label("loc_6B07")

    Jump("loc_772A")

    label("loc_6B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6BB9")

    ChrTalk(
        0xB,
        (
            "Heeey! Daddy might be coming\x01",
            "home early today.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "Yay! You think he'll really come?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "What time is Daddy going to get here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_772A")

    label("loc_6BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6C1E")

    ChrTalk(
        0xB,
        "I need to pick up the garbage!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm going to make the house sparkle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CAA")

    label("loc_6C1E")


    ChrTalk(
        0xB,
        (
            "Mommy told me that if I help her with chores,\x01",
            "Daddy might come home sooner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm going to try sooooooo hard to\x01",
            "clean the house!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6CAA")

    Jump("loc_772A")

    label("loc_6CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6D56")

    ChrTalk(
        0xB,
        (
            "Hey, did you guys see Rixia\x01",
            "leave earlier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Eheheh. She gave me a nice pat on\x01",
            "the head like she always does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "She always makes me so happy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_772A")

    label("loc_6D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6E4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6D8C")

    ChrTalk(
        0xB,
        "When's Daddy coming home?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E46")

    label("loc_6D8C")


    ChrTalk(
        0xB,
        (
            "Daddy said he finished working\x01",
            "on his building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But then he said they're already making\x01",
            "the next one.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "When the heck's Daddy going to come home?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6E46")

    Jump("loc_772A")

    label("loc_6E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6F54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6EC3")

    ChrTalk(
        0xB,
        "Daddy said he gets to take a vacation!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yaaaay! Now we can go to the festival\x01",
            "together!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F4F")

    label("loc_6EC3")


    ChrTalk(
        0xB,
        "Hey! Did you hear?! Did you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Daddy said he gets to take a vacation!\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "Yaaay! I love Daddy so much!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6F4F")

    Jump("loc_772A")

    label("loc_6F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6FE0")

    ChrTalk(
        0xB,
        "Rixia is always very nice to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't really get what kind of job\x01",
            "jumping around in the air is, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_708D")

    label("loc_6FE0")


    ChrTalk(
        0xB,
        (
            "Rixia's a super nice lady that lives\x01",
            "right beside us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She told me that her job is to\x01",
            "jump around in the air...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She looked super happy when\x01",
            "she left today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_708D")

    Jump("loc_772A")

    label("loc_7092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_70DE")

    ChrTalk(
        0xB,
        "Mommy told me I have to stay inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "What happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_772A")

    label("loc_70DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_71A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7117")

    ChrTalk(
        0xB,
        "I want to see Daddy again...\x02",
    )

    CloseMessageWindow()
    Jump("loc_719C")

    label("loc_7117")


    ChrTalk(
        0xB,
        (
            "Daddy says he's too busy with\x01",
            "work lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I don't get to see him at night anymore...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Waaahhhh... I'm so lonely...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_719C")

    Jump("loc_772A")

    label("loc_71A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_731A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7234")

    ChrTalk(
        0xB,
        (
            "I tried so hard to stay up late last night,\x01",
            "but I barely got to talk before I fell asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*yawn*\x01",
            "Sorry, Daddy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7315")

    label("loc_7234")


    ChrTalk(
        0xB,
        (
            "*yawn*\x01",
            "I'm getting sooo sleepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I tried my hardest to stay awake and wait for\x01",
            "Daddy to come home yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But I fell asleep as soon as he gave\x01",
            "me a great, big hug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I didn't get to talk to him much...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7315")

    Jump("loc_772A")

    label("loc_731A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7381")

    ChrTalk(
        0xB,
        "I don't get to see Daddy a lot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Will Daddy come home early tonight?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7462")

    label("loc_7381")


    ChrTalk(
        0xB,
        "Daddy's at work every day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He works in construction, so he leaves\x01",
            "early in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When he gets home at night,\x01",
            "I'm already asleep.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "I don't get to see Daddy a lot anymore...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7462")

    Jump("loc_772A")

    label("loc_7467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_74CF")

    ChrTalk(
        0xB,
        "That girl was really nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Eheheh. She gave me a nice pat on the head.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7542")

    label("loc_74CF")


    ChrTalk(
        0xB,
        "Heeey! I met a new girl yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She moved in next to us\x01",
            "and gave me a really nice\x01",
            "pat on the head.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7542")

    Jump("loc_772A")

    label("loc_7547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_75FE")

    ChrTalk(
        0xB,
        "Mmmm! That smells good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Doesn't that smell great?!\x01",
            "It's making me hungry!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "I want Daddy to eat with us.\x01",
            "I hope he comes home soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_772A")

    label("loc_75FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_7650")

    ChrTalk(
        0xB,
        "La la la, laaaaa... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Is Daddy coming home late tonight?\x02",
    )

    CloseMessageWindow()
    Jump("loc_772A")

    label("loc_7650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_76BA")

    ChrTalk(
        0xB,
        "I'm going to wait for Daddy to come home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Maybe Daddy's coming home late tonight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_772A")

    label("loc_76BA")


    ChrTalk(
        0xB,
        "Daddy works at a construction site.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "When's Daddy coming home tonight?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Is he coming home late?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_772A")

    TalkEnd(0xFE)
    Return()

    # Function_13_6A72 end

    def Function_14_772E(): pass

    label("Function_14_772E")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_63(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "Yaaaay! Welcome home, Daddy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm home, Lima. Sorry, did I make\x01",
            "you wait for me?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_14_772E end

    def Function_15_77BE(): pass

    label("Function_15_77BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_787F")

    ChrTalk(
        0xC,
        (
            "A lot of circumstances led to me being able\x01",
            "to come home earlier than usual today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And thanks to that, I get to enjoy a warm meal\x01",
            "with my family for once in my life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7882")

    label("loc_787F")

    Call(0, 14)

    label("loc_7882")

    TalkEnd(0xFE)
    Return()

    # Function_15_77BE end

    def Function_16_7886(): pass

    label("Function_16_7886")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_78FC")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Zat's ta' good shuff... Vaan! Bring me\x01",
            "summore booze. And no shnacks!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_78FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_79A7")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Ouchie... Where'd da' bed go? *hic*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Boooooooze... Whoops, the dam'sh\x01",
            "'boutta break. Gotta pee. Gotta pee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Bottom's up. *glug* *glug*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_79A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7A1C")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Ahhh, zat'sh ta' shtuff. When I die, lemme\x01",
            "go wisth a cold one in hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_7A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7B65")
    Call(0, 17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7A97")

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug* Hey, you! I ain't gonna letchu\x01",
            "off ta' hook so eashily next time, eh? *hic*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B60")

    label("loc_7A97")


    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug* Croshy-crosh Croshbell Shitty.\x01",
            "Heh...heheheh... Shitty. *glug* *glug*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Wh-What the...? Who the hell stole my drink?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "It's gone! And I didn't drink any yet, either!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7B60")

    Jump("loc_8333")

    label("loc_7B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7C31")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug* D'ya really think I'd go see ta'\x01",
            "doc if I had cash? Why would ya if it'sh not\x01",
            "an emer...emergeenshy. BOOZE MONEY!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Heh. Heheh. Zat'sh jusht ta' kinda guy I am.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_7C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7CAD")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Whoaaa... Da' heck'sh dat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Why'sh the rain sho many diff'rent\x01",
            "colorsh? It'sh kinda pretty...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_7CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7D01")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug* More... I need mooooore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_7D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7D45")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "No 'riendsh, only alcobaul...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Achoo!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_7D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7DA0")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Time for anodder piss break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Hmmm... Where'sh ta' baffroom?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_7DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7E07")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Jusht one more round. Preddy pleeeash?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug* Tayshtie... *burp*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_7E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7ED4")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "I went an' left me job. Rather booze it up,\x01",
            "y'know? *hic*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Huh? When'd dish go all empty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Vaan! Vaaaaan, I need yooooou! Crack\x01",
            "open zat hollat of yoursh and buy drink!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_7ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7F42")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Hey, you shuddup. Can'tcha see I'm tryna'\x01",
            "drink in peashe? *hic*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_7F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7FC0")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug* So good... *burp*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Vaan? Vaaaaan! Where'd ya go, buddy?!\x01",
            "Got a drink for me yet?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_7FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_801A")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Life? More like...mmmmm, booze. *hic*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*buuuuurp* ...Heheh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_801A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_807E")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*hic* The hell? Am I...gettin' sober?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Booze... I NEED summore booze!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_807E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_80C6")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Alcohol is...all I need...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_80C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8128")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Shud ta' hell up, Vaan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Shtop yelling! Ish too loud!\x01",
            "*glug* *glug*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_8128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_81CA")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Vaan, gimme 'nother drink!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug* Mmmmm...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81C5")

    ChrTalk(
        0x101,
        (
            "#0003F(This apartment sure doesn't seem to\x01",
            "be vacant.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81C5")

    Jump("loc_8333")

    label("loc_81CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_8277")
    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Huh? Who ta' hell is...? Ugh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug* ...Drink good.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8272")

    ChrTalk(
        0x101,
        (
            "#0003F(This apartment sure doesn't seem to\x01",
            "be vacant.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8272")

    Jump("loc_8333")

    label("loc_8277")

    Call(0, 17)

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "*glug* *glug* *glug* *glug*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "Booze! I need moreee! Gimme more\x01",
            "or I'll go bejerk, I shware!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8333")

    ChrTalk(
        0x101,
        (
            "#0003F(This apartment sure doesn't seem to\x01",
            "be vacant.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8333")

    TalkEnd(0x13)
    Return()

    # Function_16_7886 end

    def Function_17_8337(): pass

    label("Function_17_8337")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is shut tight. A voice\x01",
            "can be heard inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Return()

    # Function_17_8337 end

    def Function_18_8379(): pass

    label("Function_18_8379")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_841D")

    ChrTalk(
        0xFE,
        (
            "The people living in this apartment are\x01",
            "far more resilient than I anticipated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. No matter. I'll drive these\x01",
            "cretins out eventually.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8507")

    label("loc_841D")

    OP_93(0xFE, 0x87, 0x0)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "I think I'll examine your residency registrations.\x01",
            "It'd be a shame if you were an illegal occupant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha... Don't tell me you're\x01",
            "unregistered?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Of course I'm not. I've been living here\x01",
            "for sixty years.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 7)

    label("loc_8507")

    TalkEnd(0xFE)
    Return()

    # Function_18_8379 end

    def Function_19_850B(): pass

    label("Function_19_850B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_85F5")

    ChrTalk(
        0xFE,
        (
            "Once the redevelopment plans have been\x01",
            "finalized, there'll be a nice bidding war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha... Massive amounts of mira will move yet again.\x01",
            "We must strike a deal before the Republican Faction\x01",
            "makes their move.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A4")

    label("loc_85F5")


    ChrTalk(
        0xFE,
        (
            "Any resident around these parts\x01",
            "always has one or two things\x01",
            "they'd like to keep in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha... Even these people can contribute\x01",
            "to Crossbell's development.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86A4")

    TalkEnd(0xFE)
    Return()

    # Function_19_850B end

    def Function_20_86A8(): pass

    label("Function_20_86A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_87A5")

    ChrTalk(
        0x10,
        (
            "#1808FI think Ilya and the troupe leader may have\x01",
            "finished revising the script.\x02\x03",
            "#1802FI need to head back as soon as possible\x01",
            "and participate in the rehearsal.\x02\x03",
            "I'll leave Nikolai's investigation in your\x01",
            "hands, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B04")

    label("loc_87A5")


    ChrTalk(
        0x101,
        (
            "#0005FOh, Rixia? What are you doing here?\x02\x03",
            "#0001FIsn't it almost time for the show to start?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1805FOh. Um...\x02\x03",
            "#1800FThe daytime performance is being held\x01",
            "a little later than planned, so I came back\x01",
            "to grab something I forgot.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10)

    ChrTalk(
        0x10,
        "#1808FRegarding Nikolai...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FYeah, we've been searching\x01",
            "everywhere for him.\x02\x03",
            "#0001FWe haven't found any clues regarding\x01",
            "his whereabouts, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYep, we're just tryin' to get our hands\x01",
            "on some clues for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1806FI see...\x02\x03",
            "#1801FSorry, everyone. I'll have to leave Nikolai's\x01",
            "investigation in your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FOf course. You can rely on us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204FThe Special Support Section are the ones\x01",
            "who successfully prevented the mayor's\x01",
            "assassination, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#0601F(Grr...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1809FIndeed you did.\x02\x03",
            "#1804F*bow*... Good luck with your work,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_8B04")

    Jump("loc_8D38")

    label("loc_8B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_8C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_END)), "loc_8C1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8C15")

    ChrTalk(
        0x10,
        (
            "#1809FI have a rare day off, so I'm off to\x01",
            "have some fun with a friend of mine.\x02\x03",
            "#1804FI tried to invite Ilya, but I doubt she's\x01",
            "awake yet...\x02\x03",
            "#1802FIt's pretty normal for her to sleep through\x01",
            "the entire afternoon on her days off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C18")

    label("loc_8C15")

    Call(0, 21)

    label("loc_8C18")

    Jump("loc_8C20")

    label("loc_8C1D")

    Call(0, 22)

    label("loc_8C20")

    Jump("loc_8D38")

    label("loc_8C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_END)), "loc_8D35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8D2D")

    ChrTalk(
        0x10,
        (
            "#1802FI have the rare day off, so I'm off to\x01",
            "have some fun with a friend of mine.\x02\x03",
            "#1804FI tried to invite Ilya, but I doubt she's\x01",
            "awake yet...\x02\x03",
            "#1810FIt's pretty normal for her to sleep through\x01",
            "the entire afternoon on her days off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 2)
    Jump("loc_8D30")

    label("loc_8D2D")

    Call(0, 21)

    label("loc_8D30")

    Jump("loc_8D38")

    label("loc_8D35")

    Call(0, 22)

    label("loc_8D38")

    TalkEnd(0xFE)
    Return()

    # Function_20_86A8 end

    def Function_21_8D3C(): pass

    label("Function_21_8D3C")

    TurnDirection(0x10, 0x153, 0)

    ChrTalk(
        0x10,
        (
            "#1808F(Oh, right. Isn't this the child from\x01",
            "the incident?)\x02\x03",
            "#1803F(She SEEMS normal, but I feel like there's\x01",
            "something more than meets the eye.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#1110FOh, no. What's wrong, miss?\x01",
            "Is there something stuck on\x01",
            "my face?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FDo you know her, by any chance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1802FI don't. I'm just completely awestruck by\x01",
            "how cute she is.\x02\x03",
            "#1809FI'm jealous you guys get to spend\x01",
            "your whole day around her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1109FEheheh. Thanks, Rixia!\x01",
            "You're pretty cute, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1810FTh-Thank you.\x01",
            "(This child is too adorable for me to handle.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_21_8D3C end

    def Function_22_8F76(): pass

    label("Function_22_8F76")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-1640, 1330, 55710, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -1630, 30, 54460, 0)
    SetChrPos(0xEF, -520, 30, 54660, 315)
    SetChrPos(0x153, -2610, 30, 55090, 45)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9067")

    ChrTalk(
        0x10,
        "#1805FOh, Lloyd? And Elie, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0102FIt's good to see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_910A")

    label("loc_9067")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90BC")

    ChrTalk(
        0x10,
        "#1805FOh, Lloyd? And Tio, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202FHow do you do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_910A")

    label("loc_90BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_910A")

    ChrTalk(
        0x10,
        "#1805FOh, Lloyd? And Randy, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FYo, Rixia.\x02",
    )

    CloseMessageWindow()

    label("loc_910A")


    ChrTalk(
        0x101,
        (
            "#0002FHey, Rixia.\x02\x03",
            "I heard you moved into a place downtown.\x01",
            "So this is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1809FThat's right.\x02\x03",
            "#1800FThe rent was pretty cheap, so it was\x01",
            "a no-brainer.\x02\x03",
            "#1805FOh, um... Who's the child with you?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x10, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#0012FWe're taking care of her due to--\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)
    OP_64(0x153)

    ChrTalk(
        0x153,
        (
            "#1105FWhoaaaaaaaa...\x02\x03",
            "#1109FHey, Lloyd! Check out her boobies!\x01",
            "They're huuuuuuge!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9311")

    ChrTalk(
        0x102,
        "#0105FK-KeA! That's not very polite.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9387")

    label("loc_9311")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_935A")

    ChrTalk(
        0x103,
        "#0206FSome things are better left unsaid, KeA.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9387")

    label("loc_935A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9387")

    ChrTalk(
        0x104,
        "#0305FNice taste, KeDo!\x02",
    )

    CloseMessageWindow()

    label("loc_9387")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x101, 0x153, 500)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#0011FH-Hey, KeA! That wasn't very nice of you!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(
        0x101,
        "#0006FSorry for her rudeness, Rixia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1810FN-No. It's quite all right.\x02\x03",
            "#1809FSo you're KeA, right?\x02\x03",
            "I'm Rixia Mao.\x02\x03",
            "#1802FIt's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FYeah! You, too!\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x0)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0xB3, 1)
    EventEnd(0x5)
    Return()

    # Function_22_8F76 end

    def Function_23_94AB(): pass

    label("Function_23_94AB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_68(8420, 4790, 16630, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19850, 0)
    SetChrPos(0x101, 1590, 0, 2420, 0)
    SetChrPos(0x102, 2600, 0, 1420, 45)
    SetChrPos(0x103, 440, 0, 1710, 0)
    SetChrPos(0x104, 1800, 0, 210, 135)
    SetChrPos(0x8, 3900, 2000, 11730, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)
    FadeToBright(1000, 0)
    OP_68(2260, 1300, 1970, 4800)
    MoveCamera(45, 30, 0, 4800)
    OP_6E(500, 4800)
    SetCameraDistance(19850, 4800)
    Sleep(4800)
    BeginChrThread(0x101, 3, 0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 26)
    BeginChrThread(0x104, 3, 0, 27)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_964E")

    ChrTalk(
        0x102,
        "#11P#0100FIf I'm not mistaken, this is Lotus Heights.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FThere should be three vacancies, according\x01",
            "to the documents provided by City Hall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97A2")

    label("loc_964E")


    ChrTalk(
        0x101,
        (
            "#5P#0000FWe still have the other matter in downtown\x01",
            "to worry about, but we should have time for\x01",
            "support requests.\x02\x03",
            "This appears to be the apartment complex\x01",
            "City Hall wanted us to check up on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FYes. The Downtown District's Lotus Heights.\x02\x03",
            "There should be three vacancies, according\x01",
            "to the documents provided by City Hall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97A2")

    ClearChrFlags(0x8, 0x80)
    OP_95(0x8, 3900, 0, 3680, 2000, 0x0)
    OP_93(0x8, 0xE1, 0x1F4)

    ChrTalk(
        0x8,
        "#11POh! Are you with the government?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x0, 0x3)
    EndChrThread(0x1, 0x3)
    EndChrThread(0x2, 0x3)
    EndChrThread(0x3, 0x3)

    def lambda_9801():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9801)

    def lambda_980E():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_980E)

    def lambda_981B():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_981B)

    def lambda_9828():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_9828)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#0005FActually, we're police officers.\x02\x03",
            "#0000FWe're just here to examine some vacancies\x01",
            "to help bolster our crime prevention efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PVacancies, eh? I only recall there being\x01",
            "one vacant room, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x103,
        "#6P#0205FAre you certain? Are there not three?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PNo, I don't believe so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt doesn't shock me that the government\x01",
            "has trouble keeping up with that kind of\x01",
            "information, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThat's a symptom of why the Downtown\x01",
            "District never gets any development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnyway... You're welcome to inspect the\x01",
            "vacant room as long as you don't disturb\x01",
            "the other tenants.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9AE2():

        label("loc_9AE2")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_9AE2")

    QueueWorkItem2(0x0, 1, lambda_9AE2)

    def lambda_9AF4():

        label("loc_9AF4")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_9AF4")

    QueueWorkItem2(0x1, 1, lambda_9AF4)

    def lambda_9B06():

        label("loc_9B06")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_9B06")

    QueueWorkItem2(0x2, 1, lambda_9B06)

    def lambda_9B18():

        label("loc_9B18")

        TurnDirection(0xFE, 0x8, 300)
        Yield()
        Jump("loc_9B18")

    QueueWorkItem2(0x3, 1, lambda_9B18)
    OP_95(0x8, 4330, 0, 0, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_9B4E():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9B4E)

    def lambda_9B5B():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9B5B)

    def lambda_9B68():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9B68)

    def lambda_9B75():
        OP_93(0xFE, 0x5A, 0x1E)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_9B75)
    OP_95(0x8, 7800, 0, 0, 2000, 0x0)

    def lambda_9B96():
        OP_95(0xFE, 7800, 0, -5680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9B96)

    ChrTalk(
        0x101,
        "#5P#0000FOkay, then. Shall we go take a look?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0300FSure. Sounds swell.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x0, 1590, 0, 1570, 45)
    SetChrPos(0x1, 1590, 0, 1570, 45)
    SetChrPos(0x2, 1590, 0, 1570, 45)
    SetChrPos(0x3, 1590, 0, 1570, 45)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x8, 4270, 0, -52160, 90)
    OP_29(0x3, 0x1, 0x6)
    SetScenarioFlags(0x1, 2)
    EventEnd(0x5)
    Return()

    # Function_23_94AB end

    def Function_24_9C75(): pass

    label("Function_24_9C75")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C9C")
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(10000)
    Jump("Function_24_9C75")

    label("loc_9C9C")

    Return()

    # Function_24_9C75 end

    def Function_25_9C9D(): pass

    label("Function_25_9C9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CD8")
    Sleep(1200)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1600)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1200)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(10000)
    Jump("Function_25_9C9D")

    label("loc_9CD8")

    Return()

    # Function_25_9C9D end

    def Function_26_9CD9(): pass

    label("Function_26_9CD9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D0A")
    Sleep(1300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(10000)
    Jump("Function_26_9CD9")

    label("loc_9D0A")

    Return()

    # Function_26_9CD9 end

    def Function_27_9D0B(): pass

    label("Function_27_9D0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D3C")
    Sleep(1000)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(10000)
    Jump("Function_27_9D0B")

    label("loc_9D3C")

    Return()

    # Function_27_9D0B end

    def Function_28_9D3D(): pass

    label("Function_28_9D3D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-200, 4800, 21200, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, -1000, 3500, 19700, 0)
    SetChrPos(0x102, 370, 3500, 19700, 0)
    SetChrPos(0x103, 370, 3500, 18420, 0)
    SetChrPos(0x104, -1000, 3500, 18420, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_95(0x101, -460, 3500, 20950, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0001FExcuse me! Is anybody home?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1400)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    ChrTalk(
        0x103,
        "#0200FI fail to detect any presence inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FYeah, makes sense...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0001FCheck out all the dust on the door knob, too.\x02\x03",
            "I doubt anybody's lived here for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FFigures as much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI believe every other unit is occupied,\x01",
            "making this the only vacant unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FOkay... Unit 203 of Lotus Heights.\x01",
            "(*scribble* *scribble*)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0DE")

    ChrTalk(
        0x101,
        (
            "#0003FGreat. Now that we've confirmed the details\x01",
            "in the documents, our work here is done.\x02\x03",
            "#0000FLet's head on back to City Hall and\x01",
            "report our findings.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x1E)
    Jump("loc_A113")

    label("loc_A0DE")


    ChrTalk(
        0x101,
        "#0000FAll right. Let's move on to the next one.\x02",
    )

    CloseMessageWindow()

    label("loc_A113")

    Sleep(200)
    SetChrPos(0x0, -250, 3500, 20480, 180)
    SetChrPos(0x1, -250, 3500, 20480, 180)
    SetChrPos(0x2, -250, 3500, 20480, 180)
    SetChrPos(0x3, -250, 3500, 20480, 180)
    SetScenarioFlags(0x1, 3)
    EventEnd(0x5)
    Return()

    # Function_28_9D3D end

    def Function_29_A160(): pass

    label("Function_29_A160")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A189")
    Call(0, 28)
    Jump("loc_A21A")

    label("loc_A189")

    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_A21A")

    ChrTalk(
        0x101,
        (
            "#0001FCheck out all the dust on the door knob.\x01",
            "I doubt anybody's lived here for a long time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A21A")

    TalkEnd(0xFF)
    Return()

    # Function_29_A160 end

    SaveToFile()

Try(main)
