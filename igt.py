import tkinter as tk
from tkinter import ttk
import requests
import threading

API_KEY = "YOUR_API_KEY_HERE"
API_URL = "https://api.ipgeolocation.io/ipgeo"

def fetch_ip_info():
    ip_address = ip_entry.get().strip()
    
    if not ip_address:
        show_error("Please enter an IP address!")
        return
    
    loading_animation()
    
    def api_call():
        try:
            response = requests.get(API_URL, params={"apiKey": API_KEY, "ip": ip_address})
            if response.status_code == 200:
                ip_info = response.json()
                app.after(0, lambda: display_ip_info(ip_info))
            else:
                app.after(0, lambda: show_error(f"API Error: {response.status_code}\n{response.text}"))
        except Exception as e:
            app.after(0, lambda: show_error(f"An error occurred: {str(e)}"))
        finally:
            app.after(0, stop_loading_animation)

    threading.Thread(target=api_call, daemon=True).start()

def show_error(message):
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Error: {message}", "error")
    output_text.config(state=tk.DISABLED)

def loading_animation():
    global loading
    loading = True
    animate_loading()

def animate_loading():
    if loading:
        for i in range(4):
            if not loading:
                break
            search_button.config(text="Searching" + "." * i)
            app.after(200, animate_loading)
            return
    search_button.config(text="Lookup")

def stop_loading_animation():
    global loading
    loading = False
    search_button.config(text="Lookup")

def display_ip_info(ip_info):
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    
    sections = [
        ("Basic Information", ["ip", "hostname", "isp", "organization", "asn", "connection_type"]),
        ("Location Information", ["continent_name", "country_name", "state_prov", "city", "district", "zipcode", "latitude", "longitude"]),
        ("Time and Language", ["time_zone.name", "time_zone.current_time", "calling_code", "languages"]),
        ("Currency Information", ["currency.name", "currency.code", "currency.symbol"]),
        ("Security Information", ["security.threat_score", "security.is_proxy", "security.is_tor", "security.is_bot", "security.is_cloud_provider"]),
    ]
    
    for title, fields in sections:
        output_text.insert(tk.END, f"\n{title}\n", "section")
        output_text.insert(tk.END, "=" * 40 + "\n", "separator")
        for field in fields:
            keys = field.split('.')
            value = ip_info
            for key in keys:
                value = value.get(key, {})
            if isinstance(value, dict):
                value = "N/A"
            output_text.insert(tk.END, f"{field.split('.')[-1].replace('_', ' ').title()}: ", "field")
            output_text.insert(tk.END, f"{value}\n", "value")
    
    output_text.config(state=tk.DISABLED)

app = tk.Tk()
app.title("IGT")
app.geometry("800x600")

# Color scheme
BG_COLOR = "#0f0f23"
TEXT_COLOR = "#00ff00"
ACCENT_COLOR = "#00ffff"
BUTTON_BG = "#1a1a2e"
BUTTON_ACTIVE_BG = "#2a2a3e"

app.configure(bg=BG_COLOR)

content_frame = tk.Frame(app, bg=BG_COLOR)
content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

frame = tk.Frame(content_frame, bg=BG_COLOR)
frame.pack(pady=10)

ip_label = tk.Label(frame, text="Enter IP:", fg=TEXT_COLOR, bg=BG_COLOR, font=("Courier", 12))
ip_label.pack(side=tk.LEFT)

ip_entry = ttk.Entry(frame, font=("Courier", 12), width=30)
ip_entry.pack(side=tk.LEFT, padx=10)

search_button = ttk.Button(frame, text="Lookup", command=fetch_ip_info)
search_button.pack(side=tk.LEFT)

output_text = tk.Text(content_frame, wrap=tk.WORD, font=("Courier", 10), fg=TEXT_COLOR, bg=BUTTON_BG, insertbackground=TEXT_COLOR, height=25)
output_text.pack(pady=10, fill=tk.BOTH, expand=True)

output_text.tag_configure("section", foreground=ACCENT_COLOR, font=("Courier", 12, "bold"))
output_text.tag_configure("separator", foreground="#007700")
output_text.tag_configure("field", foreground="#00aa00")
output_text.tag_configure("value", foreground=TEXT_COLOR)
output_text.tag_configure("error", foreground="#ff0000")

app.bind('<Return>', lambda event: fetch_ip_info())

style = ttk.Style()
style.theme_use('clam')
style.configure("TEntry", foreground=TEXT_COLOR, background=BUTTON_BG, fieldbackground=BUTTON_BG, borderwidth=0)
style.configure("TButton", foreground=TEXT_COLOR, background=BUTTON_BG, borderwidth=0)
style.map("TButton", background=[('active', BUTTON_ACTIVE_BG)])

app.mainloop()

