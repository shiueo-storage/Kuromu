def delete(parent_layout):
    if parent_layout is not None:
        while parent_layout.count():
            item = parent_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                print(f"{item} removed")
                delete(parent_layout=item.layout())
