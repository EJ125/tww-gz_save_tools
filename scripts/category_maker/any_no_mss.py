from scripts.category_maker.savefile import *

offset = 32768

p0 = [0]
p1 = [0, 0, 0, 0]

num_any_no_mss_savefiles = 18

def create_any_no_mss_savefiles():
    any_no_mss_savefiles = [0]*num_any_no_mss_savefiles
    
    after_intro_requirements = 3
    after_intro_angle = -32768 + offset
    after_intro_position = Vector(-195402.0000, 1650.0, 313668.0000)
    after_intro_cam_pos = Vector(0, 0, 0)
    after_intro_cam_target = Vector(0, 0, 0)
    after_intro_counter = 0
    after_intro_file = PracticeSaveInfo(after_intro_requirements, p0, after_intro_angle, after_intro_position, after_intro_cam_pos, after_intro_cam_target, after_intro_counter, "after_intro", p1)
    any_no_mss_savefiles[0] = after_intro_file

    orca_requirements = 0
    orca_angle = -32768 + offset
    orca_position = Vector(-0.7289, 0.0, 541.7509)
    orca_cam_pos = Vector(0, 0, 0)
    orca_cam_target = Vector(0, 0, 0)
    orca_counter = 0
    orca_file = PracticeSaveInfo(orca_requirements, p0, orca_angle, orca_position, orca_cam_pos, orca_cam_target, orca_counter, "orca", p1)
    any_no_mss_savefiles[1] = orca_file

    fof_requirements = 0
    fof_angle = 0 + offset
    fof_position = Vector(0.0, 0.0, 0.0)
    fof_cam_pos = Vector(0, 0, 0)
    fof_cam_target = Vector(0, 0, 0)
    fof_counter = 0
    fof_file = PracticeSaveInfo(fof_requirements, p0, fof_angle, fof_position, fof_cam_pos, fof_cam_target, fof_counter, "forest_of_fairies", p1)
    any_no_mss_savefiles[2] = fof_file

    ropes_1_requirements = 0
    ropes_1_angle = 0 + offset
    ropes_1_position = Vector(3.7519, -100.0, 514.5142)
    ropes_1_cam_pos = Vector(0, 0, 0)
    ropes_1_cam_target = Vector(0, 0, 0)
    ropes_1_counter = 0
    ropes_1_file = PracticeSaveInfo(ropes_1_requirements, p0, ropes_1_angle, ropes_1_position, ropes_1_cam_pos, ropes_1_cam_target, ropes_1_counter, "ropes_1", p1)
    any_no_mss_savefiles[3] = ropes_1_file

    ff1_requirements = 0
    ff1_angle = 16384 + offset
    ff1_position = Vector(-229.7663, 37.4632, 305.2134)
    ff1_cam_pos = Vector(0, 0, 0)
    ff1_cam_target = Vector(0, 0, 0)
    ff1_counter = 0
    ff1_file = PracticeSaveInfo(ff1_requirements, p0, ff1_angle, ff1_position, ff1_cam_pos, ff1_cam_target, ff1_counter, "ff1", p1)
    any_no_mss_savefiles[4] = ff1_file

    windfall_requirements = 0
    windfall_angle = -24417 + offset
    windfall_position = Vector(-2183.6130, 8.9037, -202257.4531)
    windfall_cam_pos = Vector(0, 0, 0)
    windfall_cam_target = Vector(0, 0, 0)
    windfall_counter = 0
    windfall_file = PracticeSaveInfo(windfall_requirements, p0, windfall_angle, windfall_position, windfall_cam_pos, windfall_cam_target, windfall_counter, "windfall", p1)
    any_no_mss_savefiles[5] = windfall_file

    bombs_swim_requirements = 0
    bombs_swim_angle = 23982 + offset
    bombs_swim_position = Vector(196878.3125, 3.6839, -199901.4375)
    bombs_swim_cam_pos = Vector(0, 0, 0)
    bombs_swim_cam_target = Vector(0, 0, 0)
    bombs_swim_counter = 0
    bombs_swim_file = PracticeSaveInfo(bombs_swim_requirements, p0, bombs_swim_angle, bombs_swim_position, bombs_swim_cam_pos, bombs_swim_cam_target, bombs_swim_counter, "bombs_swim", p1)
    any_no_mss_savefiles[6] = bombs_swim_file

    ropes_2_requirements = 0
    ropes_2_angle = 0 + offset
    ropes_2_position = Vector(3.7519, -100.0, 514.5142)
    ropes_2_cam_pos = Vector(0, 0, 0)
    ropes_2_cam_target = Vector(0, 0, 0)
    ropes_2_counter = 0
    ropes_2_file = PracticeSaveInfo(ropes_2_requirements, p0, ropes_2_angle, ropes_2_position, ropes_2_cam_pos, ropes_2_cam_target, ropes_2_counter, "ropes_2", p1)
    any_no_mss_savefiles[7] = ropes_2_file

    fh_swim_requirements = 0
    fh_swim_angle = -9428 + offset
    fh_swim_position = Vector(672.6375, 95.2612, -197351.6719)
    fh_swim_cam_pos = Vector(0, 0, 0)
    fh_swim_cam_target = Vector(0, 0, 0)
    fh_swim_counter = 0
    fh_swim_file = PracticeSaveInfo(fh_swim_requirements, p0, fh_swim_angle, fh_swim_position, fh_swim_cam_pos, fh_swim_cam_target, fh_swim_counter, "forest_haven_swim", p1)
    any_no_mss_savefiles[8] = fh_swim_file

    dtcs_requirements = 0
    dtcs_angle = 13107 + offset
    dtcs_position = Vector(-2405.6885, 100.00, -1033.3102)
    dtcs_cam_pos = Vector(0, 0, 0)
    dtcs_cam_target = Vector(0, 0, 0)
    dtcs_counter = 0
    dtcs_file = PracticeSaveInfo(dtcs_requirements, p0, dtcs_angle, dtcs_position, dtcs_cam_pos, dtcs_cam_target, dtcs_counter, "dtcs", p1)
    any_no_mss_savefiles[9] = dtcs_file

    quiver_swim_requirements = 0
    quiver_swim_angle = 144 + offset
    quiver_swim_position = Vector(217477.4375, 35.00, 195164.3594)
    quiver_swim_cam_pos = Vector(0, 0, 0)
    quiver_swim_cam_target = Vector(0, 0, 0)
    quiver_swim_counter = 0
    quiver_swim_file = PracticeSaveInfo(quiver_swim_requirements, p0, quiver_swim_angle, quiver_swim_position, quiver_swim_cam_pos, quiver_swim_cam_target, quiver_swim_counter, "quiver_swim", p1)
    any_no_mss_savefiles[10] = quiver_swim_file

    ff2_swim_requirements = 0
    ff2_swim_angle = 0 + offset
    ff2_swim_position = Vector(320000.00, 632.1779, 20070.00)
    ff2_swim_cam_pos = Vector(0, 0, 0)
    ff2_swim_cam_target = Vector(0, 0, 0)
    ff2_swim_counter = 0
    ff2_swim_file = PracticeSaveInfo(ff2_swim_requirements, p0, ff2_swim_angle, ff2_swim_position, ff2_swim_cam_pos, ff2_swim_cam_target, ff2_swim_counter, "ff2_swim", p1)
    any_no_mss_savefiles[11] = ff2_swim_file

    helmaroc_skip_requirements = 0
    helmaroc_skip_angle = 0 + offset
    helmaroc_skip_position = Vector(0.0, 0.0, 0.0)
    helmaroc_skip_cam_pos = Vector(0, 0, 0)
    helmaroc_skip_cam_target = Vector(0, 0, 0)
    helmaroc_skip_counter = 0
    helmaroc_skip_file = PracticeSaveInfo(helmaroc_skip_requirements, p0, helmaroc_skip_angle, helmaroc_skip_position, helmaroc_skip_cam_pos, helmaroc_skip_cam_target, helmaroc_skip_counter, "helmaroc_skip", p1)
    any_no_mss_savefiles[12] = helmaroc_skip_file

    barrier_skip_requirements = 0
    barrier_skip_angle = -32768 + offset
    barrier_skip_position = Vector(0.0, -1977.6412, -8115.4683)
    barrier_skip_cam_pos = Vector(0, 0, 0)
    barrier_skip_cam_target = Vector(0, 0, 0)
    barrier_skip_counter = 0
    barrier_skip_file = PracticeSaveInfo(barrier_skip_requirements, p0, barrier_skip_angle, barrier_skip_position, barrier_skip_cam_pos, barrier_skip_cam_target, barrier_skip_counter, "barrier_skip", p1)
    any_no_mss_savefiles[13] = barrier_skip_file

    trials_skip_requirements = 0
    trials_skip_angle = -32768 + offset
    trials_skip_position = Vector(61.4388, 749.3864, 981.3656)
    trials_skip_cam_pos = Vector(0, 0, 0)
    trials_skip_cam_target = Vector(0, 0, 0)
    trials_skip_counter = 0
    trials_skip_file = PracticeSaveInfo(trials_skip_requirements, p0, trials_skip_angle, trials_skip_position, trials_skip_cam_pos, trials_skip_cam_target, trials_skip_counter, "trials_skip", p1)
    any_no_mss_savefiles[14] = trials_skip_file

    pg_fight_requirements = 0
    pg_fight_angle = -32768 + offset
    pg_fight_position = Vector(-0.2558, -22.4869, 1295.9326)
    pg_fight_cam_pos = Vector(0, 0, 0)
    pg_fight_cam_target = Vector(0, 0, 0)
    pg_fight_counter = 0
    pg_fight_file = PracticeSaveInfo(pg_fight_requirements, p0, pg_fight_angle, pg_fight_position, pg_fight_cam_pos, pg_fight_cam_target, pg_fight_counter, "puppet_ganon", p1)
    any_no_mss_savefiles[15] = pg_fight_file

    morth_hover_requirements = 0
    morth_hover_angle = -32768 + offset
    morth_hover_position = Vector(-0.2558, -22.4869, 1295.9326)
    morth_hover_cam_pos = Vector(0, 0, 0)
    morth_hover_cam_target = Vector(0, 0, 0)
    morth_hover_counter = 0
    morth_hover_file = PracticeSaveInfo(morth_hover_requirements, p0, morth_hover_angle, morth_hover_position, morth_hover_cam_pos, morth_hover_cam_target, morth_hover_counter, "morth_hover", p1)
    any_no_mss_savefiles[16] = morth_hover_file

    ganondorf_requirements = 0
    ganondorf_angle = -32768 + offset
    ganondorf_position = Vector(-4.7554, 0.0, 2644.0217)
    ganondorf_cam_pos = Vector(0, 0, 0)
    ganondorf_cam_target = Vector(0, 0, 0)
    ganondorf_counter = 0
    ganondorf_file = PracticeSaveInfo(ganondorf_requirements, p0, ganondorf_angle, ganondorf_position, ganondorf_cam_pos, ganondorf_cam_target, ganondorf_counter, "ganondorf", p1)
    any_no_mss_savefiles[17] = ganondorf_file

    return any_no_mss_savefiles