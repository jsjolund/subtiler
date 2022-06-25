import multiprocessing as mp
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


def merge_by_id(poly_maps):
    merged_poly_map = {}
    for poly_map in poly_maps:
        for id, polygons in poly_map.items():
            if id in merged_poly_map:
                merged_poly_map[id].extend(polygons)
            else:
                merged_poly_map[id] = polygons
    return merged_poly_map


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
    return merge_by_id(poly_maps)


def scale_tile(base_tile, image_size):
    # Center tiles in image and scale to max
    minmax = base_tile.get_boundingbox()
    xscl = image_size[0] / abs(minmax[1][0] - minmax[0][0])
    yscl = image_size[1] / abs(minmax[1][1] - minmax[0][1])
    scl = min(xscl, yscl)
    tx = image_size[0]/2 - (minmax[0][0] + minmax[1][0])*scl/2
    ty = image_size[1]/2 - (minmax[0][1] + minmax[1][1])*scl/2
    return base_tile.cpy().tra(tx, ty).scl(scl).push()


def zoom_tile(base_tile, image_size, focus):
    # Focus on point and scale (x, y, z). (0, 0, 1) is center of image, no scale.
    # x and y are between -1 and 1
    scl = focus[2]
    tx = (1/2 - 1/2*scl - focus[0]/2*scl)*image_size[0]
    ty = (1/2 - 1/2*scl + focus[1]/2*scl)*image_size[1]
    return base_tile.cpy().tra(tx, ty).scl(scl).push()


def draw_image(image_name, image_size, css, base_tile, substitutions, iterations, focus=(0, 0, 1)):
    base_tile = scale_tile(base_tile, image_size)
    base_tile = zoom_tile(base_tile, image_size, focus)
    poly_map = process(base_tile, substitutions, iterations, image_size)

    image = svgwrite.Drawing(image_name, size=image_size)
    image.embed_stylesheet(css)
    for id, polygons in poly_map.items():
        group = image.add(image.g(id=id))
        for polygon in polygons:
            group.add(polygon)
    return image


def draw_schematic(image_name, image_size, css, tiles, substitutions):
    image = svgwrite.Drawing(image_name, size=image_size)
    image.embed_stylesheet(css)

    poly_maps = []
    dy = 0
    for i in range(0, len(tiles)):
        base_tile = tiles[i]
        scl00 = 0.5
        scl0 = image_size[0]*base_tile.scale*scl00
        scl1 = image_size[0]*scl00

        tile = base_tile.cpy()
        tile = scale_tile(tile.cpy(), (scl1, scl1))
        tileheight = tile.get_boundingbox()[1][1]-tile.get_boundingbox()[0][1]
        tile = scale_tile(tile.cpy(), (scl1, tileheight))
        tile = tile.tra(150, dy).push()
        poly_maps.append(process(tile, substitutions, 1, image_size))

        tile = base_tile.cpy()
        tile = scale_tile(tile, (scl0, scl0))
        th = tile.get_boundingbox()[0][1]
        th2 = (tile.get_boundingbox()[1][1]-tile.get_boundingbox()[0][1])/2
        tile = tile.tra(0, dy-th-th2+tileheight/2).push()
        poly_maps.append(process(tile, substitutions, 0, image_size))

        a0 = (80, dy+tileheight/2)
        a1 = (130, dy+tileheight/2)
        image.add(image.polyline([a0, a1], stroke='black', stroke_width=2))
        head = [a1, (a1[0], a1[1]+4), (a1[0]+10, a1[1]), (a1[0], a1[1]-4)]
        image.add(image.polygon(head, fill='black'))

        dy += tileheight+10

    for id, polygons in merge_by_id(poly_maps).items():
        group = image.add(image.g(id=id))
        for polygon in polygons:
            group.add(polygon)

    image['height'] = dy
    return image
