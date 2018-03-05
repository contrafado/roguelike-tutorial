import libtcodpy as libtcod 

def render_all(con, entities, screen_width, screen_height):
    #draw all entities in the list
	for entity in entities:
	    draw_entity(con, entity)
		
def clear_all(con, entities):
    for entity in entities: 
        clear_entity(con, entity)

def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)
	
def clear_entity(con, entity):
    #erase the character that represents the object
	libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)