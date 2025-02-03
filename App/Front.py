import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from App.Interpreter.Differential import differential
from App.Interpreter.Function import function
from App.Math_Methods import MathMethods
from App.ODE_Graf import DirectionFieldPlotter
from App.ODE_Graf import AbsoluteErrorPlotter
from App.ODE_Graf import RelativeErrorPlotter
from App.ODE_Graf import ConditionPlotter

def create_calculator():
    root = tk.Tk()
    root.title("Differential Equation Calculator")
    
    # Set a smaller fixed window size
    window_width = 500  # Adjust as needed
    window_height = 800  # Adjust as needed
    
    # Center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(False, False)  # Prevent window resizing
    root.configure(bg="#2C3E50")

    # Variables to store current display
    current_display = None

    def on_entry_click(event):
        nonlocal current_display
        current_display = event.widget
        current_display.config(state='normal')
        x = event.x
        click_index = current_display.index(f"@{x}")
        current_display.icursor(click_index)
        # click_position = current_display.index(tk.INSERT)
        # current_display.icursor(click_position)
        current_display.config(state = 'readonly')
   
    def add_number(number):
     if current_display:
        cursor_pos = current_display.index(tk.INSERT)
        current_display.config(state = 'normal')
        if number == 'π':
            current_display.insert(cursor_pos, 'pi')
        elif number == 'e':
            current_display.insert(cursor_pos, 'e')
        else:
            current_display.insert(cursor_pos, str(number))
        current_display.config(state = 'readonly')    

    def add_operation(operation):
        if current_display:
            cursor_pos = current_display.index(tk.INSERT)
            current_display.config(state='normal')
            if operation == 'log':
                current_display.insert(cursor_pos, 'log(,)')
                # create suggestion
                tooltip = tk.Toplevel()
                tooltip.wm_geometry("+%d+%d" % (current_display.winfo_rootx(), 
                                          current_display.winfo_rooty() + 30))
                tooltip.wm_overrideredirect(True)
                label = tk.Label(tooltip, text="Write: argument,base", 
                           bg="yellow", relief="solid", borderwidth=1)
                label.pack()
                 # Auto-close tooltip after 3 seconds
                current_display.after(3000, tooltip.destroy)
            else:  
             current_display.insert(cursor_pos, operation)
            current_display.config(state = 'readonly')

    def clear_display():
        if current_display:
            current_display.config(state='normal')
            current_display.delete(0, tk.END)
            current_display.config(state = 'readonly')

    def ClearEverything():
       main_display.config(state='normal') 
       main_display.delete(0, tk.END)
       main_display.config(state = 'readonly')

       for entry in entries.values():
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.config(state = 'readonly')

    
    def backspace():
        if current_display:
            current_display.config(state='normal')
            text = current_display.get()
            current_display.delete(0, tk.END)
            current_display.insert(0, text[:-1])
            current_display.config(state = 'readonly')
    # Main input frame
    input_frame = tk.Frame(root, bg="#2C3E50")
    input_frame.pack(pady=10)

    input_label = tk.Label(input_frame, text="EQUATION INPUT", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white")
    input_label.pack(pady=5)

    main_display = tk.Entry(input_frame, font=("Arial", 16), width=40, justify="right",state='readonly',cursor="arrow")
    main_display.pack(pady=5, ipady=10)
    main_display.bind("<Button-1>", on_entry_click)

    # Parameters frame
    params_frame = tk.Frame(root, bg="#2C3E50")
    params_frame.pack(pady=10)

    params = [("Xo:", "x0"), ("Yo:", "y0"), 
             ("Step: h =", "h"), ("Eval. x =", "calc_x"),
             ("Plot Init:", "interval_I"),
             ("Plot End:", "interval_F"),
             ("Exact Sol:", "sol")]
    
    entries = {}
    for label_text, key in params:
        frame = tk.Frame(params_frame, bg="#2C3E50")
        frame.pack(pady=3)
        
        label = tk.Label(frame, text=label_text, font=("Arial", 12), bg="#2C3E50", fg="white",width = 8, anchor="e")
        label.pack(side=tk.LEFT, padx=5)
        
        entry = tk.Entry(frame, font=("Arial", 12), width=12,state='readonly',justify='right')
        entry.pack(side=tk.LEFT, padx=5)
        entry.bind("<Button-1>", on_entry_click)
        entries[key] = entry

    # Calculator buttons 
    calc_frame = tk.Frame(root, bg="#2C3E50")
    calc_frame.pack(pady=10)

    buttons = [
    ('(', lambda: add_operation('(')), (')', lambda: add_operation(')')), 
    ('C', lambda: clear_display()), ('⌫', lambda: backspace()),
    ('7', lambda: add_number('7')), ('8', lambda: add_number('8')), ('9', lambda: add_number('9')), 
    ('/', lambda: add_operation('/')),
    ('4', lambda: add_number('4')), ('5', lambda: add_number('5')), ('6', lambda: add_number('6')), 
    ('*', lambda: add_operation('*')),
    ('1', lambda: add_number('1')), ('2', lambda: add_number('2')), ('3', lambda: add_number('3')), 
    ('-', lambda: add_operation('-')),
    ('0', lambda: add_number('0')), ('.', lambda: add_number('.')), ('=', lambda: add_operation('=')), 
    ('+', lambda: add_operation('+')),
    ('x', lambda: add_number('x')), ('y', lambda: add_number('y')), 
    ('π', lambda: add_number('π')), ('e', lambda: add_number('e')),
    ('dy/dx', lambda: add_operation('dy/dx')), ('log', lambda: add_operation('log')),
    ('√', lambda: add_operation('√')), ('^', lambda: add_operation('^')),
    ('sin', lambda: add_operation('sin')), ('cos', lambda: add_operation('cos')), 
    ('tan', lambda: add_operation('tan')), ('ln', lambda: add_operation('ln'))
]
    row = 0
    col = 0
    for button_text, command in buttons:
        btn = tk.Button(calc_frame, text=button_text, font=("Arial", 12, "bold"),
                       width=6, height=1, bg="#34495E", fg="white",
                       activebackground="#2980B9",
                       command=command)
        btn.grid(row=row, column=col, padx=3, pady=3)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Action buttons frame
    action_frame = tk.Frame(root, bg="#2C3E50")
    action_frame.pack(pady=10)
    
    solution_label = tk.Label(root, text="", wraplength=450, justify="left", bg="#2C3E50", fg="white", font = ("Arial",12,"bold"), height =4, width=40)
    solution_label.pack(pady=20,padx=10,fill=tk.BOTH,expand=True)
    # calculate function for EDO
    def calculate():
       
      try:
        
        equationString = main_display.get()
        equation = differential(equationString)
        
        if equation is None:
            solution_label.config(text="Error: Invalid equation format")
            return
            
        x0 = float(entries["x0"].get())
        y0 = float(entries["y0"].get())
        h = float(entries["h"].get())
        x1 = float(entries["calc_x"].get())
        try:
            calculator = MathMethods(x0, y0, equation, h, x1)
            print("MathMethods created successfully")
            solution = calculator.get_evaluation()
            solution_label.config(text=f"Solución: y({solution[0]}) = {solution[1]}")
        except Exception as e:
            print("Error in MathMethods:", str(e))
            solution_label.config(text=f"Error in calculation: {str(e)}")
        
      except ValueError as e:
        solution_label.config(text=f"Error: Please enter valid numbers")
      except Exception as e:
        solution_label.config(text=f"Error: {str(e)}")
            

    # Plot function for EDO
    def Plot():
        try:
        
            equationString = main_display.get()
            equation = differential(equationString)
            
            if equation is None:
                solution_label.config(text="Error: Invalid equation format")
                return
                
            x0 = float(entries["x0"].get())
            y0 = float(entries["y0"].get())
            h = float(entries["h"].get())
            x1 = float(entries["calc_x"].get())
            x_interval = [float(entries["interval_I"].get()), float(entries["interval_F"].get())]
            y_interval = [float(entries["interval_I"].get()), float(entries["interval_F"].get())]
            try:
                calculator = MathMethods(x0, y0, equation, h, x1)
                print("MathMethods created successfully")
                solution = calculator.get_evaluation()
                x_values,y_values = calculator.get_values()
                plotter = DirectionFieldPlotter()
                plotter.plot(equation,x_interval,y_interval,x_values, y_values,x1,solution[1])
            except Exception as e:
                print("Error in MathMethods:", str(e))

        except Exception as e:
            solution_label.config(text=f"Error: {str(e)}")
    
    

    def error_analysis():
        try:
         differential_string = main_display.get()
         equationString = entries["sol"].get()
         equat, equationDer = function(equationString)
         x0 = float(entries["x0"].get())
         y0 = float(entries["y0"].get())
         h = float(entries["h"].get())
         x1 = float(entries["calc_x"].get())
         ini = float(entries["interval_I"].get())
         end = float(entries["interval_F"].get())
         error = MathMethods(x0,y0,differential(differential_string),h,x1)
         error.numeric_analysis(equat,equationDer,ini,end)
        
        except ValueError as ve:
         solution_label.config(text= f"Error: {str(ve)}")   

        except Exception as e:
         solution_label.config(text=f"Error: {e}")
         return
       
        
        #   Create new window
        analysis_window = tk.Toplevel()
        analysis_window.title("Análisis de errores")
        analysis_window.geometry("400x700")
        analysis_window.configure(bg="#2C3E50")

        # Create frames for results
        texto1= "Max absolute error:"
        texto1_1,texto1_2 = error.numeric_get_range_max_absolute_error()
        
        result_frame1 = tk.Label(analysis_window, text=f"{texto1} ({texto1_1},{texto1_2})", wraplength=350,
                            bg="#34495E", fg="white", font=("Arial", 12),
                            height=3, width=40)
        result_frame1.pack(pady=10, padx=10)
        
        texto2= f"Absolute error in f({x1}):"
        texto2_1,texto2_2= error.numeric_get_specific_absolute_error()
        result_frame2 = tk.Label(analysis_window, text=f"{texto2} ({texto2_1},{texto2_2})", wraplength=350,
                            bg="#34495E", fg="white", font=("Arial", 12),
                            height=3, width=40)
        result_frame2.pack(pady=10, padx=10)

        texto3= "Max relative error:"
        texto3_1,texto3_2 = error.numeric_get_range_max_relative_error()
        result_frame3 = tk.Label(analysis_window, text=f"{texto3} ({texto3_1},{texto3_2})", wraplength=350,
                            bg="#34495E", fg="white", font=("Arial", 12),
                            height=3, width=40)
        result_frame3.pack(pady=10, padx=10)

        texto4= f"Relative error in f({x1}):"
        texto4_1,texto4_2= error.numeric_get_specific_relative_error()
        result_frame4 = tk.Label(analysis_window, text=f"{texto4} ({texto4_1},{texto4_2})", wraplength=350,
                            bg="#34495E", fg="white", font=("Arial", 12),
                            height=3, width=40)
        result_frame4.pack(pady=10, padx=10)

        texto5= "Max condition:"
        texto5_1,texto5_2= error.numeric_get_range_max_condition()
        result_frame5 = tk.Label(analysis_window, text=f"{texto5} ({texto5_1},{texto5_2})", wraplength=350,
                            bg="#34495E", fg="white", font=("Arial", 12),
                            height=3, width=40)
        result_frame5.pack(pady=10, padx=10)

        texto6= f"Condition en f({x1}):"
        texto6_1,texto6_2 = error.numeric_get_specific_condition()
        result_frame6 = tk.Label(analysis_window, text=f"{texto6} ({texto6_1},{texto6_2})", wraplength=350,
                            bg="#34495E", fg="white", font=("Arial", 12),
                            height=3, width=40)
        result_frame6.pack(pady=10, padx=10)

        # Buttons
        plot_frame = tk.Frame(analysis_window, bg="#2C3E50")
        plot_frame.pack(pady=10)

      
        def AbsolutePlotter():
           plotter = AbsoluteErrorPlotter()
           x_values, error_values = error.numeric_get_range_absolute_error()
           plotter.plot(x_values,error_values,(texto1_1,texto1_2),(texto2_1,texto2_2),equationString)
           
        def RelativePlotter():
           plotter = RelativeErrorPlotter()
           x_values, error_values = error.numeric_get_range_relative_error()
           plotter.plot(x_values,error_values,(texto3_1,texto3_2),(texto4_1,texto4_2),equationString)  

        def ConditionPlot():
           plotter = ConditionPlotter()
           x_values, error_values = error.numeric_get_range_condition()
           plotter.plot(x_values,error_values,(texto5_1,texto5_2),(texto6_1,texto6_2),equationString)       
           
        plot1_btn = tk.Button(plot_frame, text="PLOT Absol.", font=("Arial", 12, "bold"),
                         bg="#27AE60", fg="white", width=10, height=1,command=AbsolutePlotter)
        plot1_btn.pack(side=tk.LEFT, padx=5)

        plot2_btn = tk.Button(plot_frame, text="PLOT Relat", font=("Arial", 12, "bold"),
                         bg="#2980B9", fg="white", width=10, height=1,command=RelativePlotter)
        plot2_btn.pack(side=tk.LEFT, padx=5)

        plot3_btn = tk.Button(plot_frame, text="PLOT Condit.", font=("Arial", 12, "bold"),
                         bg="#8E44AD", fg="white", width=10, height=1,command=ConditionPlot)
        plot3_btn.pack(side=tk.LEFT, padx=5)

        close_frame = tk.Frame(analysis_window, bg="#2C3E50")
        close_frame.pack(pady=10)

        close_btn = tk.Button(close_frame, text="CLOSE", font=("Arial", 12, "bold"),
                         bg="#E74C3C", fg="white", width=10, height=1,
                         command=analysis_window.destroy)
        close_btn.pack()

        


    calculate_btn = tk.Button(action_frame, text="CALCULATE", font=("Arial", 12, "bold"),
                            bg="#27AE60", fg="white", width=12, height=1,
                            command=calculate)
    calculate_btn.pack(side=tk.LEFT, padx=5)

    
    plot_btn = tk.Button(action_frame, text="PLOT", font=("Arial", 12, "bold"),
                        bg="#E74C3C", fg="white", width=12, height=1,
                        command=Plot)
    plot_btn.pack(side=tk.LEFT, padx=5)

    error_btn = tk.Button(action_frame, text="ANALYSIS", font=("Arial", 12, "bold"),
                         bg="#8E44AD", fg="white", width=12, height=1,
                         command=error_analysis)
    error_btn.pack(side=tk.LEFT, padx=5)

    clear_btn = tk.Button(action_frame, text="CLEAR", font=("Arial", 12, "bold"),
                         bg="#95A5A6", fg="white", width=8, height=1,
                         command=ClearEverything)
    clear_btn.pack(side=tk.LEFT, padx=5)
    

    root.mainloop()

