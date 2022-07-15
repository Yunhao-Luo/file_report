import os
import csv
from tkinter.tix import Tree
from turtle import color, width
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages

class DataReport:
    def __init__(self, path):
        self.path = path
        self.data = []
        self.file_names = []

    def read_files(self):
        os.chdir(self.path)
        for file in os.listdir():
            self.data.append([])
            file_content = self.data[-1]
            self.file_names.append(file.split(" ")[0])
            with open(file) as csvfile:
                content = csv.reader(csvfile, delimiter=',')
                for row in content:
                    line_dict = {}
                    file_content.append(line_dict)
                    line_dict["Elasped"] = row[1]
                    line_dict["Prescribed"] = row[2]
                    line_dict["Source"] = row[3]
                    line_dict["Name"] = row[4]

        for file in self.data:
            file.pop(0)
            for row in range(0, len(file)-1):
                file[row]["Time"] = int(file[row+1].get("Elasped")) - int(file[row].get("Elasped"))

        for file in self.data:
            for line in file[:]:
                if (line["Source"] != "Marker") or "START" in line["Name"]:
                    file.remove(line)
        self.file_num = len(self.data)

    def get_time(self):
        time_data = []
        for file in self.data:
            time_data.append([])
            time_content = time_data[-1]
            time_content.append(0)
            total_time = 0
            for line in file:
                time_content.append(int(line["Time"]) + total_time)
                total_time+=int(line["Time"])
        return time_data
    
    def get_name(self):
        name_data = []
        for file in self.data:
            name_data.append([])
            name_content = name_data[-1]
            for line in file:
                name = line["Name"].split(" ")[0]
                name_content.append(name)
            for i in range(0, len(name_content)-1):
                if name_content[i] == name_content[i+1]:
                    name_content[i] = ""
        return name_data

    def get_subsessions(self):
        session_data = []
        for line in self.data[0]:
            name = line["Name"]
            session_data.append(name)
        return session_data

    def get_subsession_time(self):
        subsession_time = []
        for file in self.data:
            subsession_time.append([])
            subsession_content = subsession_time[-1]
            for line in file:
                subsession_content.append(line["Time"])
        return subsession_time

    def get_prescribed(self, sub_name):
        for file in self.data:
            for line in file:
                if sub_name in line["Name"]:
                    return line["Prescribed"]

    def get_session_time(self):
        session_time_list = []
        for file in self.data:
            session_time_list.append([])
            file_sessions = session_time_list[-1]
            name = ""
            for line in file:
                if name != line["Name"].split(" ")[0]:
                    file_sessions.append(line["Time"])
                else:
                    file_sessions[-1] += line["Time"]
                name = line["Name"].split(" ")[0]
        return session_time_list
    
    def get_pres_setime(self):
        session_time_list = []
        for file in self.data:
            session_time_list.append([])
            file_sessions = session_time_list[-1]
            name = ""
            for line in file:
                if name != line["Name"].split(" ")[0]:
                    file_sessions.append(int(line["Prescribed"]))
                else:
                    file_sessions[-1] += int(line["Prescribed"])
                name = line["Name"].split(" ")[0]
        return session_time_list

    def plot_normal_line(self):
        time_data = self.get_time()
        name_data = self.get_name()
        for l in name_data:
            l.insert(0, '')
        fig, ax = plt.subplots(len(self.data)*2,1, figsize=(15,self.file_num))
        levels = np.tile([1,1,1,1,1,1],
                 int(np.ceil(len(time_data[0])/6)))[:len(time_data[0])]
        session_time = self.get_session_time()
        prese_time = self.get_pres_setime()
        for file_num in range(0,len(self.data)*2):
            if file_num % 2 == 0:
                time_list = time_data[int(file_num/2)]
                name_list = name_data[int(file_num/2)]
                ax[file_num].vlines(time_list, 0, levels, color="tab:red")  # The vertical stems.
                ax[file_num].plot(time_list, np.zeros_like(time_list), "-o",
                        color="k", markerfacecolor="w")  # Baseline and markers on it.
                # annotate lines
                for d, l, r in zip(time_list, levels, name_list):
                    ax[file_num].annotate(r, xy=(d, l),
                                xytext=(7, np.sign(l)-3), textcoords="offset points",
                                horizontalalignment="right",
                                verticalalignment="bottom" if l > 0 else "top")
                # remove y axis and spines
                ax[file_num].yaxis.set_visible(False)
                ax[file_num].xaxis.set_visible(False)
                ax[file_num].spines[["left", "top", "right", "bottom"]].set_visible(False)
                ax[file_num].margins(y=0.5)
                ax[file_num].margins(x=0)
            else:
                single_file_session = session_time[int(file_num/2)]
                single_file_prese = prese_time[int(file_num/2)]
                count = 0
                ec = None
                for time in range(0, len(single_file_session)):
                    if single_file_prese[time] <= single_file_session[time]:
                        ec = 'r'
                    else:
                        ec = None
                    if time%2 == 0:
                        ax[file_num].barh(self.file_names[int(file_num/2)], single_file_session[time], left = count, color='b', edgecolor=ec, hatch='//')
                    else:
                        ax[file_num].barh(self.file_names[int(file_num/2)], single_file_session[time], left = count, color='c', edgecolor=ec, hatch='//')
                    count += int(single_file_session[time])
                ax[file_num].xaxis.set_visible(False)
                ax[file_num].spines[["left", "top", "right", "bottom"]].set_visible(False)
                ax[file_num].margins(y=0)
                ax[file_num].margins(x=0)
        export_pdf.savefig()
        #plt.show()
    
    def get_individual_time(self, sub_name):
        res = []
        subsession = self.get_subsession_time()
        subsession_name = self.get_subsessions()
        for i in range(0, len(subsession_name)):
            if subsession_name[i]==sub_name:
                for j in subsession:
                    res.append(j[i])
        return res
    
    def find_max_time(self):
        whole_list = []
        for file in self.data:
            for line in file:
                whole_list.append(int(line["Prescribed"]))
        subsession_list = self.get_subsession_time()
        for file in subsession_list:
            whole_list+=file
        return max(whole_list)
    
    def get_name_start(self):
        name_data = []
        for file in self.data:
            name_data.append([])
            name_content = name_data[-1]
            for line in file:
                name = line["Name"].split(" ")[0]
                name_content.append(name)
            current_str = name_content[0]
            for i in range(1, len(name_content)):
                if name_content[i] == current_str:
                    name_content[i] = ""
                else:
                    current_str = name_content[i]
        return name_data

    def plot_detail(self):
        num_subsession = len(self.get_name()[0])
        subsession_name = self.get_subsessions()
        fig, ax = plt.subplots(int(num_subsession),1, figsize=(15, self.file_num*21))
        current_session = ""
        color_change = False
        session_list = []
        for file in self.get_name_start():
            session_list+=file
        for sub_sec in range(0, int(num_subsession)):
            if current_session != subsession_name[sub_sec].split(" ")[0]:
                color_change = not color_change
            current_session = subsession_name[sub_sec].split(" ")[0]
            time_list = self.get_individual_time(subsession_name[sub_sec])
            if color_change:
                ax[sub_sec].barh(self.file_names, time_list, color="b")
            else:
                ax[sub_sec].barh(self.file_names, time_list, color="c")
            prescribed_line = [int(self.get_prescribed(subsession_name[sub_sec]))]*len(self.file_names)
            ax[sub_sec].plot(prescribed_line, self.file_names, color="r", linewidth=3)
            ax[sub_sec].set_title(subsession_name[sub_sec][subsession_name[sub_sec].find(" ")+1:])
            if session_list[sub_sec] != "":
                ax[sub_sec].set_title(session_list[sub_sec], loc="left")
            ax[sub_sec].xaxis.set_visible(False)
            ax[sub_sec].margins(y=0.1)
            ax[sub_sec].xaxis.set_visible(False)
            ax[sub_sec].spines[["left", "top", "right", "bottom"]].set_visible(False)
            ax[sub_sec].margins(y=0.1)
            ax[sub_sec].axis(xmin=0,xmax=self.find_max_time())
        """ plt.subplots_adjust(
                    top=0.5) """
        export_pdf.savefig()
        #plt.show()




if __name__ == "__main__":
    path = os.getcwd() + "\sessionlogsforprismdatareportingproject"
    test = DataReport(path)
    test.read_files()
    print(test.file_num)
    with PdfPages(r'C:\Users\WorldViz.VIZBOX-03\Desktop\Charts.pdf') as export_pdf:
        test.plot_normal_line()
        test.plot_detail()
    plt.close