
---

## Title bar and the drag-grab trap (issue #111)

`src/crates/concat/ui/title-bar.slint` has a `drag := TouchArea` declared
**first** in the z-order. The comment says controls sit above it and take
their own presses, but `Image`, `Text`, and plain `Rectangle` are not hit
targets in Slint — presses on them fall through to the drag area.

The drag area calls `root.begin-drag()` on every `PointerEventKind.down`
with the left button, not only when the pointer actually moves. On X11 and
Wayland that grabs the pointer. A press without a drag does not release
the grab cleanly, so the app stops receiving mouse events until the next
right-click sends a `ButtonRelease` that clears it.

Symptom (issue #111, labelled duplicate): click the logo, app goes deaf
to the mouse until you right-click somewhere.

**Pattern to avoid:** any clickable thing that sits inside the drag area
without its own `TouchArea` above it inherits this. If you add something
clickable to the title bar, wrap it in its own `TouchArea` with
`mouse-cursor: pointer`.

**Pattern to use for drag:** only call `begin-drag()` after the pointer
has moved past a small threshold (3-5px), and clear the armed flag on
`PointerEventKind.up`:

    property <bool> drag-armed: false;
    property <length> press-x: 0px;
    property <length> press-y: 0px;

    pointer-event(event) => {
        if (event.kind == PointerEventKind.down && event.button == PointerEventButton.left) {
            drag-armed = true;
            press-x = event.pos.x;
            press-y = event.pos.y;
        }
        if (event.kind == PointerEventKind.move && drag-armed) {
            if (abs(event.pos.x - press-x) > 4px || abs(event.pos.y - press-y) > 4px) {
                drag-armed = false;
                root.begin-drag();
            }
        }
        if (event.kind == PointerEventKind.up) {
            drag-armed = false;
        }
    }

Do not try to fix this in the engine — it is a Slint/winit interaction,
not a Concat bug. If the upstream Slint issue gets fixed, the workaround
can be removed.
