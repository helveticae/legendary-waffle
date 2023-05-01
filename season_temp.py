import numpy as np

def get_weather(current_time):
    
    # Default sunny
    weather = 0
    temperature = get_temperature(current_time)

    # Always rainy in autumn
    if get_season(current_time) == 3:
        weather = 2

    # Always snowy when -10 to -1 temperature
    if temperature > -10 or temperature < 0:
        weather = 3
    return weather

    # For later reference
    weather = [0,1,2,3]
    weather_map = ['sunny', 'cloudy', 'rainy', 'snowy']


def get_temperature(current_time):
    season = get_season(current_time)
    base_temp = 10

    rng = np.random.uniform(-.60,.60)

    # Seasonal modifier
    if season == 0:
        s_mod = -2
    elif season == 1:
        s_mod = 1
    elif season == 2:
        s_mod = 2
    elif season == 3:
        s_mod = -1
    else:
        raise ValueError("Invalid season value")

    sun = 0 #TODO
    #if sunshine == True: 
    #    sun = 1

    summer_mod = summer_heat(current_time.days) # Add hot peak during summer

    return round((100 * summer_mod) * (sun * s_mod) + rng + (base_temp * s_mod))

def get_season(current_time):
    if current_time.days > 70 or current_time.days < 10:
        return 0
    elif current_time.days > 10 and current_time.days < 30:
        return 1
    elif current_time.days > 30 and current_time.days < 50:
        return 2
    elif current_time.days > 50 and current_time.days < 70:
        return 3
    else:
        raise ValueError("Invalid day value")

    # For later reference
    season = [0,1,2,3]
    season_map = ["Winter", "Spring", "Summer", "Autumn"]


def summer_heat(n, target_peak=50):
    """
    A small peak in temperature (0.0 to 0.08) at given peak.

    n = days
    target_peak = hottest day
    """

    if n == 0 or n == 80:
        return 0  # same output for day 0 and 80
    
    std_dev = 5  # standard deviation of the normal distribution
    mean = target_peak  # mean of the normal distribution
    
    exponent = -((n - mean) ** 2) / (2 * std_dev ** 2)
    factor = 1 / (std_dev * np.sqrt(2 * np.pi))
    output = factor * np.e ** exponent
    
    # Small fluctuate "pre-summer"
    if 1 <= n <= 25:
        output *= 32 + 1.12 * (n * 200)
    
    return output

if __name__ == "__main__":
    import matplotlib.pyplot as plt # for testing

    outputs = []
    for i in range(81):
        modified_num = summer_heat(i)
        outputs.append(modified_num)

    plt.plot(range(81), outputs)
    plt.xlabel('Input')
    plt.ylabel('Modified output')
    plt.show()