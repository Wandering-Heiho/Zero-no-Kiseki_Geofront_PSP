from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1530_1.bin",                # FileName
        "t1530",                    # MapName
        "t1530",                    # Location
        0x004F,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 79, 0, 255, 0, 255],
    )

    BuildStringList((
        "t1530_1",                # 0
    ))

    ScpFunction((
        "Function_0_1D0",          # 00, 0
        "Function_1_1D4",          # 01, 1
        "Function_2_17F1",         # 02, 2
        "Function_3_17F5",         # 03, 3
        "Function_4_297C",         # 04, 4
        "Function_5_3CA9",         # 05, 5
        "Function_6_3D7A",         # 06, 6
        "Function_7_4030",         # 07, 7
        "Function_8_5450",         # 08, 8
        "Function_9_6188",         # 09, 9
        "Function_10_62DA",        # 0A, 10
        "Function_11_75ED",        # 0B, 11
        "Function_12_7D82",        # 0C, 12
        "Function_13_7F2F",        # 0D, 13
        "Function_14_8F4A",        # 0E, 14
        "Function_15_9056",        # 0F, 15
        "Function_16_90FE",        # 10, 16
        "Function_17_9281",        # 11, 17
        "Function_18_A0D3",        # 12, 18
        "Function_19_A20A",        # 13, 19
        "Function_20_AB0F",        # 14, 20
        "Function_21_AF33",        # 15, 21
        "Function_22_B058",        # 16, 22
        "Function_23_B11B",        # 17, 23
        "Function_24_B1D3",        # 18, 24
        "Function_25_B808",        # 19, 25
        "Function_26_B812",        # 1A, 26
        "Function_27_BA60",        # 1B, 27
        "Function_28_BC4F",        # 1C, 28
        "Function_29_BE5D",        # 1D, 29
        "Function_30_C23A",        # 1E, 30
        "Function_31_C535",        # 1F, 31
        "Function_32_C6B4",        # 20, 32
        "Function_33_C82E",        # 21, 33
        "Function_34_C968",        # 22, 34
        "Function_35_CB5F",        # 23, 35
        "Function_36_CD03",        # 24, 36
        "Function_37_CEA2",        # 25, 37
        "Function_38_D18A",        # 26, 38
        "Function_39_D389",        # 27, 39
        "Function_40_D4B9",        # 28, 40
        "Function_41_D801",        # 29, 41
        "Function_42_D938",        # 2A, 42
        "Function_43_DA9D",        # 2B, 43
        "Function_44_DBE1",        # 2C, 44
        "Function_45_DEF9",        # 2D, 45
        "Function_46_E0A5",        # 2E, 46
        "Function_47_E262",        # 2F, 47
        "Function_48_E398",        # 30, 48
        "Function_49_E554",        # 31, 49
        "Function_50_E7E8",        # 32, 50
        "Function_51_E95B",        # 33, 51
        "Function_52_EBA6",        # 34, 52
        "Function_53_EDFE",        # 35, 53
        "Function_54_EFDB",        # 36, 54
        "Function_55_F1BE",        # 37, 55
        "Function_56_F34D",        # 38, 56
        "Function_57_F47B",        # 39, 57
        "Function_58_F62F",        # 3A, 58
        "Function_59_F7D0",        # 3B, 59
        "Function_60_F982",        # 3C, 60
        "Function_61_FBCD",        # 3D, 61
        "Function_62_FDE2",        # 3E, 62
        "Function_63_10002",       # 3F, 63
        "Function_64_10185",       # 40, 64
        "Function_65_10314",       # 41, 65
        "Function_66_104B1",       # 42, 66
        "Function_67_1063C",       # 43, 67
        "Function_68_1067C",       # 44, 68
        "Function_69_106B5",       # 45, 69
        "Function_70_107B3",       # 46, 70
        "Function_71_109E3",       # 47, 71
        "Function_72_10AA4",       # 48, 72
        "Function_73_10EFD",       # 49, 73
        "Function_74_111DD",       # 4A, 74
        "Function_75_119D5",       # 4B, 75
        "Function_76_121CE",       # 4C, 76
        "Function_77_136AA",       # 4D, 77
        "Function_78_1413A",       # 4E, 78
    ))


    def Function_0_1D0(): pass

    label("Function_0_1D0")

    Call(1, 1)
    Return()

    # Function_0_1D0 end

    def Function_1_1D4(): pass

    label("Function_1_1D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA")
    Call(0, 9)
    Jump("loc_17F0")

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_200")
    Call(0, 14)
    Jump("loc_17F0")

    label("loc_200")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D")
    Call(1, 76)
    Jump("loc_17F0")

    label("loc_21D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_428")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34D")

    ChrTalk(
        0x8,
        (
            "Those Heiyue Trading men ended up leaving this\x01",
            "morning... Not because we discharged them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They were nowhere near fully recovered, but as\x01",
            "soon as they were able to walk, they were gone...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_345")

    ChrTalk(
        0x10A,
        "#0603FHmph. Cao's men are as stubborn as bulls.\x02",
    )

    CloseMessageWindow()

    label("loc_345")

    SetScenarioFlags(0x0, 0)
    Jump("loc_423")

    label("loc_34D")


    ChrTalk(
        0x8,
        (
            "Those Heiyue Trading men ended up leaving this\x01",
            "morning... Not because we discharged them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They'd suffered multiple gunshot wounds, so we\x01",
            "wanted to keep them longer. They refused our\x01",
            "care, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_423")

    Jump("loc_17ED")

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_49E")

    ChrTalk(
        0x8,
        (
            "I'm glad you were able to speak with\x01",
            "Doctor Guenter, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Feel free to drop by any time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17ED")

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_545")

    ChrTalk(
        0x8,
        (
            "Doctor Guenter is waiting for you on the\x01",
            "fourth floor of the research ward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...You know, I recommend you hurry up\x01",
            "there before he sneaks away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17ED")

    label("loc_545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA")

    ChrTalk(
        0x8,
        (
            "Welcome to St. Ursula Hospital.\x01",
            "How can we be of service today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FWow. Now when was the last time I\x01",
            "stopped by St. Ursula?\x02\x03",
            "The monster attacks, I think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou make it sound like you never\x01",
            "get sick, Sergeant Major.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0504FIt's definitely rare.\x02\x03",
            "#0500FAfter joining the CGF, I've tried to stay in peak\x01",
            "condition. I've got responsibilities, you know?\x01",
            "I don't want a little sickness to get in the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish I had that motivation. Not having to\x01",
            "go to the hospital is a blessing, for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That being said, if you DO start to feel under\x01",
            "the weather, call us immediately. There's only\x01",
            "so much you can do by yourself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 5)
    Jump("loc_894")

    label("loc_7EA")


    ChrTalk(
        0x8,
        (
            "Personally, I think caring for yourself and\x01",
            "being hygienic is the best way to keep\x01",
            "hospitals out of your life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm almost envious of her drive\x01",
            "to stay healthy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_894")

    Jump("loc_17ED")

    label("loc_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_8AA")
    Call(1, 26)
    Jump("loc_17ED")

    label("loc_8AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_97B")

    ChrTalk(
        0x8,
        (
            "Doctor Guenter's lab is on the fourth floor\x01",
            "of the hospital's research ward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once you step onto the roof from the\x01",
            "hospital, you should be able to figure\x01",
            "out where the research ward is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17ED")

    label("loc_97B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A89")

    ChrTalk(
        0x8,
        "Hello, everyone. Welcome to St. Ursula.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're looking for one of the doctors,\x01",
            "unfortunately, they're in a faculty meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Allow me to check with the current doctor in\x01",
            "charge, then please fill out the examination\x01",
            "paperwork.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B4D")

    label("loc_A89")


    ChrTalk(
        0x8,
        (
            "If you're looking for one of the doctors,\x01",
            "unfortunately, they're in a faculty meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Allow me to check with the current doctor in\x01",
            "charge, then please fill out the necessary\x01",
            "paperwork.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4D")

    Jump("loc_17ED")

    label("loc_B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7A")

    ChrTalk(
        0x8,
        (
            "Apparently, getting a checkup from the doctors\x01",
            "here has become something of a tourism fad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I get how experiencing cutting-edge medical\x01",
            "treatment can sound appealing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It feels wrong to see how much longer\x01",
            "patients have to wait for their exams now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D6F")

    label("loc_C7A")


    ChrTalk(
        0x8,
        (
            "Apparently, tourists have made it a point to get\x01",
            "checkups here during their stay in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As long as they don't ask to stay at the hospital,\x01",
            "we don't exactly refuse them, but it's definitely\x01",
            "frustrating knowing their true motive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6F")

    Jump("loc_17ED")

    label("loc_D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_EC9")
    OP_93(0x8, 0x10A, 0x0)
    OP_4B(0x17, 0xFF)

    ChrTalk(
        0x8,
        "Good afternoon, Mr. Crois!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From everyone here at St. Ursula Medical College,\x01",
            "thank you for visiting us again this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm sure the patients will be absolutely delighted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#2804FOh, it's my pleasure, I assure you.\x02\x03",
            "Just figured I'd stop by and see how\x01",
            "Crossbell's favorite hospital is doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x17, 0xFF)
    Jump("loc_17ED")

    label("loc_EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1100")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDD")

    ChrTalk(
        0x8,
        (
            "Cecile and the other nurses often divide their\x01",
            "chores among themselves, allowing them to\x01",
            "take days off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* I should have become a nurse. Since\x01",
            "the administrative staff at St. Ursula is\x01",
            "understaffed, we can't exactly take time off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FB")

    label("loc_FDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_105E")

    ChrTalk(
        0x8,
        (
            "If anything ever happens,\x01",
            "please come visit again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We will make sure to offer\x01",
            "as much help as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FB")

    label("loc_105E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_10EF")

    ChrTalk(
        0x8,
        (
            "Doctor Guenter better return quickly, or\x01",
            "we're going to be in deep trouble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, we're counting on you, everyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10FB")

    label("loc_10EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_10FB")

    label("loc_10FB")

    Jump("loc_17ED")

    label("loc_1100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_126F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F3")

    ChrTalk(
        0x8,
        (
            "Superintendent Kirsch and Marone technically\x01",
            "work under Clark, but between you and me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...everyone tells me that Clark is no match for the\x01",
            "superintendent. He must be a real pushover when\x01",
            "it comes to her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_126A")

    label("loc_11F3")


    ChrTalk(
        0x8,
        (
            "Everyone tells me that Clark is no match for the\x01",
            "superintendent. He must be a real pushover when\x01",
            "it comes to her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126A")

    Jump("loc_17ED")

    label("loc_126F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_143B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138C")

    ChrTalk(
        0x8,
        (
            "Our director is rarely here. He focuses on wandering\x01",
            "from country to country, exchanging medical technology\x01",
            "and scouting out young, bright minds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that I think about it, I don't think I've ever met him\x01",
            "before. I wonder what kind of man he is...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1436")

    label("loc_138C")


    ChrTalk(
        0x8,
        (
            "Our director is an extremely busy man,\x01",
            "so he's rarely here at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Essentially, the hospital's management and\x01",
            "operations are entrusted to the doctors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1436")

    Jump("loc_17ED")

    label("loc_143B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_14D1")

    ChrTalk(
        0x8,
        "Outpatient care has ended for the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The roads get dangerous at night, so try to\x01",
            "be quick if you're visiting someone, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17ED")

    label("loc_14D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_159E")

    ChrTalk(
        0x8,
        (
            "With night fast approaching, outpatient care\x01",
            "has finally started to slow down, little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After what happened to Lytton, be sure you\x01",
            "get home before it gets dark, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17ED")

    label("loc_159E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_17E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176E")

    ChrTalk(
        0x8,
        "Um, excuse me, Miss Neues.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I just wanted to remind you, this IS a professional\x01",
            "environment. If you could refrain from the PDA,\x01",
            "that would be for the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FI'm sorry. It won't happen again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1305FOh, Lloyd. You don't have anything to\x01",
            "apologize for, silly.\x02\x03",
            "#1309FSera, you're just jealous that I have\x01",
            "such a cute little brother, aren't you?\x01",
            "I can hardly blame you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*sigh* Never mind. Just do what you want.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17DF")

    label("loc_176E")


    ChrTalk(
        0x8,
        (
            "Hug, kiss, whatever makes you happy.\x01",
            "I couldn't care less anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Yep, she's disgusted by us.)\x02",
    )

    CloseMessageWindow()

    label("loc_17DF")

    Jump("loc_17ED")

    label("loc_17E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_17ED")

    label("loc_17ED")

    TalkEnd(0x8)

    label("loc_17F0")

    Return()

    # Function_1_1D4 end

    def Function_2_17F1(): pass

    label("Function_2_17F1")

    Call(1, 3)
    Return()

    # Function_2_17F1 end

    def Function_3_17F5(): pass

    label("Function_3_17F5")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_18D4")

    ChrTalk(
        0x9,
        (
            "The hospital director may be gone, but I can\x01",
            "assure you that St. Ursula's management is\x01",
            "in pristine condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Of course, that's mainly due to the trust we\x01",
            "have managed to foster over many years.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_19B1")

    ChrTalk(
        0x9,
        (
            "Sera is fantastic at working as a middle-man of sorts,\x01",
            "connecting the front desk and the hospital within.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In terms of work, I would say Sera does the most,\x01",
            "with Cecile coming in at a close second.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_19B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1A70")

    ChrTalk(
        0x9,
        (
            "'Always assist those who come to us\x01",
            "to the best of our ability' is St. Ursula\x01",
            "Hospital's motto.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Scoundrel or not, we strive to provide\x01",
            "care to each and every patient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_1A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B89")

    ChrTalk(
        0x9,
        (
            "This hospital receives funds from many institutions\x01",
            "from all over Zemuria, but our management\x01",
            "policies are relatively conservative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Those funds exist to support the patients who\x01",
            "cannot pay their medical bills, so we do our\x01",
            "best to soley treat them as such.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_1B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1C75")

    ChrTalk(
        0x9,
        (
            "At the end of the day, we're a hospital. While\x01",
            "there may still be a bottom line to meet, our\x01",
            "patients will always be our top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's always rewarding when you send off\x01",
            "patients with smiles on their faces.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_1C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1D67")

    ChrTalk(
        0x9,
        (
            "St. Ursula's doctors also serve as professors to our\x01",
            "interns and perform individual research. Add them\x01",
            "making their rounds, and they're quite swamped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But I doubt you would think that when\x01",
            "looking at Doctor Guenter...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_1D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E90")

    ChrTalk(
        0x9,
        (
            "I'm in charge of the office work and general\x01",
            "management of the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That includes budget distribution, the handling\x01",
            "of funds for equipment, and even orbal network\x01",
            "maintenance, believe it or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It can be quite stressful at times, but it's worth it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F6C")

    label("loc_1E90")


    ChrTalk(
        0x9,
        (
            "The orbal network stuff is particularly tough.\x01",
            "After all, there's no one in the hospital who\x01",
            "knows how it works other than me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If at all possible, I would love if we could hire\x01",
            "an engineer from Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F6C")

    Jump("loc_2978")

    label("loc_1F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2090")
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0x42, 0xF, 0x0)
    OP_4B(0x42, 0xFF)

    ChrTalk(
        0x9,
        (
            "Are you here to take your physical?\x01",
            "If so, please fill out this paperwork.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since this is your first medical examination\x01",
            "with us, it might take some time to prepare.\x01",
            "Are you fine with waiting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x42,
        "I don't mind. Should I just sit over there?\x02",
    )

    CloseMessageWindow()
    OP_4C(0x42, 0xFF)
    Jump("loc_2978")

    label("loc_2090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2151")

    ChrTalk(
        0x9,
        (
            "Every year, Mr. Crois donates presents to be\x01",
            "handed out to all of our patients. Seeing them\x01",
            "get unwrapped is always a joy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Phew... Mr. Crois, you truly are a great man.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_2151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_23C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E2")

    ChrTalk(
        0x9,
        (
            "I'm considering trying to integrate a key card\x01",
            "system into front desk operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If people could get cards with their information\x01",
            "loaded on to them beforehand, it would greatly\x01",
            "decrease the load our receptionists carry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On the other hand, we would also have to deal\x01",
            "with the production of said cards and the security\x01",
            "of private information. So, perhaps not.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23C1")

    label("loc_22E2")


    ChrTalk(
        0x9,
        (
            "I'm considering trying to integrate a key card\x01",
            "system into front desk operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, progress has been rough due to\x01",
            "many, many bumps. For now, it's going to be\x01",
            "some time before it can be properly installed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C1")

    Jump("loc_2978")

    label("loc_23C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_24FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2490")

    ChrTalk(
        0x9,
        (
            "When I went to have lunch at the cafeteria,\x01",
            "Kirsch kicked me out and told me not\x01",
            "to come while the staff is eating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, dear... I really can't say no to her, can I?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24F6")

    label("loc_2490")


    ChrTalk(
        0x9,
        "Oh, dear. I really can't say no to Kirsch, can I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "She certainly is an...intimidating woman.\x02",
    )

    CloseMessageWindow()

    label("loc_24F6")

    Jump("loc_2978")

    label("loc_24FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_26EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2617")

    ChrTalk(
        0x9,
        (
            "St. Ursula Hospital is connected to Crossbell\x01",
            "City via the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Despite being somewhat experimental, our\x01",
            "appointment service and other systems run\x01",
            "using it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "People that actually take advantage of it are\x01",
            "few and far between, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26E6")

    label("loc_2617")


    ChrTalk(
        0x9,
        (
            "By using our advanced appointment service\x01",
            "on the orbal network, people can avoid wait\x01",
            "times and quickly see their doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "People that actually take advantage of it are\x01",
            "few and far between, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E6")

    Jump("loc_2978")

    label("loc_26EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_279B")

    ChrTalk(
        0x9,
        (
            "Officers, thank you for assisting us in setting\x01",
            "up the fence. You were a great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hopefully, this marks the end of monsters on\x01",
            "St. Ursula grounds...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_279B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_27EC")

    ChrTalk(
        0x9,
        (
            "Officers, have you made any progress with\x01",
            "your investigation?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_27EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_28CD")

    ChrTalk(
        0x9,
        (
            "I'm hesitant to accept that monsters made\x01",
            "their way onto the grounds, but if true, it\x01",
            "needs to be addressed, and quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope you are able to uncover evidence\x01",
            "that proves Lytton's claims, officers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2978")

    label("loc_28CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2978")

    ChrTalk(
        0x9,
        "Welcome to St. Ursula Medical College.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is the front desk, but if you have\x01",
            "any questions or concerns, direct them\x01",
            "to the receptionist to your left.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2978")

    TalkEnd(0x9)
    Return()

    # Function_3_17F5 end

    def Function_4_297C(): pass

    label("Function_4_297C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A1F")
    TurnDirection(0xFE, 0x3C, 0)

    ChrTalk(
        0xFE,
        "Hello. What can we do for you today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this is your first time here, please fill out\x01",
            "these papers for your initial examination.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA5")

    label("loc_2A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2AF0")

    ChrTalk(
        0xFE,
        (
            "The man that was rushed in here on a\x01",
            "stretcher is resting in the ICU now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't seem like he's in any immediate\x01",
            "danger. The doctors say he may even be\x01",
            "able to walk again tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA5")

    label("loc_2AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2BC0")

    ChrTalk(
        0xFE,
        (
            "The man who was carried in here seems\x01",
            "to be in stable condition now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The injury was clearly from some sort of\x01",
            "projectile, most likely a bullet. Everything\x01",
            "about it sets off my alarms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA5")

    label("loc_2BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2C84")
    TurnDirection(0xFE, 0x35, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, are you all right? I can feel the heat\x01",
            "from your forehead from over here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please stick this thermometer under your\x01",
            "armpit and don't move. It'll take a minute.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA5")

    label("loc_2C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2F26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6B")

    ChrTalk(
        0xFE,
        (
            "Have you gotten yourself into some kind\x01",
            "of trouble again, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FN-No, not exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe. It's never boring with you around.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D5C")

    ChrTalk(
        0x102,
        "#0100FSomeone's popular.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E3B")

    label("loc_2D5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DC7")

    ChrTalk(
        0x103,
        (
            "#0200FLloyd does seem to cause a stir within\x01",
            "the nursing staff whenever present.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E3B")

    label("loc_2DC7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E3B")

    ChrTalk(
        0x104,
        (
            "#0306FWait, are you sayin' that the nurses\x01",
            "gossip about Lloyd? This guy? What\x01",
            "the hell, man...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E3B")


    ChrTalk(
        0x101,
        "#0006FHey, I never asked for this.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F21")

    label("loc_2E6B")


    ChrTalk(
        0xFE,
        "I never get tired of you, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, tell me...has there been any\x01",
            "progress with Cecile lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011FWh-What? With Cecile?! That's NEVER\x01",
            "going to happen! E-Excuse me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F21")

    Jump("loc_3CA5")

    label("loc_2F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_3138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3088")

    ChrTalk(
        0xFE,
        (
            "It seems like whenever we sleep nowadays,\x01",
            "we're always woken up by some emergency...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, now that I think about it, this career\x01",
            "is something you would keep doing only if you\x01",
            "REALLY love it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before this job, I didn't know what it meant\x01",
            "to have perseverance, but...it's taught me\x01",
            "just how tough I really am.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3133")

    label("loc_3088")


    ChrTalk(
        0xFE,
        (
            "Unless you REALLY love this career, I can't\x01",
            "see someone continuing to put themselves\x01",
            "through it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cecile is one of those people that I just\x01",
            "know loves their job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3133")

    Jump("loc_3CA5")

    label("loc_3138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_356D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3457")

    ChrTalk(
        0xFE,
        (
            "In the farthest room down the hall, you'll\x01",
            "find the hospital's ICU and our dedicated\x01",
            "x-ray room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "X-rays, if you aren't aware, are the latest creation\x01",
            "from the joint research of St. Ursula Medical College\x01",
            "and a Remiferian inventor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Using a special photo-quartz, photographs\x01",
            "of human bones and internal organs can be\x01",
            "taken by the hospital staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this, we can easily pinpoint the origin of\x01",
            "diseases without having to make an incision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205FI thought this technology was still in the\x01",
            "development stage... I am surprised to hear\x01",
            "it is already being put to use.\x02\x03",
            "#0204FI suppose this goes to show the capabilities\x01",
            "of St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FYeah...I didn't even understand half of\x01",
            "that, but it's obvious that whatever it is,\x01",
            "it's amazing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3568")

    label("loc_3457")


    ChrTalk(
        0xFE,
        (
            "The x-ray is a brand new medical device\x01",
            "that takes photographs of human bones\x01",
            "and internal organs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this, we can easily pinpoint the origin of\x01",
            "diseases without having to make an incision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I still can't say I understand the intricacies\x01",
            "behind it, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3568")

    Jump("loc_3CA5")

    label("loc_356D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_365A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3588")
    Call(1, 23)
    Jump("loc_3655")

    label("loc_3588")


    ChrTalk(
        0xFE,
        (
            "Cecile is the most dedicated person I've ever\x01",
            "met, I think. Not only does she do her work,\x01",
            "she also never fails to help others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would love it if she rubbed off on\x01",
            "Doctor Guenter, that slacker.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3655")

    Jump("loc_3CA5")

    label("loc_365A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_378E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371B")

    ChrTalk(
        0xFE,
        (
            "I've worked at St. Ursula for a while now,\x01",
            "and this is always the busiest time of year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you might expect, the staff here doesn't\x01",
            "have much time to rest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3789")

    label("loc_371B")


    ChrTalk(
        0xFE,
        (
            "I remember feeling like the luckiest girl in\x01",
            "the world when I had the opening day of\x01",
            "the festival off...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3789")

    Jump("loc_3CA5")

    label("loc_378E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3843")

    ChrTalk(
        0xFE,
        (
            "Apparently, Doctor Gailey's son is part\x01",
            "of one of the city's downtown gangs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's probably just in his rebellious\x01",
            "phase. It will pass with time, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA5")

    label("loc_3843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3914")

    ChrTalk(
        0xFE,
        (
            "I recently confronted Cecile and asked her\x01",
            "if she really is friends with Arc en Ciel's\x01",
            "Ilya Platiere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...And she said she was, just like that.\x01",
            "Huh. Guess it wasn't a secret, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA5")

    label("loc_3914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A64")

    ChrTalk(
        0xFE,
        (
            "The girls have been telling me that Cecile\x01",
            "is really close with a famous celebrity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're her little brother. Do you know\x01",
            "who it is?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A24")

    ChrTalk(
        0x101,
        "#0005FMe? Uh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xFE,
        (
            "You don't know? Really? Geez, I just\x01",
            "wanna know who it is...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A5C")

    label("loc_3A24")


    ChrTalk(
        0x101,
        "#0003F(I don't know who it could be besides Ilya.)\x02",
    )

    CloseMessageWindow()

    label("loc_3A5C")

    SetScenarioFlags(0x0, 2)
    Jump("loc_3AE3")

    label("loc_3A64")


    ChrTalk(
        0xFE,
        (
            "The girls have been telling me that Cecile\x01",
            "is really close with a famous celebrity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Who in the world could it be...?\x02",
    )

    CloseMessageWindow()

    label("loc_3AE3")

    Jump("loc_3CA5")

    label("loc_3AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3B8A")

    ChrTalk(
        0xFE,
        (
            "I've heard that Doctor Gailey's son\x01",
            "hangs out with an unsavory crowd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really don't understand why, since\x01",
            "he has such an amazing father.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA5")

    label("loc_3B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_3C0A")

    ChrTalk(
        0xFE,
        "Oh, do you have an appointment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After you finish checking in with the\x01",
            "receptionist, please take a seat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA5")

    label("loc_3C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3C40")

    ChrTalk(
        0xFE,
        "And the next appointment is...you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CA5")

    label("loc_3C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5B")
    Call(1, 5)
    Jump("loc_3CA5")

    label("loc_3C5B")


    ChrTalk(
        0xFE,
        (
            "Please keep this thermometer under\x01",
            "your armpit until I say so, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CA5")

    TalkEnd(0xFE)
    Return()

    # Function_4_297C end

    def Function_5_3CA9(): pass

    label("Function_5_3CA9")

    SetChrSubChip(0x19, 0x0)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        "How are you feeling today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'm burning up... I think I might\x01",
            "have caught a cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, only one way to check. Let's take your\x01",
            "temperature while we wait for the doctor, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    SetChrSubChip(0x19, 0x0)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_5_3CA9 end

    def Function_6_3D7A(): pass

    label("Function_6_3D7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3DB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D98")
    Call(1, 11)
    Jump("loc_3DAB")

    label("loc_3D98")


    ChrTalk(
        0xFE,
        "Hiyaaaaah...!\x02",
    )

    CloseMessageWindow()

    label("loc_3DAB")

    Jump("loc_402C")

    label("loc_3DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3DBE")
    Jump("loc_402C")

    label("loc_3DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3DCC")
    Jump("loc_402C")

    label("loc_3DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3DDA")
    Jump("loc_402C")

    label("loc_3DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3DE8")
    Jump("loc_402C")

    label("loc_3DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_3DF6")
    Jump("loc_402C")

    label("loc_3DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3E04")
    Jump("loc_402C")

    label("loc_3E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3E35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1F")
    Call(1, 11)
    Jump("loc_3E30")

    label("loc_3E1F")


    ChrTalk(
        0xFE,
        "Woooooh...!\x02",
    )

    CloseMessageWindow()

    label("loc_3E30")

    Jump("loc_402C")

    label("loc_3E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E43")
    Jump("loc_402C")

    label("loc_3E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E51")
    Jump("loc_402C")

    label("loc_3E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3E5F")
    Jump("loc_402C")

    label("loc_3E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3FD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7A")
    Call(1, 73)
    Jump("loc_3FD4")

    label("loc_3E7A")

    OP_4B(0x47, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "That reminds me. Have you considered\x01",
            "my proposal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x47,
        (
            "Oh, you mean the one about me giving\x01",
            "a special lecture in the research ward?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x47,
        (
            "Hmm, I don't think it will work out, with the\x01",
            "Anniversary Festival almost here and my\x01",
            "workload increasing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What a shame. However, if you can't do\x01",
            "it, who am I to try and force you?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x47, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_3FD4")

    Jump("loc_402C")

    label("loc_3FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4007")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FF4")
    Call(1, 11)
    Jump("loc_4002")

    label("loc_3FF4")


    ChrTalk(
        0xFE,
        "Gyahhhh!\x02",
    )

    CloseMessageWindow()

    label("loc_4002")

    Jump("loc_402C")

    label("loc_4007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4015")
    Jump("loc_402C")

    label("loc_4015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_4023")
    Jump("loc_402C")

    label("loc_4023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_402C")

    label("loc_402C")

    TalkEnd(0xFE)
    Return()

    # Function_6_3D7A end

    def Function_7_4030(): pass

    label("Function_7_4030")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40C4")
    Jump("loc_410E")

    label("loc_40C4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_40E4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_410E")

    label("loc_40E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4104")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_410E")

    label("loc_4104")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_410E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4141")
    Jump("loc_5448")

    label("loc_4141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_43A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_431E")

    ChrTalk(
        0xFE,
        (
            "When treating someone through the lens of\x01",
            "internal medicine, something always goes\x01",
            "through my mind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When medicine and the body's natural healing\x01",
            "process aren't enough, we can still turn to\x01",
            "surgical procedures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, I ask myself this: Would the cooperation of\x01",
            "these two fields, covering each other's faults,\x01",
            "form the ideal medical care?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder how Doctor Gailey would respond to\x01",
            "that? He's not the most open-minded of people...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43A1")

    label("loc_431E")


    ChrTalk(
        0xFE,
        (
            "Ahem! Please, forget everything I just\x01",
            "said, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't you dare tell Doctor Gailey what\x01",
            "I said, even by accident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A1")

    Jump("loc_5448")

    label("loc_43A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4459")

    ChrTalk(
        0xFE,
        (
            "Hmph. That dog Gailey seems eager to perform\x01",
            "an operation on this morning's patient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose the Surgical Department can carry\x01",
            "its weight after all, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5448")

    label("loc_4459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_451F")

    ChrTalk(
        0xFE,
        (
            "Much to my surprise, Joachim has been avidly\x01",
            "conducting research in his lab as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sure, he skips quite a few shifts, but he never\x01",
            "disappoints when push comes to shove.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5448")

    label("loc_451F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_45A5")

    ChrTalk(
        0xFE,
        "Hmm? Why do you look so flustered, young man?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No one comes to this part of the hospital, aside\x01",
            "from patients.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5448")

    label("loc_45A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_47EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_471D")

    ChrTalk(
        0xFE,
        "*cough* Go on, why are you here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FUm, we were looking for the Neurology and\x01",
            "Pharmacology departments, actually...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Neurology and pharmacology fall under the\x01",
            "umbrella of internal medicine, but they're\x01",
            "still highly experimental fields.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you need to know something about them,\x01",
            "I recommend you talk to Joachim.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47E9")

    label("loc_471D")


    ChrTalk(
        0xFE,
        (
            "Neurology and pharmacology fall under the\x01",
            "umbrella of internal medicine, but they're\x01",
            "still highly experimental fields.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you need to know something about them,\x01",
            "I recommend you talk to Joachim.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47E9")

    Jump("loc_5448")

    label("loc_47EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_47FC")
    Jump("loc_5448")

    label("loc_47FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_480A")
    Jump("loc_5448")

    label("loc_480A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4979")

    ChrTalk(
        0xFE,
        (
            "The other day, I tried to leave the internal\x01",
            "medicine examinations to Gwen. That may\x01",
            "not have been the best decision, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't criticize her skills and knowledge,\x01",
            "but she lacks...proper bedside manner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's something she has to learn in order\x01",
            "to reach the high standards set by previous\x01",
            "St. Ursula Hospital interns.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A30")

    label("loc_4979")


    ChrTalk(
        0xFE,
        (
            "To accurately assess the specificities of a\x01",
            "disease, one must be able to get along well\x01",
            "with their patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gwen still has much to learn when it comes\x01",
            "to that, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A30")

    Jump("loc_5448")

    label("loc_4A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4B16")

    ChrTalk(
        0xFE,
        (
            "Ever since the Anniversary Festival began,\x01",
            "the interns have all seemed spent, as if they\x01",
            "had all their energy drained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*cough* I need to properly scold them, lest\x01",
            "they forget where they are interning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5448")

    label("loc_4B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4EB9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE6")

    ChrTalk(
        0xFE,
        "I'm in your debt, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, I have a lecture coming up, so I'm afraid\x01",
            "I'll have to excuse myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If I need anything else, I'll give the SSS a call.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C94")

    label("loc_4BE6")


    ChrTalk(
        0xFE,
        (
            "The days I spent studying under the guidance\x01",
            "of the Septian Church are irreplaceable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One day, I'll go to Archbishop Eralda and\x01",
            "thank him for all he's done for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C94")

    Jump("loc_4EB4")

    label("loc_4C99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_4CAE")
    Call(1, 75)
    Jump("loc_4EB4")

    label("loc_4CAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_4DC9")

    ChrTalk(
        0xFE,
        (
            "I need you to travel to Archbishop Eralda\x01",
            "at the Crossbell Cathedral and get some\x01",
            "Lupinus Grass from their reserve storage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, and just so you know... The archbishop\x01",
            "can be quite moody. Even more so than me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Be sure to mind your manners around him!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EB4")

    label("loc_4DC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4DDD")
    Call(1, 74)
    Jump("loc_4EB4")

    label("loc_4DDD")


    ChrTalk(
        0xFE,
        (
            "Hmm, can I really trust them to come all\x01",
            "this way for a request like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps I should have asked the\x01",
            "Bracer Guild after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Either way, I don't particularly want\x01",
            "to empty my wallet for this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EB4")

    Jump("loc_5448")

    label("loc_4EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4EC7")
    Jump("loc_5448")

    label("loc_4EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4ED5")
    Jump("loc_5448")

    label("loc_4ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4FB8")

    ChrTalk(
        0xFE,
        (
            "I was the one who told Lytton to write that\x01",
            "lab report the day he was injured... How\x01",
            "was I to know that he'd be attacked?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the rest of the interns are safe and\x01",
            "sound, so I can find comfort in that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5448")

    label("loc_4FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_543F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52C7")

    ChrTalk(
        0xFE,
        (
            "*cough*... Do you need something? I don't\x01",
            "remember hiring new interns...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, perhaps it's merely my first impression,\x01",
            "but you kids seem fairly intelligent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Say, how about you try tackling next year's\x01",
            "entrance exam?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FSounds like we got a chance, guys.\x02\x03",
            "#0304FI can see it now! I, Doctor Orlando, surrounded by\x01",
            "hordes of lovely nurses, beggin' for my company...\x01",
            "Not a shabby way to live, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FGet real, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0111FThat chance is pretty slim. St. Ursula gathers\x01",
            "students here as well as from neighboring countries.\x01",
            "Not to mention, there are many applicants.\x02\x03",
            "#0103FIf I remember correctly, last year's ratio of\x01",
            "accepted to unaccepted was...1:120, I think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303FYep. I give up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FImmediate white flag.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_543A")

    label("loc_52C7")


    ChrTalk(
        0xFE,
        (
            "The research labs here are so cutting edge that even\x01",
            "leaders of the medical field, like Remiferia, acknowledge\x01",
            "their superiority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our gifted students put everything they have into\x01",
            "their studies, hoping to one day become doctors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, we accept students from Crossbell, but\x01",
            "we've also had some come from Erebonia, Calvard,\x01",
            "Remiferia, and even Liberl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_543A")

    Jump("loc_5448")

    label("loc_543F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5448")

    label("loc_5448")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_4030 end

    def Function_8_5450(): pass

    label("Function_8_5450")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5461")
    Jump("loc_6184")

    label("loc_5461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_54F0")

    ChrTalk(
        0xFE,
        (
            "I hear the man that was carried in by ambulance\x01",
            "has already regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's St. Ursula doctors for you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6184")

    label("loc_54F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_54FE")
    Jump("loc_6184")

    label("loc_54FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_561C")

    ChrTalk(
        0xFE,
        (
            "Recently, I had to take another practical\x01",
            "training exam...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This time, I tried to maintain a smile for the\x01",
            "patients, so my evaluation was bumped up\x01",
            "from a B- to a B+.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a small step, but I suppose I'm a little\x01",
            "closer to becoming a full-fledged physician.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6184")

    label("loc_561C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_581D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_577B")

    ChrTalk(
        0xFE,
        (
            "I realized something while I was\x01",
            "watching Doctor Lago perform\x01",
            "an examination earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even a moody man like him was able to be\x01",
            "gentle with his patients, like he was a friend\x01",
            "instead of a doctor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After reflecting on that for a while, I realized\x01",
            "that one big thing I was missing in all of my\x01",
            "practical exams.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5818")

    label("loc_577B")


    ChrTalk(
        0xFE,
        (
            "Even a moody man like him was able to be\x01",
            "gentle with his patients, like he was a friend\x01",
            "instead of a doctor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is that what I'm lacking? Kindness?\x02",
    )

    CloseMessageWindow()

    label("loc_5818")

    Jump("loc_6184")

    label("loc_581D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_5A19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5967")

    ChrTalk(
        0xFE,
        (
            "Out of all the professors that grade my exams,\x01",
            "Doctor Lago is the one who grades the hardest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I asked him some questions about\x01",
            "what I got wrong, he just curtly told me,\x01",
            "'Figure it out for yourself!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Geez! If that's how it is, I'll observe the\x01",
            "heck out of you, Doctor! Just you wait!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5A14")

    label("loc_5967")


    ChrTalk(
        0xFE,
        (
            "Watch out, Doctor Lago! I'll follow you\x01",
            "around and learn everything I can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There has to be some hint or trick on how\x01",
            "to get good grades, and I'm going to find it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A14")

    Jump("loc_6184")

    label("loc_5A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5B10")

    ChrTalk(
        0xFE,
        (
            "Since the doctor isn't in today, I guess I'll have\x01",
            "to collaborate with Lytton. Sure, he might be\x01",
            "sort of smart, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I doubt he's going to be the one to help\x01",
            "me raise my grades, so I can't say I'm too\x01",
            "motivated about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6184")

    label("loc_5B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BCE")

    ChrTalk(
        0xFE,
        (
            "For some reason, the doctors aren't exactly\x01",
            "on the best of terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it's because they're too similar to each\x01",
            "other? Similar things repel, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5C52")

    label("loc_5BCE")


    ChrTalk(
        0xFE,
        (
            "Or perhaps they butted heads at a different hospital\x01",
            "as members of opposing departments... Hah! Yeah,\x01",
            "like that ever happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C52")

    Jump("loc_6184")

    label("loc_5C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5E5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D7C")

    ChrTalk(
        0xFE,
        (
            "Yesterday, I was given practical training\x01",
            "for a good part of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought I nailed it, but Doctor Lago\x01",
            "disagrees, apparently, judging by the B-\x01",
            "he gave me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dang. The road to becoming a capable, female\x01",
            "doctor might be steeper than I thought...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5E56")

    label("loc_5D7C")


    ChrTalk(
        0xFE,
        (
            "In my most recent practical exam, I personally\x01",
            "thought I deserved an easy A+. Everything was\x01",
            "perfect, and I knew all the answers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But a B-? That just means I have to study\x01",
            "longer and harder than I have been.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E56")

    Jump("loc_6184")

    label("loc_5E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5E69")
    Jump("loc_6184")

    label("loc_5E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5E77")
    Jump("loc_6184")

    label("loc_5E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5F5A")

    ChrTalk(
        0xFE,
        (
            "Now that his injury is healed, Lytton has\x01",
            "sprung back to work with his head held high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, Doctor Guenter decided to take\x01",
            "advantage of his good mood and forced poor\x01",
            "Lytton to do most of his work...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6184")

    label("loc_5F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_5F91")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "D-Doctors, please calm down!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6184")

    label("loc_5F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_609C")

    ChrTalk(
        0xFE,
        (
            "At any rate, Lytton sure has a case\x01",
            "of rotten luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After finally getting a chance to write his lab\x01",
            "report, he gets mugged by some monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I doubt he ever anticipated being hospitalized\x01",
            "in the very place he studies. It's pretty ironic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6184")

    label("loc_609C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_617B")

    ChrTalk(
        0xFE,
        (
            "My shift has become a lot more arduous\x01",
            "ever since Lytton was injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Assaulted by some monsters? I can't\x01",
            "help but wonder if that's really the truth. He\x01",
            "was on the roof, after all, wasn't he?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6184")

    label("loc_617B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6184")

    label("loc_6184")

    TalkEnd(0xFE)
    Return()

    # Function_8_5450 end

    def Function_9_6188(): pass

    label("Function_9_6188")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_61C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A6")
    Call(1, 11)
    Jump("loc_61BC")

    label("loc_61A6")


    ChrTalk(
        0xFE,
        "Hiiiitaaaaah...!\x02",
    )

    CloseMessageWindow()

    label("loc_61BC")

    Jump("loc_62D6")

    label("loc_61C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_61CF")
    Jump("loc_62D6")

    label("loc_61CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_61DD")
    Jump("loc_62D6")

    label("loc_61DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_61EB")
    Jump("loc_62D6")

    label("loc_61EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_61F9")
    Jump("loc_62D6")

    label("loc_61F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6207")
    Jump("loc_62D6")

    label("loc_6207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6215")
    Jump("loc_62D6")

    label("loc_6215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6248")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6230")
    Call(1, 11)
    Jump("loc_6243")

    label("loc_6230")


    ChrTalk(
        0xFE,
        "Nyooooooh...!\x02",
    )

    CloseMessageWindow()

    label("loc_6243")

    Jump("loc_62D6")

    label("loc_6248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6256")
    Jump("loc_62D6")

    label("loc_6256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6264")
    Jump("loc_62D6")

    label("loc_6264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6272")
    Jump("loc_62D6")

    label("loc_6272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6280")
    Jump("loc_62D6")

    label("loc_6280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_62B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629B")
    Call(1, 11)
    Jump("loc_62AC")

    label("loc_629B")


    ChrTalk(
        0xFE,
        "Hoooooh...!\x02",
    )

    CloseMessageWindow()

    label("loc_62AC")

    Jump("loc_62D6")

    label("loc_62B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_62BF")
    Jump("loc_62D6")

    label("loc_62BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_62CD")
    Jump("loc_62D6")

    label("loc_62CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_62D6")

    label("loc_62D6")

    TalkEnd(0xFE)
    Return()

    # Function_9_6188 end

    def Function_10_62DA(): pass

    label("Function_10_62DA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_636E")
    Jump("loc_63B8")

    label("loc_636E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_638E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_63B8")

    label("loc_638E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63AE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_63B8")

    label("loc_63AE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63B8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_63EB")
    Jump("loc_75E5")

    label("loc_63EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_667B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65C8")

    ChrTalk(
        0xFE,
        (
            "Whenever I treat patients like the man\x01",
            "from this morning, something always runs\x01",
            "through my head...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even when performing surgical procedures,\x01",
            "we have to rely on Internal Medicine, with\x01",
            "their anaesthesia and IV drips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Therefore, the best treatments are created when\x01",
            "the Surgical and Internal Medicine departments\x01",
            "set aside their differences and work as one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's quite the claim coming from the man\x01",
            "who's always at Lago's throat.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6676")

    label("loc_65C8")


    ChrTalk(
        0xFE,
        (
            "Ahem! Pardon me. I'm afraid I said something\x01",
            "rather out of character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Listen up. You CANNOT tell Lago what I just\x01",
            "said, no matter the circumstances. Are we clear?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6676")

    Jump("loc_75E5")

    label("loc_667B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67B5")

    ChrTalk(
        0xFE,
        (
            "Just earlier, many people in critical condition\x01",
            "were transported here from Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Joachim and I, along with the rest of the staff,\x01",
            "just finished patching them up, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I really am getting old... A few surgeries\x01",
            "and I already want to take a short nap.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_687B")

    label("loc_67B5")


    ChrTalk(
        0xFE,
        (
            "We had some men in critical condition carried in\x01",
            "from the city, but we managed to stabilize them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I really am getting old... A few surgeries\x01",
            "and I already want to take a short nap.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_687B")

    Jump("loc_75E5")

    label("loc_6880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6A9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D5")

    ChrTalk(
        0xFE,
        (
            "By reviewing and repeating what you've learned,\x01",
            "it switches from being stored in the brain's short\x01",
            "term memory to its long term memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, that information is stored in the\x01",
            "brain as knowledge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our interns' merit and success derives from\x01",
            "their habits to properly review material taught.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6A97")

    label("loc_69D5")


    ChrTalk(
        0xFE,
        (
            "By reviewing and repeating what you've learned,\x01",
            "it switches from being stored in the brain's short\x01",
            "term memory to its long term memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Well, that's what Joachim told me, at least.\x02",
    )

    CloseMessageWindow()

    label("loc_6A97")

    Jump("loc_75E5")

    label("loc_6A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C02")

    ChrTalk(
        0xFE,
        (
            "One of the nurses notified me that my son,\x01",
            "Kienz, stopped by the hospital earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Supposedly, my wife coerced him into bringing\x01",
            "my lunchbox all the way to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wouldn't be surprised if he's spouting out all\x01",
            "sorts of spiteful vulgarity right about now, but,\x01",
            "frankly, I'm happy he still brought it for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6CD2")

    label("loc_6C02")


    ChrTalk(
        0xFE,
        (
            "Much to my surprise, I was notified that\x01",
            "my son Kienz stopped by the hospital\x01",
            "earlier to deliver my lunchbox.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, I'm overjoyed. Heh, I should be\x01",
            "careful not to let Lago see me like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CD2")

    Jump("loc_75E5")

    label("loc_6CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6DA9")

    ChrTalk(
        0xFE,
        (
            "Valuable data gathered from our research\x01",
            "projects is stored in the research ward,\x01",
            "which you can find on the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, we like to limit outsiders entering\x01",
            "there as much as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75E5")

    label("loc_6DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6DB7")
    Jump("loc_75E5")

    label("loc_6DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6DC5")
    Jump("loc_75E5")

    label("loc_6DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6F45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EC2")

    ChrTalk(
        0xFE,
        (
            "Apparently, my son took part in the uproar\x01",
            "that happened in Crossbell City yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to the police, it was resolved with\x01",
            "no injuries, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I really wish he wouldn't cause me\x01",
            "to worry like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6F40")

    label("loc_6EC2")


    ChrTalk(
        0xFE,
        (
            "To think that, despite my scolding, he still\x01",
            "went back to that rabble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I'm a pathetic excuse for a father.\x02",
    )

    CloseMessageWindow()

    label("loc_6F40")

    Jump("loc_75E5")

    label("loc_6F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7001")

    ChrTalk(
        0xFE,
        (
            "I had plans to attend Arc en Ciel with my\x01",
            "son tomorrow, but...I'd be shocked if he\x01",
            "went through with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trying so hard to please my kid...\x01",
            "I'm pathetic, aren't I?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75E5")

    label("loc_7001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_72C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71B6")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "Do you remember when those delinquents\x01",
            "were brought to the hospital a couple of\x01",
            "months ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm ashamed to admit it, but a chill ran down\x01",
            "my spine when I thought Kienz might have\x01",
            "been one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite something that traumatic happening,\x01",
            "he still associates himself with that group...\x01",
            "I just don't get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would love it if Kienz stopped constantly\x01",
            "giving me things to worry about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_72C4")

    label("loc_71B6")


    ChrTalk(
        0xFE,
        (
            "You know, I doubt I'm held in too high\x01",
            "regard by my son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For years now, work has caused me to be an\x01",
            "absentee father. I suppose it's no wonder\x01",
            "Kienz doesn't respect me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps I'm partially to blame for my son\x01",
            "getting wrapped up with those delinquents...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72C4")

    Jump("loc_75E5")

    label("loc_72C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_736C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72E4")
    Call(1, 12)
    Jump("loc_7367")

    label("loc_72E4")

    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "Listen up, Ursuline. You're now the chief of\x01",
            "our medical equipment department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You can't act like a student forever!\x02",
    )

    CloseMessageWindow()

    label("loc_7367")

    Jump("loc_75E5")

    label("loc_736C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_737A")
    Jump("loc_75E5")

    label("loc_737A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_757A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_747D")

    ChrTalk(
        0xFE,
        (
            "Surgery is a modern medical practice that has\x01",
            "gradually grown in popularity over the past few\x01",
            "years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "In other words, it's still in its infancy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Directly operating on the human body is\x01",
            "still an unknown for the masses.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7575")

    label("loc_747D")


    ChrTalk(
        0xFE,
        (
            "As things stand, there are also many at St. Ursula,\x01",
            "including Lago, who have prejudices against the\x01",
            "Surgical Department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Old-fashioned farts like him who don't give a damn\x01",
            "about progress in the medical field are the bane of\x01",
            "my existence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7575")

    Jump("loc_75E5")

    label("loc_757A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_75DC")

    ChrTalk(
        0xFE,
        "Ursuline's late again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I swear, that woman will never\x01",
            "learn her lesson.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75E5")

    label("loc_75DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_75E5")

    label("loc_75E5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_62DA end

    def Function_11_75ED(): pass

    label("Function_11_75ED")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0xB, 0xE, 0)
    TurnDirection(0xE, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_77F0")

    ChrTalk(
        0xB,
        (
            "*cough* Just as I was hoping to not\x01",
            "see your face today, here you come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, well, well, Lago. Heard the news yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh* What are you blathering about? Is it that\x01",
            "patient that was in critical condition yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh? Does that mean my miraculous feat\x01",
            "has already reached you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Heh heh. Tell me, have you finally accepted that\x01",
            "the era of internal medicine has come to its end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#4SExcuse me?! Say that to my face!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#4SLooking for a fight, Lago?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D76")

    label("loc_77F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_77FE")
    Jump("loc_7D76")

    label("loc_77FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_780C")
    Jump("loc_7D76")

    label("loc_780C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_781A")
    Jump("loc_7D76")

    label("loc_781A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_7828")
    Jump("loc_7D76")

    label("loc_7828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7836")
    Jump("loc_7D76")

    label("loc_7836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7844")
    Jump("loc_7D76")

    label("loc_7844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7A7F")

    ChrTalk(
        0xB,
        "*cough* If it isn't the imbecile himself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now, when are you planning to shave that\x01",
            "shabby mustache of yours? It hardly befits\x01",
            "a proper doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Proud of that one, are we, Lago?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's a wonder that you haven't fixed that bald\x01",
            "head of yours. It looks like someone took a\x01",
            "torch to an Armorica pasture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "How about you remove that terrible mustache\x01",
            "with those surgeries you love so much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh, yeah? Well, can your precious internal\x01",
            "medicine fix that bald spot of yours?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#4SWhat did you just say?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#4SCome on, Lago! Let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D76")

    label("loc_7A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7A8D")
    Jump("loc_7D76")

    label("loc_7A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7A9B")
    Jump("loc_7D76")

    label("loc_7A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7AA9")
    Jump("loc_7D76")

    label("loc_7AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7AB7")
    Jump("loc_7D76")

    label("loc_7AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_7D51")

    ChrTalk(
        0xB,
        (
            "Oh, if it isn't the disgusting moustache himself!\x01",
            "What do you want? Out with it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Why hello, Lago. I must say, that bald head\x01",
            "of yours is positively shining today. It nearly\x01",
            "blinded me, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmph! It's a shame it didn't. I feel terrible\x01",
            "for our interns...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...learning from a man who only cares about\x01",
            "mutilating our patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hah! At least I'm teaching them content.\x01",
            "What exactly are you teaching again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Long dead techniques from the church?\x01",
            "I find it hard to believe someone who uses\x01",
            "that hogwash can be called a doctor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#4SH-Hogwash?! Say that again, I dare you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#4SI'll say it as many times as it takes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D76")

    label("loc_7D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_7D5F")
    Jump("loc_7D76")

    label("loc_7D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_7D6D")
    Jump("loc_7D76")

    label("loc_7D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7D76")

    label("loc_7D76")

    SetScenarioFlags(0x0, 5)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_11_75ED end

    def Function_12_7D82(): pass

    label("Function_12_7D82")

    OP_4B(0x13, 0xFF)
    SetChrSubChip(0xF, 0x0)
    TurnDirection(0x13, 0xF, 0)

    ChrTalk(
        0xF,
        "Late again, Ursuline?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "A teacher being late for her class is\x01",
            "unacceptable, you know that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Y-You're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I was tinkering with some newly-arrived\x01",
            "equipment last night, but before I knew\x01",
            "it, the sun was coming up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "So, yeah, I was sleeping like a baby\x01",
            "until about twenty minutes ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*sigh* You haven't changed from when\x01",
            "you were a student one bit, Ursuline.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_12_7D82 end

    def Function_13_7F2F(): pass

    label("Function_13_7F2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_80C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_805D")
    TurnDirection(0xFE, 0x14, 0)

    ChrTalk(
        0xFE,
        (
            "Chief Ursuline, don't you think sleeping\x01",
            "here isn't the best idea? You have a\x01",
            "dorm room, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C'mon, you have to wake up before the\x01",
            "doctors stop arguing or else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Gimme...five more minutes... Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's hopeless. Absolutely hopeless...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_80C2")

    label("loc_805D")


    ChrTalk(
        0xFE,
        (
            "I ended up helping out Chief Ursuline\x01",
            "all through the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm pretty tired myself, now.\x02",
    )

    CloseMessageWindow()

    label("loc_80C2")

    Jump("loc_8F46")

    label("loc_80C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_82BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8208")

    ChrTalk(
        0xFE,
        (
            "Everyone knows that Chief Ursuline's intellect\x01",
            "shines the most at nighttime, especially when\x01",
            "it comes to research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thing is, because of that, she pulls a ton\x01",
            "of all-nighters and sleeps in late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite being an associate professor, I don't\x01",
            "find this aspect of her too admirable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_82B6")

    label("loc_8208")


    ChrTalk(
        0xFE,
        (
            "Chief Ursuline is a night owl, so she tends to\x01",
            "sleep in late. Like, very late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite being an associate professor, I don't\x01",
            "find this aspect of her too admirable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82B6")

    Jump("loc_8F46")

    label("loc_82BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_83C7")

    ChrTalk(
        0xFE,
        (
            "Designing medical equipment is challenging.\x01",
            "On the other hand, it's fascinating to deal with\x01",
            "new, up-and-coming treatments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but get excited when I think about\x01",
            "how our designs and prototypes might be used\x01",
            "by everyone in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F46")

    label("loc_83C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_849D")

    ChrTalk(
        0xFE,
        (
            "Geez. I know Chief Ursuline is working, but\x01",
            "I wish she didn't do it to the point of collapsing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And does she really think pulling all-nighters\x01",
            "AND waking up early is going to work out well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F46")

    label("loc_849D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_8578")

    ChrTalk(
        0xFE,
        (
            "It's almost a given that the chief will sleep in\x01",
            "later, so Doctor Gailey doesn't bother getting\x01",
            "angry anymore. We just work around it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I could learn a thing or two about patience\x01",
            "from him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F46")

    label("loc_8578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_85FB")

    ChrTalk(
        0xFE,
        "Another day, another late chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what's new? I guess I'll go ahead\x01",
            "and prepare today's research lab.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F46")

    label("loc_85FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_86A1")

    ChrTalk(
        0xFE,
        (
            "Without Doctor Gailey and Chief Ursuline\x01",
            "around, this exam room feels pretty lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm short on hands, so maybe Flora would\x01",
            "come help me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F46")

    label("loc_86A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_876D")

    ChrTalk(
        0xFE,
        (
            "It never feels like the Anniversary Festival is\x01",
            "actually happening when staying at St. Ursula.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, there's no use in me arguing, so I guess\x01",
            "I'll just read a book or something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F46")

    label("loc_876D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_877B")
    Jump("loc_8F46")

    label("loc_877B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_885D")

    ChrTalk(
        0xFE,
        (
            "People keep reminding me that we're already\x01",
            "on the second day of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After going 72 hours without sleep, researching\x01",
            "with Chief Ursuline, I completely forgot about the\x01",
            "festival...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F46")

    label("loc_885D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_897C")

    ChrTalk(
        0xFE,
        (
            "Chief Ursuline may be the chief of our department,\x01",
            "but she's also an associate professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, she usually prefers to hole herself up in\x01",
            "her lab researching, rather than give lectures...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In that sense, she's in a pretty unique position\x01",
            "here at St. Ursula.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F46")

    label("loc_897C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AB5")

    ChrTalk(
        0xFE,
        (
            "While orbments are developed in a variety of\x01",
            "countries, Remiferia stands out as the leader\x01",
            "when it comes to medical orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, nearly all of the medical equipment\x01",
            "used at St. Ursula Medical College is manufactured\x01",
            "by the Seiland Company, which is Remiferia-based.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8BD3")

    label("loc_8AB5")


    ChrTalk(
        0xFE,
        (
            "Speaking of the Seiland Company, it's probably\x01",
            "the most prominent medical orbment maker in\x01",
            "all of Zemuria. Not to mention, they sponsor us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the Biomedical Engineering Department, we strive\x01",
            "to find ways to improve our current equipment while\x01",
            "still utilizing it in our work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BD3")

    Jump("loc_8F46")

    label("loc_8BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_8BE6")
    Jump("loc_8F46")

    label("loc_8BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_8E10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D46")

    ChrTalk(
        0xFE,
        (
            "The doctors study cutting-edge medical treatments\x01",
            "and technology in the research ward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In particular, the Biomedical Engineering Department\x01",
            "researches the potential of orbal-powered equipment\x01",
            "in modern hospitals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She hasn't arrived yet, but Chief Ursuline is the\x01",
            "head of the Biomedical Engineering Department.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8E0B")

    label("loc_8D46")


    ChrTalk(
        0xFE,
        (
            "She always pushes herself to the limit when it\x01",
            "comes to advancing medical equipment past\x01",
            "the bounds of modern-day surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can you even comprehend how brilliant Chief\x01",
            "Ursuline really is?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E0B")

    Jump("loc_8F46")

    label("loc_8E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_8F3D")

    ChrTalk(
        0xFE,
        (
            "My dream is to someday build a giant hospital\x01",
            "in Erebonia, my home country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And St. Ursula Medical College is the perfect\x01",
            "environment to foster my talent and eventually\x01",
            "reach my goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, this is where Zemuria's best and\x01",
            "brightest physicians gather to collaborate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F46")

    label("loc_8F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8F46")

    label("loc_8F46")

    TalkEnd(0xFE)
    Return()

    # Function_13_7F2F end

    def Function_14_8F4A(): pass

    label("Function_14_8F4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F5F")
    Call(1, 16)
    Jump("loc_9052")

    label("loc_8F5F")


    ChrTalk(
        0x11,
        (
            "#2400FI may help with the hospital rounds, but my\x01",
            "primary focus is research.\x02\x03",
            "Regrettably, this ends up putting quite a\x01",
            "strain on poor Doctor Belldine.\x02\x03",
            "#2406FIf Lytton would hurry back here, I could get\x01",
            "him to finish my busywork for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9052")

    TalkEnd(0xFE)
    Return()

    # Function_14_8F4A end

    def Function_15_9056(): pass

    label("Function_15_9056")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_906B")
    Call(1, 16)
    Jump("loc_90FA")

    label("loc_906B")


    ChrTalk(
        0xFE,
        (
            "I just finished dealing with a rather difficult\x01",
            "patient's medical examination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew... Maybe some black tea would\x01",
            "help cool me down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90FA")

    TalkEnd(0xFE)
    Return()

    # Function_15_9056 end

    def Function_16_90FE(): pass

    label("Function_16_90FE")

    TurnDirection(0x11, 0x12, 0)
    TurnDirection(0x12, 0x11, 0)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "#2400FDoctor Belldine, you look tired as ever.\x02\x03",
            "How about I prescribe you some of my new\x01",
            "supplements? They're full of royal jelly.\x02\x03",
            "#2409FStraight from Armorica Village, too, so its\x01",
            "effectiveness is guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Thank you, but I'll pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Your supplements are TOO effective. I'm\x01",
            "afraid to imagine what would happen if I\x01",
            "got hooked on them.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_16_90FE end

    def Function_17_9281(): pass

    label("Function_17_9281")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9292")
    Jump("loc_A0CF")

    label("loc_9292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_9383")

    ChrTalk(
        0xFE,
        "Hmmhmmhmmmmm... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. When the moon rises, I never get sleepy.\x01",
            "Quite the contrary, actually. My work efficiency\x01",
            "increases nearly sevenfold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right, then. Here's to another seven hours\x01",
            "of straight research!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0CF")

    label("loc_9383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9553")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9490")

    ChrTalk(
        0xFE,
        (
            "When developing medical orbments, safety\x01",
            "should be the top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, they're going to be used on people.\x01",
            "There is absolutely no room for error.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That, right there, is what makes this field so\x01",
            "difficult to begin with.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_954E")

    label("loc_9490")


    ChrTalk(
        0xFE,
        (
            "Safety takes precedent when developing\x01",
            "medical orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even with lab rodent testing, we're unable\x01",
            "to get clear data that would show how well\x01",
            "a certain treatment works on humans.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_954E")

    Jump("loc_A0CF")

    label("loc_9553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9939")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9615")

    ChrTalk(
        0xFE,
        "Oh, did you find the pendant useful?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's made of an extremely durable alloy that\x01",
            "can withstand a monster's bites, so I'm sure\x01",
            "that it will last a long time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9934")

    label("loc_9615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_9705")

    ChrTalk(
        0xFE,
        (
            "That pendant actually took the brunt of an\x01",
            "explosion from a failed experiment, but,\x01",
            "surprisingly enough, it came out scratch-free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet something as lucky as that will be\x01",
            "perfect for a present, don't you agree?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9934")

    label("loc_9705")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9719")
    Call(1, 78)
    Jump("loc_9934")

    label("loc_9719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_988F")

    ChrTalk(
        0xFE,
        (
            "I caused Chaleur nothing but trouble by\x01",
            "sleeping in, since he's been so used to\x01",
            "me being an early riser for the past week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It takes me about twelve alarms to wake up\x01",
            "in the first place, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's strange is that, for some reason,\x01",
            "I can wake up the day after an all-nighter\x01",
            "and be perfectly fine...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "Zzz...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9934")

    label("loc_988F")


    ChrTalk(
        0xFE,
        "...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Umm, if you thought I was asleep there,\x01",
            "you're wrong. I was just concentrating...a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "C-Come, now, everyone! Time for research!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Zzz...\x02",
    )

    CloseMessageWindow()

    label("loc_9934")

    Jump("loc_A0CF")

    label("loc_9939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_9947")
    Jump("loc_A0CF")

    label("loc_9947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_9955")
    Jump("loc_A0CF")

    label("loc_9955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9963")
    Jump("loc_A0CF")

    label("loc_9963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9971")
    Jump("loc_A0CF")

    label("loc_9971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9AE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A8F")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        "Ack!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        "Y-Yes, it's time to begin the lecture.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today, we will be reviewing the inner structure\x01",
            "of quartz utilized within medical equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FMiss? We aren't your students.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI think you're still half-asleep.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    BeginChrThread(0x13, 0, 0, 0)
    Jump("loc_9AE1")

    label("loc_9A8F")


    ChrTalk(
        0xFE,
        (
            "O-Oh, is that so? Then, I apologize. My\x01",
            "lectures aren't meant for outsiders.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AE1")

    Jump("loc_A0CF")

    label("loc_9AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9BF6")
    OP_93(0xFE, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BC4")

    ChrTalk(
        0xFE,
        "Now, uh... Zzz...*snore*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FD-Did she just fall asleep while standing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIt appears so. A practical skill like that may\x01",
            "prove beneficial someday. I should practice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9BF1")

    label("loc_9BC4")


    ChrTalk(
        0xFE,
        "Zzz...*snore*...Gah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Zzz... Zzz...\x02",
    )

    CloseMessageWindow()

    label("loc_9BF1")

    Jump("loc_A0CF")

    label("loc_9BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D9E")

    ChrTalk(
        0xFE,
        (
            "There's one particular engineer who I respect\x01",
            "above all others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's Erika Russell, daughter of the famous\x01",
            "Professor A. Russell, and she currently works\x01",
            "at Liberl's ZCF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite being a woman in her field of choice,\x01",
            "she's a leading authority of orbal technology\x01",
            "in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may be a doctor, but as a fellow woman, I strive to\x01",
            "achieve the same greatness in the medical field.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9E87")

    label("loc_9D9E")


    ChrTalk(
        0xFE,
        (
            "Professor Erika Russell's intelligence and\x01",
            "prowess when it comes to orbal technology\x01",
            "are even on par with her father's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may be a doctor, but as a fellow woman, I strive to\x01",
            "achieve the same greatness in the medical field.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E87")

    Jump("loc_A0CF")

    label("loc_9E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9F37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EA7")
    Call(1, 12)
    Jump("loc_9F32")

    label("loc_9EA7")


    ChrTalk(
        0xFE,
        (
            "(Gailey might make that easier said than done,\x01",
            "though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Are you even listening, Ursuline?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xF, 500)

    ChrTalk(
        0xFE,
        "O-Of course! Every word!\x02",
    )

    CloseMessageWindow()

    label("loc_9F32")

    Jump("loc_A0CF")

    label("loc_9F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_A0AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A033")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        "(*click* *clack* *click* *clack* *click* *clack*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, of course... If we were to use\x01",
            "quartz in this and put it in there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(She doesn't even realize we're here. Her\x01",
            "concentration is impressive...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A0A5")

    label("loc_A033")


    ChrTalk(
        0xFE,
        "Huh? Are my ears playing tricks on me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, weeeell, not like it's my problem.\x01",
            "Back to research I go! ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0A5")

    Jump("loc_A0CF")

    label("loc_A0AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_A0B8")
    Jump("loc_A0CF")

    label("loc_A0B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_A0C6")
    Jump("loc_A0CF")

    label("loc_A0C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A0CF")

    label("loc_A0CF")

    TalkEnd(0xFE)
    Return()

    # Function_17_9281 end

    def Function_18_A0D3(): pass

    label("Function_18_A0D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A18A")

    ChrTalk(
        0xFE,
        "Zzz...*snore*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehehe. It's finally dooooone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this...I've taken another step towards...the\x01",
            "magnificence of Professor Erika...maybe... Zzz...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_A206")

    label("loc_A18A")


    ChrTalk(
        0xFE,
        "Zzz...*snore*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this...I've taken another step towards...the\x01",
            "magnificence of Professor Erika...maybe... Zzz...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A206")

    TalkEnd(0xFE)
    Return()

    # Function_18_A0D3 end

    def Function_19_A20A(): pass

    label("Function_19_A20A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A29C")

    ChrTalk(
        0xFE,
        "*sigh* There they go again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sure, they recognize each other's intelligence,\x01",
            "but I've never once seen them get along...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0B")

    label("loc_A29C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_A2AA")
    Jump("loc_AB0B")

    label("loc_A2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A379")

    ChrTalk(
        0xFE,
        "My shift today lasts all the way until evening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, everything's so peaceful when Doctor\x01",
            "Guenter isn't around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep, I think I'll lay back and relax when\x01",
            "I get back to my room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0B")

    label("loc_A379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A48E")

    ChrTalk(
        0xFE,
        (
            "Doctor Guenter runs all sorts of research projects\x01",
            "in the Neurology and Pharmacology departments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, he looks into anesthesia and supplements\x01",
            "used in surgical procedures, and can even create his own\x01",
            "experimental kinds using the lab equipment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0B")

    label("loc_A48E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_A6A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5EB")

    ChrTalk(
        0xFE,
        (
            "Doctor Guenter runs the Neurology and Pharmacology\x01",
            "departments--two fascinating fields of research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A new, modern medical field that treats people\x01",
            "by tampering with the spirit and mind...\x01",
            "Sounds pretty mysterious, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm aiming to be a physician someday, so I\x01",
            "can't help but admire Doctor Guenter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A69F")

    label("loc_A5EB")


    ChrTalk(
        0xFE,
        (
            "Doctor Guenter runs the Neurology and Pharmacology\x01",
            "departments--two fascinating fields of research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm aiming to be a physician someday, so I\x01",
            "can't help but admire him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A69F")

    Jump("loc_AB0B")

    label("loc_A6A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_A790")

    ChrTalk(
        0xFE,
        "Hmm? You're looking for Doctor Guenter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The doctors and associate professors' labs\x01",
            "are on the research ward's fourth floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make sure not to waltz into one of the other\x01",
            "doctors' labs by accident, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0B")

    label("loc_A790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A9E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8FC")

    ChrTalk(
        0xFE,
        (
            "Doctor Lago and the others are currently\x01",
            "in a faculty meeting. He won't be back today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At faculty meetings, lots of doctors come\x01",
            "from hospitals all over Zemuria to exchange\x01",
            "information, technology, and treatments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Essentially, by complementing each other,\x01",
            "they're able to slowly improve modern\x01",
            "medicine and its practices.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A9E1")

    label("loc_A8FC")


    ChrTalk(
        0xFE,
        (
            "At faculty meetings, lots of doctors come\x01",
            "from hospitals all over Zemuria to exchange\x01",
            "information, technology, and treatments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to push medicine into the future, the\x01",
            "doctors study and research on a daily basis.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9E1")

    Jump("loc_AB0B")

    label("loc_A9E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A9F4")
    Jump("loc_AB0B")

    label("loc_A9F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_AA02")
    Jump("loc_AB0B")

    label("loc_AA02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_AA10")
    Jump("loc_AB0B")

    label("loc_AA10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_AA1E")
    Jump("loc_AB0B")

    label("loc_AA1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_AAD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA39")
    Call(1, 21)
    Jump("loc_AAD3")

    label("loc_AA39")

    TurnDirection(0x15, 0x16, 0)

    ChrTalk(
        0xFE,
        (
            "As much as I would want to, I can't\x01",
            "force him to do anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be wise to tell him to visit\x01",
            "before his condition gets any worse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAD3")

    Jump("loc_AB0B")

    label("loc_AAD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_AAE6")
    Jump("loc_AB0B")

    label("loc_AAE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_AAF4")
    Jump("loc_AB0B")

    label("loc_AAF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_AB02")
    Jump("loc_AB0B")

    label("loc_AB02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_AB0B")

    label("loc_AB0B")

    TalkEnd(0xFE)
    Return()

    # Function_19_A20A end

    def Function_20_AB0F(): pass

    label("Function_20_AB0F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ABA3")
    Jump("loc_ABED")

    label("loc_ABA3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ABC3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ABED")

    label("loc_ABC3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABE3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ABED")

    label("loc_ABE3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ABED")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AC20")
    Jump("loc_AF2B")

    label("loc_AC20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_AC2E")
    Jump("loc_AF2B")

    label("loc_AC2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AC3C")
    Jump("loc_AF2B")

    label("loc_AC3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_AC4A")
    Jump("loc_AF2B")

    label("loc_AC4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_AC58")
    Jump("loc_AF2B")

    label("loc_AC58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_AC66")
    Jump("loc_AF2B")

    label("loc_AC66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AC74")
    Jump("loc_AF2B")

    label("loc_AC74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AC82")
    Jump("loc_AF2B")

    label("loc_AC82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_AC90")
    Jump("loc_AF2B")

    label("loc_AC90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_AD36")

    ChrTalk(
        0xFE,
        (
            "I came to grab my grandpa's medicine\x01",
            "from the doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If only Grandpa would take this seriously\x01",
            "and take his medicine on time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF2B")

    label("loc_AD36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_AD44")
    Jump("loc_AF2B")

    label("loc_AD44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_ADBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD5F")
    Call(1, 21)
    Jump("loc_ADBA")

    label("loc_AD5F")

    SetChrSubChip(0x16, 0x0)

    ChrTalk(
        0xFE,
        (
            "I'm sorry that I always have to be Grandpa's\x01",
            "middle-man for the medicine, doctor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADBA")

    Jump("loc_AF2B")

    label("loc_ADBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_ADCD")
    Jump("loc_AF2B")

    label("loc_ADCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_ADDB")
    Jump("loc_AF2B")

    label("loc_ADDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_ADE9")
    Jump("loc_AF2B")

    label("loc_ADE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_AF2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE95")

    ChrTalk(
        0xFE,
        (
            "I came to grab my grandpa's medicine\x01",
            "from the doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Grandpa hates hospitals more than anything,\x01",
            "so he refuses to come get his medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF2B")

    label("loc_AE95")


    ChrTalk(
        0xFE,
        (
            "He's just stuck in his ways and won't ever\x01",
            "get out of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Basically every doctor said Grandpa\x01",
            "should be hospitalized, but, yeah...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF2B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_AB0F end

    def Function_21_AF33(): pass

    label("Function_21_AF33")

    TurnDirection(0x15, 0x16, 0)
    SetChrSubChip(0x16, 0x0)
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x16,
        (
            "So, it would be better to admit Grandpa\x01",
            "to the hospital after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "That'd definitely be the smartest decision,\x01",
            "but that man is the definition of stubborn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Y-Yeah. I'm so sorry... I'll at least tell him that\x01",
            "he needs to commute to the hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 3)
    Return()

    # Function_21_AF33 end

    def Function_22_B058(): pass

    label("Function_22_B058")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B06D")
    Call(1, 23)
    Jump("loc_B117")

    label("loc_B06D")


    ChrTalk(
        0x44,
        (
            "#1305FOh! Hi, Lloyd!\x02\x03",
            "#1306FI'd love to sit down and chat, but I'm\x01",
            "kinda pressed for time today. Next\x01",
            "time, I promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(She must be swamped with work...)\x02",
    )

    CloseMessageWindow()

    label("loc_B117")

    TalkEnd(0xFE)
    Return()

    # Function_22_B058 end

    def Function_23_B11B(): pass

    label("Function_23_B11B")

    OP_4B(0x44, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x44, 0xA, 0)
    TurnDirection(0xA, 0x44, 0)

    ChrTalk(
        0x44,
        (
            "#1300FThis is the clinical record Doctor Belldine\x01",
            "wanted.\x02\x03",
            "Could you give it to him later? For me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "S-Sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x44,
        "#1309FThank you, Lan.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x44, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_23_B11B end

    def Function_24_B1D3(): pass

    label("Function_24_B1D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B680")

    ChrTalk(
        0x101,
        "#0005FMr. Crois...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#2800FOh, hello, everyone. I'd be lying if I said I\x01",
            "expected to run into the Special Support\x01",
            "Section here.\x02\x03",
            "#2805FNo one was hurt while on duty, I hope?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FNah, nothin' like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FWhat about you? Are you injured, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FI'd be surprised if that was the case.\x02\x03",
            "Even though he has to worry about his responsibilities\x01",
            "as the IBC's CEO, he also runs quite a few philanthropic\x01",
            "projects throughout Crossbell State.\x02\x03",
            "One of those being an annual tradition where he gives\x01",
            "presents to those hospitalized at St. Ursula.\x02\x03",
            "#0102F'If they can't enjoy the Anniversary Festival, I'll bring\x01",
            "some joy to them instead,' he always says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FW-Wow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#2804FHaha. You call it philanthropy, but there's\x01",
            "hardly that much mira involved, Elie. It's\x01",
            "simply a gift from me to them.\x02\x03",
            "#2800FI even occasionally slip out of meetings\x01",
            "to do little things like this.\x02\x03",
            "You can call it self-indulgence, but this is\x01",
            "how I am and how I intend to stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303F(Wasn't ever expectin' to see this side of\x01",
            "him, that's for freakin' sure.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I always thought he was just a nice old man,\x01",
            "but it seems like he is surprisingly thoughtful.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 3)
    Jump("loc_B804")

    label("loc_B680")


    ChrTalk(
        0x17,
        (
            "#2803FOne might call what I'm doing philanthropy,\x01",
            "but I hardly spend a lot of mira on it. It's just\x01",
            "a nice hobby of mine, that's all.\x02\x03",
            "#2800FAnd while a hobby it is, Mariabell never fails\x01",
            "to indulge me in it.\x02\x03",
            "Haha, I'm incredibly thankful for her and the\x01",
            "others that understand and support me.\x02\x03",
            "#2803FIf possible, I hope I can give back to them\x01",
            "with these small shows of gratitude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B804")

    TalkEnd(0xFE)
    Return()

    # Function_24_B1D3 end

    def Function_25_B808(): pass

    label("Function_25_B808")

    TalkBegin(0xFE)
    Call(1, 26)
    TalkEnd(0xFE)
    Return()

    # Function_25_B808 end

    def Function_26_B812(): pass

    label("Function_26_B812")

    OP_4B(0x8, 0xFF)
    OP_4B(0x18, 0xFF)
    TurnDirection(0x8, 0x18, 0)
    TurnDirection(0x18, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9AC")

    ChrTalk(
        0x8,
        "You're Doctor Gailey's son, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you would like, I can call up to his\x01",
            "office right away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "H-Hmph, don't bother. If I never saw his\x01",
            "ugly mug again, it'd still be too soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Mind giving this lunchbox to him? I can't\x01",
            "stand to be in the same building as him,\x01",
            "so I wanna go home already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe. You should be more honest with\x01",
            "yourself, you know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BA57")

    label("loc_B9AC")


    ChrTalk(
        0x18,
        (
            "Th-The only reason I'm here is because\x01",
            "Mom told me to bring this to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Ugh, whatever! Get it to him, all right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Okay, all right. You can leave it to me.\x02",
    )

    CloseMessageWindow()

    label("loc_BA57")

    OP_4C(0x8, 0xFF)
    OP_4C(0x18, 0xFF)
    Return()

    # Function_26_B812 end

    def Function_27_BA60(): pass

    label("Function_27_BA60")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BAF4")
    Jump("loc_BB3E")

    label("loc_BAF4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BB14")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BB3E")

    label("loc_BB14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB34")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BB3E")

    label("loc_BB34")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BB3E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_BBC6")

    ChrTalk(
        0xFE,
        (
            "Yeah, I totally have a cold... Good thing\x01",
            "I came here sooner rather than later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC47")

    label("loc_BBC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_BC47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBE1")
    Call(1, 5)
    Jump("loc_BC47")

    label("loc_BBE1")


    ChrTalk(
        0xFE,
        (
            "Ugh, a thermometer? I can't bear that\x01",
            "metal chill. And don't get me started\x01",
            "on the goosebumps...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC47")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_BA60 end

    def Function_28_BC4F(): pass

    label("Function_28_BC4F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BCE3")
    Jump("loc_BD2D")

    label("loc_BCE3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BD03")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BD2D")

    label("loc_BD03")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD23")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BD2D")

    label("loc_BD23")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BD2D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_BDE2")

    ChrTalk(
        0xFE,
        (
            "I almost thought I was done for when I\x01",
            "burnt myself while I was cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thankfully it seems like it's nothing serious.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE55")

    label("loc_BDE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_BE55")

    ChrTalk(
        0xFE,
        (
            "I can count myself lucky that it's not very\x01",
            "crowded today. Patience and I aren't on\x01",
            "very good terms.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE55")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_BC4F end

    def Function_29_BE5D(): pass

    label("Function_29_BE5D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BEF1")
    Jump("loc_BF3B")

    label("loc_BEF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF11")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BF3B")

    label("loc_BF11")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF31")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BF3B")

    label("loc_BF31")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BF3B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_C036")

    ChrTalk(
        0xFE,
        (
            "I was a little lost when I first got to the\x01",
            "hospital, but I managed to find my way\x01",
            "to my appointment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This really is a pretty awesome place, isn't it?\x01",
            "Good, 'cause my health's in its hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C232")

    label("loc_C036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_C1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C17F")

    ChrTalk(
        0xFE,
        (
            "Huh? Am I crazy, or does that nurse\x01",
            "keep glancing in this direction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow. The nurses here are quality, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FHell yeah! Ain't that right, Cecile?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1309FOh, are we? Heehee, just so you know,\x01",
            "flattery will get you nowhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Cecile, you're too kind for your own good.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C1D0")

    label("loc_C17F")


    ChrTalk(
        0xFE,
        (
            "Hmm, they should be calling my name any\x01",
            "second now. Time to pump myself up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1D0")

    Jump("loc_C232")

    label("loc_C1D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C232")

    ChrTalk(
        0xFE,
        (
            "Phew. This is my first time coming to\x01",
            "St. Ursula, but it's pretty neat so far.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C232")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_BE5D end

    def Function_30_C23A(): pass

    label("Function_30_C23A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C2CE")
    Jump("loc_C318")

    label("loc_C2CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C2EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C318")

    label("loc_C2EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C30E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C318")

    label("loc_C30E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C318")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_C3A3")

    ChrTalk(
        0xFE,
        (
            "Phew, finally finished with the hospital\x01",
            "today. I'm just glad it didn't take long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C52D")

    label("loc_C3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_C45B")

    ChrTalk(
        0xFE,
        (
            "If all you want is a quick cure for\x01",
            "something, it's simpler to just go\x01",
            "to the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I think the checkups here at the\x01",
            "hospital are a lot more thorough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C52D")

    label("loc_C45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C52D")

    ChrTalk(
        0xFE,
        (
            "I'm quite happy with my visits here. I've\x01",
            "yet to meet a member of the staff that\x01",
            "hasn't treated me with respect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "St. Ursula might be a little far from the\x01",
            "city, but the bus fixes that issue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C52D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_C23A end

    def Function_31_C535(): pass

    label("Function_31_C535")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C5C9")
    Jump("loc_C613")

    label("loc_C5C9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C5E9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C613")

    label("loc_C5E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C609")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C613")

    label("loc_C609")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C613")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Up until now, I've only ever relied on\x01",
            "Septian Church remedies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is this hospital thingy really that good?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_C535 end

    def Function_32_C6B4(): pass

    label("Function_32_C6B4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C748")
    Jump("loc_C792")

    label("loc_C748")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C768")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C792")

    label("loc_C768")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C788")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C792")

    label("loc_C788")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C792")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I better get my checkup done by\x01",
            "one of the gorgeous female doctors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "C'mon, just don't be an old man!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_C6B4 end

    def Function_33_C82E(): pass

    label("Function_33_C82E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C8C2")
    Jump("loc_C90C")

    label("loc_C8C2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C8E2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C90C")

    label("loc_C8E2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C902")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C90C")

    label("loc_C902")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C90C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "Hey, this is a hospital! No shouting!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_C82E end

    def Function_34_C968(): pass

    label("Function_34_C968")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C9FC")
    Jump("loc_CA46")

    label("loc_C9FC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CA1C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CA46")

    label("loc_CA1C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA3C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CA46")

    label("loc_CA3C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CA46")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "After finding out that my doctor is actually\x01",
            "a professor, I couldn't help but get a little\x01",
            "nervous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but he ended up being a really nice guy.\x01",
            "It's hard to explain, but his way of speaking\x01",
            "was reassuring. Comforting, even.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_C968 end

    def Function_35_CB5F(): pass

    label("Function_35_CB5F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CBF3")
    Jump("loc_CC3D")

    label("loc_CBF3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CC13")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC3D")

    label("loc_CC13")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC33")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC3D")

    label("loc_CC33")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC3D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "*sigh* I have some meetings to get back\x01",
            "to, so it'd be nice if they let me go early...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This wait is taking forever. How is it not\x01",
            "my turn yet?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_CB5F end

    def Function_36_CD03(): pass

    label("Function_36_CD03")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CD97")
    Jump("loc_CDE1")

    label("loc_CD97")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CDB7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CDE1")

    label("loc_CDB7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CDD7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CDE1")

    label("loc_CDD7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CDE1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I think I might've caught a cold after\x01",
            "sleeping without a blanket on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leaving the window open at night\x01",
            "might not have been the best idea.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_CD03 end

    def Function_37_CEA2(): pass

    label("Function_37_CEA2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CF36")
    Jump("loc_CF80")

    label("loc_CF36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CF56")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF80")

    label("loc_CF56")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF76")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF80")

    label("loc_CF76")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF80")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D10A")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "Zzz...\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D053")
    Jump("loc_D09D")

    label("loc_D053")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D073")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D09D")

    label("loc_D073")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D093")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D09D")

    label("loc_D093")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D09D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Ack! Was I asleep? All this waiting\x01",
            "caused me to doze off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_D182")

    label("loc_D10A")


    ChrTalk(
        0xFE,
        (
            "Phew, that was a close one. Hospital waiting\x01",
            "rooms are my true weakness. A few minutes\x01",
            "in one and I'm fast asleep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D182")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_37_CEA2 end

    def Function_38_D18A(): pass

    label("Function_38_D18A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D21E")
    Jump("loc_D268")

    label("loc_D21E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D23E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D268")

    label("loc_D23E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D25E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D268")

    label("loc_D25E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D268")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "While watching the festival's opening ceremony,\x01",
            "I messed up my hips from being pushed around\x01",
            "in the crowd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's not going to stop me, though. The festival's\x01",
            "only begun! I'm going to get fixed up real quick\x01",
            "and get back to partying!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_38_D18A end

    def Function_39_D389(): pass

    label("Function_39_D389")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D41D")
    Jump("loc_D467")

    label("loc_D41D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D43D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D467")

    label("loc_D43D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D45D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D467")

    label("loc_D45D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D467")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "The hospital's as busy as ever.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_D389 end

    def Function_40_D4B9(): pass

    label("Function_40_D4B9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D54D")
    Jump("loc_D597")

    label("loc_D54D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D56D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D597")

    label("loc_D56D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D58D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D597")

    label("loc_D58D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D597")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D782")
    OP_52(0x27, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x27, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D65A")
    Jump("loc_D6A4")

    label("loc_D65A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D67A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D6A4")

    label("loc_D67A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D69A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D6A4")

    label("loc_D69A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D6A4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Now, now, everything's all right.\x01",
            "I need you to be quiet, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival is five days, remember?\x01",
            "I'll take you once your fever dies down a little.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x1, 6)
    Jump("loc_D7F9")

    label("loc_D782")


    ChrTalk(
        0xFE,
        (
            "This silly boy ended up getting a fever before the\x01",
            "festival. Maybe he was so excited for it that he\x01",
            "barely slept.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7F9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_40_D4B9 end

    def Function_41_D801(): pass

    label("Function_41_D801")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D895")
    Jump("loc_D8DF")

    label("loc_D895")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D8B5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D8DF")

    label("loc_D8B5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D8D5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D8DF")

    label("loc_D8D5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D8DF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Waaaaah! I wanna go to the festival...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_41_D801 end

    def Function_42_D938(): pass

    label("Function_42_D938")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D9CC")
    Jump("loc_DA16")

    label("loc_D9CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D9EC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DA16")

    label("loc_D9EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA0C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DA16")

    label("loc_DA0C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DA16")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "*cough* Ouch! My poor throat... *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Someone must have given me this cold...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_42_D938 end

    def Function_43_DA9D(): pass

    label("Function_43_DA9D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DB31")
    Jump("loc_DB7B")

    label("loc_DB31")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DB51")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DB7B")

    label("loc_DB51")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB71")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DB7B")

    label("loc_DB71")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DB7B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x2)

    ChrTalk(
        0xFE,
        "Hey, come on! Let's not infect me, too, eh?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_DA9D end

    def Function_44_DBE1(): pass

    label("Function_44_DBE1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DC75")
    Jump("loc_DCBF")

    label("loc_DC75")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DC95")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCBF")

    label("loc_DC95")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DCB5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCBF")

    label("loc_DCB5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DCBF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEA8")

    ChrTalk(
        0xFE,
        (
            "I was on the edge of my seat during\x01",
            "yesterday's race in the Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So much so that I fell flat on my face in\x01",
            "the excitement, and I wasn't even in the\x01",
            "race. That's why I'm here, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Yo, does this mean we indirectly\x01",
            "injured this dude?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(U-Uh... I wouldn't think about\x01",
            "it too hard, Randy.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got hurt during the race, but that's my\x01",
            "fault. Important thing is that I had fun, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_DEF1")

    label("loc_DEA8")


    ChrTalk(
        0xFE,
        (
            "Man, it would be awesome if they\x01",
            "made a yearly tradition out of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEF1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_44_DBE1 end

    def Function_45_DEF9(): pass

    label("Function_45_DEF9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DF8D")
    Jump("loc_DFD7")

    label("loc_DF8D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DFAD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFD7")

    label("loc_DFAD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFCD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFD7")

    label("loc_DFCD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DFD7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "*sigh* Of course my follow-up appointment\x01",
            "had to be on the day of the parade...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at least it's not tomorrow. Let's just\x01",
            "get this thing over with.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_45_DEF9 end

    def Function_46_E0A5(): pass

    label("Function_46_E0A5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E139")
    Jump("loc_E183")

    label("loc_E139")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E159")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E183")

    label("loc_E159")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E179")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E183")

    label("loc_E179")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E183")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "If the doc's schedule is right, today marks\x01",
            "the end of my trips to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After this last checkup, I think I'll take a\x01",
            "walk around the festival with the missus.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_46_E0A5 end

    def Function_47_E262(): pass

    label("Function_47_E262")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E2F6")
    Jump("loc_E340")

    label("loc_E2F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E316")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E340")

    label("loc_E316")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E336")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E340")

    label("loc_E336")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E340")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Ohoho, my husband's a child at heart.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_47_E262 end

    def Function_48_E398(): pass

    label("Function_48_E398")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E42C")
    Jump("loc_E476")

    label("loc_E42C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E44C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E476")

    label("loc_E44C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E46C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E476")

    label("loc_E46C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E476")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "After having our checkups, we'll take the\x01",
            "bus back to the city and wait for the ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Awesome. It looks like we'll have plenty of\x01",
            "time to hang out before it leaves.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_48_E398 end

    def Function_49_E554(): pass

    label("Function_49_E554")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E5E8")
    Jump("loc_E632")

    label("loc_E5E8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E608")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E632")

    label("loc_E608")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E628")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E632")

    label("loc_E628")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E632")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "My boyfriend and I are planning to go\x01",
            "to Mishelam tonight.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x2E, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x2E, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E72B")
    Jump("loc_E775")

    label("loc_E72B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E74B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E775")

    label("loc_E74B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E76B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E775")

    label("loc_E76B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E775")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2E, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2E, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Oh, I think he's next. Quick, miss,\x01",
            "call him up! He's ready!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_49_E554 end

    def Function_50_E7E8(): pass

    label("Function_50_E7E8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E87C")
    Jump("loc_E8C6")

    label("loc_E87C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E89C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E8C6")

    label("loc_E89C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E8BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E8C6")

    label("loc_E8BC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E8C6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I genuinely wasn't expecting for this many\x01",
            "people to show up on the closing day of the\x01",
            "festival...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_50_E7E8 end

    def Function_51_E95B(): pass

    label("Function_51_E95B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E9EF")
    Jump("loc_EA39")

    label("loc_E9EF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EA0F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EA39")

    label("loc_EA0F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA2F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EA39")

    label("loc_EA2F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EA39")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_EB30")

    ChrTalk(
        0xFE,
        (
            "The doctors lectured me about how medicine\x01",
            "isn't the end-all and be-all for lifestyle changes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not going to be easy with how demanding\x01",
            "my job is, but you only live once, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9E")

    label("loc_EB30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_EB9E")

    ChrTalk(
        0xFE,
        (
            "*cough* *cough*...I should have come here\x01",
            "sooner, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Work just keeps me so busy...\x02",
    )

    CloseMessageWindow()

    label("loc_EB9E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_51_E95B end

    def Function_52_EBA6(): pass

    label("Function_52_EBA6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EC3A")
    Jump("loc_EC84")

    label("loc_EC3A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EC5A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC84")

    label("loc_EC5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC7A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC84")

    label("loc_EC7A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC84")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_ED64")

    ChrTalk(
        0xFE,
        (
            "The doctor prescribed my father-in-law some\x01",
            "medicine after I explained his situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this, hopefully, his condition will improve,\x01",
            "even if just a little bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EDF6")

    label("loc_ED64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_EDF6")

    ChrTalk(
        0xFE,
        (
            "Waiting for a checkup here feels like it takes\x01",
            "an eternity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you're worrying about someone else,\x01",
            "it feels especially long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDF6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_52_EBA6 end

    def Function_53_EDFE(): pass

    label("Function_53_EDFE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EE92")
    Jump("loc_EEDC")

    label("loc_EE92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EEB2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EEDC")

    label("loc_EEB2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EED2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EEDC")

    label("loc_EED2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EEDC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_EF6D")

    ChrTalk(
        0xFE,
        "Based on the order, I should be up soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, I should've brought a book with me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_EFD3")

    label("loc_EF6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_EFD3")

    ChrTalk(
        0xFE,
        "This might not have been worth the trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, as long as the checkup goes well...\x02",
    )

    CloseMessageWindow()

    label("loc_EFD3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_53_EDFE end

    def Function_54_EFDB(): pass

    label("Function_54_EFDB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F06F")
    Jump("loc_F0B9")

    label("loc_F06F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F08F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F0B9")

    label("loc_F08F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F0AF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F0B9")

    label("loc_F0AF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F0B9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_F192")

    ChrTalk(
        0xFE,
        (
            "The doctor's saying that we're getting closer\x01",
            "and closer to curing my chronic disease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that makes the hard work commuting\x01",
            "here all the time worth it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1B6")

    label("loc_F192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_F1B6")

    ChrTalk(
        0xFE,
        "Is it my turn yet...?\x02",
    )

    CloseMessageWindow()

    label("loc_F1B6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_54_EFDB end

    def Function_55_F1BE(): pass

    label("Function_55_F1BE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F252")
    Jump("loc_F29C")

    label("loc_F252")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F272")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F29C")

    label("loc_F272")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F292")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F29C")

    label("loc_F292")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F29C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_F30A")

    ChrTalk(
        0xFE,
        (
            "I'm just happy my grandpa\x01",
            "seems to be getting better.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F345")

    label("loc_F30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_F345")

    ChrTalk(
        0xFE,
        "Just calm down and wait for your turn, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_F345")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_55_F1BE end

    def Function_56_F34D(): pass

    label("Function_56_F34D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F3E1")
    Jump("loc_F42B")

    label("loc_F3E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F401")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F42B")

    label("loc_F401")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F421")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F42B")

    label("loc_F421")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F42B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Ugh, my head is burning up...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_56_F34D end

    def Function_57_F47B(): pass

    label("Function_57_F47B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F50F")
    Jump("loc_F559")

    label("loc_F50F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F52F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F559")

    label("loc_F52F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F54F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F559")

    label("loc_F54F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F559")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "*cough* Ack...! As soon as I stopped coming\x01",
            "to my appointments, the relapse kicked in.\x01",
            "Just my luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Taking care of your health is a lot\x01",
            "harder than it looks.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_57_F47B end

    def Function_58_F62F(): pass

    label("Function_58_F62F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F6C3")
    Jump("loc_F70D")

    label("loc_F6C3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F6E3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F70D")

    label("loc_F6E3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F703")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F70D")

    label("loc_F703")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F70D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I love how enthusiastic the interns here\x01",
            "are when it comes to studying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It makes me unintentionally want to cheer\x01",
            "them on. Go, interns, go!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_58_F62F end

    def Function_59_F7D0(): pass

    label("Function_59_F7D0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F864")
    Jump("loc_F8AE")

    label("loc_F864")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F884")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F8AE")

    label("loc_F884")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F8A4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F8AE")

    label("loc_F8A4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F8AE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I was doing some cardio by practicing Eastern\x01",
            "self-defense styles, but I got too into it and took\x01",
            "quite the tumble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wahaha! I suppose I did overdo it a tad.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_59_F7D0 end

    def Function_60_F982(): pass

    label("Function_60_F982")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FA16")
    Jump("loc_FA60")

    label("loc_FA16")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FA36")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FA60")

    label("loc_FA36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FA56")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FA60")

    label("loc_FA56")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FA60")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_FB04")

    ChrTalk(
        0xFE,
        "It's almost time for my checkup.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing as the sun's about to set,\x01",
            "maybe I should stay here overnight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBC5")

    label("loc_FB04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_FBC5")

    ChrTalk(
        0xFE,
        (
            "This morning was the first time I've ever\x01",
            "seen someone get carried in by ambulance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, uh, sort of wish I didn't see it, actually.\x01",
            "He was writhing in pain, and...it was bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBC5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_60_F982 end

    def Function_61_FBCD(): pass

    label("Function_61_FBCD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FC61")
    Jump("loc_FCAB")

    label("loc_FC61")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FC81")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FCAB")

    label("loc_FC81")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FCA1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FCAB")

    label("loc_FCA1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FCAB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_FD6F")

    ChrTalk(
        0xFE,
        (
            "A doctor examined her and all, but are\x01",
            "we positive that it's just a cold?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What if it mutates into some incurable\x01",
            "disease? What then?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDDA")

    label("loc_FD6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_FDDA")

    ChrTalk(
        0xFE,
        (
            "Oh, sweet Aidios, please protect my\x01",
            "daughter. Keep her from contracting\x01",
            "something serious...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDDA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_61_FBCD end

    def Function_62_FDE2(): pass

    label("Function_62_FDE2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FE76")
    Jump("loc_FEC0")

    label("loc_FE76")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FE96")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FEC0")

    label("loc_FE96")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FEB6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FEC0")

    label("loc_FEB6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FEC0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_FFA0")

    ChrTalk(
        0xFE,
        (
            "Oh, just give it a rest, Mom! You are\x01",
            "freaking out in front of everyone and\x01",
            "it's embarrassing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The doctor said it was a little cold, so\x01",
            "that's what it is, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FFFA")

    label("loc_FFA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_FFFA")

    ChrTalk(
        0xFE,
        (
            "*cough* *cough* Geez, Mom. You worry\x01",
            "way too much. I said it's just a cold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFFA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_62_FDE2 end

    def Function_63_10002(): pass

    label("Function_63_10002")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10096")
    Jump("loc_100E0")

    label("loc_10096")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_100B6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_100E0")

    label("loc_100B6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_100D6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_100E0")

    label("loc_100D6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_100E0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "Wow, I didn't think a system like this\x01",
            "actually existed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's ginormous... I can't even tell what's\x01",
            "what.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_63_10002 end

    def Function_64_10185(): pass

    label("Function_64_10185")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10219")
    Jump("loc_10263")

    label("loc_10219")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10239")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10263")

    label("loc_10239")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10259")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10263")

    label("loc_10259")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10263")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "This hospital has a distinct smell to it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I kinda like the alcohol scent, though.\x01",
            "That's used for sterilization, right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_64_10185 end

    def Function_65_10314(): pass

    label("Function_65_10314")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_103A8")
    Jump("loc_103F2")

    label("loc_103A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_103C8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_103F2")

    label("loc_103C8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_103E8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_103F2")

    label("loc_103E8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_103F2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "It's bright and early in the morning,\x01",
            "and it's already this crowded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That goes to show how much trust\x01",
            "Crossbellans put in St. Ursula.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_65_10314 end

    def Function_66_104B1(): pass

    label("Function_66_104B1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10545")
    Jump("loc_1058F")

    label("loc_10545")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10565")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1058F")

    label("loc_10565")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10585")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1058F")

    label("loc_10585")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1058F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "The only reason I came so early was\x01",
            "to avoid a massive wait in line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on, make it snappy! My hips\x01",
            "are killing me!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_66_104B1 end

    def Function_67_1063C(): pass

    label("Function_67_1063C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, now I gotta find out where\x01",
            "Granny's room is...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_67_1063C end

    def Function_68_1067C(): pass

    label("Function_68_1067C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Haha, yay! This place is as big as a castle!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_68_1067C end

    def Function_69_106B5(): pass

    label("Function_69_106B5")

    TalkBegin(0xFE)
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0x42, 0xF, 0x0)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "Are you here to take your physical?\x01",
            "If so, please fill out this paperwork.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since this is your first time having a\x01",
            "checkup with us, it might take some\x01",
            "time. Are you okay with waiting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No big deal. I don't mind.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_69_106B5 end

    def Function_70_107B3(): pass

    label("Function_70_107B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10901")

    ChrTalk(
        0xFE,
        (
            "Hmm, let's see here...\x01",
            "'General Checkup Information'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'For preemptive care, we recommend patients have a\x01",
            "comprehensive examination that utilizes our most\x01",
            "advanced equipment to detect diseases in advance.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see. St. Ursula Hospital really does have it all.\x01",
            "Most other hospitals don't even offer this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109DF")

    label("loc_10901")


    ChrTalk(
        0xFE,
        (
            "Um, maybe I should have a checkup?\x01",
            "But I don't have the time for one now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A bastion of cutting-edge medical technology,\x01",
            "huh? I wasn't sure, but people really weren't\x01",
            "lying when they were talking up St. Ursula.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109DF")

    TalkEnd(0xFE)
    Return()

    # Function_70_107B3 end

    def Function_71_109E3(): pass

    label("Function_71_109E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_10A54")

    ChrTalk(
        0x45,
        (
            "I-I ate way too much food at dinner. It was\x01",
            "delicious, but my stomach is paying the price!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AA0")

    label("loc_10A54")


    ChrTalk(
        0x45,
        "M-My stomach is tearing itself apart...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x45,
        "Isn't it my turn yet?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_10AA0")

    TalkEnd(0xFE)
    Return()

    # Function_71_109E3 end

    def Function_72_10AA4(): pass

    label("Function_72_10AA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E42")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#0005FYou're with the Bracer Guild...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FIf you're here, does that mean\x01",
            "something happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unfortunately so. A traveler was taking a\x01",
            "shortcut through a thicket and was bitten\x01",
            "by an extremely venomous snake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as we found him, we carried him\x01",
            "here as fast as we could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, Aeolia was the one who gave him\x01",
            "first aid, so I think he'll pull through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FFirst aid? Can't say I knew bracers\x01",
            "were trained in medical treatment,\x01",
            "let alone for snakebites.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aeolia is a bit of an outlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's from Remiferia, one of the most\x01",
            "medically advanced places in Zemuria.\x01",
            "She even got her medical license there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211FA doctor, you say? All I see is a woman\x01",
            "who cannot keep her hands to herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, well, she might be a bit more clingy\x01",
            "than most, but she's an amazing gal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_10EF9")

    label("loc_10E42")


    ChrTalk(
        0xFE,
        (
            "Aeolia is actually from Remiferia, same\x01",
            "place she earned her medical license.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sure, she's got an eye for everything cute,\x01",
            "but she's a real genius when it comes to\x01",
            "medicine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EF9")

    TalkEnd(0xFE)
    Return()

    # Function_72_10AA4 end

    def Function_73_10EFD(): pass

    label("Function_73_10EFD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_111D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11135")
    OP_4B(0x47, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0x47, 0xB, 0)

    ChrTalk(
        0xB,
        "The traveler is currently resting in the ICU.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If treated poorly, I might have had to resort to\x01",
            "amputation, but luckily his leg is still there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks to you, Aeolia, everything went as\x01",
            "planned. Your help truly is invaluable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x47,
        (
            "No, I wouldn't go that far. I did what was\x01",
            "expected of a bracer, and that's that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0307F#4S(Damn it, someone break my leg!)\x02\x03",
            "#0304F(If that's what it takes for the lovely Aeolia\x01",
            "to nurse me back to health, I'm ready.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F(This enthusiasm is futile. Cease.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    OP_4C(0x47, 0xFF)
    OP_4C(0xB, 0xFF)
    Jump("loc_111D9")

    label("loc_11135")


    ChrTalk(
        0x47,
        (
            "Oh, oh, oh! It's Tio and the Special\x01",
            "Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x47,
        (
            "Heehee, give me a few minutes and I'll\x01",
            "give you aaaall the hugs and kisses! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0206FDeclined.\x02",
    )

    CloseMessageWindow()

    label("loc_111D9")

    TalkEnd(0xFE)
    Return()

    # Function_73_10EFD end

    def Function_74_111DD(): pass

    label("Function_74_111DD")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(49870, 1000, 57910, 0)
    MoveCamera(64, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20540, 0)
    SetChrPos(0x101, 48800, 0, 57000, 0)
    SetChrPos(0x102, 50000, 0, 57000, 0)
    SetChrPos(0x103, 48800, 0, 55500, 0)
    SetChrPos(0x104, 50000, 0, 55500, 0)
    SetChrSubChip(0xC, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#5PHmm, can I really trust them to come all\x01",
            "this way for a request like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PPerhaps I should have asked the\x01",
            "Bracer Guild after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PEither way, I don't particularly want\x01",
            "to empty my wallet for this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006F(Hard to get a word in edgewise...)\x02\x03",
            "#0000FExcuse me, sir. We're from the Crossbell Police\x01",
            "Department, Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xC, 0x1)

    ChrTalk(
        0xC,
        "#5POh, you came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI've been waiting for you. Come, now,\x01",
            "take a seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FThanks, but we're okay. Standing's fine.\x02\x03",
            "#0000FDoctor, would you mind explaining the\x01",
            "details of your support request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PY-Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PAhem! My request is simple, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI need you to retrieve a certain herb that\x01",
            "we use in our Internal Medicine lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIt's called Lupinus Grass. Sadly, it's become\x01",
            "something of a rarity these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0205FLupinus... As in the Lupinus River, which\x01",
            "flows through Crossbell City's harbor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FCould be. So, you want us to find the grass\x01",
            "ourselves and bring it back here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PNo, not exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIn actuality, I need you to obtain some from\x01",
            "the Crossbell Cathedral. They should have\x01",
            "a small reserve supply of the herb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PArchbishop Eralda has already agreed to\x01",
            "my request, so I would like for you to go\x01",
            "there as my representative and pick it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI'd go myself, normally, but...I'm afraid I'm\x01",
            "preoccupied at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FI think we can oblige, Doctor Lago. You said\x01",
            "Archbishop Eralda of the Crossbell Cathedral?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PThat's him. Thanks, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5POnce you get the Lupinus Grass, please\x01",
            "bring it back here right away.\x02",
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
            "[Rare Herb Retrieval]\x07\x00",
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
    OP_29(0x13, 0x1, 0x0)
    SetChrPos(0x0, 50500, 0, 57500, 0)
    SetChrPos(0x1, 50500, 0, 57500, 0)
    SetChrPos(0x2, 50500, 0, 57500, 0)
    SetChrPos(0x3, 50500, 0, 57500, 0)
    Sleep(500)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_74_111DD end

    def Function_75_119D5(): pass

    label("Function_75_119D5")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(49870, 1000, 57910, 0)
    MoveCamera(64, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20540, 0)
    SetChrPos(0x101, 48800, 0, 57000, 0)
    SetChrPos(0x102, 50000, 0, 57000, 0)
    SetChrPos(0x103, 48800, 0, 55500, 0)
    SetChrPos(0x104, 50000, 0, 55500, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xC,
        "#5POh, back already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PDid you get the Lupinus Grass like I asked?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FYes, sir.\x02\x03",
            "Mind checking if it's the right thing?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x341),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x341, 1)

    ChrTalk(
        0xC,
        "#5PHmm, yes, this looks authentic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PNow, uh... Hmm, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI'm sure the archbishop told you\x01",
            "some stories about me, didn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FNo, nothing in particular.\x02\x03",
            "#0200FApparently, he did not even open the letter\x01",
            "you sent, Doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PBig surprise there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PConsidering how long it took him to\x01",
            "respond, I thought that might have\x01",
            "been the case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FSo, that whole thing about him agreein'\x01",
            "to the deal was a big fat lie.\x02\x03",
            "#0306FWell, it wasn't easy getting the stuff,\x01",
            "since we came with no appointment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI truly am sorry about that. It's hard to\x01",
            "talk about these sort of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PDue to our strained relationship, I turned\x01",
            "to the Special Support Section to go in\x01",
            "my stead. That's the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FOne of the priests there filled us in.\x02\x03",
            "Despite his stubbornness, I'm almost positive\x01",
            "that Archbishop Eralda approves of the path\x01",
            "you chose, Doctor Lago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYou know, I've always respected him. That\x01",
            "much has never changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PSomeday, when medical care has progressed\x01",
            "and become more accessible, I'll meet with him\x01",
            "to apologize and thank him for all he's done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FI think he would appreciate that, sir. I think\x01",
            "he would appreciate that quite a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PAnyway, you've been a great help to St. Ursula.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIf I need another courier or something in the future,\x01",
            "I'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FAny time, Doctor.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Rare Herb Retrieval]\x07\x00",
            " completed!\x02",
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
    OP_29(0x13, 0x1, 0x3)
    OP_29(0x13, 0x4, 0x10)
    SetChrPos(0x0, 50500, 0, 57500, 0)
    SetChrPos(0x1, 50500, 0, 57500, 0)
    SetChrPos(0x2, 50500, 0, 57500, 0)
    SetChrPos(0x3, 50500, 0, 57500, 0)
    Sleep(500)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_75_119D5 end

    def Function_76_121CE(): pass

    label("Function_76_121CE")

    OP_4B(0x8, 0xFF)
    OP_4B(0x15, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x0, 0x8, 0)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15620, 400, 7920, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 14410, 0, 6710, 90)
    SetChrPos(0x102, 13420, 0, 4760, 90)
    SetChrPos(0x103, 12160, 0, 4910, 90)
    SetChrPos(0x104, 12810, 0, 6540, 90)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    SetChrPos(0x15, 11940, 1230, 16600, 0)
    SetChrFlags(0x15, 0x40)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#11P*sigh* Doctor, where could you be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FGood afternoon, Sera.\x02\x03",
            "We saw the support request you submitted.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        "#11POh, the Special Support Section?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PThank Aidios you're here.\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#11PWait, what's going on again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FU-Umm, you don't remember?\x02\x03",
            "#0005FOne of St. Ursula's doctors has gone missing,\x01",
            "and we were asked to search for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0305FY'know, lady, you seem awfully calm about\x01",
            "this whole thing. What gives?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYes, well, I wouldn't call this calm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI think saying I'm fed up would be\x01",
            "a bit more accurate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105FF-Fed up? Is that what you should be saying...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FCould you clarify the details of your request?\x02\x03",
            "#0200FThere seems to be a misunderstanding over\x01",
            "how severe we each consider a missing\x01",
            "persons case to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POh, I should explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe doctor in question is a man named\x01",
            "Joachim Guenter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PDoctor Guenter is, well... Despite being an\x01",
            "expert in his field, he sometimes disappears\x01",
            "at the most inconvenient times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FDoctor Guenter... Wasn't he that doctor with\x01",
            "the blue hair and glasses from before?\x02\x03",
            "#0005FAnd, by missing, you really meant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0306FThe guy's playin' hooky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PIf we're being blunt, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe hospital still has a lot of things left\x01",
            "on its plate, and with him gone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FSo, what you're trying to tell us...\x02\x03",
            "#0100F...is that you have no idea where the\x01",
            "doctor could have gone off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PY-Yes. Unfortunately, that's exactly right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'm sorry, everyone. It might have been\x01",
            "irresponsible for me to write the request\x01",
            "like I did. 'Gone missing' and all that.\x02",
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
    Sleep(1200)

    ChrTalk(
        0x101,
        "#6P#0003FWhat do you think, guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FI think we could postpone this, if we want.\x02\x03",
            "#0200FBased on the information given, the level\x01",
            "of urgency seems quite low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FSince Sera's the one askin' us, I wanna\x01",
            "follow up on this if we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0105FI suppose there's still a chance he could've\x01",
            "gotten mixed up into some trouble...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Man's Voice",
        "#4SS-Sera!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_12BE6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_12BE6)

    def lambda_12BF3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_12BF3)

    def lambda_12C00():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_12C00)

    def lambda_12C0D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_12C0D)

    def lambda_12C1A():

        label("loc_12C1A")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_12C1A")

    QueueWorkItem2(0x8, 1, lambda_12C1A)
    OP_68(14200, 600, 9330, 1500)
    MoveCamera(45, 18, 0, 1500)
    OP_6E(400, 1500)
    SetCameraDistance(25000, 1500)
    Sleep(1500)
    ClearChrFlags(0x15, 0x80)
    OP_95(0x15, 11810, 0, 9710, 7000, 0x0)

    def lambda_12C76():
        OP_95(0xFE, 13460, 0, 8990, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_12C76)
    OP_68(14770, 600, 8480, 500)
    MoveCamera(45, 18, 0, 500)
    OP_6E(400, 500)
    SetCameraDistance(25000, 500)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    OP_93(0x8, 0x10E, 0x0)

    ChrTalk(
        0x15,
        "#5P*pant* *pant* *pant*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PLytton, how many times do I have to tell you?\x01",
            "Shouting in the hospital is against the rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PS-Sorry about that. I didn't actually mean to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FHey, if it isn't our favorite assault victim!\x01",
            "How ya holdin' up, man?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x104, 0)

    ChrTalk(
        0x15,
        (
            "#5PWh-What? Oh! Hey, everyone. I really\x01",
            "appreciate everything you did for m--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x8, 0)

    ChrTalk(
        0x15,
        (
            "#5PWait, that's not the problem right now!\x01",
            "Sera, where the heck is Doctor Guenter?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAbout that... I'm sorry, Lytton. He still\x01",
            "isn't back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PY-You're joking, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5POh, Goddess, what am I going to do\x01",
            "about all this work? I'm just an intern...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PArgh! There's no time to complain!\x01",
            "I can do some of it, at the very least!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12F9E():

        label("loc_12F9E")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_12F9E")

    QueueWorkItem2(0x8, 1, lambda_12F9E)
    OP_95(0x15, 11810, 0, 9710, 6000, 0x0)
    OP_95(0x15, 11940, 1230, 16600, 7000, 0x0)
    SetChrFlags(0x15, 0x80)
    Sleep(800)

    ChrTalk(
        0x101,
        "#6P#0005FWhat was up with that?\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_13008():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13008)

    def lambda_13015():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_13015)

    def lambda_13022():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_13022)

    def lambda_1302F():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1302F)
    Sleep(100)
    EndChrThread(0x8, 0x1)
    OP_93(0x8, 0x10E, 0x12C)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#11POh, Doctor Guenter just likes to coerce\x01",
            "Lytton into doing his work pretty regularly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThis time, I believe he's desperately trying\x01",
            "to follow up with the mountain of invoices\x01",
            "the doctor has been avoiding...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0106FThat must make his job ten times harder...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FYeah, doubt we can leave this one hangin',\x01",
            "if that's the case.\x02\x03",
            "#0300FWe gotta do it for poor Lytton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0206FI agree. My pity for him is becoming\x01",
            "too much to bear...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FWell, all right, then.\x02\x03",
            "#0000FSera, do you have any idea where\x01",
            "Doctor Guenter might have gone?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#11POh? Does this mean you're accepting\x01",
            "my request? Thank you, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PRecently, Doctor Guenter has been talking\x01",
            "about participating in an Anniversary Festival\x01",
            "fishing tournament...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's not impossible that his disappearance had\x01",
            "something to do with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PConsidering he left during work hours, he\x01",
            "should probably still be wearing his labcoat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI'm sure he'll stick out like a sore thumb.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FA fishing tournament? I guess fishing is\x01",
            "more than just a hobby to him.\x02\x03",
            "#0003F(If it involves fishing, I'm sure the Fisherman's\x01",
            "Guild on East Street will know something.)\x02\x03",
            "#0000FAnyway, we accept your request, Sera.\x01",
            "Once we find him, we'll contact the\x01",
            "hospital and bring him back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PSounds great. Thank you very much.\x02",
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
            "[Missing Doctor]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(14410, 1000, 6710, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 14410, 0, 6710, 90)
    SetChrPos(0x1, 14410, 0, 6710, 90)
    SetChrPos(0x2, 14410, 0, 6710, 90)
    SetChrPos(0x3, 14410, 0, 6710, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x15, 0xFF)
    ClearChrFlags(0x15, 0x40)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    OP_29(0x16, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_76_121CE end

    def Function_77_136AA(): pass

    label("Function_77_136AA")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_68(15690, 500, 7880, 0)
    MoveCamera(51, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25880, 0)
    SetChrPos(0x101, 14410, 0, 6210, 0)
    SetChrPos(0x102, 13420, 0, 4260, 0)
    SetChrPos(0x104, 12160, 0, 4410, 0)
    SetChrPos(0x103, 12810, 0, 6140, 0)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    SetChrPos(0x11, 13650, 0, 7450, 90)
    SetChrFlags(0x11, 0x40)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    Sleep(500)
    SetCameraDistance(24880, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#11PWhere in the world were you, Doctor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PDue to your absence, staff and patients have\x01",
            "been very inconvenienced...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#2409FHaha! Well, if you must know, I was competing\x01",
            "in an intense event known as the Fisher Cup.\x02\x03",
            "#2400FThe Fisherman's Guild ran it, and being a\x01",
            "member of it myself, I couldn't exactly skip\x01",
            "it, could I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PDoctor, this is serious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou do realize that Lytton is filling in\x01",
            "for you as we speak, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#2405FOh? Lytton is?\x02\x03",
            "#2400FHaha, I really am blessed to have such a\x01",
            "capable pupil.\x02\x03",
            "#2403FI think it would be rude of me to rain on his\x01",
            "parade, considering how hard he's working.\x01",
            "So, why not let things continue as they are?\x02\x03",
            "#2409FYes, I think that's for the best. It will be very\x01",
            "educational for him. Very educational, indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#4S#200WGet #200Wback #200Wto #200Wwork#200W\x01",
            "#200Wright #200Wthis #200Winstant#200W.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#6P#2406FYes, ma'am.\x02",
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
    Sleep(1200)

    ChrTalk(
        0x101,
        "#12P#0006F(Is this guy...always like this?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200F(If he's qualified to teach, as well, he must\x01",
            "be quite gifted in his field...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0309F(You ask me, he's workin' smarter, not harder.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106F(It figures that you'd sympathize with\x01",
            "his work ethic...)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x12C)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#5P#2400FWell, ladies and gentlemen, it's been a pleasure,\x01",
            "but I'll have to excuse myself here.\x02\x03",
            "#2409FNext time we meet, let's go fishing again,\x01",
            "all right? I won't take no as an answer!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13D69():

        label("loc_13D69")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_13D69")

    QueueWorkItem2(0x0, 1, lambda_13D69)

    def lambda_13D7B():

        label("loc_13D7B")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_13D7B")

    QueueWorkItem2(0x1, 1, lambda_13D7B)

    def lambda_13D8D():

        label("loc_13D8D")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_13D8D")

    QueueWorkItem2(0x2, 1, lambda_13D8D)

    def lambda_13D9F():

        label("loc_13D9F")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_13D9F")

    QueueWorkItem2(0x3, 1, lambda_13D9F)

    def lambda_13DB1():

        label("loc_13DB1")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_13DB1")

    QueueWorkItem2(0x8, 1, lambda_13DB1)
    OP_95(0x11, 11810, 0, 9710, 2000, 0x0)
    OP_95(0x11, 11940, 1230, 16600, 2000, 0x0)
    SetChrFlags(0x11, 0x80)
    Sleep(800)

    ChrTalk(
        0x8,
        "#11P'Again'?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_13E15():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13E15)

    def lambda_13E22():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_13E22)

    def lambda_13E2F():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_13E2F)

    def lambda_13E3C():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_13E3C)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#0003FU-Um, ignore that. I don't know what\x01",
            "he's talking about.\x02\x03",
            "#0000FSo, do you need anything else from us?\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)
    OP_93(0x8, 0x10E, 0x12C)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#11PAh, no, that should be everything. Thanks\x01",
            "for the help. You four are lifesavers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYou brought him back in record time, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWe'll be calling you if something like this\x01",
            "happens again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI have a good feeling you all will be able\x01",
            "to handle whatever we throw at you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FOf course. You can count on us, Sera.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Missing Doctor]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(14410, 1000, 6710, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 14410, 0, 6710, 90)
    SetChrPos(0x1, 14410, 0, 6710, 90)
    SetChrPos(0x2, 14410, 0, 6710, 90)
    SetChrPos(0x3, 14410, 0, 6710, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x11, 0xFF)
    ClearChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    OP_29(0x16, 0x4, 0x10)
    OP_29(0x16, 0x1, 0x6)
    SetScenarioFlags(0x0, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_77_136AA end

    def Function_78_1413A(): pass

    label("Function_78_1413A")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(55410, 1000, -55440, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, 55250, 0, -54750, 135)
    SetChrPos(0x102, 54080, 0, -54680, 90)
    SetChrPos(0x103, 54670, 0, -57660, 45)
    SetChrPos(0x104, 53490, 0, -57740, 45)
    SetChrPos(0x109, 52630, 0, -56430, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_93(0x13, 0x10E, 0x0)
    SetChrSubChip(0x13, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x13,
        "#11P*yaaaaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PStaying up all night in the research lab\x01",
            "might not have been the best decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PMy goal was to make something portable\x01",
            "and more convenient, but it didn't pan out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005F(It sounds like she specializes in medical\x01",
            "equipment.)\x02\x03",
            "#0003F(Who knows? She might have something\x01",
            "that would be a good addition to Shizuku's\x01",
            "present.)\x02\x03",
            "#0000FExcuse me, ma'am. Do you have a minute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#11PYes? What is it?\x02",
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
            "#5P#0000FSo, we were wondering if you have\x01",
            "anything you're willing to give away.\x01",
            "If you don't, I completely understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11POh, is that all? I shouldn't be surprised\x01",
            "that Shizuku loves cute things, too. Girls\x01",
            "will be girls, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#11PNow, let me see... This might do the trick.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x342),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x342, 1)

    ChrTalk(
        0x101,
        "#5P#0005FIs this a pendant?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PThat it is. The kind you can place a gem\x01",
            "inside of, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PMy research last night into portable, pendant-like\x01",
            "medical tools was a spectacular failure, and this\x01",
            "is the byproduct of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0205FPortable...medical equipment? Is that the standard\x01",
            "in hospitals nowadays?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11POh, no. It was just tests. No one can find practical\x01",
            "significance in using them yet, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PThe idea is that you use quartz within the pendant\x01",
            "to generate healing properties, which in turn promotes\x01",
            "self-recovery. It's fascinating stuff, in theory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0305FHot damn. St. Ursula's research is no joke.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0500FI'm sure the CGF would find something like that\x01",
            "very handy, especially in combat scenarios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FBut you said it was a failure, correct? What\x01",
            "exactly went wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PYes, well, I was researching it well into the\x01",
            "night, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P...I must have made a mistake somewhere,\x01",
            "because when I activated the prototype,\x01",
            "it created a massive explosion.\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#0006FI-Isn't that a little dangerous? You are\x01",
            "in a hospital, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PFunny thing is, that pendant was at the\x01",
            "center of it, and it still made it in one\x01",
            "piece. That's a miracle, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PSomething as lucky as that is perfect for\x01",
            "a present, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0006F(That's a pretty unscientific response from\x01",
            "someone in the medical field, isn't it?)\x02\x03",
            "#0000FWell, thank you very much. We would be\x01",
            "more than happy to take it off your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#11PPlease, I'm just happy to help.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CC6")

    ChrTalk(
        0x101,
        (
            "#5P#0003F(If we were to put Shizuku's stone in this,\x01",
            "it would probably look great.)\x02\x03",
            "#0000F(All that's left is to find something that can\x01",
            "substitute as a chain for the pendant.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14CC6")

    OP_29(0x2C, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14DB0")
    OP_29(0x2C, 0x1, 0x5)

    ChrTalk(
        0x101,
        (
            "#5P#0000F(We should have everything, now. I bet\x01",
            "the gift box and ribbon will go great with\x01",
            "the rest of the present, too.)\x02\x03",
            "(I think it's about time to show Shizuku\x01",
            "what we found.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DB0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x13, 0x5A, 0x0)
    SetChrPos(0x0, 54500, 0, -55500, 90)
    SetChrPos(0x1, 54500, 0, -55500, 90)
    SetChrPos(0x2, 54500, 0, -55500, 90)
    SetChrPos(0x3, 54500, 0, -55500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_78_1413A end

    SaveToFile()

Try(main)
