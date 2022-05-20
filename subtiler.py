import multiprocessing as mp
import time
import svgwrite
from functools import partial
from tile import Tile
import threefold
import fourfold
import eightfold


def tiles_to_polygons(tiles):
    if type(tiles) is Tile:
        tiles = [tiles]
    polygons = {}
    for t in tiles:
        polygon = svgwrite.shapes.Polygon(points=t.transform())
        if t.name in polygons:
            polygons[t.name].append(polygon)
        else:
            polygons[t.name] = [polygon]
    return polygons


def substitute(input_tiles, substitutions, iterations):
    subs_tiles = [input_tiles]
    for _ in range(0, iterations):
        Ti = []
        for t in subs_tiles:
            Ts = substitutions(t)
            for ts in Ts:
                Ti.append(ts.cpy().inherit_transform(t))
        subs_tiles = Ti
    return tiles_to_polygons(subs_tiles)


def draw_image(image_name, image_size, css, base_tile, substitutions, iterations):
    tic = time.perf_counter()

    image = svgwrite.Drawing(image_name, size=image_size)
    image.embed_stylesheet(css)

    minmax = base_tile.get_boundingbox()
    xscl = image_size[0] / abs(minmax[1][0] - minmax[0][0])
    yscl = image_size[1] / abs(minmax[1][1] - minmax[0][1])
    scl = min(xscl, yscl)
    tx = image_size[0]/2 - (minmax[0][0] + minmax[1][0])*scl/2
    ty = image_size[1]/2 - (minmax[0][1] + minmax[1][1])*scl/2
    base_tile = base_tile.cpy().tra(tx, ty).scl(scl).push()

    with mp.Pool(mp.cpu_count()) as pool:
        poly_maps = pool.map(partial(
            substitute, substitutions=substitutions, iterations=iterations), [base_tile])
        time.sleep(0.5)
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

    print(f"substitute took {time.perf_counter() - tic:0.4f} seconds")
    return image


image_size = (600, 600)
css = """
#T1, #T2, #T3, #T4 {
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
""".replace('\n', '')

base_tile = threefold.T1
substitutions = threefold.substitutions
iterations = 4
image_name = 'threefold.svg'
image = draw_image(image_name, image_size, css,
                   base_tile, substitutions, iterations)
image.save()

base_tile = fourfold.T1
substitutions = fourfold.substitutions
iterations = 5
image_name = 'fourfold.svg'
image = draw_image(image_name, image_size, css,
                   base_tile, substitutions, iterations)
image.save()

base_tile = eightfold.T1
substitutions = eightfold.substitutions
iterations = 2
image_name = 'eightfold.svg'
image = draw_image(image_name, image_size, css,
                   base_tile, substitutions, iterations)
image.save()
