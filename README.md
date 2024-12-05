# Horror Movies and Political Climate Analysis

## Project Overview
This project analyzes popular horror movies to explore how they reflect or respond to the political environment of their respective decades. By examining the themes, plots, and societal anxieties presented in these films, the project draws connections between the horror genre and the sociopolitical context of the times.

## Features
This project includes data collection of horror movies by decade, including titles, release years, box office performance, and critical reception. It also examines political events or movements occurring during each film's release decade, highlights correlations between horror film themes and political climates through charts and graphs, and features an interactive dashboard that allows users to explore data by decade or political event.

## Tools and Technologies
The project uses Python for data analysis and visualization. Libraries such as Pandas are used for data manipulation and analysis, Matplotlib/Seaborn for data visualization, and Beautiful Soup or Scrapy for web scraping movie data. APIs include the IMDb API to gather movie-related data (e.g., genre, ratings) and political event databases for documenting political events. Data is stored in CSV format, with SQLite optionally used for structured storage.

## Integration Plan
The integration plan begins with data collection of horror movie data and political event data. The next step is to clean and preprocess the data to ensure consistency, followed by exploratory data analysis (EDA) to uncover patterns in the data. Visualizations are then created to represent findings, and the project concludes with developing an interactive dashboard to present the analysis.

## Problem Description
There is often a disconnect between popular culture, particularly film, and the sociopolitical issues that shape society. This project bridges this gap by showing how horror movies serve as a lens for understanding historical and political contexts.

## Opportunities and Goals
The primary goal of this project is to analyze how horror movies from various decades reflect and respond to the political environment of their times. Additional goals include identifying patterns by linking recurring themes in horror films to political events, exploring how horror films address marginalized groups and social justice issues, creating timelines mapping notable horror films against political events, and presenting findings through a structured report or dashboard.

## Evaluation Methods
Evaluation methods include unit testing to ensure individual code components function correctly, integration testing to ensure modules work seamlessly together, and user acceptance testing (UAT) to gather end-user feedback before rollout. User feedback will be gathered through surveys, focus groups, and interviews to gauge usability. Performance metrics will track error rates, task completion rates, and application performance.

## Project Steps and Instructions
To set up this project, start by installing Python 3.7 or higher. Ensure you have it installed on your system by visiting [Python's official website](https://www.python.org/downloads/). Set up a virtual environment using the following command:

```bash
python -m venv env
Activate the virtual environment:

For Mac/Linux:
bash
Copy code
source env/bin/activate
For Windows:
bash
Copy code
.\env\Scripts\activate
Install dependencies with:

bash
Copy code
pip install -r requirements.txt
To run the scripts, begin with the web scraper to fetch movie data:

bash
Copy code
python web_scraper.py
Next, convert political events from Excel to CSV format:

bash
Copy code
python convert_excel_to_csv.py
Combine movie and political event datasets:

bash
Copy code
python data_integration.py
Perform analysis and generate visualizations:

bash
Copy code
python analyze_data.py
Visualizations are saved as .png files in the project directory. Open and review these visualizations to explore the insights.

To push changes to GitHub, stage and commit your changes:

bash
Copy code
git add .
git commit -m "Updated project with analysis and visualizations"
Then push changes:

bash
Copy code
git push
Conclusion
This project reveals the intersection of horror movies and political climates across decades, highlighting the horror genre as a medium for cultural commentary and historical reflection.