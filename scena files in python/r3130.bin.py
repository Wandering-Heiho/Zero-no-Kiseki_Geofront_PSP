from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r3130.bin",                # FileName
        "r3130",                    # MapName
        "r3130",                    # Location
        0x0066,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -6000, 0, -16500, 0, 0, 1, 102, 0, 0, 0, 1],
    )

    BuildStringList((
        "r3130",                  # 0
        "br0000",                 # 1
        "br000b",                 # 2
        "br1000",                 # 3
        "br0100",                 # 4
        "br1500",                 # 5
        "br1510",                 # 6
        "br1520",                 # 7
        "br2000",                 # 8
        "br2010",                 # 9
        "br2040",                 # 10
        "br2050",                 # 11
        "br2060",                 # 12
        "br206b",                 # 13
        "br2070",                 # 14
        "br3000",                 # 15
        "br300b",                 # 16
        "br3100",                 # 17
        "bm1000",                 # 18
        "bm1010",                 # 19
        "bm1020",                 # 20
        "bm1030",                 # 21
        "bm1040",                 # 22
        "bm2000",                 # 23
        "bm2020",                 # 24
        "bm2050",                 # 25
        "bm2099",                 # 26
        "bm3000",                 # 27
        "bm3010",                 # 28
        "bm3020",                 # 29
        "bm3030",                 # 30
        "bm3040",                 # 31
        "bm3050",                 # 32
        "bm3060",                 # 33
        "bm3070",                 # 34
        "bm3080",                 # 35
        "bm3081",                 # 36
        "bm3090",                 # 37
        "bc130b",                 # 38
        "bc1400",                 # 39
        "bc140b",                 # 40
        "bc1410",                 # 41
        "bc141b",                 # 42
        "bc1420",                 # 43
        "bc0510",                 # 44
        "bc0520",                 # 45
        "bc0530",                 # 46
        "bc0540",                 # 47
        "bc0550",                 # 48
        "bc1460",                 # 49
        "bc1470",                 # 50
        "bm0000",                 # 51
        "bm0001",                 # 52
        "bm0002",                 # 53
        "bm0010",                 # 54
        "bm0011",                 # 55
        "bm0012",                 # 56
        "bm0013",                 # 57
        "bm0100",                 # 58
        "bm0101",                 # 59
        "bm0102",                 # 60
        "bm0110",                 # 61
        "bm0111",                 # 62
        "bm0112",                 # 63
        "bm0113",                 # 64
        "bm0114",                 # 65
        "bt050b",                 # 66
        "bt0600",                 # 67
        "bt0610",                 # 68
        "BT150b",                 # 69
        "BT152b",                 # 70
        "BT154b",                 # 71
        "BT160b",                 # 72
        "BT162b",                 # 73
        "BT163b",                 # 74
        "BT100b",                 # 75
        "BT101b",                 # 76
        "BT102b",                 # 77
        "BT110b",                 # 78
        "BT111b",                 # 79
        "BT112b",                 # 80
        "BT113b",                 # 81
        "BT114b",                 # 82
        "BT115b",                 # 83
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_B4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_D8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_E0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_E4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_E8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_EC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_F4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_FC", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_100", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 0, 0, 180)

    # monster count: 0

    # event battle count: 83

    BattleInfo(
        "BattleInfo_114", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_158", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br000b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_19C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1E0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_224", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_268", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2AC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br1520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2F0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_334", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02100.dat", "ms02200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_378", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3BC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_400", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_444", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br206b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_488", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4CC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_510", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_554", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm1020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_598", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm1030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5DC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm1040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_620", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_664", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm2020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02100.dat", "ms02200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6A8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm2050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6EC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm2099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_730", 0x0010, 3, 6, 3, 90, 1, 1000, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_774", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br300b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7B8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br3100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7FC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_840", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_884", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8C8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_90C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_950", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_994", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9D8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A1C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3080", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A60", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3081", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AA4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3090", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AE8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B2C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B70", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc140b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BB4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc1410", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BF8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc141b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C3C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc1420", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C80", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc0520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_CC4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc0530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D08", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc0540", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D4C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc0550", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D90", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_DD4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E18", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E5C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0001", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_EA0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0002", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_EE4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_F28", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0011", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_F6C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0012", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_FB0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0013", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_FF4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1038", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0101", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_107C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0102", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_10C0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0110", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1104", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0111", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1148", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0112", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_118C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0113", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_11D0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0114", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1214", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bt050b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1258", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bt0600", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_129C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bt0610", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_12E0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT150b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1324", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT152b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1368", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT154b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_13AC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT160b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_13F0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT162b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1434", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT163b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1478", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT100b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_14BC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT101b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1500", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT102b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1544", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT110b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1588", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT111b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_15CC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT112b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1610", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT113b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1654", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT114b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1698", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT115b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    DeclActor(6500,    100,     7500,    1200,    6000,    1100,    -10500,  0x007C, 0,  2,  0x0000)
    DeclActor(6500,    100,     0,       1200,    -6000,   1100,    28500,   0x007C, 0,  3,  0x0000)
    DeclActor(6500,    100,     -7500,   1200,    -6000,   1100,    28500,   0x007C, 0,  4,  0x0000)
    DeclActor(6500,    100,     -25000,  1200,    -6000,   1100,    28500,   0x007C, 0,  5,  0x0000)
    DeclActor(6500,    100,     -29500,  1200,    -6000,   1100,    28500,   0x007C, 0,  6,  0x0000)
    DeclActor(6500,    100,     -35000,  1200,    -6000,   1100,    28500,   0x007C, 0,  7,  0x0000)
    DeclActor(6500,    100,     -42000,  1200,    -6000,   1100,    28500,   0x007C, 0,  8,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 0
    ChipFrameInfo(5000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_1814",         # 00, 0
        "Function_1_1815",         # 01, 1
        "Function_2_1816",         # 02, 2
        "Function_3_1B1E",         # 03, 3
        "Function_4_1D56",         # 04, 4
        "Function_5_211B",         # 05, 5
        "Function_6_24DF",         # 06, 6
        "Function_7_28E1",         # 07, 7
        "Function_8_2D23",         # 08, 8
    ))


    def Function_0_1814(): pass

    label("Function_0_1814")

    Return()

    # Function_0_1814 end

    def Function_1_1815(): pass

    label("Function_1_1815")

    Return()

    # Function_1_1815 end

    def Function_2_1816(): pass

    label("Function_2_1816")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1820")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0D")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "br0000 East Highway\x01",                      # 0
            "br000b East Highway (Bridge, Night)\x01",      # 1
            "br1000 West Highway\x01",                      # 2
            "br0100 Armorica\x01",                          # 3
            "br1500 Ursula By Cliff\x01",                   # 4
            "br1510 Ursula Forest\x01",                     # 5
            "br1520 Ursula By Water\x01",                   # 6
            "br2000 Mainz\x01",                             # 7
            "br2010 Mainz By River\x01",                    # 8
            "br2040 Mainz Mine\x01",                        # 9
            "br2050 Mainz Tunnel\x01",                      # 10
            "br2060 Mainz High Ground\x01",                 # 11
            "br206b Mainz High Ground (Night)\x01",         # 12
            "br2070 Mainz By Cliff\x01",                    # 13
            "Cancel\x01",                                   # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19D8"),
        (1, "loc_19ED"),
        (2, "loc_1A02"),
        (3, "loc_1A17"),
        (4, "loc_1A2C"),
        (5, "loc_1A41"),
        (6, "loc_1A56"),
        (7, "loc_1A6B"),
        (8, "loc_1A80"),
        (9, "loc_1A95"),
        (10, "loc_1AAA"),
        (11, "loc_1ABF"),
        (12, "loc_1AD4"),
        (13, "loc_1AE9"),
        (SWITCH_DEFAULT, "loc_1AFE"),
    )


    label("loc_19D8")

    Battle("BattleInfo_114", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_19ED")

    Battle("BattleInfo_158", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1A02")

    Battle("BattleInfo_19C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1A17")

    Battle("BattleInfo_1E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1A2C")

    Battle("BattleInfo_224", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1A41")

    Battle("BattleInfo_268", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1A56")

    Battle("BattleInfo_2AC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1A6B")

    Battle("BattleInfo_2F0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1A80")

    Battle("BattleInfo_334", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1A95")

    Battle("BattleInfo_378", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1AAA")

    Battle("BattleInfo_3BC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1ABF")

    Battle("BattleInfo_400", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1AD4")

    Battle("BattleInfo_444", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1AE9")

    Battle("BattleInfo_488", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AFE")

    label("loc_1AFE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1820")

    label("loc_1B0D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_2_1816 end

    def Function_3_1B1E(): pass

    label("Function_3_1B1E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D45")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "bm1000 Stargazer's Tower 1\x01",              # 0
            "bm1010 Stargazer's Tower Boss Room\x01",      # 1
            "bm1020 Stargazer's Tower 2\x01",              # 2
            "bm1030 Stargazer's Tower Entrance\x01",       # 3
            "bm1040 Stargazer's Tower Library\x01",        # 4
            "bm2000 Temple\x01",                           # 5
            "bm2020 Temple Cemetary\x01",                  # 6
            "bm2050 Temple Outside\x01",                   # 7
            "bm2099 Temple Boss Room\x01",                 # 8
            "Cancel\x01",                                  # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C79"),
        (1, "loc_1C8E"),
        (2, "loc_1CA3"),
        (3, "loc_1CB8"),
        (4, "loc_1CCD"),
        (5, "loc_1CE2"),
        (6, "loc_1CF7"),
        (7, "loc_1D0C"),
        (8, "loc_1D21"),
        (SWITCH_DEFAULT, "loc_1D36"),
    )


    label("loc_1C79")

    Battle("BattleInfo_4CC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D36")

    label("loc_1C8E")

    Battle("BattleInfo_510", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D36")

    label("loc_1CA3")

    Battle("BattleInfo_554", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D36")

    label("loc_1CB8")

    Battle("BattleInfo_598", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D36")

    label("loc_1CCD")

    Battle("BattleInfo_5DC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D36")

    label("loc_1CE2")

    Battle("BattleInfo_620", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D36")

    label("loc_1CF7")

    Battle("BattleInfo_664", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D36")

    label("loc_1D0C")

    Battle("BattleInfo_6A8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D36")

    label("loc_1D21")

    Battle("BattleInfo_6EC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D36")

    label("loc_1D36")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B28")

    label("loc_1D45")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_3_1B1E end

    def Function_4_1D56(): pass

    label("Function_4_1D56")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210A")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "br3000 Ancient Battlefield\x01",                               # 0
            "br300b Ancient Battlefield (Night)\x01",                       # 1
            "br3100 Ancient Battlefield Inside\x01",                        # 2
            "bm3000 Sun Fort First Stratum\x01",                            # 3
            "bm3010 Sun Fort Lab\x01",                                      # 4
            "bm3020 Sun Fort Third Stratum\x01",                            # 5
            "bm3030 Sun Fort Fourth Stratum Inside\x01",                    # 6
            "bm3040 Sun Fort Fourth Stratum Outside\x01",                   # 7
            "bm3050 Final Boss (Human Form)\x01",                           # 8
            "bm3060 Final Boss (Demonic Form)\x01",                         # 9
            "bm3070 Final Boss (Red Demonic Form)\x01",                     # 10
            "bm3080 Sun Fort Third to Fourth Stratum Shaft\x01",            # 11
            "bm3081 Sun Fort Third to Fourth Stratum Shaft (Red)\x01",      # 12
            "bm3090 Sun Fort Third to Fourth Stratum Mid-Boss\x01",         # 13
            "Cancel\x01",                                                   # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1FD5"),
        (1, "loc_1FEA"),
        (2, "loc_1FFF"),
        (3, "loc_2014"),
        (4, "loc_2029"),
        (5, "loc_203E"),
        (6, "loc_2053"),
        (7, "loc_2068"),
        (8, "loc_207D"),
        (9, "loc_2092"),
        (10, "loc_20A7"),
        (11, "loc_20BC"),
        (12, "loc_20D1"),
        (13, "loc_20E6"),
        (SWITCH_DEFAULT, "loc_20FB"),
    )


    label("loc_1FD5")

    Battle("BattleInfo_730", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_1FEA")

    Battle("BattleInfo_774", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_1FFF")

    Battle("BattleInfo_7B8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_2014")

    Battle("BattleInfo_7FC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_2029")

    Battle("BattleInfo_840", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_203E")

    Battle("BattleInfo_884", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_2053")

    Battle("BattleInfo_8C8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_2068")

    Battle("BattleInfo_90C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_207D")

    Battle("BattleInfo_950", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_2092")

    Battle("BattleInfo_994", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_20A7")

    Battle("BattleInfo_9D8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_20BC")

    Battle("BattleInfo_A1C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_20D1")

    Battle("BattleInfo_A60", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_20E6")

    Battle("BattleInfo_AA4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20FB")

    label("loc_20FB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D60")

    label("loc_210A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_4_1D56 end

    def Function_5_211B(): pass

    label("Function_5_211B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2125")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24CE")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "bc130b In Front of IBC (Night)\x01",               # 0
            "bc1400 Downtown District 1\x01",                   # 1
            "bc140b Downtown District 1 (Night)\x01",           # 2
            "bc1410 Downtown District 2\x01",                   # 3
            "bc141b Downtown District 2 (Night)\x01",           # 4
            "bc1420 Ignis Garage\x01",                          # 5
            "bc0520 Revache Right (Normal)\x01",                # 6
            "bc0530 Revache Right (Boss)\x01",                  # 7
            "bc0540 Revache Left (Normal)\x01",                 # 8
            "bc0550 Revache Left (Boss)\x01",                   # 9
            "bc1460 Abandoned Apartment Room\x01",              # 10
            "bc1470 Abandoned Apartment Hallway\x01",           # 11
            "bm0000 Geofront A Initial Stage Hallway\x01",      # 12
            "bm0001 Geofront A Initial Stage Passage\x01",      # 13
            "bm0002 Geofront A Initial Stage Boss\x01",         # 14
            "Cancel\x01",                                       # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2384"),
        (1, "loc_2399"),
        (2, "loc_23AE"),
        (3, "loc_23C3"),
        (4, "loc_23D8"),
        (5, "loc_23ED"),
        (6, "loc_2402"),
        (7, "loc_2417"),
        (8, "loc_242C"),
        (9, "loc_2441"),
        (10, "loc_2456"),
        (11, "loc_246B"),
        (12, "loc_2480"),
        (13, "loc_2495"),
        (14, "loc_24AA"),
        (SWITCH_DEFAULT, "loc_24BF"),
    )


    label("loc_2384")

    Battle("BattleInfo_AE8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_2399")

    Battle("BattleInfo_B2C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_23AE")

    Battle("BattleInfo_B70", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_23C3")

    Battle("BattleInfo_BB4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_23D8")

    Battle("BattleInfo_BF8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_23ED")

    Battle("BattleInfo_C3C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_2402")

    Battle("BattleInfo_C80", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_2417")

    Battle("BattleInfo_CC4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_242C")

    Battle("BattleInfo_D08", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_2441")

    Battle("BattleInfo_D4C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_2456")

    Battle("BattleInfo_D90", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_246B")

    Battle("BattleInfo_DD4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_2480")

    Battle("BattleInfo_E18", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_2495")

    Battle("BattleInfo_E5C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_24AA")

    Battle("BattleInfo_EA0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24BF")

    label("loc_24BF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2125")

    label("loc_24CE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_5_211B end

    def Function_6_24DF(): pass

    label("Function_6_24DF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28D0")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "bm0010 Geofront A Later Stage Hallway\x01",          # 0
            "bm0011 Geofront A Later Stage Passage\x01",          # 1
            "bm0012 Geofront A Later Stage Boss\x01",             # 2
            "bm0013 Geofront A Later Stage Duct\x01",             # 3
            "bm0100 Geofront B Initial Stage Hallway\x01",        # 4
            "bm0101 Geofront B Initial Stage Passage\x01",        # 5
            "bm0102 Geofront B Initial Stage Boss\x01",           # 6
            "bm0110 Geofront B Later Stage Hallway\x01",          # 7
            "bm0111 Geofront B Later Stage Passage\x01",          # 8
            "bm0112 Geofront B Later Stage Boss\x01",             # 9
            "bm0111 Geofront B Later Stage Ice Hallway\x01",      # 10
            "bm0112 Geofront B Later Stage Ice Passage\x01",      # 11
            "bt050b Mainz Village (Night)\x01",                   # 12
            "bt0600 Mine (No Water)\x01",                         # 13
            "bt0610 Mine (With Water)\x01",                       # 14
            "Cancel\x01",                                         # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2786"),
        (1, "loc_279B"),
        (2, "loc_27B0"),
        (3, "loc_27C5"),
        (4, "loc_27DA"),
        (5, "loc_27EF"),
        (6, "loc_2804"),
        (7, "loc_2819"),
        (8, "loc_282E"),
        (9, "loc_2843"),
        (10, "loc_2858"),
        (11, "loc_286D"),
        (12, "loc_2882"),
        (13, "loc_2897"),
        (14, "loc_28AC"),
        (SWITCH_DEFAULT, "loc_28C1"),
    )


    label("loc_2786")

    Battle("BattleInfo_EE4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_279B")

    Battle("BattleInfo_F28", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_27B0")

    Battle("BattleInfo_F6C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_27C5")

    Battle("BattleInfo_FB0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_27DA")

    Battle("BattleInfo_FF4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_27EF")

    Battle("BattleInfo_1038", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_2804")

    Battle("BattleInfo_107C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_2819")

    Battle("BattleInfo_10C0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_282E")

    Battle("BattleInfo_1104", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_2843")

    Battle("BattleInfo_1148", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_2858")

    Battle("BattleInfo_118C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_286D")

    Battle("BattleInfo_11D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_2882")

    Battle("BattleInfo_1214", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_2897")

    Battle("BattleInfo_1258", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_28AC")

    Battle("BattleInfo_129C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28C1")

    label("loc_28C1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24E9")

    label("loc_28D0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_6_24DF end

    def Function_7_28E1(): pass

    label("Function_7_28E1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D12")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "BT150b Medical College Outside (Night)\x01",             # 0
            "BT152b Medical College Dorm (Night)\x01",                # 1
            "BT154b Medical College Dorm Corridor (Night)\x01",       # 2
            "BT160b Medical College Roof (Night)\x01",                # 3
            "BT162b Medical College Ward Corridor (Night)\x01",       # 4
            "BT163b Medical College Boss (Night)\x01",                # 5
            "BT100b Mishelam Hotel Outside (Night)\x01",              # 6
            "BT101b Mishelam Mansion (Night)\x01",                    # 7
            "BT102b Mishelam Hotel Interior (Night)\x01",             # 8
            "BT110b Mishelam Mansion Out Front (Night)\x01",          # 9
            "BT111b Mishelam Mansion Corridor (Night)\x01",           # 10
            "BT112b Mishelam Mansion Inner Passage (Night)\x01",      # 11
            "BT113b Mishelam Mansion Bedroom (Night)\x01",            # 12
            "BT114b Mishelam Mansion Inner Hallway (Night)\x01",      # 13
            "BT115b Mishelam Mansion Venue (Night)\x01",              # 14
            "Cancel\x01",                                             # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BC8"),
        (1, "loc_2BDD"),
        (2, "loc_2BF2"),
        (3, "loc_2C07"),
        (4, "loc_2C1C"),
        (5, "loc_2C31"),
        (6, "loc_2C46"),
        (7, "loc_2C5B"),
        (8, "loc_2C70"),
        (9, "loc_2C85"),
        (10, "loc_2C9A"),
        (11, "loc_2CAF"),
        (12, "loc_2CC4"),
        (13, "loc_2CD9"),
        (14, "loc_2CEE"),
        (SWITCH_DEFAULT, "loc_2D03"),
    )


    label("loc_2BC8")

    Battle("BattleInfo_12E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2BDD")

    Battle("BattleInfo_1324", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2BF2")

    Battle("BattleInfo_1368", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2C07")

    Battle("BattleInfo_13AC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2C1C")

    Battle("BattleInfo_13F0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2C31")

    Battle("BattleInfo_1434", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2C46")

    Battle("BattleInfo_1478", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2C5B")

    Battle("BattleInfo_14BC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2C70")

    Battle("BattleInfo_1500", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2C85")

    Battle("BattleInfo_1544", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2C9A")

    Battle("BattleInfo_1588", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2CAF")

    Battle("BattleInfo_15CC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2CC4")

    Battle("BattleInfo_1610", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2CD9")

    Battle("BattleInfo_1654", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2CEE")

    Battle("BattleInfo_1698", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D03")

    label("loc_2D03")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28EB")

    label("loc_2D12")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_7_28E1 end

    def Function_8_2D23(): pass

    label("Function_8_2D23")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D8C")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Reserved\x01",      # 0
            "Cancel\x01",        # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D68"),
        (SWITCH_DEFAULT, "loc_2D7D"),
    )


    label("loc_2D68")

    Battle("BattleInfo_12E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D7D")

    label("loc_2D7D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D2D")

    label("loc_2D8C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_8_2D23 end

    SaveToFile()

Try(main)
