from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c103c.bin",                # FileName
        "c103c",                    # MapName
        "c103c",                    # Location
        0x0012,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 18, 0, 3, 0, 4],
    )

    BuildStringList((
        "c103c",                  # 0
        "Zhang Hui",              # 1
        "Finn",                   # 2
        "Shanshan",               # 3
        "Gryd",                   # 4
        "Puck",                   # 5
        "Roose",                  # 6
        "Tourist",                # 7
        "Bracer Scott",           # 8
        "Bracer Wenzel",          # 9
        "Bracer Lynn",            # 10
        "Kilika",                 # 11
    ))

    AddCharChip((
        "chr/ch31600.itc",                   # 00
        "chr/ch25100.itc",                   # 01
        "chr/ch32500.itc",                   # 02
        "chr/ch26302.itc",                   # 03
        "chr/ch20402.itc",                   # 04
        "chr/ch21202.itc",                   # 05
        "chr/ch24202.itc",                   # 06
        "chr/ch27202.itc",                   # 07
        "chr/ch27302.itc",                   # 08
        "chr/ch32002.itc",                   # 09
        "chr/ch07302.itc",                   # 0A
    ))

    DeclNpc(16000,   0,       15989,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(16030,   0,       6050,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(12310,   0,       -1990,   225,  261,  0x0, 0,   2,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(7130,    150,     -1480,   180,  261,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(10689,   150,     3170,    270,  261,  0x0, 0,   4,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(7300,    150,     3230,    90,   261,  0x0, 0,   5,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(13949,   150,     2900,    90,   261,  0x0, 0,   6,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(3220,    150,     5539,    0,    389,  0x0, 0,   7,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(3130,    150,     8930,    180,  389,  0x0, 0,   8,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(1440,    150,     7170,    90,   389,  0x0, 0,   9,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(4989,    150,     7179,    270,  389,  0x0, 0,   10,  0,   255, 255, 0,   18,  255,  0)

    DeclActor(14590,   0,       4630,    1000,    16030,   1500,    6050,    0x007E, 0,  5,  0x0000)

    ScpFunction((
        "Function_0_264",          # 00, 0
        "Function_1_31C",          # 01, 1
        "Function_2_470",          # 02, 2
        "Function_3_49B",          # 03, 3
        "Function_4_57B",          # 04, 4
        "Function_5_5CC",          # 05, 5
        "Function_6_61D",          # 06, 6
        "Function_7_714",          # 07, 7
        "Function_8_CC9",          # 08, 8
        "Function_9_DC0",          # 09, 9
        "Function_10_1494",        # 0A, 10
        "Function_11_1954",        # 0B, 11
        "Function_12_202C",        # 0C, 12
        "Function_13_2477",        # 0D, 13
        "Function_14_293F",        # 0E, 14
        "Function_15_2D71",        # 0F, 15
        "Function_16_2FB3",        # 10, 16
        "Function_17_314F",        # 11, 17
        "Function_18_361C",        # 12, 18
    ))


    def Function_0_264(): pass

    label("Function_0_264")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2A4"),
        (1, "loc_2B0"),
        (2, "loc_2BC"),
        (3, "loc_2C8"),
        (4, "loc_2D4"),
        (5, "loc_2E0"),
        (6, "loc_2EC"),
        (SWITCH_DEFAULT, "loc_2F8"),
    )


    label("loc_2A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_31B")

    Return()

    # Function_0_264 end

    def Function_1_31C(): pass

    label("Function_1_31C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46F")
    OP_95(0xFE, 7200, 0, 370, 1000, 0x0)
    OP_95(0xFE, 7280, 30, 1390, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_95(0xFE, 5850, 0, 1930, 1000, 0x0)
    OP_95(0xFE, 4730, 0, 3700, 1000, 0x0)
    OP_95(0xFE, 4840, 0, 5570, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, 5660, 0, 5540, 1000, 0x0)
    OP_95(0xFE, 10470, 0, 10350, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1200)
    OP_95(0xFE, 12980, 0, 7230, 1000, 0x0)
    OP_95(0xFE, 12730, 0, 2100, 1000, 0x0)
    OP_95(0xFE, 13200, 0, 1420, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1600)
    OP_95(0xFE, 12280, 0, 680, 1000, 0x0)
    OP_95(0xFE, 11230, 0, 110, 1000, 0x0)
    OP_95(0xFE, 8930, 30, -1570, 1000, 0x0)
    Sleep(1400)
    OP_95(0xFE, 8720, 0, -510, 1000, 0x0)
    Jump("Function_1_31C")

    label("loc_46F")

    Return()

    # Function_1_31C end

    def Function_2_470(): pass

    label("Function_2_470")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49A")
    OP_94(0xFE, 0xFFFF408E, 0xFFFF30F8, 0xFFFF3724, 0xFFFF236A, 0x3E8)
    Sleep(300)
    Jump("Function_2_470")

    label("loc_49A")

    Return()

    # Function_2_470 end

    def Function_3_49B(): pass

    label("Function_3_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4B3")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_57A")

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_50A")
    SetChrPos(0x8, 16030, 0, 6050, 270)
    SetChrPos(0x9, 12310, 0, -1990, 225)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, -49600, 30, -55300, 135)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_57A")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_557")
    SetChrPos(0x8, 16030, 0, 6050, 270)
    SetChrPos(0x9, 12310, 0, -1990, 225)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, -53960, 0, -55210, 180)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_57A")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_571")
    OP_93(0x8, 0xB4, 0x0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_57A")

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_57A")

    label("loc_57A")

    Return()

    # Function_3_49B end

    def Function_4_57B(): pass

    label("Function_4_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_58C")
    SetScenarioFlags(0x1, 0)
    Jump("loc_5CB")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_59D")
    SetScenarioFlags(0x0, 7)
    Jump("loc_5CB")

    label("loc_59D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5AE")
    SetScenarioFlags(0x0, 7)
    Jump("loc_5CB")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5BF")
    SetScenarioFlags(0x1, 0)
    Jump("loc_5CB")

    label("loc_5BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5CB")
    SetScenarioFlags(0x1, 0)

    label("loc_5CB")

    Return()

    # Function_4_57B end

    def Function_5_5CC(): pass

    label("Function_5_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5DD")
    Call(0, 8)
    Jump("loc_61C")

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5EE")
    Call(0, 6)
    Jump("loc_61C")

    label("loc_5EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5FF")
    Call(0, 6)
    Jump("loc_61C")

    label("loc_5FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_610")
    Call(0, 8)
    Jump("loc_61C")

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_61C")
    Call(0, 8)

    label("loc_61C")

    Return()

    # Function_5_5CC end

    def Function_6_61D(): pass

    label("Function_6_61D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_70D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_633")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_708")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Rest\x01",       # 2
            "Leave\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_693")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_693")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B3")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_703")

    label("loc_6B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D3")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_703")

    label("loc_6D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E7")
    Jump("loc_703")

    label("loc_6E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_703")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_703")

    Jump("loc_633")

    label("loc_708")

    Jump("loc_710")

    label("loc_70D")

    Call(0, 7)

    label("loc_710")

    TalkEnd(0x8)
    Return()

    # Function_6_61D end

    def Function_7_714(): pass

    label("Function_7_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79F")

    ChrTalk(
        0x8,
        "Order up! Two fried rice specials!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Pretty busy day today, so far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "We'll make it through, though.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_822")

    label("loc_79F")


    ChrTalk(
        0x8,
        (
            "This big a crowd will only last for today.\x01",
            "Tomorrow on, it'll just be our regulars again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I think we'll make it through.\x02",
    )

    CloseMessageWindow()

    label("loc_822")

    Jump("loc_CC8")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_932")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AC")

    ChrTalk(
        0x8,
        "Customers! What'll you be having today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm? Hmmmm? You there!\x01",
            "You're eating something, right?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_92D")

    label("loc_8AC")


    ChrTalk(
        0x8,
        (
            "If you plan to check into the inn, that\x01",
            "doesn't begin until 5PM!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The rooms are off limits until then,\x01",
            "am I understood?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92D")

    Jump("loc_CC8")

    label("loc_932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_999")

    ChrTalk(
        0x8,
        "Are you here to eat some grub?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm? You're here for food, right?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A32")

    label("loc_999")


    ChrTalk(
        0x8,
        "I made Shanshan go clean the guest rooms for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm worried about all of these men gawking at my\x01",
            "daughter. I might have to strangle someone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A32")

    Jump("loc_CC8")

    label("loc_A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B02")
    TurnDirection(0x8, 0xE, 300)

    ChrTalk(
        0x8,
        (
            "That man over there bothers me. I can see his\x01",
            "lustful gaze towards Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "(*murderous stare*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "W-Weird... I just felt a chill run\x01",
            "down my spine...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_B7F")

    label("loc_B02")


    ChrTalk(
        0x8,
        (
            "I will slay that beast the moment he tries to\x01",
            "lay a single finger on Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "He'd better watch himself, or else.\x02",
    )

    CloseMessageWindow()

    label("loc_B7F")

    Jump("loc_CC8")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C46")
    OP_63(0x8, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x8,
        "The Anniversary Festival is always too noisy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I prefer a more quiet and relaxing restaurant.\x01",
            "Sometimes I wish we weren't so busy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CC8")

    label("loc_C46")


    ChrTalk(
        0x8,
        (
            "This noisy atmosphere reminds me of my\x01",
            "time back in the Eastern Quarter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The Eastern Quarter was always like this, too.\x02",
    )

    CloseMessageWindow()

    label("loc_CC8")

    Return()

    # Function_7_714 end

    def Function_8_CC9(): pass

    label("Function_8_CC9")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_DB9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Rest\x01",       # 2
            "Leave\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D3F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_D3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5F")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DAF")

    label("loc_D5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7F")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DAF")

    label("loc_D7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D93")
    Jump("loc_DAF")

    label("loc_D93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_DAF")

    Jump("loc_CDF")

    label("loc_DB4")

    Jump("loc_DBC")

    label("loc_DB9")

    Call(0, 9)

    label("loc_DBC")

    TalkEnd(0x9)
    Return()

    # Function_8_CC9 end

    def Function_9_DC0(): pass

    label("Function_9_DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF6")

    ChrTalk(
        0x9,
        "Man, this year's super busy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Considering it was Shanshan's first time working\x01",
            "during the Anniversary Festival, she did really well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "And because of her, our revenue has doubled. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I noticed that Master looked pretty uncomfortable\x01",
            "through the whole thing, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F8F")

    label("loc_EF6")


    ChrTalk(
        0x9,
        (
            "Shanshan started helping out with the restaurant\x01",
            "earlier this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Watching Master freak out like that\x01",
            "was pretty entertaining, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8F")

    Jump("loc_1493")

    label("loc_F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1093")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFB")

    ChrTalk(
        0x9,
        "You there! Have a seat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "No loitering allowed in here, I'm afraid.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_108E")

    label("loc_FFB")


    ChrTalk(
        0x9,
        (
            "We've got our hands full, but if you want some food,\x01",
            "just let the master know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't get intimidated by his scary mug, though!\x01",
            "Hahahaha!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108E")

    Jump("loc_1493")

    label("loc_1093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_11CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1136")

    ChrTalk(
        0x9,
        (
            "Hey there, police officers. We appreciate\x01",
            "all the hard work that you do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You feelin' hungry? Boy, today's\x01",
            "been insanely busy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11C8")

    label("loc_1136")


    ChrTalk(
        0x9,
        "Man, Master's been on edge ever since yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Makes sense, I guess. His daughter's super cute,\x01",
            "so she attracts a bunch of attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C8")

    Jump("loc_1493")

    label("loc_11CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_133D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1289")

    ChrTalk(
        0x9,
        (
            "There was some kinda commotion coming\x01",
            "from the Downtown District yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Man, what the heck happened there?\x01",
            "It was annoying our customers real bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1338")

    label("loc_1289")


    ChrTalk(
        0x9,
        (
            "There was some kinda commotion coming\x01",
            "from the Downtown District yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Our customers were all raving about something\x01",
            "happening, but I never caught what it was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1338")

    Jump("loc_1493")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1493")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D9")

    ChrTalk(
        0x9,
        "40,000, 50,000, 60,000 mira...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hahaha! What a profitable day we're having!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Praise be to the Anniversary Festival!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1493")

    label("loc_13D9")


    ChrTalk(
        0x9,
        (
            "Hey there. Welcome to our little bar and inn on\x01",
            "the outskirts of town!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We're the closest restaurant to the east exit,\x01",
            "and you'd better not forget it! Come here\x01",
            "any time, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1493")

    Return()

    # Function_9_DC0 end

    def Function_10_1494(): pass

    label("Function_10_1494")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1542")

    ChrTalk(
        0xFE,
        (
            "We've made it to the last day of the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Look at how eager all of our customers are.\x01",
            "I'm going to savor this until the very end!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1950")

    label("loc_1542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_164A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CB")

    ChrTalk(
        0xFE,
        "Daddy told me to clean the inn today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's his problem? It's not like it even\x01",
            "needs cleaning yet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1645")

    label("loc_15CB")


    ChrTalk(
        0xFE,
        (
            "Oh, well. Not like it's going to take\x01",
            "long to clean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I wanted to watch the parade.\x01",
            "Is it over already?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1645")

    Jump("loc_1950")

    label("loc_164A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_17DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1754")

    ChrTalk(
        0xFE,
        (
            "Oh, I bet Rixia's performing right this very second.\x01",
            "I hope she's doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure she'll get a standing ovation\x01",
            "from the audience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't let her outshine me so easily, so\x01",
            "I've got to try just as hard with my work! ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_17D7")

    label("loc_1754")


    ChrTalk(
        0xFE,
        "The entire inn was booked today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heehee. I'm going to make this place sparkle.\x01",
            "That should lead to some repeat business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D7")

    Jump("loc_1950")

    label("loc_17DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1885")

    ChrTalk(
        0xFE,
        (
            "Oh, Daddy... He went and scared another\x01",
            "customer away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can't just keep doing that... You have to\x01",
            "put on your best smile for the customers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1950")

    label("loc_1885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1900")

    ChrTalk(
        0xFE,
        "Ah, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew... All of these customers coming in\x01",
            "isn't making my job any easier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1950")

    label("loc_1900")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1200)

    ChrTalk(
        0xFE,
        (
            "Ugh... This crowd's a little too\x01",
            "overwhelming for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1950")

    TalkEnd(0xFE)
    Return()

    # Function_10_1494 end

    def Function_11_1954(): pass

    label("Function_11_1954")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19E8")
    Jump("loc_1A32")

    label("loc_19E8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A08")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A32")

    label("loc_1A08")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A28")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A32")

    label("loc_1A28")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A32")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2D")

    ChrTalk(
        0xFE,
        (
            "*chew, chew*...\x01",
            "Everybody's excited today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just like any other day, I'm headed\x01",
            "off to Calvard in a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Us guys in the transportation industry\x01",
            "don't get vacations, y'know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1B6F")

    label("loc_1B2D")


    ChrTalk(
        0xFE,
        (
            "*chew, chew*...\x01",
            "Gotta admit, I envy all these excited folks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6F")

    Jump("loc_2024")

    label("loc_1B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1C9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4D")

    ChrTalk(
        0xFE,
        (
            "Gimme a break. This crowd is going to make\x01",
            "driving the truck through Crossbell hell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even a small accident would hurt business,\x01",
            "so I'll just leave Crossbell via some side streets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C99")

    label("loc_1C4D")


    ChrTalk(
        0xFE,
        (
            "You're joking! Apparently, today's\x01",
            "deliveries are going to be delayed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C99")

    Jump("loc_2024")

    label("loc_1C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1E15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D89")

    ChrTalk(
        0xFE,
        "I heard something about a parade happening today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pretty sure our company loaned out\x01",
            "one of our drivers for it, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, our business only consists\x01",
            "of the most professional drivers!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E10")

    label("loc_1D89")


    ChrTalk(
        0xFE,
        (
            "We're so professional that the government\x01",
            "recognizes our skills by requesting our help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm even busier because of the fact.\x02",
    )

    CloseMessageWindow()

    label("loc_1E10")

    Jump("loc_2024")

    label("loc_1E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1EAC")

    ChrTalk(
        0xFE,
        "A bunch of tour buses are starting to arrive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's still a lot of tourists waiting to enter\x01",
            "Crossbell over at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2024")

    label("loc_1EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7D")

    ChrTalk(
        0xFE,
        (
            "The road out to Calvard is real congested,\x01",
            "all thanks to the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm kinda surprised... This the first time\x01",
            "a highway's ever been packed with\x01",
            "orbal cars?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2024")

    label("loc_1F7D")


    ChrTalk(
        0xFE,
        (
            "Much like orbal buses in Calvard, orbal cars\x01",
            "are becoming all the rage in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that Calvard's packed with buses\x01",
            "trying to get people out here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2024")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_1954 end

    def Function_12_202C(): pass

    label("Function_12_202C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20C0")
    Jump("loc_210A")

    label("loc_20C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20E0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_210A")

    label("loc_20E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2100")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_210A")

    label("loc_2100")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_210A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_21B3")

    ChrTalk(
        0xFE,
        "I decided to make amends with my buddy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh. Yeah, I do think I want to open a store\x01",
            "with Roose, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246F")

    label("loc_21B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_224D")

    ChrTalk(
        0xFE,
        "I can't believe how many tourists there are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Roose was right! There's no way a tourist-\x01",
            "aimed business in Crossbell could fail!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246F")

    label("loc_224D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2346")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B5")

    ChrTalk(
        0xFE,
        "Man, there are so many people here, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Okay, fine. I'll admit it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2341")

    label("loc_22B5")


    ChrTalk(
        0xFE,
        (
            "I've actually been fighting with a friend of mine\x01",
            "over this recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, I'll admit it. There's actually a ton\x01",
            "of people here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2341")

    Jump("loc_246F")

    label("loc_2346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_23D0")

    ChrTalk(
        0xFE,
        (
            "Man, my buddy keeps babbling on\x01",
            "about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though I already told him that\x01",
            "I don't wanna be a merchant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246F")

    label("loc_23D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_246F")
    SetChrSubChip(0xC, 0x0)

    ChrTalk(
        0xFE,
        (
            "*chew, chew*...\x01",
            "Hmph. Where I choose to have fun isn't\x01",
            "anybody else's business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't you dare interfere with my festival\x01",
            "plans, Roose!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_202C end

    def Function_13_2477(): pass

    label("Function_13_2477")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_250B")
    Jump("loc_2555")

    label("loc_250B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_252B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2555")

    label("loc_252B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_254B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2555")

    label("loc_254B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2555")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2673")

    ChrTalk(
        0xFE,
        "So, I decided to open a store with Puck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It won't be open in time for the festival, but\x01",
            "Crossbell's always got a ton of tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pretty confident this'll all work out.\x01",
            "That perfect store is just waiting to be made!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2937")

    label("loc_2673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_276C")

    ChrTalk(
        0xFE,
        (
            "I kind of subconsciously analyze\x01",
            "what the tourists are into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like, for instance, what kind of goods are\x01",
            "the most popular with them, and whatnot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I'm being honest with myself, I really\x01",
            "would like to become a merchant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2937")

    label("loc_276C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2810")

    ChrTalk(
        0xFE,
        (
            "Holy... I can't believe so many tourists\x01",
            "came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we take advantage of the sheer amount of\x01",
            "people, I'm sure we'll make a hefty profit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2937")

    label("loc_2810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28AB")
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xFE,
        (
            "Hey, Puck, check it out. There's a ton of\x01",
            "people outside.\x02",
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
            "If we opened up a shop, I'm sure\x01",
            "it'd become a big success.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2937")

    label("loc_28AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2937")
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xFE,
        (
            "*munch, crunch*...\x01",
            "Hey Puck, why are you\x01",
            "hanging around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Didn't you promise not to show\x01",
            "your face here anymore?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2937")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_2477 end

    def Function_14_293F(): pass

    label("Function_14_293F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29D3")
    Jump("loc_2A1D")

    label("loc_29D3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29F3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A1D")

    label("loc_29F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A13")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A1D")

    label("loc_2A13")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A1D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2AF6")

    ChrTalk(
        0xFE,
        "You gotta watch out for the owner here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I started chatting up the waitress, and he\x01",
            "walked over and smacked me with a ladle!\x01",
            "That was pretty friggin' scary!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D69")

    label("loc_2AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2B5F")

    ChrTalk(
        0xFE,
        "Huh? Where'd that waitress run off to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, what a bummer. She was super cute...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D69")

    label("loc_2B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2C28")

    ChrTalk(
        0xFE,
        (
            "People keep talking about some parade,\x01",
            "so I might as well go check it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, the owner of this place seems\x01",
            "kinda tyrannical... Hmm, it's probably\x01",
            "just my imagination.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D69")

    label("loc_2C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2CC7")

    ChrTalk(
        0xFE,
        (
            "Man, the food here really\x01",
            "is to die for, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That waitress is super cute, too.\x01",
            "Haha. I even lost track of time hanging out here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D69")

    label("loc_2CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2D69")

    ChrTalk(
        0xFE,
        (
            "Man, I'm beat. You can already see the\x01",
            "huge crowds outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you're probably aware, I'd advise against\x01",
            "visiting places without having a map.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D69")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_293F end

    def Function_15_2D71(): pass

    label("Function_15_2D71")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E05")
    Jump("loc_2E4F")

    label("loc_2E05")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E25")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E4F")

    label("loc_2E25")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E45")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E4F")

    label("loc_2E45")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E4F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F39")

    ChrTalk(
        0xFE,
        "Hey guys, you just get back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I actually just finished giving my\x01",
            "report on that request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope we can work together again soon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah, likewise.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2FAB")

    label("loc_2F39")


    ChrTalk(
        0xFE,
        (
            "Arios totally saved us when he rushed out\x01",
            "that one time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've still got a long way to go, to be honest.\x02",
    )

    CloseMessageWindow()

    label("loc_2FAB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_2D71 end

    def Function_16_2FB3(): pass

    label("Function_16_2FB3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3047")
    Jump("loc_3091")

    label("loc_3047")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3067")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3091")

    label("loc_3067")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3087")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3091")

    label("loc_3087")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3091")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3147")

    ChrTalk(
        0xFE,
        (
            "So, I heard you all worked with Scott\x01",
            "to complete a request, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, hopefully, it's a trend that\x01",
            "continues into the future!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3147")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_2FB3 end

    def Function_17_314F(): pass

    label("Function_17_314F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31E3")
    Jump("loc_322D")

    label("loc_31E3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3203")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322D")

    label("loc_3203")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3223")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322D")

    label("loc_3223")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_322D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3483")

    ChrTalk(
        0x12,
        (
            "#3400FIt's been quite some time, hasn't it, Lynn?\x01",
            "You've grown spectacularly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Well, of course. It's been about eight years!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I don't think I'll ever be able to forget the day\x01",
            "we had our fight. It's still clearly etched in\x01",
            "my mind to this day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3404FThat certainly was an experience,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Oh, I didn't know Kilika and Lynn\x01",
            "were acquainted. They seem close.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(You think Kilika's a practitioner of Taito?\x01",
            "I kinda had my suspicions that she was\x01",
            "more than she was lettin' on to be.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3614")

    label("loc_3483")


    ChrTalk(
        0x11,
        (
            "What? You're seriously not going to go\x01",
            "and greet those two?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "And just when you finally came to visit\x01",
            "Crossbell, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3403FI'm sorry, but I'll have to respectfully decline.\x01",
            "Don't forget that I've long retired from that role.\x02\x03",
            "#3400FBut regardless, please pass on my highest of regards\x01",
            "to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hmm, I see. It's a bit disappointing, but I'm\x01",
            "sure they'll be excited to hear from you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3614")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_314F end

    def Function_18_361C(): pass

    label("Function_18_361C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36B0")
    Jump("loc_36FA")

    label("loc_36B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36D0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36FA")

    label("loc_36D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36F0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36FA")

    label("loc_36F0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36FA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3919")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3742")
    Call(0, 17)
    Jump("loc_3919")

    label("loc_3742")


    ChrTalk(
        0x12,
        (
            "#3404FI've heard tales of your exploits, but one quick\x01",
            "glance is all I need to know that you've grown\x01",
            "into a fine bracer.\x02\x03",
            "#3400FI've also taken notice of the fact that your\x01",
            "enthusiastic mannerisms have not changed one\x01",
            "bit since we last met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Haha... Quit it, you're embarrassing me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Actually, Kilika... What have you been up to\x01",
            "these past eight years?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3404FWouldn't you like to know? Let's just say\x01",
            "that there hasn't been a dull moment in my life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3919")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_361C end

    SaveToFile()

Try(main)
