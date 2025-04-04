from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1300.bin",                # FileName
        "c1300",                    # MapName
        "c1300",                    # Location
        0x001B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 27, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1300",                  # 0
        "Security Guard Bills",   # 1
        "Security Guard Wang",    # 2
        "Secretary Ernest",       # 3
        "Grace",                  # 4
        "It's a dummyyy!",        # 5
        "Central Square",         # 6
        "West Street",            # 7
        "Administrative District",# 8
        "Residential District",   # 9
        "Entertainment District", # 10
        "East Street",            # 11
        "Downtown District",      # 12
        "Harbor District",        # 13
        "IBC",                    # 14
        "Station Street",         # 15
        "Back Alley",             # 16
        "Ursula Road",            # 17
        "East Crossbell Highway", # 18
        "West Crossbell Highway", # 19
        "Mainz Mountain Path",    # 20
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
    ))

    DeclNpc(3910,    0,       5050,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(1700,    0,       -22129,  180,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(1750,    0,       -1799,   0,    510,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(7000,    0,       2300,    1200,    7000,    1700,    2300,    0x007C, 0,  10, 0x0000)
    DeclActor(1750,    0,       -1800,   1500,    1750,    1500,    -1800,   0x007C, 0,  5,  0x0000)

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "Central Square")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "West Street")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "Administrative District")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "Residential District")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "Downtown District")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "Harbor District")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "IBC")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "Station Street")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "Back Alley")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "Ursula Road")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-284.45001220703125, 0.0, -47.290000915527344, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-163.66000366210938, 0.0, -206.52999877929688, 0x0000, 0x0051, "")
    PlaceName(-90.51000213623047, 0.0, -171.14999389648438, 0x0000, 0x0054, "")
    PlaceName(-130.32000732421875, 0.0, -217.4199981689453, 0x0000, 0x0057, "")
    PlaceName(-164.67999267578125, 0.0, -167.05999755859375, 0x0000, 0x0053, "")
    PlaceName(-136.77999877929688, 0.0, -134.39999389648438, 0x0000, 0x0053, "")
    PlaceName(-205.85000610351562, 0.0, -173.8699951171875, 0x0000, 0x0053, "")
    PlaceName(-219.1199951171875, 0.0, -145.2899932861328, 0x0000, 0x0053, "")
    PlaceName(-186.4600067138672, 0.0, -101.7300033569336, 0x0000, 0x0052, "")
    PlaceName(-179.99000549316406, 0.0, -119.43000030517578, 0x0000, 0x0053, "")
    PlaceName(-168.0800018310547, 0.0, -131.0, 0x0000, 0x0053, "")
    PlaceName(-129.3000030517578, 0.0, -34.369998931884766, 0x0000, 0x0051, "")
    PlaceName(23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0052, "")
    PlaceName(0.0, 0.0, -341.95001220703125, 0x0000, 0x0053, "")
    PlaceName(-17.690000534057617, 0.0, -316.7699890136719, 0x0000, 0x0053, "")
    PlaceName(-118.41000366210938, 0.0, -203.80999755859375, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_4A8",          # 01, 1
        "Function_2_6C0",          # 02, 2
        "Function_3_813",          # 03, 3
        "Function_4_1D36",         # 04, 4
        "Function_5_1E6D",         # 05, 5
        "Function_6_2192",         # 06, 6
        "Function_7_221D",         # 07, 7
        "Function_8_2871",         # 08, 8
        "Function_9_4E01",         # 09, 9
        "Function_10_58F4",        # 0A, 10
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_430"),
        (1, "loc_43C"),
        (2, "loc_448"),
        (3, "loc_454"),
        (4, "loc_460"),
        (5, "loc_46C"),
        (6, "loc_478"),
        (SWITCH_DEFAULT, "loc_484"),
    )


    label("loc_430")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_43C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_448")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_454")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_460")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_46C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_478")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_484")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_490")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_4A7")

    Return()

    # Function_0_3F0 end

    def Function_1_4A8(): pass

    label("Function_1_4A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_557")
    SetChrPos(0x0, -230, -1450, -33980, 0)
    SetChrPos(0x1, -230, -1450, -33980, 0)
    SetChrPos(0x2, -230, -1450, -33980, 0)
    SetChrPos(0x3, -230, -1450, -33980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52F")
    SetChrPos(0x4, -230, -1450, -33980, 0)
    SetChrPos(0x5, -230, -1450, -33980, 0)
    Jump("loc_54E")

    label("loc_52F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54E")
    SetChrPos(0x4, -230, -1450, -33980, 0)

    label("loc_54E")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_557")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_56F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 6)

    label("loc_56F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A")
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_5AD")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A0")
    Event(0, 9)
    Jump("loc_5AD")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AD")
    SetScenarioFlags(0x53, 2)

    label("loc_5AD")

    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5DB")
    SetChrPos(0x8, -2040, 0, -21950, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_6A8")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5E9")
    Jump("loc_6A8")

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5F7")
    Jump("loc_6A8")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_616")
    SetChrPos(0x8, 2610, 0, 2230, 160)
    Jump("loc_6A8")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_635")
    SetChrPos(0x8, -180, 0, -22030, 180)
    Jump("loc_6A8")

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_643")
    Jump("loc_6A8")

    label("loc_643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_651")
    Jump("loc_6A8")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_65F")
    Jump("loc_6A8")

    label("loc_65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_66D")
    Jump("loc_6A8")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_67B")
    Jump("loc_6A8")

    label("loc_67B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_689")
    Jump("loc_6A8")

    label("loc_689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_697")
    Jump("loc_6A8")

    label("loc_697")

    SetChrPos(0x8, -180, 0, -22030, 180)

    label("loc_6A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BF")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_6BF")

    Return()

    # Function_1_4A8 end

    def Function_2_6C0(): pass

    label("Function_2_6C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_718")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_779")

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_754")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_779")

    label("loc_754")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_779")

    SetMapObjFlags(0x2, 0x4)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A8")
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_7A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B6")

    label("loc_7B6")

    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D2")
    OP_70(0x1, 0x0)

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E4")
    OP_70(0x1, 0x0)

    label("loc_7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7F1")
    OP_70(0x1, 0x0)

    label("loc_7F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80D")
    Jump("loc_812")

    label("loc_80D")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_812")

    Return()

    # Function_2_6C0 end

    def Function_3_813(): pass

    label("Function_3_813")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_897")

    ChrTalk(
        0xFE,
        (
            "I'm terribly sorry, but the IBC only conducts\x01",
            "business up until 4:30PM.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come back another time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E5")

    label("loc_897")


    ChrTalk(
        0xFE,
        "The gate's lock is fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No abnormalities found. All clear!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0x8, 0x10)

    label("loc_8E5")

    Jump("loc_1D32")

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9BB")

    ChrTalk(
        0xFE,
        (
            "We boast excellent security, and we even\x01",
            "receive reports regarding incidents in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That being said, a case involving missing people\x01",
            "falls within the CPD's jurisdiction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAD")

    label("loc_9BB")


    ChrTalk(
        0xFE,
        (
            "The security department recently received\x01",
            "some troubling information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's been a massive surge in reports\x01",
            "of people going missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything's been fine at the IBC,\x01",
            "so I guess we'll just have to leave\x01",
            "it to the police.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AAD")

    Jump("loc_1D32")

    label("loc_AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B4C")

    ChrTalk(
        0xFE,
        (
            "There was a firefight in the Harbor District\x01",
            "last night. It just serves as a reminder that\x01",
            "guards like us have to stay sharp.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C34")

    label("loc_B4C")


    ChrTalk(
        0xFE,
        (
            "We saw a report about a shooting that\x01",
            "took place in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I kinda got the impression that there's some sort\x01",
            "of turf war going on in the underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have a lot more guards posted\x01",
            "than usual today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C34")

    Jump("loc_1D32")

    label("loc_C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D02")

    ChrTalk(
        0xFE,
        (
            "Probably has something to do with those\x01",
            "strange rumors I've been hearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At first glance, you'd think the man's a playboy, but\x01",
            "he's apparently the CEO's acquaintance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA1")

    label("loc_D02")


    ChrTalk(
        0xFE,
        (
            "Mr. Crois went out of his way to greet\x01",
            "us, now that he's back in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who was the young man, though?\x01",
            "Must have been the CEO's acquaintance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_DA1")

    Jump("loc_1D32")

    label("loc_DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_F34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E9C")

    ChrTalk(
        0xFE,
        (
            "By the way, Mariabell took a little trip out\x01",
            "into the city while the CEO is gone for\x01",
            "a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I remember her mentioning something\x01",
            "about taking care of some business in the\x01",
            "Administrative District.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2F")

    label("loc_E9C")


    ChrTalk(
        0xFE,
        (
            "Hey there. Sorry to stop you, but today's\x01",
            "a corporate holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Entry by any unauthorized individuals\x01",
            "is prohibited. Sorry about that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F2F")

    Jump("loc_1D32")

    label("loc_F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1167")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1029")

    ChrTalk(
        0xFE,
        (
            "I heard that somebody hacked into the\x01",
            "IBC's systems through the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, man. Us guards don't deal with that stuff.\x01",
            "I guess the boys in the tech department\x01",
            "will have their hands full with this one, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1162")

    label("loc_1029")


    ChrTalk(
        0xFE,
        (
            "There aren't any problems with how the\x01",
            "IBC building's security is handled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have guards posted in there twenty-four\x01",
            "hours a day, so it's locked down tightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not much we can do against hacks, though.\x01",
            "That technical junk flies over my head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, man. I have no clue about any of that junk.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1162")

    Jump("loc_1D32")

    label("loc_1167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11E3")

    ChrTalk(
        0xFE,
        "Do you have business here? Step right inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The receptionist is just ahead in the lobby.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12C0")

    label("loc_11E3")

    SetScenarioFlags(0x0, 0)

    ChrTalk(
        0xFE,
        (
            "Good morning. This is some nice weather\x01",
            "we're having, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The IBC is far from the bustle of the streets,\x01",
            "so it has a nice and quiet atmosphere during\x01",
            "the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My motivation has returned today!\x02",
    )

    CloseMessageWindow()

    label("loc_12C0")

    Jump("loc_1D32")

    label("loc_12C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1379")

    ChrTalk(
        0xFE,
        (
            "To be a guard means to not interfere with the\x01",
            "customers, and to keep the peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But we also have to deal with the\x01",
            "occasional security threat, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145B")

    label("loc_1379")


    ChrTalk(
        0xFE,
        (
            "You should have seen how dejected those businessmen\x01",
            "walking through the lobby today looked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm guessing they struck out hard on some deals.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, we're just guards.\x01",
            "It's not our job to give them a pep talk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_145B")

    Jump("loc_1D32")

    label("loc_1460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1620")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_150D")

    ChrTalk(
        0xFE,
        (
            "It's my duty to welcome Mr. Crois\x01",
            "whenever he enters the bank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you've ever seen a fancy red limousine\x01",
            "cruising through town, that's his.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161B")

    label("loc_150D")


    ChrTalk(
        0xFE,
        (
            "Considering he's the head of the IBC,\x01",
            "Mr. Crois is an extremely busy man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's usually out conducting business in other\x01",
            "countries, so he's not around often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But when he does return, I'd damn well better\x01",
            "be sure to welcome him with everything I've got.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_161B")

    Jump("loc_1D32")

    label("loc_1620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1705")

    ChrTalk(
        0xFE,
        (
            "The IBC sits pretty high up on the land, so\x01",
            "even us guards get to enjoy a nice view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll hear no complaints about my job from me.\x01",
            "Everybody working in the main building seems\x01",
            "to enjoy it here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187B")

    label("loc_1705")


    ChrTalk(
        0xFE,
        (
            "I often like to think about how wonderful a place\x01",
            "the IBC is to work at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can see the entire cityscape, along with a\x01",
            "long, flowing river with just one quick glance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's green as far as the eye can see.\x01",
            "I've got no complaints about my workplace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only is the view great, but the location itself\x01",
            "has a tactical advantage in terms of security.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_187B")

    Jump("loc_1D32")

    label("loc_1880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_194A")

    ChrTalk(
        0xFE,
        (
            "Oh, yeah, there was a mayoral election that\x01",
            "year, wasn't there? Those only happen once\x01",
            "every five years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was a busy and stressful year for\x01",
            "a greenhorn like myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6F")

    label("loc_194A")


    ChrTalk(
        0xFE,
        (
            "It's been about ten years since I was first assigned\x01",
            "to work for the IBC's security department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Around the time this building was finished, I think...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, that was a pretty busy year for me.\x01",
            "I had just taken up a new post, only to be\x01",
            "reassigned to the IBC's main building.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A6F")

    Jump("loc_1D32")

    label("loc_1A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B02")

    ChrTalk(
        0xFE,
        (
            "Welcome to the IBC's corporate headquarters.\x01",
            "Is there something we can help you with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please take your time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C24")

    label("loc_1B02")


    ChrTalk(
        0xFE,
        (
            "Good morning. Welcome to the IBC's\x01",
            "corporate headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Are you surprised? Pretty impressive\x01",
            "building, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not unusual for people to be astonished the\x01",
            "first time they see the building in all of its glory.\x01",
            "The awe has worn off on the employees, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C24")

    Jump("loc_1D32")

    label("loc_1C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C8F")

    ChrTalk(
        0xFE,
        "The IBC is closed today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Entry by any unauthorized individuals\x01",
            "is prohibited.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D32")

    label("loc_1C8F")


    ChrTalk(
        0xFE,
        "Hi there. Good weather today, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today's a corporate holiday for the\x01",
            "IBC, so we're closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Entry by any unauthorized individuals\x01",
            "is prohibited.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D32")

    TalkEnd(0xFE)
    Return()

    # Function_3_813 end

    def Function_4_1D36(): pass

    label("Function_4_1D36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1DD1")

    ChrTalk(
        0xFE,
        (
            "We're in the middle of locking up\x01",
            "the front gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but if you have business, we'll have\x01",
            "to ask you to come back tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E69")

    label("loc_1DD1")


    ChrTalk(
        0xFE,
        "Oh, it's closing time already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone is about to go home for\x01",
            "the day. If you have any banking to\x01",
            "do, it'll have to wait until tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1E69")

    TalkEnd(0xFE)
    Return()

    # Function_4_1D36 end

    def Function_5_1E6D(): pass

    label("Function_5_1E6D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2120")
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)

    NpcTalk(
        0xC,
        "Man's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#N#2SHa ha ha...\x01",
            "What a truly interesting thing to mention.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Man's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#N#2SWell, it's exactly as you say!\x01",
            "Who would have thought I'd meet a character\x01",
            "such as yourself in Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Young Man's Voice")
    SetMessageWindowPos(240, 150, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2SYou're something, too, old man.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2SYou weren't satisfied with just being a banker\x01",
            "your whole life, so you shot for the stars.\x01",
            "I should follow in your footsteps. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FHey, isn't that Mr. Crois' limousine?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FThey seem to be engaged in some kind\x01",
            "of conversation in there...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2120")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Peer Inside the Limousine\x01",      # 0
            "Don't\x01",                          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2184")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("e0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_2191")

    label("loc_2184")

    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_2191")

    Return()

    # Function_5_1E6D end

    def Function_6_2192(): pass

    label("Function_6_2192")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1020, 2500, -560, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, 1020, 0, -560, 135)
    SetChrPos(0x1, 1020, 0, -560, 135)
    SetChrPos(0x2, 1020, 0, -560, 135)
    SetChrPos(0x3, 1020, 0, -560, 135)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_6_2192 end

    def Function_7_221D(): pass

    label("Function_7_221D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, -970, 0, -25140, 0)
    SetChrPos(0x102, 630, 0, -25140, 0)
    SetChrPos(0x103, 630, 0, -26970, 0)
    SetChrPos(0x104, -970, 0, -26970, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-3130, 2500, -17030, 0)
    MoveCamera(48, 16, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_68(-140, 4630, 2210, 8000)
    MoveCamera(24, 23, 0, 8000)
    OP_6E(750, 8000)
    SetCameraDistance(39300, 8000)
    PlaceName2(340, 200, "c_plac06", 0x0, 4000)
    OP_6F(0x79)
    Sleep(1000)

    AnonymousTalk(
        0x101,
        (
            "#0000FThis is the IBC's main headquarters, isn't it?\x01",
            "It's an impressive building.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#0104FYes, this is indeed the IBC's main headquarters.\x02\x03",
            "Not only do they have many branches spread\x01",
            "throughout all of Zemuria, but their services\x01",
            "extend beyond just banking.\x02\x03",
            "#0102FThey became the continent's lead asset holder ten\x01",
            "years ago. It wouldn't be an exaggeration to call\x01",
            "the IBC the cornerstone of Crossbell's economy.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#0200FIndeed. The IBC is an unfathomed force in \x01",
            "the finance, construction, and real estate\x01",
            "industries.\x02\x03",
            "#0203FTheir latest ambition has been to fund a variety\x01",
            "of massive public projects for Crossbell.\x02\x03",
            "Reports have shown them investing a fortune\x01",
            "into the expansion of the Geofront and\x01",
            "the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#0305F*sigh* Not the kinda place I'd normally\x01",
            "associate with.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1890, 2500, -27740, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(10800, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    TurnDirection(0x103, 0x104, 500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#0200F#11PExcuse me, Randy. You are aware\x01",
            "that our salaries are transferred to\x01",
            "us through the IBC, correct?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        "#0301F#6PW-Wait, are you kiddin' me?\x02",
    )

    CloseMessageWindow()

    def lambda_275D():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_275D)
    Sleep(50)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#0000F#5PConsidering they're within the city,\x01",
            "it's pretty convenient for us.\x02\x03",
            "#0006FAlthough, I think the bank's closed today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104F#11PCorrect. The employees are given weekends\x01",
            "off.\x02\x03",
            "#0100FLet's come back some other time.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -970, 0, -25140, 0)
    SetScenarioFlags(0x47, 4)
    EventEnd(0x5)
    Return()

    # Function_7_221D end

    def Function_8_2871(): pass

    label("Function_8_2871")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02300.itc", 0x1E)
    LoadChrToIndex("chr/ch06000.itc", 0x1F)
    OP_68(0, -1000, -34200, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15000, 0)
    OP_90(0x101, -650, -1700, -37200, 0)
    OP_90(0x102, 650, -1700, -37200, 0)
    OP_90(0x103, -1200, -1900, -38400, 0)
    OP_90(0x104, 1200, -1900, -38400, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 0, -10500, 180)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 0, 0, -12500, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02600.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    ClearMapFlags(0x10000000)

    def lambda_29A1():
        OP_96(0xFE, 0xFFFFFD76, 0x0, 0xFFFF9D90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29A1)
    Sleep(200)

    def lambda_29BE():
        OP_96(0xFE, 0x28A, 0x0, 0xFFFF9D90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29BE)
    Sleep(100)

    def lambda_29DB():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0xFFFF98E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29DB)
    Sleep(200)

    def lambda_29F8():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFF98E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29F8)
    OP_68(0, 4700, -17700, 8000)
    MoveCamera(0, -9, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(13000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x41)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BA0")

    ChrTalk(
        0x104,
        (
            "#2200176V#0305FThis is the fancy-schmancy IBC building, eh?\x02\x03",
            "#2200177V#0302FMan, take a look at our surroundings.\x01",
            "They freakin' went all out building this thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200178V#0204FI agree wholeheartedly.\x02\x03",
            "#2200179V#0202FYou are unlikely to find any other buildings\x01",
            "as advanced as this one in Zemuria.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x53, 2)
    Jump("loc_2BEB")

    label("loc_2BA0")


    ChrTalk(
        0x104,
        (
            "#2200180V#0302FThe IBC building, eh? Thing never fails\x01",
            "to impress me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BEB")


    ChrTalk(
        0x101,
        (
            "#2200181V#0002F#5PYeah, it's enormous. I'd guess it's\x01",
            "at least 10 stories high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200182V#0104F#11PI believe it's about 16 stories...\x02\x03",
            "#2200183V#0100FI've also heard companies unaffiliated with\x01",
            "the IBC rent office space between the fifth\x01",
            "and tenth floors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200184V#0000F#5POh, really? That's news to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200185V#0204FIndeed. They are a significant source of\x01",
            "Crossbell's tax revenue.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1000, -25800, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2200186V#6P#0001FSo...what's the plan?\x02\x03",
            "#2200187VWe did show up without an appointment,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#2200188V#11P#0101FWhy don't we try speaking with the receptionist?\x01",
            "She may be able to help us.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    NpcTalk(
        0xA,
        "Man's Voice",
        "#2200189VOh, Elie?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_2F1E():
        OP_95(0xFE, 0, 0, -22600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2F1E)
    Sleep(1000)

    def lambda_2F3B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F3B)

    def lambda_2F48():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F48)
    OP_68(0, 1000, -24000, 3000)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#2200221V#0105FE-Ernest...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            "#2200191VFancy meeting you here.\x02\x03",
            "#2200192VI see you're with your colleagues,\x01",
            "so I can only assume you're\x01",
            "here for work.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#2200193V#0104FYes, we are. There's something we'd\x01",
            "like to look into.\x02\x03",
            "#2200194V#0100FAre you here to see Dieter Crois, Ernest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200195V#2604F#5PAh, yes. I went for a consultation regarding how\x01",
            "to manage the office's operational funds.\x02\x03",
            "#2200196V#2600FAs you know, work will become much busier next\x01",
            "month, so I'm trying to get a head start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200197V#0108FI see. That makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200198V#2603F#5POh, by the way, Elie.\x02\x03",
            "#2200199V#2601FHave you given my offer some thought?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200200V#0103F...Yes, I have.\x02\x03",
            "#2200201V#0101FI apologize, but I'm not ready to resign\x01",
            "from the force just yet.\x02\x03",
            "#2200202VI still haven't truly accomplished my goal.\x02\x03",
            "#2200203VAnd as long as that continues to be the\x01",
            "case, I'm only half the woman I could be.\x02\x03",
            "#2200204V#0103FAs a matter of fact, I'm positive I'd only be a\x01",
            "burden to Grandfather with the way I am now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200205V#2605F#5PCould you answer this, at least?\x02\x03",
            "#2200206V#2601FIs the road you've taken the only way for\x01",
            "you to achieve your goal?\x02\x03",
            "#2200207VWhat if it's an illusion? All your efforts\x01",
            "would go to waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200208V#0106FI don't deny the possibility...\x02\x03",
            "#2200209V#0102F...however, the knowledge I've gained these\x01",
            "last two months has broadened my horizons\x01",
            "more than I could have ever hoped.\x02\x03",
            "#2200210VI feel myself growing as a person with\x01",
            "each new obstacle we overcome.\x02\x03",
            "#2200211V#0109FHad I followed your advice and immediately became\x01",
            "one of Grandfather's secretaries, I would have\x01",
            "missed out on all of these valuable experiences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200212V#2605F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200213V#0104FI'll have to apologize to you once more.\x02\x03",
            "#2200214V#0100FI'm going to continue to work with the SSS as\x01",
            "hard as I can until I've reached my full potential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200215V#2606F#5P*sigh*...\x02\x03",
            "#2200216V#2600FWell, at least you're not as uncertain\x01",
            "as you were before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200217V#0105FIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200218V#2600F#5PVery well, then. I won't press you any further.\x02\x03",
            "#2200219V#2604FHow unfortunate. Just when I thought I'd\x01",
            "gained a capable aide.\x02\x03",
            "#2200220VYou've defied my expectations, Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200190V#0102FErnest...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200222V#2603F#5PI have one small request of you, though.\x02\x03",
            "#2200223V#2600FI would like you to attend the Anniversary\x01",
            "Festival's opening ceremony next month.\x02\x03",
            "#2200224VAs much as I'd love for your mother to come,\x01",
            "we know that won't be happening.\x02\x03",
            "#2200225VYour Grandfather may become lonely if\x01",
            "none of his family members attend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200226V#0104FUnderstood. I'll make sure to be there.\x02\x03",
            "#2200227V#0100FWell, Ernest, thank you for everything\x01",
            "you've done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200228V#2604F#5PHaha. Well, I was your teacher at\x01",
            "one point, remember?\x02\x03",
            "#2200229V#2600FThis is trivial compared to that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#2200230V#2605F#5POh, would you look at the time? I didn't mean\x01",
            "to take you all away from your duties.\x02\x03",
            "#2200231V#2604FIf you'll excuse me, everyone.\x02\x03",
            "#2200232V#2600FAlso, I'll be leaving Elie in your care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200233V#12P#0002FRight...\x02",
    )

    CloseMessageWindow()

    def lambda_3BE8():

        label("loc_3BE8")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_3BE8")

    QueueWorkItem2(0x101, 2, lambda_3BE8)

    def lambda_3BFA():

        label("loc_3BFA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_3BFA")

    QueueWorkItem2(0x102, 2, lambda_3BFA)

    def lambda_3C0C():
        OP_95(0xFE, -1900, 0, -24200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3C0C)
    Sleep(500)

    def lambda_3C29():

        label("loc_3C29")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_3C29")

    QueueWorkItem2(0x104, 2, lambda_3C29)

    def lambda_3C3B():

        label("loc_3C3B")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_3C3B")

    QueueWorkItem2(0x103, 2, lambda_3C3B)
    WaitChrThread(0xA, 1)
    OP_68(0, 1000, -27000, 3000)

    def lambda_3C62():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD120, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3C62)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)
    EndChrThread(0x101, 0x2)

    def lambda_3C86():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C86)
    Sleep(50)
    EndChrThread(0x102, 0x2)

    def lambda_3C9A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C9A)
    EndChrThread(0x103, 0x2)

    def lambda_3CAB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3CAB)
    Sleep(50)
    EndChrThread(0x104, 0x2)

    def lambda_3CBF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3CBF)
    WaitChrThread(0x104, 2)
    ClearChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    ChrTalk(
        0x102,
        "#2200234V#5P#0108F...\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, -25800, 1000)

    def lambda_3D0B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D0B)
    Sleep(150)

    def lambda_3D1B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3D1B)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#2200235V#6P#0000FI get the impression you're on his mind\x01",
            "a lot, Elie.\x02\x03",
            "#2200236VAlso, what was that about Ernest being\x01",
            "your teacher?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#2200237V#5P#0102FOh, that? He was my tutor when I was\x01",
            "a child.\x02\x03",
            "#2200238V#0104FSadly, we haven't talked much since I\x01",
            "returned from my studies abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200239V#6P#0200FI assume he wishes to become a\x01",
            "member of the diet, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200240V#5P#0100FCorrect. I think he plans to announce his\x01",
            "candidacy for next year's diet election.\x02\x03",
            "#2200241V#0108FIt'll be difficult for him to win, though. I don't\x01",
            "think he plans on joining either the Imperial\x01",
            "or Republican factions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200242V#12P#0303FSo he's an aspiring politician, eh?\x02\x03",
            "#2200243V#0300FThough I gotta say, he's pretty built for a\x01",
            "secretary.\x02\x03",
            "#2200244VHe practice some kinda martial arts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200245V#5P#0105FHe's an experienced fencer, if I recall correctly.\x02\x03",
            "#2200246V#0100FI heard that he also serves as Grandfather's\x01",
            "bodyguard because of his skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200247V#6P#0000FOh, I see. That'd explain why he's in shape.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)

    NpcTalk(
        0xB,
        "Woman's Voice",
        "#2200248VWell, well, well. Who do we have here?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_41E3():
        OP_95(0xFE, 0, 0, -22600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_41E3)
    Sleep(1000)
    OP_68(0, 1000, -24000, 3000)

    def lambda_4211():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4211)
    Sleep(50)

    def lambda_4221():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4221)
    Sleep(50)

    def lambda_4231():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4231)
    Sleep(50)

    def lambda_4241():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4241)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 3)), scpexpr(EXPR_END)), "loc_43AF")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xB,
        "#2200249VWe meet again, my friends!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        "#2200255V#12P#0005FOh, you're here, too, Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2200251V#2105F#5PWhat'cha guys up to? Police business?\x02\x03",
            "#2200263V#2102FDo I detect hints of another sensational\x01",
            "investigation blossoming?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486A")

    label("loc_43AF")

    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xB,
        (
            "#2200252VIt feels like it's been forever\x01",
            "since we last met.\x02\x03",
            "#2200253VThe news about last month's\x01",
            "incidents with those monsters\x01",
            "left me speechless!\x02\x03",
            "#2200254VDon't you worry, my friends. I know\x01",
            "you've been busting your humps!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        "#2200250V#12P#0005FGrace, please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200256V#0100FNow that you mention it, you didn't write\x01",
            "that article, did you, Grace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2200257V#2106F#5PCorrect. Alas, I was away from Crossbell,\x01",
            "covering a different event that needed\x01",
            "the Grace touch.\x02\x03",
            "#2200258V#2102FTo be honest, I was hoping I could be the\x01",
            "SSS's sole reporter. I like writing articles\x01",
            "about you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200259V#12P#0206FOur hypothesis was accurate, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200260V#0302FWell, gettin' dunked on all the time by your\x01",
            "articles can wear you down, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2200261V#2104F#5PIt's like you can't understand the immense\x01",
            "love I harbor for the SSS. I'm like a mama\x01",
            "bird watching her chicks grow up!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#2200262V#2105F#5PWell, putting that aside for just a sec...\x01",
            "You DO have business here, right?\x02\x03",
            "#2200263V#2102FDo I detect hints of another sensational\x01",
            "investigation blossoming?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486A")


    ChrTalk(
        0x101,
        "#2200264V#12P#0012FN-No, not at all. It's just your imagination.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200265V#0100FWe're just here to ask a few questions,\x01",
            "that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2200266V#2101F#5PWell, if you say so.\x02\x03",
            "#2200267V#2104FI'm actually pretty busy myself, so\x01",
            "I'll leave you guys alone...for now.\x02\x03",
            "#2200268V#2110FI'll catch up with my besties later!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49B7():

        label("loc_49B7")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_49B7")

    QueueWorkItem2(0x101, 2, lambda_49B7)

    def lambda_49C9():

        label("loc_49C9")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_49C9")

    QueueWorkItem2(0x102, 2, lambda_49C9)

    def lambda_49DB():
        OP_95(0xFE, 1900, 0, -24200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_49DB)
    Sleep(500)

    def lambda_49F8():

        label("loc_49F8")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_49F8")

    QueueWorkItem2(0x104, 2, lambda_49F8)

    def lambda_4A0A():

        label("loc_4A0A")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_4A0A")

    QueueWorkItem2(0x103, 2, lambda_4A0A)
    WaitChrThread(0xB, 1)
    OP_68(0, 1000, -27000, 3000)

    def lambda_4A31():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD120, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4A31)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)
    EndChrThread(0x104, 0x2)

    def lambda_4A55():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4A55)
    Sleep(50)
    EndChrThread(0x102, 0x2)

    def lambda_4A69():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4A69)
    EndChrThread(0x103, 0x2)

    def lambda_4A7A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4A7A)
    Sleep(50)
    EndChrThread(0x101, 0x2)

    def lambda_4A8E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A8E)
    WaitChrThread(0x101, 2)
    ClearChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_68(0, 1000, -25800, 1000)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#2200269V#0306F#5P*sigh* That foxy lady's always marchin'\x01",
            "to the beat of her own drum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200270V#6P#0200FShe did not hound us as much as she usually\x01",
            "does, however.\x02\x03",
            "#2200271VDo you think she is busy with something else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200272V#5P#0100FI would assume so. She has a lot of ground\x01",
            "to cover with the Anniversary Festival on\x01",
            "the horizon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200273V#5P#0006FIt'd be nice if she'd refrain from\x01",
            "writing another article on us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#2200274V#6P#0000FWell, whatever... I think we've wasted\x01",
            "enough time here already.\x02\x03",
            "#2200275VLet's see if we can get ourselves an\x01",
            "appointment with the CEO.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D24():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D24)
    Sleep(50)

    def lambda_4D34():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4D34)
    Sleep(50)

    def lambda_4D44():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4D44)
    Sleep(150)

    ChrTalk(
        0x102,
        "#2200276V#11P#0102FOkay.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(0, 2500, -24000, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, 0, 0, -24000, 0)
    SetChrPos(0x1, 0, 0, -24000, 0)
    SetChrPos(0x2, 0, 0, -24000, 0)
    SetChrPos(0x3, 0, 0, -24000, 0)
    SetScenarioFlags(0x82, 1)
    OP_29(0x43, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_8_2871 end

    def Function_9_4E01(): pass

    label("Function_9_4E01")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, 10800, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29500, 0)
    SetChrPos(0x101, 0, 400, 8500, 180)
    SetChrPos(0x102, 700, 400, 8500, 180)
    SetChrPos(0x103, -700, 400, 8500, 180)
    SetChrPos(0x104, 0, 400, 8500, 180)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_68(0, 1100, 1800, 4000)
    MoveCamera(0, 25, 0, 4000)
    SetCameraDistance(19500, 4000)

    def lambda_4F04():
        OP_96(0xFE, 0x0, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F04)

    def lambda_4F1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4F1E)
    Sleep(500)

    def lambda_4F32():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F32)

    def lambda_4F4C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4F4C)
    Sleep(400)

    def lambda_4F60():
        OP_96(0xFE, 0x384, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F60)

    def lambda_4F7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4F7A)
    Sleep(500)

    def lambda_4F8E():
        OP_96(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F8E)

    def lambda_4FA8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4FA8)
    Sleep(1500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x104, 1)

    def lambda_4FDB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4FDB)
    WaitChrThread(0x103, 1)

    def lambda_4FEC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4FEC)
    WaitChrThread(0x102, 1)

    def lambda_4FFD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4FFD)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#2200788V#5P#0006F*sigh*...\x02\x03",
            "#2200789VI'm glad we finally have a lead, but\x01",
            "wow, I'm exhausted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200790V#6P#0309FNo kiddin'.\x02\x03",
            "#2200791V#0302FCan't imagine that confrontation\x01",
            "helped much, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200792V#5P#0001FI wonder whose fault that was, exactly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200793V#0202FI have to say, it is rare to see someone\x01",
            "not specialized in orbal technology reach\x01",
            "her level of proficiency.\x02\x03",
            "#2200794VMariabell is not an engineer, is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200795V#0104FShe certainly has experience from her studies,\x01",
            "but no. She specializes in business management.\x02\x03",
            "#2200796V#0100FAs her father's right-hand, I've heard she's tasked\x01",
            "with managing several of his projects.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#2200797V#5P#0000FWow, that's incredible...\x02\x03",
            "#2200798V#0005FSo, is that what she wanted to hire you\x01",
            "for, Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200799V#0106FY-Yes... I do appreciate her offer, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200800V#6P#0306FHow about how gung ho her old man\x01",
            "got on us?\x02\x03",
            "#2200801V#0301FDon't think I've ever heard a speech that\x01",
            "intense in person before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200802V#0203FI must say, it was quite interesting.\x02\x03",
            "#2200803V#0201FI had never considered that seeking justice\x01",
            "was one of mankind's driving forces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200804V#0104FHe's been teaching me various life lessons\x01",
            "through stories ever since I was little.\x02\x03",
            "#2200805V#0100FToday's has given me even more to think\x01",
            "about when it comes to our duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200806V#5P#0003FYeah, same here.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#2200807V#0000F#5PAnyway, we've got a good lead to go off of.\x02\x03",
            "#2200808VLet's go get the Geofront key from\x01",
            "the receptionist at City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200809V#0102FLead the way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200810V#6P#0302FAll you, man.\x02",
    )

    CloseMessageWindow()

    def lambda_567D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_567D)
    Sleep(100)

    def lambda_568D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_568D)
    Sleep(50)

    def lambda_569D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_569D)
    WaitChrThread(0x104, 2)
    OP_68(0, 1100, -4200, 3000)

    def lambda_56BF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_56BF)
    Sleep(150)
    WaitChrThread(0x103, 2)

    def lambda_56E0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_56E0)
    Sleep(150)
    WaitChrThread(0x102, 2)

    def lambda_5701():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5701)
    Sleep(150)

    def lambda_571E():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_571E)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_6F(0x1)
    OP_93(0x101, 0x0, 0x12C)
    Fade(500)
    OP_68(0, 1100, -2200, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 2200, -2200, 1500)
    MoveCamera(0, 0, 0, 1500)
    OP_6F(0x41)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#2200811V#0001F#6P#N...\x02\x03",
            "#2200812V#0003F(Justice...)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x190)

    def lambda_5809():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5809)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x101, 0x1)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 2500, -10000, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, 0, 0, -10000, 180)
    SetChrPos(0x1, 0, 0, -10000, 180)
    SetChrPos(0x2, 0, 0, -10000, 180)
    SetChrPos(0x3, 0, 0, -10000, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetScenarioFlags(0x83, 1)
    Sleep(10)
    PlayBGM("ed7102", 0)
    EventEnd(0x5)
    Return()

    # Function_9_4E01 end

    def Function_10_58F4(): pass

    label("Function_10_58F4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "                              IBC\x01",
            "          International Bank of Crossbell\x01\x01",
            "Companies wishing to inquire about business\x01",
            "matters should consult with the receptionist\x01",
            "on the first floor lobby.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_58F4 end

    SaveToFile()

Try(main)
