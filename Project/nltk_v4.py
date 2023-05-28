from tkinter import filedialog
import sys
import matplotlib.pyplot as plt
from Kmeans import Kmeans
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from Aproiri import Aprori
import pandas as pd
from utils import make_dic, make_pattern
import numpy as np
global data
global apriori
global kmeans
apriori = None
kmeans = None
data = None
# Create the main window
root = tk.Tk()
root.title("KDD project")
root.geometry("1080x700")
root.configure(bg="#1c1c1c")

# Create the left sidebar
sidebar = tk.Frame(root, width=200, bg="#303030")
sidebar.pack(side="left", fill="y")

# Add the logo to the sidebar
logos = Image.open(
    r"C:\\Users\\East-Sound\Desktop\\KDD_project-20230521T170014Z-001\\KDD_project\\logos.jpg")
width, hight = logos.size
new_width = int(width * 0.25)  # reduce the width by 50%
new_height = int(hight * 0.25)  # reduce the height by 50%
logos = logos.resize((new_width, new_height), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(logos)

logo = tk.Label(sidebar, image=logo_image, bg="black")
logo.pack(pady=20, padx=10)

# Add the pages to the sidebar
pages = ["Home", "K-Means", "Apriori", "About Us"]
page_frames = {}
for page in pages:
    frame = tk.Frame(root, bg="black")
    frame.pack(side="right", fill="both", expand=True)
    page_frames[page] = frame

# Define the styles for the buttons in the sidebar
style = ttk.Style()
style.configure("Sidebar.TButton", fg="red",
                bg="red", font=("Helvetica", 14), width=25)


home_content = tk.Frame(page_frames["Home"], bg="#1c1c1c")  # bg Color
home_content.pack(fill="both", expand=True)

# =========================background========================================
background = Image.open(
    r"C:\\Users\\East-Sound\Desktop\\KDD_project-20230521T170014Z-001\\KDD_project\background.jpg")
# load the images
width, hight = background.size
new_width = int(width * 0.70)  # reduce the width by 50%
new_height = int(hight * 0.70)  # reduce the height by 50%
background = background.resize((new_width, new_height), Image.LANCZOS)
image4 = ImageTk.PhotoImage(background)


# ================================photos import================================
image_1 = Image.open(
    r"C:\\Users\\East-Sound\Desktop\\KDD_project-20230521T170014Z-001\\KDD_project\samir.jpeg")
# load the images
width, hight = image_1.size
new_width = int(width * 0.15)  # reduce the width by 50%
new_height = int(hight * 0.15)  # reduce the height by 50%
image_1 = image_1.resize((new_width, new_height), Image.LANCZOS)
image1 = ImageTk.PhotoImage(image_1)


image_2 = Image.open(
    r"C:\\Users\\East-Sound\Desktop\\KDD_project-20230521T170014Z-001\\KDD_project\Ahmed.jpg")
# load the images
width, hight = image_2.size
new_width = int(width * 0.25)  # reduce the width by 50%
new_height = int(hight * 0.25)  # reduce the height by 50%
image_2 = image_2.resize((new_width, new_height), Image.LANCZOS)
image2 = ImageTk.PhotoImage(image_2)

# image_3 = Image.open(r"./ziad.jpg")
# ==================================load the images===============================
# width, hight = image_3.size
new_width = int(width * 0.25)  # reduce the width by 50%
new_height = int(hight * 0.25)  # reduce the height by 50%
# image_3 = image_3.resize((new_width, new_height), Image.LANCZOS)
# image3 = ImageTk.PhotoImage(image_3)

# ==================================images captions==================================
home_picture_3 = tk.Label(home_content, image=image4)
home_picture_3.place(x=-10, y=-10)

home_title = tk.Label(home_content, text="Home Page", font=(
    "Helvetica", 25), fg="white", bg="#1c1c1c")
home_title.pack(pady=20)

# ==================================images captions==================================
cap2 = tk.Label(home_content, text="Dr. Amera El-zeniy", font=(
    "Arial", 20), fg="black", bg="#ffffff", bd=2, padx=10, pady=5, width=20)
cap2.place(x=210, y=140)
# create labels with the images
home_picture_1 = tk.Label(home_content, image=image1)
home_picture_1.place(x=50, y=250)
home_picture_2 = tk.Label(home_content, image=image2)
home_picture_2.place(x=300, y=250)
# home_picture_3 = tk.Label(home_content, image=image3)
home_picture_3.place(x=550, y=250)
samir = tk.Label(home_content, text="Samir Elkassar", font=(
    "Helvetica", 16), fg="white", bg="#1c1c1c")
samir.place(x=50, y=440)
ahmed = tk.Label(home_content, text="Ahmed Abdo", font=(
    "Helvetica", 16), fg="white", bg="#1c1c1c")
ahmed.place(x=300, y=440)
# ziad = tk.Label(home_content, text="Ziad sakr", font=(
# "Helvetica", 16), fg="white", bg="#1c1c1c")
# ziad.place(x=550, y=440)

cap1 = tk.Label(home_content, text="Computer Science", font=(
    "Arial", 12), fg="#c5cadb", bg="#1c1c1c")
cap1.place(x=50, y=470)
cap2 = tk.Label(home_content, text="Computer Science", font=(
    "Arial", 12), fg="#c5cadb", bg="#1c1c1c")
cap2.place(x=300, y=470)
# cap3 = tk.Label(home_content, text="Information technology", font=(
# "Arial", 12), fg="#c5cadb", bg="#1c1c1c")
# cap3.place(x=550, y=470)
# ================================================================================
# ================================[ kmeaans content ]===========================================
kmeans_content = tk.Frame(page_frames["K-Means"], bg="#1c1c1c")
kmeans_content.pack(fill="both", expand=True)
kmeans_title = tk.Label(kmeans_content, text="K-Means Page",
                        font=("Helvetica", 20), fg="white", bg="#1c1c1c")
kmeans_title.pack(pady=20)


def open_csv_file():
    csv_file = filedialog.askopenfilename(
        initialdir="/", title="Select CSV file", filetypes=(("CSV files", "*.csv"),))
    data_file = pd.read_csv(csv_file)
    global data
    data = data_file


kmeans_button_1 = ttk.Button(
    kmeans_content, text="Import CSV file", style="Sidebar.TButton", command=open_csv_file)
kmeans_button_1.place(x=90, y=90)


# =============[ comands ]===========================================
def Fit_kmeans():
    print("kmeans results")
    redirect_output()


def run_kmeans():
    global kmeans
    n_clusters = int(kmeans_input1.get())
    kmeans = Kmeans(n_clusters)
    dataset = data.values[:, 1:4]

    plt.xlabel('Iterations', fontsize=12, color='b', fontweight='bold')
    plt.ylabel('Distortion Values', fontsize=12, color='b', fontweight='bold')
    plt.title('The Distortion Function of Clusters',
              fontsize=16, color='r', fontweight='bold')
    colors = ['r', 'g', 'b', 'y']
    for i in range(4):
        kmeans = Kmeans(3)
        kmeans.fit(3, dataset)
        plt.plot(np.array(kmeans.distortion)/1000, marker='x',
                 color=colors[i], linewidth=3.0, markersize=10, markeredgewidth=4)
    plt.savefig('./results.png')
    plt.show()


def predict_kmeans():
    sample = kmeans_input2.get()
    sample = sample.split(' ')
    sample = [float(s) for s in sample]
    global prediction
    prediction = 'Empty'
    try:
        prediction = kmeans.predict(sample)
    except Exception as err:
        print(err)

    prediction = str(prediction)
    prediction = '\n\t\tCluster Number: ' + prediction + '\n'
    kmeans_output_text.insert(tk.END, str(prediction))


def run_apriori():
    support_count = int(input_var1.get())
    support_confidence = int(input_var2.get())
    global apriori
    apriori = Aprori(support_count, support_confidence)
    data_dic = make_dic(data)
    apriori.fit(data_dic)
    apriori.run()


def Fit_Aprior():
    print('\tFrequent Itemsets Are', apriori.old_item_set, '\n')
    print('\tFrom', '==>', 'To, ', 'Confidence = --\n', )
    for st in apriori.rules:
        for r in st:
            print('\t', r.A, '==>', r.B, ', Confidence = ',
                  str(r.confidence*10)[0:5]+'%', '\n')
    redirect_output()

# ====================================================================


kmeans_button_2 = ttk.Button(
    kmeans_content, text="Fit the model", style="Sidebar.TButton", command=run_kmeans)
kmeans_button_2.place(x=90, y=150)


kmeans_button_3 = ttk.Button(
    kmeans_content, text="Predict", style="Sidebar.TButton", command=predict_kmeans)
kmeans_button_3.place(x=90, y=210)

# ===================================aprior input=====================
kmeans_input1 = tk.StringVar()
kmeans_input2 = tk.StringVar()

input_field = tk.Entry(kmeans_content, textvariable=kmeans_input1)
input_field.place(x=640, y=105)
apriori_result = tk.Label(kmeans_content, text="Number of Clusters", font=(
    "Helvetica", 16), fg="green", bg="#1c1c1c")
apriori_result.place(x=435, y=100)

input_field1 = tk.Entry(
    kmeans_content, textvariable=kmeans_input2, width=27)
input_field1.place(x=600, y=165)
apriori_result1 = tk.Label(kmeans_content, text="Data to predict", font=(
    "Helvetica", 16), fg="green", bg="#1c1c1c")
apriori_result1.place(x=430, y=160)


# ==============================================


kmeans_result = tk.Label(kmeans_content, text="Result Window", font=(
    "Helvetica", 14), fg="green", bg="#1c1c1c")
kmeans_result.place(x=300, y=270)


# create a Text widget with a larger size
kmeans_output_text = tk.Text(kmeans_content, height=10, width=42, bg='#2F73C1')
kmeans_output_text.place(x=90, y=320)

# change the size of the Text widget dynamically
kmeans_output_text.config(font=("Helvetica", 18, 'bold'), fg='white',)

# define a function to redirect the program output to the Text widget


def redirect_output():
    sys.stdout = OutputRedirector(output_text)

# define a class to redirect the output to the Text widget


class OutputRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert("end", text)
        self.text_widget.see("end")


# call the redirect_output function to redirect the output


# run your program

# ================================[ aprior content ]===========================================
apriori_content = tk.Frame(page_frames["Apriori"], bg="#1c1c1c")
apriori_content.pack(fill="both", expand=True)
apriori_title = tk.Label(apriori_content, text="Apriori Page", font=(
    "Helvetica", 20), fg="white", bg="#1c1c1c")
apriori_title.pack(pady=20)
apriori_button_1 = ttk.Button(
    apriori_content, text="Import CSV file", style="Sidebar.TButton", command=open_csv_file)
apriori_button_1.place(x=90, y=90)
apriori_button_2 = ttk.Button(
    apriori_content, text="Fit the model", style="Sidebar.TButton", command=run_apriori)
apriori_button_2.place(x=90, y=150)


apriori_button_3 = ttk.Button(
    apriori_content, text="Show results", style="Sidebar.TButton", command=Fit_Aprior)
apriori_button_3.place(x=90, y=210)
# ===================================aprior input=====================
input_var1 = tk.StringVar()
input_var2 = tk.StringVar()

input_field = tk.Entry(apriori_content, textvariable=input_var1)
input_field.place(x=640, y=105)
apriori_result = tk.Label(apriori_content, text="Support Count", font=(
    "Helvetica", 16), fg="green", bg="#1c1c1c")
apriori_result.place(x=475, y=100)

input_field1 = tk.Entry(apriori_content, textvariable=input_var2)
input_field1.place(x=640, y=165)
apriori_result1 = tk.Label(apriori_content, text="Support Confidence", font=(
    "Helvetica", 16), fg="green", bg="#1c1c1c")
apriori_result1.place(x=445, y=160)


def Get_first_input():
    input_value1 = input_var1.get()
    print(input_value1)


def Get_second_input():
    input_value2 = input_var2.get()
    print(input_value2)


# =======================================================================
apriori_result = tk.Label(apriori_content, text="Result Window", font=(
    "Helvetica", 14), fg="green", bg="#1c1c1c")
apriori_result.place(x=300, y=270)


# create a Text widget with a larger size
output_text = tk.Text(apriori_content, height=13, width=50)
output_text.place(x=90, y=320)


# change the size of the Text widget dynamically
output_text.config(font=("Helvetica", 14))

# define a function to redirect the program output to the Text widget


def redirect_output():
    sys.stdout = OutputRedirector(output_text)

# define a class to redirect the output to the Text widget


class OutputRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert("end", text)
        self.text_widget.see("end")


# call the redirect_output function to redirect the output
# ================================[ about us content ]===========================================
about_content = tk.Frame(page_frames["About Us"], bg="#1c1c1c")
about_content.pack(fill="both", expand=True)
about_title = tk.Label(about_content, text="About Us Page", font=(
    "Helvetica", 20), fg="white", bg="#1c1c1c")
about_title.pack(pady=20)
about_text = tk.Label(about_content, text="We are a team of developers.", font=(
    "Helvetica", 14), fg="white", bg="#1c1c1c")
about_text.pack(pady=20)


# Define a function to switch between pages


def show_page(page):
    for p in pages:
        if p == page:
            page_frames[p].pack(fill="both", expand=True)
        else:
            page_frames[p].pack_forget()


# Add the sidebar buttons
home_button = ttk.Button(
    sidebar, text="Home", style="Sidebar.TButton", command=lambda: show_page("Home"))
home_button.pack(pady=10)
kmeans_button = ttk.Button(
    sidebar, text="K-Means", style="Sidebar.TButton", command=lambda: show_page("K-Means"))
kmeans_button.pack(pady=10)
apriori_button = ttk.Button(
    sidebar, text="Apriori", style="Sidebar.TButton", command=lambda: show_page("Apriori"))
apriori_button.pack(pady=10)
about_button = ttk.Button(sidebar, text="About Us",
                          style="Sidebar.TButton", command=lambda: show_page("About Us"))
about_button.pack(pady=10)


# Set the style for the sidebar buttons


# Show the home page initially
show_page("Home")


# Run the app
root.mainloop()
