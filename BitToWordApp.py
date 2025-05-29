import tkinter as tk

class BitUpdater:
    def __init__(self, master):
        self.master = master
        master.title("32-bit Integer Updater")

        self.bit_vars = [tk.IntVar() for _ in range(32)]
        self.integer_value = 0

        # --- UI Elements ---
        self.checkbox_frame = tk.Frame(master)
        self.checkbox_frame.pack(pady=10)

        self.checkboxes = []
        for i in range(32):
            cb = tk.Checkbutton(
                self.checkbox_frame,
                text=f"Bit {31-i}", # Display as Bit 31 down to Bit 0
                variable=self.bit_vars[i],
                command=self.update_integer
            )
            # Arrange checkboxes in 4 columns for better layout
            row = i // 8
            col = i % 8
            cb.grid(row=row, column=col, sticky="w", padx=5, pady=2)
            self.checkboxes.append(cb)

        self.result_label_text = tk.StringVar()
        self.result_label_text.set(f"Integer Value: {self.integer_value}")
        self.result_label = tk.Label(
            master,
            textvariable=self.result_label_text,
            font=("Arial", 14)
        )
        self.result_label.pack(pady=10)

        # Initialize display
        self.update_integer()

    def update_integer(self):
        """
        Updates the unsigned integer based on the current state of the checkboxes.
        Bit 0 is the least significant bit (LSB), controlled by checkboxes[31].
        Bit 31 is the most significant bit (MSB), controlled by checkboxes[0].
        """
        self.integer_value = 0
        for i in range(32):
            if self.bit_vars[i].get() == 1:
                # The checkbox bit_vars[0] corresponds to the MSB (bit 31)
                # The checkbox bit_vars[31] corresponds to the LSB (bit 0)
                self.integer_value |= (1 << (31 - i))

        self.result_label_text.set(f"Hex Integer Value: {hex(self.integer_value)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BitUpdater(root)
    root.mainloop()