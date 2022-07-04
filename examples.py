import random
from subtiler import draw_image, draw_schematic
from tilesets import fold3, fold4, fold5a, fold5b, fold6a, fold6b, fold6c, fold6d, fold7, fold8, penrose
from tile import Tile
from types import ModuleType


class Config:
    def __init__(self,
                 tileset: ModuleType,
                 base_tile: Tile,
                 focus: tuple[float, float, float],
                 iterations: int,
                 image_name: str,
                 schematic_name: str,
                 css: str):
        self.tileset = tileset
        self.base_tile = base_tile
        self.focus = focus
        self.iterations = iterations
        self.image_name = image_name
        self.schematic_name = schematic_name
        self.css = css
        self.image_size = (600, 600)
        self.schematic_width = (300, 2000)

    def random_hex(self) -> str:
        return "#"+''.join([random.choice('ABCDEF0123456789') for _ in range(6)])

    def random_color_css(self) -> str:
        css = f"* {{ stroke: black; stroke-width: 0.5px;}}"
        for i in range(0, len(self.tileset.tiles)):
            css += f"\n#T{i+1} {{ fill: {self.random_hex()}; }} "
        return css

    def draw(self, random_colors: bool = False) -> None:
        if random_colors:
            self.css = self.random_color_css()
            print(self.css)
        draw_image(self.image_name, self.image_size, self.css, self.base_tile,
                   self.tileset.map, self.iterations, self.focus).save()
        print(f'Wrote: {self.image_name}')
        tiles = list(self.tileset.map.keys())
        tiles.sort(key=lambda x: x.name)  # type: ignore
        draw_schematic(self.schematic_name, self.schematic_width, self.css,
                       tiles, self.tileset.map).save()
        print(f'Wrote: {self.schematic_name}')


conf3 = Config(
    tileset=fold3,
    base_tile=fold3.T1,
    focus=(0, 0, 8),
    iterations=6,
    image_name='svg/fold3.svg',
    schematic_name='svg/fold3_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px; }
#T1 { fill: #E8D050; }
#T2 { fill: #DE105B; }
""")

conf4 = Config(
    tileset=fold4,
    base_tile=fold4.T1,
    focus=(0, 0, 1),
    iterations=5,
    image_name='svg/fold4.svg',
    schematic_name='svg/fold4_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px; }
#T1 { fill: #D29CE5; }
#T2 { fill: #2F6AEA; }
""")

conf5a = Config(
    tileset=fold5a,
    base_tile=fold5a.T1,
    focus=(-0.255, 0.460, 400),
    iterations=5,
    image_name='svg/fold5a.svg',
    schematic_name='svg/fold5a_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px; }
#T1 { fill: #1f4384; }
#T2 { fill: #1f4384; }
#T3 { fill: #9d91a5; }
#T4 { fill: #f87d93; }
#T5 { fill: #ab8be2; }
#T6 { fill: #ffffff; }
#T7 { fill: #a0cb70; }
""")

conf6a = Config(
    tileset=fold6a,
    base_tile=fold6a.T1,
    focus=(-0.25, 0.460, 800),
    iterations=7,
    image_name='svg/fold6a.svg',
    schematic_name='svg/fold6a_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px; }
#T1 { fill: #8CDCC0; }
#T2 { fill: #704098; }
#T3 { fill: #D8634D; }""")

conf8 = Config(
    tileset=fold8,
    base_tile=fold8.T1,
    focus=(-0.27, 0.360, 250),
    iterations=5,
    image_name='svg/fold8.svg',
    schematic_name='svg/fold8_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px; }
#T1 { fill: #000000; }
#T2 { fill: #b59592; }
#T3 { fill: #77545b; }
#T4 { fill: #d91a25; }
""")

conf5b = Config(
    tileset=fold5b,
    base_tile=fold5b.T1,
    focus=(0, 0, 5),
    iterations=10,
    image_name='svg/fold5b.svg',
    schematic_name='svg/fold5b_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px; }
#T1 { fill: #562EE1; }
#T2 { fill: #D7CEEA; }
""")

conf6b = Config(
    tileset=fold6b,
    base_tile=fold6b.T1,
    focus=(0, 0, 12),
    iterations=10,
    image_name='svg/fold6b.svg',
    schematic_name='svg/fold6b_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px; }
#T1 { fill: #F5425E; }
#T2 { fill: #85BC54; }
#T3 { fill: #C6C7BC; }
""")

conf6c = Config(
    tileset=fold6c,
    base_tile=fold6c.T4,
    focus=(0, 0, 4),
    iterations=9,
    image_name='svg/fold6c.svg',
    schematic_name='svg/fold6c_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px; }
#T1 { fill: #3A82DC; }
#T2 { fill: #E2220E; }
#T3 { fill: #81E8D7; }
#T4 { fill: #972202; }
""")

conf6d = Config(
    tileset=fold6d,
    base_tile=fold6d.T6,
    focus=(0, 0, 2),
    iterations=7,
    image_name='svg/fold6d.svg',
    schematic_name='svg/fold6d_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px;}
#T1 { fill: #DB15B9; } 
#T2 { fill: #18C0EC; } 
#T3 { fill: #0D3262; } 
#T4 { fill: #2F5620; } 
#T5 { fill: #E8F5E1; } 
#T6 { fill: #4667AD; } 
""")

conf7 = Config(
    tileset=fold7,
    base_tile=fold7.T3,
    focus=(0, 0, 50),
    iterations=7,
    image_name='svg/fold7.svg',
    schematic_name='svg/fold7_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px; }
#T1 { fill: #41d2ba; }
#T2 { fill: #ffe777; }
#T3 { fill: #465b52; }
""")

confPenrose = Config(
    tileset=penrose,
    base_tile=penrose.C2,
    focus=(0, 0, 1),
    iterations=8,
    image_name='svg/penrose.svg',
    schematic_name='svg/penrose_schematic.svg',
    css="""
* { stroke: black; stroke-width: 0.5px; }
#T1 { fill: yellow; } 
#T2 { fill: red; } 
#T3 { fill: #FFFFFF; } 
#T4 { fill: #FFFFFF; } 
""")

conf3.draw()
conf4.draw()
conf5a.draw()
conf6a.draw()
conf8.draw()
conf5b.draw()
conf6b.draw()
conf6c.draw()
conf6d.draw()
conf7.draw()
confPenrose.draw()
