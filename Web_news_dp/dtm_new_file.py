import argparse
from datetime import datetime, timedelta
import pandas as pd
import json
import concurrent.futures
import re
from gnews import GNews

def parse_args():
    parser = argparse.ArgumentParser(description="Process news data for specified date range.")
    parser.add_argument("--start_date", required=True, help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end_date", required=True, help="End date in YYYY-MM-DD format")
    parser.add_argument("--max_results", type=int, default=10, help="Maximum results to fetch per country")
    return parser.parse_args()


def regexWordBoundary_replace_CaretDollar(regexString):
    MetaRegex = r"((?<!\\|\[)\^)|((?<!\\)\$)"
    CompiledMetaRegex = re.compile(MetaRegex)
    return CompiledMetaRegex.sub(r"\\b", regexString)

def fetch_news(country, start_date, end_date):
    google_news = GNews(language='en', max_results=10, start_date=start_date, end_date=end_date)
    terms = "Migration OR Flood OR Conflict"
    query = f"({terms}) AND {country}"
    news_results = google_news.get_news(query)
    for news in news_results:
        news['Country_Search'] = country
    return news_results

def main():
    args = parse_args()
    start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
    end_date = datetime.strptime(args.end_date, '%Y-%m-%d')

    # Load country data from CSV
    CtaConventions_RawDf = pd.read_csv("./Countries & Territories Taxonomy MVP - C&T Taxonomy with HXL Tags.csv")
    CtaConventionsDf = CtaConventions_RawDf.drop(index=[0], axis=0).copy()
    CtaConventionsDf['Adjusted_Regex'] = CtaConventionsDf['Regex'].apply(regexWordBoundary_replace_CaretDollar)

    with open('./countries_all.json') as f:
        country_data = json.load(f)
    countries = [country['name'] for country in country_data]

    all_news_items = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_news, country, start_date, end_date): country for country in countries}
        for future in concurrent.futures.as_completed(futures):
            all_news_items.extend(future.result())

    df = pd.DataFrame(all_news_items)
    df['Relevant_Term_Found'] = df.apply(lambda x: any(keyword in x['description'].lower() for keyword in ['migration', 'flood', 'conflict']), axis=1)
    filtered_df = df[df['Relevant_Term_Found']]

    # Use CSV data here if needed for further processing
    # Example: Match news items with country data using regex from CSV

    expanded_df = filtered_df.copy()
    expanded_df.to_excel(f"ExplodedRows_{args.start_date}_{args.end_date}.xlsx", index=False)

if __name__ == "__main__":
    main()
