# tww-gz Save Tools
This git repository contains all the scripts needed to make practice saves for tww-gz. This README will serve as a guide on how to turn in-game saves to saves that can be added to tww-gz.

## GCMM
Firstly, all the saves made in-game need to be copied from your Wii to a USB stick or SD card that can be moved to your computer.  This can be achieved by using GCMM on a HomeBrewed Wii. When moving the gci files to your computer, I recommend giving them a name that keeps track of which save file is where (like `trials--barrier--ff2.gci` for example).  This README will assume the reader already has a Homebrewed Wii and knows how to install and use GCMM.

Once all the wanted gci files are on your computer, proceed to the next step.

## GCI to Quest Logs
Just to keep things simple, a gci file contains three savefiles.  We need to extract the data from these savefiles and put them into their own files.  This is where the `gci2qlogs.py` script comes in.  This script takes a gci file as input and outputs three .bin files: `qlog1.bin`, `qlog2.bin`, `qlog3.bin`

`python3 gci2qlogs.py <gci file>`

Once you have the three bin files, rename them to match their contents (like `trials.bin`, `barrier.bin`, `ff2.bin` for example) because these are the files tww-gz will load when the user picks a practice save.  Do not make the filenames too long because there is a limit to the length of the filename.

Repeat this process for all of your gci files and place all of the bin files in their own folder in the res/save_files folder.

## Quest Log Dumper (Optional)
This is not at all required to add new saves to tww-gz and is more for debugging problems or if anyone's just interested in seeing what a save file looks like.  The Quest Log Dumper script takes a bin file made by `gci2qlogs.py` and outputs its contents in plain-text.

`python3 qlog_dumper.py > <output file>`

This script is still a work in progress.  There are a couple misalignments, so the contents of the text file do not completely match up with the actual savefile, and it reads the data in the bin file as little-endian (what modern PCs use) instead of big-endian (what the GameCube uses).  If you don't know what this means, don't worry:  just know a lot of the numbers in the text file will be wrong (if Link has 12 health, this script will print "12" as "3072").  Also, you have to manually edit the script to pick the bin file you want to look at.

## Category Maker
At this point, you should have a folder inside res/save_files/ containing a bin file for each save you want for your category.  Now, we need an additional bin file to tie them all together and add additional configurations for each practice save.  The `category_maker.py` script will make this bin file, but it currently requires the user to add some Python code for their new category (if there's a high enough demand, maybe someone can make a gui to remove the programming requirement).

For now, you will have to manually edit `category_maker.py` to change the name of the category bin file to the name of the category you want to add.  You also have to update the for loop with the correct number of bin files and replace the call to `create_any_no_mss_savefiles()` with a similar function that you have to write (here's where the programming skills come in, but it won't be hard, I promise).  Use `any_no_mss.py` as a basis for your new category.  You pretty much need to make a list of `PracticeSaveInfo` objects where each object corresponds to a bin file from your category.  The order of this list needs to match the order you wants the practice saves to be listed in tww-gz.

The save manager in tww-gz is still very much a work in progress, because a big thing you cannot do with it yet is override actor information (like an actor's spawn location).  Most of the content in a `PracticeSaveInfo` object pertains to overriding data for spawn information for Link and the camera, so this content is not currently used (the camera not being supported is unrelated to the lack of actor support).  The only information currently being used from `PracticeSaveInfo` is the name of the bin file that gets loaded, so it is up to you to decide if you want to make everything zero (except for bin filename) and edit it later once save manager is updated, or add the overriden data now so someone doesn't have to update it later once the save manager is in a more complete state.

Here is information on each field in `PracticeSaveInfo`, all of which you need to define for each save:
- requirements
    - This currently isn't used by tww-gz, but it will eventually specify whether or not you want to override Link's default spawn location and angle, as well as the camera's default spawn position and target.
    - Possible Values:
        - 0:  Keep Link and the camera default
        - 1:  Override Link's spawn position and angle
        - 2:  Override Link's spawn position and the camera's spawn position and target
- p0
    - This is always a list of size one containing a single zero.
    - I made this script before realizing this is just padding, so eventually, I will update `PractiveSaveInfo` to automatically include this padding.
- angle
    - If Link's spawn angle is overriden, this value will be Link's new spawn angle
- position
    - If Link's position is overriden, this `Vector` will be Link's new spawn position
- cam_pos
    - If the camera's position is overriden, this `Vector` will be the camera's new spawn position
- cam_target
    - If the camera's target is overriden, this `Vector` will be the camera's new spawn target
- counter
    - Just set it to 0
    - I copied this field from tpgz.  They don't seem to use it ever, but my guess is it was once used to determine how many frames to wait after starting to load the save data before overriding Link's and/or the camera's spawn info.  If this is what the counter was for, it is useless now that tpgz properly waits for the save data to be loaded before overriding the spawn info (as of tpgz version 0.6.0b?).  Again, this is just a guess, so ask someone from the tpgz development team about this if you want to know it's real purpose.
- filename
    - The name of the bin file to associate with this `PracticeSaveInfo` object
- p1
    - This is always a list of size four containing four zeroes.
    - I made this script before realizing this is just padding, so eventually, I will update `PractiveSaveInfo` to automatically include this padding.

Once all of that's done, run the script like so:

`python3 category_maker.py`

This should output a bin file with the name you gave it in `category_maker.py`.  Put this file in res/save_files

## Final Step
If you now try to patch your legally obtained iso of The Wind Waker, it will fail because the patcher cannot find all the bin files you made. You will need to edit `RomHack-template.toml` in order for the patcher to recognize your new bin files. Just use what is currently listed under `#save_files` as a guide, but all you need to do is add a line, like the line below, for each bin file you added:

`"twwgz/save_files/<category>/<filename>.bin" = "res/save_files/<category>/<filename>.bin"`

This also includes the category bin file:

`"twwgz/save_files/<category>.bin" = "res/save_files/<category>.bin"`

## Potential Problems
- Loading a practice save behaves like an area reload

The bin file corresponding to that practice save is not getting loaded, so tww-gz just reloads the current area instead.  Make sure the filename of the bin file is not too long.

- The patcher cannot find a bin file

Make sure to add that bin file to `RomHack-template.toml` as described by "Final Step"

- The game's layer when I made the save does not match the layer when I load it

The layer is not part of the save file data, so you have to manually override it using specials.  Look at `save_specials.cpp` and `any_no_mss_saves_menu.cpp` to get an idea for how to do this.  Specials can be used to override the layer as well as the entrance id, room number, stage, and anything else really (except for actor spawn location, for now).

- Sometimes, Link spawns out of bounds when I load a practice save

If you reload an area by jumping in lava and then load a practice save, Link will spawn in with the getup animation as if he had just fallen in lava.  For example, if you load a save that puts Link on the pirate ship, he will clip out of bounds and spawn in the water.  His swimming animation prevents his getup animation from finishing, so you will be stuck under the pirate ship.  The only way to escape is to load a different practice save or reset the game.

- I want to edit the contents of a bin file before I put it in tww-gz.  How should I go about doing this?

Don't edit any bin files.  Just use specials to override data inside of them.  See `save_specials.cpp` and `any_no_mss_saves_menu.cpp` to get an idea for how to do this.

- The special I made to override an actor's spawn position isn't working

Currently, an actor's spawn position cannot be overriden in tww-gz.  My guess is it cannot get overriden until the load sequence ends, but injecting code at the end of a load sequence is not supported yet.