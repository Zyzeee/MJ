import tkinter as tk
from tkinter import *
import math

window = tk.Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Converter")
window.configure(bg="#C3E0E5")


def ieee74_window():
    ieee74_window = Toplevel(window)
    ieee74_window.title("IEE74 CONVERTER")

    def binaryOfFraction(fraction):
        binary = str()
        while fraction:
            fraction *= 2
            if fraction >= 1:
                int_part = 1
                fraction -= 1
            else:
                int_part = 0
            binary += str(int_part)
        return binary

    def floatingPoint(real_no):
        sign_bit = 0
        if real_no < 0:
            sign_bit = 1
        real_no = abs(real_no)
        int_str = bin(int(real_no))[2:]
        fraction_str = binaryOfFraction(real_no - int(real_no))
        ind = int_str.index('1')
        exp_str = bin((len(int_str) - ind - 1) + 127)[2:]
        mant_str = int_str[ind + 1:] + fraction_str
        mant_str = mant_str + ('0' * (23 - len(mant_str)))
        return sign_bit, exp_str, mant_str

    def convert():
        inp = float(entry.get())
        sign_bit, exp_str, mant_str = floatingPoint(inp)
        ieee_32 = str(sign_bit) + '|' + exp_str + '|' + mant_str
        result_label.config(text="IEEE 754 representation of {} is:\n{}".format(inp, ieee_32))

    # Create input field
    entry = tk.Entry(ieee74_window)
    entry.pack()

    # Create convert button
    convert_button = tk.Button(ieee74_window, text="Convert", command=convert)
    convert_button.pack()

    # Create label for displaying the result
    result_label = tk.Label(ieee74_window, text="")
    result_label.pack()


ieee74_btn = tk.Button(
    text="IEEE74 CONVERTER",
    width=25,
    height=10,
    bg="#41729F",
    fg="white",
    command=ieee74_window
)
ieee74_btn.pack()


