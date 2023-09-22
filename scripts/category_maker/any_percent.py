import savefile

offset = 32768

p0 = [0]
p1 = [0, 0, 0, 0]

num_any_percent_savefiles = 19

def create_any_percent_savefiles():
    any_percent_savefiles = [0]*num_any_percent_savefiles
    
    mss_requirements = 0
    mss_angle = 0 + offset
    mss_position = savefile.Vector(0.0, 0.0, 0.0)
    mss_cam_pos = savefile.Vector(0, 0, 0)
    mss_cam_target = savefile.Vector(0, 0, 0)
    mss_counter = 0
    mss_file = savefile.PracticeSaveInfo(mss_requirements, p0, mss_angle, mss_position, mss_cam_pos, mss_cam_target, mss_counter, "1.mss", p1)
    any_percent_savefiles[0] = mss_file

    post_mss_requirements = 0
    post_mss_angle = 0 + offset
    post_mss_position = savefile.Vector(0.0, 0.0, 0.0)
    post_mss_cam_pos = savefile.Vector(0, 0, 0)
    post_mss_cam_target = savefile.Vector(0, 0, 0)
    post_mss_counter = 0
    post_mss_file = savefile.PracticeSaveInfo(post_mss_requirements, p0, post_mss_angle, post_mss_position, post_mss_cam_pos, post_mss_cam_target, post_mss_counter, "2.post_mss", p1)
    any_percent_savefiles[1] = post_mss_file

    ff1_requirements = 0
    ff1_angle = 0 + offset
    ff1_position = savefile.Vector(0.0, 0.0, 0.0)
    ff1_cam_pos = savefile.Vector(0, 0, 0)
    ff1_cam_target = savefile.Vector(0, 0, 0)
    ff1_counter = 0
    ff1_file = savefile.PracticeSaveInfo(ff1_requirements, p0, ff1_angle, ff1_position, ff1_cam_pos, ff1_cam_target, ff1_counter, "3.ff1", p1)
    any_percent_savefiles[2] = ff1_file

    bombs_requirements = 0
    bombs_angle = 0 + offset
    bombs_position = savefile.Vector(0.0, 0.0, 0.0)
    bombs_cam_pos = savefile.Vector(0, 0, 0)
    bombs_cam_target = savefile.Vector(0, 0, 0)
    bombs_counter = 0
    bombs_file = savefile.PracticeSaveInfo(bombs_requirements, p0, bombs_angle, bombs_position, bombs_cam_pos, bombs_cam_target, bombs_counter, "4.bombs", p1)
    any_percent_savefiles[3] = bombs_file

    sail_skip_requirements = 0
    sail_skip_angle = 0 + offset
    sail_skip_position = savefile.Vector(0.0, 0.0, 0.0)
    sail_skip_cam_pos = savefile.Vector(0, 0, 0)
    sail_skip_cam_target = savefile.Vector(0, 0, 0)
    sail_skip_counter = 0
    sail_skip_file = savefile.PracticeSaveInfo(sail_skip_requirements, p0, sail_skip_angle, sail_skip_position, sail_skip_cam_pos, sail_skip_cam_target, sail_skip_counter, "5.sail_skip", p1)
    any_percent_savefiles[4] = sail_skip_file

    ropes_2_requirements = 0
    ropes_2_angle = 0 + offset
    ropes_2_position = savefile.Vector(0.0, 0.0, 0.0)
    ropes_2_cam_pos = savefile.Vector(0, 0, 0)
    ropes_2_cam_target = savefile.Vector(0, 0, 0)
    ropes_2_counter = 0
    ropes_2_file = savefile.PracticeSaveInfo(ropes_2_requirements, p0, ropes_2_angle, ropes_2_position, ropes_2_cam_pos, ropes_2_cam_target, ropes_2_counter, "6.ropes_2", p1)
    any_percent_savefiles[5] = ropes_2_file

    fh_swim_requirements = 0
    fh_swim_angle = 0 + offset
    fh_swim_position = savefile.Vector(0.0, 0.0, 0.0)
    fh_swim_cam_pos = savefile.Vector(0, 0, 0)
    fh_swim_cam_target = savefile.Vector(0, 0, 0)
    fh_swim_counter = 0
    fh_swim_file = savefile.PracticeSaveInfo(fh_swim_requirements, p0, fh_swim_angle, fh_swim_position, fh_swim_cam_pos, fh_swim_cam_target, fh_swim_counter, "7.fh_swim", p1)
    any_percent_savefiles[6] = fh_swim_file

    dtcs_requirements = 0
    dtcs_angle = 0 + offset
    dtcs_position = savefile.Vector(0.0, 0.0, 0.0)
    dtcs_cam_pos = savefile.Vector(0, 0, 0)
    dtcs_cam_target = savefile.Vector(0, 0, 0)
    dtcs_counter = 0
    dtcs_file = savefile.PracticeSaveInfo(dtcs_requirements, p0, dtcs_angle, dtcs_position, dtcs_cam_pos, dtcs_cam_target, dtcs_counter, "8.dtcs", p1)
    any_percent_savefiles[7] = dtcs_file

    quiver_ssff2_requirements = 0
    quiver_ssff2_angle = 0 + offset
    quiver_ssff2_position = savefile.Vector(0.0, 0.0, 0.0)
    quiver_ssff2_cam_pos = savefile.Vector(0, 0, 0)
    quiver_ssff2_cam_target = savefile.Vector(0, 0, 0)
    quiver_ssff2_counter = 0
    quiver_ssff2_file = savefile.PracticeSaveInfo(quiver_ssff2_requirements, p0, quiver_ssff2_angle, quiver_ssff2_position, quiver_ssff2_cam_pos, quiver_ssff2_cam_target, quiver_ssff2_counter, "9.quiver_ssff2", p1)
    any_percent_savefiles[8] = quiver_ssff2_file

    ff2_swim_requirements = 0
    ff2_swim_angle = 0 + offset
    ff2_swim_position = savefile.Vector(0.0, 0.0, 0.0)
    ff2_swim_cam_pos = savefile.Vector(0, 0, 0)
    ff2_swim_cam_target = savefile.Vector(0, 0, 0)
    ff2_swim_counter = 0
    ff2_swim_file = savefile.PracticeSaveInfo(ff2_swim_requirements, p0, ff2_swim_angle, ff2_swim_position, ff2_swim_cam_pos, ff2_swim_cam_target, ff2_swim_counter, "10.ff2_swim", p1)
    any_percent_savefiles[9] = ff2_swim_file

    helmaroc_skip_requirements = 0
    helmaroc_skip_angle = 0 + offset
    helmaroc_skip_position = savefile.Vector(0.0, 0.0, 0.0)
    helmaroc_skip_cam_pos = savefile.Vector(0, 0, 0)
    helmaroc_skip_cam_target = savefile.Vector(0, 0, 0)
    helmaroc_skip_counter = 0
    helmaroc_skip_file = savefile.PracticeSaveInfo(helmaroc_skip_requirements, p0, helmaroc_skip_angle, helmaroc_skip_position, helmaroc_skip_cam_pos, helmaroc_skip_cam_target, helmaroc_skip_counter, "11.helm_skip", p1)
    any_percent_savefiles[10] = helmaroc_skip_file

    barrier_skip_requirements = 0
    barrier_skip_angle = 0 + offset
    barrier_skip_position = savefile.Vector(0.0, 0.0, 0.0)
    barrier_skip_cam_pos = savefile.Vector(0, 0, 0)
    barrier_skip_cam_target = savefile.Vector(0, 0, 0)
    barrier_skip_counter = 0
    barrier_skip_file = savefile.PracticeSaveInfo(barrier_skip_requirements, p0, barrier_skip_angle, barrier_skip_position, barrier_skip_cam_pos, barrier_skip_cam_target, barrier_skip_counter, "12.bs", p1)
    any_percent_savefiles[11] = barrier_skip_file

    trials_skip_requirements = 0
    trials_skip_angle = 0 + offset
    trials_skip_position = savefile.Vector(0.0, 0.0, 0.0)
    trials_skip_cam_pos = savefile.Vector(0, 0, 0)
    trials_skip_cam_target = savefile.Vector(0, 0, 0)
    trials_skip_counter = 0
    trials_skip_file = savefile.PracticeSaveInfo(trials_skip_requirements, p0, trials_skip_angle, trials_skip_position, trials_skip_cam_pos, trials_skip_cam_target, trials_skip_counter, "13.trials_skip", p1)
    any_percent_savefiles[12] = trials_skip_file

    las_requirements = 0
    las_angle = 0 + offset
    las_position = savefile.Vector(0.0, 0.0, 0.0)
    las_cam_pos = savefile.Vector(0, 0, 0)
    las_cam_target = savefile.Vector(0, 0, 0)
    las_counter = 0
    las_file = savefile.PracticeSaveInfo(las_requirements, p0, las_angle, las_position, las_cam_pos, las_cam_target, las_counter, "14.las", p1)
    any_percent_savefiles[13] = barrier_skip_file

    pgcs_requirements = 0
    pgcs_angle = 0 + offset
    pgcs_position = savefile.Vector(0.0, 0.0, 0.0)
    pgcs_cam_pos = savefile.Vector(0, 0, 0)
    pgcs_cam_target = savefile.Vector(0, 0, 0)
    pgcs_counter = 0
    pgcs_file = savefile.PracticeSaveInfo(pgcs_requirements, p0, pgcs_angle, pgcs_position, pgcs_cam_pos, pgcs_cam_target, pgcs_counter, "15.pgcs", p1)
    any_percent_savefiles[14] = trials_skip_file

    pg_skip_requirements = 0
    pg_skip_angle = 0 + offset
    pg_skip_position = savefile.Vector(0.0, 0.0, 0.0)
    pg_skip_cam_pos = savefile.Vector(0, 0, 0)
    pg_skip_cam_target = savefile.Vector(0, 0, 0)
    pg_skip_counter = 0
    pg_skip_file = savefile.PracticeSaveInfo(pg_skip_requirements, p0, pg_skip_angle, pg_skip_position, pg_skip_cam_pos, pg_skip_cam_target, pg_skip_counter, "16.pg_skip", p1)
    any_percent_savefiles[15] = pg_skip_file
    
    pg_fight_requirements = 0
    pg_fight_angle = 0 + offset
    pg_fight_position = savefile.Vector(0.0, 0.0, 0.0)
    pg_fight_cam_pos = savefile.Vector(0, 0, 0)
    pg_fight_cam_target = savefile.Vector(0, 0, 0)
    pg_fight_counter = 0
    pg_fight_file = savefile.PracticeSaveInfo(pg_fight_requirements, p0, pg_fight_angle, pg_fight_position, pg_fight_cam_pos, pg_fight_cam_target, pg_fight_counter, "17.pg", p1)
    any_percent_savefiles[16] = pg_fight_file

    morth_hover_requirements = 0
    morth_hover_angle = 0 + offset
    morth_hover_position = savefile.Vector(0.0, 0.0, 0.0)
    morth_hover_cam_pos = savefile.Vector(0, 0, 0)
    morth_hover_cam_target = savefile.Vector(0, 0, 0)
    morth_hover_counter = 0
    morth_hover_file = savefile.PracticeSaveInfo(morth_hover_requirements, p0, morth_hover_angle, morth_hover_position, morth_hover_cam_pos, morth_hover_cam_target, morth_hover_counter, "18.morth_hover", p1)
    any_percent_savefiles[17] = morth_hover_file

    ganondorf_requirements = 0
    ganondorf_angle = 0 + offset
    ganondorf_position = savefile.Vector(0.0, 0.0, 0.0)
    ganondorf_cam_pos = savefile.Vector(0, 0, 0)
    ganondorf_cam_target = savefile.Vector(0, 0, 0)
    ganondorf_counter = 0
    ganondorf_file = savefile.PracticeSaveInfo(ganondorf_requirements, p0, ganondorf_angle, ganondorf_position, ganondorf_cam_pos, ganondorf_cam_target, ganondorf_counter, "19.ganondorf", p1)
    any_percent_savefiles[18] = ganondorf_file

    return any_percent_savefiles
