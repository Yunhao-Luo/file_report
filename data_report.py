import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

class DataReport:
    def __init__(self, path):
        self.path = path
        self.data = []

    def read_files(self):
        os.chdir(self.path)
        for file in os.listdir():
            self.data.append([])
            file_content = self.data[-1]
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

    def get_time(self):
        time_data = []
        for file in self.data:
            time_data.append([])
            time_content = time_data[-1]
            for line in file:
                time_content.append(int(line["Elasped"]) + int(line["Time"]))
        return time_data
    
    def get_name(self):
        name_data = []
        for file in self.data:
            name_data.append([])
            name_content = name_data[-1]
            for line in file:
                name = line["Name"].split(" ")[0]
                name_content.append(name)
        return name_data

    def plot_normal_line(self):
        time_data = self.get_time()
        name_data = self.get_name()
        fig, ax = plt.subplots(len(self.data),1)
        levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(time_data[0])/6)))[:len(time_data[0])]
        for file_num in range(0,len(self.data)):
            time_list = time_data[file_num]
            name_list = name_data[file_num]
            ax[file_num].vlines(time_list, 0, levels, color="tab:red")  # The vertical stems.
            ax[file_num].plot(time_list, np.zeros_like(time_list), "-o",
                    color="k", markerfacecolor="w")  # Baseline and markers on it.

            # annotate lines
            for d, l, r in zip(time_list, levels, name_data):
                ax[file_num].annotate(r, xy=(d, l),
                            xytext=(-3, np.sign(l)*3), textcoords="offset points",
                            horizontalalignment="right",
                            verticalalignment="bottom" if l > 0 else "top")

            # remove y axis and spines
            ax[file_num].yaxis.set_visible(False)
            ax[file_num].xaxis.set_visible(False)
            ax[file_num].spines[["left", "top", "right"]].set_visible(False)

            ax[file_num].margins(y=0.1)

        plt.show()



if __name__ == "__main__":
    path = os.getcwd() + "\sessionlogsforprismdatareportingproject"
    test = DataReport(path)
    test.read_files()
    print("finish reading")
    """  for file in test.data:
        print("new file")
        for line in file:
            print(line)
            pass """
    res = test.get_time()
    for i in res:
        print(len(i))
        print(i)

    res = test.get_name()
    for i in res:
        print(len(i))
        print(i)

    test.plot_normal_line()