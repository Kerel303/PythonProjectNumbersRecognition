import tkinter as tk

# Rozmiar siatki pikseli
GRID_WIDTH = 32
GRID_HEIGHT = 32
PIXEL_SIZE = 15

class Editor:
    # Kolorki
    BG = "#1e1e1e"
    PANEL_BG = "#2d2d2d"
    PIXEL_OFF = "#3a3a3a"
    PIXEL_ON = "#ffffff"
    TEXT_COLOR = "#e0e0e0"
    OUTLINE = "#505050"

    def __init__(self, root, recognize_callback, teach_callback):
        self.root = root
        self.recognize_callback = recognize_callback
        self.teach_callback = teach_callback
        self.root.title("Rozpoznawanie liczb")
        self.root.configure(background=self.BG)

        self.pixel_state = [[False for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        # Obszar rysowania
        self.canvas = tk.Canvas(
            root,
            width=GRID_WIDTH * PIXEL_SIZE,
            height=GRID_HEIGHT * PIXEL_SIZE,
            bg=self.PANEL_BG,
            highlightthickness=0,
            bd=0
        )
        self.canvas.pack()

        self.pixels = []

        for y in range(GRID_HEIGHT):
            row = []
            for x in range(GRID_WIDTH):
                rect = self.canvas.create_rectangle(
                    x * PIXEL_SIZE,
                    y * PIXEL_SIZE,
                    (x + 1) * PIXEL_SIZE,
                    (y + 1) * PIXEL_SIZE,
                    fill=self.PIXEL_OFF,
                    outline=self.OUTLINE
                )
                row.append(rect)
            self.pixels.append(row)

        # Tutaj zaznaczanie pikseli
        self.canvas.bind("<Button-1>", self.paint_pixel)
        self.canvas.bind("<B1-Motion>", self.paint_pixel)

        # Tutaj usuwanie zaznaczenia pikseli
        self.canvas.bind("<B3-Motion>", self.erase_pixel)
        self.canvas.bind("<Button-3>", self.erase_pixel)

        # Pole odpowiedzi programu
        self.response_var = tk.StringVar()
        self.response_var.set("Tutaj będzie odpowiedź programu")

        self.response_label = tk.Label(
            root,
            textvariable=self.response_var,
            font=("Segoe UI", 12),
            bg=self.PANEL_BG,
            fg=self.TEXT_COLOR,
        )
        self.response_label.pack(fill="x", padx=5, pady=10)

        # Przyciski

        button_frame = tk.Frame(root, bg=self.BG)
        button_frame.pack(padx=5, pady=5)

        # Przycisk testowy
        tk.Button(
            button_frame,
            text="Rozpoznaj",
            command=self.recognize
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Wyczyść",
            command=self.clear_canvas
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Naucz",
            command=self.teach
        ).pack(side="left", padx=5)

        # Koniec przycisków

    #Funkcje UI

    def paint_pixel(self, event):
        x = event.x // PIXEL_SIZE
        y = event.y // PIXEL_SIZE

        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            self.pixel_state[y][x] = True

            self.canvas.itemconfig(
                self.pixels[y][x],
                fill=self.PIXEL_ON
            )

    def erase_pixel(self, event):
        x = event.x // PIXEL_SIZE
        y = event.y // PIXEL_SIZE

        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            self.pixel_state[y][x] = False

            self.canvas.itemconfig(
                self.pixels[y][x],
                fill=self.PIXEL_OFF
            )

    def clear_canvas(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                self.pixel_state[y][x] = False

                self.canvas.itemconfig(
                    self.pixels[y][x],
                    fill=self.PIXEL_OFF
                )

    def recognize(self):
        full_list = []
        for row in self.pixel_state:
            row_list = []
            for pixel in row:
                if pixel == True:
                    row_list.append(1)
                else:
                    row_list.append(0)
            full_list.append(row_list)
        if self.recognize_callback:
            self.recognize_callback(full_list)

    def teach(self):
        full_list = []
        for row in self.pixel_state:
            row_list = []
            for pixel in row:
                if pixel == True:
                    row_list.append(1)
                else:
                    row_list.append(0)
            full_list.append(row_list)
        if self.teach_callback:
            self.teach_callback(full_list)


    def set_text(self, text):
        self.response_var.set(text)
