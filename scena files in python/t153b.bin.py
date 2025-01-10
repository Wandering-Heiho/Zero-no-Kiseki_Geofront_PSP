from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t153b.bin",                # FileName
        "t153b",                    # MapName
        "t153b",                    # Location
        0x004F,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 79, 0, 1, 0, 2],
    )

    BuildStringList((
        "t153b",                  # 0
        "Mafioso",                # 1
        "Mafioso",                # 2
        "Receptionist Sera",      # 3
        "Chief Clark",            # 4
        "Doctor Duster (unused)", # 5
        "Medical Intern Lisl (unused)",# 6
        "Medical Intern Chaleur", # 7
        "Medical Intern Flora",   # 8
        "bt154b",                 # 9
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 5, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_B4", 11, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_E4", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt154b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", "ms67101.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50362.itc",                   # 00
        "apl/ch50363.itc",                   # 01
        "chr/ch28202.itc",                   # 02
        "chr/ch28000.itc",                   # 03
        "chr/ch29302.itc",                   # 04
        "chr/ch29400.itc",                   # 05
        "chr/ch32800.itc",                   # 06
        "chr/ch29502.itc",                   # 07
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(48319,   150,     52389,   90,   341,  0x0, 0,   2,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(53840,   0,       52029,   135,  261,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(50979,   150,     59069,   300,  469,  0x0, 0,   4,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(48700,   0,       59700,   90,   389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(48700,   0,       59700,   90,   261,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59159,   400,     55750,   0,    341,  0x0, 0,   7,   0,   255, 255, 0,   9,   255,  0)

    DeclActor(58800,   0,       5460,    1200,    58800,   1500,    5460,    0x007C, 0,  14, 0x0000)

    ScpFunction((
        "Function_0_2E0",          # 00, 0
        "Function_1_398",          # 01, 1
        "Function_2_3ED",          # 02, 2
        "Function_3_405",          # 03, 3
        "Function_4_436",          # 04, 4
        "Function_5_59D",          # 05, 5
        "Function_6_7D2",          # 06, 6
        "Function_7_B1B",          # 07, 7
        "Function_8_D00",          # 08, 8
        "Function_9_EF4",          # 09, 9
        "Function_10_10E8",        # 0A, 10
        "Function_11_1553",        # 0B, 11
        "Function_12_186A",        # 0C, 12
        "Function_13_18E5",        # 0D, 13
        "Function_14_1F08",        # 0E, 14
    ))


    def Function_0_2E0(): pass

    label("Function_0_2E0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_320"),
        (1, "loc_32C"),
        (2, "loc_338"),
        (3, "loc_344"),
        (4, "loc_350"),
        (5, "loc_35C"),
        (6, "loc_368"),
        (SWITCH_DEFAULT, "loc_374"),
    )


    label("loc_320")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_380")

    label("loc_32C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_380")

    label("loc_338")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_380")

    label("loc_344")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_380")

    label("loc_350")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_380")

    label("loc_35C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_380")

    label("loc_368")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_380")

    label("loc_374")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_380")

    label("loc_380")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_397")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_380")

    label("loc_397")

    Return()

    # Function_0_2E0 end

    def Function_1_398(): pass

    label("Function_1_398")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B7")
    Event(0, 13)
    Jump("loc_3EC")

    label("loc_3B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D6")
    Event(0, 11)
    Jump("loc_3EC")

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EC")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_3EC")

    Return()

    # Function_1_398 end

    def Function_2_3ED(): pass

    label("Function_2_3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FE")
    Call(0, 12)

    label("loc_3FE")

    ClearMapObjFlags(0x0, 0x10)
    Return()

    # Function_2_3ED end

    def Function_3_405(): pass

    label("Function_3_405")

    TalkBegin(0xFE)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The mafioso is unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_3_405 end

    def Function_4_436(): pass

    label("Function_4_436")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CA")
    Jump("loc_514")

    label("loc_4CA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_514")

    label("loc_4EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_514")

    label("loc_50A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_514")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "There's still a lot of employees\x01",
            "and patients hiding upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, save them!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_436 end

    def Function_5_59D(): pass

    label("Function_5_59D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FC")

    ChrTalk(
        0xFE,
        (
            "I finally felt at ease once that massive\x01",
            "fence was installed after the whole\x01",
            "monster attack fiasco.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who the heck could have guessed that\x01",
            "the mafia would flat out attack us...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've received funding from all over Zemuria!\x01",
            "If this situation isn't handled delicately, we'll\x01",
            "have an international crisis on our hands!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7CE")

    label("loc_6FC")


    ChrTalk(
        0xFE,
        (
            "I always assumed the mafia were under more\x01",
            "organized leadership, but apparently not...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering the circumstances, we'll have\x01",
            "an international crisis on our hands if this\x01",
            "isn't handled delicately!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CE")

    TalkEnd(0xFE)
    Return()

    # Function_5_59D end

    def Function_6_7D2(): pass

    label("Function_6_7D2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_866")
    Jump("loc_8B0")

    label("loc_866")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_886")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B0")

    label("loc_886")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B0")

    label("loc_8A6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1C")

    ChrTalk(
        0xFE,
        (
            "O-Oh, Aidios. I was scheduled to perform\x01",
            "an examination on one of the patients this\x01",
            "evening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Under this amount of stress, it's not an\x01",
            "impossibility that his body will go into a\x01",
            "seizure... What should I do?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I need to calm down. All of us doctors\x01",
            "need to if we want to make it through this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B13")

    label("loc_A1C")


    ChrTalk(
        0xFE,
        (
            "I just remembered that I had an appointment\x01",
            "scheduled today with a patient who came in after a\x01",
            "small seizure. I pray that his condition doesn't worsen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I'll pray to Aidios that this turmoil\x01",
            "doesn't cause his seizures to worsen...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B13")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_7D2 end

    def Function_7_B1B(): pass

    label("Function_7_B1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1F")

    ChrTalk(
        0xFE,
        (
            "Despite being in such an insane situation,\x01",
            "I've managed to stay relatively calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe studying under Doctor Belldine has\x01",
            "paid off. After all, he's as level-headed as\x01",
            "you can get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I sure hope the doctor is all right, too...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CFC")

    label("loc_C1F")


    ChrTalk(
        0xFE,
        (
            "Taking the time of day into account, the\x01",
            "possibility of the outpatients getting involved\x01",
            "in this is...quite high, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There were gunshots fired. I'm sure of it.\x01",
            "Hopefully, everyone at the dorms is safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFC")

    TalkEnd(0xFE)
    Return()

    # Function_7_B1B end

    def Function_8_D00(): pass

    label("Function_8_D00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E39")

    ChrTalk(
        0xFE,
        (
            "Those morons! St. Ursula is conducting\x01",
            "crucial research for the medical field!\x01",
            "What are they thinking?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And first of all, this is a hospital! This is no\x01",
            "place for weapons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they somehow destroyed our research\x01",
            "equipment, it would be a massive loss for\x01",
            "the future of medicine!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_EF0")

    label("loc_E39")


    ChrTalk(
        0xFE,
        (
            "No matter how long I think about it, I just\x01",
            "can't pinpoint what their objective is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I can do is pray to Aidios that none of\x01",
            "our equipment is destroyed in this fiasco...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF0")

    TalkEnd(0xFE)
    Return()

    # Function_8_D00 end

    def Function_9_EF4(): pass

    label("Function_9_EF4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F88")
    Jump("loc_FD2")

    label("loc_F88")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FA8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD2")

    label("loc_FA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FC8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD2")

    label("loc_FC8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1087")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "Calm down, Flora. Deep breaths.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-If you let something like this bother you,\x01",
            "how will you ever become a doctor?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_10E0")

    label("loc_1087")


    ChrTalk(
        0xFE,
        "You have to stay calm, Flora.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sorry, but could you leave me\x01",
            "alone for now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_EF4 end

    def Function_10_10E8(): pass

    label("Function_10_10E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17480, 600, -4610, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22180, 0)
    SetChrPos(0x101, -600, 0, 600, 90)
    SetChrPos(0x102, -600, 0, -600, 90)
    SetChrPos(0x103, -1900, 0, -600, 90)
    SetChrPos(0x104, -1900, 0, 600, 90)
    SetChrPos(0x106, -3200, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(12880, 600, 6580, 7000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(4870, 2400, -280, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19020, 0)
    OP_68(4870, 900, -280, 3000)
    Sleep(1000)

    def lambda_1221():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1221)
    Sleep(50)

    def lambda_1239():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1239)
    Sleep(50)

    def lambda_1251():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1251)
    Sleep(50)

    def lambda_1269():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1269)
    Sleep(50)

    def lambda_1281():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1281)
    Sleep(200)

    def lambda_1299():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1299)
    Sleep(50)

    def lambda_12AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12AD)
    Sleep(500)

    def lambda_12C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12C1)
    Sleep(50)

    def lambda_12D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12D5)
    Sleep(500)

    def lambda_12E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_12E9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#5100520V#0001F#5PNo staff or patients...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100521V#0108F#6PNot a trace of the mafia, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100522V\x07\x03",
            "#0700F#6PThat's not true. I can sense them\x01",
            "moving about...\x02\x03",
            "#5100523VThe hospital staff are likely taking\x01",
            "shelter throughout the entire building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100524V#0203F#6PAgreed. I am detecting the presence\x01",
            "of multiple people in here.\x02\x03",
            "#5100525V#0201FNot just the staff, but the mafia as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100526V#0301F#5PGuess it's time for the main event.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100527V#0013F#5PAll right, everyone. Stay alert!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 3190, 0, -210, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE1, 4)
    EventEnd(0x5)
    Return()

    # Function_10_10E8 end

    def Function_11_1553(): pass

    label("Function_11_1553")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch31000.itc", 0x23)
    LoadChrToIndex("chr/ch31050.itc", 0x24)
    LoadChrToIndex("chr/ch31051.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31150.itc", 0x27)
    LoadChrToIndex("chr/ch31151.itc", 0x28)
    OP_68(47500, 1000, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 47400, 0, 600, 90)
    SetChrPos(0x102, 47400, 0, -600, 90)
    SetChrPos(0x103, 46100, 0, -600, 90)
    SetChrPos(0x104, 46100, 0, 600, 90)
    SetChrPos(0x106, 44800, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 55000, 0, 580, 270)
    SetChrPos(0x9, 54750, 0, -800, 270)
    FadeToBright(1000, 0)
    OP_68(49500, 1000, 0, 1200)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#5100528V#0105F#6PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100529V#0013F#6PAn ambush!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(48500, 1000, 0, 1000)
    SetCameraDistance(17500, 1000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)

    def lambda_1783():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1783)

    def lambda_1798():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1798)
    Sleep(300)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sleep(100)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Call(0, 12)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x0, 51690, 0, -10, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE1, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_1553 end

    def Function_12_186A(): pass

    label("Function_12_186A")

    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x8, 54860, 0, 580, 315)
    SetChrPos(0x9, 55500, 0, -1070, 225)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_12_186A end

    def Function_13_18E5(): pass

    label("Function_13_18E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28200.itc", 0x1E)
    LoadChrToIndex("chr/ch29300.itc", 0x1F)
    LoadChrToIndex("chr/ch29500.itc", 0x20)
    OP_68(54490, 1000, 57780, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 49490, 0, 49500, 0)
    SetChrPos(0x102, 50490, 0, 49500, 0)
    SetChrPos(0x103, 49490, 0, 48300, 0)
    SetChrPos(0x104, 50490, 0, 48300, 0)
    SetChrPos(0x106, 49990, 0, 47100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xA, 54390, 0, 55860, 180)
    SetChrPos(0xE, 54520, 0, 54400, 0)
    SetChrPos(0xF, 58520, 0, 57440, 90)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xF, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(51800, 1000, 55090, 3000)
    Sleep(500)

    def lambda_1A41():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A41)
    Sleep(50)

    def lambda_1A59():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A59)
    Sleep(50)

    def lambda_1A71():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A71)
    Sleep(50)

    def lambda_1A89():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A89)
    Sleep(50)

    def lambda_1AA1():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1AA1)
    Sleep(200)

    def lambda_1AB9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AB9)
    Sleep(50)

    def lambda_1ACD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1ACD)
    Sleep(500)

    def lambda_1AE1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1AE1)
    Sleep(50)

    def lambda_1AF5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1AF5)
    Sleep(500)

    def lambda_1B09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1B09)
    WaitChrThread(0x101, 1)

    def lambda_1B1E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B1E)
    WaitChrThread(0x102, 1)

    def lambda_1B2F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B2F)
    WaitChrThread(0x103, 1)

    def lambda_1B40():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B40)
    WaitChrThread(0x104, 1)

    def lambda_1B51():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B51)
    WaitChrThread(0x106, 1)

    def lambda_1B62():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1B62)
    EndChrThread(0xA, 0xFF)
    SetChrSubChip(0xA, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)
    EndChrThread(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1BF3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BF3)
    Sleep(50)

    def lambda_1C03():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C03)
    Sleep(50)

    def lambda_1C13():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C13)
    Sleep(50)

    def lambda_1C23():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C23)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)

    ChrTalk(
        0xA,
        "#5100530V#5PLloyd?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100531V#0002F#6PThank goodness you're safe, Sera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5100532V#11PY-You're the police...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5100533V#5PYou must have come to rescue us, right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100534V#0300F#6PYep. Right now, we're checkin' on everyone\x01",
            "while takin' out the baddies we come across.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100535V#0201F#6P#NIt is still dangerous, so please wait here for\x01",
            "a little while longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xA,
        "#5100536V#5PW-We understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5100537V#5PThere's still a lot of employees\x01",
            "and patients upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5100538V#5PPlease, save them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100539V#6P#0001FLeave it to us!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 50090, 0, 51200, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xA, 48320, 150, 52390, 90)
    SetChrPos(0xF, 59160, 400, 55750, 0)
    OP_93(0xB, 0x87, 0x0)
    SetChrPos(0xE, 48700, 0, 59700, 90)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetScenarioFlags(0xE1, 6)
    OP_29(0x4D, 0x1, 0x7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_18E5 end

    def Function_14_1F08(): pass

    label("Function_14_1F08")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Orbal power is offline.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_1F08 end

    SaveToFile()

Try(main)
