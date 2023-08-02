import struct

def checkStructSize(name, format, expected_size):
    format_size = struct.calcsize(format)
    assert format_size == expected_size, f"Incorrect format:  {name} is expected to be of size {expected_size}, but is of size {format_size} instead"

stage_max = 16

def cat_format_str(format_string, num):
    final_format_str = ''
    for i in range(0, num):
        final_format_str += format_string
    return final_format_str


cXyz = '3f'
numFields_cXyz = 3
sizeof_cXyz = 12

checkStructSize("cXyz", cXyz, sizeof_cXyz)

def print_cXyz(data):
    print('cXyz')
    print(f'x:\t{data[0]}')
    print(f'y:\t{data[1]}')
    print(f'z:\t{data[2]}')



dSv_player_status_a_c = '4HB5B4B5BB'
numFields_dSv_player_status_a_c = 5 + 5 + 4 + 5 + 1
sizeof_player_status_a_c = 0x18

checkStructSize("dSv_player_status_a_c", dSv_player_status_a_c, sizeof_player_status_a_c)

def print_dSv_player_status_a_c(data):
    print('dSv_player_status_a_c')
    print(f'mMaxLife:\t{data[0]}')
    print(f'mLife:\t{data[1]}')
    print(f'mRupee:\t{data[2]}')
    print(f'field_0x6:\t{data[3]}')
    print(f'field_0x8:\t{data[4]}')
    print(f'mSelectItem:\t{data[5:10]}')
    print(f'mSelectEquip:\t{data[10:14]}')
    print(f'mWalletSize:\t{data[14]}')
    print(f'mMaxMagic:\t{data[15]}')
    print(f'mMagic:\t{data[16]}')
    print(f'field_0x15:\t{data[17]}')
    print(f'field_0x16:\t{data[18]}')
    print(f'padding:\t{data[19]}')
    print('\n\n')



dSv_player_status_b_c = 'QffHhhh'
numFields_dSv_player_status_b_c = 7
sizeof_dSv_player_status_b_c = 0x18

checkStructSize("dSv_player_status_b_c", dSv_player_status_b_c, sizeof_dSv_player_status_b_c)

def print_dSv_player_status_b_c(data):
    print('dSv_player_status_b_c')
    print(f'mDateIPL:\t{data[0]}')
    print(f'field_0x8:\t{data[1]}')
    print(f'mTime:\t{data[2]}')
    print(f'mDate:\t{data[3]}')
    print(f'mTactWindAngleX:\t{data[4]}')
    print(f'mTactWindAngleY:\t{data[5]}')
    print(f'padding:\t{data[6]}')
    print('\n\n')


dSv_player_return_place_c = '8cb3B'
numFields_dSv_player_return_place_c = 12
sizeof_dSv_player_return_place_c = 0xC

checkStructSize("dSv_player_return_place_c", dSv_player_return_place_c, sizeof_dSv_player_return_place_c)

def print_dSv_player_return_place_c(data):
    print('dSv_player_return_place_c')
    print('mName:\t', data[0:8])
    print(f'mRoomNo:\t{data[8]}')
    print(f'mPlayerStatus:\t{data[9]}')
    print(f'unk10:\t{data[10]}')
    print(f'unk11:\t{data[11]}')
    print('\n\n')


dSv_player_item_c = '21B'
numFields_dSv_player_item_c = 21
sizeof_dSv_player_item_c = 0x15

checkStructSize("dSv_player_item_c", dSv_player_item_c, sizeof_dSv_player_item_c)

def print_dSv_player_item_c(data):
    print('dSv_player_item_c')
    for i in range(0, numFields_dSv_player_item_c):
        print(f'mItemSlots[{i}]:\t{data[i]}')
    print('\n\n')


dSv_player_get_item_c = '21B'
numFields_dSv_player_get_item_c = 21
sizeof_dSv_player_get_item_c = 0x15

checkStructSize("dSv_player_get_item_c", dSv_player_get_item_c, sizeof_dSv_player_get_item_c)

