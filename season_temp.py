import numpy as np

def logistic_bump(n, k=-0.1):
    """
    A smooth logistic bump.
    Default output values for 80 days are 0 to 2.

    k: slope
    n: days
    """

    if n < 0 or n > 80:
        return None
    
    max_value = 1 / (1 + np.exp(-k)) # maximum value of the logistic function
    return (1 / (1 + np.exp(k * n)) - 1 / (1 + np.exp(k * (n - 80)))) / max_value

def summer_heat(n, target_peak_day=50):
    """
    A tiny, smooth peak in temperature (0.0 to 0.08) at given target_peak_day.

    n: days
    target_peak_day: hottest day
    """

    if n == 0 or n == 80:
        return 0  # same output for day 0 and 80
    
    std_dev = 5  # standard deviation of the normal distribution
    mean = target_peak_day  # mean of the normal distribution
    
    exponent = -((n - mean) ** 2) / (2 * std_dev ** 2)
    factor = 1 / (std_dev * np.sqrt(2 * np.pi))
    output = factor * np.e ** exponent
    
    # Small fluctuate "pre-summer"
    if 1 <= n <= 25:
        output *= 32 + 1.12 * (n * 200)
    
    return output


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
    bump = logistic_bump(current_time.days) # Add smoother higher temperature up until day 50 (peak summer)

    # TODO: This equation is broken, also TODO: add colder temp during night
    return round(s_mod * (1 + rng + summer_mod) * (base_temp + bump) + sun)

def get_season(current_time):
    if current_time.days > 70 or current_time.days < 10:
        return 0
    elif current_time.days >= 10 and current_time.days < 30:
        return 1
    elif current_time.days >= 30 and current_time.days < 50:
        return 2
    elif current_time.days >= 50 and current_time.days < 70:
        return 3
    else:
        raise ValueError("Invalid day value")

    # For later reference
    season = [0,1,2,3]
    season_map = ["Winter", "Spring", "Summer", "Autumn"]


if __name__ == "__main__":
    import matplotlib.pyplot as plt # for testing

    #outputs = []
    #for i in range(81):
    #    modified_num = summer_heat(i)
    #    outputs.append(modified_num)

    #plt.plot(range(81), outputs)
    #plt.xlabel('Input')
    #plt.ylabel('Modified output')
    #plt.show()
    
    outputs = []
    for i in range(81):
        modified_num = logistic_bump(i)
        outputs.append(modified_num)

    plt.plot(range(81), outputs)
    plt.xlabel('Input')
    plt.ylabel('Modified output')
    plt.show()