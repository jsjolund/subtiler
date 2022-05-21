import multiprocessing as mp
import time
import svgwrite
from functools import partial
from tile import Tile


def tiles_to_polygons(tiles):
    if type(tiles) is Tile:
        tiles = [tiles]
    polygons = {}
    for t in tiles:
        polygon = svgwrite.shapes.Polygon(points=t.transform())
        title = t.name
        if t.user_data:
            title = f'{t.name}-{t.user_data}'
        if title in polygons:
            polygons[title].append(polygon)
        else:
            polygons[title] = [polygon]
    return polygons


def substitute(tile, substitutions, iterations):
    tiles = [tile]
    for _ in range(0, iterations):
        Ti = []
        for t in tiles:
            Ts = substitutions(t)
            for ts in Ts:
                new_t = ts.cpy().inherit_transform(t)
                new_t.user_data = tile.user_data
                Ti.append(new_t)
        tiles = Ti
    return tiles


def process(tile, substitutions, iterations):
    subs_tiles = substitute(tile, substitutions, iterations)
    polygons = tiles_to_polygons(subs_tiles)
    return polygons


def draw_image(image_name, image_size, css, base_tile, substitutions, iterations, use_depth=False):
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

    if iterations > 0:
        subs_tiles = substitute(base_tile, substitutions, 1)
        if use_depth: # TODO: better color support
            for i in range(0, len(subs_tiles)):
                subs_tiles[i].user_data = f'C{i+1}'
        iterations -= 1
    else:
        subs_tiles = [base_tile]

    with mp.Pool(mp.cpu_count()) as pool:
        poly_maps = pool.map(partial(
            process, substitutions=substitutions, iterations=iterations), subs_tiles)
        merged_poly_map = {}
        for poly_map in poly_maps:
            for title, polygons in poly_map.items():
                if title in merged_poly_map:
                    merged_poly_map[title].extend(polygons)
                else:
                    merged_poly_map[title] = polygons
        for title, polygons in merged_poly_map.items():
            split = title.split()
            id = split[0]
            class_ = 'none'
            if len(split) > 1:
                class_ = split[1]
            group = image.add(image.g(id=id, class_=class_))
            for polygon in polygons:
                group.add(polygon)

    print(f"substitute took {time.perf_counter() - tic:0.4f} seconds")
    return image