def print_dSv_player_get_item_c(data):
    print('dSv_player_get_item_c')
    for i in range(0, numFields_dSv_player_get_item_c):
        print(f'mItemFlags[{i}]:\t{data[i]}')
    print('\n\n')


dSv_player_item_record_c = 'H3B3B'
numFields_dSv_player_item_record_c = 7
sizeof_dSv_player_item_record_c = 0x8

checkStructSize("dSv_player_item_record_c", dSv_player_item_record_c, sizeof_dSv_player_item_record_c)

def print_dSv_player_item_record_c(data):
    print('dSv_player_item_record_c')
    print(f'mTimer:\t{data[0]}')
    print(f'field_0x2:\t{data[1]}')
    print(f'mArrowNum:\t{data[2]}')
    print(f'mBombNum:\t{data[3]}')
    print(f'mBottleNum:\t{data[4:7]}')
    print('\n\n')


dSv_player_item_max_c = '8B'
numFields_dSv_player_item_max_c = 8
sizeof_dSv_player_item_max_c = 0x8

checkStructSize("dSv_player_item_max_c", dSv_player_item_max_c, sizeof_dSv_player_item_max_c)

def print_dSv_player_item_max_c(data):
    print('dSv_player_item_max_c')
    print(f'field_0x0:\t{data[0]}')
    print(f'mArrowNum:\t{data[1]}')
    print(f'mBombNum:\t{data[2]}')
    print(f'field_0x3:\t{data[3:8]}')
    print('\n\n')


dSv_player_bag_item_c = '24B'
numFields_dSv_player_bag_item_c = 24
sizeof_dSv_player_bag_item_c = 0x18

checkStructSize("dSv_player_bag_item_c", dSv_player_bag_item_c, sizeof_dSv_player_bag_item_c)

def print_dSv_player_bag_item_c(data):
    print('dSv_player_bag_item_c')
    print(f'field_0x0:\t{data[0:8]}')
    print(f'field_0x8:\t{data[8:16]}')
    print(f'field_0x10:\t{data[16:24]}')
    print('\n\n')


dSv_player_get_bag_item_c = 'IBB6B'
numFields_dSv_player_get_bag_item_c = 9
sizeof_dSv_player_get_bag_item_c = 0xC

checkStructSize("dSv_player_get_bag_item_c", dSv_player_get_bag_item_c, sizeof_dSv_player_get_bag_item_c)

def print_dSv_player_get_bag_item_c(data):
    print('dSv_player_get_bag_item_c')
    print(f'mReserveFlags:\t{data[0]}')
    print(f'mBeastFlags:\t{data[1]}')
    print(f'mBaitFlags:\t{data[2]}')
    print(f'unk_0x6:\t{data[3:9]}')
    print('\n\n')


dSv_player_bag_item_record_c = '24B'
numFields_dSv_player_bag_item_record_c = 24
sizeof_dSv_player_bag_item_record_c = 0x18

checkStructSize("dSv_player_bag_item_record_c", dSv_player_bag_item_record_c, sizeof_dSv_player_bag_item_record_c)

def print_dSv_player_bag_item_record_c(data):
    print('dSv_player_bag_item_record_c')
    print(f'field_0x0:\t{data[0:8]}')
    print(f'field_0x8:\t{data[8:16]}')
    print(f'field_0x10:\t{data[16:24]}')
    print('\n\n')


dSv_player_collect_c = '8B5B'
numFields_dSv_player_collect_c = 13
sizeof_dSv_player_collect_c = 0xD

checkStructSize("dSv_player_collect_c", dSv_player_collect_c, sizeof_dSv_player_collect_c)

def print_dSv_player_collect_c(data):
    print('dSv_player_collect_c')
    index = 0
    print(f'mItem:\t{data[index:index + 8]}')
    index += 8
    print(f'unk8:\t{data[index:index + 1]}')
    index += 1
    print(f'mTact:\t{data[index:index + 1]}')
    index += 1
    print(f'mTriforce:\t{data[index:index + 1]}')
    index += 1
    print(f'mSymbol:\t{data[index:index + 1]}')
    index += 1
    print(f'field_0xc:\t{data[index:index + 1]}')
    index += 1
    print('\n\n')


