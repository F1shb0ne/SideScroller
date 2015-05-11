"""
This module describes how external resources (images, sfx, metadata, etc) are loaded and saved
"""

import src.res.Sprite


def load_sprite(filename):
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

    print "Loading sprite: " + filename

    with open('sprites/' + filename + '.spr', 'r') as f:

        for line in f:

            # Before moving on to the next line, do we have enough data to make up an AnimationRef object?
            if (animation_name is not None and
                    owner is not None and
                    file_url is not None and
                    frame_width is not None and
                    frame_height is not None and
                    center_x is not None and
                    center_y is not None and
                    frame is not None):

                # Store complete object
                sprites.append(src.res.Sprite.AnimationRef(animation_name,
                                                           owner,
                                                           file_url,
                                                           frame_width,
                                                           frame_height,
                                                           center_x,
                                                           center_y,
                                                           frame))

                print "  Merged: " + animation_name

                # Reset and move on
                animation_name = None
                owner = None
                file_url = None
                frame_width = None
                frame_height = None
                center_x = None
                center_y = None
                frame = None

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
