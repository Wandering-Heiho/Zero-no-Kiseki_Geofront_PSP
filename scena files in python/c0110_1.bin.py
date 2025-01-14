from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0110_1.bin",                # FileName
        "c0110",                    # MapName
        "c0110",                    # Location
        0x0009,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1000, 0, 2000, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0110_1",                # 0
    ))

    DeclEvent(0x0000, 0, 17,  10.0,                  10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -5.0,                  -2.0999999046325684,   -0.0,                  1.0])

    ScpFunction((
        "Function_0_194",          # 00, 0
        "Function_1_431",          # 01, 1
        "Function_2_435",          # 02, 2
        "Function_3_B0A",          # 03, 3
        "Function_4_218C",         # 04, 4
        "Function_5_251B",         # 05, 5
        "Function_6_26E0",         # 06, 6
        "Function_7_2E47",         # 07, 7
        "Function_8_3459",         # 08, 8
        "Function_9_377B",         # 09, 9
        "Function_10_3923",        # 0A, 10
        "Function_11_3BA0",        # 0B, 11
        "Function_12_3EC7",        # 0C, 12
        "Function_13_42BD",        # 0D, 13
        "Function_14_4881",        # 0E, 14
        "Function_15_5426",        # 0F, 15
        "Function_16_5463",        # 10, 16
        "Function_17_5BFD",        # 11, 17
        "Function_18_5E78",        # 12, 18
        "Function_19_5F17",        # 13, 19
        "Function_20_6145",        # 14, 20
        "Function_21_68DE",        # 15, 21
        "Function_22_6F20",        # 16, 22
        "Function_23_70F4",        # 17, 23
        "Function_24_72C8",        # 18, 24
        "Function_25_74A2",        # 19, 25
        "Function_26_7687",        # 1A, 26
        "Function_27_7856",        # 1B, 27
        "Function_28_7A25",        # 1C, 28
        "Function_29_7BF1",        # 1D, 29
        "Function_30_7DC8",        # 1E, 30
        "Function_31_7E44",        # 1F, 31
        "Function_32_7EEC",        # 20, 32
        "Function_33_8029",        # 21, 33
        "Function_34_80CC",        # 22, 34
        "Function_35_8172",        # 23, 35
        "Function_36_8218",        # 24, 36
        "Function_37_82BE",        # 25, 37
        "Function_38_836E",        # 26, 38
        "Function_39_8410",        # 27, 39
    ))


    def Function_0_194(): pass

    label("Function_0_194")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_277")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's a note stuck to the bulletin board.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The fox needed to talk, so I'll be back once\x01",
            "I'm done dealing with him.\x01",
            "                                       - Sergei\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_42D")

    label("loc_277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_357")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's a note stuck to the bulletin board.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'm off to the Police Department. Should be\x01",
            "back by evening. Hopefully.\x01",
            "                                       - Sergei\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_42D")

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_42D")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's a note stuck to the bulletin board.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I've got some errands to run. Wrap up the\x01",
            "case however you see fit.\x01",
            "                                      - Sergei\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_42D")

    TalkEnd(0xFF)
    Return()

    # Function_0_194 end

    def Function_1_431(): pass

    label("Function_1_431")

    Call(1, 3)
    Return()

    # Function_1_431 end

    def Function_2_435(): pass

    label("Function_2_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_450")
    Call(0, 48)
    Jump("loc_B09")

    label("loc_450")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_461")
    Jump("loc_B06")

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_46F")
    Jump("loc_B06")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_47D")
    Jump("loc_B06")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_596")
    OP_93(0xFE, 0x5A, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Sergei's cleaning up the kitchen after\x01",
            "breakfast.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "#1003FIf the mafia's involved, it should fall to\x01",
            "the First Division.\x02\x03",
            "#1000FThey can't ignore a case this big.\x02\x03",
            "I'll head to the department to ask them\x01",
            "about it, just in case.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5FF")

    label("loc_596")


    ChrTalk(
        0x8,
        (
            "#1000FThat's all I got. Dismissed.\x02\x03",
            "I'll head to the police department later\x01",
            "and ask them about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FF")

    Jump("loc_B06")

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_612")
    Jump("loc_B06")

    label("loc_612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_620")
    Jump("loc_B06")

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_62E")
    Jump("loc_B06")

    label("loc_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_63C")
    Jump("loc_B06")

    label("loc_63C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_64A")
    Jump("loc_B06")

    label("loc_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_658")
    Jump("loc_B06")

    label("loc_658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_666")
    Jump("loc_B06")

    label("loc_666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94D")

    ChrTalk(
        0x8,
        "#1005FOh, you're back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FChief...\x01",
            "It's rare to see you in your room.\x02\x03",
            "Looking for something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1002FNot really. Well, sort of, I guess.\x02\x03",
            "Ran out of cigarettes, so now I'm\x01",
            "searching for my secret stash of\x01",
            "mira.\x02",
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
        0x103,
        (
            "#0206FI assumed it was something like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1003FOh, yeah. That Zeit was loafing\x01",
            "around near the back entrance.\x02\x03",
            "#1000FHe's your responsibility, so take\x01",
            "care of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0302FNot a problem!\x02\x03",
            "#0309FTio Tot and Mademois-Elie's constant petting\x01",
            "should probably be enough for the guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0113FAhem. Affection IS rather important, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202FYes. Extremely important.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_A19")

    label("loc_94D")


    ChrTalk(
        0x8,
        (
            "#1003FOh, yeah. That Zeit was loafing\x01",
            "around near the back entrance.\x02\x03",
            "#1000FHe's your responsibility, so take\x01",
            "care of him.\x02\x03",
            "I'll give him a bite to eat every now\x01",
            "and then, but the rest is up to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A19")

    Jump("loc_B06")

    label("loc_A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A2C")
    Jump("loc_B06")

    label("loc_A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A3A")
    Jump("loc_B06")

    label("loc_A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A48")
    Jump("loc_B06")

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A56")
    Jump("loc_B06")

    label("loc_A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A64")
    Jump("loc_B06")

    label("loc_A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_B06")

    ChrTalk(
        0x8,
        (
            "#1000FWhat's wrong? Those support requests won't\x01",
            "take care of themselves.\x02\x03",
            "All you have to do is log in to the terminal\x01",
            "and see what they're about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B06")

    TalkEnd(0x8)

    label("loc_B09")

    Return()

    # Function_2_435 end

    def Function_3_B0A(): pass

    label("Function_3_B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B25")
    Call(0, 48)
    Jump("loc_218B")

    label("loc_B25")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BB9")
    Jump("loc_C03")

    label("loc_BB9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BD9")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C03")

    label("loc_BD9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF9")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C03")

    label("loc_BF9")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C03")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_106F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 2)), scpexpr(EXPR_END)), "loc_CB9")

    ChrTalk(
        0x9,
        (
            "#1005FBack already?\x02\x03",
            "#1003FLeave getting in touch with Sonya\x01",
            "to me.\x02\x03",
            "#1001FYou guys should hurry on to the\x01",
            "hospital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106A")

    label("loc_CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_EC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5A")

    ChrTalk(
        0x9,
        (
            "#1005FWhat's the matter? Weren't you\x01",
            "supposed to be going to St. Ursula?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FYeah, but the thing is...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained what Dudley had told them and\x01",
            "that they had lost all contact with St. Ursula.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1010F...\x02\x03",
            "Damn. Doubt that's a coincidence.\x02\x03",
            "#1003FFor now, I'll try to get in contact with them.\x02\x03",
            "#1001FYou guys should hurry on to St. Ursula.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0013FYes, sir!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 5)
    Jump("loc_EBB")

    label("loc_E5A")


    ChrTalk(
        0x9,
        (
            "#1001FI'll try to get in contact with an employee.\x02\x03",
            "You guys should hurry on to St. Ursula.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EBB")

    Jump("loc_106A")

    label("loc_EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAE")

    ChrTalk(
        0x9,
        (
            "#1000FI'll stay in touch with the guild, okay?\x02\x03",
            "Shouldn't you be off to meet with that doctor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FLooks like Shizuku's staying with KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1002FYeah. Zeit's with them, too.\x01",
            "Don't worry about stuff here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_106A")

    label("loc_FAE")


    ChrTalk(
        0x9,
        (
            "#1003FDon't worry about stuff here. I've got\x01",
            "everything under control.\x02\x03",
            "#1000FYou guys should hurry on to St. Ursula.\x02\x03",
            "We need the results of the drug analysis\x01",
            "by the end of the day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106A")

    Jump("loc_2184")

    label("loc_106F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_12EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_112A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1093")
    Call(1, 13)
    Jump("loc_1125")

    label("loc_1093")


    ChrTalk(
        0x9,
        (
            "#1003FDon't worry. Leave the higher-ups to me.\x02\x03",
            "#1001FIf you want to investigate, you better get a\x01",
            "move on. I won't be here for much longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1125")

    Jump("loc_12E6")

    label("loc_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1267")

    ChrTalk(
        0x9,
        (
            "#1003FOne of your witnesses vanished?\x02\x03",
            "#1001FThe situation might be deteriorating faster\x01",
            "than we thought it would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FApparently so. And we still don't know\x01",
            "how this happened in the first place...\x02\x03",
            "#0000FSorry, Chief. We're counting on you to\x01",
            "hold down the fort!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1000FSure thing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_12E6")

    label("loc_1267")


    ChrTalk(
        0x9,
        (
            "#1000FIf that cult really is involved...you'll be\x01",
            "near the end of your investigation.\x02\x03",
            "Don't let your guard down, got it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E6")

    Jump("loc_2184")

    label("loc_12EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1403")

    ChrTalk(
        0x9,
        (
            "#1003FIn the meantime, we should let the First\x01",
            "Division do their job...\x02\x03",
            "#1002F...especially while those drugs are being\x01",
            "looked at. They're good at what they do,\x01",
            "so I'm sure they will deliver.\x02\x03",
            "Just do your own thing for now... Y'know,\x01",
            "like you've always done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2184")

    label("loc_1403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_1545")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#4200618V#1005FYou're late.\x02\x03",
            "#4200619V#1000FInterrogating Heiyue really take you\x01",
            "that long?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200620V#0003FNo, actually. We may have just stumbled\x01",
            "into another case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200621V#0101FBut we'll include it in the usual report,\x01",
            "along with details on the Heiyue raid.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 47)
    Return()

    label("loc_1545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1553")
    Jump("loc_2184")

    label("loc_1553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1561")
    Jump("loc_2184")

    label("loc_1561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_156F")
    Jump("loc_2184")

    label("loc_156F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_163A")

    ChrTalk(
        0x9,
        (
            "#1004FLloyd, I have to leave KeA to you for\x01",
            "a while.\x02\x03",
            "#1000FBut if you find something, call me as\x01",
            "soon as you can. The entire CPD\x01",
            "is involved now, you understand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYes, sir.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2184")

    label("loc_163A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1648")
    Jump("loc_2184")

    label("loc_1648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1833")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A6")

    ChrTalk(
        0x9,
        (
            "#1000FHmph. You look prepared for the\x01",
            "worst, at least.\x02\x03",
            "#1004FWell, act as you see fit. I'll cover\x01",
            "you, as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks, Chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWe couldn't do this without you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1002FDon't mention it. After all, the Special\x01",
            "Support Section was established for\x01",
            "times like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FTh-That's true.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_182E")

    label("loc_17A6")


    ChrTalk(
        0x9,
        (
            "#1004FMaybe I can throw them off guard by\x01",
            "making them a nice cup of joe...\x02\x03",
            "#1002FDon't worry about me. I was born for\x01",
            "this stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182E")

    Jump("loc_2184")

    label("loc_1833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1841")
    Jump("loc_2184")

    label("loc_1841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_184F")
    Jump("loc_2184")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_185D")
    Jump("loc_2184")

    label("loc_185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1A36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B2")

    ChrTalk(
        0x9,
        (
            "#1003FEstelle and Joshua Bright, eh?\x02\x03",
            "#1002FThey seem to have quite the history,\x01",
            "those two.\x02\x03",
            "Remember: if you don't work quickly,\x01",
            "the guild is bound to get involved.\x02\x03",
            "#1004FAnd if that doesn't sound appealing,\x01",
            "you'll just have to work harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0111F(...Is he trying to encourage us? I can't\x01",
            "quite tell.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1A31")

    label("loc_19B2")


    ChrTalk(
        0x9,
        (
            "#1004FRemember: if you don't work quickly,\x01",
            "the guild is bound to get involved.\x02\x03",
            "#1002FWell, break a leg. Hell, maybe two.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A31")

    Jump("loc_2184")

    label("loc_1A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1A44")
    Jump("loc_2184")

    label("loc_1A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1D14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C66")
    SetChrSubChip(0x9, 0x0)

    ChrTalk(
        0x9,
        "#1003F*sigh* Nothing beats an early smoke...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B36")
    Jump("loc_1B80")

    label("loc_1B36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B56")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B80")

    label("loc_1B56")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B76")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B80")

    label("loc_1B76")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B80")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(
        0x9,
        (
            "#1005FSo, you already heard what's what?\x02\x03",
            "#1004FIf so, stop dilly-dallying and do your best.\x01",
            "At least do enough that you don't piss off\x01",
            "the vice commissioner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FYes, sir.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1D0F")

    label("loc_1C66")


    ChrTalk(
        0x9,
        (
            "#1002FI don't know the details, but the case is related\x01",
            "to the Guardian Force, right?\x02\x03",
            "If you fail to deliver, I can't save you from the\x01",
            "vice commissioner's wrath.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0F")

    Jump("loc_2184")

    label("loc_1D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1E98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3F")

    ChrTalk(
        0x9,
        (
            "#1000FHead over to the law office on West Street.\x02\x03",
            "I've told the lawyer who runs the place\x01",
            "about our new division here. He should\x01",
            "be willing to lend an ear.\x02\x03",
            "#1003FPay attention to what he says. Might have\x01",
            "some useful info for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FNo pep talk, eh, Chief?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1E93")

    label("loc_1E3F")


    ChrTalk(
        0x9,
        (
            "#1003FJust pay attention to what he says. Might\x01",
            "have some useful info for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E93")

    Jump("loc_2184")

    label("loc_1E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_END)), "loc_2031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC8")

    ChrTalk(
        0x9,
        (
            "#1005FWhat's with you guys? Didn't I tell you to\x01",
            "check out the Downtown District?\x02\x03",
            "#1003FDon't forget that you're still rookies.\x01",
            "Complete support requests, and who knows?\x01",
            "An urgent investigation might come your way.\x02\x03",
            "#1000FSo, make sure you keep your priorities straight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_202C")

    label("loc_1FC8")


    ChrTalk(
        0x9,
        (
            "#1003FCheck out the Downtown District ASAP.\x02\x03",
            "#1000FI still don't know what's going on, either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202C")

    Jump("loc_2184")

    label("loc_2031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2184")

    ChrTalk(
        0x9,
        (
            "#1003FTaking care of smaller support requests is the\x01",
            "Special Support Section's job.\x02\x03",
            "#1000FIt's up to you whether you complete them or not,\x01",
            "but at least head to the police department later.\x02\x03",
            "And if you want to learn about fine-tuning your\x01",
            "Enigmas, you should stop by the orbal store, too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2184")

    ChrTalk(
        0x101,
        "#0000FRoger that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2184")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)

    label("loc_218B")

    Return()

    # Function_3_B0A end

    def Function_4_218C(): pass

    label("Function_4_218C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_21A0")
    Call(1, 5)
    Jump("loc_2517")

    label("loc_21A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2369")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2311")

    ChrTalk(
        0xA,
        "#1110FEveryone! Welcome back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FHaha. You two could almost pass\x01",
            "as sisters, couldn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1109FHehehe.\x02\x03",
            "#1110FDo you have to go to work now, guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FYeah, we do. We'll be back soon enough,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202FWe will cook a big dinner together when\x01",
            "we get back, okay? Shizuku can join us, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1109FAwesome!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2364")

    label("loc_2311")

    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xA,
        (
            "#1100FLook! If you pet him right here, he wags\x01",
            "his big, fluffy tail...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2364")

    Jump("loc_2517")

    label("loc_2369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_23EA")

    ChrTalk(
        0xFE,
        (
            "#1104FHmmmm hmmm hmm. ♪ Putting away\x01",
            "dishes! Hmmmm hmmm hmm. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(She's really getting into this.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_23EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2517")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B1")
    OP_93(0xFE, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "KeA is in the kitchen, cleaning up after breakfast.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xA,
        (
            "#1100FIf you figure something out, you better\x01",
            "tell me, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FHaha. Will do, KeA.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2517")

    label("loc_24B1")


    ChrTalk(
        0xA,
        (
            "#1104FCleeeaning, cleeeeeaning! ♪\x02\x03",
            "#1110FIf you figure out something, you better\x01",
            "tell me, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2517")

    TalkEnd(0xFE)
    Return()

    # Function_4_218C end

    def Function_5_251B(): pass

    label("Function_5_251B")

    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xF, 0xE1, 0x0)
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "#6005FOh, you were right! His coat is so soft\x01",
            "and cuddly...\x02\x03",
            "#6000FI'm Shizuku. It's nice to meet you, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#1200FGrrrrr, grrrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1110FUmmm...\x02\x03",
            "#1109FHe said, 'Kids aren't half bad when they\x01",
            "are as polite as you.'\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D7")

    ChrTalk(
        0x102,
        (
            "#0108F(We probably shouldn't let KeA and Shizuku\x01",
            "know about the current situation...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Yeah. We can let Zeit watch over them\x01",
            "while we hurry to the hospital.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_26D7")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_5_251B end

    def Function_6_26E0(): pass

    label("Function_6_26E0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2774")
    Jump("loc_27BE")

    label("loc_2774")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2794")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27BE")

    label("loc_2794")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27B4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27BE")

    label("loc_27B4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27BE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_27F1")
    Jump("loc_2E3F")

    label("loc_27F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A53")

    ChrTalk(
        0xB,
        "#1105FHuh? Who's this angry-looking guy?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2876")
    OP_63(0x10A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2876")


    ChrTalk(
        0x10A,
        (
            "#0603FE-Excuse me? I'm in a perfectly fine\x01",
            "mood, thank you very much.\x02\x03",
            "#0600FAnd my name is Dudley! Could you\x01",
            "at least remember that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1109FYep! I'll never forget! Nice to\x01",
            "meet'cha, Dudley!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2964")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2964")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_298A")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_298A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29B0")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_29B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29D6")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_29D6")

    Sleep(1000)

    ChrTalk(
        0x10A,
        (
            "#0603F(Hey. You guys should try to teach her\x01",
            "to show some manners to her seniors.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(W-We'll try.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2A87")

    label("loc_2A53")


    ChrTalk(
        0xB,
        "#1110FGood luck today, guys! You, too, Dudley!\x02",
    )

    CloseMessageWindow()

    label("loc_2A87")

    Jump("loc_2E3F")

    label("loc_2A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDD")

    ChrTalk(
        0x103,
        "#0202FYou were here all along, KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0302FOh? That's a library book, ain't it? You go\x01",
            "check out some books while we were out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1100FI already had this one checked out! So, I\x01",
            "thought I might as well finish reading it.\x02\x03",
            "#1109FWell, good luck today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks. We'll try to get home early.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2BFC")

    label("loc_2BDD")


    ChrTalk(
        0xB,
        "#1110FDo your best, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_2BFC")

    Jump("loc_2E3F")

    label("loc_2C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2E3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E17")

    ChrTalk(
        0xB,
        "#1105FAw, guys... Do you have to leave again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FSorry, KeA. We've got something to take care\x01",
            "of. We'll be back by evening, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FWant us to buy a souvenir while\x01",
            "we're out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1111FWell, no. You don't have to do that.\x02\x03",
            "#1109FComing home safe is good enough\x01",
            "for me!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0012FKeA...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0109FM-My heart...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0204FHer smile has pierced my very soul.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0302FHaha. The grim atmosphere ran away\x01",
            "at the first sight of her smile.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)

    ChrTalk(
        0xB,
        "#1100FHuh?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 6)
    Jump("loc_2E3F")

    label("loc_2E17")


    ChrTalk(
        0xB,
        "#1110FHave a good day! Be careful!\x02",
    )

    CloseMessageWindow()

    label("loc_2E3F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_26E0 end

    def Function_7_2E47(): pass

    label("Function_7_2E47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_2E5B")
    Call(1, 5)
    Jump("loc_3455")

    label("loc_2E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2E7E")

    ChrTalk(
        0xFE,
        "#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3455")

    label("loc_2E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2F53")

    ChrTalk(
        0xFE,
        "#1200FGrrrrrrrrr...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EE4")
    OP_63(0x10A, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4E")

    ChrTalk(
        0x10A,
        (
            "#0606F(They're treating him like a police dog?)\x02\x03",
            "#0610F(Isn't this a bit much, Sergei?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_2F4E")

    Jump("loc_3455")

    label("loc_2F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD9")

    ChrTalk(
        0xFE,
        "#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202FWe are glad to have you on the\x01",
            "team, too, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1203FGrrrrr... Woof!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2FF2")

    label("loc_2FD9")


    ChrTalk(
        0xFE,
        "#1200FGrrrrrrrrr...\x02",
    )

    CloseMessageWindow()

    label("loc_2FF2")

    Jump("loc_3455")

    label("loc_2FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_311E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3104")

    ChrTalk(
        0xFE,
        "#1203FGrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202F'As long as I am here, this place is nigh untouchable.'\x01",
            "He would seem to be boasting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYou're invaluable, Zeit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FS'pose we'll have to reward him with\x01",
            "a slab of meat or somethin' after this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3119")

    label("loc_3104")


    ChrTalk(
        0xFE,
        "#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    label("loc_3119")

    Jump("loc_3455")

    label("loc_311E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3246")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322C")

    ChrTalk(
        0xFE,
        "#1200FGrrrrrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Proud as always, but there's no doubt\x01",
            "that he's one of us. A vigilant protector\x01",
            "of the Special Support Section.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202F(Agreed. I imagine he will eviscerate any\x01",
            "suspicious characters that dare enter.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3241")

    label("loc_322C")


    ChrTalk(
        0xFE,
        "#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    label("loc_3241")

    Jump("loc_3455")

    label("loc_3246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_3254")
    Jump("loc_3455")

    label("loc_3254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3262")
    Jump("loc_3455")

    label("loc_3262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337E")

    ChrTalk(
        0x153,
        (
            "#1110FZeit, we're going to leave for a bit!\x02\x03",
            "#1109FYou be a good boy and watch the\x01",
            "house, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3334")

    ChrTalk(
        0x103,
        (
            "#0202F'No soul shall enter while I sit vigil.\x01",
            "Go now.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3334")


    ChrTalk(
        0x101,
        (
            "#0012FHahaha... Sounds like we've got\x01",
            "the green light, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3393")

    label("loc_337E")


    ChrTalk(
        0xFE,
        "#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    label("loc_3393")

    Jump("loc_3455")

    label("loc_3398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_33F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_33C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 5)), scpexpr(EXPR_END)), "loc_33BE")
    Call(1, 8)
    Jump("loc_33C1")

    label("loc_33BE")

    Call(1, 19)

    label("loc_33C1")

    Jump("loc_33F2")

    label("loc_33C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_33DB")
    Call(1, 17)
    Jump("loc_33F2")

    label("loc_33DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_33EF")
    Call(1, 16)
    Jump("loc_33F2")

    label("loc_33EF")

    Call(1, 8)

    label("loc_33F2")

    Jump("loc_3455")

    label("loc_33F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3455")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_343D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 5)), scpexpr(EXPR_END)), "loc_3435")

    ChrTalk(
        0xFE,
        "#1200FGrrrrr... Woof!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3438")

    label("loc_3435")

    Call(1, 19)

    label("loc_3438")

    Jump("loc_3455")

    label("loc_343D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3452")
    Call(1, 17)
    Jump("loc_3455")

    label("loc_3452")

    Call(1, 16)

    label("loc_3455")

    TalkEnd(0xFE)
    Return()

    # Function_7_2E47 end

    def Function_8_3459(): pass

    label("Function_8_3459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36B7")
    EventBegin(0x0)
    Fade(500)
    OP_68(3640, 1000, 5390, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(23630, 0)
    SetChrPos(0x101, 2060, 0, 5360, 90)
    SetChrPos(0x102, 2250, 0, 6760, 135)
    SetChrPos(0x103, 3500, 30, 4350, 0)
    SetChrPos(0x104, 4770, 30, 6030, 270)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    BeginChrThread(0xD, 1, 0, 0)
    OP_0D()

    ChrTalk(
        0xD,
        "#1200F#5PGrrrrr?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204F#12PYes. We must leave for a bit.\x02\x03",
            "#0202FThings could become dangerous, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#1203F#5PGrrrrr... Grrrrr woof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F#6PUh, Tio? What'd he say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202F#12PHe says that he knows we are searching\x01",
            "for something.\x02\x03",
            "#0204F'Worry not. I can help you,' he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309F#11PDependable as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102F#5PIndeed. When the going gets tough,\x01",
            "Zeit never fails to help us out.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 3500, 30, 4350, 0)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0x8E, 4)
    EventEnd(0x5)
    Jump("loc_377A")

    label("loc_36B7")


    ChrTalk(
        0xFE,
        "#1203FGrrrrr... Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206F'Go with haste. Your speed is, sadly,\x01",
            "not one of your strengths.'\x02\x03",
            "#0200FBad dog.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_377A")

    Return()

    # Function_8_3459 end

    def Function_9_377B(): pass

    label("Function_9_377B")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_378F")
    Call(1, 5)
    Jump("loc_391F")

    label("loc_378F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_391F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38ED")
    TurnDirection(0xF, 0x0, 0)

    ChrTalk(
        0xF,
        "#6005FOh, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FSorry. We have to step out for a bit.\x02\x03",
            "Could we leave KeA and Zeit to you,\x01",
            "Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6000FOf course.\x02\x03",
            "I'm having so much fun playing\x01",
            "with them anyway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FWell, it's your day off, ain't it? I say\x01",
            "you play till you drop, Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#6002FHeehee. We will.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xF, 0xE1, 0x0)
    Jump("loc_391F")

    label("loc_38ED")


    ChrTalk(
        0xF,
        "#6001FC-Can I really pet him? *heart pounds*\x02",
    )

    CloseMessageWindow()

    label("loc_391F")

    TalkEnd(0xF)
    Return()

    # Function_9_377B end

    def Function_10_3923(): pass

    label("Function_10_3923")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A7C")

    ChrTalk(
        0x10,
        (
            "#0100FOh, KeA! How's your first trip into the\x01",
            "city been going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1109FIt's been SO much fun! I wish you could've\x01",
            "come, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#0109FWell, today was my turn to look\x01",
            "after the office.\x02\x03",
            "#0102FHow about this, KeA? Want to go walk\x01",
            "around the city together next time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FI'd love that! It's a promise, okay?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3B9C")

    label("loc_3A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3AF1")

    ChrTalk(
        0x10,
        (
            "#0100FLloyd, Tio, please take care.\x02\x03",
            "We can't afford for Revache to catch\x01",
            "on to what we're doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B63")

    label("loc_3AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3B63")

    ChrTalk(
        0x10,
        (
            "#0100FLloyd, Randy, please take care.\x02\x03",
            "We can't afford for Revache to catch\x01",
            "on to what we're doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B63")


    ChrTalk(
        0x101,
        "#0000FOf course. We'll be extra careful, I promise.\x02",
    )

    CloseMessageWindow()

    label("loc_3B9C")

    TalkEnd(0xFE)
    Return()

    # Function_10_3923 end

    def Function_11_3BA0(): pass

    label("Function_11_3BA0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C34")
    Jump("loc_3C7E")

    label("loc_3C34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C54")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C7E")

    label("loc_3C54")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C74")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C7E")

    label("loc_3C74")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C7E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E58")

    ChrTalk(
        0x11,
        "#0200FI thought you were going out, KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FI did, but I came back to see you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0205F...\x02\x03",
            "#0204FKeA is too cute. Can I please cuddle\x01",
            "with her? Just for a little while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012F(Haha...)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3DF1")

    ChrTalk(
        0x102,
        (
            "#0102F(Honestly, I totally understand where\x01",
            "Tio's coming from. KeA's hugs are a\x01",
            "magical thing.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E50")

    label("loc_3DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3E50")

    ChrTalk(
        0x104,
        (
            "#0309F(Who knew our cool, collected Tio Tot would\x01",
            "get so attached to the kiddo?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E50")

    SetScenarioFlags(0x1, 1)
    Jump("loc_3EBF")

    label("loc_3E58")


    ChrTalk(
        0x11,
        (
            "#0202FWatch out for cars, okay? And make sure\x01",
            "you stay by the two of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FOkie dokie!\x02",
    )

    CloseMessageWindow()

    label("loc_3EBF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_3BA0 end

    def Function_12_3EC7(): pass

    label("Function_12_3EC7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F5B")
    Jump("loc_3FA5")

    label("loc_3F5B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F7B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FA5")

    label("loc_3F7B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F9B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FA5")

    label("loc_3F9B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FA5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A1")

    ChrTalk(
        0x153,
        "#1110FRandy, we're going to leave now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0302FHeck yeah! Keep that pep in your step!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_40E3")

    ChrTalk(
        0x12,
        (
            "#0300FLloyd, Mademois-Elie. I'm leavin' this rascal\x01",
            "in your hands, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FShe's safe with us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWe'll try not to stay out for too long.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4199")

    label("loc_40E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4199")

    ChrTalk(
        0x12,
        (
            "#0300FLloyd, Tio Tot. I'm leavin' this rascal in\x01",
            "your hands, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FShe's safe with us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202FWe intend to stick to our charted course\x01",
            "and be back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4199")

    SetScenarioFlags(0x1, 2)
    Jump("loc_42B5")

    label("loc_41A1")


    ChrTalk(
        0x12,
        (
            "#0303FHeh. Think I might hit up the latest\x01",
            "edition of Hot Shot while you're out.\x02\x03",
            "#0309FBeen a lil' on edge this last week. Haven't\x01",
            "been able to relax, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Randy, you can't just talk about your glorified\x01",
            "smut magazines in front of KeA...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1105F...?\x02",
    )

    CloseMessageWindow()

    label("loc_42B5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_3EC7 end

    def Function_13_42BD(): pass

    label("Function_13_42BD")

    EventBegin(0x0)
    Fade(500)
    OP_68(63930, 1330, 8550, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 65489, 0, 8029, 315)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#1005FDudley? Any particular reason for your\x01",
            "visit?\x02\x03",
            "#1001FWe got a problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0601FNo, nothing urgent. A certain team beat me\x01",
            "to the punch, that's all.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Dudley quickly explained the circumstances\x01",
            "surrounding Revache & Co.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1001F...\x02\x03",
            "#1003FWhat a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603FThat's an understatement. At any rate, I'm\x01",
            "investigating Revache with your rookies.\x02\x03",
            "#0600FSergei, the top brass...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FHell, I bet anything they aren't expectin' a\x01",
            "damn thing.\x02\x03",
            "#0301FThe timing of the airport bomb threat was\x01",
            "way too good to be a coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FChief? Could you do us a favor and cover\x01",
            "for us again, like you usually do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1004FNo problem. I'll come up with something.\x02\x03",
            "#1002FBut, Lloyd, you DO realize that screwing with\x01",
            "them now is like playing with fire. Do you really\x01",
            "think deception is the right call?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FIt's our only option right now. All we need\x01",
            "is a little bit of time, Chief.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0xE1, 0x1F4)

    ChrTalk(
        0x10A,
        (
            "#0610FA-Are you serious? You're under MY command,\x01",
            "and you're still asking Sergei for help? We don't\x01",
            "need to involve anyone other than...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0204FIt is too late for any elaborate plans.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1004FHeh. Sorry, Dudley. This is just how the\x01",
            "Special Support Section operates.\x02\x03",
            "#1000FAnyway, hurry up. Things are going to\x01",
            "Gehenna in a handbasket.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 64000, 30, 7000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xCC, 4)
    EventEnd(0x5)
    Return()

    # Function_13_42BD end

    def Function_14_4881(): pass

    label("Function_14_4881")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(254990, 1300, 67290, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x101, 251150, 0, 65900, 90)
    SetChrPos(0xEF, 249150, 0, 65900, 90)
    SetChrPos(0x153, 250150, 0, 65500, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetCameraDistance(25000, 3000)
    FadeToBright(500, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 1, 15)
    Sleep(500)
    BeginChrThread(0x153, 3, 1, 15)
    Sleep(500)
    BeginChrThread(0xEF, 3, 1, 15)
    Sleep(500)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x153, 3)

    ChrTalk(
        0x101,
        (
            "#0005FLooks like you've already settled in to\x01",
            "your new room.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4A30")

    ChrTalk(
        0x153,
        (
            "#1109F#6PI still gotta show you all the\x01",
            "pretty clothes I can wear!\x02\x03",
            "#1110FElie and Tio went and bought me a ton\x01",
            "of cute clothes and stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AC0")

    label("loc_4A30")


    ChrTalk(
        0x153,
        (
            "#1109F#6PI still gotta show you all the\x01",
            "pretty clothes I can wear!\x02\x03",
            "#1110FElie and Tio went and bought me a ton\x01",
            "of cute clothes and stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AC0")


    def lambda_4AC5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4AC5)
    Sleep(50)

    def lambda_4AD5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AD5)
    Sleep(250)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4C11")

    ChrTalk(
        0x102,
        (
            "#0105F#6PGood idea, KeA.\x02\x03",
            "#0109FI still want to have a little more fun\x01",
            "planning all of your outfits...like this\x01",
            "blouse, for example!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011FN-No, that's fine. Can we save it for\x01",
            "a cloudy day? We've got some work\x01",
            "to take care of.\x02\x03",
            "#0012F(Besides, we'd probably be here for\x01",
            "hours...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E64")

    label("loc_4C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4D70")

    ChrTalk(
        0x103,
        (
            "#0205F#6PFantastic idea, KeA.\x02\x03",
            "#0204FI think planning and showing off some of your\x01",
            "outfits could be quite entertaining... Like, that\x01",
            "knit cap would look incredibly cute on you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011FN-No, that's fine. Can we save it for\x01",
            "a cloudy day? We've got some work\x01",
            "to take care of.\x02\x03",
            "#0012F(Besides, we'd probably be here for\x01",
            "hours...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E64")

    label("loc_4D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4E64")

    ChrTalk(
        0x104,
        (
            "#0309F#6PHey, we'll make an entire show out of it.\x02\x03",
            "#0300FBut yeah, we should definitely save\x01",
            "that for another time.\x02\x03",
            "#0306FKnowin' Tio Tot and Elie, they're gonna\x01",
            "go all out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FHaha, it'll be something, that's for sure.\x02",
    )

    CloseMessageWindow()

    label("loc_4E64")

    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0000FStill, this room turned out pretty well.\x02\x03",
            "Cleaning and dusting everything took a long\x01",
            "time, but the furniture Elie found looks great.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F18():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4F18)
    Sleep(200)

    def lambda_4F28():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_4F28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_50DA")

    ChrTalk(
        0x102,
        (
            "#0102F#12PDoesn't it? Not bad for mainly being\x01",
            "old things from my home.\x02\x03",
            "#0106FI do feel a little bad, though. This was\x01",
            "my parents' furniture, so it's all much\x01",
            "too big for little KeA...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FFD():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FFD)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#0002FDon't worry about it. They're perfect.\x02\x03",
            "#0004F(Though, once we figure out KeA's\x01",
            "identity, we'll have to send her back\x01",
            "to her parents...)\x02\x03",
            "(But until then, I want to make KeA\x01",
            "feel at home here.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_540F")

    label("loc_50DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_5278")

    ChrTalk(
        0x103,
        (
            "#0202F#12PThese were apparently old furnishings\x01",
            "from Elie's house.\x02\x03",
            "#0204FAlthough, KeA is a bit too tiny for furniture\x01",
            "intended for adults. It should not pose any\x01",
            "issues in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_51A9():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51A9)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#0002FThey look good, I think!\x02\x03",
            "#0004F(Though, once we figure out KeA's\x01",
            "identity, we'll have to send her back\x01",
            "to her parents...)\x02\x03",
            "(But until then, I want to make KeA\x01",
            "feel at home here.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_540F")

    label("loc_5278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_540F")

    ChrTalk(
        0x104,
        (
            "#0300F#12PMademois-Elie apparently pulled some strings\x01",
            "to get her old furniture moved over here.\x02\x03",
            "#0309FThey might be a lil' big for KeDo here, but I'm\x01",
            "willing to bet that she doesn't mind.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5349():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5349)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#0002FYeah, I suppose not.\x02\x03",
            "#0004F(Though, once we figure out KeA's identity,\x01",
            "we'll have to send her back to her parents...)\x02\x03",
            "(But until then, I want to make KeA feel at\x01",
            "home here.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_540F")

    SetChrPos(0x0, 255350, 0, 64650, 0)
    SetScenarioFlags(0xD8, 6)
    EventEnd(0x5)
    Return()

    # Function_14_4881 end

    def Function_15_5426(): pass

    label("Function_15_5426")


    def lambda_542B():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_542B)

    def lambda_5445():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5445)
    WaitChrThread(0xFE, 1)

    def lambda_545A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_545A)
    Return()

    # Function_15_5426 end

    def Function_16_5463(): pass

    label("Function_16_5463")


    ChrTalk(
        0x101,
        (
            "#0000FThere he is.\x02\x03",
            "So, should we try asking for Zeit's help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYes. With Zeit's nose, following the vice commissioner's\x01",
            "trail should be quick and painless. Accurate, too.\x02\x03",
            "We should explain the situation to him and ask if he is\x01",
            "willing to cooperate.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("apl/ch50116.itc", 0x1E)
    OP_68(2940, 1200, 4980, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(24570, 0)
    SetChrPos(0x101, 2250, 30, 5500, 90)
    SetChrPos(0x102, 2500, 30, 6850, 135)
    SetChrPos(0x103, 3500, 30, 4500, 0)
    SetChrPos(0x104, 3000, 30, 3150, 0)
    OP_93(0xD, 0xB4, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Special Support Section informed Zeit of the request\x01",
            "and asked if he would lend a paw.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#0003FAnd so, we're really hoping that you'd\x01",
            "help us out with the support request...\x02\x03",
            "#0012FUh, Zeit? Did you hear a word I just\x01",
            "said?\x02",
        )
    )

    CloseMessageWindow()
    Sound(848, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_A1(0xD, 0x4E2, 0x8, 0x0, 0x1, 0x1, 0x1, 0x1, 0x2, 0x3, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#11P#1200FGrrrrr...\x02\x03",
            "Grrrrr... Woof!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 1, 0, 0)

    ChrTalk(
        0x104,
        "#12P#0305FThat a yes or a no?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FMaybe he's not interested.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#12P#0200FNo, he is simply being...difficult.\x02\x03",
            "#0203F'Ever the disappointing lot...'\x01",
            "Despite his grumbling, I believe\x01",
            "he plans to assist us.\x02\x03",
            "#0200FLloyd, would you please show Zeit the\x01",
            "handkerchief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FSure thing. Here you go, boy.\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 2900, 850, 5000, 2000, 0x0)
    Sleep(500)
    OP_96(0x101, 0x8CA, 0x0, 0x157C, 0x7D0, 0x0)

    def lambda_58C9():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58C9)

    def lambda_58D6():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58D6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x103,
        (
            "#12P#0200FThis is our target's scent.\x02\x03",
            "Got it?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x2)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xC, 0x1)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#5P#1203F*sniff* *sniff*\x02\x03",
            "#1200FGrrrrr...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200F'What an unpleasant smell.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P#1200FGrrrrr... Woof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200F'Considering how hopeless you are, I shall help.\x01",
            "Talk to me when you are prepared to leave.'\x01",
            "...I believe that means he is in.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xC, 0x1)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12P#0306FDamn. Zeit really sounds like an old man,\x01",
            "doesn't he? Learn to relax, dude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FConducting a search with a police\x01",
            "dog... We're proper police officers\x01",
            "now, aren't we?\x02\x03",
            "This search might take some time,\x01",
            "so let's prepare beforehand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FSounds like a plan.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_68(3500, 1030, 4500, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 3500, 0, 4500, 0)
    SetChrPos(0x1, 3500, 0, 4500, 0)
    SetChrPos(0x2, 3500, 0, 4500, 0)
    SetChrPos(0x3, 3500, 0, 4500, 0)
    OP_29(0x15, 0x1, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_16_5463 end

    def Function_17_5BFD(): pass

    label("Function_17_5BFD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E77")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Ask for help\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5C66"),
        (1, "loc_5D1E"),
        (SWITCH_DEFAULT, "loc_5E72"),
    )


    label("loc_5C66")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xD,
        (
            "#1200FGrrrrr...\x01",
            "Grrrrrrrrr...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F'If you desire the wedding ring or whatever\x01",
            "foolishness it is, just ask me.'\x02\x03",
            "'In the meantime, I will tail you,' he says.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E72")

    label("loc_5D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_5D7F")

    ChrTalk(
        0x101,
        (
            "#0000FAll right, then. Our first stop will be the\x01",
            "Entertainment District!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E43")

    label("loc_5D7F")


    ChrTalk(
        0x101,
        (
            "#0000FAll right, then. Our first stop will be the\x01",
            "Entertainment District!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThe vice commissioner claimed he still had it\x01",
            "when he left the casino, so our best bet is to\x01",
            "start there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E43")

    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    AddParty(0x1B, 0xFF, 0xFF)
    SetScenarioFlags(0x93, 6)
    OP_C7(0x0, 0x1000)
    SetScenarioFlags(0x5C, 5)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Jump("loc_5E72")

    label("loc_5E72")

    Jump("loc_5C07")

    label("loc_5E77")

    Return()

    # Function_17_5BFD end

    def Function_18_5E78(): pass

    label("Function_18_5E78")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    RemoveParty(0x1B, 0x0)
    ClearScenarioFlags(0x93, 6)
    OP_C7(0x1, 0x1000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(3500, 1030, 4500, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 3500, 0, 4500, 0)
    SetChrPos(0x1, 3500, 0, 4500, 0)
    SetChrPos(0x2, 3500, 0, 4500, 0)
    SetChrPos(0x3, 3500, 0, 4500, 0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x4)
    Return()

    # Function_18_5E78 end

    def Function_19_5F17(): pass

    label("Function_19_5F17")


    ChrTalk(
        0x101,
        (
            "#0000FThanks for all your help today, Zeit. I'll\x01",
            "never underestimate your nose again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYes. He is our irreplaceable police dog.\x02\x03",
            "Good boy. We will make sure to ask you for\x01",
            "help whenever we need to find evidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#1200FWoof! Grrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F'Try to provide me with an\x01",
            "actual challenge next time.'\x01",
            "...He is boasting again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FHe really thinks he's all that, don't he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FTo be fair, he probably put in more effort on\x01",
            "this request than we did.\x02\x03",
            "Okay, Zeit. From now on, we'll be counting\x01",
            "on that keen nose of yours.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 5)
    Return()

    # Function_19_5F17 end

    def Function_20_6145(): pass

    label("Function_20_6145")

    EventBegin(0x0)
    Fade(500)
    OP_68(15900, 1550, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 14100, 850, 9500, 45)
    SetChrPos(0x104, 15600, 850, 8000, 45)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0000F#6PSo, all we have to do is use this terminal\x01",
            "and report our progress to headquarters,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202F#6PThat is correct. We should try testing it.\x02",
    )

    CloseMessageWindow()
    OP_E3(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()

    label("loc_627B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68B8")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_62AE"),
        (1, "loc_62D4"),
        (255, "loc_6806"),
        (SWITCH_DEFAULT, "loc_68B3"),
    )


    label("loc_62AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_62CA")
    OP_2B(0x1, 0x2, 0x3, 0x35, 0xFFFF)
    Jump("loc_62CF")

    label("loc_62CA")

    OP_2B(0x1, 0xFFFF)

    label("loc_62CF")

    Jump("loc_68B3")

    label("loc_62D4")

    SetMapFlags(0x40000000)
    OP_E3(0x7)
    Sleep(500)
    SetChrName("Receptionist Fran")
    Sound(2062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Hello, you've reached the CPD. This is Fran speaking!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_6568")
    Sound(2067, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "As always, we appreciate your hard work!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_64EE")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_63A1"),
        (13, "loc_63D8"),
        (12, "loc_6408"),
        (SWITCH_DEFAULT, "loc_6436"),
    )


    label("loc_63A1")

    Sound(2075, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "1st Class... You're phenomenal, Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6464")

    label("loc_63D8")

    Sound(2074, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "2nd Class... Great work, Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6464")

    label("loc_6408")

    Sound(2073, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "3rd Class... Good job, Lloyd.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6464")

    label("loc_6436")

    Sound(2073, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "3rd Class... Good job, Lloyd.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6464")

    label("loc_6464")

    Sound(2076, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "I'll make sure your bonuses get transferred to you immediately!\x02",
    )

    CloseMessageWindow()
    Sound(2077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Thank you, and please keep up the good work!\x07\x00\x02",
    )

    CloseMessageWindow()
    Jump("loc_6560")

    label("loc_64EE")

    Sound(2078, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Thanks for the report, everyone.\x02",
    )

    CloseMessageWindow()
    Sound(2079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "If you finish more support requests, please let me know!\x07\x00\x02",
    )

    CloseMessageWindow()

    label("loc_6560")

    SetScenarioFlags(0x1, 5)
    Jump("loc_668E")

    label("loc_6568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_6616")
    Sound(2063, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Hello again! Did you forget or something?\x02",
    )

    CloseMessageWindow()
    Sound(2064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "You already submitted your report to me, so\x01",
            "call me when you complete more requests!\x01",
            "Bye-bye!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668E")

    label("loc_6616")

    Sound(2065, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
        "Hi, everyone! It seems there's nothing you\x01",
        "have to report now.\x02",
        )
    )

    CloseMessageWindow()
    Sound(2066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "When you do, please let me know!\x07\x00\x02",
    )

    CloseMessageWindow()

    label("loc_668E")

    OP_57(0x0)
    OP_E3(0x8)
    ClearMapFlags(0x40000000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6801")
    Sleep(1000)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0002FIt only took a moment to send our report.\x01",
            "Talk about efficient.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#0109FFrom here on out, I assume we'll be reporting\x01",
            "finished support requests in the same manner.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(824, 0, 100, 0)
    Sleep(1000)

    AnonymousTalk(
        0x103,
        (
            "#0205FAnother update? It appears that more requests\x01",
            "have already been added to our system.\x02\x03",
            "#0202FWe should verify each one, just to be safe.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1, 0x1, 0x2)

    label("loc_6801")

    Jump("loc_68B3")

    label("loc_6806")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68AE")

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0203FIt appears that more requests have already\x01",
            "come in.\x02\x03",
            "#0200FWe should verify each one, just to be safe.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68AE")

    Jump("loc_68B3")

    label("loc_68B3")

    Jump("loc_627B")

    label("loc_68B8")

    OP_E3(0x6)
    FadeToBright(300, 0)
    OP_0D()
    OP_E3(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_68DB")
    Call(1, 21)
    Jump("loc_68DD")

    label("loc_68DB")

    EventEnd(0x5)

    label("loc_68DD")

    Return()

    # Function_20_6145 end

    def Function_21_68DE(): pass

    label("Function_21_68DE")

    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#0301F#12PWhew, that's a lot. More monsters in\x01",
            "the Geofront, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FSo, this is an extermination request?\x02\x03",
            "From what I've heard, those are usually\x01",
            "handled by the Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0003F#5PHear me out, guys.\x02\x03",
            "#0001FWhy don't we take care of this\x01",
            "extermination ourselves?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6A60():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A60)
    Sleep(50)

    def lambda_6A70():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6A70)
    Sleep(50)

    def lambda_6A80():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A80)
    Sleep(300)

    ChrTalk(
        0x102,
        "#0105FAre you inferring...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305F#12PLookin' for a bit of redemption, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F#5PSomething like that. It was because\x01",
            "of Arios MacLaine that we came out\x01",
            "unscathed last time.\x02\x03",
            "#0001FIf we had time to prepare, I genuinely\x01",
            "believe that we could have handled it\x01",
            "ourselves.\x02\x03",
            "Besides, today's our first official day\x01",
            "on the job...so why not start off with\x01",
            "a bang?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0103FYou make a compelling argument...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204F#6PIt seems unnecessary,\x01",
            "but your logic is sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304F#12PI like the way you think, Lloyd!\x01",
            "We better start repairing our\x01",
            "already-rocky image, y'know?\x02\x03",
            "#0300FNow that we've got a plan,\x01",
            "I guess we should head to the\x01",
            "Geofront when we're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#5PYeah!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Among the support requests, there are some\x01",
            "that are higher priority and mandatory.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "These are marked as 'urgent' and, when completed,\x01",
            "the story will advance.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Other support requests are not mandatory.\x01",
            "Please pay attention to them, however.\x01",
            "They have time limits and will expire if ignored.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(15730, 1850, 9350, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 15730, 850, 9350, 225)
    SetChrPos(0x1, 15730, 850, 9350, 225)
    SetChrPos(0x2, 15730, 850, 9350, 225)
    SetChrPos(0x3, 15730, 850, 9350, 225)
    OP_29(0x3D, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_21_68DE end

    def Function_22_6F20(): pass

    label("Function_22_6F20")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    OP_68(-1560, 1330, 122920, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F78")
    SetChrFlags(0x0, 0x8)

    label("loc_6F78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F8B")
    SetChrFlags(0x1, 0x8)

    label("loc_6F8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F9E")
    SetChrFlags(0x2, 0x8)

    label("loc_6F9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FB1")
    SetChrFlags(0x3, 0x8)

    label("loc_6FB1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FC4")
    SetChrFlags(0x4, 0x8)

    label("loc_6FC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FD7")
    SetChrFlags(0x5, 0x8)

    label("loc_6FD7")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1830, 30, 122400, 270)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0000FThis looks good, right?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Lloyd's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x50, 6)
    OP_66(0x7, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_707E")
    ClearChrFlags(0x0, 0x8)

    label("loc_707E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7091")
    ClearChrFlags(0x1, 0x8)

    label("loc_7091")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70A4")
    ClearChrFlags(0x2, 0x8)

    label("loc_70A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70B7")
    ClearChrFlags(0x3, 0x8)

    label("loc_70B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70CA")
    ClearChrFlags(0x4, 0x8)

    label("loc_70CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70DD")
    ClearChrFlags(0x5, 0x8)

    label("loc_70DD")

    Call(1, 39)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_22_6F20 end

    def Function_23_70F4(): pass

    label("Function_23_70F4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    OP_68(-2440, 1300, 129810, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_714C")
    SetChrFlags(0x0, 0x8)

    label("loc_714C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_715F")
    SetChrFlags(0x1, 0x8)

    label("loc_715F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7172")
    SetChrFlags(0x2, 0x8)

    label("loc_7172")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7185")
    SetChrFlags(0x3, 0x8)

    label("loc_7185")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7198")
    SetChrFlags(0x4, 0x8)

    label("loc_7198")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71AB")
    SetChrFlags(0x5, 0x8)

    label("loc_71AB")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1940, 0, 128820, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0000FThat looks good, right?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Lloyd's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x50, 7)
    OP_66(0x8, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7252")
    ClearChrFlags(0x0, 0x8)

    label("loc_7252")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7265")
    ClearChrFlags(0x1, 0x8)

    label("loc_7265")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7278")
    ClearChrFlags(0x2, 0x8)

    label("loc_7278")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_728B")
    ClearChrFlags(0x3, 0x8)

    label("loc_728B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_729E")
    ClearChrFlags(0x4, 0x8)

    label("loc_729E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72B1")
    ClearChrFlags(0x5, 0x8)

    label("loc_72B1")

    Call(1, 39)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_23_70F4 end

    def Function_24_72C8(): pass

    label("Function_24_72C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "05", 0x1, 0x1)
    OP_68(153830, 1330, 130810, 0)
    MoveCamera(29, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7320")
    SetChrFlags(0x0, 0x8)

    label("loc_7320")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7333")
    SetChrFlags(0x1, 0x8)

    label("loc_7333")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7346")
    SetChrFlags(0x2, 0x8)

    label("loc_7346")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7359")
    SetChrFlags(0x3, 0x8)

    label("loc_7359")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_736C")
    SetChrFlags(0x4, 0x8)

    label("loc_736C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_737F")
    SetChrFlags(0x5, 0x8)

    label("loc_737F")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 155090, 30, 129770, 344)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FHmm, does this look all right?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Elie's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x352, 1)
    SetScenarioFlags(0x51, 0)
    OP_66(0x9, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_742C")
    ClearChrFlags(0x0, 0x8)

    label("loc_742C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_743F")
    ClearChrFlags(0x1, 0x8)

    label("loc_743F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7452")
    ClearChrFlags(0x2, 0x8)

    label("loc_7452")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7465")
    ClearChrFlags(0x3, 0x8)

    label("loc_7465")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7478")
    ClearChrFlags(0x4, 0x8)

    label("loc_7478")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_748B")
    ClearChrFlags(0x5, 0x8)

    label("loc_748B")

    Call(1, 39)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_24_72C8 end

    def Function_25_74A2(): pass

    label("Function_25_74A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x1, 0x1)
    OP_68(154150, 1330, 121920, 0)
    MoveCamera(53, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7505")
    SetChrFlags(0x0, 0x8)

    label("loc_7505")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7518")
    SetChrFlags(0x1, 0x8)

    label("loc_7518")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_752B")
    SetChrFlags(0x2, 0x8)

    label("loc_752B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_753E")
    SetChrFlags(0x3, 0x8)

    label("loc_753E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7551")
    SetChrFlags(0x4, 0x8)

    label("loc_7551")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7564")
    SetChrFlags(0x5, 0x8)

    label("loc_7564")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154150, 30, 121920, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FHmm, does this look all right?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Elie's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x353, 1)
    SetScenarioFlags(0x51, 1)
    OP_66(0xA, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7611")
    ClearChrFlags(0x0, 0x8)

    label("loc_7611")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7624")
    ClearChrFlags(0x1, 0x8)

    label("loc_7624")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7637")
    ClearChrFlags(0x2, 0x8)

    label("loc_7637")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_764A")
    ClearChrFlags(0x3, 0x8)

    label("loc_764A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_765D")
    ClearChrFlags(0x4, 0x8)

    label("loc_765D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7670")
    ClearChrFlags(0x5, 0x8)

    label("loc_7670")

    Call(1, 39)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_25_74A2 end

    def Function_26_7687(): pass

    label("Function_26_7687")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "07", 0x1, 0x1)
    OP_68(208030, 1330, 127590, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76DF")
    SetChrFlags(0x0, 0x8)

    label("loc_76DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76F2")
    SetChrFlags(0x1, 0x8)

    label("loc_76F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7705")
    SetChrFlags(0x2, 0x8)

    label("loc_7705")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7718")
    SetChrFlags(0x3, 0x8)

    label("loc_7718")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_772B")
    SetChrFlags(0x4, 0x8)

    label("loc_772B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_773E")
    SetChrFlags(0x5, 0x8)

    label("loc_773E")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208030, 30, 127590, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FThis should be fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Tio's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x51, 2)
    OP_66(0xB, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77E0")
    ClearChrFlags(0x0, 0x8)

    label("loc_77E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77F3")
    ClearChrFlags(0x1, 0x8)

    label("loc_77F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7806")
    ClearChrFlags(0x2, 0x8)

    label("loc_7806")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7819")
    ClearChrFlags(0x3, 0x8)

    label("loc_7819")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_782C")
    ClearChrFlags(0x4, 0x8)

    label("loc_782C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_783F")
    ClearChrFlags(0x5, 0x8)

    label("loc_783F")

    Call(1, 39)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_26_7687 end

    def Function_27_7856(): pass

    label("Function_27_7856")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "08", 0x1, 0x1)
    OP_68(207830, 1330, 127120, 0)
    MoveCamera(56, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78AE")
    SetChrFlags(0x0, 0x8)

    label("loc_78AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78C1")
    SetChrFlags(0x1, 0x8)

    label("loc_78C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78D4")
    SetChrFlags(0x2, 0x8)

    label("loc_78D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78E7")
    SetChrFlags(0x3, 0x8)

    label("loc_78E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78FA")
    SetChrFlags(0x4, 0x8)

    label("loc_78FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_790D")
    SetChrFlags(0x5, 0x8)

    label("loc_790D")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 207830, 30, 127120, 107)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FThis should be fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Tio's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x51, 3)
    OP_66(0xC, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79AF")
    ClearChrFlags(0x0, 0x8)

    label("loc_79AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79C2")
    ClearChrFlags(0x1, 0x8)

    label("loc_79C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79D5")
    ClearChrFlags(0x2, 0x8)

    label("loc_79D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79E8")
    ClearChrFlags(0x3, 0x8)

    label("loc_79E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79FB")
    ClearChrFlags(0x4, 0x8)

    label("loc_79FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A0E")
    ClearChrFlags(0x5, 0x8)

    label("loc_7A0E")

    Call(1, 39)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_27_7856 end

    def Function_28_7A25(): pass

    label("Function_28_7A25")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "03", 0x1, 0x1)
    OP_68(51760, 1300, 129800, 0)
    MoveCamera(29, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A7D")
    SetChrFlags(0x0, 0x8)

    label("loc_7A7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A90")
    SetChrFlags(0x1, 0x8)

    label("loc_7A90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AA3")
    SetChrFlags(0x2, 0x8)

    label("loc_7AA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AB6")
    SetChrFlags(0x3, 0x8)

    label("loc_7AB6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AC9")
    SetChrFlags(0x4, 0x8)

    label("loc_7AC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7ADC")
    SetChrFlags(0x5, 0x8)

    label("loc_7ADC")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 51760, 0, 129800, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#0300FNot too shabby.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Randy's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x51, 4)
    OP_66(0xD, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B7B")
    ClearChrFlags(0x0, 0x8)

    label("loc_7B7B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B8E")
    ClearChrFlags(0x1, 0x8)

    label("loc_7B8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BA1")
    ClearChrFlags(0x2, 0x8)

    label("loc_7BA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BB4")
    ClearChrFlags(0x3, 0x8)

    label("loc_7BB4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BC7")
    ClearChrFlags(0x4, 0x8)

    label("loc_7BC7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BDA")
    ClearChrFlags(0x5, 0x8)

    label("loc_7BDA")

    Call(1, 39)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_28_7A25 end

    def Function_29_7BF1(): pass

    label("Function_29_7BF1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x1, 0x1)
    OP_68(52520, 1300, 124040, 0)
    MoveCamera(70, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C54")
    SetChrFlags(0x0, 0x8)

    label("loc_7C54")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C67")
    SetChrFlags(0x1, 0x8)

    label("loc_7C67")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C7A")
    SetChrFlags(0x2, 0x8)

    label("loc_7C7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C8D")
    SetChrFlags(0x3, 0x8)

    label("loc_7C8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CA0")
    SetChrFlags(0x4, 0x8)

    label("loc_7CA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CB3")
    SetChrFlags(0x5, 0x8)

    label("loc_7CB3")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52520, 0, 124040, 25)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#0300FNot too shabby.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Randy's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x51, 5)
    OP_66(0xE, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D52")
    ClearChrFlags(0x0, 0x8)

    label("loc_7D52")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D65")
    ClearChrFlags(0x1, 0x8)

    label("loc_7D65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D78")
    ClearChrFlags(0x2, 0x8)

    label("loc_7D78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D8B")
    ClearChrFlags(0x3, 0x8)

    label("loc_7D8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D9E")
    ClearChrFlags(0x4, 0x8)

    label("loc_7D9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DB1")
    ClearChrFlags(0x5, 0x8)

    label("loc_7DB1")

    Call(1, 39)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_29_7BF1 end

    def Function_30_7DC8(): pass

    label("Function_30_7DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E43")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When Lloyd finds decorations, he can give them\x01",
            "to each of the members to display in their rooms.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x51, 6)

    label("loc_7E43")

    Return()

    # Function_30_7DC8 end

    def Function_31_7E44(): pass

    label("Function_31_7E44")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis164.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a model orbal car.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_31_7E44 end

    def Function_32_7EEC(): pass

    label("Function_32_7EEC")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis165.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an orbal stereo.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_7FB2"),
        (1, "loc_7FBB"),
        (2, "loc_7FC4"),
        (3, "loc_7FCD"),
        (4, "loc_7FD6"),
        (5, "loc_7FDF"),
        (6, "loc_7FE8"),
        (7, "loc_7FF1"),
        (SWITCH_DEFAULT, "loc_7FFA"),
    )


    label("loc_7FB2")

    PlayBGM("ed7400", 0)
    Jump("loc_7FFA")

    label("loc_7FBB")

    PlayBGM("ed7401", 0)
    Jump("loc_7FFA")

    label("loc_7FC4")

    PlayBGM("ed7402", 0)
    Jump("loc_7FFA")

    label("loc_7FCD")

    PlayBGM("ed7204", 0)
    Jump("loc_7FFA")

    label("loc_7FD6")

    PlayBGM("ed7205", 0)
    Jump("loc_7FFA")

    label("loc_7FDF")

    PlayBGM("ed7201", 0)
    Jump("loc_7FFA")

    label("loc_7FE8")

    PlayBGM("ed7200", 0)
    Jump("loc_7FFA")

    label("loc_7FF1")

    PlayBGM("ed7202", 0)
    Jump("loc_7FFA")

    label("loc_7FFA")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_7EEC end

    def Function_33_8029(): pass

    label("Function_33_8029")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis167.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a wall clock.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_33_8029 end

    def Function_34_80CC(): pass

    label("Function_34_80CC")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis166.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elegant vase.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_34_80CC end

    def Function_35_8172(): pass

    label("Function_35_8172")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis168.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a hanging Mishy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_35_8172 end

    def Function_36_8218(): pass

    label("Function_36_8218")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis057.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a sitting Mishy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_36_8218 end

    def Function_37_82BE(): pass

    label("Function_37_82BE")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis171.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a poster of Ilya Platiere.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_37_82BE end

    def Function_38_836E(): pass

    label("Function_38_836E")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis170.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a dartboard.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_38_836E end

    def Function_39_8410(): pass

    label("Function_39_8410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8448")
    OP_DE(0x16, 0x0)

    label("loc_8448")

    Return()

    # Function_39_8410 end

    SaveToFile()

Try(main)
