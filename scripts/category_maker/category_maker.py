import struct
from scripts.category_maker.any_no_mss import *

format_string = '>BBH9fI32s4B'

with open('any_no_mss.bin', 'wb') as tww_any_no_mss_fp:
    any_no_mss_savefiles = create_any_no_mss_savefiles()
    for i in range(0, num_any_no_mss_savefiles):
        tww_any_no_mss_fp.write(struct.pack(format_string, any_no_mss_savefiles[i].requirements, 0, any_no_mss_savefiles[i].angle, any_no_mss_savefiles[i].position.x, any_no_mss_savefiles[i].position.y, any_no_mss_savefiles[i].position.z, any_no_mss_savefiles[i].cam_pos.x, any_no_mss_savefiles[i].cam_pos.y, any_no_mss_savefiles[i].cam_pos.z, any_no_mss_savefiles[i].cam_target.x, any_no_mss_savefiles[i].cam_target.y, any_no_mss_savefiles[i].cam_target.z, any_no_mss_savefiles[i].counter, any_no_mss_savefiles[i].filename.encode('ascii'), 0, 0, 0, 0))