def point_in_polygon(point, edges) -> bool:
    """
    Method to match point inside are of edges or not.

    :param point:
    :param edges:
    :return inside:
    """
    x, y = point
    inside = False

    for edge in edges:
        (x1, y1), (x2, y2) = edge
        if ((y1 > y) != (y2 > y)) and (x <= (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside
