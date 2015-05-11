"""
This module describes how external resources (images, sfx, metadata, etc) are loaded and saved
"""
import pygame
import pygame.locals
import subprocess
import src.res.Sprite


"""
The GameResources object is the object that will hold references to all graphic, animation, sound and map data.
"""


class GameResources:
    def __init__(self):
        self.sprite = {}
        self.frame = {}

        self.load_sprite_data()
        self.build_frames()

    def load_sprite_data(self):
        sprite_file_list = get_sprite_file_list()
        for sprite_file in sprite_file_list:
            sprite_array = load_sprite_file(sprite_file)
            for entry in sprite_array:
                name = entry.owner + ":" + entry.name  # eg. "mario:walk_right"
                self.sprite[name] = entry

    # Build the frame dictionary. Using self.sprite, this will build associations for "mario:walk_right:1"
    # which will point to an image object containing the first frame of mario walking right.

    def build_frames(self):
        for aref in self.sprite:
            framecount = 0
            width = self.sprite[aref].frame_width
            height = self.sprite[aref].frame_height
            source_image = pygame.image.load("./gfx/" + self.sprite[aref].url + ".png")

            for frame_element in self.sprite[aref].frames:
                framecount += 1
                name = aref + ":" + str(framecount)
                print "Loading: " + name
                # Load the sub image and flip if necessary
                self.frame[name] = pygame.transform.flip(source_image.subsurface(
                                                         (frame_element.offset_x,
                                                          frame_element.offset_y,
                                                          width,
                                                          height)),
                                                         frame_element.flip_horiz,
                                                         frame_element.flip_vert)


# Operating system dependant method of searching the ./sprite sub-folder for sprite files
# and returning a list of strings of each url
def get_sprite_file_list():
    sprite_file_list = []
    # Get a list of all the sprite files in the sprites sub directory.
    raw_list = subprocess.Popen(["find", "./sprites", "-name", "*.spr"], stdout=subprocess.PIPE).stdout.readlines()
    for line in raw_list:
        sprite_file_list.append(str.rstrip(line))

    return sprite_file_list


# Load the contents of a sprite file which may contain one or more AnimationRef objects
# Returns a list of AnimationRef objects
def load_sprite_file(filename):
    supported_version = 1
    correct_version = False
    inside_anim_def = False

    # Contents of each AnimationRef object
    animation_name = None
    owner = None
    file_url = None
    frame_width = None
    frame_height = None
    center_x = None
    center_y = None
    frame = None

    # List of AnimationRef objects to be returned
    sprites = []

    with open(filename, 'r') as f:

        for line in f:

            # Before moving on to the next line, do we have enough data to make up an AnimationRef object?

            # remove trailing newline
            line = str.rstrip(line)

            tokens = line.split(' ')
            if tokens[0] == 'version':
                if tokens[1] == 'sprite' and int(tokens[2]) == supported_version:
                    correct_version = True
                    continue

            if correct_version:
                if tokens[0] == 'animation':
                    inside_anim_def = True
                    animation_name = tokens[1]
                    continue

                if tokens[0] == 'end_animation':
                    # finish AnimationRef object
                    inside_anim_def = False
                    if (animation_name is not None and
                            owner is not None and
                            file_url is not None and
                            frame_width is not None and
                            frame_height is not None and
                            center_x is not None and
                            center_y is not None and
                            frame is not None and
                            inside_anim_def is False):

                        # Store complete object
                        print "Storing " + owner + ":" + animation_name
                        sprites.append(src.res.Sprite.AnimationRef(animation_name,
                                                                   owner,
                                                                   file_url,
                                                                   frame_width,
                                                                   frame_height,
                                                                   center_x,
                                                                   center_y,
                                                                   frame))

                        # Reset and move on
                        animation_name = None
                        owner = None
                        file_url = None
                        frame_width = None
                        frame_height = None
                        center_x = None
                        center_y = None
                        frame = None

                    continue

                if inside_anim_def:
                    if tokens[0] == 'owner':
                        owner = tokens[1]
                        continue

                    if tokens[0] == 'url':
                        file_url = tokens[1]
                        continue

                    if tokens[0] == 'dimensions':
                        frame_width = int(tokens[1])
                        frame_height = int(tokens[2])
                        continue

                    if tokens[0] == 'center':
                        center_x = tokens[1]
                        center_y = tokens[2]
                        continue

                    if tokens[0] == 'frame':
                        if frame is None:
                            frame = []
                        frame.append(src.res.Sprite.AnimationFrame(tokens[1], tokens[2], tokens[3], tokens[4]))
                        continue

    return sprites
