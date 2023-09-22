import struct
import any_percent

format_string = '>BBH9fI32s4B'

with open('any_percent.bin', 'wb') as tww_any_percent_fp:
    any_percent_savefiles = any_percent.create_any_percent_savefiles()
    for i in range(0, any_percent.num_any_percent_savefiles):
        tww_any_percent_fp.write(struct.pack(format_string, any_percent_savefiles[i].requirements, 0, any_percent_savefiles[i].angle, any_percent_savefiles[i].position.x, any_percent_savefiles[i].position.y, any_percent_savefiles[i].position.z, any_percent_savefiles[i].cam_pos.x, any_percent_savefiles[i].cam_pos.y, any_percent_savefiles[i].cam_pos.z, any_percent_savefiles[i].cam_target.x, any_percent_savefiles[i].cam_target.y, any_percent_savefiles[i].cam_target.z, any_percent_savefiles[i].counter, any_percent_savefiles[i].filename.encode('ascii'), 0, 0, 0, 0))
