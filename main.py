# “学生成绩管理系统”

#该系统功能如下：录入学生信息，包括学号、姓名、英语成绩、Python成绩、数学成绩、中文成绩、物理成绩、总成绩；
#并具有 GUI 界面，通过点击按钮，实现录入、查找、删除、修改、排序、统计平均分、显示、退出等功能。
#运用 matplotlib（可视化）完成成绩分布图，并且实现成绩的保存（保存学生信息到文件）功能。


import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
#matplotlib 是一个用于绘制图形和数据可视化的库。
#pyplot是matplotlib中的一个子模块，提供了一系列用于绘制图表的函数。


class Student:
    def __init__(self, student_id, name, english_score, python_score, math_score,chinese_score,physics_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.python_score = python_score
        self.math_score = math_score
        self.chinese_score = chinese_score
        self.physics_score = physics_score
        self.total_score = english_score + python_score + math_score + chinese_score + physics_score


class StudentManagementSystem:
    def __init__(self, master):
        # self.master 用于引用和操作Tkinter主窗口的属性，使在类的不同方法中能够方便地访问同一个窗口对象。
        self.master = master
        #设置系统标头。
        self.master.title("学生成绩管理系统")
        self.students = []

        self.main_menu()


    def main_menu(self):
        #主菜单界面
        for widget in self.master.winfo_children():
            widget.destroy()
        # winfo_children()返回的是一个包含所有子组件的列表，这些子组件是当前窗口或框架的直接子项

        #遍历当前窗口中的所有子组件（如标签、按钮等），并将它们从窗口中移除。
        #目的是为了在显示主菜单之前先清空任何现有的界面内容，确保用户看到的是最新的主菜单界面。

        tk.Label(self.master, text="学生成绩管理系统", font=("Arial", 20)).pack(pady=10)  #pady表示间距。
        # 使用Label小部件创建一个标签，并使用pack()方法将其添加到窗口中。

        tk.Button(self.master, text="录入学生信息", command=self.add_student_menu).pack(pady=5)
        tk.Button(self.master, text="查找学生信息", command=self.find_student_menu).pack(pady=5)
        tk.Button(self.master, text="删除学生信息", command=self.delete_student_menu).pack(pady=5)
        tk.Button(self.master, text="修改学生信息", command=self.modify_student_menu).pack(pady=5)
        tk.Button(self.master, text="排序学生信息", command=self.sort_students_menu).pack(pady=5)
        tk.Button(self.master, text="统计各科成绩", command=self.statistics_menu).pack(pady=5)
        tk.Button(self.master, text="显示所有学生信息", command=self.display_students).pack(pady=5)
        tk.Button(self.master, text="保存学生信息", command=self.save_students).pack(pady=5)
        tk.Button(self.master, text="加载学生信息", command=self.load_students).pack(pady=5)
        tk.Button(self.master, text="成绩分布图", command=self.plot_scores).pack(pady=5)
        tk.Button(self.master, text="退出", command=self.master.quit).pack(pady=5)
        #设置各个按钮。


    def add_student_menu(self):
        #录入学生信息界面。
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="录入学生信息", font=("Arial", 20)).pack(pady=10)

        tk.Label(self.master, text="学号").pack()
        student_id_entry = tk.Entry(self.master)  #tk.Entry()获取用户的单行文本输入。
        student_id_entry.pack()

        tk.Label(self.master, text="姓名").pack()
        name_entry = tk.Entry(self.master)
        name_entry.pack()

        tk.Label(self.master, text="英语成绩").pack()
        english_score_entry = tk.Entry(self.master)
        english_score_entry.pack()

        tk.Label(self.master, text="Python成绩").pack()
        python_score_entry = tk.Entry(self.master)
        python_score_entry.pack()

        tk.Label(self.master, text="数学成绩").pack()
        math_score_entry = tk.Entry(self.master)
        math_score_entry.pack()

        tk.Label(self.master, text="中文成绩").pack()
        chinese_score_entry = tk.Entry(self.master)
        chinese_score_entry.pack()

        tk.Label(self.master, text="物理成绩").pack()
        physics_score_entry = tk.Entry(self.master)
        physics_score_entry.pack()

        def save_student():
            #读取获得用户输入的信息，判断学生信息是否录入成功，并创建保存、返回按钮
            student_id = student_id_entry.get()
            name = name_entry.get()
            try:
                english_score = float(english_score_entry.get())
                python_score = float(python_score_entry.get())
                math_score = float(math_score_entry.get())
                chinese_score = float(chinese_score_entry.get())
                physics_score = float(physics_score_entry.get())

            except ValueError:
                messagebox.showerror("错误", "请输入有效的成绩")
                return

            if any(s.student_id == student_id for s in self.students):
                messagebox.showerror("错误", "学号已存在")
                return

            student = Student(student_id, name, english_score, python_score, math_score,chinese_score,physics_score)
            self.students.append(student)

            messagebox.showinfo("成功", "学生信息已录入")

            self.main_menu()

        tk.Button(self.master, text="保存", command=save_student).pack(pady=5)
        tk.Button(self.master, text="返回", command=self.main_menu).pack(pady=5)


    def find_student_menu(self):
        #查找学生信息界面
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="查找学生信息", font=("Arial", 20)).pack(pady=10)

        tk.Label(self.master, text="学号").pack()
        student_id_entry = tk.Entry(self.master)
        student_id_entry.pack()

        def find_student():
            #查找学生信息并显示
            student_id = student_id_entry.get()
            for student in self.students:
                if student.student_id == student_id:
                    messagebox.showinfo("学生信息", f"姓名: {student.name}\n英语成绩: {student.english_score}\nPython成绩: {student.python_score}\n数学成绩: {student.math_score}\n中文成绩：{student.chinese_score}\n物理成绩：{student.physics_score}\n总成绩: {student.total_score}")
                    return
            messagebox.showerror("错误", "未找到该学生")

        tk.Button(self.master, text="查找", command=find_student).pack(pady=5)
        tk.Button(self.master, text="返回", command=self.main_menu).pack(pady=5)


    def delete_student_menu(self):
        #删除学生信息界面
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="删除学生信息", font=("Arial", 20)).pack(pady=10)

        tk.Label(self.master, text="学号").pack()
        student_id_entry = tk.Entry(self.master)
        student_id_entry.pack()

        def delete_student():
            #删除学生信息
            student_id = student_id_entry.get()
            for student in self.students:
                if student.student_id == student_id:
                    self.students.remove(student)
                    messagebox.showinfo("成功", "学生信息已删除")
                    return
            messagebox.showerror("错误", "未找到该学生")

        tk.Button(self.master, text="删除", command=delete_student).pack(pady=5)
        tk.Button(self.master, text="返回", command=self.main_menu).pack(pady=5)


    def modify_student_menu(self):
        #修改学生信息界面
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="修改学生信息", font=("Arial", 20)).pack(pady=10)

        tk.Label(self.master, text="学号").pack()
        student_id_entry = tk.Entry(self.master)
        student_id_entry.pack()

        def modify_student():
            #查找学生并修改信息
            student_id = student_id_entry.get()
            for student in self.students:
                if student.student_id == student_id:
                    # 显示当前成绩并允许修改
                    tk.Label(self.master, text="新英语成绩").pack()
                    new_english_entry = tk.Entry(self.master)
                    new_english_entry.pack()

                    tk.Label(self.master, text="新Python成绩").pack()
                    new_python_entry = tk.Entry(self.master)
                    new_python_entry.pack()

                    tk.Label(self.master, text="新数学成绩").pack()
                    new_math_entry = tk.Entry(self.master)
                    new_math_entry.pack()

                    tk.Label(self.master, text="新中文成绩").pack()
                    new_chinese_entry = tk.Entry(self.master)
                    new_chinese_entry.pack()

                    tk.Label(self.master, text="新物理成绩").pack()
                    new_physics_entry = tk.Entry(self.master)
                    new_physics_entry.pack()

                    def save_changes():
                        #保存修改后的学生信息
                        try:
                            student.english_score = float(new_english_entry.get())
                            student.python_score = float(new_python_entry.get())
                            student.math_score = float(new_math_entry.get())
                            student.chinese_score = float(new_chinese_entry.get())
                            student.physics_score = float(new_physics_entry.get())

                        except ValueError:
                            messagebox.showerror("错误", "请输入有效的成绩")
                            return

                        student.total_score = student.english_score + student.python_score + student.math_score + student.chinese_score + student.physics_score
                        messagebox.showinfo("成功", "学生信息已修改")

                        self.main_menu()

                    tk.Button(self.master, text="保存", command=save_changes).pack(pady=5)
                    return
            messagebox.showerror("错误", "未找到该学生")

        tk.Button(self.master, text="查找", command=modify_student).pack(pady=5)
        tk.Button(self.master, text="返回", command=self.main_menu).pack(pady=5)


    def sort_students_menu(self):
       #排序学生信息的界面。
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="排序学生信息", font=("Arial", 20)).pack(pady=10)

        # 将学生总成绩依照降序排列。
        sorted_students = sorted(self.students, key=lambda s: s.total_score, reverse=True)

       # 创建一个 Canvas 和 Scrollbar
       # 使用 Canvas 时，可以很容易地实现滚动功能，特别是在内容超出可见区域时。通过结合 Scrollbar，用户可以上下或左右滚动查看内容。
       # 并创建一个垂直的 Scrollbar 用于滚动。scrollable_frame 是一个框架，用于容纳所有的学生信息标签。
        canvas = tk.Canvas(self.master)
        scrollbar = tk.Scrollbar(self.master, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

       # 当scrollable_frame的内容改变时，更新canvas的滚动区域，以确保可以滚动查看所有信息
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
       # 在 canvas 中创建一个窗口，将 scrollable_frame 放进去，并设置 canvas 和 scrollbar 的位置和填充方式。最后，将滚动条与 canvas 绑定。
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        display_text = "\n".join(
            [f"{student.student_id} {student.name} {student.total_score}" for student in sorted_students])

        # 在可滚动的 Frame 中添加学生信息标签
        for line in display_text.split('\n'):
            tk.Label(scrollable_frame, text=line).pack()

        tk.Button(self.master, text="返回", command=self.main_menu).pack(pady=5)


    def statistics_menu(self):
        #统计各科成绩界面
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="各科成绩统计", font=("Arial", 20)).pack(pady=10)

        if not self.students:
            tk.Label(self.master, text="没有学生信息").pack()
            tk.Button(self.master, text="返回", command=self.main_menu).pack(pady=5)
            return

        english_total = sum(student.english_score for student in self.students)
        python_total = sum(student.python_score for student in self.students)
        math_total = sum(student.math_score for student in self.students)
        chinese_total = sum(student.chinese_score for student in self.students)
        physics_total = sum(student.physics_score for student in self.students)

        avg_english = english_total / len(self.students)
        avg_python = python_total / len(self.students)
        avg_math = math_total / len(self.students)
        avg_chinese = chinese_total / len(self.students)
        avg_physics = physics_total / len(self.students)

        max_english = max(student.english_score for student in self.students)
        max_python = max(student.python_score for student in self.students)
        max_math = max(student.math_score for student in self.students)
        max_chinese = max(student.chinese_score for student in self.students)
        max_physics = max(student.physics_score for student in self.students)

        min_english = min(student.english_score for student in self.students)
        min_python = min(student.python_score for student in self.students)
        min_math = min(student.math_score for student in self.students)
        min_chinese = min(student.chinese_score for student in self.students)
        min_physics = min(student.physics_score for student in self.students)

        display_text = (f"英语平均分: {avg_english:.2f}\n"
                        f"Python平均分: {avg_python:.2f}\n"
                        f"数学平均分: {avg_math:.2f}\n"
                        f"中文平均分: {avg_chinese:.2f}\n"
                        f"物理平均分: {avg_physics:.2f}\n"
                        f"英语最高分: {max_english}, 最低分: {min_english}\n"
                        f"Python最高分: {max_python}, 最低分: {min_python}\n"
                        f"数学最高分: {max_math}, 最低分: {min_math}\n"
                        f"中文最高分: {max_chinese}, 最低分: {min_chinese}\n"
                        f"物理最高分: {max_physics}, 最低分: {min_physics}")

        tk.Label(self.master, text=display_text).pack(pady=10)
        tk.Button(self.master, text="返回", command=self.main_menu).pack(pady=5)


    def display_students(self):
        #显示所有学生信息界面。
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="所有学生信息", font=("Arial", 20)).pack(pady=10)

        if not self.students:
            tk.Label(self.master, text="没有学生信息").pack()
            tk.Button(self.master, text="返回", command=self.main_menu).pack(pady=5)
            return

        # 创建一个 Canvas 和 Scrollbar
        #使用 Canvas 时，可以很容易地实现滚动功能，特别是在内容超出可见区域时。通过结合 Scrollbar，用户可以上下或左右滚动查看内容。
        #并创建一个垂直的 Scrollbar 用于滚动。scrollable_frame 是一个框架，用于容纳所有的学生信息标签。
        canvas = tk.Canvas(self.master)
        scrollbar = tk.Scrollbar(self.master, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        #当scrollable_frame的内容改变时，更新canvas的滚动区域，以确保可以滚动查看所有信息。
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        #在 canvas 中创建一个窗口，将 scrollable_frame 放进去，并设置 canvas 和 scrollbar 的位置和填充方式。最后，将滚动条与 canvas 绑定。
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        # 遍历 self.students 列表，创建一个标签来显示每个学生的信息，包括学号、姓名和总分，每个标签之间有一定的垂直间距。
        for student in self.students:
            display_text = f"{student.student_id} {student.name} {student.total_score}"
            label = tk.Label(scrollable_frame, text=display_text, justify="center", anchor="center")
            label.pack(pady=5)  # 每个学生信息之间留一些空间。

        tk.Button(self.master, text="返回", command=self.main_menu).pack(pady=5)


    def save_students(self):
        #保存学生信息到文件
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        #filedialog.asksaveasfilename(),打开一个文件保存对话框，允许用户选择保存文件的路径和名称。
        # defaultextension = ".txt",指定默认扩展名为.txt，
        # filetypes限定文件类型为文本文件。

        if not file_path:
            return

        with open(file_path, 'w') as file:
            #打开指定路径的文件，以写入模式（'w'）打开。
            #以 'w' 模式打开一个文件时，Python会准备将数据写入该文件。
            for student in self.students:
                file.write(f"{student.student_id},{student.name},{student.english_score},{student.python_score},{student.math_score},{student.chinese_score},{student.physics_score}\n")

        messagebox.showinfo("成功", "学生信息已保存")  #显示保存成功消息框。


    def load_students(self):
        #从文件加载学生信息
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        #打开一个文件选择对话框，允许用户选择要加载的文件。这个文件应该是一个文本文件，包含学生的相关信息。

        if not file_path:
            return

        with open(file_path, 'r') as file:
            #'r'表示以只读模式打开文件。
            for line in file:
                #遍历文件中的每一行。
                student_id, name, english_score, python_score, math_score, chinese_score, physics_score= line.strip().split(',')
                #line.strip().split(',') 方法去掉行首尾的空白字符，并以逗号为分隔符将字符串分割成多个部分。每一部分对应学生的学号、姓名、英语成绩、Python成绩、数学成绩、中文成绩和物理成绩。

                student = Student(student_id, name, float(english_score), float(python_score), float(math_score), float(chinese_score), float(physics_score))
                self.students.append(student)

        messagebox.showinfo("成功", "学生信息已加载")


    def plot_scores(self):
        #绘制成绩分布图
        if not self.students:
            messagebox.showerror("错误", "没有学生信息")
            return

        subjects = ['English', 'Python', 'Math', 'Chinese', 'Physics']
        scores = [
            [student.english_score for student in self.students],
            [student.python_score for student in self.students],
            [student.math_score for student in self.students],
            [student.chinese_score for student in self.students],
            [student.physics_score for student in self.students]
        ]

        plt.boxplot(scores, labels=subjects)
        #plt.boxplot用于绘制箱线图（BoxPlot），箱线图是一种用于显示数据分布的图形，它能够清晰地展示数据的集中趋势、离散程度以及异常值。
        plt.title("Distribution of grades in various subjects")
        plt.ylabel("grade")  #设置y轴标签。
        plt.grid(color='blue',linestyle='--',linewidth=0.5)
        #用于在绘图中添加网格线。

        plt.show() #用于显示生成的图表。


if __name__ == "__main__":
    root = tk.Tk()
    # 表示创建一个主窗口，通过这个主窗口，可以添加各种GUI组件，并处理用户的输入和事件。

    app = StudentManagementSystem(root)
    # app = StudentManagementSystem()创建了StudentManagementSystem类的一个实例，并将其赋值给变量 app。
    # 通过app变量访问该类中的属性和方法，从而实现学生管理相关的功能。

    root.mainloop()
    #表示启动Tkinter的事件循环，等待用户与窗口的交互。