import multiprocessing as mp
import time
import svgwrite
import itertools
from functools import partial


def overlap(amin, amax, bmin, bmax):
    return amin[0] < bmax[0] and amax[0] > bmin[0] and amax[1] > bmin[1] and amin[1] < bmax[1]


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def tiles_to_polygons(tiles):
    polygons = {}
    for t in tiles:
        polygon = svgwrite.shapes.Polygon(points=t.transform())
        id = t.name
        if id in polygons:
            polygons[id].append(polygon)
        else:
            polygons[id] = [polygon]
    return polygons


def substitute(input_tiles, substitutions, image_size):
    output_tiles = []
    for t in input_tiles:
        Ts = substitutions(t)
        for ts in Ts:
            new_t = ts.cpy().inherit_transform(t)
            aabb = new_t.get_boundingbox()
            if overlap(aabb[0], aabb[1], (0, 0), image_size):
                output_tiles.append(new_t)
    return output_tiles


def process(base_tile, substitutions, iterations, image_size):
    if iterations == 0:
        return tiles_to_polygons([base_tile])
    with mp.Pool(mp.cpu_count()) as pool:
        subs_tiles = [[base_tile]]
        for _ in range(0, iterations):
            subs_tiles_list = pool.map(partial(
                substitute, substitutions=substitutions, image_size=image_size), subs_tiles)
            subs_tiles = list(itertools.chain.from_iterable(subs_tiles_list))
            chunk_size = max(1, int(len(subs_tiles_list)/mp.cpu_count()))
            subs_tiles = list(chunks(subs_tiles, chunk_size))
        poly_maps = pool.map(tiles_to_polygons, subs_tiles)
    merged_poly_map = {}
    for poly_map in poly_maps:
        for id, polygons in poly_map.items():
            if id in merged_poly_map:
                merged_poly_map[id].extend(polygons)
            else:
                merged_poly_map[id] = polygons
    return merged_poly_map


def draw_image(image_name, image_size, css, base_tile, substitutions, iterations, focus=(0, 0, 1)):
    tic = time.perf_counter()

    image = svgwrite.Drawing(image_name, size=image_size)
    image.embed_stylesheet(css)

    # Center tiles in image and scale to max
    minmax = base_tile.get_boundingbox()
    xscl = image_size[0] / abs(minmax[1][0] - minmax[0][0])
    yscl = image_size[1] / abs(minmax[1][1] - minmax[0][1])
    scl = min(xscl, yscl)
    tx = image_size[0]/2 - (minmax[0][0] + minmax[1][0])*scl/2
    ty = image_size[1]/2 - (minmax[0][1] + minmax[1][1])*scl/2
    base_tile = base_tile.cpy().tra(tx, ty).scl(scl).push()

    # Focus on point and scale
    scl = focus[2]
    tx = (1/2 - 1/2*scl - focus[0]/2*scl)*image_size[0]
    ty = (1/2 - 1/2*scl + focus[1]/2*scl)*image_size[1]
    base_tile = base_tile.cpy().tra(tx, ty).scl(scl).push()

    poly_map = process(base_tile, substitutions, iterations, image_size)
    for id, polygons in poly_map.items():
        group = image.add(image.g(id=id))
        for polygon in polygons:
            group.add(polygon)

    print(f"substitute took {time.perf_counter() - tic:0.4f} seconds")
    return image
