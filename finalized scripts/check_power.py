import pandas as pd
import os
import scipy.stats as st
import statistics as stats


def power_analysis(sd, average_observation, difference_percent=0.10, alpha=0.05, beta=0.2):
    """
    :param sd: standard deviation of reference population data
    :param average_observation: Mean of reference population data
    :param difference_percent: Decimal percent difference you want to detect. Eg. 0.05 -> 5% change detected
    :param alpha: p_value
    :param beta: power is 1-beta. Power of 80% translates to beta of 0.2
    :return: number of samples needed
    """
    z_alpha = st.norm.ppf(1 - alpha)
    z_beta = st.norm.ppf(1 - beta)
    n_samples = (2 * pow(sd, 2) * pow(z_alpha + z_beta, 2)) / pow(average_observation * difference_percent, 2)
    return n_samples


df = pd.read_excel(r"C:\Users\Acer\Desktop\DEPTH.xlsx".replace("\\", os.sep))
col_names = df.columns
num_samples = []

for column in col_names:
    try:
        print(column + ":" + str(power_analysis(sd=stats.stdev(df[column]),
                                                average_observation=stats.mean(df[column]))))
        num_samples.append(power_analysis(sd=stats.stdev(df[column]),
                                          average_observation=stats.mean(df[column])))
    except Exception as e:
        print(e)


# organized_df = pd.DataFrame(list(zip(col_names, num_samples)))
# organized_df.to_excel(r"C:\Users\Acer\Desktop\power05.xlsx".replace("\\", os.sep))

organized_df = pd.DataFrame(list(zip(col_names, num_samples)))
