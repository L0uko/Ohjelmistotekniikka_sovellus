 ### Tetris alustava luokkakaavio


```mermaid
classDiagram
    class Map {
        -_map: list
        -_rows: int
        -_columns: int
        -_block_i: list
        -_block_o: list
        -_block_t: list
        -_block_s: list
        -_block_z: list
        -_block_j: list
        -_block_l: list
        -_possible_blocks: list
        -_colors: list
        +rows() int
        +columns() int
        +return_map() list
        +return_block_list() list
        +color_for_index(idx) tuple
        +return_map_str() str
        +in_bounds(r, c) bool
        +get_cell(r, c) int
        +set_cell(r, c, val)
        +rotate_block(block) list
        +can_place(block, top_r, left_c) bool
        +place_block(block, top_r, left_c, val)
        +clear_block(block, top_r, left_c)
        +lock_piece(block, top_r, left_c, color_value)
        +clear_full_lines() int
    }

    class Clock {
        -_clock: pygame.time.Clock
        +tick(fps)
        +get_ticks() int
    }

    class CurrentPiece {
        -_field: Map
        -shape_index: int
        -block: list
        -top_r: int
        -left_c: int
        -color: tuple
        +spawn(shape_index) bool
        +try_move(d_r, d_c) bool
        +try_rotate() bool
        +hard_drop()
        +lock_to_field()
    }

    class Gameloop {
        -_field: Map
        -_ui: userinterface.UI
        -_clock: Clock
        -_running: bool
        -_piece: CurrentPiece
        -_score: int
        -_level: int
        -_lines_cleared: int
        -_fall_interval_ms: int
        -_last_fall_tick: int
        +update_level_speed()
        +handle_lock_and_new()
        +process_input()
        +gravity_step(now_ticks)
        +draw()
        +start()
    }

    Gameloop --> Map
    Gameloop --> Clock
    Gameloop --> CurrentPiece
    CurrentPiece --> Map
 ```
 