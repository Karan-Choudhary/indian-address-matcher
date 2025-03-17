import pandas as pd
from src.address_matcher import AddressMatcher
from tqdm import tqdm
from pandarallel import pandarallel

tqdm.pandas()
pandarallel.initialize(progress_bar=True)


def load_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df


def start_test(df):
    matcher = AddressMatcher(threshold=0.60, fuzzy_threshold=85)
    df['match'] = df.parallel_apply(lambda x: matcher.match_with_details(x['given_address'], x['address_preprocessed']), axis=1)
    return df


def main():
    csv_path = 'address_testset.csv'
    data = load_csv(csv_path)
    data = start_test(data)
    breakpoint()


if __name__ == "__main__":
    main()