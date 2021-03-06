metadata = {
    'protocolName': 'Distribute master mix into sample plates',
    'author': 'AMB, last updated 5/3/22',
    'description': 'Generic protocol to distribute master mix from 2 mL tube to PCR plates or strip tubes.',
    'apiLevel': '2.11'
}


def run(protocol):
    ########## EDIT THESE RUN OPTIONS AS NEEDED ##########

    # location of p20 single channel ('left' or 'right', all lowercase and in single quotes)
    pipette_mount_20 = 'right'

    # master mix on temperature block to keep cold ('yes' or 'no', all lowercase and in single quotes)
    mm_block = 'no'

    # temperature that block should be set to (integar, min: 4, max: 95)
    # put None if not using temp block (no quotes, first letter capitalized)
    mm_temp = None

    # number of sample plates (integer, max: 5)
    sample_plates = 1

    # volume (ul) of master mix to add to each well (must be 1-20 ul)
    mm_vol = 5

    # specify if pipette tip should tap the side of well after dispensing ('yes' or 'no', all lowercase and in single quotes)
    # recommended 'yes' if dispensing <10 ul
    touch_tip = 'yes'

    # mix after pipetting master mix into well ('yes' or 'no', all lowercase and in single quotes)
    mix_sample = 'no'

    # specify if tip should be changed in between wells ('yes' or 'no', all lowercase and in single quotes)
    # if tip touches sides of wells after dispensing and there is DNA already present in well this should be 'yes'
    # if mixing sample after dispensing, should be 'yes'
    change_tip = 'no'

    # number of 20 ul tip racks loaded (integer, max: 5, should match the number of sample plates if changing tips between wells)
    num_racks = 1

    # number of samples in each plate (list of integers, surrounded by brackets and separated by commas)
    # ex: [96, 12, 72]
    # (will go by rows, i.e. 12 would mean samples A1-A12, 30 would mean A1-C6)
    num_samples_each_plate = [12]

    # list wells that should be skipped (well name in single quotes and in brackets. Multiple wells separated by commas
    # ex: ['C2', 'D11', 'E1']
    # these samples should be included in the sample count above
    # ex: you want the protocol to distribute all the way to A12, but skip A10
    # your sample count would be 12 and then you would indicate to skip A10: P1_skip = ['A10']
    # if not skipping anything or not using that plate don't put anything between brackets
    P1_skip = []
    P2_skip = []
    P3_skip = []
    P4_skip = []
    P5_skip = []

    # sample plate type ('biorad_200ul', 'nest_100ul', or 'strip_tubes', all lowercase and in single quotes)
    plate_type = 'biorad_200ul'

    # type of tube containing master mix ('1.5ml' or '2ml', all lowercase and in single quotes)
    mm_tube_type = '1.5ml'

    ########## DO NOT EDIT BELOW THIS LINE ##########

    # turn on lights if not on already
    protocol.set_rail_lights(True)

    # checks
    if len(num_samples_each_plate) != sample_plates:
        raise Exception("The number of sample plates does not match the number of samples for each plate.")

    # Define hardware
    # load designated number of tip racks
    slot_range = list(range(7, 7 + num_racks))
    tips20 = [protocol.load_labware(
            'opentrons_96_tiprack_20ul', str(slot)) for slot in slot_range]

    # specify pipette, mount location, and tips
    p20 = protocol.load_instrument("p20_single_gen2", mount=pipette_mount_20, tip_racks=tips20)

    # load plates
    plate_names = []
    # add 1st plate
    if plate_type == 'nest_100ul':
        plate_1 = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '2', 'sample plate 1')
        plate_names.append(plate_1)
    elif plate_type == 'biorad_200ul':
        plate_1 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '2', 'sample plate 1')
        plate_names.append(plate_1)
    elif plate_type == "strip_tubes":
        plate_1 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '2', 'sample plate 1')
        plate_names.append(plate_1)
    else:
        raise Exception("Invalid source plate type")

    # add 2nd plate
    if sample_plates > 1:
        if plate_type == 'nest_100ul':
            plate_2 = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '3', 'sample plate 2')
            plate_names.append(plate_2)
        elif plate_type == 'biorad_200ul':
            plate_2 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '3', 'sample plate 2')
            plate_names.append(plate_2)
        elif plate_type == "strip_tubes":
            plate_2 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '3', 'sample plate 2')
            plate_names.append(plate_2)

    # add 3rd plate
    if sample_plates > 2:
        if plate_type == 'nest_100ul':
            plate_3 = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '4', 'sample plate 3')
            plate_names.append(plate_3)
        elif plate_type == 'biorad_200ul':
            plate_3 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '4', 'sample plate 3')
            plate_names.append(plate_3)
        elif plate_type == "strip_tubes":
            plate_3 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '4', 'sample plate 3')
            plate_names.append(plate_3)

    # add 4th plate
    if sample_plates > 3:
        if plate_type == 'nest_100ul':
            plate_4 = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '5', 'sample plate 4')
            plate_names.append(plate_4)
        elif plate_type == 'biorad_200ul':
            plate_4 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '5', 'sample plate 4')
            plate_names.append(plate_4)
        elif plate_type == "strip_tubes":
            plate_4 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '5', 'sample plate 4')
            plate_names.append(plate_4)

    # add 5th plate
    if sample_plates > 4:
        if plate_type == 'nest_100ul':
            plate_5 = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '6', 'sample plate 5')
            plate_names.append(plate_5)
        elif plate_type == 'biorad_200ul':
            plate_5 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '6', 'sample plate 5')
            plate_names.append(plate_5)
        elif plate_type == "strip_tubes":
            plate_5 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '6', 'sample plate 5')
            plate_names.append(plate_5)

    # add master mix tube/plate & temp block if specified
    if mm_block == 'yes':
        temp_mod = protocol.load_module('temperature module gen2', '1')
        temp_mod.set_temperature(mm_temp) # set temp block temperature
        if mm_tube_type == '1.5ml':
            tube_rack = temp_mod.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', 'master mix tube')
        elif mm_tube_type == '2ml':
            tube_rack = temp_mod.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', 'master mix tube')
        else:
            raise Exception('Invalid tube type for master mix.')
    elif mm_block == 'no':
        if mm_tube_type == '1.5ml':
            tube_rack = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', '1', 'master mix tube')
        elif mm_tube_type == '2ml':
            tube_rack = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap', '1', 'master mix tube')
        else:
            raise Exception('Invalid tube type for master mix.')
    else:
        raise Exception("Did not specify if temperature block should be used. Should be 'yes' or 'no'")

    mm_tube = tube_rack.wells_by_name()['A1']

    # set aspirate and dispense speeds
    p20.flow_rate.aspirate = 150
    p20.flow_rate.dispense = 150

    # list of possible wells
    well_names = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12',
                  'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12',
                  'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12',
                  'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12',
                  'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12',
                  'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
                  'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12',
                  'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12']

    # list of wells to skip for each plate
    wells_skip = [P1_skip, P2_skip, P3_skip, P4_skip, P5_skip]

    # pick up tip that will be used the whole time if not changing in between
    if change_tip == 'no':
        p20.pick_up_tip()
    # distribute master mix
    for num_plate in range(0, len(plate_names)):
        for sample in range(0, num_samples_each_plate[num_plate]):
            plate = plate_names[num_plate]
            sample_name = well_names[sample]
            # move on to next iteration of loop if sample name is in the skip list for this plate
            if sample_name in wells_skip[num_plate]:
                continue
            # pick up tip if changing every time
            if change_tip == 'yes':
                p20.pick_up_tip()
            p20.aspirate(mm_vol, mm_tube)
            p20.dispense(mm_vol, plate.wells_by_name()[sample_name].top())
            if mix_sample == 'yes':
                p20.mix(5, mm_vol)
            p20.blow_out()
            if touch_tip == 'yes':
                p20.touch_tip()
            if change_tip == 'yes':
                p20.drop_tip()

    # drop tip at end if tip wasnt changed between samples
    if change_tip == 'no':
        p20.drop_tip()

    # turn off lights when protocol complete
    protocol.set_rail_lights(False)