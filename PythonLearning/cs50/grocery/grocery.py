items = []
try:
    while True:
            item = input("")
            items.append(item)
except EOFError:
        item_counts = {}
        for item in items:
            item_counts[item.upper()] = item_counts.get(item.upper(), 0) + 1

        sorted_items = sorted(item_counts.items(), key=lambda x: x[0])

        for item, count in sorted_items:
            print(f"{count} {item}")
