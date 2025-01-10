from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0310.bin",                # FileName
        "c0310",                    # MapName
        "c0310",                    # Location
        0x002B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 43, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0310",                  # 0
        "Helmer",                 # 1
        "Joanna",                 # 2
        "Mayor MacDowell",        # 3
        "イス",                   # 4
        "彫像",                   # 5
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
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

    DeclNpc(0,       0,       0,       180,  257,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-45349,  59,      3900,    360,  257,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 12,  41.130001068115234,    44.029998779296875,    0.05999999865889549,   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -20.565000534057617,   -14.676666259765625,   -0.012000001035630703, 1.0])

    DeclActor(-40820,  0,       40910,   1500,    -40820,  1500,    40910,   0x007C, 0,  13, 0x0000)

    ScpFunction((
        "Function_0_254",          # 00, 0
        "Function_1_30C",          # 01, 1
        "Function_2_337",          # 02, 2
        "Function_3_362",          # 03, 3
        "Function_4_38D",          # 04, 4
        "Function_5_518",          # 05, 5
        "Function_6_592",          # 06, 6
        "Function_7_266F",         # 07, 7
        "Function_8_2ACB",         # 08, 8
        "Function_9_2BC9",         # 09, 9
        "Function_10_4A39",        # 0A, 10
        "Function_11_4D60",        # 0B, 11
        "Function_12_604E",        # 0C, 12
        "Function_13_703D",        # 0D, 13
    ))


    def Function_0_254(): pass

    label("Function_0_254")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_294"),
        (1, "loc_2A0"),
        (2, "loc_2AC"),
        (3, "loc_2B8"),
        (4, "loc_2C4"),
        (5, "loc_2D0"),
        (6, "loc_2DC"),
        (SWITCH_DEFAULT, "loc_2E8"),
    )


    label("loc_294")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_30B")

    Return()

    # Function_0_254 end

    def Function_1_30C(): pass

    label("Function_1_30C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_336")
    OP_94(0xFE, 0xFFFFF63C, 0x0, 0x9C4, 0x73A, 0x3E8)
    Sleep(300)
    Jump("Function_1_30C")

    label("loc_336")

    Return()

    # Function_1_30C end

    def Function_2_337(): pass

    label("Function_2_337")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_361")
    OP_94(0xFE, 0xFFFFF8B2, 0x1A36, 0x744, 0x26DE, 0x3E8)
    Sleep(300)
    Jump("Function_2_337")

    label("loc_361")

    Return()

    # Function_2_337 end

    def Function_3_362(): pass

    label("Function_3_362")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38C")
    OP_94(0xFE, 0xA00A, 0xA05A, 0xB31A, 0xB220, 0x3E8)
    Sleep(300)
    Jump("Function_3_362")

    label("loc_38C")

    Return()

    # Function_3_362 end

    def Function_4_38D(): pass

    label("Function_4_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_39C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 11)

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C7")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3F1")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    SetChrFlags(0x9, 0x80)
    Jump("loc_517")

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_41C")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_436")
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_461")
    SetChrPos(0x8, 0, 4059, 13210, 360)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_49D")
    SetChrPos(0x8, 2580, 4000, 13150, 45)
    SetChrPos(0x9, -44780, 60, 47510, 270)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C8")
    SetChrPos(0x9, 43580, 0, 43630, 180)
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 3)
    Jump("loc_517")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4F3")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_50D")
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_50D")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_517")

    Return()

    # Function_4_38D end

    def Function_5_518(): pass

    label("Function_5_518")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_53F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_558")
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    Jump("loc_55E")

    label("loc_558")

    OP_10(0x0, 0x1)
    OP_10(0xB, 0x0)

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57A")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_591")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_591")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_591")

    label("loc_591")

    Return()

    # Function_5_518 end

    def Function_6_592(): pass

    label("Function_6_592")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_85C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_692")

    ChrTalk(
        0xFE,
        (
            "Master Henry will only heed\x01",
            "Lady Elie's words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I offer my sincerest apologies, but\x01",
            "that would be for the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FAs a politician, Grandfather can be very\x01",
            "stubborn. Hopefully, I'll be able to get\x01",
            "through to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_857")

    label("loc_692")


    ChrTalk(
        0xFE,
        (
            "If I may interrupt, my lady. I've been informed that\x01",
            "the master will be working overtime yet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I worry for his health. Now that the\x01",
            "diet has concluded, I will urge him to take\x01",
            "some much-needed rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FMy grandfather is stubborn to his core, so I\x01",
            "fear he won't listen to what you have to say.\x02\x03",
            "#0100FPerhaps I'll ask him again when the time\x01",
            "is right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I offer my sincerest apologies, but\x01",
            "that would be for the best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_857")

    Jump("loc_266B")

    label("loc_85C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8F5")

    ChrTalk(
        0xFE,
        "A shooting occurred at the harbor yesterday...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do worry that Mr. Bond may have\x01",
            "been caught up in a terrible incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EC")

    label("loc_8F5")


    ChrTalk(
        0xFE,
        "Miss Creil came to visit us a moment ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She asked if I had seen her husband, Mr. Bond.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Could it mean he's gone missing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard news of many concerning incidents\x01",
            "occurring as of late. I feel a bit unnerved at\x01",
            "the fact.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_9EC")

    Jump("loc_266B")

    label("loc_9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A87")

    ChrTalk(
        0xFE,
        (
            "I've been in Master Henry's\x01",
            "service for forty years now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I find it difficult to forgive\x01",
            "Speaker Hartmann's attitude.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDC")

    label("loc_A87")


    ChrTalk(
        0xFE,
        (
            "Speaker Hartmann is a state representative,\x01",
            "much like Master Henry. He should be\x01",
            "working to unify the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, for him to sit silently in his chair and\x01",
            "to allow the laxity of the diet to continue as is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can only imagine he continues to do this as a\x01",
            "way to torment the master.\x01",
            "I shall never forgive that vile man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_BDC")

    Jump("loc_266B")

    label("loc_BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 3)), scpexpr(EXPR_END)), "loc_D40")

    ChrTalk(
        0xFE,
        (
            "The diet's budget meeting is to be extended,\x01",
            "resulting in the master continuing to work overtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's as I feared. Worrying for Master Henry's\x01",
            "well-being has become my highest priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially with the mayoral election\x01",
            "approaching next month...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108FI agree. I hope he doesn't strain\x01",
            "himself too hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF1")

    label("loc_D40")

    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        (
            "Ah, Lady Elie. Your countenance appears\x01",
            "to be dreadful today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FE-Excuse me?! I-I assure you that's\x01",
            "patently false.\x02\x03",
            "#0103FPlease refrain from saying such a\x01",
            "strange thing, Helmer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I apologize for misunderstanding, my lady.\x01",
            "However, if one were to consider your\x01",
            "weaknesses, only one thing comes to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, I seem to recall you being visibly\x01",
            "shaken at any mention of ghosts when\x01",
            "you were but a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FWait, so Mademois-Elie ISN'T perfect?\x01",
            "Color me surprised!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0503FI apologize, Elie. My request has\x01",
            "made you uncomfortable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0112FO-Oh, please. I-It's not like I'm b-bad\x01",
            "with gh-ghosts... You don't need to\x01",
            "worry about me, Noel.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 3)

    label("loc_FF1")

    Jump("loc_266B")

    label("loc_FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_13DC")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10B9")

    ChrTalk(
        0xFE,
        (
            "If you insist, my lady... In any case, this\x01",
            "residency is most assuredly safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you should run into danger, then by all means,\x01",
            "please hide here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11EF")

    label("loc_10B9")


    ChrTalk(
        0xFE,
        (
            "Ah, Lady Elie and the SSS have arrived.\x01",
            "Master Henry has already informed me\x01",
            "of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(*frantically looks around*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2S(This estate is most assuredly safe.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2S(If you are to run into danger, then by all means,\x01",
            "please hide here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FTh-Thank you, Helmer, but we're fine.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11EF")

    Jump("loc_13D7")

    label("loc_11F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1292")

    ChrTalk(
        0xFE,
        (
            "If you insist... In any case, this estate\x01",
            "is most assuredly safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are to run into danger, then by all means,\x01",
            "please hide here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D7")

    label("loc_1292")


    ChrTalk(
        0xFE,
        (
            "Welcome, Special Support Section.\x01",
            "Master Henry has already informed me\x01",
            "of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*nervously looks around*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The MacDowell estate is most\x01",
            "assuredly safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are to run into danger, then by all means,\x01",
            "please hide here with Lady Elie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FTh-Thank you for your offer,\x01",
            "but we're fine now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_13D7")

    Jump("loc_266B")

    label("loc_13DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1901")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1514")

    ChrTalk(
        0xFE,
        (
            "Goodness. The shock from the\x01",
            "previous matter remains with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How does such a thing happen\x01",
            "so suddenly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I shall break the news to the master\x01",
            "upon his return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FR-Right. Could you please do so\x01",
            "when Grandfather does?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, my lady. With pleasure.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15BD")

    label("loc_1514")


    ChrTalk(
        0xFE,
        (
            "However, to think that Phantom Thief B\x01",
            "was able to breach the estate with\x01",
            "relative ease...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The responsibility lies with me.\x01",
            "I should have paid more attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BD")

    Jump("loc_18FC")

    label("loc_15C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1654")

    ChrTalk(
        0xFE,
        (
            "Your recent achievements as the SSS\x01",
            "have brought great joy to Master Henry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope to see your continued\x01",
            "efforts at work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18FC")

    label("loc_1654")

    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        "Ah, Lady Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am pleased to inform you Master Henry\x01",
            "will be returning early today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FOh, really? Thank you for notifying me.\x02\x03",
            "#0104FI'm pleased to know that Grandfather is\x01",
            "able to take a much-needed break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Likewise, my lady. Joanna has been cheerfully preparing\x01",
            "dinner to celebrate this occasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And on that note, would you care to\x01",
            "join us for dinner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FOh... I apologize, Helmer. I have important\x01",
            "work to take care of today.\x02\x03",
            "#0106FI'm unsure of when I'll be able to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is that so? Pardon me for being presumptuous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please make sure you are well prepared\x01",
            "for your day ahead, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do your best at work.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18FC")

    Jump("loc_266B")

    label("loc_1901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1A7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19E0")

    ChrTalk(
        0xFE,
        "Master Henry has a strong sense of responsibility.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As his butler, I feel as if I am placed in a difficult\x01",
            "situation. I cannot keep him from his duties, and\x01",
            "thus, I worry for his well-being.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A78")

    label("loc_19E0")


    ChrTalk(
        0xFE,
        (
            "The master is exhausted from attending\x01",
            "events and parties every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be nice if he were able to return\x01",
            "home early every so often.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A78")

    Jump("loc_266B")

    label("loc_1A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1D1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AE8")

    ChrTalk(
        0xFE,
        "It truly is a shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, then, shall we open this in another\x01",
            "ten years?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D17")

    label("loc_1AE8")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x102, 500)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Oh, Lady Elie!\x01",
            "You've come at the most\x01",
            "splendid time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FHas something happened, Helmer?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I found this wooden box while I was\x01",
            "cleaning the attic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe this to be the box you stored\x01",
            "your treasures in as a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, my lady was most adorable during her\x01",
            "childhood. She would often collect a\x01",
            "myriad of accessories and baubles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What shall I do with it, my lady?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0113FPlease put it back where you found it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Would you look at that? Elie DOES\x01",
            "have girly hobbies, after all...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D17")

    Jump("loc_266B")

    label("loc_1D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1F61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DAF")

    ChrTalk(
        0xFE,
        (
            "I apologize for having disturbed\x01",
            "you with my noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I tend to take care of the cleaning\x01",
            "while the family is away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F5C")

    label("loc_1DAF")


    ChrTalk(
        0xFE,
        "I apologize for the commotion, Lady Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FYou seem to be in a good mood\x01",
            "today, Helmer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, not particularly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's just that, around this time of year,\x01",
            "the master is too busy attending various\x01",
            "events to come home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And given that I am his butler, I thought to use\x01",
            "this opportunity to make this home spotless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This has actually become an annual event,\x01",
            "ever since my lady went to study abroad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F5C")

    Jump("loc_266B")

    label("loc_1F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2005")

    ChrTalk(
        0xFE,
        (
            "Considering the master's position, it's not\x01",
            "as if I could suddenly abandon him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, being a butler is no simple\x01",
            "task, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2112")

    label("loc_2005")


    ChrTalk(
        0xFE,
        (
            "It appears that the master has finally\x01",
            "regained his strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Preparing those healthy dishes seems to\x01",
            "have helped him make a swift recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And with that, I would appreciate if he\x01",
            "wouldn't overwork himself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Being the mayor is not an easy job.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2112")

    Jump("loc_266B")

    label("loc_2117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2208")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2132")
    Call(0, 8)
    Jump("loc_2203")

    label("loc_2132")


    ChrTalk(
        0xFE,
        (
            "Ever since my daughter, Joanna, was seven\x01",
            "years old, she's been watching over Lady Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And for that reason, she cares deeply\x01",
            "about my lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope you don't mind her behaving overly familiar.\x02",
    )

    CloseMessageWindow()

    label("loc_2203")

    Jump("loc_266B")

    label("loc_2208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 2)), scpexpr(EXPR_END)), "loc_2668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2223")
    Call(0, 8)
    Jump("loc_2663")

    label("loc_2223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2424")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_227F")

    ChrTalk(
        0xFE,
        "That remark may have been uncalled for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do take care, SSS.\x02",
    )

    CloseMessageWindow()
    Jump("loc_241F")

    label("loc_227F")


    ChrTalk(
        0xFE,
        "I met with Ernest yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I assure you that he worries about you\x01",
            "in his own way, my lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can sympathize with the feelings\x01",
            "he has.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing my lady suffer and appear lost\x01",
            "has taken a toll on my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FThank you for your concern, Helmer.\x02\x03",
            "#0100FI'm going to be fine, though. I've\x01",
            "no longer got any doubts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. That remark may have been\x01",
            "uncalled for, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_241F")

    Jump("loc_2663")

    label("loc_2424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_24BA")

    ChrTalk(
        0xFE,
        (
            "I hope you all continue to look after\x01",
            "Lady Elie in our stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may be a mere butler, but I couldn't\x01",
            "be prouder of Lady Elie.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2663")

    label("loc_24BA")


    ChrTalk(
        0xFE,
        (
            "Am I correct for assuming you're her\x01",
            "colleagues? I've been informed of the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope you all continue to look after\x01",
            "Lady Elie in our stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lady Elie has been both brilliant\x01",
            "and lovely ever since she was\x01",
            "a small child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may be a mere butler, but I couldn't\x01",
            "be prouder of Lady Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0112FDon't you think you're showering me with\x01",
            "too much praise, Helmer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha. My apologies, my lady.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2663")

    Jump("loc_266B")

    label("loc_2668")

    Call(0, 7)

    label("loc_266B")

    TalkEnd(0xFE)
    Return()

    # Function_6_592 end

    def Function_7_266F(): pass

    label("Function_7_266F")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x102, 500)
    Sleep(500)

    ChrTalk(
        0x8,
        "Ah, Lady Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's been far too long. I do not believe\x01",
            "you've visited ever since you joined\x01",
            "the police force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FI apologize for not getting in contact sooner,\x01",
            "Helmer.\x02\x03",
            "#0100FSo, has anything changed around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Not that I am aware of.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Joanna and I have managed to stay\x01",
            "in good health, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Master Henry continues to work tirelessly...\x01",
            "to no one's surprise, I might add.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWhat are we ever going to do with him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Man, Mademois-Elie's place is as decked out\x01",
            "as I was anticipating. Bet it cost her a fortune.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2919")

    ChrTalk(
        0x103,
        (
            "#0200F(She also appears to be well acquainted\x01",
            "with her butler.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B3")

    label("loc_2919")


    ChrTalk(
        0x103,
        (
            "#0200F(We had only seen the outside of her home,\x01",
            "but the inside is even more incredible.)\x02\x03",
            "(She also appears to be well acquainted\x01",
            "with her butler.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B3")


    ChrTalk(
        0x101,
        (
            "#0000F(Well, the MacDowell family's been\x01",
            "distinguished for a long time now.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#0106FThis is precisely why I didn't want to\x01",
            "bring you all here. I knew this was\x01",
            "bound to happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 2)
    Return()

    # Function_7_266F end

    def Function_8_2ACB(): pass

    label("Function_8_2ACB")


    ChrTalk(
        0xFE,
        "Do you all like to read novels?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I enjoyed reading this book during my\x01",
            "breaks, but I've finished it. I'd like for\x01",
            "you to have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope you read it some time.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2C9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C9, 1)
    SetScenarioFlags(0x9C, 3)
    Return()

    # Function_8_2ACB end

    def Function_9_2BC9(): pass

    label("Function_9_2BC9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2E16")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C97")

    ChrTalk(
        0xFE,
        (
            "I've heard the Special Support Section has\x01",
            "become quite the respectable name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope you all continue to strive for excellence.\x01",
            "I shall wait here for your return.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E11")

    label("loc_2C97")


    ChrTalk(
        0xFE,
        (
            "It appears the master will be returning\x01",
            "late again tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you working today, my lady?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard the Special Support Section has\x01",
            "become quite the respectable name.\x01",
            "I hope you all continue to strive for excellence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThank you, Joanna. We'll try.\x01",
            "I'll leave Grandfather in your care, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Of course. I shall take good care of him.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E11")

    Jump("loc_4A35")

    label("loc_2E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_30B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E59")
    TurnDirection(0x9, 0x102, 0)

    ChrTalk(
        0xFE,
        "Stay safe out there, Lady Elie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_30AD")

    label("loc_2E59")


    ChrTalk(
        0xFE,
        (
            "I've heard rumors of various happenings\x01",
            "throughout the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am worried you may get involved, given\x01",
            "that you work for the police, Lady Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI appreciate the concern, but I'm always\x01",
            "worried for both you and Helmer, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI'm pretty sure no one other than the\x01",
            "servants are usually home.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_3052")

    ChrTalk(
        0x104,
        (
            "#0300FWell, not a whole lot goin' on around these\x01",
            "parts. I figure they'll be fine.\x02\x03",
            "#0303FThough that neighbor of yours is\x01",
            "still a stupid little mystery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30AA")

    label("loc_3052")


    ChrTalk(
        0x104,
        (
            "#0300FWell, not a whole lot goin' on around these\x01",
            "parts. I figure they'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AA")

    SetScenarioFlags(0x0, 1)

    label("loc_30AD")

    Jump("loc_4A35")

    label("loc_30B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3438")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_318D")
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        "Lady Elie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please do not hesitate to rely on others\x01",
            "in the face of something frightening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F(I was trying my hardest to hide it,\x01",
            "so how was she able to figure it out?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3433")

    label("loc_318D")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        "...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "E-Excuse me, Lady Elie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWh-What is it, Joanna?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't hesitate to call me if there's anything\x01",
            "you're ever afraid of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Much like the past, I shall protect you.\x01",
            "Whether it be sleeping in the same bed\x01",
            "or guiding you to the restroom at night.\x02",
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
        0x109,
        (
            "#0500FI'm soooo sorry, Elie. I didn't mean to put\x01",
            "you through this humiliation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0113FTh-That's enough already. I was only a\x01",
            "child when those happened!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FSo Joanna was your caretaker, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Haha. I gotta admit, Elie's pretty\x01",
            "cute right now.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3433")

    Jump("loc_4A35")

    label("loc_3438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_381C")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3522")
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        "I shall prepare a feast tonight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please join your grandfather if you're\x01",
            "able to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FI'd love to.\x02\x03",
            "#0100FI'll leave the preparations to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*nod*\x01",
            "Allow me, my lady!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AE")

    label("loc_3522")

    TurnDirection(0xFE, 0x102, 500)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, Lady Elie! Thank Aidios, you're safe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FI'm sorry, Joanna... I haven't been able\x01",
            "to return for a long while.\x02\x03",
            "#0100FI must have worried you deeply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*shakes*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I believed in you, my lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0109FHahaha... I appreciate it.\x02\x03",
            "#0100FThank you, Joanna. I'll be back\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*nod*\x01",
            "U-Um... I'll be waiting for you, my lady!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_36AE")

    Jump("loc_3817")

    label("loc_36B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_36F8")

    ChrTalk(
        0xFE,
        (
            "I implore you all to take good\x01",
            "care of Lady Elie.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3817")

    label("loc_36F8")

    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Excuse me, where's Lady Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FSorry, Joanna. She's not with us\x01",
            "today.\x02\x03",
            "#0000FDon't worry, though. We were able to\x01",
            "solve the case, so everything is going\x01",
            "to be okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*nod*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I implore you all to take good\x01",
            "care of Lady Elie.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3817")

    Jump("loc_4A35")

    label("loc_381C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3C31")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3A3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F7")

    ChrTalk(
        0xFE,
        (
            "I heard the news, my lady. You had a\x01",
            "fateful confrontation with Phantom Thief B.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Would you do me the honor of equipping\x01",
            "yourself with my frying pan? I am sure\x01",
            "it'll be useful for you in your endeavors.\x02",
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
        0x102,
        "#0105FTh-Thank you, Joanna...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Is she supposed to use that for self-defense...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A39")

    label("loc_39F7")


    ChrTalk(
        0xFE,
        "My lady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please be careful while you're hard at work.\x02",
    )

    CloseMessageWindow()

    label("loc_3A39")

    Jump("loc_3C2C")

    label("loc_3A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3ACF")

    ChrTalk(
        0xFE,
        (
            "It appears that Master Henry will be\x01",
            "returning earlier than anticipated today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please continue the hard work, Lady Elie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C2C")

    label("loc_3ACF")


    ChrTalk(
        0xFE,
        (
            "It appears that Master Henry will be\x01",
            "returning earlier than anticipated today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Umm...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "Never mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope you continue to keep up the good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Yo, Mademois-Elie. It kinda looked like she\x01",
            "had somethin' she wanted to tell you.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0103F(I'm sorry, Joanna. I can't leave my post today...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3C2C")

    Jump("loc_4A35")

    label("loc_3C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3CA7")

    ChrTalk(
        0xFE,
        "Today's parade seemed utterly delightful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I was thrilled to see all the children enjoying it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A35")

    label("loc_3CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3E9D")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3D68")

    ChrTalk(
        0xFE,
        (
            "I tasked myself with the responsibility of\x01",
            "cleaning Lady Elie's room every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rest assured, your room will always\x01",
            "be ready to give you a warm welcome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E98")

    label("loc_3D68")


    ChrTalk(
        0xFE,
        "Lady Elie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I shall continue to make the bed daily, so\x01",
            "come rest whenever you feel the need to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FTh-Thank you, Joanna.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Dang, Mademois-Elie! One helluva dedicated\x01",
            "maid you got there, eh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(I'll never get used to it, though.\x01",
            "Joanna and I are the same age...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3E98")

    Jump("loc_4A35")

    label("loc_3E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3FAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3EF4")

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Truth be told, I worry for Master Henry's health.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FA8")

    label("loc_3EF4")


    ChrTalk(
        0xFE,
        "I am currently cleaning the master's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I should adjust the curtains while I'm at it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should the sun's rays be too powerful, it could\x01",
            "cause harm to your body.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3FA8")

    Jump("loc_4A35")

    label("loc_3FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_434D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4053")
    TurnDirection(0x9, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "Please continue to put forth your best\x01",
            "effort in your endeavors, my lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will continue to cheer you on from the sidelines.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4348")

    label("loc_4053")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x102, 500)
    Sleep(500)

    ChrTalk(
        0xFE,
        "Lady Elie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please forgive me, for I've held the wrong\x01",
            "impression this whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FWhat do you mean?\x01",
            "(Has something happened?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Special Support Section is a wonderful\x01",
            "career choice. I deeply apologize for ever\x01",
            "doubting that fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I now understand that you are an elite group\x01",
            "that possesses more authority than the First\x01",
            "Division. Your accomplishments tell as much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please forgive me for maintaining this\x01",
            "embarrassing misconception.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0306F(Laying on the compliments\x01",
            "a bit thick there, eh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F(Oh, dear... Joanna seems to be\x01",
            "slightly confused in regard to\x01",
            "how we operate...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4348")

    Jump("loc_4A35")

    label("loc_434D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_45AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_43DA")

    ChrTalk(
        0xFE,
        (
            "I've heard the Chief Sergei from the SSS\x01",
            "is a no-good, foul man who lazes around\x01",
            "the city all day long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_45A5")

    label("loc_43DA")


    ChrTalk(
        0xFE,
        (
            "I've heard Chief Sergei is responsible\x01",
            "for overseeing the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've also heard that he's a no-good man\x01",
            "who lazes around the city all day long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Poor Chief... Doesn't have much of a\x01",
            "reputation, does he?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Can ya blame 'em? Just look at the man.)\x02\x03",
            "#0300F(Not too worried, though. He'll be fine so long as\x01",
            "Old Man MacDowell doesn't shut him down.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0103F(As if that would ever happen.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_45A5")

    Jump("loc_4A35")

    label("loc_45AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 3)), scpexpr(EXPR_END)), "loc_4A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_480C")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4668")

    ChrTalk(
        0xFE,
        (
            "I think you would excel at any job you wish\x01",
            "to pursue with your talents, Lady Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do hope you come to visit. You're\x01",
            "always welcome home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4807")

    label("loc_4668")


    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FIs something wrong, Joanna?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, well...actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been hearing that the Special Support\x01",
            "Section is a thankless post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#0200F(She seems concerned for you, Elie.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103F(I'm sorry, Joanna, but I'd like to continue\x01",
            "working at the SSS for a little while longer.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4807")

    Jump("loc_4A2D")

    label("loc_480C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_48B2")

    ChrTalk(
        0xFE,
        (
            "I think you would exceed at any job you wish\x01",
            "to pursue with your talents, Lady Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do hope you come to visit. You're\x01",
            "always welcome home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A2D")

    label("loc_48B2")


    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FIs something wrong, Joanna?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, well...actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been hearing that the Special Support\x01",
            "Section is a thankless post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#0200F(She seems concerned for you, Elie.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F(R-Right... Joanna's always been a bit\x01",
            "of a worrywart.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4A2D")

    Jump("loc_4A35")

    label("loc_4A32")

    Call(0, 10)

    label("loc_4A35")

    TalkEnd(0xFE)
    Return()

    # Function_9_2BC9 end

    def Function_10_4A39(): pass

    label("Function_10_4A39")

    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x102, 500)
    Sleep(500)

    ChrTalk(
        0x9,
        "Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Lady Elie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FIt's been far too long, Joanna.\x02\x03",
            "I apologize for showing up\x01",
            "unannounced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "*shiver*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I shall prepare a meal immediately, as I was\x01",
            "already getting ready to do so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So, um... I was wondering. Have you retired from\x01",
            "the police force and returned back home?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(
        0x9,
        (
            "I washed your jammies. They should be\x01",
            "in the designated location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh! And, I already clean your room and make\x01",
            "your bed every day, so you're welcome to use\x01",
            "it whenever you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FI apologize, Joanna. I only came here to visit.\x02\x03",
            "I haven't quite retired from the police yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    ChrTalk(
        0x9,
        "O-Oh. I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "My apologies for assuming otherwise, my lady.\x01",
            "I...hope you continue to work your hardest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FOf course. Thank you, Joanna.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 3)
    Return()

    # Function_10_4A39 end

    def Function_11_4D60(): pass

    label("Function_11_4D60")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50235.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50236.itc", 0x20)
    OP_68(45500, 1200, 48400, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 44700, 250, 48500, 90)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 46100, 550, 48650, 180)
    ClearMapObjFlags(0x5, 0x4)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x5, 0xB)
    OP_49()
    SetChrPos(0xB, 44500, 0, 48600, 0)
    OP_D3(0xB, 0x0, 0x0, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#2201743VS-Seriously?\x02\x03",
            "#2201744VTomorrow is FAR too early for you\x01",
            "to return to work!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(20000, 2500)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#2201745V#11P#6503FIt's nothing more than a bruise and a\x01",
            "minor sprain.\x02\x03",
            "#2201746V#6500FFive days of rest has been more than enough.\x01",
            "Worry not, for I have recharged my batteries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201747V#6P#0106FD-Don't take this so lightly, Grandfather!\x02\x03",
            "#2201748V#0108FPlease think about everything that's happened...\x01",
            "You no longer have Ernest, and you could have died!\x02\x03",
            "#2201749V#0101FDon't you think you've earned more than\x01",
            "five days of rest?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2201750V#11P#6500FYou may feel so, but the Anniversary Festival\x01",
            "draws near. Duty calls, so I cannot fall behind.\x02\x03",
            "#2201751V#6509FI can't abandon my role as Crossbell's mayor\x01",
            "over a minor spat like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201752V#6P#0106FA minor spat?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#2201753V#6P#0108FGrandfather. Are you not in pain? Are you\x01",
            "not mortified?\x02\x03",
            "#2201754VErnest was like a son to you, yet he\x01",
            "betrayed you!\x02\x03",
            "#2201755VSo...why? Why do you continue?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#2201756V#5P#6503FIf I told you what happened didn't shock\x01",
            "me, I would be lying through my teeth.\x02\x03",
            "#2201757VAs I'm sure you've heard, Ernest has long been\x01",
            "embezzling public funds from under our noses.\x02\x03",
            "#2201758VPerhaps his actions caused extreme stress,\x01",
            "and being trapped in his own mind caused\x01",
            "him to go berserk.\x02\x03",
            "#2201759VI do believe I bear some responsibility for not\x01",
            "taking notice in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201760V#6P#0105FGrandfather...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2201761V#5P#6501FNevertheless, I am a statesman.\x02\x03",
            "#2201762VI have sworn to serve Crossbell\x01",
            "State in the present and future.\x02\x03",
            "#2201763VNo matter what happens, it's my duty\x01",
            "to uphold that oath and lead this state.\x02\x03",
            "#2201764VThat is a self-imposed commitment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201765V#6P#0108F...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#2201766V#11P#6503FI truly apologize, Elie...\x02\x03",
            "#2201767VMuch like ten years ago, I was unable\x01",
            "to stop your father, Ryan...\x02\x03",
            "#2201768V#6503FNot only that, but my own daughter,\x01",
            "your mother, left you behind.\x02\x03",
            "#2201769VAnd yet as powerless as I often am,\x01",
            "I continue to fulfill the role of mayor.\x02\x03",
            "#2201770V#6501FSurely you must despise me, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201771V#6P#0101FThere's no way that could ever be true!\x01",
            "You're my hero, Grandfather!\x02\x03",
            "#2201772V#0108FI occasionally keep in touch with\x01",
            "Mother and Father...\x02\x03",
            "#2201773V#0106FIt may be heartbreaking, but\x01",
            "I know I can overcome it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2201774V#11P#6500FElie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201775V#6P#0103FI originally joined the police because\x01",
            "I wished to help you in my own way.\x02\x03",
            "#2201776VI thought this different approach would be\x01",
            "a good way for me to help Crossbell, too...\x02\x03",
            "#2201777V#0108FHowever, now that Ernest is no longer\x01",
            "at your side...\x02\x03",
            "#2201778V#0101FI-I was thinking, I should retire from\x01",
            "the police and assist--\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        "#2201779V#11P#6507F#4S#NSpare me the nonsense!\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#2201780V#6P#0105FG-Grandfather?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2201781V#11P#6501FIf you truly regretted the path you chose,\x01",
            "then surely you would have returned\x01",
            "home immediately.\x02\x03",
            "#2201782VHowever...such was not the case, correct?\x02\x03",
            "#2201783VImagine how insulting it would be to turn\x01",
            "your back on the road you've taken.\x02\x03",
            "#2201784V#6503FTo your colleagues, to me, and above all...\x01",
            "to yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201799V#6P#0108FI...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2201786V#11P#6500FYou need not be concerned about me.\x02\x03",
            "#2201787VAfter all, I have more than a single secretary.\x01",
            "And if necessary, I shall seek Helmer's\x01",
            "assistance.\x02\x03",
            "#2201788VHowever, my plan to retire as mayor seems\x01",
            "to have been delayed, though.\x02\x03",
            "#2201789V#6509FWell, I suppose I've got another five years\x01",
            "until I'm able to comfortably retire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201790V#6P#0106F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2201791V#11P#6503FTherefore, Elie...\x01",
            "You must continue on the path you've chosen.\x02\x03",
            "#2201792VAt least until you've become satisfied with\x01",
            "all you've accomplished.\x02\x03",
            "#2201793V#6500FYour indomitable drive toward that end\x01",
            "motivates me more than anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201794V#6P#0108FGrandfather...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2201795V#11P#6503FNot to mention, if you all hadn't intervened,\x01",
            "I likely wouldn't be sitting here right now.\x02\x03",
            "#2201796V#6500FStand proud, Elie--of what you do and\x01",
            "how you've grown.\x02\x03",
            "#2201797VFor you shall continue to shine even\x01",
            "brighter and reach new heights.\x02\x03",
            "#2201798V#6509FMuch like Arc en Ciel's new play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201785V#6P#0105FAh...\x02\x03",
            "#2201800V#0102FYes, Grandfather!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 44700, 0, 47600, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetCameraDistance(19500, 800)
    Fade(500)
    SetChrSubChip(0x102, 0x1)
    Sound(804, 0, 80, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#2201801V#6P#0104FI, Elie MacDowell...\x02\x03",
            "#2201802V#0100F...will return to my post tomorrow and\x01",
            "strive to make Crossbell a better place!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 1)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_4D60 end

    def Function_12_604E(): pass

    label("Function_12_604E")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    EndChrThread(0x8, 0x0)
    OP_68(41010, 1500, 43700, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 41690, 60, 43300, 90)
    SetChrPos(0x102, 41690, 60, 44420, 90)
    SetChrPos(0x103, 40640, 60, 43300, 90)
    SetChrPos(0x104, 40550, 60, 44420, 90)
    SetChrPos(0x8, 37190, 60, 43820, 90)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x6, 0xC)
    OP_49()
    SetChrPos(0xC, 45500, 0, 43500, 0)
    ClearMapObjFlags(0x3, 0x4)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    OP_0D()

    ChrTalk(
        0x102,
        "#5P#0105FHuh?!\x02",
    )

    CloseMessageWindow()
    OP_68(43290, 1500, 44170, 2000)
    MoveCamera(54, 18, 0, 2000)

    def lambda_616E():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_616E)

    def lambda_6183():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6183)

    def lambda_6198():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6198)

    def lambda_61AD():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_61AD)
    Sleep(2000)

    ChrTalk(
        0x101,
        "#12P#0011FWh-Wha...?! How'd this even get here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0305FIf this ain't a bruh moment,\x01",
            "then I don't know what is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FThere is no mistaking it. This is the\x01",
            "Saint's Prayer statue that was stolen\x01",
            "from City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FWhy... Why is it in Grandfather's room,\x01",
            "of all places?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man's Voice",
        "#2PIs everything all right in there, my lady?\x02",
    )

    CloseMessageWindow()
    OP_68(42240, 1500, 44090, 1800)
    MoveCamera(55, 26, 0, 1800)

    def lambda_634D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_634D)
    Sleep(12)

    def lambda_635D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_635D)

    def lambda_636A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_636A)
    Sleep(15)

    def lambda_637A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_637A)

    def lambda_6387():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6387)
    OP_95(0x8, 40640, 60, 43910, 1500, 0x0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#6PExcuse me?! Did you all carry this\x01",
            "in here by yourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0203FClearly not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FLong story short: You're looking\x01",
            "at the work of the notorious\x01",
            "Phantom Thief B.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYou couldn't mean THE Phantom Thief B,\x01",
            "could you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0101FWas anything suspicious delivered to\x01",
            "the house today, Helmer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6PWe haven't had a visitor today, my lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PMaster Henry is exceedingly busy today,\x01",
            "so no one has any reason to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FNo witnesses, then? How the hell'd\x01",
            "he manage to lug this thing in here?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_65E4():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_65E4)
    Sleep(50)

    def lambda_65F4():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_65F4)
    Sleep(50)

    def lambda_6604():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6604)
    Sleep(50)

    def lambda_6614():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_6614)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#0003FI don't think any of us will ever find\x01",
            "the answer to that question...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#0005FHold on. There's a card attached to the\x01",
            "side of the statue.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_66D9():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66D9)

    def lambda_66E6():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_66E6)

    def lambda_66F3():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_66F3)
    OP_95(0x101, 44380, 0, 42120, 1000, 0x0)
    OP_93(0x101, 0x2D, 0x190)
    Sleep(800)
    OP_95(0x101, 42890, 60, 43300, 1000, 0x0)

    def lambda_6732():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6732)

    def lambda_673F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_673F)

    def lambda_674C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_674C)

    def lambda_6759():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6759)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A splendid job, ladies and gentlemen of the\x01",
            "Special Support Section. Your noble efforts\x01",
            "have proved this festival to be more enjoyable\x01",
            "than I could have ever desired. Your courage\x01",
            "and toil have earned my respect.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It pains me to say so, but certain...circumstances\x01",
            "have arisen. Rest easy, my friends, for I have\x01",
            "no intention of interfering any longer.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "P.S. It appears you assisted my\x01",
            "dearest friend, Kitty, yesterday.\x01",
            "You have my utmost gratitude.\x01",
            "   - Phantom Thief B\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#12P#0200FHe took pleasure in toying with us until\x01",
            "the final moment... I must admit, it feels\x01",
            "slightly humiliating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0105FMore importantly, he mentioned his\x01",
            "'dearest friend, Kitty.'\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        "#12P#0001FWait, you don't think...\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#0305FOh, snap! You mean Renne?!\x02\x03",
            "#0301FGuess it ain't too crazy for them to be friends\x01",
            "if B has connections to the society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0008FWe don't have any evidence to confirm it, so\x01",
            "let's just leave that aside for now.\x02\x03",
            "#0006FBased on what we've seen, Phantom Thief B's\x01",
            "strength lies in spreading confusion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203FThat man truly agitates me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0103FWe should be thankful he didn't have\x01",
            "any grander schemes planned.\x02\x03",
            "#0100FHopefully, he won't resort to tormenting\x01",
            "others, now that he's had his fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FWe couldn't arrest this jackass,\x01",
            "but I guess you're right, Lloyd.\x01",
            "Not much more we can really do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FRight. I'm just relieved we were able to\x01",
            "safely recover the statue.\x02\x03",
            "#0001FAnyway, I think we can move on now!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E19():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6E19)
    Sleep(50)

    def lambda_6E29():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6E29)
    Sleep(50)

    def lambda_6E39():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6E39)
    Sleep(50)

    def lambda_6E49():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_6E49)
    Sleep(300)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)
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
        (
            "#12P#0006FAs for this thing... Let's contact Chief Clipp\x01",
            "and arrange to have it shipped back.\x02\x03",
            "I figure the four of us don't stand a chance\x01",
            "of carrying it over ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106FRight... It really does make you wonder\x01",
            "how he was able to tote this around town.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_604E end

    def Function_13_703D(): pass

    label("Function_13_703D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Even a Cat Can Do It! How to Prepare a Delicious Cake\x01",
            "is on the shelf.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x11)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7120")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C1),
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
            scpstr(SCPSTR_CODE_ITEM, 0x1C1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x11)

    label("loc_7120")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_13_703D end

    SaveToFile()

Try(main)
