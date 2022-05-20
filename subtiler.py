import multiprocessing as mp
import time
import svgwrite
from functools import partial
from tile import Tile
from eightfold import T1, substitutions

def tiles_to_polygons(tiles, image_size):
    if type(tiles) is Tile:
        tiles = [tiles]
    polygons = {}
    for t in tiles:
        # move & scale to fit document
        scl = min(image_size[0], image_size[1])*0.4
        t.tra(image_size[0]/2, image_size[1]/2).scl(scl).push()  
        polygon = svgwrite.shapes.Polygon(points=t.transform())
        if t.name in polygons:
            polygons[t.name].append(polygon)
        else:
            polygons[t.name] = [polygon]
    return polygons


def substitute(input_tiles, iterations, image_size):
    subs_tiles = [input_tiles]
    for _ in range(0, iterations):
        Ti = []
        for t in subs_tiles:
            Ts = substitutions(t)
            for ts in Ts:
                Ti.append(ts.cpy().inherit_transform(t))
        subs_tiles = Ti
    return tiles_to_polygons(subs_tiles, image_size)


def draw_image(image_name, image_size, css, base_tile, iterations):
    image = svgwrite.Drawing(image_name, size=image_size)
    image.embed_stylesheet(css)
    with mp.Pool(mp.cpu_count()) as pool:
        poly_maps = pool.map(partial(substitute, iterations=iterations, image_size=image_size), [base_tile])
        merged_poly_map = {}
        for poly_map in poly_maps:
            for id, polygons in poly_map.items():
                if id in merged_poly_map:
                    merged_poly_map[id].extend(polygons)
                else:
                    merged_poly_map[id] = polygons
        for id, polygons in merged_poly_map.items():
            group = image.add(image.g(id=id))
            for polygon in polygons:
                group.add(polygon)
    return image


base_tile = T1
iterations = 2
image_name = 'test.svg'
image_size = (600, 600)
css = """
#T1, #T2, #T3, #T4 {
  stroke: black;
  stroke-width: 0.05px;
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
""".replace('\n', '')

tic = time.perf_counter()
image = draw_image(image_name, image_size, css, base_tile, iterations)
print(f"substitute took {time.perf_counter() - tic:0.4f} seconds")

tic = time.perf_counter()
image.save()
print(f"save took {time.perf_counter() - tic:0.4f} seconds")
