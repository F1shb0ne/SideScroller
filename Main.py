import pyglet

# Global variables
player_posx = 0
player_posy = 0

player_step_anim_delay = 0
player_step_anim_index = 0

framelimit = 100
frame = 0

# Initialize window
window = pyglet.window.Window()

# Load external game resources
sprite_link_stand = pyglet.resource.image('gfx/link-stand.png')
sprite_link_walk1 = pyglet.resource.image('gfx/link-walk1.png')
sprite_link_walk2 = pyglet.resource.image('gfx/link-walk2.png')
sprite_link_walk3 = pyglet.resource.image('gfx/link-walk3.png')



"""
This routine is responsible for:
 - determining where the character will be
 - how fast the character is going
 - which animation frame it will advance to
"""
def game_logic(self):
    global frame
    global player_posx, player_posy
    global player_step_anim_delay, player_step_anim_index
    
    frame += 1
    if frame < framelimit:

        player_posx += 2
        player_step_anim_delay += 1
        
        # delay between changing animation frames
        if player_step_anim_delay == 3:
            player_step_anim_delay = 0
            player_step_anim_index += 1
            
            # there are three step animation frames available
            if player_step_anim_index > 2:
                player_step_anim_index = 0
    else:
        player_step_anim_index = 3
        
@window.event
def on_draw():
    global player_posx
    global player_posy
    window.clear()
    
    # blit sprite to screen according to which animation frame is being used
    if player_step_anim_index == 0:
        sprite_link_walk1.blit(player_posx, player_posy)
    if player_step_anim_index == 1:
        sprite_link_walk2.blit(player_posx, player_posy)
    if player_step_anim_index == 2:
        sprite_link_walk3.blit(player_posx, player_posy)
    if player_step_anim_index == 3:
        sprite_link_stand.blit(player_posx, player_posy)



# Main module code starts here

window.set_vsync(False)

# register game logic routine
pyglet.clock.schedule_interval(game_logic, 0.05)

pyglet.app.run()
