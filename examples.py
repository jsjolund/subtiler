import random
from subtiler import draw_image
import fold3
import fold4
import fold5
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

################################################################################

base_tile = fold3.T1
substitutions = fold3.substitutions
iterations = 6
image_name = 'svg/fold3.svg'
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
#T
"""
draw_image(image_name, image_size, css, base_tile,
           substitutions, iterations, focus=(0, 0, 8)).save()

################################################################################

base_tile = fold4.T1
substitutions = fold4.substitutions
iterations = 5
image_name = 'svg/fold4.svg'
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

################################################################################

base_tile = fold5.T1
substitutions = fold5.substitutions
iterations = 5
image_name = 'svg/fold5.svg'
css = """
* {
  stroke: black;
  stroke-width: 0.5px;
}
#T1 {
  fill: #204883;
}
#T2 {
  fill: #204883;
}
#T3 {
  fill: #808ca0;
}
#T4 {
  fill: #c67b90;
}
#T5 {
  fill: #8b87d5;
}
#T6 {
  fill: #cbedee;
}
#T7 {
  fill: #82bf72;
}
"""

draw_image(image_name, image_size, css, base_tile,
           substitutions, iterations, focus=(-0.255, 0.460, 400)).save()

################################################################################

base_tile = fold6.T1
substitutions = fold6.substitutions
iterations = 7
image_name = 'svg/fold6.svg'
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
draw_image(image_name, image_size, css, base_tile,
           substitutions, iterations, focus=(-0.25, 0.460, 800)).save()

################################################################################

base_tile = fold8.T1
substitutions = fold8.substitutions
iterations = 5
image_name = 'svg/fold8.svg'
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
draw_image(image_name, image_size, css, base_tile,
           substitutions, iterations, focus=(-0.27, 0.360, 250)).save()
