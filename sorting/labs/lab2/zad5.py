E_OPEN = "open"
E_CLOSE = "close"

type Point = tuple[int, int]


class Event:
    def __init__(self, type, y, width):
        self.type = type
        self.y = y
        self.width = width


def merge(a, l, mid, r):
    left = a[l:mid + 1]
    right = a[mid + 1:r + 1]

    i = 0
    j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i].y < right[j].y:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def merge_sort(a, l, r):
    if l < r:
        mid = l + (r - l) // 2
        merge_sort(a, l, mid)
        merge_sort(a, mid + 1, r)
        merge(a, l, mid, r)


def find_filled_tanks(a: list[tuple[Point, Point]], water):
    n = len(a)
    events = []

    # Create events from container
    for i in range(n):
        top, bottom = a[i]
        width = bottom[0] - top[0]
        events.append(Event(type=E_OPEN, y=bottom[1], width=width))
        events.append(Event(type=E_CLOSE, y=top[1], width=width))

    # Sort events by occurrence height.
    merge_sort(events, 0, len(events) - 1)

    filled_count = 0
    current_width = 0
    current_y = 0

    # Process sorted events.
    for e in events:
        water -= current_width * (e.y - current_y)

        if water < 0:
            break

        if e.type is E_OPEN:
            current_width += e.width
        if e.type is E_CLOSE:
            filled_count += 1
            current_width -= e.width

        current_y = e.y

    return filled_count


if __name__ == "__main__":
    tanks = [((10, 4), (14, 2)), ((5, 3), (8, 1)), ((3, 9), (7, 4))]
    print(find_filled_tanks(tanks, 20))
