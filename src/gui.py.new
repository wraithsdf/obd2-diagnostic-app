import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from obd_reader import OBDReader
import threading
import time

class OBDGUI:
    def __init__(self):
        self.root = ThemedTk(theme="equilux")  # Modern dark theme
        self.root.title("OBD-II Diagnostic Pro")
        self.root.geometry("800x600")
        self.root.configure(bg='#2e2e2e')
        
        self.reader = OBDReader()
        self.running = False
        self.update_thread = None
        self.setup_styles()
        self.setup_gui()

    def setup_styles(self):
        style = ttk.Style()
        style.configure('Custom.TFrame', background='#2e2e2e')
        style.configure('Custom.TLabel', 
                       background='#2e2e2e', 
                       foreground='white',
                       font=('Arial', 10))
        style.configure('Header.TLabel',
                       background='#2e2e2e',
                       foreground='white',
                       font=('Arial', 12, 'bold'))
        style.configure('Value.TLabel',
                       background='#2e2e2e',
                       foreground='#00ff00',
                       font=('Arial', 20, 'bold'))
        style.configure('Custom.TButton',
                       padding=10,
                       font=('Arial', 10, 'bold'))

    def setup_gui(self):
        main_frame = ttk.Frame(self.root, style='Custom.TFrame')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        self.setup_connection_section(main_frame)
        self.setup_data_section(main_frame)
        self.setup_dtc_section(main_frame)

    def setup_connection_section(self, parent):
        conn_frame = ttk.LabelFrame(parent, text="Connection Status", style='Custom.TFrame')
        conn_frame.pack(fill='x', padx=5, pady=5)

        status_frame = ttk.Frame(conn_frame, style='Custom.TFrame')
        status_frame.pack(fill='x', padx=10, pady=5)

        self.status_label = ttk.Label(status_frame, 
                                    text="⚫ Disconnected", 
                                    style='Custom.TLabel')
        self.status_label.pack(side='left')

        self.conn_button = ttk.Button(status_frame, 
                                    text="Connect",
                                    style='Custom.TButton',
                                    command=self.toggle_connection)
        self.conn_button.pack(side='right')

    def setup_data_section(self, parent):
        data_frame = ttk.LabelFrame(parent, text="Vehicle Data", style='Custom.TFrame')
        data_frame.pack(fill='x', padx=5, pady=5)

        for i in range(3):
            data_frame.columnconfigure(i, weight=1)

        self.setup_data_widget(data_frame, 0, "Engine RPM", "rpm_value")
        self.setup_data_widget(data_frame, 1, "Vehicle Speed", "speed_value")
        self.setup_data_widget(data_frame, 2, "Coolant Temp", "temp_value")

    def setup_data_widget(self, parent, column, title, value_name):
        frame = ttk.Frame(parent, style='Custom.TFrame')
        frame.grid(row=0, column=column, padx=10, pady=5, sticky='nsew')
        
        ttk.Label(frame, text=title, style='Header.TLabel').pack()
        
        value_label = ttk.Label(frame, text="--", style='Value.TLabel')
        value_label.pack(pady=5)
        setattr(self, value_name, value_label)

    def setup_dtc_section(self, parent):
        dtc_frame = ttk.LabelFrame(parent, text="Diagnostic Trouble Codes", style='Custom.TFrame')
        dtc_frame.pack(fill='both', expand=True, padx=5, pady=5)

        self.dtc_text = tk.Text(dtc_frame, 
                               height=8,
                               bg='#1e1e1e',
                               fg='white',
                               font=('Courier', 10))
        scrollbar = ttk.Scrollbar(dtc_frame, orient='vertical', command=self.dtc_text.yview)
        self.dtc_text.configure(yscrollcommand=scrollbar.set)
        
        self.dtc_text.pack(side='left', fill='both', expand=True, padx=(5,0), pady=5)
        scrollbar.pack(side='right', fill='y', padx=(0,5), pady=5)

        button_frame = ttk.Frame(dtc_frame, style='Custom.TFrame')
        button_frame.pack(fill='x', padx=5, pady=5)

        ttk.Button(button_frame,
                  text="Clear DTCs",
                  style='Custom.TButton',
                  command=self.clear_dtc).pack(side='right', padx=5)
        
        ttk.Button(button_frame,
                  text="Refresh DTCs",
                  style='Custom.TButton',
                  command=self.refresh_dtc).pack(side='right', padx=5)

    def toggle_connection(self):
        if not self.running:
            if self.reader.connect():
                self.conn_button.configure(text="Disconnect")
                self.status_label.configure(text="🟢 Connected")
                self.running = True
                self.update_thread = threading.Thread(target=self.update_data, daemon=True)
                self.update_thread.start()
                messagebox.showinfo("Success", "Successfully connected to vehicle!")
            else:
                messagebox.showerror("Error", "Failed to connect to vehicle!")
        else:
            self.running = False
            self.conn_button.configure(text="Connect")
            self.status_label.configure(text="⚫ Disconnected")

    def update_data(self):
        while self.running:
            try:
                # Update RPM
                rpm = self.reader.get_rpm()
                self.rpm_value.configure(text=f"{rpm if rpm else '--'} RPM")

                # Update Speed
                speed = self.reader.get_speed()
                self.speed_value.configure(text=f"{speed if speed else '--'} km/h")

                # Update Temperature
                temp = self.reader.get_coolant_temp()
                self.temp_value.configure(text=f"{temp if temp else '--'}°C")

            except Exception as e:
                print(f"Error updating data: {e}")
            
            time.sleep(0.1)  # Update 10 times per second

    def clear_dtc(self):
        if self.reader.clear_dtc():
            self.dtc_text.delete(1.0, tk.END)
            self.dtc_text.insert(tk.END, "No DTCs present")
            messagebox.showinfo("Success", "DTCs cleared successfully!")
        else:
            messagebox.showerror("Error", "Failed to clear DTCs!")

    def refresh_dtc(self):
        dtc_codes = self.reader.get_dtc_codes()
        self.dtc_text.delete(1.0, tk.END)
        if dtc_codes:
            for code in dtc_codes:
                self.dtc_text.insert(tk.END, f"{code}\n")
        else:
            self.dtc_text.insert(tk.END, "No DTCs present")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = OBDGUI()
    app.run()
