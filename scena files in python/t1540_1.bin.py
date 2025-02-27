from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1540_1.bin",                # FileName
        "t1540",                    # MapName
        "t1540",                    # Location
        0x0051,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 81, 0, 1, 0, 3],
    )

    BuildStringList((
        "t1540_1",                # 0
    ))

    ScpFunction((
        "Function_0_15C",          # 00, 0
        "Function_1_88F",          # 01, 1
        "Function_2_C13",          # 02, 2
        "Function_3_127E",         # 03, 3
        "Function_4_15BE",         # 04, 4
        "Function_5_15C2",         # 05, 5
        "Function_6_2A1F",         # 06, 6
        "Function_7_4221",         # 07, 7
        "Function_8_5283",         # 08, 8
        "Function_9_5CC9",         # 09, 9
        "Function_10_6A2E",        # 0A, 10
        "Function_11_6B8E",        # 0B, 11
        "Function_12_6C72",        # 0C, 12
        "Function_13_6FD9",        # 0D, 13
        "Function_14_7221",        # 0E, 14
        "Function_15_7275",        # 0F, 15
        "Function_16_7607",        # 10, 16
        "Function_17_7985",        # 11, 17
        "Function_18_7DA4",        # 12, 18
        "Function_19_804B",        # 13, 19
        "Function_20_81A0",        # 14, 20
        "Function_21_8204",        # 15, 21
        "Function_22_83AA",        # 16, 22
        "Function_23_85FE",        # 17, 23
        "Function_24_8674",        # 18, 24
        "Function_25_88FB",        # 19, 25
        "Function_26_8B2F",        # 1A, 26
        "Function_27_8E71",        # 1B, 27
        "Function_28_92EB",        # 1C, 28
        "Function_29_9668",        # 1D, 29
        "Function_30_99A1",        # 1E, 30
        "Function_31_9CB4",        # 1F, 31
        "Function_32_9FF9",        # 20, 32
        "Function_33_A277",        # 21, 33
        "Function_34_A4F2",        # 22, 34
        "Function_35_A7AE",        # 23, 35
        "Function_36_A91C",        # 24, 36
        "Function_37_AB14",        # 25, 37
        "Function_38_AE30",        # 26, 38
        "Function_39_AE92",        # 27, 39
        "Function_40_B1B6",        # 28, 40
        "Function_41_B397",        # 29, 41
        "Function_42_B6D7",        # 2A, 42
        "Function_43_BAF4",        # 2B, 43
        "Function_44_BCFF",        # 2C, 44
        "Function_45_BEEB",        # 2D, 45
        "Function_46_C273",        # 2E, 46
        "Function_47_C7D2",        # 2F, 47
        "Function_48_C9DC",        # 30, 48
        "Function_49_CB91",        # 31, 49
    ))


    def Function_0_15C(): pass

    label("Function_0_15C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F0")
    Jump("loc_23A")

    label("loc_1F0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_210")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A")

    label("loc_210")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_230")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A")

    label("loc_230")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_26D")
    Jump("loc_887")

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_27B")
    Jump("loc_887")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_289")
    Jump("loc_887")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_297")
    Jump("loc_887")

    label("loc_297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2A5")
    Jump("loc_887")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2B3")
    Jump("loc_887")

    label("loc_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C1")
    Jump("loc_887")

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2CF")
    Jump("loc_887")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2DD")
    Jump("loc_887")

    label("loc_2DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2EB")
    Jump("loc_887")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F9")
    Jump("loc_887")

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_307")
    Jump("loc_887")

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_432")

    ChrTalk(
        0xFE,
        (
            "That reminds me. Doctor Guenter said,\x01",
            "with luck, I can be discharged tomorrow.\x01",
            "I can't say I'm excited for it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just thinking about all the paperwork that's piled\x01",
            "up while I've been MIA makes my head spin. If\x01",
            "only I got two...no, three more days to rest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_48F")

    label("loc_432")


    ChrTalk(
        0xFE,
        (
            "*sigh* You'd think I'd be happy to get back\x01",
            "to work, but nope. I'm utterly depressed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48F")

    Jump("loc_887")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_75C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_720")

    ChrTalk(
        0xFE,
        "Hey, guys. How'd the search go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FPretty good. There are still lots of loose ends\x01",
            "to tie up, but we managed to find evidence\x01",
            "proving that the monsters were up there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wh-Whoa. You're serious, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess it wasn't a dream, after all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks, guys. Just knowing that\x01",
            "I'm not crazy is enough for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FOur pleasure, Lytton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FNow, should we go report our findings\x01",
            "to Cecile?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_6B5")

    ChrTalk(
        0x104,
        (
            "#0300FYup. She's on the third floor, right?\x01",
            "Better not keep the lady waitin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_718")

    label("loc_6B5")


    ChrTalk(
        0x104,
        (
            "#0300FI'm sure the nurses' station would\x01",
            "know where she's at. Wanna try\x01",
            "checkin' there first?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_718")

    SetScenarioFlags(0x0, 0)
    Jump("loc_757")

    label("loc_720")


    ChrTalk(
        0xFE,
        "It couldn't have been a dream. It was too real...\x02",
    )

    CloseMessageWindow()

    label("loc_757")

    Jump("loc_887")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_87E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_800")

    ChrTalk(
        0xFE,
        (
            "Huh. Was all of that really just my\x01",
            "imagination...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sure would be nice if it was, but how\x01",
            "does that explain my injuries...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_879")

    label("loc_800")


    ChrTalk(
        0xFE,
        (
            "Anyway, I'd appreciate it if you'd look\x01",
            "into this some more. Dream or not, I\x01",
            "just want to know what did this to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_879")

    Jump("loc_887")

    label("loc_87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_887")

    label("loc_887")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_0_15C end

    def Function_1_88F(): pass

    label("Function_1_88F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AD")
    Call(1, 2)
    Jump("loc_95E")

    label("loc_8AD")

    TurnDirection(0xC, 0x9, 0)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        "Whoopsie. I messed up again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I won't let it bring me down!\x01",
            "After all, everyone makes mistakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How can one person be THIS\x01",
            "incapable? Sheesh.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_95E")

    Jump("loc_C0F")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_971")
    Jump("loc_C0F")

    label("loc_971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_97F")
    Jump("loc_C0F")

    label("loc_97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_98D")
    Jump("loc_C0F")

    label("loc_98D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_99B")
    Jump("loc_C0F")

    label("loc_99B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_9A9")
    Jump("loc_C0F")

    label("loc_9A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9B7")
    Jump("loc_C0F")

    label("loc_9B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D2")
    Call(1, 2)
    Jump("loc_A30")

    label("loc_9D2")


    ChrTalk(
        0xFE,
        (
            "Oh? Michael? He went on a walk\x01",
            "outside with Ada.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They might be by the water by now.\x02",
    )

    CloseMessageWindow()

    label("loc_A30")

    Jump("loc_C0F")

    label("loc_A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A43")
    Jump("loc_C0F")

    label("loc_A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A51")
    Jump("loc_C0F")

    label("loc_A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_AE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6C")
    Call(1, 3)
    Jump("loc_ADB")

    label("loc_A6C")


    ChrTalk(
        0xFE,
        (
            "With this many thermometers, it\x01",
            "doesn't matter if I make a mistake or\x01",
            "two. Everything's going to be A-OK.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADB")

    Jump("loc_C0F")

    label("loc_AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFB")
    Call(1, 3)
    Jump("loc_B52")

    label("loc_AFB")


    ChrTalk(
        0xFE,
        (
            "Hehe, oopsie! I thought I lost my thermometer,\x01",
            "but it was in my pocket all along.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B52")

    Jump("loc_C0F")

    label("loc_B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_B65")
    Jump("loc_C0F")

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_B73")
    Jump("loc_C0F")

    label("loc_B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_C06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8E")
    Call(1, 2)
    Jump("loc_C01")

    label("loc_B8E")


    ChrTalk(
        0xFE,
        "*sigh* Meifa is such a fussypants.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Later, I have to check on Mr. Gable.\x01",
            "See how he's doing and all that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C01")

    Jump("loc_C0F")

    label("loc_C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C0F")

    label("loc_C0F")

    TalkEnd(0xFE)
    Return()

    # Function_1_88F end

    def Function_2_C13(): pass

    label("Function_2_C13")

    TurnDirection(0x9, 0xC, 0)
    TurnDirection(0xC, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D69")

    ChrTalk(
        0xC,
        (
            "Ciroooone...! Did you never learn\x01",
            "how to brew coffee correctly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Why the heck can I smell tea coming\x01",
            "from the pot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmmm, that's probably because I\x01",
            "mixed the tea and coffee together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, I'm WELL aware you did that!\x01",
            "What I'm asking is WHY you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...*sigh* You know what? Forget it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_126F")

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_D77")
    Jump("loc_126F")

    label("loc_D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D85")
    Jump("loc_126F")

    label("loc_D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D93")
    Jump("loc_126F")

    label("loc_D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_DA1")
    Jump("loc_126F")

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_DAF")
    Jump("loc_126F")

    label("loc_DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_DBD")
    Jump("loc_126F")

    label("loc_DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_FE9")

    ChrTalk(
        0x9,
        (
            "Hey, Meifa. What kind of disease\x01",
            "does Michael actually have?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Let's see... Well, it's very complex, and he\x01",
            "needs an operation to make a full recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Of course, most kids are scared of surgeries.\x01",
            "It might take a lot of time to convince him to\x01",
            "go through with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, I get that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope he can find the courage to undergo\x01",
            "the operation. It's for the best, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If only there were something that could\x01",
            "give him that little push he needs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You know, you say some pretty wise\x01",
            "stuff, once in a blue moon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126F")

    label("loc_FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FF7")
    Jump("loc_126F")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1005")
    Jump("loc_126F")

    label("loc_1005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1013")
    Jump("loc_126F")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1021")
    Jump("loc_126F")

    label("loc_1021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_102F")
    Jump("loc_126F")

    label("loc_102F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_103D")
    Jump("loc_126F")

    label("loc_103D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1266")

    ChrTalk(
        0xC,
        (
            "Let me get this straight. You spilled a\x01",
            "bunch of tomato soup on Mr. Gable's\x01",
            "bedsheets yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yep. Scared me, that's for sure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "One of the passing doctors mistook it for\x01",
            "a massive hemorrhage and passed out...\x01",
            "so maybe it scared him a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "You're unbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Wh-Whatever. The sheets were cleaned,\x01",
            "so that's all that matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now go take some new bedsheets to\x01",
            "Mr. Gable and apologize, okay? Like,\x01",
            "as sincerely as you can muster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Aw, seriously? That guy's so annoying...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "No complaining! Go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_126F")

    label("loc_1266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_126F")

    label("loc_126F")

    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_2_C13 end

    def Function_3_127E(): pass

    label("Function_3_127E")

    TurnDirection(0x9, 0x1B, 0)
    SetChrSubChip(0x1B, 0x2)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_129B")
    Jump("loc_15B2")

    label("loc_129B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_143C")

    ChrTalk(
        0x9,
        (
            "Okie dokie, time to take your temperature.\x01",
            "Raise that arm reeeal high and then lower\x01",
            "it once I put in the thermometer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "E-Excuse me, miss. I'm perfectly okay\x01",
            "with you taking my temperature, but why\x01",
            "do you have TEN thermometers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, if I accidentally break one while\x01",
            "taking your temperature, I'll have plenty\x01",
            "of backups! It's a foolproof plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "(I-I have a bad feeling about this...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B2")

    label("loc_143C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_15B2")

    ChrTalk(
        0x9,
        (
            "Okay, ready for me to take your temperature?\x01",
            "Better raise that arm, 'cause here it comes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "W-Wait a second, miss. You made sure to\x01",
            "double-check you're using a thermometer\x01",
            "and NOT an injection needle, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Psh! 'Course I did. I may be prone to\x01",
            "making mistakes, but I'd never make\x01",
            "a dumb one like that twice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, would you look at that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "...\x02",
    )

    CloseMessageWindow()

    label("loc_15B2")

    SetScenarioFlags(0x0, 1)
    SetChrSubChip(0x1B, 0x0)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_3_127E end

    def Function_4_15BE(): pass

    label("Function_4_15BE")

    Call(1, 5)
    Return()

    # Function_4_15BE end

    def Function_5_15C2(): pass

    label("Function_5_15C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D8")
    Call(0, 11)
    Jump("loc_2A1E")

    label("loc_15D8")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_186E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CE")

    ChrTalk(
        0xA,
        "Someday I'll have that day off, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll make sure to give you a call when that\x01",
            "happens, okay? The two of us and some\x01",
            "friends can all go have some fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FI'll be waitin'!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C6")

    ChrTalk(
        0x10A,
        (
            "#0603FYou have some real guts to make date\x01",
            "plans while on duty and in front of me,\x01",
            "Orlando.\x02\x03",
            "#0600FIf you were a part of the First Division,\x01",
            "I'd have you write a formal apology and\x01",
            "have it on my desk by this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FAck?! C'mon, man, lighten up!\x02",
    )

    CloseMessageWindow()

    label("loc_17C6")

    SetScenarioFlags(0x0, 3)
    Jump("loc_1869")

    label("loc_17CE")


    ChrTalk(
        0xA,
        (
            "Now that the festival's over, I can finally\x01",
            "take some time off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You're still up for that date, right? I'll make\x01",
            "sure to invite Ada and Lan, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1869")

    Jump("loc_2A1B")

    label("loc_186E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_18F7")

    ChrTalk(
        0xA,
        "It's almost dinner time, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I should go ahead and grab the patients' meals\x01",
            "from Kirsch while I have time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_18F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1988")

    ChrTalk(
        0xA,
        (
            "Thankfully, the patient that was carried in today\x01",
            "only suffered minor injuries. As of now, he should\x01",
            "be sleeping in Room 201.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_1988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1C1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B08")

    ChrTalk(
        0xA,
        (
            "We admitted Mr. Gable, one of the diet members,\x01",
            "into a private room on the third floor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...recently, he got a bit tipsy and barged into the\x01",
            "nurses' station, asking for some company. Quite\x01",
            "rudely, I might add.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Soon after, Miss Martha threw open the door\x01",
            "and dragged him back to his room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Honestly, did he mistake us for hostesses?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C16")

    label("loc_1B08")


    ChrTalk(
        0xA,
        (
            "Occasionally, we have to deal with some\x01",
            "less-than-pleasant individuals, like Mr. Gable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They always stay longer than necessary because\x01",
            "they think the hospital is cozy, or they just like to\x01",
            "sexually harass the nurses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Honestly, how disgusting can men get?\x02",
    )

    CloseMessageWindow()

    label("loc_1C16")

    Jump("loc_2A1B")

    label("loc_1C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1CCC")

    ChrTalk(
        0xA,
        (
            "I saw a little girl run towards the lower floor\x01",
            "with her cheeks puffed up like balloons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She looked furious, but at the same time,\x01",
            "super, super cute! ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_1CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1D33")

    ChrTalk(
        0xA,
        "Oh, hello there, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you're looking for Cecile, she went up\x01",
            "to Room 301.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_1D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1DF4")

    ChrTalk(
        0xA,
        (
            "You know, it kinda freaks me out when\x01",
            "the doctors aren't around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I know they say the interns are incredibly\x01",
            "bright, but that doesn't mean they're on\x01",
            "the doctors' level.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_1DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F00")

    ChrTalk(
        0xA,
        "I'm staaaaarving...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since the nurses' breaks are divvied up through\x01",
            "a shift system, I often end up having to eat later\x01",
            "than I'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Trust me, it's always embarrassing when you're\x01",
            "taking temperatures and your stomach growls.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1F42")

    label("loc_1F00")


    ChrTalk(
        0xA,
        "(*groooowl*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "*sigh* Lunch break can't come soon enough.\x02",
    )

    CloseMessageWindow()

    label("loc_1F42")

    Jump("loc_2A1B")

    label("loc_1F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2129")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DB")

    ChrTalk(
        0xA,
        (
            "To be honest, I'd be perfectly okay with only\x01",
            "having tomorrow off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After all, the parade is tomorrow! You can't\x01",
            "say you truly experienced the Anniversary\x01",
            "Festival without seeing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm jealous of you police officers. You're\x01",
            "probably able to use work as an excuse\x01",
            "to go watch the parade, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FH-Hey. We'd never abuse our power like\x01",
            "that...probably.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2124")

    label("loc_20DB")


    ChrTalk(
        0xA,
        (
            "I'd love to see the parade tomorrow, but\x01",
            "if duty calls, duty calls.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2124")

    Jump("loc_2A1B")

    label("loc_2129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_21FC")

    ChrTalk(
        0xA,
        (
            "After covering for me yesterday, I'm happy\x01",
            "that Meifa and Cirone were given the day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since we spent all day at the festival yesterday,\x01",
            "we can't slack off now that we're back at work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_21FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_23F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234C")

    ChrTalk(
        0xA,
        (
            "I still can't wrap my head around the fact that\x01",
            "one of my coworkers is practically best friends\x01",
            "with Ilya Platiere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Do you think it'd be weird to ask\x01",
            "Cecile if she could get Ilya to sign\x01",
            "something of mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(It seems like you can't swing a stick\x01",
            "in Crossbell without hitting an Ilya fan.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_23EB")

    label("loc_234C")


    ChrTalk(
        0xA,
        (
            "Do you think it'd be weird to ask\x01",
            "Cecile if she could get Ilya to sign\x01",
            "something of mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If I can find the right time, maybe\x01",
            "I'll try asking her...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23EB")

    Jump("loc_2A1B")

    label("loc_23F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_24DF")

    ChrTalk(
        0xA,
        (
            "Darn it. I ended up not being able to\x01",
            "get those Arc en Ciel tickets I wanted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Miss Martha keeps bragging that she's seen\x01",
            "them before, but I bet the current Arc en Ciel\x01",
            "is way better now compared to when she went.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_24DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2545")

    ChrTalk(
        0xA,
        "97.8 degrees... Everything looks normal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "And next, we have...Lytton, I think.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_2545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_25F5")

    ChrTalk(
        0xA,
        (
            "The really scary thing about Miss Martha\x01",
            "is how sharp her hearing is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You never know when she's listening in, so\x01",
            "we always have to watch what we say...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1B")

    label("loc_25F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2A12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A3")

    ChrTalk(
        0xA,
        (
            "Ah, Cecile. I was wondering when I was\x01",
            "going to run into you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our break's almost over... Is something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1300FOh, I'm just helping these four for a bit. I'm\x01",
            "sorry. I'll be back as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No need to apologize, Cecile. If it won't take\x01",
            "too long, go ahead. But, um...hello?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FSorry for takin' up Cecile's time. The name's\x01",
            "Randy. Randy Orlando.\x02\x03",
            "#0300FAnd you are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Uh, I'm Philia. Nice to meet you, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FOh, come on, Randy. Can't you save the flirting\x01",
            "for when we're not in the middle of a case?\x02\x03",
            "#0000FAhem. Sorry for not introducing ourselves. I'm\x01",
            "Lloyd, and we're the Special Support Section\x01",
            "of the Crossbell Police Department.\x02\x03",
            "We're here to investigate Lytton's attack...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ohhh, that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(Lloyd? Could this guy be the person\x01",
            "Cecile's always talking about...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Heeheehee. Well, good luck with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(Wh-What was with that laugh?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 1)
    Jump("loc_2A0D")

    label("loc_29A3")


    ChrTalk(
        0xA,
        "Good luck with the investigation!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(That smile is giving me the creeps\x01",
            "for some reason...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A0D")

    Jump("loc_2A1B")

    label("loc_2A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2A1B")

    label("loc_2A1B")

    TalkEnd(0xA)

    label("loc_2A1E")

    Return()

    # Function_5_15C2 end

    def Function_6_2A1F(): pass

    label("Function_6_2A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A46")
    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2A41")
    SetScenarioFlags(0x0, 5)

    label("loc_2A41")

    Jump("loc_4220")

    label("loc_2A46")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2AF4")

    ChrTalk(
        0xB,
        "Today is going to be a good day. I'm sure of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's the duty of us nurses to put everything we\x01",
            "have into our jobs, for the sake of our patients.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_2AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC8")
    TurnDirection(0xB, 0x103, 0)

    ChrTalk(
        0xB,
        (
            "Tio? Are you feeling all right?\x01",
            "You look a little pale, dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FThis is my natural complexion. Please,\x01",
            "do not pay it any mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm? Just my imagination, then?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2C52")

    label("loc_2BC8")


    ChrTalk(
        0xB,
        "Perhaps my mind is playing tricks on me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, well. The sun's going to set soon, so\x01",
            "try to be careful when heading back, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C52")

    Jump("loc_421D")

    label("loc_2C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2D3B")

    ChrTalk(
        0xB,
        (
            "Ever since this morning, the entire hospital\x01",
            "has been awfully hectic. It seems to finally\x01",
            "be calming down, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "All things considered, I'm just thankful that\x01",
            "the man brought in is in stable condition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_2D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2EF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E53")

    ChrTalk(
        0xB,
        (
            "It soothes my heart to see Shizuku so\x01",
            "cheerful as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When I asked her what happened, she\x01",
            "got a big smile on her face and told me\x01",
            "that she made a friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm so happy for her. They say friends are\x01",
            "life's greatest treasure, you know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2EEB")

    label("loc_2E53")


    ChrTalk(
        0xB,
        (
            "It soothes my heart to see Shizuku so\x01",
            "cheerful as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hearing that she's made a friend made the\x01",
            "entire nursing staff as happy as can be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EEB")

    Jump("loc_421D")

    label("loc_2EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3177")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309E")

    ChrTalk(
        0xB,
        "Cecile is quite the hardworking young lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because of that, essentially everyone who comes\x01",
            "into contact with her finds her easy to confide in.\x01",
            "Nurses, doctors, patients, you name it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I were to choose someone to be my successor\x01",
            "as head nurse, Cecile would be at the top of my list.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FWow... That really says a lot about her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Haha. With luck, that won't be for some time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3172")

    label("loc_309E")


    ChrTalk(
        0xB,
        (
            "If I were to choose someone to succeed me as\x01",
            "head nurse, Cecile would be at the top of my list.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I plan to continue working for at least another\x01",
            "20 years, though. That's something in the distant\x01",
            "future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3172")

    Jump("loc_421D")

    label("loc_3177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_3301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_325A")

    ChrTalk(
        0xB,
        (
            "Can't we have Mr. Gable discharged from the\x01",
            "hospital soon? He's taking up Room 302.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Besides, us nurses have actual jobs to do.\x01",
            "We don't have time to attend to a man\x01",
            "who's faking an illness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_32FC")

    label("loc_325A")


    ChrTalk(
        0xB,
        (
            "Well, as long as he's considered a patient,\x01",
            "there's not much I can do about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I suppose we have to wait until he's fed up\x01",
            "with life at St. Ursula...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32FC")

    Jump("loc_421D")

    label("loc_3301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_342D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A7")

    ChrTalk(
        0xB,
        (
            "Trying to get all the nurses on the\x01",
            "same page is tiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Aidios bless Cecile. Her being here makes\x01",
            "things a little easier on me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3428")

    label("loc_33A7")


    ChrTalk(
        0xB,
        (
            "I can trust Cecile to even cover tasks\x01",
            "befitting of the head nurse position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I don't know what I would do without her.\x02",
    )

    CloseMessageWindow()

    label("loc_3428")

    Jump("loc_421D")

    label("loc_342D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3555")

    ChrTalk(
        0xB,
        "Philia still has a lot to learn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Everyone gets hungry, even the nurses, but\x01",
            "it's not necessary to wait for your lunch break\x01",
            "to start eating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Take me for example. When I'm on the move\x01",
            "or have a moment's rest, I'm scarfing down a\x01",
            "sandwich! Grit, that's what she needs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_3555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3717")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3668")

    ChrTalk(
        0xB,
        "Cecile? I believe she went to Shizuku's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm afraid Shizuku can be a difficult child\x01",
            "sometimes. Perhaps losing her mother so\x01",
            "early has caused her to grow up too soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think it would do her good if she acted\x01",
            "more like her age.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3712")

    label("loc_3668")


    ChrTalk(
        0xB,
        (
            "Perhaps losing her mother so early in her\x01",
            "life caused Shizuku to grow up before she\x01",
            "had to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think it would do her good if she acted more\x01",
            "like the kid she is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3712")

    Jump("loc_421D")

    label("loc_3717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_389B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37CE")

    ChrTalk(
        0xB,
        "Where was I yesterday? Here, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There's no such thing as rest for nurses. After all,\x01",
            "patients aren't going to treat themselves, are they?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3896")

    label("loc_37CE")


    ChrTalk(
        0xB,
        (
            "The hospital can't afford to take time off. The needs\x01",
            "of the patients always come first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Someone should tell Doctor Guenter that. Maybe\x01",
            "it'd nip his nasty habit of playing hooky in the bud.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3896")

    Jump("loc_421D")

    label("loc_389B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_398C")

    ChrTalk(
        0xB,
        (
            "After finding out that Cecile is friends with\x01",
            "Ilya Platiere, the rest of the nurses have\x01",
            "gotten their panties in a bunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Honestly, can't they worry less about that and\x01",
            "focus more on being as diligent as her instead?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_398C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC9")

    ChrTalk(
        0xB,
        (
            "Fliers detailing Arc en Ciel's upcoming show\x01",
            "finally made their way to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When I was a young girl, Arc en Ciel had neither\x01",
            "fame nor that superstar, Ilya Platiere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now you can't say Crossbell without thinking\x01",
            "of Arc en Ciel. It sure has come a long way,\x01",
            "hasn't it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B48")

    label("loc_3AC9")


    ChrTalk(
        0xB,
        (
            "Ah, I went to see Arc en Ciel many, many\x01",
            "times when I was a young girl. The thought\x01",
            "of it makes me a tad bit nostalgic...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B48")

    Jump("loc_421D")

    label("loc_3B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3D0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_3C40")

    ChrTalk(
        0xB,
        (
            "Well, well, well... The Tio I knew from years\x01",
            "back looked nothing like the one I see now.\x01",
            "That's a compliment, if I must add.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Are you heading back already? Please, stop\x01",
            "by and say hello when you find the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D07")

    label("loc_3C40")


    ChrTalk(
        0xB,
        (
            "Thanks to you, I don't think we will have to\x01",
            "worry about any more monsters intruding\x01",
            "and causing a ruckus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "On the behalf of the staff and patients of\x01",
            "St. Ursula Medical College, thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D07")

    Jump("loc_421D")

    label("loc_3D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_3F8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_3EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF3")

    ChrTalk(
        0xB,
        (
            "After treating a patient, I never forget their\x01",
            "face. That being said, I still didn't recognize\x01",
            "you, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Come again, will you? I would love to sit\x01",
            "down and chat if you have the chance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3EE8")

    label("loc_3DF3")


    ChrTalk(
        0xB,
        (
            "Oh, you'll find Cecile in the farthest room\x01",
            "down the hall on the third floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Shizuku is here under special circumstances,\x01",
            "but I assure you, she's a lovely girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If possible, I would love it if you could spend\x01",
            "some time with her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE8")

    Jump("loc_3F86")

    label("loc_3EED")


    ChrTalk(
        0xB,
        (
            "Pardon me, everyone. My plate is full with\x01",
            "balancing the hospital's account book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you need anything, confer with Philia\x01",
            "outside, all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F86")

    Jump("loc_421D")

    label("loc_3F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_4214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4174")

    ChrTalk(
        0xB,
        "Hello, Cecile. Guiding visitors, are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#1300FWell, sort of...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cecile explained the details behind the Special Support\x01",
            "Section's visit to the head nurse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Very well. If that's the case, you are free to show\x01",
            "them around and assist them if need be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The Special Support Section, hmm? Good luck\x01",
            "with that investigation of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FTh-Thank you, ma'am. (I wouldn't want to\x01",
            "get on her bad side, that's for sure...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0208F...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_420F")

    label("loc_4174")


    ChrTalk(
        0xB,
        (
            "If monsters truly made their way onto\x01",
            "St. Ursula grounds, we have a serious\x01",
            "problem on our hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Everyone, I hope your investigation\x01",
            "goes well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_420F")

    Jump("loc_421D")

    label("loc_4214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_421D")

    label("loc_421D")

    TalkEnd(0xB)

    label("loc_4220")

    Return()

    # Function_6_2A1F end

    def Function_7_4221(): pass

    label("Function_7_4221")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_42CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_423F")
    Call(1, 2)
    Jump("loc_42C6")

    label("loc_423F")


    ChrTalk(
        0xFE,
        "*sigh* I swear, this girl just doesn't get it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe I made the mistake of asking\x01",
            "Cirone to do something for me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42C6")

    Jump("loc_527F")

    label("loc_42CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_42D9")
    Jump("loc_527F")

    label("loc_42D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_452C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4483")

    ChrTalk(
        0xFE,
        (
            "The bedsheets used at St. Ursula are\x01",
            "bought from Mr. Hayworth, a local trader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I, being the intelligent person I am, decided\x01",
            "to put Cirone in charge of ordering more. I told\x01",
            "her to buy 50 sheets, and she bought 500.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "500, you hear me? FIVE! HUNDRED! Thank\x01",
            "Aidios Mr. Hayworth noticed something was\x01",
            "off and notified the hospital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* What am I going to do with that girl?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4527")

    label("loc_4483")


    ChrTalk(
        0xFE,
        (
            "If it had been ANY other trader, we would\x01",
            "have definitely been forced to buy the 500.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I can say anything about Cirone, it's that\x01",
            "she's absurdly lucky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4527")

    Jump("loc_527F")

    label("loc_452C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4932")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4613")

    ChrTalk(
        0xFE,
        (
            "You know what? It was Cirone who suggested\x01",
            "I buy that ribbon in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How much does that girl have to make fun of\x01",
            "me until she's finally satisfied? It's becoming\x01",
            "too much to handle...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_492D")

    label("loc_4613")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_46D5")

    ChrTalk(
        0xFE,
        "Still, I'm glad I didn't throw it away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's pretty long, so I'm sure it will be perfect\x01",
            "for gift wrapping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, good luck with finding whatever else\x01",
            "you need.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_492D")

    label("loc_46D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_46E9")
    Call(1, 49)
    Jump("loc_492D")

    label("loc_46E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4824")

    ChrTalk(
        0xFE,
        (
            "Cirone's been tight-lipped since her\x01",
            "last mess-up. For good reason, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She put the blood bags that were just delivered\x01",
            "from Remiferia in the COMMUNAL FREEZER.\x01",
            "We put our lunch in there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I was looking for my cup of yogurt in the\x01",
            "freezer, I swear my heart skipped a few beats.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_492D")

    label("loc_4824")


    ChrTalk(
        0xFE,
        (
            "Don't fool yourselves. Cirone's mistakes are not\x01",
            "'cute' nor is she just a simple airhead. Oh, she is\x01",
            "much, much, much worse than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Storing blood bags meant for transfusions in the\x01",
            "communal freezer...? That's domestic terrorism,\x01",
            "I tell you. Terrorism!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_492D")

    Jump("loc_527F")

    label("loc_4932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_4940")
    Jump("loc_527F")

    label("loc_4940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_494E")
    Jump("loc_527F")

    label("loc_494E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4A79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A32")

    ChrTalk(
        0xFE,
        (
            "Cirone took my favorite casual dress\x01",
            "out of my dorm...without telling me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without that, I'm stuck in this uniform\x01",
            "even in the comfort of my dorm room.\x01",
            "Cirone, prepare for an interrogation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A74")

    label("loc_4A32")


    ChrTalk(
        0xFE,
        (
            "Cirone, where the heck did you go?!\x01",
            "Give me my clothes back!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A74")

    Jump("loc_527F")

    label("loc_4A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A94")
    Call(1, 2)
    Jump("loc_4B06")

    label("loc_4A94")


    ChrTalk(
        0xFE,
        (
            "Even though they're only children, Shizuku\x01",
            "and Michael are doing their best with the\x01",
            "hand they were dealt...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B06")

    Jump("loc_527F")

    label("loc_4B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4B19")
    Jump("loc_527F")

    label("loc_4B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4B27")
    Jump("loc_527F")

    label("loc_4B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4C90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C0D")

    ChrTalk(
        0xFE,
        (
            "Ugh, my head... It's like I can sense when\x01",
            "Cirone is out there doing something utterly\x01",
            "moronic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Goddess. Have I formed a sixth sense\x01",
            "revolving around Cirone because I'm around\x01",
            "her so much?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4C8B")

    label("loc_4C0D")


    ChrTalk(
        0xFE,
        (
            "*sigh* Surely Cirone can at least take\x01",
            "someone's temperature, right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "On second thought, I'll check on her later.\x02",
    )

    CloseMessageWindow()

    label("loc_4C8B")

    Jump("loc_527F")

    label("loc_4C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4ED0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E15")

    ChrTalk(
        0xFE,
        "The clumsiness of Cirone knows no bounds.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She usually grabs the wrong medical utensils,\x01",
            "spills chemicals and medicine on the floor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I'm being honest, the only reason someone\x01",
            "hasn't got hurt yet is because of the people\x01",
            "surrounding her, catching her mistakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* It sure would do me a favor if she took\x01",
            "a page out of Cecile's book...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4ECB")

    label("loc_4E15")


    ChrTalk(
        0xFE,
        (
            "Cirone's clumsiness is NOT a joke, okay?\x01",
            "It's honestly a miracle that no one's been\x01",
            "hurt yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* It sure would do me a favor if she took\x01",
            "a page out of Cecile's book...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ECB")

    Jump("loc_527F")

    label("loc_4ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_502F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE7")

    ChrTalk(
        0xFE,
        "Argh! She's late! Again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cirone, how is it humanly possible to\x01",
            "take this long to hang up some wet\x01",
            "bedsheets?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, don't tell me... Did she get them dirty\x01",
            "again?! I had those sheets shining so much\x01",
            "I could do my makeup in the reflection!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_502A")

    label("loc_4FE7")


    ChrTalk(
        0xFE,
        (
            "Cirone, I swear to Aidios if you messed up\x01",
            "those bedsheets...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_502A")

    Jump("loc_527F")

    label("loc_502F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_50D8")

    ChrTalk(
        0xFE,
        (
            "Cirone went to apologize to Diet Member\x01",
            "Gable, did she? Good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering her track record, I wouldn't\x01",
            "be surprised if this goes horribly wrong.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_527F")

    label("loc_50D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_518D")

    ChrTalk(
        0xFE,
        "You're looking for Cecile?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I don't think she went back to the\x01",
            "nurses' station, but I could be wrong...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She must still be finishing up some chores.\x02",
    )

    CloseMessageWindow()
    Jump("loc_527F")

    label("loc_518D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A8")
    Call(1, 2)
    Jump("loc_5271")

    label("loc_51A8")


    ChrTalk(
        0xFE,
        (
            "Cirone has a knack for making absolutely\x01",
            "mind-blowing mistakes, forcing us to pick\x01",
            "up after her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And despite all that, she's somehow incredibly\x01",
            "popular with the patients, which baffles me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5271")

    Jump("loc_527F")

    label("loc_5276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_527F")

    label("loc_527F")

    TalkEnd(0xFE)
    Return()

    # Function_7_4221 end

    def Function_8_5283(): pass

    label("Function_8_5283")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5294")
    Jump("loc_5CC5")

    label("loc_5294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_52A2")
    Jump("loc_5CC5")

    label("loc_52A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_52B0")
    Jump("loc_5CC5")

    label("loc_52B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_52BE")
    Jump("loc_5CC5")

    label("loc_52BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_52CC")
    Jump("loc_5CC5")

    label("loc_52CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_52DA")
    Jump("loc_5CC5")

    label("loc_52DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_52E8")
    Jump("loc_5CC5")

    label("loc_52E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_52F6")
    Jump("loc_5CC5")

    label("loc_52F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5304")
    Jump("loc_5CC5")

    label("loc_5304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5656")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5510")

    ChrTalk(
        0xD,
        (
            "#1302FOh, Lloyd! Back on the clock already?\x02\x03",
            "#1309FDid you four have a good break?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FDefinitely. I was finally able to relax at\x01",
            "home for the first time in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202FI didn't do much. So, yes, it was very nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FY'know, I'm of the opinion that one day\x01",
            "hardly qualifies as a genuine break.\x02\x03",
            "#0300FBesides, I'm kinda bummed that I wasn't\x01",
            "able to spend some time with ya, Cecile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F(Despite all that complaining, you had a\x01",
            "pretty great day off, huh, Randy?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 5)
    Jump("loc_5651")

    label("loc_5510")


    ChrTalk(
        0xD,
        (
            "#1304FI certainly made the most of my short,\x01",
            "little break. Ilya even introduced me to\x01",
            "Rixia, finally.\x02\x03",
            "#1302FOh, I nearly forgot. Ilya told me it was\x01",
            "silly to not have invited you, too. She\x01",
            "seemed pretty torn up about it.\x02\x03",
            "#1309FPopular, aren't you, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FPopular? I feel more like a toy, if anything...\x02",
    )

    CloseMessageWindow()

    label("loc_5651")

    Jump("loc_5CC5")

    label("loc_5656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5A21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_595C")

    ChrTalk(
        0xD,
        (
            "#1300FOh, Lloyd! Spectacular timing.\x02\x03",
            "I just managed to obtain two tickets for\x01",
            "Arc en Ciel's public show next month.\x02\x03",
            "#1309FIf you're free, won't you go with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0009FReally? Thanks, Cecile, I'd love to.\x02\x03",
            "#0004FI can't say exactly when I'll be free due to\x01",
            "work and all that, but I definitely want to go\x01",
            "if I'm able to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#1309FMusic to my ears. If that's the case,\x01",
            "I'll hang on to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F(Judging by how impressive that practice looked,\x01",
            "the real deal must be out of this world...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F(*staaaaare*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0111F(Planning dates while on the job, are we?\x01",
            "Congratulations, Lloyd.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301F(Lloyd, you lucky son of a bitch!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Ugh, I almost wish they'd chew me out\x01",
            "instead of shooting these glares at me...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 4)
    Jump("loc_5A1C")

    label("loc_595C")


    ChrTalk(
        0xD,
        (
            "#1300FI really hope we'll be able to see Arc en Ciel's\x01",
            "new show together, Lloyd.\x02\x03",
            "#1309FYou had better find some time, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FS-Sure. I'll try my best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F(*staaaaare*)\x02",
    )

    CloseMessageWindow()

    label("loc_5A1C")

    Jump("loc_5CC5")

    label("loc_5A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5A2F")
    Jump("loc_5CC5")

    label("loc_5A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_5CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B85")

    ChrTalk(
        0xD,
        "#1305FLloyd? Did you forget something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FNo, nothing like that, Cecile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#1305FOh! Does that mean it's finally time for\x01",
            "you to give me your report?\x02\x03",
            "#1309FSo tell me, out of Elie, Tio, and Randy...\x02\x03",
            "...who did you decide to date?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FYou know full well that's not what\x01",
            "I was talking about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5C9B")

    label("loc_5B85")


    ChrTalk(
        0xD,
        (
            "#1300FHeehee. Sorry, I couldn't help myself.\x02\x03",
            "Lloyd, if something happens here again...\x01",
            "No, actually, even if something doesn't\x01",
            "happen again, stop by to see me, okay?\x02\x03",
            "#1304FWell, if you'll excuse me, I have to bring\x01",
            "Shizuku her dinner. Have a wonderful\x01",
            "evening, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C9B")

    Jump("loc_5CC5")

    label("loc_5CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5CAE")
    Jump("loc_5CC5")

    label("loc_5CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5CBC")
    Jump("loc_5CC5")

    label("loc_5CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5CC5")

    label("loc_5CC5")

    TalkEnd(0xFE)
    Return()

    # Function_8_5283 end

    def Function_9_5CC9(): pass

    label("Function_9_5CC9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5D70")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "Though it's a relatively simple operation, that\x01",
            "doesn't mean you can proceed without caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just rest here and recover, all right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A2A")

    label("loc_5D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_5E1B")

    ChrTalk(
        0xFE,
        (
            "Much to my surprise, that particular patient\x01",
            "never tries to resist our treatment. He's quite\x01",
            "calm, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, hopefully things stay that way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A2A")

    label("loc_5E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_60FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F98")

    ChrTalk(
        0xFE,
        (
            "Several men from the Heiyue Trading, Ltd.\x01",
            "were carried in on stretchers this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One was transferred to this ward, and for the time\x01",
            "being, that's where he will stay--at least, until he's\x01",
            "well enough to be able to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it's clear that these aren't wounds normal\x01",
            "civilians would ever get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "These men are very suspicious.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_60F9")

    label("loc_5F98")


    ChrTalk(
        0xFE,
        (
            "Men from an organization called Heiyue were rushed\x01",
            "into the hospital this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most of them are resting in the ICU, which is good.\x01",
            "They'll need rest if they want to recover. Now, as for\x01",
            "the one staying here, he requires a bit more attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, the circumstances surrounding them are\x01",
            "a tad too suspicious for my liking...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60F9")

    Jump("loc_6A2A")

    label("loc_60FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_610C")
    Jump("loc_6A2A")

    label("loc_610C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6386")

    ChrTalk(
        0xFE,
        (
            "I was giving Shizuku an examination until\x01",
            "a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her particular condition is tricky to fully cure\x01",
            "with modern technology, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surgery, internal medicine, neurology... Each of\x01",
            "these fields' current problems interfere with\x01",
            "each other, obstructing the path to a cure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Due to her not having complete blindness, there\x01",
            "is still a small chance of recovery, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "What am I doing? You aren't members of her\x01",
            "family, nor do you have permission to know any\x01",
            "of this. How careless of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Forget everything I've said up until now, all right?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_643C")

    label("loc_6386")


    ChrTalk(
        0xFE,
        (
            "What am I doing? You aren't members of her\x01",
            "family, nor do you have permission to know any\x01",
            "of this. How careless of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Forget everything I've said up until now, all right?\x02",
    )

    CloseMessageWindow()

    label("loc_643C")

    Jump("loc_6A2A")

    label("loc_6441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_644F")
    Jump("loc_6A2A")

    label("loc_644F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_645D")
    Jump("loc_6A2A")

    label("loc_645D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_653F")

    ChrTalk(
        0xFE,
        (
            "I can't say I enjoy wasting my time examining\x01",
            "perfectly healthy people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm in the middle of making my rounds now.\x01",
            "Remember, if you become a nuisance to our\x01",
            "patients, I won't hesitate to call security.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A2A")

    label("loc_653F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_654D")
    Jump("loc_6A2A")

    label("loc_654D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_673C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A1")

    ChrTalk(
        0xFE,
        "Day two, here we go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With that comes even more merriment, causing\x01",
            "people to pay less attention to their surroundings.\x01",
            "In my experience, that's when people get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How nice would it be if those petty gang members\x01",
            "aren't carried into the hospital again tomorrow. I'm\x01",
            "not holding my breath, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6737")

    label("loc_66A1")


    ChrTalk(
        0xFE,
        (
            "Merriment is fine and all, but it causes you to pay\x01",
            "less attention to your surroundings, leading to risk\x01",
            "of injury. Be careful out there, folks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6737")

    Jump("loc_6A2A")

    label("loc_673C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6820")

    ChrTalk(
        0xFE,
        (
            "My next operation is a relatively minor one,\x01",
            "but I absolutely will not take any shortcuts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surgeons hold an obligation to the patient\x01",
            "and themselves to follow that credo. It's the\x01",
            "bare minimum we can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A2A")

    label("loc_6820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6944")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "Tomophobia is perfectly understandable.\x01",
            "Natural, even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, the risk of danger in this particular\x01",
            "operation is astronomically low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anxiety will only serve as a detriment to the\x01",
            "surgery. Please, try to calm yourself and go\x01",
            "to sleep early tonight, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A2A")

    label("loc_6944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_6A05")

    ChrTalk(
        0xFE,
        (
            "I'm heading to Room 202 now. There's a few\x01",
            "more patients I have to check on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You aren't inpatients, right? If so, I recommend\x01",
            "you catch the bus before it gets too late.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A2A")

    label("loc_6A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_6A13")
    Jump("loc_6A2A")

    label("loc_6A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_6A21")
    Jump("loc_6A2A")

    label("loc_6A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6A2A")

    label("loc_6A2A")

    TalkEnd(0xFE)
    Return()

    # Function_9_5CC9 end

    def Function_10_6A2E(): pass

    label("Function_10_6A2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A43")
    Call(1, 12)
    Jump("loc_6B8A")

    label("loc_6A43")


    ChrTalk(
        0xFE,
        (
            "I've been telling the brass since this morning,\x01",
            "but we aren't getting anywhere. Shouldn't we\x01",
            "withdraw and stop wasting manpower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These Heiyue guys are tough customers,\x01",
            "I'll give them that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's the first time I've interacted with them,\x01",
            "but it's obvious that their camaraderie runs\x01",
            "deep, even in the lower ranks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B8A")

    TalkEnd(0xFE)
    Return()

    # Function_10_6A2E end

    def Function_11_6B8E(): pass

    label("Function_11_6B8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BA3")
    Call(1, 12)
    Jump("loc_6C6E")

    label("loc_6BA3")


    ChrTalk(
        0xFE,
        (
            "Damn the First Division! I knew this whole\x01",
            "thing was pointless from the start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They always waltz in and snatch our cases,\x01",
            "and they have the balls to work us to the\x01",
            "friggin' bone like this...?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C6E")

    TalkEnd(0xFE)
    Return()

    # Function_11_6B8E end

    def Function_12_6C72(): pass

    label("Function_12_6C72")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    TurnDirection(0xF, 0x0, 0)
    TurnDirection(0x10, 0x0, 0)

    ChrTalk(
        0xF,
        "Tch. Heiyue goons, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Aren't they cute, having a story lined up\x01",
            "beforehand? They went the whole nine arge.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#0105FInspector, is the Second Division looking\x01",
            "into the attack on Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Yep. Request came straight from the First Division.\x01",
            "They asked if we could get statements from those\x01",
            "hospitalized and see what we can dig up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "But it's not like these guys will ever rat on\x01",
            "Heiyue. Their lips are sealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Those First Division guys really piss me off\x01",
            "sometimes! They knew we'd get jack squat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011F(Were they taken advantage of because the\x01",
            "First Division didn't want to go through the\x01",
            "formality of taking statements? That's rough.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Guess the Second Division has their own\x01",
            "problems to deal with, eh?)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x0)
    OP_93(0x10, 0x5A, 0x0)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Return()

    # Function_12_6C72 end

    def Function_13_6FD9(): pass

    label("Function_13_6FD9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_706D")
    Jump("loc_70B7")

    label("loc_706D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_708D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70B7")

    label("loc_708D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70B7")

    label("loc_70AD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70B7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_70EA")
    Jump("loc_7219")

    label("loc_70EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_7152")

    ChrTalk(
        0xFE,
        (
            "Evening already? Well, when you sleep all\x01",
            "day, you aren't going to see too much sun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7219")

    label("loc_7152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_7160")
    Jump("loc_7219")

    label("loc_7160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_7210")

    ChrTalk(
        0xFE,
        (
            "He's supposed to be a medical intern, yet he\x01",
            "still found himself hospitalized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess even medical people can neglect\x01",
            "their own health sometimes, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7219")

    label("loc_7210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7219")

    label("loc_7219")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_6FD9 end

    def Function_14_7221(): pass

    label("Function_14_7221")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It's been dreadfully loud for a while now.\x01",
            "Can't you pipe down already?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_7221 end

    def Function_15_7275(): pass

    label("Function_15_7275")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7309")
    Jump("loc_7353")

    label("loc_7309")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7329")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7353")

    label("loc_7329")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7349")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7353")

    label("loc_7349")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7353")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7386")
    Jump("loc_75FF")

    label("loc_7386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_73B5")

    ChrTalk(
        0xFE,
        "Hospitals are boooooring...\x02",
    )

    CloseMessageWindow()
    Jump("loc_75FF")

    label("loc_73B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_7402")

    ChrTalk(
        0xFE,
        (
            "Can't one of the gorgeous nurses here\x01",
            "keep a guy company?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75FF")

    label("loc_7402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_75F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_754C")

    ChrTalk(
        0xFE,
        (
            "Wh-Who the heck was that doctor with\x01",
            "the glasses...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was talking about medical procedures\x01",
            "when all of a sudden, he started rambling\x01",
            "about sadism and masochism...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1306FI'm very sorry about that. Doctor Guenter\x01",
            "is a...unique individual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FI doubt that will be the end of that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_75F1")

    label("loc_754C")


    ChrTalk(
        0xFE,
        (
            "That doctor with the glasses just now didn't\x01",
            "strike me as a doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But they called him an associate professor,\x01",
            "so that must be he's qualified, I guess...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75F1")

    Jump("loc_75FF")

    label("loc_75F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_75FF")

    label("loc_75FF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_7275 end

    def Function_16_7607(): pass

    label("Function_16_7607")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_769B")
    Jump("loc_76E5")

    label("loc_769B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_76BB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_76E5")

    label("loc_76BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76DB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_76E5")

    label("loc_76DB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_76E5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7718")
    Jump("loc_797D")

    label("loc_7718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_77CC")

    ChrTalk(
        0xFE,
        (
            "That old lady's had a smile plastered on her face\x01",
            "for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if she's able to stay positive while staying\x01",
            "here, there's no reason I can't, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_797D")

    label("loc_77CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_7895")

    ChrTalk(
        0xFE,
        (
            "That lady's granddaughter has come\x01",
            "to visit her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After complaining and complaining about how\x01",
            "no one has come to see her, she finally got\x01",
            "what she wanted. Good for her, I guess?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_797D")

    label("loc_7895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_7974")

    ChrTalk(
        0xFE,
        (
            "*sigh* That old lady keeps complaining about\x01",
            "how no one's come to see her while at the\x01",
            "hospital. It never ends...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wouldn't be surprised if I ended up with a\x01",
            "minor case of depression because of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_797D")

    label("loc_7974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_797D")

    label("loc_797D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_7607 end

    def Function_17_7985(): pass

    label("Function_17_7985")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A19")
    Jump("loc_7A63")

    label("loc_7A19")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A39")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A63")

    label("loc_7A39")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A59")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A63")

    label("loc_7A59")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A63")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7A96")
    Jump("loc_7D9C")

    label("loc_7A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_7B6E")

    ChrTalk(
        0xFE,
        (
            "My adorable granddaughter came to visit me,\x01",
            "but I sent her back home before it got dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, thanks to her, I feel like a new woman.\x01",
            "It's time to perk up and work towards getting\x01",
            "discharged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D9C")

    label("loc_7B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_7CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B89")
    Call(1, 19)
    Jump("loc_7CAB")

    label("loc_7B89")


    ChrTalk(
        0xFE,
        (
            "Believe it or not, but my granddaughter came\x01",
            "to visit me all by herself. She even rode the bus\x01",
            "alone! Oh, she sure makes this old heart happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm told that my son and his family have been\x01",
            "preoccupied lately. Honestly, I feel terrible for\x01",
            "venting all my frustrations out on them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CAB")

    Jump("loc_7D9C")

    label("loc_7CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_7D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_END)), "loc_7CD4")
    Call(1, 18)
    Jump("loc_7D56")

    label("loc_7CD4")


    ChrTalk(
        0xFE,
        (
            "No one from my family has come to visit me\x01",
            "yet...and it's been days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I just want to see my granddaughter...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_7D56")

    Jump("loc_7D8E")

    label("loc_7D5B")


    ChrTalk(
        0xFE,
        "*sigh* I just want to see my granddaughter...\x02",
    )

    CloseMessageWindow()

    label("loc_7D8E")

    Jump("loc_7D9C")

    label("loc_7D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7D9C")

    label("loc_7D9C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_7985 end

    def Function_18_7DA4(): pass

    label("Function_18_7DA4")

    OP_93(0x30, 0xB4, 0x0)
    SetChrSubChip(0x15, 0x2)
    OP_4B(0x30, 0xFF)

    ChrTalk(
        0x15,
        (
            "No one from my family has come to visit me\x01",
            "yet...and it's been days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "*sigh* I just want to see my granddaughter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Busy or not, my son's family lacks basic\x01",
            "consideration!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "#2406FYou're preaching to the choir. They sound\x01",
            "like quite the deplorable bunch.\x02\x03",
            "#2400FWell, anyway, if you have enough energy to rant,\x01",
            "I think you'll probably be discharged soon. Don't\x01",
            "worry, you'll see your grandkid soon enough.\x02\x03",
            "#2409FBy the way, want some of this candy? I'm sure it'll\x01",
            "help calm you down. Smother the fire, if you will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "*sigh* You're the only one who understands\x01",
            "my woes, doctor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(He's such an...unorthodox doctor.)\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x30, 0xFF)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 5)
    Return()

    # Function_18_7DA4 end

    def Function_19_804B(): pass

    label("Function_19_804B")

    TurnDirection(0x16, 0x15, 0)
    SetChrSubChip(0x15, 0x2)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x16,
        (
            "Granny, Granny! Guess what? I rode the\x01",
            "bus by myself for the first time ever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I think it was even more fun than riding it\x01",
            "with Mama and Papa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Oh, is that right? How wonderful, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Here. Doctor Guenter gave me a candy bar\x01",
            "earlier, but I'd love for you to have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Yay! Thank you, Granny!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_19_804B end

    def Function_20_81A0(): pass

    label("Function_20_81A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81B5")
    Call(1, 19)
    Jump("loc_8200")

    label("loc_81B5")


    ChrTalk(
        0xFE,
        (
            "Granny looks a lot better than I was\x01",
            "expecting. Heehee, I'm so happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8200")

    TalkEnd(0xFE)
    Return()

    # Function_20_81A0 end

    def Function_21_8204(): pass

    label("Function_21_8204")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8298")
    Jump("loc_82E2")

    label("loc_8298")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_82B8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_82E2")

    label("loc_82B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82D8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_82E2")

    label("loc_82D8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_82E2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I banged up my knee, but considering how\x01",
            "much I've improved today, the doctor said\x01",
            "I might be able to leave soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hoho. I can't wait to go home.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_8204 end

    def Function_22_83AA(): pass

    label("Function_22_83AA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_843E")
    Jump("loc_8488")

    label("loc_843E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_845E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8488")

    label("loc_845E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_847E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8488")

    label("loc_847E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8488")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_84BB")
    Jump("loc_85F6")

    label("loc_84BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8576")

    ChrTalk(
        0xFE,
        (
            "I-I'm finally having m-my surgery later.\x01",
            "They told me my surgeon's going to be\x01",
            "Doctor Belldine, so that's reassuring, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* The butterflies won't go away.\x02",
    )

    CloseMessageWindow()
    Jump("loc_85F6")

    label("loc_8576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_85F6")

    ChrTalk(
        0xFE,
        "*sigh* This is the end for me, I think.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The doctor said the operation's a piece\x01",
            "of cake, but I don't know...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85F6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_83AA end

    def Function_23_85FE(): pass

    label("Function_23_85FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_860F")
    Jump("loc_8670")

    label("loc_860F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_864F")

    ChrTalk(
        0xFE,
        "Mmgrmmm... *snore*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mmm... Zzz... Zzz...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8670")

    label("loc_864F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8670")

    ChrTalk(
        0xFE,
        "Mmgrmmm... *snore*\x02",
    )

    CloseMessageWindow()

    label("loc_8670")

    TalkEnd(0xFE)
    Return()

    # Function_23_85FE end

    def Function_24_8674(): pass

    label("Function_24_8674")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8708")
    Jump("loc_8752")

    label("loc_8708")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8728")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8752")

    label("loc_8728")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8748")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8752")

    label("loc_8748")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8752")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8785")
    Jump("loc_88F3")

    label("loc_8785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8854")

    ChrTalk(
        0xFE,
        (
            "Sometimes, you almost don't want to leave\x01",
            "this place. It's just too comfy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On top of that, the doctors and nurses are\x01",
            "so nice to everyone... Hehe, what should I\x01",
            "do if I want to stay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88F3")

    label("loc_8854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_88F3")

    ChrTalk(
        0xFE,
        (
            "These hospital beds are far finer than mine at\x01",
            "home. Also, I can't remember the last time I was\x01",
            "brought food without having to ask. It's lovely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88F3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_8674 end

    def Function_25_88FB(): pass

    label("Function_25_88FB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_898F")
    Jump("loc_89D9")

    label("loc_898F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_89AF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89D9")

    label("loc_89AF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89CF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89D9")

    label("loc_89CF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_89D9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8A0C")
    Jump("loc_8B27")

    label("loc_8A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8A82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A27")
    Call(1, 3)
    Jump("loc_8A7D")

    label("loc_8A27")


    ChrTalk(
        0xFE,
        (
            "How in the world does she manage to break\x01",
            "the thermometer every...single...time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A7D")

    Jump("loc_8B27")

    label("loc_8A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8B27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A9D")
    Call(1, 3)
    Jump("loc_8B27")

    label("loc_8A9D")


    ChrTalk(
        0xFE,
        (
            "If I were a cat, I doubt my nine lives would\x01",
            "be enough to save me from a klutz like her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Still, she's pretty cute, so whatever.\x02",
    )

    CloseMessageWindow()

    label("loc_8B27")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_88FB end

    def Function_26_8B2F(): pass

    label("Function_26_8B2F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x1C)
    ClearChrFlags(0x1C, 0x10)
    TurnDirection(0x1C, 0x0, 0)
    OP_52(0x1C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BC3")
    Jump("loc_8C0D")

    label("loc_8BC3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8BE3")
    OP_52(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C0D")

    label("loc_8BE3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C03")
    OP_52(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C0D")

    label("loc_8C03")

    OP_52(0x1C, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C0D")

    OP_52(0x1C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1C, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_8C40")
    Jump("loc_8E69")

    label("loc_8C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8D12")

    ChrTalk(
        0x1C,
        (
            "The nurses have been giving me the\x01",
            "stink eye ever since they found that\x01",
            "mag I tried to hide...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "It's all that old man's fault! He's the one who\x01",
            "gave me the damn thing in the first place!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E69")

    label("loc_8D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8DA0")

    ChrTalk(
        0x1C,
        (
            "The nurse found the mag that old man\x01",
            "planted on me while taking my temp...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "Man, my face went as red as a tomartian...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E69")

    label("loc_8DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8DFE")

    ChrTalk(
        0x1C,
        (
            "(Is this guy really some great doctor?\x01",
            "I'm, uh, not sure if I buy that...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E69")

    label("loc_8DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8E69")

    ChrTalk(
        0x1C,
        (
            "*sigh* This blows... If I didn't get hurt like\x01",
            "an idiot, I'd be in full-blown festival mode.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E69")

    SetChrSubChip(0x1C, 0x0)
    TalkEnd(0x1C)
    Return()

    # Function_26_8B2F end

    def Function_27_8E71(): pass

    label("Function_27_8E71")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F05")
    Jump("loc_8F4F")

    label("loc_8F05")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8F25")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F4F")

    label("loc_8F25")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F45")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F4F")

    label("loc_8F45")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F4F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_8F82")
    Jump("loc_92E3")

    label("loc_8F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9069")

    ChrTalk(
        0xFE,
        (
            "After I gave that youngin' one of my magazines,\x01",
            "he started shooting glares in my direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm? That means he wants some more?\x01",
            "I guess I wouldn't mind tossing him a few\x01",
            "more. That's what friends do, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92E3")

    label("loc_9069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9165")

    ChrTalk(
        0xFE,
        (
            "Yesterday, out of the kindness of my heart,\x01",
            "I gave that youngin' next to me one of my\x01",
            "sexy magazines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering how flustered he got when the\x01",
            "nurse took his temperature, it definitely looks\x01",
            "like he's feeling a lot better now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92E3")

    label("loc_9165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9212")

    ChrTalk(
        0xFE,
        (
            "Handing out erotic magazines is my special\x01",
            "way of greeting someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doctor Guenter, being the friendly guy\x01",
            "he is, already decided to be my supplier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92E3")

    label("loc_9212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_92E3")

    ChrTalk(
        0xFE,
        (
            "Doesn't that youngin' laying down over\x01",
            "there look pretty down in the dumps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Oh, my bleeding heart. I guess I'll gift\x01",
            "him one of my prized magazines. That will\x01",
            "cheer him up, no doubt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92E3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_8E71 end

    def Function_28_92EB(): pass

    label("Function_28_92EB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_937F")
    Jump("loc_93C9")

    label("loc_937F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_939F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93C9")

    label("loc_939F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93BF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93C9")

    label("loc_93BF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_93C9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_93FC")
    Jump("loc_9660")

    label("loc_93FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_94D3")

    ChrTalk(
        0xFE,
        (
            "Through intense research, I've been able to figure\x01",
            "out who's coming to check on the patients today,\x01",
            "and it's...Doctor Gailey? Who the heck is that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just want Doctor Guenter to check on me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9660")

    label("loc_94D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_953B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94EE")
    Call(1, 47)
    Jump("loc_9536")

    label("loc_94EE")


    ChrTalk(
        0xFE,
        (
            "You're quite the shy man, aren't you,\x01",
            "Doctor Guenter? Heehee... ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9536")

    Jump("loc_9660")

    label("loc_953B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_95BA")

    ChrTalk(
        0xFE,
        "So Doctor Guenter is single, hmm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm no doctor, but I'm sure I can\x01",
            "fill that hole in his heart. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9660")

    label("loc_95BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9660")

    ChrTalk(
        0xFE,
        (
            "Aw, shouldn't Doctor Guenter be here\x01",
            "already? My heart can't wait any longer! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That reserved, easygoing attitude...\x01",
            "Oh, he's exactly my type! ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9660")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_92EB end

    def Function_29_9668(): pass

    label("Function_29_9668")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96FC")
    Jump("loc_9746")

    label("loc_96FC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_971C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9746")

    label("loc_971C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_973C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9746")

    label("loc_973C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9746")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_9779")
    Jump("loc_9999")

    label("loc_9779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9804")

    ChrTalk(
        0xFE,
        (
            "Today, the hospital's surgeon is coming\x01",
            "to check how my leg is doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I do hope it's getting better and not worse.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9999")

    label("loc_9804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_986B")

    ChrTalk(
        0xFE,
        (
            "My, oh, my. That doctor was such a cutie.\x01",
            "I've no doubt he's a hit with the ladies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9999")

    label("loc_986B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_98F7")

    ChrTalk(
        0xFE,
        (
            "The nurses have been very kind to me\x01",
            "during my stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some have their quirks, sure,\x01",
            "but they're all very nice girls.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9999")

    label("loc_98F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9999")

    ChrTalk(
        0xFE,
        "This hospital is quite the quaint place, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until my leg fully recovers, I plan to simply\x01",
            "relax and enjoy what St. Ursula has to offer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9999")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_9668 end

    def Function_30_99A1(): pass

    label("Function_30_99A1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A35")
    Jump("loc_9A7F")

    label("loc_9A35")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9A55")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A7F")

    label("loc_9A55")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A75")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A7F")

    label("loc_9A75")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A7F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9AB2")
    Jump("loc_9CAC")

    label("loc_9AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_9C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BA5")

    ChrTalk(
        0xFE,
        (
            "When the nurse was checkin' our temps,\x01",
            "she found one of my mags. You know\x01",
            "the kind I'm talkin' about, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She gave me a smile and didn't push it,\x01",
            "but I honestly think a frown would have\x01",
            "stung less...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9BFF")

    label("loc_9BA5")


    ChrTalk(
        0xFE,
        (
            "*sigh* I should have never grabbed that\x01",
            "dirty magazine from the old coot next to\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BFF")

    Jump("loc_9CAC")

    label("loc_9C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_9CAC")

    ChrTalk(
        0xFE,
        (
            "Heh heh... The nurses here are a bunch of\x01",
            "beauts, aren't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hell, I'd take one of them over those fake\x01",
            "ones in the magazines any day of the week.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CAC")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_99A1 end

    def Function_31_9CB4(): pass

    label("Function_31_9CB4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D48")
    Jump("loc_9D92")

    label("loc_9D48")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9D68")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D92")

    label("loc_9D68")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D88")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D92")

    label("loc_9D88")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D92")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9DC5")
    Jump("loc_9FF1")

    label("loc_9DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_9EFD")

    ChrTalk(
        0xFE,
        "Doc says I'm almost ready to head home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gotta say, I'm sorta blue. I was becoming\x01",
            "fast friends with my hospital buddies, but\x01",
            "that's how life is, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I think a farewell gift is in order. I'll give\x01",
            "that kid another magazine from my private\x01",
            "collection. A real special one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FF1")

    label("loc_9EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_9FF1")

    ChrTalk(
        0xFE,
        (
            "I handed over some of my sexy magazines to the\x01",
            "guy staying next to me as a sign of friendship.\x01",
            "That's true generosity, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And get this. During one of the nurse checkups,\x01",
            "he was caught red-handed! Wahaha, amazing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FF1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_9CB4 end

    def Function_32_9FF9(): pass

    label("Function_32_9FF9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A08D")
    Jump("loc_A0D7")

    label("loc_A08D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A0AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0D7")

    label("loc_A0AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A0CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0D7")

    label("loc_A0CD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A0D7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A10A")
    Jump("loc_A26F")

    label("loc_A10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_A19F")

    ChrTalk(
        0xFE,
        "Some kid just sprinted down the hallway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did her parents not teach her any manners?\x01",
            "Don't run in the hallway. It's not hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A26F")

    label("loc_A19F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_A26F")

    ChrTalk(
        0xFE,
        (
            "Last week, Doctor Lago came in to inspect\x01",
            "my aching stomach, and now I get to finally go\x01",
            "home sometime this week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Food poisoning is scary stuff. Make sure to\x01",
            "watch what you eat, all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A26F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_9FF9 end

    def Function_33_A277(): pass

    label("Function_33_A277")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A30B")
    Jump("loc_A355")

    label("loc_A30B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A32B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A355")

    label("loc_A32B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A34B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A355")

    label("loc_A34B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A355")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A388")
    Jump("loc_A4EA")

    label("loc_A388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_A436")

    ChrTalk(
        0xFE,
        "Huh?! You met with Doctor Guenter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Grrr, that man! If he had time to meet with\x01",
            "kids like yourselves, then he should have\x01",
            "had time to make his rounds!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4EA")

    label("loc_A436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_A4EA")

    ChrTalk(
        0xFE,
        (
            "Once I started to realize that he wasn't checking\x01",
            "on his patients, someone told me that he wasn't\x01",
            "even in charge of that anymore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh! Doctor Guenter, you jerk!\x02",
    )

    CloseMessageWindow()

    label("loc_A4EA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_A277 end

    def Function_34_A4F2(): pass

    label("Function_34_A4F2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A586")
    Jump("loc_A5D0")

    label("loc_A586")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A5A6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5D0")

    label("loc_A5A6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A5C6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5D0")

    label("loc_A5C6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A5D0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A603")
    Jump("loc_A7A6")

    label("loc_A603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_A66F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A61E")
    Call(1, 36)
    Jump("loc_A66A")

    label("loc_A61E")


    ChrTalk(
        0xFE,
        (
            "W-Well, no matter what happened, I'm\x01",
            "glad he was able to make it here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A66A")

    Jump("loc_A7A6")

    label("loc_A66F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_A7A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A774")

    ChrTalk(
        0xFE,
        (
            "I got a call yesterday saying that one of\x01",
            "my friends was coming to visit, but he\x01",
            "ended up being a no-show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That guy has absolutely no sense of direction.\x01",
            "He could be going to the Harbor District and\x01",
            "somehow end up in Mainz.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A7A6")

    label("loc_A774")


    ChrTalk(
        0xFE,
        "Will he be able to make it to St. Ursula...?\x02",
    )

    CloseMessageWindow()

    label("loc_A7A6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_A4F2 end

    def Function_35_A7AE(): pass

    label("Function_35_A7AE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A842")
    Jump("loc_A88C")

    label("loc_A842")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A862")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A88C")

    label("loc_A862")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A882")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A88C")

    label("loc_A882")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A88C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8C3")
    Call(1, 36)
    Jump("loc_A914")

    label("loc_A8C3")


    ChrTalk(
        0xFE,
        (
            "Dang, man. I don't know what to say.\x01",
            "This hospital is a freaking labyrinth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A914")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_A7AE end

    def Function_36_A91C(): pass

    label("Function_36_A91C")

    TurnDirection(0x2D, 0x24, 0)
    SetChrSubChip(0x24, 0x1)
    OP_4B(0x2D, 0xFF)

    ChrTalk(
        0x2D,
        (
            "Hey, man. Had enough of the hospital life\x01",
            "yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "Haha, I'm getting there. Thanks for coming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "But, didn't you call up and say you were\x01",
            "planning to stop by yesterday? What ever\x01",
            "happened to that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "Funny thing about that. I made it here, but\x01",
            "I couldn't find your room for the life of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "Once the sun started to set, I just gave\x01",
            "up and stayed in one of the dorm rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Whew. Maybe you should see if St. Ursula\x01",
            "could fix that internal compass of yours...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetChrSubChip(0x24, 0x0)
    OP_4C(0x2D, 0xFF)
    Return()

    # Function_36_A91C end

    def Function_37_AB14(): pass

    label("Function_37_AB14")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ABA8")
    Jump("loc_ABF2")

    label("loc_ABA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ABC8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ABF2")

    label("loc_ABC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABE8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ABF2")

    label("loc_ABE8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ABF2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_ACEA")

    ChrTalk(
        0xFE,
        (
            "That guy was hospitalized yesterday, but this morning,\x01",
            "before I even noticed, he was discharged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm sure he probably did something pretty\x01",
            "stupid to end up here in the first place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE28")

    label("loc_ACEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_ACF8")
    Jump("loc_AE28")

    label("loc_ACF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AD90")

    ChrTalk(
        0xFE,
        (
            "That new guy apparently got banged up\x01",
            "bad during a fight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I dunno how I feel about sharing a room\x01",
            "with that type of person...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE28")

    label("loc_AD90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_AE28")

    ChrTalk(
        0xFE,
        (
            "Recently, my attending physician has been\x01",
            "Doctor Lago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It really is a privilege to be treated by such\x01",
            "a prestigious doctor like him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE28")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_37_AB14 end

    def Function_38_AE30(): pass

    label("Function_38_AE30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AE41")
    Jump("loc_AE8E")

    label("loc_AE41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_AE77")

    ChrTalk(
        0xFE,
        "Mmmm... *snore*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Zzz... Zzz...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE8E")

    label("loc_AE77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AE85")
    Jump("loc_AE8E")

    label("loc_AE85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_AE8E")

    label("loc_AE8E")

    TalkEnd(0xFE)
    Return()

    # Function_38_AE30 end

    def Function_39_AE92(): pass

    label("Function_39_AE92")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AF26")
    Jump("loc_AF70")

    label("loc_AF26")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF46")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AF70")

    label("loc_AF46")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF66")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AF70")

    label("loc_AF66")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AF70")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B021")

    ChrTalk(
        0xFE,
        (
            "Yesterday, my girlfriend came to visit\x01",
            "me, and boy, was that embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She brought the waterworks, all right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1AE")

    label("loc_B021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_B09F")

    ChrTalk(
        0xFE,
        "Didn't I tell you not to come?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I told you! I'm not causing trouble\x01",
            "for anyone, and that's the truth!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1AE")

    label("loc_B09F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B12D")

    ChrTalk(
        0xFE,
        "My girlfriend's stopping by to visit today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...despite my begging her not to come.\x01",
            "It's too embarrassing, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1AE")

    label("loc_B12D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B1AE")

    ChrTalk(
        0xFE,
        (
            "Ugh. Hospitals drive me up the wall.\x01",
            "I can never get a moment's rest at them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just let me outta here already!\x02",
    )

    CloseMessageWindow()

    label("loc_B1AE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_AE92 end

    def Function_40_B1B6(): pass

    label("Function_40_B1B6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B24A")
    Jump("loc_B294")

    label("loc_B24A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B26A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B294")

    label("loc_B26A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B28A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B294")

    label("loc_B28A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B294")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B2C7")
    Jump("loc_B38F")

    label("loc_B2C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_B378")
    TurnDirection(0xFE, 0x27, 0)

    ChrTalk(
        0xFE,
        (
            "Heehee, you look well. I'll count my\x01",
            "blessings as they come, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You aren't causing the staff and the\x01",
            "rest of the patients trouble, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B38F")

    label("loc_B378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B386")
    Jump("loc_B38F")

    label("loc_B386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B38F")

    label("loc_B38F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_40_B1B6 end

    def Function_41_B397(): pass

    label("Function_41_B397")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B42B")
    Jump("loc_B475")

    label("loc_B42B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B44B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B475")

    label("loc_B44B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B46B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B475")

    label("loc_B46B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B475")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B564")

    ChrTalk(
        0xFE,
        (
            "The old man staying in this room went\x01",
            "out on a walk with one of the nurses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, he's got the right idea. Maybe I\x01",
            "should ask the next nurse I see if she\x01",
            "will do the same for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6CF")

    label("loc_B564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_B5B2")

    ChrTalk(
        0xFE,
        (
            "Everyone staying in this room\x01",
            "is quirky in their own ways.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6CF")

    label("loc_B5B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B616")

    ChrTalk(
        0xFE,
        "Oh, my, there's so many people here today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So, who are you here to visit?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B6CF")

    label("loc_B616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B6CF")

    ChrTalk(
        0xFE,
        (
            "After living by myself, it's refreshing to stay\x01",
            "in a bustling place like St. Ursula.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone I've met has been friendly, so\x01",
            "I'll try my best to get along with them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6CF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_41_B397 end

    def Function_42_B6D7(): pass

    label("Function_42_B6D7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B76B")
    Jump("loc_B7B5")

    label("loc_B76B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B78B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B7B5")

    label("loc_B78B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B7AB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B7B5")

    label("loc_B7AB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B7B5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B8B8")

    ChrTalk(
        0xFE,
        (
            "My son and mother-in-law are coming to visit\x01",
            "me tomorrow, so I'm quite excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Throughout my stay here, my mother-in-law has\x01",
            "been extremely sympathetic. I really should find\x01",
            "some way to thank her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAEC")

    label("loc_B8B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_B925")

    ChrTalk(
        0xFE,
        (
            "I've only had a few meals, but the food here is\x01",
            "top-notch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What a pleasant surprise.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BAEC")

    label("loc_B925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B9F7")

    ChrTalk(
        0xFE,
        (
            "I just got a phone call from my mother-in-law\x01",
            "saying that she's bringing my son to come pay\x01",
            "me a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Aidios, what do I do? What if he did\x01",
            "something horrible while I was away...?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAEC")

    label("loc_B9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BAEC")

    ChrTalk(
        0xFE,
        (
            "After being hospitalized, I put my son in the\x01",
            "hands of my mother-in-law, Aidios bless her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In my experience, most newly-wed wives and\x01",
            "their mother-in-laws clash with each other, but\x01",
            "fortunately, we've been able to avoid that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAEC")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_42_B6D7 end

    def Function_43_BAF4(): pass

    label("Function_43_BAF4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BB88")
    Jump("loc_BBD2")

    label("loc_BB88")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BBA8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BBD2")

    label("loc_BBA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBC8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BBD2")

    label("loc_BBC8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BBD2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BC05")
    Jump("loc_BCF7")

    label("loc_BC05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_BC13")
    Jump("loc_BCF7")

    label("loc_BC13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BC21")
    Jump("loc_BCF7")

    label("loc_BC21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BCF7")

    ChrTalk(
        0xFE,
        (
            "As soon as my stomach started aching, I was\x01",
            "told that I had something called 'appendicitis'\x01",
            "and driven here before I even had time to blink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, how bad could it be?! I just want to go\x01",
            "home!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCF7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_BAF4 end

    def Function_44_BCFF(): pass

    label("Function_44_BCFF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BDBD")

    ChrTalk(
        0xFE,
        (
            "Ugh... It feels like a thousand needles are\x01",
            "being poked into my belly, over and over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The surgery might be over, but now I have\x01",
            "to endure the recovery period...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEE7")

    label("loc_BDBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_BE20")

    ChrTalk(
        0xFE,
        (
            "I just had my surgery this morning. Mind\x01",
            "leaving me alone and letting me sleep?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEE7")

    label("loc_BE20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BEDE")

    ChrTalk(
        0xFE,
        (
            "Ugh... I just had my appendectomy this\x01",
            "morning, and Goddess, was it horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It hurts...and I'm hungry...and I wanna sleep...\x01",
            "but I don't wanna do anything, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEE7")

    label("loc_BEDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BEE7")

    label("loc_BEE7")

    TalkEnd(0xFE)
    Return()

    # Function_44_BCFF end

    def Function_45_BEEB(): pass

    label("Function_45_BEEB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BF7F")
    Jump("loc_BFC9")

    label("loc_BF7F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF9F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BFC9")

    label("loc_BF9F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BFBF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BFC9")

    label("loc_BFBF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BFC9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BFFC")
    Jump("loc_C26B")

    label("loc_BFFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_C0C5")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "(Staying here too long will only\x01",
            "cause the company trouble...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Tomorrow, when the rest of them wake\x01",
            "up, we'll force the staff to discharge us\x01",
            "whether they like it or not.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C26B")

    label("loc_C0C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1AF")

    ChrTalk(
        0xFE,
        "Damn police are pests as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They can ask me whatever questions they'd\x01",
            "like. Still won't get anything outta me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may look all right, but I'm still a patient,\x01",
            "am I not? I have needs, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C25D")

    label("loc_C1AF")


    ChrTalk(
        0xFE,
        (
            "Apparently, my coworkers who were admitted\x01",
            "with me are still in the ICU. I'm sure they'll\x01",
            "wake up by tomorrow, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Heh. I must admit, St. Ursula works wonders.\x02",
    )

    CloseMessageWindow()

    label("loc_C25D")

    Jump("loc_C26B")

    label("loc_C262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C26B")

    label("loc_C26B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_45_BEEB end

    def Function_46_C273(): pass

    label("Function_46_C273")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C284")
    Jump("loc_C7CE")

    label("loc_C284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_C292")
    Jump("loc_C7CE")

    label("loc_C292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C2A0")
    Jump("loc_C7CE")

    label("loc_C2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C2AE")
    Jump("loc_C7CE")

    label("loc_C2AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_C2BC")
    Jump("loc_C7CE")

    label("loc_C2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_C2CA")
    Jump("loc_C7CE")

    label("loc_C2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C2D8")
    Jump("loc_C7CE")

    label("loc_C2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C376")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2F3")
    Call(1, 47)
    Jump("loc_C371")

    label("loc_C2F3")


    ChrTalk(
        0x30,
        (
            "#2406F*sigh* Being popular can be such a hassle\x01",
            "sometimes. I'd much rather finish my rounds\x01",
            "and hurry on home, but alas.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C371")

    Jump("loc_C7CE")

    label("loc_C376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C677")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C54B")

    ChrTalk(
        0x30,
        (
            "#2400FSo, are you enjoying the Anniversary Festival?\x02\x03",
            "#2409FI know I am. I just found a new fishing hole\x01",
            "yesterday and, wow, is it something. I plan\x01",
            "to run over there as soon as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FUh, aren't you in the middle of work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "#2409FHahaha. Well, yes, but be a friend and\x01",
            "keep that from the other doctors, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x1, 5)
    Jump("loc_C672")

    label("loc_C54B")


    ChrTalk(
        0x30,
        (
            "#2405FYou know, despite what I was saying, there\x01",
            "actually is a little something I have to finish\x01",
            "up today.\x02\x03",
            "#2400FAnd everyone gets a break, right? Why complain\x01",
            "if I decide to spend mine differently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(If that's really how you feel, why the need\x01",
            "to go under everyone's radar...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C672")

    Jump("loc_C7CE")

    label("loc_C677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C685")
    Jump("loc_C7CE")

    label("loc_C685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C693")
    Jump("loc_C7CE")

    label("loc_C693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C6A1")
    Jump("loc_C7CE")

    label("loc_C6A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_C6AF")
    Jump("loc_C7CE")

    label("loc_C6AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_C6BD")
    Jump("loc_C7CE")

    label("loc_C6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_C7C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6D8")
    Call(1, 18)
    Jump("loc_C7C0")

    label("loc_C6D8")


    ChrTalk(
        0x30,
        (
            "#2403FHey, I've heard people say sickness and health\x01",
            "come from the mind. As long as she's this lively,\x01",
            "I doubt we'll keep her here too much longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1306FPlease try to sound a bit more like a professional,\x01",
            "Doctor Guenter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7C0")

    Jump("loc_C7CE")

    label("loc_C7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C7CE")

    label("loc_C7CE")

    TalkEnd(0xFE)
    Return()

    # Function_46_C273 end

    def Function_47_C7D2(): pass

    label("Function_47_C7D2")

    TurnDirection(0x30, 0x1E, 0)
    SetChrSubChip(0x1E, 0x2)
    OP_4B(0x30, 0xFF)

    ChrTalk(
        0x1E,
        (
            "Surely, Doctor Guenter, a man of your caliber\x01",
            "must have a wife, or at least a girlfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "#2409FHaha! I'm afraid I'm living the single life,\x01",
            "and I'm quite enjoying it. I tend to avoid\x01",
            "ladies whenever I can, actually.\x02\x03",
            "#2400FNow, putting my love life aside, this\x01",
            "particular medical examina--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Oh, there's no one special? How lovely!\x01",
            "I-I mean, what a waste!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Well, if that's the case, I think I'll\x01",
            "volunteer. Tonight. You. And. Me. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "#2406FO-Oh, dear, not again. Hahaha...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    SetChrSubChip(0x1E, 0x0)
    OP_4C(0x30, 0xFF)
    Return()

    # Function_47_C7D2 end

    def Function_48_C9DC(): pass

    label("Function_48_C9DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAD7")

    ChrTalk(
        0xFE,
        (
            "I'm observing at St. Ursula in order to\x01",
            "get a feel for how doctors operate. For\x01",
            "future reference, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's easy to understand how they became so\x01",
            "renowned in their respective fields, seeing\x01",
            "how efficient they are.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_CB8D")

    label("loc_CAD7")


    ChrTalk(
        0xFE,
        (
            "I'm observing at St. Ursula in order to\x01",
            "get a feel for how doctors operate. For\x01",
            "future reference, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hopefully, I'm not being a nuisance or\x01",
            "overstaying my welcome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB8D")

    TalkEnd(0xFE)
    Return()

    # Function_48_C9DC end

    def Function_49_CB91(): pass

    label("Function_49_CB91")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(110090, 1000, -5610, 0)
    MoveCamera(68, 34, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20480, 0)
    SetChrPos(0x101, 110500, 0, -6000, 0)
    SetChrPos(0x102, 109200, 0, -6000, 45)
    SetChrPos(0x103, 110500, 0, -7300, 0)
    SetChrPos(0x104, 109200, 0, -7300, 45)
    SetChrPos(0x109, 109200, 0, -4700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    TurnDirection(0xC, 0x101, 0)
    SetChrSubChip(0xC, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#5PHmm... Do I return it to the store or not?\x01",
            "It's so hard to figure out what I want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FUm, excuse me. Is something\x01",
            "bothering you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHuh? No, I wouldn't say I'm particularly\x01",
            "bothered by it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P...the other day, when I went to the city\x01",
            "for the festival, I bought this ribbon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI mean, I thought it was really cute. I'd say\x01",
            "it was more of an impulse buy, if anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PBut, after giving it a lot of thought, I realized\x01",
            "that it's a little TOO cute for my personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003F(A ribbon...)\x02\x03",
            "(That might be just the thing we\x01",
            "need for wrapping the present.)\x02\x03",
            "#0000FWould you mind doing us a favor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PA favor? What do you mean?\x02",
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
            "#12P#0000FSo, we were wondering if you would\x01",
            "let us give that ribbon to Shizuku. If\x01",
            "you can't, I understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWow. So that's what Shizuku has\x01",
            "been up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0304FYep. Nothin' shady about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#0506FR-Randy, why would she think it's shady...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FOn the contrary, claiming it is not suspicious\x01",
            "makes it sound even more so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PIf it's for Shizuku, how could I say no?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PPut it to good use, okay?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x344),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x344, 1)

    ChrTalk(
        0x102,
        (
            "#12P#0100FSorry for asking such a big favor, Meifa.\x01",
            "I know you spent mira on it and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PNo, don't worry about that. At least I'm\x01",
            "not throwing it away like I considered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PWell, good luck with the rest of your collecting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FThanks. I'm sure Shizuku will be ecstatic.\x02",
    )

    CloseMessageWindow()
    OP_29(0x2C, 0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D36D")
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

    label("loc_D36D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(110500, 1000, -6000, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_93(0xC, 0x5A, 0x0)
    SetChrPos(0x0, 110500, 0, -6000, 0)
    SetChrPos(0x1, 110500, 0, -6000, 0)
    SetChrPos(0x2, 110500, 0, -6000, 0)
    SetChrPos(0x3, 110500, 0, -6000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_49_CB91 end

    SaveToFile()

Try(main)