dSv_player_map_c = '16I49B16BB2B'
numFields_dSv_player_map_c = 16 + 49 + 16 + 1 + 2
sizeof_dSv_player_map_c = 0x84

checkStructSize("dSv_player_map_c", dSv_player_map_c, sizeof_dSv_player_map_c)

def print_dSv_player_map_c(data):
    print('dSv_player_map_c')
    index = 0
    print(f'field_0x0:\t{data[index:index + 16]}')
    index += 16
    print(f'field_0x40:\t{data[index:index + 49]}')
    index += 49
    print(f'field_0x71:\t{data[index:index + 16]}')
    index += 16
    print(f'field_0x81:\t{data[index:index + 1]}')
    index += 1
    print(f'field_0x82:\t{data[index:index + 2]}')
    index += 2
    print('\n\n')


dSv_player_info_c = '16B2H17c17c17c17c2B2B'
numFields_dSv_player_info_c = 16 + 2 + 4*17 + 2 + 2
sizeof_dSv_player_info_c = 0x5C

checkStructSize("dSv_player_info_c", dSv_player_info_c, sizeof_dSv_player_info_c)

def print_dSv_player_info_c(data):
    print('dSv_player_info_c')
    index = 0
    print(f'field_0x0:\t{data[index:index + 16]}')
    index += 16
    print(f'field_0x10:\t{data[index:index + 1]}')
    index += 1
    print(f'field_0x12:\t{data[index:index + 1]}')
    index += 1
    print(f'mPlayerName:\t{data[index:index + 17]}')
    index += 17
    print(f'field_0x25:\t{data[index:index + 17]}')
    index += 17
    print(f'field_0x36:\t{data[index:index + 17]}')
    index += 17
    print(f'field_0x47:\t{data[index:index + 17]}')
    index += 17
    print(f'mClearCount:\t{data[index:index + 1]}')
    index += 1
    print(f'mFmapIdx:\t{data[index:index + 1]}')
    index += 1
    print(f'field_0x5a:\t{data[index:index + 2]}')
    index += 2
    print('\n\n')


dSv_player_config_c = '5B'
numFields_dSv_player_config_c = 5
sizeof_dSv_player_config_c = 0x5

checkStructSize("dSv_player_config_c", dSv_player_config_c, sizeof_dSv_player_config_c)

def print_dSv_player_config_c(data):
    print(f'field_0x0:\t{data[0]}')
    print(f'mSoundMode:\t{data[1]}')
    print(f'mAttentionType:\t{data[2]}')
    print(f'mVibration:\t{data[3]}')
    print(f'field_0x4:\t{data[4]}')
    print('\n\n')


dSv_player_priest_c = cXyz + 'hbB'
numFields_dSv_player_priest_c = 6
sizeof_dSv_player_priest_c = 0x10

checkStructSize("dSv_player_priest_c", dSv_player_priest_c, sizeof_dSv_player_priest_c)

def print_dSv_player_priest_c(data):
    print('player_priest_c')
    index = 0
    print_cXyz(data[index:index + numFields_cXyz])
    index += numFields_cXyz
    print(f'field_0xc:\t{data[index:index + 1]}')
    index += 1
    print(f'field_0xe:\t{data[index:index + 1]}')
    index += 1
    print(f'field_0xf:\t{data[index:index + 1]}')
    index += 1
    print('\n\n')



dSv_player_status_c_c = dSv_player_status_a_c + dSv_player_item_c + '3B3B' + dSv_player_bag_item_c + dSv_player_bag_item_record_c + '13B'
numFields_dSv_player_status_c_c = numFields_dSv_player_status_a_c + numFields_dSv_player_item_c + 6 + numFields_dSv_player_bag_item_c + numFields_dSv_player_bag_item_record_c + 13
sizeof_dSv_player_status_c_c = 0x70

checkStructSize("dSv_player_status_c_c", dSv_player_status_c_c, sizeof_dSv_player_status_c_c)

