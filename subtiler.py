import multiprocessing as mp
import itertools
from functools import partial
from tile import Tile, aabb
from typing import Any, Generator, Dict, Callable, Optional
from svgwrite import Drawing         # type: ignore
from svgwrite.shapes import Polygon  # type: ignore

Vec2 = tuple[float, float]
Vec2i = tuple[int, int]
Vec2Pair = tuple[Vec2, Vec2]
PolygonIdMap = Dict[str, list[Polygon]]


def overlap(amin: Vec2,
            amax: Vec2,
            bmin: Vec2,
            bmax: Vec2) -> bool:
    return amin[0] < bmax[0] and amax[0] > bmin[0] and amax[1] > bmin[1] and amin[1] < bmax[1]


def chunks(lst: list[Any], n: int) -> Generator[list[Any], None, None]:
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def tiles_to_polygons(tiles: list[Tile]) -> PolygonIdMap:
    polygons: PolygonIdMap = {}
    for t in tiles:
        polygon = Polygon(points=t.transform())
        id = t.name
        if id in polygons:
            polygons[id].append(polygon)
        else:
            polygons[id] = [polygon]
    return polygons


def substitute(input_tiles: list[Tile],
               substitutions: Dict[Tile, list[Tile]],
               image_size: Vec2i
               ) -> list[Tile]:
    output_tiles = []
    for t in input_tiles:
        Ts = substitutions[t]
        for ts in Ts:
            new_t = ts.cpy().inherit_transform(t)
            aabb = new_t.aabb()
            if overlap(aabb[0], aabb[1], (0, 0), image_size):
                output_tiles.append(new_t)
    return output_tiles


def merge_by_id(poly_maps: list[PolygonIdMap]) -> PolygonIdMap:
    merged_poly_map: PolygonIdMap = {}
    for poly_map in poly_maps:
        for id, polygons in poly_map.items():
            if id in merged_poly_map:
                merged_poly_map[id].extend(polygons)
            else:
                merged_poly_map[id] = polygons
    return merged_poly_map


def process(base_tile: Tile,
            substitutions: Dict[Tile, list[Tile]],
            iterations: int,
            image_size: Vec2i) -> PolygonIdMap:
    if iterations == 0:
        return tiles_to_polygons([base_tile])
    with mp.Pool(mp.cpu_count()) as pool:
        input_tiles: list[list[Tile]] = [[base_tile]]
        for _ in range(0, iterations):
            subs_tiles_list: list[list[Tile]] = pool.map(partial(
                substitute, substitutions=substitutions, image_size=image_size), input_tiles)
            subs_tiles: list[Tile] = list(
                itertools.chain.from_iterable(subs_tiles_list))
            chunk_size = max(1, int(len(subs_tiles_list)/mp.cpu_count()))
            input_tiles = list(chunks(subs_tiles, chunk_size))
        poly_maps = pool.map(tiles_to_polygons, input_tiles)
    return merge_by_id(poly_maps)


def get_aabb(base_tile: Tile,
             substitutions: Dict[Tile, list[Tile]]) -> Vec2Pair:
    if len(base_tile.vec) <= 1:
        v = []
        for tile in substitutions[base_tile]:
            v.extend(tile.transform())
        return aabb(v)
    return base_tile.aabb()


def scale_tile(base_tile: Tile,
               image_size: Vec2i,
               aabb: Optional[Vec2Pair] = None) -> Tile:
    # Center tiles in image and scale to max
    if not aabb:
        aabb = base_tile.aabb()
    xscl = image_size[0] / abs(aabb[1][0] - aabb[0][0])
    yscl = image_size[1] / abs(aabb[1][1] - aabb[0][1])
    scl = min(xscl, yscl)
    tx = image_size[0]/2 - (aabb[0][0] + aabb[1][0])*scl/2
    ty = image_size[1]/2 - (aabb[0][1] + aabb[1][1])*scl/2
    return base_tile.cpy().tra(tx, ty).scl(scl).push()


def zoom_tile(base_tile: Tile,
              image_size: Vec2i,
              focus: tuple[float, float, float]) -> Tile:
    # Focus on point and scale (x, y, z). (0, 0, 1) is center of image, no scale.
    # x and y are between -1 and 1
    scl = focus[2]
    tx = (1/2 - 1/2*scl - focus[0]/2*scl)*image_size[0]
    ty = (1/2 - 1/2*scl + focus[1]/2*scl)*image_size[1]
    return base_tile.cpy().tra(tx, ty).scl(scl).push()


def draw_image(image_name: str,
               image_size: Vec2i,
               css: str,
               base_tile: Tile,
               substitutions: Dict[Tile, list[Tile]],
               iterations: int,
               focus: tuple[float, float, float] = (0, 0, 1)) -> Drawing:
    base_tile = scale_tile(base_tile, image_size,
                           aabb=get_aabb(base_tile, substitutions))
    base_tile = zoom_tile(base_tile, image_size, focus)
    poly_map = process(base_tile, substitutions, iterations, image_size)

    image = Drawing(image_name, size=image_size)
    image.embed_stylesheet(css)
    for id, polygons in poly_map.items():
        group = image.add(image.g(id=id))
        for polygon in polygons:
            group.add(polygon)
    return image


def draw_schematic(image_name: str,
                   image_size: Vec2i,
                   css: str,
                   tiles: list[Tile],
                   substitutions: Dict[Tile, list[Tile]]) -> Drawing:
    image = Drawing(image_name, size=image_size)
    image.embed_stylesheet(css)

    poly_maps = []
    arrows = []
    dy = 0
    for i in range(0, len(tiles)):
        tile = tiles[i]
        if len(tile.vec) <= 1:
            continue

        scl0 = int(image_size[0]*tile.scale*0.5)
        scl1 = int(image_size[0]*0.5)

        tile = scale_tile(tile.cpy(), (scl1, scl1))
        tileheight = tile.aabb()[1][1]-tile.aabb()[0][1]
        tile = scale_tile(tile.cpy(), (scl1, int(tileheight)))
        tile = tile.tra(150, dy).push()
        poly_maps.append(process(tile, substitutions, 1, image_size))

        tile = scale_tile(tile.cpy(), (scl0, scl0))
        th = tile.aabb()[0][1]
        th2 = (tile.aabb()[1][1]-tile.aabb()[0][1])/2
        tile = tile.tra(0, dy-th-th2+tileheight/2).push()
        poly_maps.append(process(tile, substitutions, 0, image_size))

        a0 = (100, dy+tileheight/2)
        a1 = (130, dy+tileheight/2)
        head = [a1, (a1[0], a1[1]+4), (a1[0]+10, a1[1]), (a1[0], a1[1]-4)]
        arrows.append(image.polyline([a0, a1], stroke='black', stroke_width=2))
        arrows.append(image.polygon(head, fill='black'))

        dy += int(tileheight)+10

    image['height'] = dy-10
    image.add(image.rect(
        (0, 0), (image['width'], image['height']),  fill='white'))
    for arrow in arrows:
        image.add(arrow)
    for id, polygons in merge_by_id(poly_maps).items():
        group = image.add(image.g(id=id))
        for polygon in polygons:
            group.add(polygon)

    return image
