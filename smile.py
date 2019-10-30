import arcade

sw = 600
sh = 600

arcade.open_window(sw, sh, "example")

arcade.set_background_color(arcade.color.BLACK)


#Start the render process. This must be done before any drawing commands.
arcade.start_render()


#draw a head
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x,y,radius, arcade.color.BANANA_YELLOW)

#draw left eyes
x = 375
y = 350
radius = 50
width = 35
height = 60
s_num = 300
arcade.arcade.draw_ellipse_filled(x,y,width, height, arcade.color.BLACK ,0,s_num)

#draw right eyes
x = 225
y = 350
radius = 50
width = 35
height = 60
s_num = 300
arcade.arcade.draw_ellipse_filled(x,y,width, height, arcade.color.BLACK ,0,s_num)

#draw mouth 
start_x = 220
start_y = 220
end_y = 380
arcade.draw_parabola_outline(start_x, start_y, end_y, 3,  arcade.color.BLACK, 7, 180 )

arcade.finish_render()

arcade.run()