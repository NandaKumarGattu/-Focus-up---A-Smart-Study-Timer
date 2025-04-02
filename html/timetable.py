from typing import List, Dict
import random
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Subject:
    name: str
    level: int  # 1 to 5, where 5 is highest priority
    weekly_hours: int

class TimetableGenerator:
    def __init__(self, working_hours: tuple = (8, 16)):
        self.start_hour, self.end_hour = working_hours
        self.daily_slots = (self.end_hour - self.start_hour)
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
    def generate_timetable(self, subjects: List[Subject]) -> Dict:
        # Sort subjects by level (priority) in descending order
        subjects.sort(key=lambda x: x.level, reverse=True)
        
        # Initialize empty timetable
        timetable = {day: ['Free' for _ in range(self.daily_slots)] 
                    for day in self.weekdays}
        
        # Track allocated hours for each subject
        allocated_hours = defaultdict(int)
        
        # Allocate subjects to timetable
        for subject in subjects:
            remaining_hours = subject.weekly_hours
            
            while remaining_hours > 0:
                # Try to find a suitable slot
                day = random.choice(self.weekdays)
                hour = random.randint(0, self.daily_slots - 1)
                
                if timetable[day][hour] == 'Free':
                    timetable[day][hour] = subject.name
                    allocated_hours[subject.name] += 1
                    remaining_hours -= 1
        
        return timetable
    
    def print_timetable(self, timetable: Dict):
        # Print header
        print("\nTIMETABLE\n")
        print("Time", end="\t")
        for day in self.weekdays:
            print(f"{day:12}", end="\t")
        print("\n" + "="*80)
        
        # Print schedule
        for hour in range(self.daily_slots):
            current_time = f"{self.start_hour + hour:02d}:00"
            print(f"{current_time}", end="\t")
            
            for day in self.weekdays:
                print(f"{timetable[day][hour]:12}", end="\t")
            print()

def main():
    # Example usage
    subjects = [
        Subject("Mathematics", level=5, weekly_hours=6),
        Subject("Physics", level=4, weekly_hours=4),
        Subject("Chemistry", level=4, weekly_hours=4),
        Subject("English", level=3, weekly_hours=4),
        Subject("History", level=2, weekly_hours=3),
    ]
    
    # Create timetable generator
    generator = TimetableGenerator(working_hours=(8, 16))
    
    # Generate and print timetable
    timetable = generator.generate_timetable(subjects)
    generator.print_timetable(timetable)

if __name__ == "__main__":
    main()