# SMA_project

- SP500_List.csv: a list of S&P500 stocks labeled with noise (0/1).
- raw_videos.json: a json file mapping all scrapped videos to stock tickers. e.g., {“A”: {video with attributes…}, “AAPL”: {….} …}
- Ticker_Channel.csv: a table mapping the top 20 channel to ticker. Columns of the table are ['Ticker', 'Stock_Name', 'noise', 'Channel_Name', 'Channel_link’].
- Channel_Ticker.csv: a table  mapping tickers to channel. Columns of the table are ['Channel_Name', 'Channel_Link', 'Ticker', 'Stock_Name’].
- crawler_v2.ipynb: the Jupiter notebook that documents the whole process with detailed descriptions.
- youtube_crawler.py: python file that contains a function to scrape all YouTube videos (with views >= 1000) of one stock, sorted by relevance (default).
