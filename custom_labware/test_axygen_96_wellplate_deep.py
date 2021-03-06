import json
from opentrons import protocol_api, types


TEST_LABWARE_SLOT = '5'

RATE = 0.25  # % of default speeds

PIPETTE_MOUNT = 'right'
PIPETTE_NAME = 'p20_single_gen2'

TIPRACK_SLOT = '11'
TIPRACK_LOADNAME = 'opentrons_96_tiprack_20ul'
LABWARE_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"Axygen","brandId":["P-2ML-SQ-C"]},"metadata":{"displayName":"Axygen 96 Well Deep Well Plate","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.64,"yDimension":85.34,"zDimension":43.99},"wells":{"A1":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":14.38,"y":74.09,"z":2.59},"B1":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":14.38,"y":65.1,"z":2.59},"C1":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":14.38,"y":56.11,"z":2.59},"D1":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":14.38,"y":47.12,"z":2.59},"E1":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":14.38,"y":38.13,"z":2.59},"F1":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":14.38,"y":29.14,"z":2.59},"G1":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":14.38,"y":20.15,"z":2.59},"H1":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":14.38,"y":11.16,"z":2.59},"A2":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":23.37,"y":74.09,"z":2.59},"B2":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":23.37,"y":65.1,"z":2.59},"C2":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":23.37,"y":56.11,"z":2.59},"D2":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":23.37,"y":47.12,"z":2.59},"E2":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":23.37,"y":38.13,"z":2.59},"F2":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":23.37,"y":29.14,"z":2.59},"G2":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":23.37,"y":20.15,"z":2.59},"H2":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":23.37,"y":11.16,"z":2.59},"A3":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":32.36,"y":74.09,"z":2.59},"B3":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":32.36,"y":65.1,"z":2.59},"C3":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":32.36,"y":56.11,"z":2.59},"D3":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":32.36,"y":47.12,"z":2.59},"E3":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":32.36,"y":38.13,"z":2.59},"F3":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":32.36,"y":29.14,"z":2.59},"G3":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":32.36,"y":20.15,"z":2.59},"H3":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":32.36,"y":11.16,"z":2.59},"A4":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":41.35,"y":74.09,"z":2.59},"B4":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":41.35,"y":65.1,"z":2.59},"C4":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":41.35,"y":56.11,"z":2.59},"D4":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":41.35,"y":47.12,"z":2.59},"E4":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":41.35,"y":38.13,"z":2.59},"F4":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":41.35,"y":29.14,"z":2.59},"G4":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":41.35,"y":20.15,"z":2.59},"H4":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":41.35,"y":11.16,"z":2.59},"A5":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":50.34,"y":74.09,"z":2.59},"B5":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":50.34,"y":65.1,"z":2.59},"C5":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":50.34,"y":56.11,"z":2.59},"D5":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":50.34,"y":47.12,"z":2.59},"E5":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":50.34,"y":38.13,"z":2.59},"F5":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":50.34,"y":29.14,"z":2.59},"G5":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":50.34,"y":20.15,"z":2.59},"H5":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":50.34,"y":11.16,"z":2.59},"A6":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":59.33,"y":74.09,"z":2.59},"B6":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":59.33,"y":65.1,"z":2.59},"C6":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":59.33,"y":56.11,"z":2.59},"D6":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":59.33,"y":47.12,"z":2.59},"E6":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":59.33,"y":38.13,"z":2.59},"F6":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":59.33,"y":29.14,"z":2.59},"G6":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":59.33,"y":20.15,"z":2.59},"H6":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":59.33,"y":11.16,"z":2.59},"A7":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":68.32,"y":74.09,"z":2.59},"B7":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":68.32,"y":65.1,"z":2.59},"C7":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":68.32,"y":56.11,"z":2.59},"D7":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":68.32,"y":47.12,"z":2.59},"E7":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":68.32,"y":38.13,"z":2.59},"F7":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":68.32,"y":29.14,"z":2.59},"G7":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":68.32,"y":20.15,"z":2.59},"H7":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":68.32,"y":11.16,"z":2.59},"A8":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":77.31,"y":74.09,"z":2.59},"B8":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":77.31,"y":65.1,"z":2.59},"C8":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":77.31,"y":56.11,"z":2.59},"D8":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":77.31,"y":47.12,"z":2.59},"E8":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":77.31,"y":38.13,"z":2.59},"F8":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":77.31,"y":29.14,"z":2.59},"G8":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":77.31,"y":20.15,"z":2.59},"H8":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":77.31,"y":11.16,"z":2.59},"A9":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":86.3,"y":74.09,"z":2.59},"B9":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":86.3,"y":65.1,"z":2.59},"C9":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":86.3,"y":56.11,"z":2.59},"D9":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":86.3,"y":47.12,"z":2.59},"E9":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":86.3,"y":38.13,"z":2.59},"F9":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":86.3,"y":29.14,"z":2.59},"G9":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":86.3,"y":20.15,"z":2.59},"H9":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":86.3,"y":11.16,"z":2.59},"A10":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":95.29,"y":74.09,"z":2.59},"B10":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":95.29,"y":65.1,"z":2.59},"C10":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":95.29,"y":56.11,"z":2.59},"D10":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":95.29,"y":47.12,"z":2.59},"E10":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":95.29,"y":38.13,"z":2.59},"F10":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":95.29,"y":29.14,"z":2.59},"G10":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":95.29,"y":20.15,"z":2.59},"H10":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":95.29,"y":11.16,"z":2.59},"A11":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":104.28,"y":74.09,"z":2.59},"B11":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":104.28,"y":65.1,"z":2.59},"C11":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":104.28,"y":56.11,"z":2.59},"D11":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":104.28,"y":47.12,"z":2.59},"E11":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":104.28,"y":38.13,"z":2.59},"F11":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":104.28,"y":29.14,"z":2.59},"G11":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":104.28,"y":20.15,"z":2.59},"H11":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":104.28,"y":11.16,"z":2.59},"A12":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":113.27,"y":74.09,"z":2.59},"B12":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":113.27,"y":65.1,"z":2.59},"C12":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":113.27,"y":56.11,"z":2.59},"D12":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":113.27,"y":47.12,"z":2.59},"E12":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":113.27,"y":38.13,"z":2.59},"F12":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":113.27,"y":29.14,"z":2.59},"G12":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":113.27,"y":20.15,"z":2.59},"H12":{"depth":41.4,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8.26,"yDimension":8.26,"x":113.27,"y":11.16,"z":2.59}},"groups":[{"metadata":{"wellBottomShape":"u"},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"axygen_96_wellplate_deep"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
LABWARE_DEF = json.loads(LABWARE_DEF_JSON)
LABWARE_LABEL = LABWARE_DEF.get('metadata', {}).get(
    'displayName', 'test labware')
LABWARE_DIMENSIONS = LABWARE_DEF.get('wells', {}).get('A1', {}).get('yDimension')

metadata = {'apiLevel': '2.0'}


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(TIPRACK_LOADNAME, TIPRACK_SLOT)
    pipette = protocol.load_instrument(
        PIPETTE_NAME, PIPETTE_MOUNT, tip_racks=[tiprack])

    test_labware = protocol.load_labware_from_definition(
        LABWARE_DEF,
        TEST_LABWARE_SLOT,
        LABWARE_LABEL,
    )

    num_cols = len(LABWARE_DEF.get('ordering', [[]]))
    num_rows = len(LABWARE_DEF.get('ordering', [[]])[0])
    total = num_cols * num_rows
    pipette.pick_up_tip()

    def set_speeds(rate):
        protocol.max_speeds.update({
            'X': (600 * rate),
            'Y': (400 * rate),
            'Z': (125 * rate),
            'A': (125 * rate),
        })

        speed_max = max(protocol.max_speeds.values())

        for instr in protocol.loaded_instruments.values():
            instr.default_speed = speed_max

    set_speeds(RATE)

    pipette.home()
    if(PIPETTE_NAME == 'p20_single_gen2' or PIPETTE_NAME == 'p300_single_gen2' or PIPETTE_NAME == 'p1000_single_gen2' or PIPETTE_NAME == 'p50_single' or PIPETTE_NAME == 'p10_single' or PIPETTE_NAME == 'p300_single' or PIPETTE_NAME == 'p1000_single'):
        if(total > 1):
            #testing with single channel
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]

            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            
            #last well testing
            last_well = (num_cols) * (num_rows)
            well = test_labware.well(last_well-1)
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            set_speeds(RATE)
            #test bottom of last well
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)
        else:
            #testing with single channel + 1 well labware
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]

            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            
            #test bottom of first well
            well = test_labware.well('A1')
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)
    else:
        #testing for multichannel
        if(total == 96 or total == 384): #testing for 96 well plates and 384 first column
            #test first column
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            
            #test last column
            if(total == 96):
                last_col = (num_cols * num_rows) - num_rows
                well = test_labware.well(last_col)
                all_4_edges = [
                    [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                    [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                    [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                    [well._from_center_cartesian(x=0, y=1, z=1), 'back']
                ]
                for edge_pos, edge_name in all_4_edges:
                    set_speeds(RATE)
                    edge_location = types.Location(point=edge_pos, labware=None)
                    pipette.move_to(edge_location)
                    protocol.pause("If the position is accurate click 'resume.'")
                set_speeds(RATE)
                #test bottom of last column
                pipette.move_to(well.bottom())
                protocol.pause("If the position is accurate click 'resume.'")
                pipette.blow_out(well)
            elif(total == 384):
                #testing for 384 well plates - need to hit well 369, last column
                well369 = (total) - (num_rows) + 1
                well = test_labware.well(well369)
                pipette.move_to(well.top())
                protocol.pause("If the position is accurate click 'resume.'")
                all_4_edges = [
                    [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                    [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                    [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                    [well._from_center_cartesian(x=0, y=1, z=1), 'back']
                ]
                for edge_pos, edge_name in all_4_edges:
                    set_speeds(RATE)
                    edge_location = types.Location(point=edge_pos, labware=None)
                    pipette.move_to(edge_location)
                    protocol.pause("If the position is accurate click 'resume.'")
                set_speeds(RATE)
                #test bottom of last column
                pipette.move_to(well.bottom())
                protocol.pause("If the position is accurate click 'resume.'")
                pipette.blow_out(well)
        elif(num_rows == 1 and total > 1 and LABWARE_DIMENSIONS >= 71.2):
            #for 1 row reservoirs - ex: 12 well reservoirs
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=1, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=1, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=0.75, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            #test last well
            well = test_labware.well(-1)
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=1, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=1, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=0.75, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
                #test bottom of first well
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)

        
        elif(total == 1 and LABWARE_DIMENSIONS >= 71.2 ):
            #for 1 well reservoirs
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=1, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=1, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=0.75, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
                #test bottom of first well
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)
        
        else:
            #for incompatible labwares
            protocol.pause("labware is incompatible to calibrate with a multichannel pipette")




    set_speeds(1.0)
    pipette.return_tip()