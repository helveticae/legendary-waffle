import sqlite3

class WorldTime:
    """
    ~ Tempus edax rerum.
    """

    SECONDS_PER_DAY = 10 * 60  # 10 minutes IRL = 1 day ingame
    DAYS_PER_YEAR = 80         # 80 days ingame = 1 year

    def __init__(self, days=0, hours=0, minutes=0, seconds=0, year=0):
        total_seconds = (days * self.DAYS_PER_YEAR * self.SECONDS_PER_DAY) + \
                        (hours * 60 * 60) + \
                        (minutes * 60) + \
                        seconds
        self.days = total_seconds // (self.DAYS_PER_YEAR * self.SECONDS_PER_DAY)
        remaining_seconds = total_seconds % (self.DAYS_PER_YEAR * self.SECONDS_PER_DAY)
        self.hours = (remaining_seconds // (60 * 60)) % 24
        self.minutes = (remaining_seconds // 60) % 60
        self.seconds = remaining_seconds % 60
        self.year = year

        # Increment year if 80 days have elapsed
        if self.days >= self.DAYS_PER_YEAR:
            self.year += self.days // self.DAYS_PER_YEAR
            self.days = self.days % self.DAYS_PER_YEAR

    def __str__(self):
        return f"Year {self.year}, day {self.days}, {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

if __name__ == "__main__":
    # Testing
    current_time = WorldTime(124, 912, 2, 2, 1)
    print(current_time)
    current_time = WorldTime(0, 0, 2, 2, 0)
    print(current_time)