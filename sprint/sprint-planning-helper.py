import sys, pandas, numpy as np
from operator import itemgetter

def sprint_planning(path, velocity):
        dataframe = pandas.read_csv(path, skiprows=0)
        dataset = dataframe.values
        tasks = dataset[:,:].astype(float)
        numrows = len(tasks)
        arr=[[] for i in range(numrows)]
        for task_row in range(numrows):
            params_array = (tasks[task_row,2]/tasks[task_row,1]) #KSP/story_points parameter
            arr[task_row].append(params_array)
        tasks = np.insert(tasks,3, values=0, axis=1)
        counter = 0
        for task_row in tasks:
            task_row[3]=arr[counter][0]
            counter += 1
        tasks_sorted = sorted(tasks, key=itemgetter(3,-1), reverse=True)
        tasks_array = np.array(tasks_sorted)
        story_points_counter(numrows, tasks_array, velocity)

def story_points_counter(numrows, tasks_array, velocity):
            story_points = 0.0
            tasks_ids = []
            for element_index in range(0,numrows):
                story_points = story_points + tasks_array[element_index][1]
                if story_points > velocity:
                    story_points = story_points - tasks_array[element_index][1]
                else:
                    tasks_ids.append(tasks_array[element_index][0])
                    if story_points == velocity:
                        break
            numrows2 = len(tasks_ids)
            for element_idx in range(0,numrows2):
                tasks_ids[element_idx] = str(int(tasks_ids[element_idx]))
                if element_idx < len(tasks_ids)- 1:
                    sys.stdout.write(tasks_ids[element_idx]+", ")
                else:
                    sys.stdout.write(tasks_ids[element_idx]+'\n')

if __name__ == '__main__':
    path = str(sys.argv[1])
    velocity = int(sys.argv[2])
    sprint_planning(path, velocity)