def print_dSv_player_status_c_c(data):
    index = 0
    print('dSv_player_status_c_c')
    print_dSv_player_status_a_c(data[index:index + numFields_dSv_player_status_a_c])
    index += numFields_dSv_player_status_a_c
    print_dSv_player_item_c(data[index:index + numFields_dSv_player_item_c])
    index += numFields_dSv_player_item_c
    print(f'mRecollectItemRecord:\t{data[index:index+3]}')
    index += 3
    print(f'mRecollectItemMax:\t{data[index:index+3]}')
    index += 3
    print_dSv_player_bag_item_c(data[index:index + numFields_dSv_player_bag_item_c])
    index += numFields_dSv_player_bag_item_c
    print_dSv_player_bag_item_record_c(data[index:index + numFields_dSv_player_bag_item_record_c])
    index += numFields_dSv_player_bag_item_record_c
    print(f'mRecollectCollect:\t{data[index:index + 13]}')
    index += 13
    print('\n\n')


dSv_memBit_c = 'I4II2I2Bh'
numFields_dSv_memBit_c = 11
sizeof_dSv_memBit_c = 0x24

checkStructSize("dSv_memBit_c", dSv_memBit_c, sizeof_dSv_memBit_c)

def print_dSv_memBit_c(data):
    print('dSv_memBit_c')
    print(f'mTbox:\t{data[0]}')
    print(f'mSwitch:\t{data[1:5]}')
    print(f'mItem:\t{data[5]}')
    print(f'mVisitedRoom:\t{data[6:8]}')
    print(f'field_0x20:\t{data[8]}')
    print(f'mDungeonItem:\t{data[9]}')
    print(f'padding:\t{data[10]}')
    print('\n\n')



dSv_player_c = dSv_player_status_a_c + dSv_player_status_b_c + dSv_player_return_place_c \
                + dSv_player_item_c + dSv_player_get_item_c + dSv_player_item_record_c \
                + dSv_player_item_max_c + dSv_player_bag_item_c + dSv_player_get_bag_item_c \
                + dSv_player_bag_item_record_c + dSv_player_collect_c + dSv_player_map_c \
                + dSv_player_info_c + dSv_player_config_c + dSv_player_priest_c \
                + dSv_player_status_c_c + dSv_player_status_c_c + dSv_player_status_c_c + dSv_player_status_c_c + '4B'

numFields_dSv_player_c = numFields_dSv_player_status_a_c + numFields_dSv_player_status_b_c + numFields_dSv_player_return_place_c \
                + numFields_dSv_player_item_c + numFields_dSv_player_get_item_c + numFields_dSv_player_item_record_c \
                + numFields_dSv_player_item_max_c + numFields_dSv_player_bag_item_c + numFields_dSv_player_get_bag_item_c \
                + numFields_dSv_player_bag_item_record_c + numFields_dSv_player_collect_c + numFields_dSv_player_map_c \
                + numFields_dSv_player_info_c + numFields_dSv_player_config_c + numFields_dSv_player_priest_c \
                + numFields_dSv_player_status_c_c + numFields_dSv_player_status_c_c + numFields_dSv_player_status_c_c + numFields_dSv_player_status_c_c + 4

sizeof_dSv_player_c = 0x380

checkStructSize("dSv_player_c", dSv_player_c, sizeof_dSv_player_c)

