from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4100.bin",                # FileName
        "t4100",                    # MapName
        "t4100",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4100",                  # 0
        "Musha",                  # 1
        "Old Man Quint",          # 2
        "Tourist Ryuma",          # 3
        "Flowers in front of Guy's grave",# 4
        "Flowers in front of Arios' family grave",# 5
        "Grimwood's family grave",# 6
    ))

    AddCharChip((
        "chr/ch20100.itc",                   # 00
        "chr/ch20000.itc",                   # 01
        "apl/ch50423.itc",                   # 02
        "chr/ch34200.itc",                   # 03
    ))

    DeclNpc(8579,    2000,    25379,   0,    257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-8869,   0,       11800,   0,    385,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(24340,   0,       33569,   45,   385,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(20600,   0,       34000,   0,    502,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(12000,   4000,    37000,   0,    502,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(190,     4200,    45040,   1200,    190,     5700,    45040,   0x007C, 0,  8,  0x0000)
    DeclActor(-23050,  0,       25770,   1200,    -22620,  1500,    25860,   0x007C, 0,  9,  0x0000)
    DeclActor(5560,    4000,    44710,   5000,    5560,    4000,    44710,   0x007C, 0,  12, 0x0000)
    DeclActor(20570,   0,       34830,   1500,    20570,   1500,    34830,   0x007C, 0,  10, 0x0000)
    DeclActor(12080,   4000,    37650,   1500,    12080,   5500,    37650,   0x007C, 0,  11, 0x0000)

    ScpFunction((
        "Function_0_238",          # 00, 0
        "Function_1_2E4",          # 01, 1
        "Function_2_741",          # 02, 2
        "Function_3_88B",          # 03, 3
        "Function_4_956",          # 04, 4
        "Function_5_19E1",         # 05, 5
        "Function_6_222B",         # 06, 6
        "Function_7_235E",         # 07, 7
        "Function_8_2E2F",         # 08, 8
        "Function_9_2F56",         # 09, 9
        "Function_10_348E",        # 0A, 10
        "Function_11_3533",        # 0B, 11
        "Function_12_3640",        # 0C, 12
        "Function_13_4529",        # 0D, 13
    ))


    def Function_0_238(): pass

    label("Function_0_238")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_278"),
        (1, "loc_284"),
        (2, "loc_290"),
        (3, "loc_29C"),
        (4, "loc_2A8"),
        (5, "loc_2B4"),
        (6, "loc_2C0"),
        (SWITCH_DEFAULT, "loc_2CC"),
    )


    label("loc_278")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_284")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_290")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_29C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2E3")

    Return()

    # Function_0_238 end

    def Function_1_2E4(): pass

    label("Function_1_2E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_740")
    OP_95(0xFE, -8870, 0, 11800, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -16950, 0, 11340, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -19140, 0, 11340, 2000, 0x0)
    OP_95(0xFE, -19140, 0, 16070, 2000, 0x0)
    OP_95(0xFE, -21040, 0, 16090, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -16960, 0, 16090, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -1200, 0, 16090, 2000, 0x0)
    OP_95(0xFE, -1200, 2000, 25270, 2000, 0x0)
    OP_95(0xFE, -10990, 2000, 25270, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -4930, 2000, 25270, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -1200, 2000, 25270, 2000, 0x0)
    OP_95(0xFE, -1200, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, -8460, 4000, 35990, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -170, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, -50, 4200, 43970, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, -170, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, 12000, 4000, 35990, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 4970, 4000, 36140, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 1310, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, 1310, 0, 8039, 2000, 0x0)
    OP_95(0xFE, 15920, 0, 8039, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 22720, 0, 8039, 2000, 0x0)
    OP_95(0xFE, 22720, 0, 13250, 2000, 0x0)
    OP_95(0xFE, 20500, 0, 13250, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 11500, 0, 13250, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 9240, 0, 13250, 2000, 0x0)
    OP_95(0xFE, 9240, 0, 16390, 2000, 0x0)
    OP_95(0xFE, 15980, 0, 19640, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 23050, 0, 19550, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 21270, 0, 25620, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 27500, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 27500, 0, 31330, 2000, 0x0)
    OP_95(0xFE, 20470, 0, 33170, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x6A, 0x190)
    Sleep(100)
    OP_95(0xFE, 27500, 0, 31330, 2000, 0x0)
    OP_95(0xFE, 27500, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 19550, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 6410, 2000, 0x0)
    OP_95(0xFE, 30, 0, 6690, 2000, 0x0)
    Jump("Function_1_2E4")

    label("loc_740")

    Return()

    # Function_1_2E4 end

    def Function_2_741(): pass

    label("Function_2_741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_750")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 7)

    label("loc_750")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_768")
    Event(0, 13)

    label("loc_768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_776")
    Jump("loc_832")

    label("loc_776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_784")
    Jump("loc_832")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_792")
    Jump("loc_832")

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7A5")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_832")

    label("loc_7A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7B8")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_832")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7CB")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_832")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7D9")
    Jump("loc_832")

    label("loc_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7EC")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_832")

    label("loc_7EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7FA")
    Jump("loc_832")

    label("loc_7FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_808")
    Jump("loc_832")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_81B")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_832")

    label("loc_81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_829")
    Jump("loc_832")

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_832")

    label("loc_832")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_871")
    SetChrChipByIndex(0xB, 0x2)
    SetChrPos(0xB, -23000, 0, 25500, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)

    label("loc_871")

    BeginChrThread(0x9, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88A")
    ClearChrFlags(0xA, 0x80)

    label("loc_88A")

    Return()

    # Function_2_741 end

    def Function_3_88B(): pass

    label("Function_3_88B")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_89D")
    Jump("loc_8DA")

    label("loc_89D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8B7")
    Jump("loc_8DA")

    label("loc_8B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_8C9")
    Jump("loc_8DA")

    label("loc_8C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_8DA")
    OP_66(0x2, 0x1)

    label("loc_8DA")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8F6")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_90D")

    SoundDistance(0x84, 0xFFFFD878, 0xFA0, 0xDEA8, 0x2710, 0x186A0, 0x64, 0x0)
    OP_E1(0x6C2, 0xFA0, 0xDEA8)
    OP_E1(0x4F60, 0xFA0, 0xDEA8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_955")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_955")

    Return()

    # Function_3_88B end

    def Function_4_956(): pass

    label("Function_4_956")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A09")

    ChrTalk(
        0xFE,
        "That grave you were looking at...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Parts of the name to whom it belongs\x01",
            "crumbled quite a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whose grave could it be...?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A90")

    label("loc_A09")


    ChrTalk(
        0xFE,
        (
            "I come here daily to pay my respects,\x01",
            "but I've never seen anyone visit that\x01",
            "particular grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder whose grave it is...?\x02",
    )

    CloseMessageWindow()

    label("loc_A90")

    TalkEnd(0xFE)
    Return()

    label("loc_A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEA")

    ChrTalk(
        0xFE,
        (
            "Others wonder whether my attachment\x01",
            "to the deceased is a waste of the time\x01",
            "I still have left in this world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But...I'm afraid I don't have a choice in the\x01",
            "matter. This is the only way I won't forget\x01",
            "about the one I once held most dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why you'll see me visiting\x01",
            "this grave every single day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C84")

    label("loc_BEA")


    ChrTalk(
        0xFE,
        (
            "No matter what the people may say,\x01",
            "I will keep visiting my dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no other way to stay in touch\x01",
            "for a married couple separated by death.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C84")

    Jump("loc_19DD")

    label("loc_C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D9F")

    ChrTalk(
        0xFE,
        "War is most saddening...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be it a conflict between organizations or nations,\x01",
            "innocents always suffer the consequences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they'd resort to diplomacy and solve their\x01",
            "differences with civility, like Liberl's queen did\x01",
            "with the Non-Aggression Pact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DD")

    label("loc_D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E57")

    ChrTalk(
        0xFE,
        "Every day, the gravekeeper checks up on the graves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The gravestones themselves are nothing but markers,\x01",
            "but I'm sure those who rest here are glad to have them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DD")

    label("loc_E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAF")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FHey, Granny. Are you asleep?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FH-Hey, KeA!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hoho. It's okay, dears.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You see, my husband rests beneath the soil,\x01",
            "so I came to offer him my prayers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1106FPrayers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, yes. It feels as if I can chat with my\x01",
            "husband again when I visit his grave.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10D0")

    label("loc_FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1010")

    ChrTalk(
        0xFE,
        "But...I think it's about time I head home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It was nice seeing you again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10D0")

    label("loc_1010")


    ChrTalk(
        0xFE,
        (
            "It's been a while since I've been able to\x01",
            "chat with someone as young as you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You remind me of my son back when\x01",
            "he was a young man. Unfortunately,\x01",
            "he's been living abroad these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D0")

    Jump("loc_19DD")

    label("loc_10D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_11D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118D")

    ChrTalk(
        0xFE,
        (
            "I think I'll celebrate Crossbell's 70th\x01",
            "anniversary in silence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gazing at the beautiful view from\x01",
            "up here sounds like a good way\x01",
            "to spend the day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11CC")

    label("loc_118D")


    ChrTalk(
        0xFE,
        (
            "I'll spend the day up here, enjoying\x01",
            "the peace and quiet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CC")

    Jump("loc_19DD")

    label("loc_11D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_12F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1293")

    ChrTalk(
        0xFE,
        (
            "Last night, I took a stroll\x01",
            "through a crowded street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The illuminated townscape\x01",
            "was just fabulous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If only I could've had my\x01",
            "better half there with me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12F4")

    label("loc_1293")


    ChrTalk(
        0xFE,
        (
            "I wish I could've marveled over\x01",
            "Crossbell's beautiful skyline at\x01",
            "night together with him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F4")

    Jump("loc_19DD")

    label("loc_12F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_150B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1436")

    ChrTalk(
        0xFE,
        (
            "I had the opportunity to talk to\x01",
            "the gravekeeper when I finished\x01",
            "paying my respects yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He gave me the idea that it would be\x01",
            "a waste to do nothing but pray during\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose he has a point. Tonight, I will\x01",
            "enjoy Crossbell's night sky instead.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1506")

    label("loc_1436")


    ChrTalk(
        0xFE,
        (
            "He gave me the idea that it would be\x01",
            "a waste to do nothing but praying\x01",
            "during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel sorry for my husband who's resting here,\x01",
            "but today I'll take it easy and enjoy myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1506")

    Jump("loc_19DD")

    label("loc_150B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_15AB")
    OP_93(0xFE, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159D")

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001F(Her dedication is saint-like...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F(We shouldn't disturb her. Come on, let's go.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15A6")

    label("loc_159D")


    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    label("loc_15A6")

    Jump("loc_19DD")

    label("loc_15AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_179E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170A")

    ChrTalk(
        0xFE,
        (
            "My husband passed away during a bloody\x01",
            "dispute 30 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The day it happened, we had gotten into an\x01",
            "argument and he stormed out of the house.\x01",
            "I never got to say goodbye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't all of you have someone you\x01",
            "really, truly care about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make sure you don't wind up like me.\x01",
            "Alive, sure, but full of regret.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1799")

    label("loc_170A")


    ChrTalk(
        0xFE,
        (
            "Don't all of you have someone you\x01",
            "really, truly care about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make sure you don't wind up like me.\x01",
            "Alive, sure, but full of regret.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1799")

    Jump("loc_19DD")

    label("loc_179E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_18D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1865")

    ChrTalk(
        0xFE,
        (
            "A skirmish between Erebonia and\x01",
            "Calvard 30 years ago robbed me\x01",
            "of my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We had fights day in, day out,\x01",
            "but if I had known how things\x01",
            "would've turned out...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18D4")

    label("loc_1865")


    ChrTalk(
        0xFE,
        (
            "I know that damned skirmish\x01",
            "30 years ago is the real culprit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...but I can't help but feel guilty.\x02",
    )

    CloseMessageWindow()

    label("loc_18D4")

    Jump("loc_19DD")

    label("loc_18D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_19DD")
    OP_93(0xFE, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1971")

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Oh, do forgive me.\x01",
            "I hadn't noticed you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To She who hears our prayers\x01",
            "do I beg forgiveness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19DD")

    label("loc_1971")


    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105F(Her dedication is saint-like...)\x02\x03",
            "#0108F(We shouldn't disturb her. Come on, let's go.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DD")

    TalkEnd(0xFE)
    Return()

    # Function_4_956 end

    def Function_5_19E1(): pass

    label("Function_5_19E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_19F2")
    Jump("loc_2227")

    label("loc_19F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A00")
    Jump("loc_2227")

    label("loc_1A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1A0E")
    Jump("loc_2227")

    label("loc_1A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF0")

    ChrTalk(
        0xFE,
        "I'm busy with my daily cleaning of the graves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With so many tombstones here, I can't help\x01",
            "but think I end up neglecting some of them.\x01",
            "I try not to, but the thought of it pulls at my heart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BDB")

    label("loc_1AF0")


    ChrTalk(
        0xFE,
        (
            "With so many tombstones here, I can't help\x01",
            "but think I end up neglecting some of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The circumstances surrounding each of the souls\x01",
            "sleeping here are vastly different, but I do wish\x01",
            "more people would visit every so often.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDB")

    Jump("loc_2227")

    label("loc_1BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1CA8")

    ChrTalk(
        0xFE,
        (
            "Most of the Sunday School kids are too shy\x01",
            "to venture into the cemetery.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    ChrTalk(
        0xFE,
        "Hohoho. You must be the exception, missy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1111FHo...ho? You've got a funny laugh, mister.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2227")

    label("loc_1CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1F0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E96")

    ChrTalk(
        0xFE,
        "I see you've brought along a new face this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FHeya! What the heck are you doing\x01",
            "in a place like this, Grandpa?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    ChrTalk(
        0xFE,
        (
            "Well, it's my job to watch over this place.\x01",
            "I wouldn't want anyone to disturb the\x01",
            "souls sleeping here, now would I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fortunately, nonsense like grave-robbing\x01",
            "is a rare occurrence in this day and age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1106FUh, I dunno what you're talking about...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho, pardon me. You're probably a bit\x01",
            "too young to understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F0A")

    label("loc_1E96")


    ChrTalk(
        0xFE,
        (
            "I doubt she'd be able to understand all I\x01",
            "do as a gravekeeper at her age. Not that\x01",
            "that's an issue, of course.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F0A")

    Jump("loc_2227")

    label("loc_1F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F1D")
    Jump("loc_2227")

    label("loc_1F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2016")

    ChrTalk(
        0xFE,
        (
            "Before the Non-Aggression Pact was signed,\x01",
            "bloodshed and the loss of loved ones were as\x01",
            "common as breathing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I still remember the dread I felt during all of\x01",
            "those funerals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't say I'd like to experience that again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2227")

    label("loc_2016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2024")
    Jump("loc_2227")

    label("loc_2024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2032")
    Jump("loc_2227")

    label("loc_2032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2210")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2146")

    ChrTalk(
        0xFE,
        (
            "Sunday School never fails to put a smile on\x01",
            "this old man's face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hearing the cheerful voices of children reach\x01",
            "a sad place like this is a lifesaver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can get lonely tending the graves when the\x01",
            "cathedral isn't holding Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_220B")

    label("loc_2146")


    ChrTalk(
        0xFE,
        (
            "On school days, the excited voices of children\x01",
            "as they play is enough to save me from those\x01",
            "feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can get lonely tending the graves when the\x01",
            "cathedral isn't holding Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220B")

    Jump("loc_2227")

    label("loc_2210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_221E")
    Jump("loc_2227")

    label("loc_221E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2227")

    label("loc_2227")

    TalkEnd(0xFE)
    Return()

    # Function_5_19E1 end

    def Function_6_222B(): pass

    label("Function_6_222B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E1")

    ChrTalk(
        0xFE,
        (
            "Ignoring the fact that I somehow ended up\x01",
            "near a bunch of dead guys...this place has\x01",
            "quite the view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it's hard to beat high-up vistas like this.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_235A")

    label("loc_22E1")


    ChrTalk(
        0xFE,
        (
            "Taking the clear skies and amazing scenery\x01",
            "into account...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...this might be the best view in all of Crossbell.\x02",
    )

    CloseMessageWindow()

    label("loc_235A")

    TalkEnd(0xFE)
    Return()

    # Function_6_222B end

    def Function_7_235E(): pass

    label("Function_7_235E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50013.itc", 0x1E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis009.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis010.itp")
    Sleep(500)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300001V\x07\x0C",
            "#30WOur beloved Goddess, Aidios, who art in the sky...\x02\x03",
            "#0300002V...we beseech Thee. Open Thy heavenly gates for\x01",
            "the soul running towards Your loving embrace.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    PlayBGM("ed7534", 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1500)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300003V\x07\x0C",
            "#30W(I couldn't believe the news when I first heard it.\x01",
            "A guy like him, passing this young...?)\x02\x03",
            "#0300004V(Wasn't he about to get married to that beautiful fiancee\x01",
            "of his, too? Why did things end up like this? Why...?)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(150)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300005V\x07\x0C",
            "#30W(Damn it all! What the hell are the police doing?!)\x02\x03",
            "#0300006V(One of their own was killed! Are they going to let\x01",
            "this become another unsolved case?!)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(150)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300007V\x07\x0C",
            "#30W(It's horrible, absolutely horrible. His parents passed away\x01",
            "a while ago, didn't they?)\x02\x03",
            "#0300008V(How will his younger brother handle all this...?)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(800)
    SetChrName("Woman")

    AnonymousTalk(
        0xFF,
        (
            "#0300009V\x07\x0C",
            "#30W...Lloyd. Are you feeling all right?\x02\x03",
            "#0300010VPlease, don't push yourself. I know you\x01",
            "haven't been sleeping much recently.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#0300011V\x07\x0C",
            "#30WI'm fine, Cecile.\x02\x03",
            "#0300012VI'm just sorry that you've had to go out of the way for me\x01",
            "like this. I should have taken care of all this myself...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Woman")

    AnonymousTalk(
        0xFF,
        (
            "#0300013V\x07\x0C",
            "#30WYou don't have to keep up this distant facade around me.\x01",
            "We're family, aren't we?\x02\x03",
            "#0300014V#40WBesides, Guy was my... My...\x02\x03",
            "#0300015V#40W...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#0300016V\x07\x0C",
            "#30WCecile...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Woman")

    AnonymousTalk(
        0xFF,
        (
            "#0300017V\x07\x0C",
            "#30WI'm so, so sorry, Lloyd. I know that you're\x01",
            "hurting the most out of all of us.\x02\x03",
            "#0300018VThings are going to be hard from now on,\x01",
            "but please don't forget that I'm here for you.\x02\x03",
            "#0300019VUntil you can stand on your own two feet,\x01",
            "I'll stand by your side...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_68(11000, 1500, 18800, 0)
    MoveCamera(312, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrPos(0x101, -23000, 0, 24500, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x2)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -23000, 0, 25500, 0)
    MoveCamera(322, 13, 0, 6000)
    SetCameraDistance(37500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x50)
    Fade(1000)
    OP_68(-23300, 600, 21800, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-23300, 600, 25800, 4000)
    SetCameraDistance(15500, 4000)
    OP_6F(0x11)

    ChrTalk(
        0x101,
        (
            "#0300020V#6P#0008F...\x02\x03",
            "#0300021V#0004FI really was a brat, wasn't I?\x02\x03",
            "#0300022VI shouldn't have been so stubborn.\x01",
            "I should have taken her outstretched\x01",
            "hand...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x101, 0x1)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0300023V#6P#0003F(I'm home, Guy.)\x02\x03",
            "#0300024V#0008F(I'm sorry for not visiting you sooner.\x01",
            "I guess I'm still as stubborn as I ever\x01",
            "was.)\x02\x03",
            "#0300025V#0002F(But I'm here now. I'm back.)\x02\x03",
            "#0300026V(I became a detective of the CPD, just like\x01",
            "you were.)\x02\x03",
            "#0300027V#0004F(I've got a long way to go to catch up, and\x01",
            "I was assigned to a weird division...but I'll\x01",
            "do the best with the hand I was dealt.)\x02\x03",
            "#0300028V#0000F(Keep watching over me, Guy. I'll talk to you\x01",
            "again soon.)\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_235E end

    def Function_8_2E2F(): pass

    label("Function_8_2E2F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            " Oh, sweet lambs born beneath the bell,\x01",
            "          sleep peacefully.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Let the golden light shining betwixt the pure clouds\x01",
            "          lead ye to the great blue sky\x01",
            "     and guide your souls back to the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_2E2F end

    def Function_9_2F56(): pass

    label("Function_9_2F56")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "   　　　　　Here Lies\x01",
            "   　　　　Guy Bannings\x01",
            "───────────────\x01",
            "  　　　　S1176 - S1201\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300F")

    ChrTalk(
        0x101,
        "#6P#0008F...\x02",
    )

    CloseMessageWindow()

    label("loc_300F")

    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_348D")
    Sleep(150)
    EventBegin(0x0)
    StopBGM(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    SetChrPos(0x101, -22900, 0, 24540, 0)
    SetChrPos(0x102, -23050, 0, 21800, 0)
    SetChrPos(0x103, -21380, 0, 22100, 350)
    SetChrPos(0x104, -24580, 0, 22100, 0)
    OP_68(-22960, 2500, 24900, 0)
    MoveCamera(334, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(14810, 0)
    Sleep(10)
    PlayBGM("ed7001", 0)
    FadeToBright(1000, 0)
    OP_68(-22960, 1500, 24900, 3000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#0003F(I finally found your badge, Guy.)\x02\x03",
            "(With this in hand, I can finally take the first steps\x01",
            "toward avenging your death.)\x02\x03",
            "#0008F(But, I'm sorry. That has to wait. For now, I have\x01",
            "to focus on the case in front of me.)\x02\x03",
            "(Citizens getting wrapped up with some mysterious\x01",
            "drug and vanishing into thin air? I'm not sure if\x01",
            "Crossbell's ever dealt with something this big.)\x02\x03",
            "#0001F(I know that you'd never let a case like this go\x01",
            "unsolved...)\x02\x03",
            "#0004F(And while I'm still nowhere close to you, what\x01",
            "I do have is a team that has my back. I know\x01",
            "I can count on them when the going gets tough.)\x02\x03",
            "(Most importantly...I've found someone who I'm\x01",
            "going to protect, no matter the costs.)\x02\x03",
            "#0000F(That's why you don't need to worry about me,\x01",
            "Guy. Just watch me!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105F...Lloyd? Are you all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYou seem fired up. What's the deal?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#0004F#11PIt's nothing. Just a quick chat.\x02\x03",
            "#0000FLet's move out, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202F#2PRoger!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0xE7, 1)
    EventEnd(0x5)

    label("loc_348D")

    Return()

    # Function_9_2F56 end

    def Function_10_348E(): pass

    label("Function_10_348E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　　　   Here Lies\x01",
            "　　　　   Saya MacLaine\x01",
            "───────────────\x01",
            "　　　　  S1175 - S1199\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_348E end

    def Function_11_3533(): pass

    label("Function_11_3533")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "   .....r...    ....es\x01",
            ".....    .......................\x01",
            ".......  .......................\x01",
            "───────────────\x01",
            "S1...... - S1....8....\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_363C")
    SetScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 0)

    label("loc_363C")

    TalkEnd(0xFF)
    Return()

    # Function_11_3533 end

    def Function_12_3640(): pass

    label("Function_12_3640")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(4760, 5200, 45880, 0)
    MoveCamera(339, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19410, 0)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, 7090, 4000, 45490, 320)
    SetChrPos(0x102, 5840, 4000, 45440, 320)
    SetChrPos(0x103, 6560, 4000, 43510, 320)
    SetChrPos(0x104, 5070, 4000, 43640, 320)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#6P#0305FSheesh. Safety hazard, much? There\x01",
            "ain't even a fence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FI really doubt anyone would be standing on\x01",
            "the edge of a cliff like this in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FLook, you can see the bottom of the valley\x01",
            "from here. Quite the drop, isn't it?\x02\x03",
            "#0103FIf you stare for too long, it starts to feel like\x01",
            "it's sucking you down into it. It's not a very\x01",
            "pleasant feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FThis is a cemetery, after all.\x02\x03",
            "#0204FPerhaps someone from the other side\x01",
            "is beckoning you to join them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FD-Did you really have to phrase it like\x01",
            "that, Tio...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FWell, putting the supernatural aside...\x02\x03",
            "#0000FThis spot would make a nice photo\x01",
            "for Grace's article.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4177")
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#12P#0000FDo you mind taking a few photos\x01",
            "for us, Elie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#6P#0108FN-Not at all. Don't expect a masterpiece\x01",
            "from me, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#6P#0300FPssh. Relax, Mademois-Elie.\x02\x03",
            "Ya just gotta peek through that lens,\x01",
            "give it a lil' click, then bam, we good!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#6P#0103F*sigh* If only capturing a great\x01",
            "photo were that simple...\x02\x03",
            "#0100FYou need to pay close attention to\x01",
            "your composition to ensure you've\x01",
            "captured everything in frame.\x02\x03",
            "The weather, wind speed, and lighting\x01",
            "can completely alter the impression\x01",
            "a photo gives.\x02\x03",
            "There are no second chances when\x01",
            "it comes to a picture-perfect moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FThe difference in quality between\x01",
            "amateur and professional photography\x01",
            "is immediately apparent.\x02\x03",
            "#0203FI would imagine a simpleton would have\x01",
            "difficulty grasping any level of intricacy\x01",
            "or nuance, however.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        "#6P#0306FDamn, Tio Tot. You implyin' something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FC-Calm down, everyone. We should\x01",
            "let Elie focus on taking the photo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FRight... I'll try to live up to your\x01",
            "expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x12C, 0x1F4)
    OP_93(0x101, 0x12C, 0x1F4)
    OP_93(0x103, 0x12C, 0x1F4)
    OP_93(0x104, 0x12C, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#6P#0103FPhew... There we go. I took a\x01",
            "couple of extras, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FHey, it looks like you pulled through.\x02\x03",
            "Well? How'd they turn out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FI won't have an answer for you until\x01",
            "I've seen the developed photos.\x02\x03",
            "At the very least, I think they'll\x01",
            "get the job done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FIt would be a safe assumption to think\x01",
            "Elie has regained her photography skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FWell, I'm no picture-takin' guru,\x01",
            "but I'm sure they turned out fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FRight. We should keep our eyes\x01",
            "peeled for other scenic locations\x01",
            "we can take photos of.\x02\x03",
            "But anyway, let's get a move on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44F3")

    label("loc_4177")

    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#12P#0000FWill you do the honors, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FOkay. Leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x12C, 0x1F4)
    OP_93(0x101, 0x12C, 0x1F4)
    OP_93(0x103, 0x12C, 0x1F4)
    OP_93(0x104, 0x12C, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#0103FPhew... I hope they turned out okay.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_430E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_430E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_4325")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4325")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_433C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_433C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_4353")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4353")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_436A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_436A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_4381")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4381")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_4398")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4398")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_43AF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_43C6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4494")

    ChrTalk(
        0x101,
        (
            "#12P#0000FGood job, Elie. You look like you're\x01",
            "getting the hang of it again.\x02\x03",
            "And now we've managed to meet Grace's\x01",
            "five-photo quota. Let's run these by her\x01",
            "when we get the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44F3")

    label("loc_4494")


    ChrTalk(
        0x101,
        (
            "#12P#0000FNice, Elie! You looked pretty confident\x01",
            "taking that picture.\x02\x03",
            "Shall we move on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44F3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5840, 4000, 45440, 320)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x5)
    Sleep(500)
    OP_65(0x2, 0x1)
    EventEnd(0x5)
    Return()

    # Function_12_3640 end

    def Function_13_4529(): pass

    label("Function_13_4529")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(21970, 1500, 30960, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 21500, 0, 30200, 0)
    SetChrPos(0x102, 20300, 0, 30200, 0)
    SetChrPos(0x103, 21500, 0, 29000, 0)
    SetChrPos(0x104, 20300, 0, 29000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45D2")
    SetChrPos(0x10A, 22710, 0, 29860, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_45D2")

    SetChrPos(0x9, 20830, 0, 32299, 0)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    OP_4B(0x9, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xB, 0x2)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -23000, 0, 25500, 0)
    SetCameraDistance(16000, 3000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　　　Here Lies\x01",
            "　　　　Saya MacLaine\x01",
            "───────────────\x01",
            "　　　　S1175 - S1199\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0x101,
        "#6P#0005F(MacLaine?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0105F(Could this be Arios' wife?)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4741")

    ChrTalk(
        0x10A,
        "#12P#0608F(...)\x02",
    )

    CloseMessageWindow()

    label("loc_4741")

    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        "#11POn to the next one.\x02",
    )

    CloseMessageWindow()

    def lambda_477B():
        OP_95(0xFE, 24000, 0, 32299, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_477B)
    WaitChrThread(0x9, 1)

    def lambda_4799():
        OP_95(0xFE, 24000, 0, 29000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4799)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_68(13470, 5500, 33550, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16200, 0)
    SetChrPos(0x101, 13200, 4000, 33300, 0)
    SetChrPos(0x102, 12000, 4000, 33300, 0)
    SetChrPos(0x103, 13200, 4000, 32100, 0)
    SetChrPos(0x104, 12000, 4000, 32100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4850")
    SetChrPos(0x10A, 14210, 4000, 32460, 0)

    label("loc_4850")

    SetChrPos(0x9, 12330, 4000, 35000, 0)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    OP_4B(0x9, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetCameraDistance(15200, 3000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "   .....r...    ....es\x01",
            ".....    .......................\x01",
            ".......  .......................\x01",
            "───────────────\x01",
            "S1...... - S1....8....\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#6P#0303F(This one's seen better days. Can't\x01",
            "even make out whose name's on it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200F(Perhaps the gravekeeper knows?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHere's the last one.\x02",
    )

    CloseMessageWindow()

    def lambda_4A37():
        OP_95(0xFE, 10300, 4000, 35000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4A37)
    WaitChrThread(0x9, 1)

    def lambda_4A55():
        OP_95(0xFE, 10300, 4000, 33300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4A55)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_68(-21390, 1500, 21840, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -21500, 0, 21800, 0)
    SetChrPos(0x102, -22700, 0, 21800, 0)
    SetChrPos(0x103, -21500, 0, 20600, 0)
    SetChrPos(0x104, -22700, 0, 20600, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B0C")
    SetChrPos(0x10A, -20400, 0, 20980, 0)

    label("loc_4B0C")

    SetChrPos(0x9, -22460, 0, 23700, 0)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    OP_4B(0x9, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetCameraDistance(16000, 3000)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#0005F...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　　　　Here Lies\x01",
            "　　　　　Guy Bannings\x01",
            "───────────────\x01",
            "　　　　　S1176 - S1201\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#5P#0305FIs this who I think it is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0105FLloyd's older brother...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0208F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe reason I asked you to gather those\x01",
            "three flowers is pretty simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI wanted to give them to Guy Bannings\x01",
            "and to the families of those that were\x01",
            "precious to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's only natural to want to show respect\x01",
            "to one's closest friends, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DF0")

    ChrTalk(
        0x10A,
        "#12P#0603FYou knew him, didn't you?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E1F")

    label("loc_4DF0")


    ChrTalk(
        0x101,
        "#6P#0005FSir...did you know Guy Bannings?\x02",
    )

    CloseMessageWindow()

    label("loc_4E1F")

    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#11PThat's right. Doubt I could forget\x01",
            "him even if I tried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBack when he was alive, he often\x01",
            "came to visit me in my cabin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWe'd share drinks and stories till\x01",
            "the sun rose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI never had a family, you see, but I can't\x01",
            "tell you how many times he saved this\x01",
            "old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0003FI had no idea...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FI am starting to understand the nature\x01",
            "of this support request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWhen it came time for his funeral, I felt\x01",
            "like I was torn to shreds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYour name was Lloyd, right? So you\x01",
            "must be Guy's younger brother.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#0005FY-You know who I am?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI first saw you at your brother's funeral.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAfter seeing the SSS's photo in the\x01",
            "Crossbell Times four months ago, I\x01",
            "finally remembered you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHeh. Your faces aren't anything alike,\x01",
            "but I'm starting to see the resemblance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0012FHaha. Yeah, he was always the bulkier\x01",
            "brother. I'll get there someday, maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0108FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PActually, there's another reason why I\x01",
            "submitted such an annoying job to the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI needed to ascertain firsthand whether you\x01",
            "four, Guy's successors, had grown any.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0300FAnd...? Did we make the grade?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, you finished the job, so that's something.\x01",
            "However, you're still rough around the edges.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0306FDamn. Tell us how you really feel.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53D7")

    ChrTalk(
        0x10A,
        (
            "#12P#0603FI'd say that's an apt assessment of greenhorns\x01",
            "such as yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D7")


    ChrTalk(
        0x9,
        (
            "#11PHohoho. Despite all that, I think the\x01",
            "Special Support Section has a bright\x01",
            "future ahead of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou'll catch up to Guy someday. You\x01",
            "may even be able to overtake him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd when that happens...come back\x01",
            "here and pay me a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWe'll share some drinks, the same\x01",
            "as I did with Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0004FAll right. I'm looking forward to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FYour older brother lives on through\x01",
            "a lot of people, doesn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0202FI agree.\x02\x03",
            "#0204F(Through me, as well.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FCatchin' up to a guy that talented ain't the\x01",
            "easiest thing in the world. It's going to take\x01",
            "quite a while, I bet.\x02\x03",
            "#0309FHonestly, that goal might end up bein' a\x01",
            "bigger barrier than takin' down the mafia\x01",
            "or Crossbell's corruption, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0004FYeah, you said it.\x02\x03",
            "#0001F(And yet I will surpass him someday.\x01",
            "I have to.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PLooks like I've talked your ears\x01",
            "off. Time to head back inside.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("t4020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_4529 end

    SaveToFile()

Try(main)
