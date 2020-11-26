import ip138
import common
import pandas as pd
if __name__ == '__main__':
    ground_truth = pd.read_csv("gov.csv")
    ips = ground_truth['ip'].head(30).values.tolist()
    common.m_addrs_to_csv(ips, ip138, 'ip138_gov.csv')