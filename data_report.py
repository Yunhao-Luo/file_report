import os
import csv

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
            for line in file:
                if (line["Source"] != "Marker") or "START" in line["Name"]:
                    file.remove(line)
    
    def plot_normal_line(self):
        pass



if __name__ == "__main__":
    path = os.getcwd() + "\sessionlogsforprismdatareportingproject"
    test = DataReport(path)
    test.read_files()
    print("finish reading")
    for file in test.data:
        print("new file")
        for line in file:
            print(line)
            pass