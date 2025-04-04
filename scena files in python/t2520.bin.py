from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2520.bin",                # FileName
        "t2520",                    # MapName
        "t2520",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 90, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2520",                  # 0
        "Sergeant Major Seeker",  # 1
        "Deputy Commander Baelz", # 2
        "Guardsman Flammy",       # 3
        "Guardsman Burrell",      # 4
        "Tourist Beltia",         # 5
    ))

    AddCharChip((
        "chr/ch34100.itc",                   # 00
        "apl/ch50147.itc",                   # 01
        "chr/ch00800.itc",                   # 02
        "chr/ch05702.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch34500.itc",                   # 05
    ))

    DeclNpc(740,     0,       4469,    349,  257,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6210,    150,     -150,    260,  341,  0x0, 0,   3,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-30899,  0,       43400,   0,    257,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-70010,  449,     -32430,  90,   469,  0x0, 0,   1,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-52060,  0,       5650,    225,  385,  0x0, 0,   5,   0,   0,   1,   0,   11,  255,  0)

    DeclActor(-28890,  10,      42110,   1200,    -28890,  1500,    42110,   0x007C, 0,  20, 0x0000)
    DeclActor(4760,    0,       -280,    1200,    6210,    1500,    -150,    0x007E, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_1D4",          # 00, 0
        "Function_1_28C",          # 01, 1
        "Function_2_2B7",          # 02, 2
        "Function_3_459",          # 03, 3
        "Function_4_4EE",          # 04, 4
        "Function_5_1F0C",         # 05, 5
        "Function_6_21FE",         # 06, 6
        "Function_7_2202",         # 07, 7
        "Function_8_5141",         # 08, 8
        "Function_9_53DE",         # 09, 9
        "Function_10_5ED8",        # 0A, 10
        "Function_11_608F",        # 0B, 11
        "Function_12_61C5",        # 0C, 12
        "Function_13_7304",        # 0D, 13
        "Function_14_755A",        # 0E, 14
        "Function_15_7D9F",        # 0F, 15
        "Function_16_8BB6",        # 10, 16
        "Function_17_8BD5",        # 11, 17
        "Function_18_8BF4",        # 12, 18
        "Function_19_8C13",        # 13, 19
        "Function_20_8C32",        # 14, 20
    ))


    def Function_0_1D4(): pass

    label("Function_0_1D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_214"),
        (1, "loc_220"),
        (2, "loc_22C"),
        (3, "loc_238"),
        (4, "loc_244"),
        (5, "loc_250"),
        (6, "loc_25C"),
        (SWITCH_DEFAULT, "loc_268"),
    )


    label("loc_214")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_220")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_22C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_238")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_244")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_250")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_25C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_268")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_274")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_28B")

    Return()

    # Function_0_1D4 end

    def Function_1_28C(): pass

    label("Function_1_28C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B6")
    OP_94(0xFE, 0xFFFF2E82, 0x1770, 0xFFFF3CB0, 0x170C, 0x3E8)
    Sleep(300)
    Jump("Function_1_28C")

    label("loc_2B6")

    Return()

    # Function_1_28C end

    def Function_2_2B7(): pass

    label("Function_2_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2CF")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_445")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2EE")
    SetChrPos(0x8, 3980, 0, -150, 90)
    Jump("loc_445")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_31C")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -69630, 0, -30590, 180)
    Jump("loc_445")

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_32A")
    Jump("loc_445")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_338")
    Jump("loc_445")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3BA")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_363")
    Event(0, 15)

    label("loc_363")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_374")
    Jump("loc_3B5")

    label("loc_374")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_397")
    SetChrPos(0x8, 6080, 0, 2120, 270)
    Jump("loc_3B5")

    label("loc_397")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x8, 6080, 0, 2120, 180)

    label("loc_3B5")

    Jump("loc_445")

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C8")
    Jump("loc_445")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3E0")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_445")

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3EE")
    Jump("loc_445")

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_445")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_406")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)

    label("loc_406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_428")
    SetChrPos(0x8, 6080, 0, 2120, 270)
    Jump("loc_445")

    label("loc_428")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_445")
    SetChrPos(0x8, 6080, 0, 2120, 270)

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_458")
    ClearChrFlags(0xC, 0x80)

    label("loc_458")

    Return()

    # Function_2_2B7 end

    def Function_3_459(): pass

    label("Function_3_459")

    SetMapObjFrame(0xFF, "futon00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futon01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_485")
    Jump("loc_4AC")

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4AC")
    SetMapObjFrame(0xFF, "futon00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futon01", 0x1, 0x1)

    label("loc_4AC")

    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4D7")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ED")
    OP_66(0x0, 0x1)

    label("loc_4ED")

    Return()

    # Function_3_459 end

    def Function_4_4EE(): pass

    label("Function_4_4EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4FF")
    Jump("loc_1F08")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_69F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D")
    Call(0, 5)
    SetScenarioFlags(0x0, 1)
    Jump("loc_69A")

    label("loc_51D")


    ChrTalk(
        0xFE,
        (
            "#0502FWe really appreciate your help yesterday,\x01",
            "everyone. I couldn't have done it without you.\x02\x03",
            "#0504FWhen I went to inform the deputy commander\x01",
            "of our success, she asked me to put together\x01",
            "the report ASAP, so I did, of course.\x02\x03",
            "#0508FI sure hope the Septian Church will cooperate\x01",
            "with us. Without their expertise, I doubt we'll\x01",
            "be able to uncover the truth behind that bell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69A")

    Jump("loc_1F08")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6AD")
    Jump("loc_1F08")

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F4")

    ChrTalk(
        0xFE,
        (
            "#0500FWe received a report yesterday about a pair\x01",
            "of tourists that wandered into the Ancient\x01",
            "Battlefield near Armorica Village.\x02\x03",
            "#0504FMuch to our surprise, it said that the Special\x01",
            "Support Section were the ones who rescued\x01",
            "them. Thank you, everyone.\x02\x03",
            "#0508FOur patrols should have kept something like\x01",
            "that from happening in the first place, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FDon't mention it, Sergeant Major. We did what\x01",
            "anyone would do in those circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYup, what he said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0504FThank you... I can always count on the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9B3")

    label("loc_8F4")


    ChrTalk(
        0xFE,
        (
            "#0504FEveryone here really appreciated what\x01",
            "you did at the Ancient Battlefield.\x02\x03",
            "#0500FFrom here on out, we're going to make\x01",
            "sure to be much more thorough with our\x01",
            "patrols in that area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B3")

    Jump("loc_1F08")

    label("loc_9B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_BA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB4")

    ChrTalk(
        0xFE,
        (
            "#0501FThe commander put all of our investigations\x01",
            "into the ruins throughout Crossbell on ice.\x02\x03",
            "#0506FBecause of that, we still have no idea what\x01",
            "the true purpose of Stargazer's Tower is...\x01",
            "or if it's a potential threat.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B9F")

    label("loc_AB4")


    ChrTalk(
        0xFE,
        (
            "#0501FIf we were given official permission, I would\x01",
            "be more than happy to take a scouting unit\x01",
            "to investigate places like Stargazer's Tower...\x02\x03",
            "#0506F...but the commander claims missions like\x01",
            "that are a waste of the CGF's budget.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9F")

    Jump("loc_1F08")

    label("loc_BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C68")

    ChrTalk(
        0xFE,
        (
            "#0502FThe tests of our new border countermeasures\x01",
            "were a massive success!\x02\x03",
            "It looks like it was worth the effort, after all.\x01",
            "That sure is a weight off my shoulders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F8")

    label("loc_C68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_D3E")

    ChrTalk(
        0xFE,
        (
            "#0503FSpeaking of counterfeit dealers, they've been a\x01",
            "big pain in our backside here at the gate...\x02\x03",
            "#0501FBut now that we have the SSS's help, I'm sure\x01",
            "we'll finally be able to rein them in!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F8")

    label("loc_D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE4")

    ChrTalk(
        0xFE,
        (
            "#0500FThe guardsmen should be in the middle of\x01",
            "conducting their daily patrols.\x02\x03",
            "#0506FSince there's been an influx of new tourists,\x01",
            "we have to be even more vigilant than usual.\x01",
            "You never know what might happen.\x02\x03",
            "#0501FAfter all, Crossbell isn't the safest place in the\x01",
            "world. Remember Stargazer's Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FDo I ever! Well, keep up the good work, Noel.\x02\x03",
            "#0302FIf ya ever need us, just give us a ring. We've\x01",
            "got your back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202FIs this what they call grandstanding?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0310FWhat's that s'pose to mean?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FCome, now, Tio. You don't have\x01",
            "to be THAT frank with Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FM-Mademois-Elie, c'mon... Tell her she's\x01",
            "bein' crazy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_10F8")

    label("loc_FE4")


    ChrTalk(
        0xFE,
        (
            "#0509FRandy? If it's any consolation, I didn't think\x01",
            "you were being patronizing or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0308FI appreciate that, but...you don't\x01",
            "have to go so far as to comfort...\x02\x03",
            "#0306F...someone like me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0501FH-Hang in there, Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FWhat a drama queen...\x02",
    )

    CloseMessageWindow()

    label("loc_10F8")

    Jump("loc_1F08")

    label("loc_10FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_17A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_1446")

    ChrTalk(
        0xFE,
        (
            "#0502FOh, Lloyd? I've been wanting to thank\x01",
            "you for yesterday.\x02\x03",
            "#0504FNot just for me, but for Fran, too. I know\x01",
            "she had a wonderful time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FNo, I should be the one thanking you for\x01",
            "inviting me in the first place.\x02\x03",
            "#0004FI can't say I get many opportunities to go\x01",
            "to concerts nowadays, so it really was an\x01",
            "awesome experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0509FI'm happy to hear that.\x02\x03",
            "#0500FBy the way, you don't have to worry. I'm\x01",
            "sure you'll get other opportunities to go to\x01",
            "more eventually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012F(Randy is probably going to throw a fit\x01",
            "in three...two...one.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FYou got to spend your afternoon with\x01",
            "the sisters?! The Goddess must really\x01",
            "like you, bud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F*sigh* The men of the SSS are animals...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FTruly despicable human beings.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011F(Why does everyone always misunderstand?!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_16E3")

    label("loc_1446")


    ChrTalk(
        0xFE,
        (
            "#0500FExcuse me, Lloyd, Randy. Did you two\x01",
            "go the concert at the harbor yesterday...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FThe concert? How did you know about...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0502FAha! I knew it! I took the day off yesterday,\x01",
            "so Fran and I went to have some fun in the city.\x02\x03",
            "#0504FDuring the concert, I could've sworn that I saw\x01",
            "some familiar faces in the crowd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0302FWhy didn't ya just come say hi?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0509FN-No, I couldn't have done that...\x02\x03",
            "I'm pretty sure there were three ladies\x01",
            "hanging on to you two, so I thought it\x01",
            "would be rude to interrupt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0111FOh, DID you now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FI hope you had fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FHahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Those stares never fail to scare me.)\x02",
    )

    CloseMessageWindow()

    label("loc_16E3")

    SetScenarioFlags(0x0, 2)
    Jump("loc_17A2")

    label("loc_16EB")


    ChrTalk(
        0xFE,
        (
            "#0504FYesterday's break was the first time in a\x01",
            "while that I was able to actually stretch\x01",
            "my legs.\x02\x03",
            "#0502FBut to be honest, I was just happy to hear\x01",
            "that Fran's been doing okay.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A2")

    Jump("loc_1F08")

    label("loc_17A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_17B5")
    Jump("loc_1F08")

    label("loc_17B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_18AE")

    ChrTalk(
        0xFE,
        (
            "#0500FHello, everyone. I was just about to head\x01",
            "out for my daily patrol of the highway.\x02\x03",
            "#0503FI'm sure you all are painfully aware of how\x01",
            "dangerous Crossbell can be. I can't let any\x01",
            "tourists wander into the lion's den, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F08")

    label("loc_18AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1F08")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1992")

    ChrTalk(
        0xFE,
        (
            "#0503FAfter experiencing all of your fighting styles\x01",
            "first-hand, I know I have a long way to go.\x02\x03",
            "#0501FIf I don't buckle down on my training regimen,\x01",
            "how else will I be able to protect Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F08")

    label("loc_1992")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1A2F")

    ChrTalk(
        0xFE,
        (
            "#0500FI think training with the new recruits\x01",
            "will mutually benefit both the SSS\x01",
            "and the CGF.\x02\x03",
            "Try to kick them into shape, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F08")

    label("loc_1A2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1B08")

    ChrTalk(
        0xFE,
        (
            "#0500FThe Special Support Section? Thanks\x01",
            "for coming on such short notice.\x02\x03",
            "Deputy Commander Baelz has been\x01",
            "wanting to discuss the details of the\x01",
            "support request with you.\x02\x03",
            "Can you hear her out?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F08")

    label("loc_1B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E61")

    ChrTalk(
        0xFE,
        "#0508FHey there, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FSomething wrong, Sergeant Major? You\x01",
            "look pretty down in the dumps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0506FAs you know, the culprits behind the\x01",
            "monster attacks were some mafia thugs.\x02\x03",
            "#0508FDespite catching them in the act, they\x01",
            "were let out of prison not too long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FTheir bail was paid, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FWhy are we throwin' a big pity party?\x02\x03",
            "#0300FDidn't we see this comin' a selge away?\x01",
            "It's not like there's anything we can do\x01",
            "about it, 'cept moan and groan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou're right. If we keep pushing on,\x01",
            "I'm sure that the system will gradually\x01",
            "improve, little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0503FAgreed. Right now, all I can do is continue\x01",
            "to do my duty to the best of my ability, so\x01",
            "that's what I intend to do.\x02\x03",
            "#0502FThanks for snapping me out of that, guys.\x01",
            "I feel a little bit better now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F08")

    label("loc_1E61")


    ChrTalk(
        0xFE,
        (
            "#0500FThanks for snapping me out of that, guys.\x01",
            "I feel a little bit better now.\x02\x03",
            "#0503FAll I can do right now is work my hardest\x01",
            "within the CGF's jurisdiction...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F08")

    TalkEnd(0xFE)
    Return()

    # Function_4_4EE end

    def Function_5_1F0C(): pass

    label("Function_5_1F0C")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x9, 0x0)
    TurnDirection(0x8, 0x9, 0)

    ChrTalk(
        0x9,
        (
            "#2003FI see. So these are your discoveries from\x01",
            "the Moon Temple investigation.\x02\x03",
            "#2002FGood work, Seeker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0504FThe Special Support Section are the ones you\x01",
            "should be complimenting, ma'am. Without them,\x01",
            "this investigation wouldn't have been a success.\x02\x03",
            "#0501FSo, ma'am...what do you think we should do\x01",
            "about all this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2003FYou described in your report a bell that\x01",
            "seemed to summon fiends, correct...?\x02\x03",
            "#2001FIf my hunch is right, it might have\x01",
            "something to do with artifacts.\x02\x03",
            "I plan to consult Archbishop Eralda\x01",
            "about his opinion on the matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0503FThat sounds like a smart decision, ma'am.\x02\x03",
            "#0501FIf you want, I can go ahead and contact the\x01",
            "cathedral and try to set up a meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2000FPlease do.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_5_1F0C end

    def Function_6_21FE(): pass

    label("Function_6_21FE")

    Call(0, 7)
    Return()

    # Function_6_21FE end

    def Function_7_2202(): pass

    label("Function_7_2202")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2296")
    Jump("loc_22E0")

    label("loc_2296")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22B6")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22E0")

    label("loc_22B6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22D6")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22E0")

    label("loc_22D6")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22E0")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2895")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2787")

    ChrTalk(
        0x9,
        (
            "#2005FOh? Hello, everyone.\x02\x03",
            "#2000FIf you were looking for the sergeant major,\x01",
            "she's out delivering the Moon Temple\x01",
            "investigation report to the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, so the church ended up agreeing\x01",
            "to assist the CGF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FYou sure that's smart? You didn't exactly\x01",
            "get permission from the commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2003FYes, well, he rejected our second request\x01",
            "to investigate Stargazer's Tower as well.\x02\x03",
            "#2000FIn his eyes, any and all incidents of that\x01",
            "nature should be left to the archbishop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FSo that's how things stand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FMaybe it's because the commander hasn't\x01",
            "seen the situation for himself, or...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI think you are giving him too much credit.\x01",
            "He probably just believes it is more trouble\x01",
            "than it is worth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301FHmph. I'm sure it's a lil' of both.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_269C")

    ChrTalk(
        0x10A,
        (
            "#0603FIt's a shame that the CGF has declined\x01",
            "as much as it has because of that man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269C")


    ChrTalk(
        0x9,
        (
            "#2003FAnyway, the Septian Church and the\x01",
            "Tangram Gate unit will proceed to\x01",
            "jointly investigate this incident.\x02\x03",
            "#2000FAnd it's thanks to your assistance that\x01",
            "we were able to reach this stage. As\x01",
            "always, you have my thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2890")

    label("loc_2787")


    ChrTalk(
        0x9,
        (
            "#2003FFirst we have Stargazer's Tower and now\x01",
            "this temple...\x02\x03",
            "#2000FThese are very delicate situations, given\x01",
            "their potential connection to artifacts.\x02\x03",
            "Therefore, we've reached out to the\x01",
            "Septian Church in hopes that they will\x01",
            "lend their expertise to the CGF.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2890")

    Jump("loc_5139")

    label("loc_2895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_29E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B3")
    Call(0, 5)
    SetScenarioFlags(0x0, 1)
    Jump("loc_29E3")

    label("loc_28B3")


    ChrTalk(
        0x9,
        (
            "#2000FGood work yesterday, everyone.\x02\x03",
            "#2003FYour investigation was a success. Even without\x01",
            "finding the phenomenon's source, you managed to\x01",
            "handle both the bell and those monsters.\x02\x03",
            "I couldn't have asked for a better outcome.\x02\x03",
            "#2000FYou can leave the rest of the investigation to the\x01",
            "Guardian Force.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29E3")

    Jump("loc_5139")

    label("loc_29E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2F6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E18")

    ChrTalk(
        0x9,
        (
            "#2000FI see you were able to enlist the Special Support\x01",
            "Section's assistance for the case, Seeker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FYes, ma'am. They were more than\x01",
            "happy to lend a hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0109FO-Of course we were! H-Haha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0004FYou okay, Elie? You look a little tense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0107FH-How many times do I have to say\x01",
            "that I'm fine?! Perfectly fine!\x02\x03",
            "#0112FIf we're going to investigate, let's just\x01",
            "get on with it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FMademois-Elie is real intimidatin' when\x01",
            "she wants to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FElie has nerves of steel. I doubt we have\x01",
            "anything to worry about, especially when\x01",
            "she gets like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2000FAlways a lively bunch, aren't you?\x02\x03",
            "#2003FRegrettably, the investigation conducted by\x01",
            "the CGF ultimately ended in failure.\x02\x03",
            "If failures such as this keep piling up, it's likely\x01",
            "that our gracious commander will call off the\x01",
            "investigation entirely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303FYeah, I wouldn't be surprised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2000FBut, of course, your safety and well-being\x01",
            "are to be your top priority. Do I make myself\x01",
            "absolutely clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FYes, ma'am. We won't forget.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F6A")

    label("loc_2E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2A")
    Call(0, 8)
    Jump("loc_2F6A")

    label("loc_2E2A")


    ChrTalk(
        0x9,
        (
            "#2000FRegrettably, the investigation conducted by\x01",
            "the CGF ultimately ended in failure.\x02\x03",
            "#2003FBut luckily, we suffered no casualties, barring a\x01",
            "guardsman who was bedridden from the shock\x01",
            "of coming face-to-face with monsters...\x02\x03",
            "#2000FStill, I'll repeat myself again. Take extreme\x01",
            "caution while exploring the ruins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F6A")

    Jump("loc_5139")

    label("loc_2F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_32C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3199")

    ChrTalk(
        0x9,
        "#2006F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FUm, Deputy Commander...?\x01",
            "Is something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2003F...No.\x02\x03",
            "I simply noticed you four are each\x01",
            "wearing an interesting expression.\x02\x03",
            "#2000FThe kind of face someone makes when\x01",
            "they're about to go against orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(*gulp*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(She must have realized that we plan\x01",
            "to sneak into the auction...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(A woman's intuition is a powerful weapon.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F(I-I don't like that look one bit.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2004FHehe. Did I say something strange? Well,\x01",
            "I wouldn't worry too much about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32C3")

    label("loc_3199")


    ChrTalk(
        0x9,
        (
            "#2003FAt the very least, try not to overdo it like\x01",
            "you did with the string of monster attacks.\x02\x03",
            "#2000FIf you uncover anything of importance,\x01",
            "consult with Sergei before anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FG-Got it.\x02\x03",
            "#0006F(Even if we wanted to ask the chief for\x01",
            "advice, he'd just shoot down our plan...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C3")

    Jump("loc_5139")

    label("loc_32C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3823")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3745")
    SetChrSubChip(0x9, 0x0)

    ChrTalk(
        0x9,
        "#2003FThis should be enough to do the job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhat are you up to, Deputy Commander?\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33D4")
    Jump("loc_341E")

    label("loc_33D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33F4")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_341E")

    label("loc_33F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3414")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_341E")

    label("loc_3414")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_341E")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(
        0x9,
        (
            "#2000FAh, I've been assembling files regarding\x01",
            "everything we know about Stargazer's\x01",
            "Tower.\x02\x03",
            "Once the commander returns to the gate,\x01",
            "I intend to make an appeal to organize a\x01",
            "scouting unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FYou sure you wanna do that?\x02\x03",
            "#0303FThis IS the commander we're talkin' about.\x01",
            "He'll probably shoot down your plan faster\x01",
            "than you can explain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2003FI'm well aware of the risks, Orlando.\x02\x03",
            "#2000FBut even if that is the outcome, I'll begin\x01",
            "to consider alternative approaches.\x02\x03",
            "I told you back in Mainz, didn't I? If we\x01",
            "give up, all the sacrifice that precedes\x01",
            "us would be in vain.\x02\x03",
            "#2002FWith that in mind, I at least have to try,\x01",
            "don't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0103FYou're absolutely right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe're going to keep giving it our all, too,\x01",
            "Deputy Commander Baelz.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_381E")

    label("loc_3745")


    ChrTalk(
        0x9,
        (
            "#2000FOnce the commander returns to the gate,\x01",
            "I intend to make an appeal to organize a\x01",
            "scouting unit.\x02\x03",
            "And if that is unsuccessful, I'll simply have\x01",
            "to organize a more convincing argument\x01",
            "and continue my battle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_381E")

    Jump("loc_5139")

    label("loc_3823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_42B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_394B")

    ChrTalk(
        0x9,
        (
            "#2000FNot too long ago, I was contacted by an\x01",
            "inspector from the CPD. Donovan was\x01",
            "his name, I believe.\x02\x03",
            "He informed me of your success in\x01",
            "arresting the counterfeit dealer.\x02\x03",
            "#2004FHehe. It's reassuring to hear that you're\x01",
            "getting the hang of the detective business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42AD")

    label("loc_394B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3C52")

    ChrTalk(
        0x9,
        (
            "#2003FThere's little time remaining until the\x01",
            "bus arrives from the Republic.\x02\x03",
            "#2000FIf you stay at the gate, you should have\x01",
            "enough time to rest beforehand.\x02\x03",
            "How about it? I can have beds prepared\x01",
            "for you, if needed.\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Still have some errands to run.\x01",              # 0
            "Time for some R&R before the bus comes.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3AA0"),
        (1, "loc_3B44"),
        (SWITCH_DEFAULT, "loc_3C4D"),
    )


    label("loc_3AA0")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#0001FI think we still need a little more time to\x01",
            "prepare, if that's okay with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2004FVery well.\x02\x03",
            "#2000FWhen you're ready to go, let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C4D")

    label("loc_3B44")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#0000FI think we'll take you up on that offer,\x01",
            "Deputy Commander Baelz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2004FVery well.\x02\x03",
            "#2000FOnce the bus arrives, I'll give you a\x01",
            "call on your Enigma.\x02\x03",
            "Until then, use your free time to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYes, ma'am!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1B, 0x1, 0x3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Jump("loc_3C4D")

    label("loc_3C4D")

    Jump("loc_42AD")

    label("loc_3C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4145")

    ChrTalk(
        0x9,
        (
            "#2002FI heard an interesting story, recently. Apparently,\x01",
            "a fight broke out between some delinquents and\x01",
            "bracers, and you decided to intervene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FCrap. You heard about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FU-Uh, we have a perfectly sound reason\x01",
            "for everything that happened yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2003FI don't want to hear your excuses. Delinquents\x01",
            "or not, it's unacceptable for the police to lay\x01",
            "their hands on citizens.\x02\x03",
            "#2000FWell, that's what I would normally say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2003FIn reality, police work requires you to subdue\x01",
            "criminals whether you'd like to or not.\x02\x03",
            "#2000FHowever, you're the Special Support Section--far\x01",
            "from a traditional police squad. You have the\x01",
            "advantage of tackling things unconventionally.\x02\x03",
            "#2004FIf you're dealing with hormone-crazed delinquents,\x01",
            "perhaps finding somewhere they can vent their\x01",
            "frustration isn't a bad idea... That's how see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FAre you sure you should be saying things\x01",
            "like that to us, Deputy Commander?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2004FI don't see why I should be the one to scold\x01",
            "you if Sergei didn't find it necessary.\x02\x03",
            "#2000FHehe. Just continue to do as you have\x01",
            "been, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FW-Will do, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Her ability to adapt to any situation is a\x01",
            "testament to her caliber as a guardswoman.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_42AD")

    label("loc_4145")


    ChrTalk(
        0x9,
        (
            "#2004FI don't see why I should be the one to scold\x01",
            "you, if Sergei didn't find it necessary. Simply\x01",
            "continue to do your best, like you have been.\x02\x03",
            "#2000FHowever, keep in mind that unconventional\x01",
            "methods can bring in unexpected results.\x02\x03",
            "Never forget to think long and hard about\x01",
            "what sort of outcome your actions will bring.\x01",
            "Do that, then act accordingly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42AD")

    Jump("loc_5139")

    label("loc_42B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_45EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A0")

    ChrTalk(
        0x9,
        "#2000FEnjoying the festival, everyone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FHah, that's a pretty cruel question. You know\x01",
            "better than anyone how insanely busy we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FLook on the bright side, Randy. At least we\x01",
            "were able to have the opening day of the\x01",
            "festival off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2003FI hope you used it to recover your energy.\x02\x03",
            "#2000FI imagine you'll encounter your share of\x01",
            "trouble throughout the festival.\x02\x03",
            "Just think of the event as an opportunity\x01",
            "to show off how you've improved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_45E7")

    label("loc_44A0")


    ChrTalk(
        0x9,
        (
            "#2000FNow, then, I think I'm going to start today's\x01",
            "work by putting together the results of the\x01",
            "Stargazer's Tower investigation.\x02\x03",
            "#2003FIf Seeker's report is anything to go by, this\x01",
            "isn't the sort of thing that we should ignore.\x02\x03",
            "#2000FIf possible, I'd like to organize a scouting\x01",
            "unit to dig a little deeper before long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45E7")

    Jump("loc_5139")

    label("loc_45EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4973")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F8")

    ChrTalk(
        0x9,
        "#2005FOh, did you need me for something?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_END)), "loc_47C5")

    ChrTalk(
        0x101,
        (
            "#0003F(I know we're going to investigate\x01",
            "Stargazer's Tower...but do you think\x01",
            "we should ask her for permission?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303F(I say we just keep quiet for now.)\x02\x03",
            "#0300F(No tellin' how much trouble we'd\x01",
            "get in if we spill the beans.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Hmm, that's a good point, I guess...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2005FHmm? What are you two whispering about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FN-Nothing, ma'am.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jump("loc_48F0")

    label("loc_47C5")


    ChrTalk(
        0x101,
        (
            "#0000FWe were in the area, so we thought we'd\x01",
            "stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205FCome to think of it, Sergeant Major Seeker is not\x01",
            "here, is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2000FThat's correct. She should be patrolling\x01",
            "the highways right about now.\x02\x03",
            "She'll be back sometime this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0103FIt sounds like she's very busy.\x02",
    )

    CloseMessageWindow()

    label("loc_48F0")

    SetScenarioFlags(0x0, 1)
    Jump("loc_496E")

    label("loc_48F8")


    ChrTalk(
        0x9,
        (
            "#2003FI'm sorry, but things have been hectic.\x01",
            "If you have business here, would you\x01",
            "mind postponing it for today?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_496E")

    Jump("loc_5139")

    label("loc_4973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4BB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ABA")

    ChrTalk(
        0x9,
        (
            "#2000FNot too long ago, there was a suspicious car\x01",
            "wreck that took place between Tangram Gate\x01",
            "and Altair.\x02\x03",
            "#2003FI insisted we investigate it, and we discovered\x01",
            "that the license plate matched the Revache\x01",
            "truck used in the monster attacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Did Heiyue have something to do with this?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4BAB")

    label("loc_4ABA")


    ChrTalk(
        0x9,
        (
            "#2003FA while ago, one of Revache's trucks wrecked\x01",
            "under suspicious circumstances...\x02\x03",
            "#2001F...and considering Revache men were injured\x01",
            "in the process, I can't write this off as a simple\x01",
            "accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001F(She's as sharp as always.)\x02",
    )

    CloseMessageWindow()

    label("loc_4BAB")

    Jump("loc_5139")

    label("loc_4BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5139")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4CB1")

    ChrTalk(
        0x9,
        (
            "#2000FI'd recommend that you all stay on guard\x01",
            "from here on out.\x02\x03",
            "We'll make sure to contact the SSS if we\x01",
            "ever require your assistance again.\x02\x03",
            "Though we can't publicly support your\x01",
            "endeavors, know that we're rooting for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5139")

    label("loc_4CB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_4D1A")

    ChrTalk(
        0x9,
        (
            "#2000FWe can start the training session whenever.\x02\x03",
            "So, are you ready to begin?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 13)
    Jump("loc_5139")

    label("loc_4D1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4D2E")
    Call(0, 12)
    Jump("loc_5139")

    label("loc_4D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FDE")

    ChrTalk(
        0x9,
        (
            "#2005FComing to see me directly isn't an\x01",
            "everyday occurrence. Is something\x01",
            "the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FNothing in particular. We were just in the\x01",
            "area and thought we'd check in on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303F#2S(Wasn't too hot about the idea myself...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2004FYet you still accompanied them, Orlando.\x01",
            "Still, there's no need to be embarrassed about\x01",
            "seeing me after such a praiseworthy feat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FY-You heard that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2002FThere was no need. Your face told me\x01",
            "all I needed to know.\x02\x03",
            "#2003FAnyway, you can count on the Guardian\x01",
            "Force's cooperation in missions to come.\x02\x03",
            "#2000FAnd if you ever require our support, you\x01",
            "need only ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThank you very much, ma'am.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5139")

    label("loc_4FDE")


    ChrTalk(
        0x9,
        (
            "#2003FAs I'm sure you're painfully aware, the corruption\x01",
            "that plagues Crossbell has even dug its claws into\x01",
            "the CGF...\x02\x03",
            "#2000FThat being said, since you four are free from the\x01",
            "obligations that tie us down, I believe that you'll\x01",
            "be able to fix the issues we can't face ourselves.\x02\x03",
            "Remember. If you ever require our support, you\x01",
            "need only ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5139")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    Return()

    # Function_7_2202 end

    def Function_8_5141(): pass

    label("Function_8_5141")


    ChrTalk(
        0x9,
        (
            "#2000FSince you're here, do you happen to\x01",
            "read often?\x02\x03",
            "If so, I wholeheartedly recommend this.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2D1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
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
            "#0300FHuh, wasn't expectin' ya to be such\x01",
            "a hardcore reader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2003FBe it for pleasure or not, reading is a cultural\x01",
            "experience that should be appreciated, no matter\x01",
            "the material.\x02\x03",
            "#2002FAnd I find these novels much more enjoyable than\x01",
            "the profane magazines you love to read. Although,\x01",
            "I assume you do more staring than reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FHey, don't go knocking on photo shoots...\x02\x03",
            "#0309FAfter all, they're my lifeblood! Couldn't\x01",
            "live without 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Really, Randy...?)\x02",
    )

    CloseMessageWindow()
    AddItemNumber(0x2D1, 1)
    SetScenarioFlags(0x9D, 3)
    Return()

    # Function_8_5141 end

    def Function_9_53DE(): pass

    label("Function_9_53DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_54A6")

    ChrTalk(
        0xFE,
        (
            "I assisted Sergeant Major Seeker's unit\x01",
            "in reinvestigating those ruins yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fortunately enough, no fiends have\x01",
            "reappeared. I'd be glad if things\x01",
            "stayed that way, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED4")

    label("loc_54A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_56F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55EC")

    ChrTalk(
        0xFE,
        (
            "In the end, the guardsmen weren't able\x01",
            "to finish the investigation, and you four plus\x01",
            "the sergeant major had to take over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess when push comes to shove, you\x01",
            "all are just better than us right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as one of Deputy Commander Baelz's\x01",
            "guardsmen, I don't plan on giving up...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_56EC")

    label("loc_55EC")


    ChrTalk(
        0xFE,
        (
            "Apparently, Sergeant Major Seeker and Deputy\x01",
            "Commander Baelz are having an important\x01",
            "discussion in the deputy commander's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Deputy Commander Baelz mentioned that\x01",
            "she's been wanting to thank you four. So,\x01",
            "if you're free, why not go see her?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56EC")

    Jump("loc_5ED4")

    label("loc_56F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_579B")

    ChrTalk(
        0xFE,
        (
            "Despite having hardly any injuries, Burrell\x01",
            "has been holed up in bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well. With a good rest, he'll be able to\x01",
            "return to his post in no time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED4")

    label("loc_579B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5807")

    ChrTalk(
        0xFE,
        (
            "I never have any time to relax here. I have\x01",
            "to see if anyone needs my help, after all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED4")

    label("loc_5807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_590C")

    ChrTalk(
        0xFE,
        (
            "CGF training is conducted at the police\x01",
            "academy's security department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Get this. I've heard that Sergeant Major\x01",
            "Seeker graduated from the academy with the\x01",
            "highest marks you can get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've really got to focus if I want to beat her...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5ED4")

    label("loc_590C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5A03")

    ChrTalk(
        0xFE,
        (
            "Deputy Commander Baelz couldn't care less\x01",
            "whether you're male or female. If you have\x01",
            "skill, then that's what she'll take note of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, we have to work harder than\x01",
            "what we're used to...but it's totally worth it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED4")

    label("loc_5A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B8D")

    ChrTalk(
        0xFE,
        (
            "Both Sergeant Major Seeker and Deputy\x01",
            "Commander Baelz had the day off yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that the sergeant major went to the city\x01",
            "to spend the day with her little sister, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but wonder what the deputy\x01",
            "commander ended up doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She isn't exactly the most social of people,\x01",
            "so I'm having a hard time coming up with\x01",
            "possibilities...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5C7F")

    label("loc_5B8D")


    ChrTalk(
        0xFE,
        (
            "Everything I've heard tells me that the deputy\x01",
            "commander is married to her job...but what if\x01",
            "she's in the middle of a passionate love affair?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She always scolds me for gossiping while\x01",
            "on duty, so I can't really go up and ask her...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C7F")

    Jump("loc_5ED4")

    label("loc_5C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D2C")

    ChrTalk(
        0xFE,
        (
            "CGF guardsmen are required to live at the\x01",
            "gate they're stationed at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even Sergeant Major Seeker stays here most\x01",
            "of the time, believe it or not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED4")

    label("loc_5D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5ED4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E14")

    ChrTalk(
        0xFE,
        (
            "Rumor says Deputy Commander Baelz and\x01",
            "your Chief Sergei go way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On top of that, they even talk on the phone\x01",
            "every so often...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Could they be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ahem. You can forget that nonsense.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5ED4")

    label("loc_5E14")


    ChrTalk(
        0xFE,
        "Putting aside their fishy relationship for now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I think that their connection will make the\x01",
            "teamwork between us that much stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's keep up the good work, all right?\x02",
    )

    CloseMessageWindow()

    label("loc_5ED4")

    TalkEnd(0xFE)
    Return()

    # Function_9_53DE end

    def Function_10_5ED8(): pass

    label("Function_10_5ED8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_605E")

    ChrTalk(
        0xFE,
        "O-Oh, Goddess...there were gh-ghosts...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0503FWhile investigating that temple, poor Burrell\x01",
            "here ran face-first into some monsters.\x02\x03",
            "#0501FAnd considering that he's pretty faint of\x01",
            "heart, he immediately passed out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0101F(*gulp*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FLet's make sure to go into this mission\x01",
            "prepared, everyone. Whatever scared\x01",
            "him this bad isn't going to be weak.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_608B")

    label("loc_605E")


    ChrTalk(
        0xFE,
        "P-Please...stay away from me, ghosts...\x02",
    )

    CloseMessageWindow()

    label("loc_608B")

    TalkEnd(0xFE)
    Return()

    # Function_10_5ED8 end

    def Function_11_608F(): pass

    label("Function_11_608F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6160")

    ChrTalk(
        0xFE,
        (
            "I've been informed that this isn't, in fact, the\x01",
            "passenger waiting room. How careless of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, be that as it may, I still have the\x01",
            "irresistible urge to clean up this mess...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_61C1")

    label("loc_6160")


    ChrTalk(
        0xFE,
        "Honestly, wanting to clean while on a trip...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's the mindset of a maid, I suppose.\x02",
    )

    CloseMessageWindow()

    label("loc_61C1")

    TalkEnd(0xFE)
    Return()

    # Function_11_608F end

    def Function_12_61C5(): pass

    label("Function_12_61C5")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0xE1, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_68(3870, 1200, -590, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25200, 0)
    SetChrPos(0x101, 3000, 0, 0, 90)
    SetChrPos(0x102, 3000, 0, -1500, 90)
    SetChrPos(0x103, 1500, 0, -1500, 90)
    SetChrPos(0x104, 1500, 0, 0, 90)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#11P#2002FFinally arrived, have you?\x02\x03",
            "I've been waiting, Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#0500FThanks for coming on such short notice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FIt means a lot that you're turning to us,\x01",
            "Deputy Commander, Sergeant Major\x01",
            "Seeker.\x02\x03",
            "I'm sure you're aware, but we're\x01",
            "here about your support request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0300F#2S(Wasn't too hot about coming myself...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2004FYet still you came, Orlando.\x02\x03",
            "There's no need to be embarrassed about\x01",
            "seeing me after such a praiseworthy feat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0305FY-You heard that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2004FHehe. There was no need. Your face\x01",
            "told me all I needed to know.\x02\x03",
            "#2000FNow, I'd like to go ahead and explain\x01",
            "the details of the support request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FPlease, by all means.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2000FHehe, very well, then. If you would do\x01",
            "the honors, Seeker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#0501FYes, ma'am!\x02\x03",
            "What we want from you four is pretty\x01",
            "straightforward, really.\x02\x03",
            "#0503FYou see, we're conducting a combat\x01",
            "training session for the new recruits today...\x02\x03",
            "#0501F...and we'd like for the SSS to serve as their\x01",
            "opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FYou want us to fight CGF members?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FThey may be recruits, but we would be\x01",
            "foolish to underestimate them.\x02\x03",
            "The Guardian Force is renowned for\x01",
            "their combat prowess, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2002FYou're well informed, Miss MacDowell.\x02\x03",
            "#2003FBesides, training with them will only improve\x01",
            "your own ability in the long run, right? I think\x01",
            "it's quite the deal, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FExcuse me, but why exactly did you choose the\x01",
            "SSS in particular for this request?\x02\x03",
            "#0203FI am loath to admit it, but there are likely many\x01",
            "other groups and individuals who excel in combat\x01",
            "that you could have picked instead.\x02\x03",
            "#0200FFor example...the Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0011FT-Tio, wait a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0303FI was actually wonderin' the same thing.\x02\x03",
            "Everyone knows that practicin' against\x01",
            "stronger guys gives ya better results.\x02\x03",
            "#0309FWhy DIDN'T you ask the bracers? Hell,\x01",
            "you still could, if you wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2004FSurely you aren't just grasping at any chance\x01",
            "to slip away from me, Orlando. Because that's\x01",
            "how I see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0306F*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2003FTo answer your question...\x02\x03",
            "...of course, given that the SSS has only been\x01",
            "operating for two months, veteran bracers would\x01",
            "be the better choice in terms of raw power.\x02\x03",
            "#2000FHowever, you four were able to solve the monster\x01",
            "attack case when the Guardian Force couldn't.\x01",
            "That, in and of itself, is quite special.\x02\x03",
            "To be more specific, you all operate under unique\x01",
            "circumstances that, in turn, allow you to shift your\x01",
            "focus away from just pure strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FUnique circumstances?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#0500FTake Randy, for example. Everyone at\x01",
            "Bellguard Gate goes on and on about\x01",
            "how exceptional he is in combat.\x02\x03",
            "I would think even the Bracer Guild\x01",
            "would find him to be a very valuable\x01",
            "asset.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6D97():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D97)
    Sleep(100)

    def lambda_6DA7():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6DA7)
    Sleep(50)

    def lambda_6DB7():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6DB7)
    Sleep(800)

    ChrTalk(
        0x101,
        "#6P#0005FS-Seriously? OUR Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0205FThat's the first I have heard of this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FI wasn't expecting to hear something like\x01",
            "that when I woke up this morning.\x02\x03",
            "#0100FWe're a team, Randy. Don't you think you\x01",
            "should have told us something that big?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FEh, it's old news. Not to mention, it'd\x01",
            "take forever to explain everything.\x02\x03",
            "#0306FMy lovely self aside, I gotta be honest.\x01",
            "I'm really not too pumped about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2003FIf you truly wish to sit on the sidelines, you\x01",
            "have my permission.\x02\x03",
            "#2002FI just thought you would have a tad more\x01",
            "gratitude for the one who recommended\x01",
            "you to the SSS in the first place.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_704F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_704F)
    Sleep(100)

    def lambda_705F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_705F)
    Sleep(50)

    def lambda_706F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_706F)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#0306FYou just HAD to pull that card!\x02\x03",
            "#0301FI get it, okay?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#2003FWise decision.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0012F(Something tells me that the deputy commander\x01",
            "is going to milk that for as long as she can...)\x02\x03",
            "#0003FB-Back to the topic at hand, I think we understand\x01",
            "what you want from us.\x02\x03",
            "#0000FWhen exactly does this training session start?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2000FI can mobilize the guardsmen immediately.\x02\x03",
            "Are you ready to begin as well? I hope you\x01",
            "came well prepared.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xF, 0x1, 0x0)
    Call(0, 13)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3000, 0, 0, 90)
    SetChrPos(0x1, 3000, 0, 0, 90)
    SetChrPos(0x2, 3000, 0, 0, 90)
    SetChrPos(0x3, 3000, 0, 0, 90)
    OP_68(3000, 900, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_12_61C5 end

    def Function_13_7304(): pass

    label("Function_13_7304")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "We need a few minutes.\x01",       # 0
            "Let's get this started!\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7355"),
        (1, "loc_73FE"),
        (SWITCH_DEFAULT, "loc_7559"),
    )


    label("loc_7355")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#6P#0006FI'm sorry. We still need some time\x01",
            "to get all our equipment in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2004FAh, I understand.\x02\x03",
            "#2000FWhen you're ready, just let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7559")

    label("loc_73FE")

    OP_4B(0x8, 0xFF)
    OP_60(0x0)

    ChrTalk(
        0x101,
        "#6P#0000FWe should be good to go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2004FGood.\x02\x03",
            "#2000FSeeker, if you would show them\x01",
            "to the parking lot?\x02\x03",
            "The training session will be held there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 300)

    ChrTalk(
        0x8,
        (
            "#5P#0501FYes, ma'am.\x02\x03",
            "#0500FEveryone, follow me!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Guardian Force Drill Participation]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_7559")

    label("loc_7559")

    Return()

    # Function_13_7304 end

    def Function_14_755A(): pass

    label("Function_14_755A")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0xE1, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_68(3870, 1200, -590, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26200, 0)
    SetChrPos(0x101, 3000, 0, 0, 90)
    SetChrPos(0x102, 3000, 0, -1500, 90)
    SetChrPos(0x103, 1500, 0, -1500, 90)
    SetChrPos(0x104, 1500, 0, 0, 90)
    Sleep(500)
    SetCameraDistance(25200, 1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#11P#2004FThank you once again, everyone.\x02\x03",
            "#2000FYour participation in today's training session\x01",
            "will no doubt prove invaluable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FNo need for thanks, ma'am. This has been\x01",
            "a great experience for us, too.\x02\x03",
            "It's not every day that we get to fight against\x01",
            "trained professionals like the Guardian Force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0109FIndeed. We should be the ones thanking you\x01",
            "for choosing us in the first place.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_78C0")
    OP_2C(0xF, 0x3)

    ChrTalk(
        0x104,
        (
            "#6P#0309FPlus, it felt good to lay the smackdown on\x01",
            "some of the CGF. No offense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FWe would have set a bad example if\x01",
            "we lost after all your colorful boasting\x01",
            "beforehand.\x02\x03",
            "#0200FYou must have been getting nervous\x01",
            "towards the end of the match, right, Randy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE0")

    label("loc_78C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_79C4")
    OP_2C(0xF, 0x1)

    ChrTalk(
        0x104,
        "#6P#0309FMan, whupping those guys sure felt good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FDid you forget that we lost once the\x01",
            "sergeant major entered the fray?\x02\x03",
            "#0200FFor one that constantly acts as her senior, I\x01",
            "assumed you would be a bit more embarrassed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE0")

    label("loc_79C4")


    ChrTalk(
        0x104,
        (
            "#6P#0300FHard to believe those guys actually got\x01",
            "the best of us, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FWell, despite it being a practice match and\x01",
            "you goading them beforehand, we still lost.\x02\x03",
            "#0200FRandy is probably going to cry himself to sleep\x01",
            "tonight, with his only company being his pillow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AE0")


    ChrTalk(
        0x104,
        "#6P#0306FLearn to pull your punches, Tio Tot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#0509FH-Haha. She got you there, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2004FRegardless of the result...\x02\x03",
            "#2000F...please continue the good work. Strive\x01",
            "for even greater heights.\x02\x03",
            "If your assistance is ever needed again,\x01",
            "we'll make sure to submit another request.\x02\x03",
            "And in return, you can count on the CGF\x01",
            "supporting the SSS from behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FThank you, ma'am! We'll do the same!\x02",
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
            "[Guardian Force Drill Participation]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3000, 0, 0, 90)
    SetChrPos(0x1, 3000, 0, 0, 90)
    SetChrPos(0x2, 3000, 0, 0, 90)
    SetChrPos(0x3, 3000, 0, 0, 90)
    OP_68(3000, 900, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    OP_29(0xF, 0x1, 0x4)
    OP_29(0xF, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_755A end

    def Function_15_7D9F(): pass

    label("Function_15_7D9F")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x9, 0x2)
    OP_68(6140, 900, -20, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24460, 0)
    SetChrPos(0x101, -3000, 0, 0, 90)
    SetChrPos(0x102, -3000, 0, -1500, 90)
    SetChrPos(0x103, -4500, 0, -1500, 90)
    SetChrPos(0x104, -4500, 0, 0, 90)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0000FExcuse us, ma'am.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xE1, 0x1F4)
    SetChrSubChip(0x9, 0x0)
    OP_68(3870, 1200, -590, 5000)
    MoveCamera(55, 17, 0, 5000)
    SetCameraDistance(26200, 5000)
    BeginChrThread(0x101, 3, 0, 16)
    BeginChrThread(0x102, 3, 0, 17)
    BeginChrThread(0x103, 3, 0, 18)
    BeginChrThread(0x104, 3, 0, 19)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x101,
        (
            "#0000FGood afternoon, Deputy Commander,\x01",
            "Sergeant Major.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#0500FNice to see you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2000FHello, you four.\x02\x03",
            "#2001FGiven you came to see me directly, I\x01",
            "assume that something's happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FYes, actually. There's something we'd\x01",
            "like to discuss with you, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that they had come to Tangram Gate\x01",
            "in order to figure out how to crack down on counterfeit\x01",
            "dealers crossing the border.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#11P#2003FI think I understand your predicament.\x02\x03",
            "#2000FYou can count on Tangram Gate's cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FThank you, Deputy Commander.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0305FHold up. That's that?\x02\x03",
            "Ain't the border gates crazy busy during\x01",
            "the Anniversary Festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#0500FNo need to worry about that, Randy.\x02\x03",
            "#0503FAs I'm sure you know, the CGF primarily\x01",
            "focuses on border security here at the gates.\x02\x03",
            "#0500FSure, we may be swamped, but I think\x01",
            "we're obligated to help out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2004FWell put, Seeker. The Special Support Section\x01",
            "shouldn't have to worry about our workload.\x02\x03",
            "#2000FThat being said, we are currently short on hands,\x01",
            "so we can't do much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0202FAny assistance you can provide is welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FAnd I know it's sudden, but do you think\x01",
            "we'll have an opportunity to interview the\x01",
            "incoming passengers from the Republic?\x02\x03",
            "#0003FAccording to police intel, the counterfeit\x01",
            "dealer will be arriving at Tangram Gate\x01",
            "around noon today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2003FNoon, hmm? Now that you mention it,\x01",
            "I believe there is a bus scheduled to\x01",
            "arrive relatively soon.\x02\x03",
            "If your intel truly is accurate, your\x01",
            "dealer should be on board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#0501FYou know, there's a bit of a delay before\x01",
            "the bus heading to the city shows up.\x02\x03",
            "Usually, passengers waiting for the\x01",
            "connection go to the mess hall to rest\x01",
            "or have a quick meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FSounds like we've got ourselves a plan, then.\x02\x03",
            "#0303FFirst, the sergeant major will escort all\x01",
            "of the passengers into the mess hall.\x02\x03",
            "#0300FNext, we'll stroll in, not causin' any ruckus,\x01",
            "and try to find our counterfeit dealer.\x02\x03",
            "#0309FIf you've ever wanted to show off your\x01",
            "detective chops, Lloyd, now's your time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FLeave it to me.\x02\x03",
            "We may have a small window, but\x01",
            "it should be enough time to screen\x01",
            "most of the passengers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FI am curious to see whether we can pull\x01",
            "this off without giving ourselves away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0101FThe pressure is starting to get to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2003FThere's little time remaining until the\x01",
            "bus arrives from the Republic.\x02\x03",
            "If you stay at the gate, you should have\x01",
            "enough time to rest beforehand.\x02\x03",
            "#2000FHow about it? I can have beds prepared\x01",
            "for you, if needed.\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Still have some errands to run.\x01",              # 0
            "Time for some R&R before the bus comes.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8963"),
        (1, "loc_8AA2"),
        (SWITCH_DEFAULT, "loc_8BB5"),
    )


    label("loc_8963")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#0003FI think we still need a little more time to\x01",
            "prepare, if that's okay with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2000FVery well.\x02\x03",
            "When you're ready to go, let me know.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 3000, 0, 0, 90)
    SetChrPos(0x1, 3000, 0, 0, 90)
    SetChrPos(0x2, 3000, 0, 0, 90)
    SetChrPos(0x3, 3000, 0, 0, 90)
    OP_68(3000, 900, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    OP_93(0x8, 0x10E, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    OP_29(0x1B, 0x1, 0x2)
    EventEnd(0x5)
    Jump("loc_8BB5")

    label("loc_8AA2")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#6P#0000FI think we'll take you up on that offer,\x01",
            "Deputy Commander Baelz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#2000FVery well.\x02\x03",
            "Once the bus arrives, I'll give you a\x01",
            "call on your Enigma.\x02\x03",
            "Until then, use your free time to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001FYes, ma'am!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1B, 0x1, 0x2)
    OP_29(0x1B, 0x1, 0x3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Jump("loc_8BB5")

    label("loc_8BB5")

    Return()

    # Function_15_7D9F end

    def Function_16_8BB6(): pass

    label("Function_16_8BB6")


    def lambda_8BBB():
        OP_95(0xFE, 3000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8BBB)
    WaitChrThread(0x101, 1)
    Return()

    # Function_16_8BB6 end

    def Function_17_8BD5(): pass

    label("Function_17_8BD5")


    def lambda_8BDA():
        OP_95(0xFE, 3000, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8BDA)
    WaitChrThread(0x102, 1)
    Return()

    # Function_17_8BD5 end

    def Function_18_8BF4(): pass

    label("Function_18_8BF4")


    def lambda_8BF9():
        OP_95(0xFE, 1500, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8BF9)
    WaitChrThread(0x103, 1)
    Return()

    # Function_18_8BF4 end

    def Function_19_8C13(): pass

    label("Function_19_8C13")


    def lambda_8C18():
        OP_95(0xFE, 1500, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8C18)
    WaitChrThread(0x104, 1)
    Return()

    # Function_19_8C13 end

    def Function_20_8C32(): pass

    label("Function_20_8C32")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F18")

    ChrTalk(
        0x103,
        (
            "#0205FThis stuffed animal...\x02\x03",
            "#0203FWhat is this sense of deja vu?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0509FHaha... That's mine, actually.\x02\x03",
            "#0500FTruth is, Fran gave it to me back when I was\x01",
            "going through training. She wanted my room\x01",
            "to have a bit more color, apparently.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8DA2")

    ChrTalk(
        0x101,
        (
            "#0002FNow that I think about it, Fran's stuffed\x01",
            "animal was a different color, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E42")

    label("loc_8DA2")


    ChrTalk(
        0x101,
        (
            "#0005FOh, now that you mention it...\x02\x03",
            "#0002FWe saw a similar stuffed animal when we\x01",
            "stopped by Fran's house, right? But it was\x01",
            "a different color, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E42")


    ChrTalk(
        0x104,
        "#0309FHaha! A matchin' set, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FI can't help but feel a little jealous of how\x01",
            "well you get along with your sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0509FR-Really? (Geez, how can she say\x01",
            "that with a straight face...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 2)
    Jump("loc_8FB4")

    label("loc_8F18")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's Noel's stuffed animal. Fran has the same\x01",
            "animal, but it's a different color.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#0506F(Maybe I should have kept it hidden, after all...)\x02",
    )

    CloseMessageWindow()

    label("loc_8FB4")

    TalkEnd(0xFF)
    Return()

    # Function_20_8C32 end

    SaveToFile()

Try(main)
