import random
from subtiler import draw_image, draw_schematic
import fold3
import fold4
import fold5
import fold5n
import fold6
import fold8

# def rcolor():
#     return "#"+''.join([random.choice('ABCDEF0123456789') for _ in range(6)])
# rcss = f"""
# * {{
#   stroke: black;
#   stroke-width: 0.5px;
# }}
# #T1 {{
#   fill: {rcolor()};
# }}
# #T2 {{
#   fill: {rcolor()};
# }}
# #T3 {{
#   fill: {rcolor()};
# }}
# #T4 {{
#   fill: {rcolor()};
# }}
# #T5 {{
#   fill: {rcolor()};
# }}
# #T6 {{
#   fill: {rcolor()};
# }}
# #T7 {{
#   fill: {rcolor()};
# }}
# """
# print(rcss)

################################################################################

image_size = (600, 600)
schematic_width = (300, 2000)
################################################################################

base_tile = fold3.T1
substitutions = fold3.substitutions
iterations = 6
image_name = 'svg/fold3.svg'
schematic_name = 'svg/fold3_schematic.svg'
css = """
* {
  stroke: black;
  stroke-width: 0.5px;
}
#T1 {
  fill: #E8D050;
}
#T2 {
  fill: #DE105B;
}
"""
draw_image(image_name, image_size, css, base_tile,
           substitutions, iterations, focus=(0, 0, 8)).save()
draw_schematic(schematic_name, schematic_width, css,
               fold3.tiles, substitutions).save()

################################################################################

base_tile = fold4.T1
substitutions = fold4.substitutions
iterations = 5
image_name = 'svg/fold4.svg'
schematic_name = 'svg/fold4_schematic.svg'
css = """
* {
  stroke: black;
  stroke-width: 0.5px;
}
#T1 {
  fill: #D29CE5;
}
#T2 {
  fill: #2F6AEA;
}
"""
draw_image(image_name, image_size, css, base_tile,
           substitutions, iterations).save()
draw_schematic(schematic_name, schematic_width, css,
               fold4.tiles, substitutions).save()
################################################################################

base_tile = fold5.T1
substitutions = fold5.substitutions
iterations = 5
image_name = 'svg/fold5.svg'
schematic_name = 'svg/fold5_schematic.svg'
css = """
* {
  stroke: black;
  stroke-width: 0.5px;
}
#T1 {
  fill: #1f4384;
}
#T2 {
  fill: #1f4384;
}
#T3 {
  fill: #9d91a5;
}
#T4 {
  fill: #f87d93;
}
#T5 {
  fill: #ab8be2;
}
#T6 {
  fill: #ffffff;
}
#T7 {
  fill: #a0cb70;
}
"""
draw_image(image_name, image_size, css, base_tile, substitutions,
           iterations, focus=(-0.255, 0.460, 400)).save()
draw_schematic(schematic_name, schematic_width, css,
               fold5.tiles, substitutions).save()
################################################################################

base_tile = fold6.T1
substitutions = fold6.substitutions
iterations = 7
image_name = 'svg/fold6.svg'
schematic_name = 'svg/fold6_schematic.svg'
css = """
* {
  stroke: black;
  stroke-width: 0.5px;
}
#T1 {
  fill: #8CDCC0;
}
#T2 {
  fill: #704098;
}
#T3 {
  fill: #D8634D;
}
"""
draw_image(image_name, image_size, css, base_tile, substitutions,
           iterations, focus=(-0.25, 0.460, 800)).save()
draw_schematic(schematic_name, schematic_width, css,
               fold6.tiles, substitutions).save()

################################################################################

base_tile = fold8.T1
substitutions = fold8.substitutions
iterations = 5
image_name = 'svg/fold8.svg'
schematic_name = 'svg/fold8_schematic.svg'
css = """
* {
  stroke: black;
  stroke-width: 0.5px;
}
#T1 {
  fill: #000000;
}
#T2 {
  fill: #b59592;
}
#T3 {
  fill: #77545b;
}
#T4 {
  fill: #d91a25;
}
"""
draw_image(image_name, image_size, css, base_tile, substitutions,
           iterations, focus=(-0.27, 0.360, 250)).save()
draw_schematic(schematic_name, schematic_width, css,
               fold8.tiles, substitutions).save()

################################################################################

base_tile = fold5n.T1
substitutions = fold5n.substitutions
iterations = 10
image_name = 'svg/fold5n.svg'
schematic_name = 'svg/fold5n_schematic.svg'
css = """
* {
  stroke: black;
  stroke-width: 0.5px;
}
#T1 {
  fill: #562EE1;
}
#T2 {
  fill: #D7CEEA;
}
"""
draw_image(image_name, image_size, css, base_tile, substitutions,
           iterations, focus=(0, 0, 5)).save()
draw_schematic(schematic_name, schematic_width, css,
               fold5n.tiles, substitutions).save()