def openmethod_window():
    openmethod_window = Toplevel(window)
    openmethod_window.title("OPEN METHOD")
    greeting = tk.Label(
        openmethod_window,
        text="Instruction: Please use ** instead of ^ for the exponent. and Use * for a monomial with variable x, e.g., 2x ; 2*x",
        fg="white",
        bg="black",
    )
    greeting.pack()

    def newton_raphson_method():
        openmethod_window = Toplevel(window)
        openmethod_window.title("OPEN METHOD")
        greeting = tk.Label(
            openmethod_window,
            text="Instruction: Please use ** instead of ^ for the exponent. and Use * for a monomial with variable x, e.g., 2x ; 2*x",
            fg="white",
            bg="black",
            )
        greeting.pack()
    
    def newton_raphson_method(eq, x0, pr):
        def evaluate_equation(x):
            return eval(eq.replace('x', repr(x)), {'e': math.e, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'log': math.log})

        def newtonRaphson(expression, x0, precision, max_iterations=100):
            x = sp.Symbol('x')
            f = sp.sympify(expression)
            f_prime = f.diff(x)

            x_n = x0
            iteration = 1

            result_text = "  i   |   x0    |   xN    |   y0    |   yN    \n"

            while iteration <= max_iterations:
                f_value = evaluate_equation(x_n)
                f_prime_value = evaluate_equation(str(f_prime))

                x_n_minus_1 = x_n

                if abs(f_prime_value) < 1e-10:
                    result_text += "Derivative value too close to zero. Exiting."
                    break

                x_n = x_n - f_value / f_prime_value

                result_text += "{:^5d} | {:^7.4f} | {:^7.4f} | {:^7.4f} | {:^7.4f}\n".format(iteration, x_n_minus_1, x_n, f_value, evaluate_equation(x_n))

                if abs(x_n - x_n_minus_1) < precision:
                    break

                iteration += 1

            result_text += "\nRoot Value: {:^7.4f}".format(x_n)
            result_label.config(text=result_text)

        # Create input fields
        equation_label = tk.Label(openmethod_window, text="Equation:")
        equation_label.pack()
        equation_entry = tk.Entry(openmethod_window)
        equation_entry.pack()

        x0_label = tk.Label(openmethod_window, text="x0:")
        x0_label.pack()
        x0_entry = tk.Entry(openmethod_window)
        x0_entry.pack()

        precision_label = tk.Label(openmethod_window, text="Precision:")
        precision_label.pack()
        precision_entry = tk.Entry(openmethod_window)
        precision_entry.pack()

        newton_button = tk.Button(openmethod_window, text="Newton Raphson Method", command=newton_raphson_method)
        newton_button.pack()

        # Create label for displaying the result
        result_label = tk.Label(openmethod_window, text="")
        result_label.pack()

    def secant_method():
        eq = equation_entry_sec.get()
        XA = float(XA_entry.get())
        XB = float(XB_entry.get())
        pr = float(precision_entry_sec.get())

        def evaluate_equation(x):
            return eval(eq.replace('x', repr(x)), {'e': math.e, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'log': math.log})

        result_text = "Iteration |     XA    |     XB    |     XN    |     YA    |     YB    |     YN    \n"

        YB = round(evaluate_equation(XB), 4)
        YA = round(evaluate_equation(XA), 4)

        for i in range(1, 100):
            if YA == YB:
                break

            XN = XA - (YA * (XA - XB) / (YA - YB))
            YN = round(evaluate_equation(XN), 4)

            result_text += "{:^9d} | {:^9.4f} | {:^9.4f} | {:^9.4f} | {:^9.4f} | {:^9.4f} | {:^9.4f}\n".format(i, XA, XB, XN, YA, YB, YN)

            if abs(XA - XB) < pr:
                break

            XA = XB
            XB = XN
            YA = YB
            YB = YN

        result_text += "Root Value: {:^7.4f}".format(round(XN, 4))
        result_label_sec.config(text=result_text)

    # Create input fields for Newton Raphson method
    equation_label = tk.Label(openmethod_window, text="Equation:")
    equation_label.pack()
    equation_entry = tk.Entry(openmethod_window)
    equation_entry.pack()

    x0_label = tk.Label(openmethod_window, text="x0:")
    x0_label.pack()
    x0_entry = tk.Entry(openmethod_window)
    x0_entry.pack()

    precision_label = tk.Label(openmethod_window, text="Precision:")
    precision_label.pack()
    precision_entry = tk.Entry(openmethod_window)
    precision_entry.pack()

    newton_button = tk.Button(openmethod_window, text="Newton Raphson Method", command=newton_raphson_method)
    newton_button.pack()

    # Create label for displaying the result of Newton Raphson method
    result_label = tk.Label(openmethod_window, text="")
    result_label.pack()

    # Create input fields for Secant method
    equation_label_sec = tk.Label(openmethod_window, text="Equation:")
    equation_label_sec.pack()
    equation_entry_sec = tk.Entry(openmethod_window)
    equation_entry_sec.pack()

    XA_label = tk.Label(openmethod_window, text="XA:")
    XA_label.pack()
    XA_entry = tk.Entry(openmethod_window)
    XA_entry.pack()

    XB_label = tk.Label(openmethod_window, text="XB:")
    XB_label.pack()
    XB_entry = tk.Entry(openmethod_window)
    XB_entry.pack()

    precision_label_sec = tk.Label(openmethod_window, text="Precision:")
    precision_label_sec.pack()
    precision_entry_sec = tk.Entry(openmethod_window)
    precision_entry_sec.pack()

    secant_button = tk.Button(openmethod_window, text="Secant Method", command=secant_method)
    secant_button.pack()

    # Create label for displaying the result of Secant method
    result_label_sec = tk.Label(openmethod_window, text="")
    result_label_sec.pack()


openmethod_btn = tk.Button(
    text="OPEN METHOD",
    width=25,
    height=5,
    bg="#41729F",
    fg="white",
    command=openmethod_window
)
openmethod_btn.pack()


# Add remaining code for the Bracket and Jacobi methods


