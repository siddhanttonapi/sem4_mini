def studentdashboard(id):
    def create_quiz_graph(id):
        # Connect to the database and extract data
        conn = sqlite3.connect('test2.db')
        c = conn.cursor()
        c.execute(f"SELECT Quizname, Quizscore FROM {id}")
        rows = c.fetchall()
        conn.close()

        # Convert the Quizscore from string to float and multiply by 100
        scores = [float(row[1]) * 100 for row in rows]

        # Create a bar graph
        fig = plt.figure(figsize=(8, 5))
        ax = fig.add_subplot(111)
        ax.bar([row[0] for row in rows], scores)

        # Set y limit to 100
        ax.set_ylim([0, 100])

        # Create a Tkinter window and add the graph to it
        root = tk.Tk()
        root.geometry("600x400")
        root.title("Bar Graph")
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        root.mainloop()
    def create_line_graph(id):
        # Connect to the database and extract data
        conn = sqlite3.connect('test2.db')
        c = conn.cursor()
        c.execute(f"SELECT Quizname, Quizscore FROM {id}")
        rows = c.fetchall()
        conn.close()

        # Convert the Quizscore from string to float and multiply by 100
        scores = [float(row[1]) * 100 for row in rows]

        # Create a line graph
        fig = plt.figure(figsize=(8, 5))
        ax = fig.add_subplot(111)
        ax.plot([row[0] for row in rows], scores)

        # Set y limit to 100
        ax.set_ylim([0, 100])

        # Create a Tkinter window and add the graph to it
        root = tk.Tk()
        root.geometry("600x400")
        root.title("Line Graph")
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        root.mainloop()
    # Create a new window
    dashboard_window = tk.Tk()
    dashboard_window.title('Dashboard')
    dashboard_window.geometry('800x600')
    dashboard_window.configure(bg='#f2f2f2')

    # Define the fonts
    title_font = ('Arial', 24, 'bold')
    welcome_font = ('Arial', 18, 'bold')
    button_font = ('Arial', 16, 'bold')

    # Create the header
    header_frame = tk.Frame(dashboard_window, bg='#b58868')
    header_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')
    header_frame.columnconfigure(0, weight=1)

    # Add the welcome label
    welcome_label = tk.Label(header_frame, text="Welcome, " + id, font=welcome_font, bg='#b58868', fg='white', padx=10)
    welcome_label.grid(row=0, column=0, sticky='w')

    # Add a spacer
    spacer_label = tk.Label(header_frame, text="", bg='#b58868')
    spacer_label.grid(row=0, column=1, sticky='e')

    # Create the widgets
    subject1_button = tk.Button(dashboard_window, text='VCPDE', font=button_font, bg='#4CAF50', fg='white', command=lambda: convert_tables_to_quiz(id,"vcpde"))
    subject2_button = tk.Button(dashboard_window, text='DSA-II', font=button_font, bg='#4CAF50', fg='white', command=lambda: convert_tables_to_quiz(id,"dsa"))
    subject3_button = tk.Button(dashboard_window, text='MPT', font=button_font, bg='#4CAF50', fg='white', command=lambda: convert_tables_to_quiz(id,"mpt"))
    subject4_button = tk.Button(dashboard_window, text='DC', font=button_font, bg='#4CAF50', fg='white', command=lambda: convert_tables_to_quiz(id,"dc"))
    
    # Create the graph buttons
    graph1_button = tk.Button(dashboard_window, text='View Bar Graph', font=button_font, bg='#4CAF50', fg='white', command=lambda: create_quiz_graph(id))
    graph2_button = tk.Button(dashboard_window, text='View Line Graph', font=button_font, bg='#4CAF50', fg='white', command=lambda: create_line_graph(id))
    
    # Add the widgets to the window
    subject1_button.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
    subject2_button.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')
    subject3_button.grid(row=2, column=0, padx=20, pady=20, sticky='nsew')
    subject4_button.grid(row=2, column=1, padx=20, pady=20, sticky='nsew')
    graph1_button.grid(row=3, column=0, padx=20, pady=20, sticky='nsew')
    graph2_button.grid(row=3, column=1, padx=20, pady=20, sticky='nsew')

    # Set the grid layout parameters
    for i in range(4):
        dashboard_window.rowconfigure(i, weight=1)
    for i in range(2):
        dashboard_window.columnconfigure(i, weight=1)

    # Center the welcome label
    welcome_label.grid_configure(padx=(200, 0))

    # Add styles to the buttons
    dashboard_window.option_add('*Button.activeBackground', '#3e8e41')
    dashboard_window.option_add('*Button.activeForeground', 'white')
    dashboard_window.option_add('*Button.highlightBackground', '#7be583')
    dashboard_window.option_add('*Button.highlightColor', 'white')
    dashboard_window.option_add('*Button.relief', 'raised')
    dashboard_window.option_add('*Button.borderWidth', '2')

    # Add styles to the header
    header_frame.configure(highlightbackground='#b58868', highlightcolor='#b58868', highlightthickness=1)

    # Add styles to the welcome label
    welcome_label.configure(anchor='center')

    # Add styles to the subject buttons
    subject1_button.configure(width=20, height=10)
    subject2_button.configure(width=20, height=10)
    subject3_button.configure(width=20, height=10)
    subject4_button.configure(width=20, height=10)

    # Add styles to the graph buttons
    graph1_button.configure(width=20, height=5)
    graph2_button.configure(width=20, height=5)

    # Add a style for the spacer label
    spacer_label.configure(width=30)

    # Add a footer
    footer_frame = tk.Frame(dashboard_window, bg='#b58868')
    footer_frame.grid(row=4, column=0, columnspan=2, sticky='nsew')
    footer_label = tk.Label(footer_frame, text='© 2023 All Rights Reserved. | Created by ChatGPT', font=('Arial', 10, 'italic'), bg='#b58868', fg='white')
    footer_label.pack(pady=10)

    # Start the window
    dashboard_window.mainloop()



        # Create the register window
    admin_window = tk.Tk()
    admin_window.title('Admin')
    admin_window.geometry('400x300')
    admin_window.configure(bg='#f2f2f2')
    root.destroy()
    # Create the widgets
    titleadmin_label = tk.Label(admin_window, text='Login', font=title_font, bg='#f2f2f2')
    id_label = tk.Label(admin_window, text='ID', font=label_font, bg='#f2f2f2')
    id_entry = tk.Entry(admin_window, font=entry_font)
    pw_label = tk.Label(admin_window, text='Password', font=label_font, bg='#f2f2f2')
    pw_entry = tk.Entry(admin_window, show='*', font=entry_font)
    loginadmin_button = tk.Button(admin_window, text='Login', font=button_font, bg='#4CAF50', fg='white')
    regadmin_button = tk.Button(admin_window, text='Register', font=button_font, bg='#4CAF50', fg='white')
    # Define the layout
    titleadmin_label.place(relx=0.5, rely=0.1, anchor='center')
    id_label.place(relx=0.3, rely=0.3, anchor='center')
    id_entry.place(relx=0.7, rely=0.3, anchor='center')
    pw_label.place(relx=0.3, rely=0.4, anchor='center')
    pw_entry.place(relx=0.7, rely=0.4, anchor='center')
    loginadmin_button.place(relx=0.5, rely=0.6, anchor='center')
    regadmin_button.place(relx=0.8, rely=0.8, anchor='center')