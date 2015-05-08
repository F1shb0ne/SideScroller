""" Sprite classes """

""" Animation reference object

This object is a reference for a sequence of frames that make up an animation for an actor.
It will refer to a single PNG file containing the frames the animation will use.
There will be meta data to define its bounding box / dimensions and where the center point is.
Each AnimationRef object will contain an array of AnimationFrame objects

These objects will be used to organize the sprites used to animate an action for a specific actor by name.
For instance, Mario and Luigi have different sprites for the animation used to make them appear to be walking.
Mario and Luigi will have their own actor objects. Actor objects will have a hash of actions. Both actors are similar
in that they should be able to walk left or right, so they will have animation references that will be of the same name,
but point to different AnimationRef objects for their own sprite image data.
"""


class AnimationRef:
    def __init__(self, name, url, frame_width, frame_height, center_x, center_y, frames):

        self.name = name
        self.url = url
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.center_x = center_x
        self.center_y = center_y

        # This holds a sequential list of AnimationFrame objects
        self.frames = frames


""" Animation frame object
Contains the frame position in an image for a specific frame in an object's animation state.
"""


class AnimationFrame:

    def __init__(self, offset_x, offset_y, frame_delay, flip):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.frame_delay = int(frame_delay)

        self.flip_vert = False
        self.flip_horiz = False

        if flip == 'v':
            self.flip_vert = True
        if flip == 'h':
            self.flip_horiz = True
        if flip == 'vh' or flip == 'hv':
            self.flip_vert = True
            self.flip_horiz = True