def print_dSv_player_c(data):
    print('dSv_player_c')
    index = 0
    print_dSv_player_status_a_c(data[index:index + numFields_dSv_player_status_a_c])
    index += numFields_dSv_player_status_a_c
    print_dSv_player_status_b_c(data[index:index + numFields_dSv_player_status_b_c])
    index += numFields_dSv_player_status_b_c
    print_dSv_player_return_place_c(data[index:index + numFields_dSv_player_return_place_c])
    index += numFields_dSv_player_return_place_c
    print_dSv_player_item_c(data[index:index + numFields_dSv_player_item_c])
    index += numFields_dSv_player_item_c
    print_dSv_player_get_item_c(data[index:index + numFields_dSv_player_get_item_c])
    index += numFields_dSv_player_get_item_c
    print_dSv_player_item_record_c(data[index:index + numFields_dSv_player_item_record_c])
    index += numFields_dSv_player_item_record_c
    print_dSv_player_item_max_c(data[index:index + numFields_dSv_player_item_max_c])
    index += numFields_dSv_player_item_max_c
    print_dSv_player_bag_item_c(data[index:index + numFields_dSv_player_bag_item_c])
    index += numFields_dSv_player_bag_item_c
    print_dSv_player_get_bag_item_c(data[index:index + numFields_dSv_player_get_bag_item_c])
    index += numFields_dSv_player_get_bag_item_c
    print_dSv_player_bag_item_record_c(data[index:index + numFields_dSv_player_bag_item_record_c])
    index += numFields_dSv_player_bag_item_record_c
    print_dSv_player_collect_c(data[index:index + numFields_dSv_player_collect_c])
    index += numFields_dSv_player_collect_c
    print_dSv_player_map_c(data[index:index + numFields_dSv_player_map_c])
    index += numFields_dSv_player_map_c
    print_dSv_player_info_c(data[index:index + numFields_dSv_player_info_c])
    index += numFields_dSv_player_info_c
    print_dSv_player_config_c(data[index:index + numFields_dSv_player_config_c])
    index += numFields_dSv_player_config_c
    print_dSv_player_priest_c(data[index:index + numFields_dSv_player_priest_c])
    index += numFields_dSv_player_priest_c
    for i in range(0, 4):
        print_dSv_player_status_c_c(data[index:index + numFields_dSv_player_status_c_c])
        index += numFields_dSv_player_status_c_c
    print(f'padding:\t{data[index:index+4]}')
    index += 4
    print('\n\n')


dSv_memory_c = dSv_memBit_c
numFields_dSv_memory_c = numFields_dSv_memBit_c
sizeof_dSv_memory_c = 0x24

checkStructSize("dSv_memory_c", dSv_memory_c, sizeof_dSv_memory_c)

def print_dSv_memory_c(data):
    print_dSv_memBit_c(data)


dSv_ocean_c = '50H'
numFields_dSv_ocean_c = 50
sizeof_dSv_ocean_c = 0x64

checkStructSize("dSv_ocean_c", dSv_ocean_c, sizeof_dSv_ocean_c)

def print_dSv_ocean_c(data):
    print('dSv_ocean_c')
    for i in range(0, numFields_dSv_ocean_c):
        print(f'Ocean Short {i}:\t{data[i]}')
    print('\n\n')


dSv_event_c = '256B'
numFields_dSv_event_c = 256
sizeof_dSv_event_c = 0x100

checkStructSize("dSv_event_c", dSv_event_c, sizeof_dSv_event_c)

def print_dSv_event_c(data):
    print('dSv_event_c')
    for i in range(0, numFields_dSv_event_c):
        print(f'Flag {i}:\t{data[i]}')
    print('\n\n')


dSv_save_c = '@' + dSv_player_c + cat_format_str(dSv_memory_c, stage_max) + dSv_ocean_c + dSv_event_c
numFields_dSv_save_c = numFields_dSv_player_c + stage_max * numFields_dSv_memory_c + numFields_dSv_ocean_c + numFields_dSv_event_c
sizeof_dSv_save_c = 0x724

checkStructSize("dSv_save_c", dSv_save_c, sizeof_dSv_save_c)

def print_dSv_save_c(qlog):
    print('dSv_save_c')
    index = 0
    print_dSv_player_c(qlog[index:index + numFields_dSv_player_c])
    index += numFields_dSv_player_c
    for i in range(0, stage_max):
        print_dSv_memory_c(qlog[index:index + numFields_dSv_memory_c])
        index += numFields_dSv_memory_c
    print_dSv_ocean_c(qlog[index:index + numFields_dSv_ocean_c])
    index += numFields_dSv_ocean_c
    print_dSv_event_c(qlog[index:index + numFields_dSv_event_c])


def main():
    with open('helmaroc_skip.bin', 'rb') as fp:
        qlog = struct.unpack(dSv_save_c, fp.read(sizeof_dSv_save_c))
    print_dSv_save_c(qlog)

if __name__ == "__main__":
    main()