def bracketmethod_window():
    bracketmethod_window = Toplevel(window)
    bracketmethod_window.title("BRACKET METHOD")

    def bisection_method():
        print("You choose Bisection Method")
        print("Instruction: Pls use ** instead of ^ for the exponent. and Use * for monomial with variable x ex: 2x ; 2*x")
        eq = equation_entry.get()
        equation_entry.pack()
        XL = float(XL_entry.get())
        XL_entry.pack()
        XR = float(XR_entry.get())
        XR_entry.pack()
        pr = float(pr_entry.get())
        pr_entry.pack()
        

        YL = eval(eq.replace('x', repr(XL)))
        YR = eval(eq.replace('x', repr(XR)))

        if XL >= XR:
            result_label.config(text="Assumption is incorrect. Please try again. XL should be smaller than XR")
        elif YL * YR >= 0:
            result_label.config(text="Assumption is incorrect. Please try again. YL and YR should have opposite signs")
        else:
            prev_values = [XL, (XL + XR) / 2, XR, eval(eq.replace('x', repr(XL))), eval(eq.replace('x', repr((XL + XR) / 2))), eval(eq.replace('x', repr(XR)))]

            for i in range(100):
                XM = round((XL + XR) / 2, 4)
                YL = round(eval(eq.replace('x', f'{XL:.4f}')), 4)
                YR = round(eval(eq.replace('x', f'{XR:.4f}')), 4)
                YM = round(eval(eq.replace('x', f'{XM:.4f}')), 4)

                print((i + 1), XL, XM, XR, YL, YM, YR)

                if YL * YM < 0:
                    XR = XM
                elif YL * YM > 0:
                    XL = XM
                else:
                    break

                current_values = [XL, XM, XR, YL, YM, YR]
                if current_values == prev_values:
                    break
                prev_values = current_values

            result_label.config(text="Root Value: {}".format(XM))

    def false_position_method():
        print("You choose False Position Method")
        print("Instruction: Pls use ** instead of ^ for the exponent. and Use * for monomial with variable x ex: 2x ; 2*x")
        eq = equation_entry.get()
        XL = float(XL_entry.get())
        XR = float(XR_entry.get())
        pr = float(pr_entry.get())

        def evaluate_equation(x):
            return eval(eq.replace('x', repr(x)), math.__dict__)
    
        YL = eval(eq.replace('x', repr(XL)))
        YR = eval(eq.replace('x', repr(XR)))

        if XL >= XR:
            print("Assumption is incorrect. Please try again. XL should be smaller than XR")
        elif YL * YR >= 0:
            print("Assumption is incorrect. Please try again. YL and YR should have opposite signs")
        else:
            prev_values = [XL, (XL + XR) / 2, XR, evaluate_equation(XL), evaluate_equation((XL + XR) / 2), evaluate_equation(XR)]

            # Print table header
            result_text = "Iteration |   XL    |   XM    |   XR    |   YL    |   YM    |   YR    \n"

            for i in range(100):
                XM = round((XL * YR - XR * YL) / (YR - YL), 4)
                YL = round(evaluate_equation(XL), 4)
                YR = round(evaluate_equation(XR), 4)
                YM = round(evaluate_equation(XM), 4)

                # Print table row
                result_text += "{:^9d} | {:^9.4f} | {:^9.4f} | {:^9.4f} | {:^9.4f} | {:^9.4f} | {:^9.4f}\n".format(i+1, XL, XM, XR, YL, YM, YR)

                if YL * YM < 0:
                    XR = XM
                elif YL * YM > 0:
                    XL = XM
                else:
                    break

                current_values = [XL, XM, XR, YL, YM, YR]
                if current_values == prev_values:
                    break
                prev_values = current_values
                
            result_text += "Root Value: {:^7.4f}".format(round(XM, 4))
            
            result_label.config(text=result_text)

            print("Root Value:", XM)
        
                
    equation_label = tk.Label(bracketmethod_window, text="Equation:")
    equation_label.pack()
    equation_entry = tk.Entry(bracketmethod_window)
    equation_entry.pack()

    XL_label = tk.Label(bracketmethod_window, text="XL:")
    XL_label.pack()
    XL_entry = tk.Entry(bracketmethod_window)
    XL_entry.pack()

    XR_label = tk.Label(bracketmethod_window, text="XR:")
    XR_label.pack()
    XR_entry = tk.Entry(bracketmethod_window)
    XR_entry.pack()

    pr_label = tk.Label(bracketmethod_window, text="Precision:")
    pr_label.pack()
    pr_entry = tk.Entry(bracketmethod_window)
    pr_entry.pack()

    false_button = tk.Button(bracketmethod_window, text="False Position Method", command=false_position_method)
    false_button.pack()

    result_label = tk.Label(bracketmethod_window, text="")
    result_label.pack()

    
           
bracketmethod_btn = tk.Button(
    text="BRACKET METHOD",
    width=25,
    height=5,
    bg="#41729F",
    fg="white",
    command=bracketmethod_window
)
bracketmethod_btn.pack()


def jacobimethod_window():
    new_window = Toplevel(window)
    new_window.title("JACOBI METHOD")
    # Add code for the Jacobi method window


jacobimethod_btn = tk.Button(
    text="JACOBI METHOD",
    width=25,
    height=5,
    bg="#41729F",
    fg="white",
    command=jacobimethod_window
)
jacobimethod_btn.pack()

window.mainloop()
