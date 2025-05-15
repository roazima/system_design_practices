class Workout:
    def __init__(self, workout_type, workout_time, workout_date):
        self.workout_type = workout_type
        self.workout_time = workout_time
        self.workout_date = workout_date

    def to_string(self):
        return f"{self.workout_type}, {self.workout_time} , {self.workout_date} "

class wokroutLogger:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_workout(self,workout):
        with open(self.file_path, "a") as f:
            f.write(workout.to_string() + "\n")
    def load_workout(self):
        with open(self.file_path, "r") as l:
            lines = l.readlines()
            for line in lines:
                print(line.strip())


w1 = Workout("Run" , 15, "2025-04-02")
logger = wokroutLogger("workout_info.txt")
logger.save_workout(w1)
logger.load_workout()