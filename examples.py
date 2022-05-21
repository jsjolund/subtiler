from subtiler import draw_image
import fold3
import fold4
import fold6
import fold8


image_size = (600, 600)

base_tile = fold3.T1
substitutions = fold3.substitutions
iterations = 4
image_name = 'svg/fold3.svg'
css = """
* {
  stroke: black;
  stroke-width: 0.5px;
}
#T1-C1 {
  fill: #00FF88;
}
#T2-C1 {
  fill: #0037FF;
}
#T1-C2 {
  fill: #00F7FF;
}
#T2-C2 {
  fill: #00B7FF;
}
#T1-C3 {
  fill: #00FFC8;
}
#T2-C3 {
  fill: #0077FF;
}
#T1-C4 {
  fill: #0AFF0D;
}
#T2-C4 {
  fill: #0014A8;
}
"""
draw_image(image_name, image_size, css, base_tile,
           substitutions, iterations, True).save()


base_tile = fold4.T1
substitutions = fold4.substitutions
iterations = 5
image_name = 'svg/fold4.svg'
css = """
* {
  stroke-width: 1px;
}
#T1-C1 {
  fill: #0CC0E4;
  stroke: black;
}
#T2-C1 {
  fill: #300CE4;
  stroke: black;
}
#T1-C2 {
  fill: #660CE4;
  stroke: black;
}
#T2-C2 {
  fill: #0C8AE4;
  stroke: black;
}
#T1-C3 {
  fill: #0C54E4;
  stroke: black;
}
#T2-C3 {
  fill: #0C1EE4;
  stroke: black;
}
#T1-C4 {
  fill: #9855F6;
  stroke: black;
}
#T2-C4 {
  fill: #558BF6;
  stroke: black;
}
#T1-C5 {
  fill: white;
  stroke: black;
}
#T2-C5 {
  fill: black;
  stroke: white;
}
"""
draw_image(image_name, image_size, css, base_tile,
           substitutions, iterations, True).save()

base_tile = fold6.T1
substitutions = fold6.substitutions
iterations = 2
image_name = 'svg/fold6.svg'
css = """
* {
  stroke: black;
  stroke-width: 0.5px;
}
#T1 {
  stroke: #8F0000;
  fill: #FE52F0;
}
#T2 {
  fill: #D686FE;
}
#T3 {
  fill: #B752FE;
}
#T4 {
  fill: #FE6152;
  stroke-width: 0px;
}
"""
draw_image(image_name, image_size, css, base_tile,
           substitutions, iterations).save()


base_tile = fold8.T1
substitutions = fold8.substitutions
iterations = 2
image_name = 'svg/fold8.svg'
css = """
* {
  stroke: black;
  stroke-width: 0.5px;
}
#T1 {
  stroke: #8F0000;
  fill: #FE52F0;
}
#T2 {
  fill: #D686FE;
}
#T3 {
  fill: #B752FE;
}
#T4 {
  fill: #FE6152;
  stroke-width: 0px;
}
"""
draw_image(image_name, image_size, css, base_tile,
           substitutions, iterations).save()
