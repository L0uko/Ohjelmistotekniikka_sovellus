import pygame


class UI:
    def __init__(self, cell_size=30):
        self.cell_size = cell_size
        self.margin = 20
        self.font = None
        self.screen = None
        self.bg_color = (20, 20, 20)
        self.grid_color = (40, 40, 40)
        self.border_color = (200, 200, 200)

    def init_window(self, columns, rows):
        width = columns * self.cell_size + self.margin * 2
        height = rows * self.cell_size + self.margin * 2 + 80  # extra for HUD
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Tetris")
        self.font = pygame.font.SysFont("consolas", 20)

    def draw_cell(self, r, c, color):
        x = self.margin + c * self.cell_size
        y = self.margin + r * self.cell_size
        rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, color, rect)
        # cell border
        pygame.draw.rect(self.screen, self.grid_color, rect, 1)

    def draw_grid(self, field):
        self.screen.fill(self.bg_color)
        rows = field.rows()
        cols = field.columns()

        # Border around grid
        border_rect = pygame.Rect(
            self.margin - 2, self.margin - 2,
            cols * self.cell_size + 4, rows * self.cell_size + 4
        )
        pygame.draw.rect(self.screen, self.border_color, border_rect, 2)

        # Draw existing locked cells
        for r in range(rows):
            for c in range(cols):
                val = field.get_cell(r, c)
                if val == 0:
                    # draw empty with subtle grid lines
                    self.draw_cell(r, c, (25, 25, 25))
                else:
                    # val is color tuple (R,G,B)
                    self.draw_cell(r, c, val)

    def draw_piece(self, block, top_r, left_c, color):
        if block is None:
            return
        for i_r, row in enumerate(block):
            for i_c, v in enumerate(row):
                if v == 1:
                    r = top_r + i_r
                    c = left_c + i_c
                    self.draw_cell(r, c, color)

    def draw_hud(self, score, level, lines):
        w, h = self.screen.get_size()
        hud_y = h - 70
        # HUD background
        hud_rect = pygame.Rect(0, hud_y, w, 70)
        pygame.draw.rect(self.screen, (15, 15, 15), hud_rect)

        text_color = (220, 220, 220)
        s_text = self.font.render(f"Score: {score}", True, text_color)
        l_text = self.font.render(f"Level: {level}", True, text_color)
        lines_text = self.font.render(f"Lines: {lines}", True, text_color)

        self.screen.blit(s_text, (self.margin, hud_y + 10))
        self.screen.blit(l_text, (self.margin + 200, hud_y + 10))
        self.screen.blit(lines_text, (self.margin + 360, hud_y + 10))

        tip_text = self.font.render(
            "Arrows to move/rotate (Up to rotate). Space to hard drop. Esc to quit.",
            True, (150, 150, 150)
        )
        self.screen.blit(tip_text, (self.margin, hud_y + 40))

    def draw_game_over(self, score):
        self.screen.fill((10, 10, 10))
        title = pygame.font.SysFont("consolas", 36).render(
            "Game Over", True, (230, 60, 60))
        score_text = pygame.font.SysFont("consolas", 28).render(
            f"Final Score: {score}", True, (220, 220, 220))
        w, h = self.screen.get_size()
        self.screen.blit(title, (w // 2 - title.get_width() // 2, h // 2 - 40))
        self.screen.blit(
            score_text, (w // 2 - score_text.get_width() // 2, h // 2 + 10))
