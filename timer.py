import time
import tkinter as tk

class CountdownTimer:
    def __init__(self, master, countdown_time=60):
        self.master = master
        self.countdown_time = countdown_time
        self.remaining_time = countdown_time
        self.paused = False
        self.timer_running = False
        self.master.geometry("700x700")
        self.master.configure(bg="blue")
        
        self.display = tk.Label(master, text=countdown_time,font=("Arial", 70))
        self.display.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer, height=5, width=20,font=("Arial", 16))
        self.start_button.pack()

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_timer, state="disabled", height=5, width=20,font=("Arial", 16))
        self.pause_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer, state="disabled", height=5, width=20,font=("Arial", 16))
        self.reset_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state="disabled", height=5, width=20,font=("Arial", 16))
        self.stop_button.pack()
        
        # Display the current time
        self.current_time = tk.Label(master, text="", font=("Arial", 16))
        self.current_time.pack()
        
        
        # Start updating the current time label
        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.current_time.config(text=current_time)
        self.master.after(1000, self.update_time)


        
    

    def start_timer(self, countdown_time=None):
        if countdown_time:
            self.countdown_time = countdown_time
            self.remaining_time = countdown_time
            self.display.config(text=countdown_time)
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")
            self.reset_button.config(state="normal")
            self.stop_button.config(state="normal")
            self.countdown()
            
    
        

    def pause_timer(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")
            self.countdown()

    def reset_timer(self):
        self.paused = False
        self.timer_running = False
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled", text="Pause")
        self.reset_button.config(state="disabled")
        self.stop_button.config(state="disabled")
        self.remaining_time = self.countdown_time
        self.display.config(text=self.remaining_time)

    def stop_timer(self):
        self.paused = False
        self.timer_running = False
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled", text="Pause")
        self.reset_button.config(state="disabled")
        self.stop_button.config(state="disabled")
        self.remaining_time = self.countdown_time
        self.display.config(text=self.remaining_time)
        
   

    

    

    def countdown(self):
        if not self.paused and self.timer_running:
            self.remaining_time -= 1
            self.display.config(text=self.remaining_time)
            if self.remaining_time <= 0:
                self.stop_timer()
            else:
                self.master.after(1000, self.countdown)
                
                


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Countdown Timer")

    timer = CountdownTimer(root, 60)

    root.mainloop()
