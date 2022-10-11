def add_time(start, duration, display_day = False):

    days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    start_h, start_min_am_pm = start.split(":")
    start_min, am_pm = start_min_am_pm.split()
    dur_h, dur_min = duration.split(":")

    if am_pm == "AM" and int(start_h) == 12:
        start_h = 0

    end_h = int(start_h) + int(dur_h)
    end_min = int(start_min) + int(dur_min)
    end_am_pm = am_pm
    days_passed = 0

    if end_min >= 60:
        end_h += end_min // 60
        end_min = end_min % 60

    if end_h >= 12:
        if am_pm == "AM":
            days_passed = end_h // 24
            end_h = end_h % 24
            if end_h >= 12:
                end_am_pm = "PM"
                end_h -= 12
        elif am_pm == "PM":
            end_h += 12
            days_passed = end_h // 24
            end_h = end_h % 24
            if end_h >= 12:
                end_am_pm = "PM"
            else: end_am_pm = "AM"

    if end_h == 0:
        end_h = 12

    new_time = f"{end_h}:{end_min:02} {end_am_pm}"

    if display_day != False:
        current_day_index = days_of_week.index(display_day.lower().capitalize())
        end_day_index = (current_day_index + days_passed) % 7
        end_day = days_of_week[end_day_index]
        new_time += f", {end_day}"

    if days_passed > 0:
        if days_passed == 1:
            days_passed = " (next day)"
        else: days_passed = f" ({days_passed} days later)"
        new_time += days_passed

    return new_time

