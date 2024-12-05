# Horror Movies and Political Climate Analysis

This project explores how popular horror movies reflect or respond to the political environments of their respective decades. By analyzing themes, plots, and societal anxieties, we aim to draw connections between the horror genre and sociopolitical contexts over time.

## Features
- **Data Collection**: Horror movies by decade, including titles, release years, box office performance, and critical reception.
- **Political Context Analysis**: Examination of political events and movements occurring during each film’s release decade.
- **Visualizations**: Trends illustrating correlations between horror film themes and political climates.
- **Interactive Dashboard**: A user-friendly interface to explore data by decade or political event.

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**:
  - `pandas` for data manipulation and analysis.
  - `matplotlib`/`seaborn` for data visualization.
  - `Beautiful Soup`/`Scrapy` for web scraping (if needed).
- **APIs**:
  - IMDb API for movie-related data.
  - Political Event Databases for documenting significant historical events.
- **Data Storage**: SQLite or CSV files for datasets.

## Problem Statement
While horror movies are a staple of American cinema, their potential as a lens for understanding historical and political contexts is often overlooked. This project bridges the gap by exploring how horror films engage with societal fears and reflect political climates.

## Goals
### Primary Goal
To analyze horror movies across decades, understanding how their themes and narratives reflect societal anxieties and political environments.

### Additional Goals
1. **Identify Patterns**: Highlight recurring themes and motifs in horror films linked to significant political events.
2. **Cultural Analysis**: Examine portrayals of marginalized groups and social justice issues.
3. **Visual Representations**: Develop visual aids mapping movie releases against political events.
4. **Engagement**: Present findings in an accessible format, inviting discussions on societal and political reflections in horror films.

## Integration Plan
1. Collect horror movie and political event data.
2. Clean and preprocess data for consistency.
3. Perform exploratory data analysis (EDA) to identify patterns.
4. Create visualizations to highlight findings.
5. Develop an interactive dashboard for user exploration.

## Evaluation Methods
- **Testing**: Unit testing, integration testing, and user acceptance testing (UAT) for functionality.
- **User Feedback**: Surveys, focus groups, and interviews to assess usability and satisfaction.
- **Performance Metrics**:
  - Usage statistics: User engagement and task completion rates.
  - Error rates: Track bugs and issues.
  - Load times and response times: Ensure smooth performance.

## Post-Launch Evaluation
- Conduct follow-up surveys to gauge long-term impact.
- Use performance metrics to identify areas for iterative improvement.

## Conclusion
This project demonstrates how horror films reflect societal fears and engage with the political landscapes of their times. By leveraging data analysis, visualizations, and interactive tools, we uncover the genre's role as a medium for cultural commentary and historical reflection.

---

## Running the Project

### Prerequisites
- Python installed on your machine.
- Required libraries installed via `pip install -r requirements.txt`.

### Steps to Run
1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/your-repo/horror-movie-analysis.git
   cd horror-movie-analysis
2. Set Virtual Environment
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
3. Install Dependencies:
pip install -r requirements.txt
4. Run Data Integration:
python data_integration.py
5. Analyze Data:
python analyze_data.py
6. Visualize Data: Visualizations are generated using matplotlib and seaborn. Run the visualization script:
python visualize_data.py
7. View Results: Results are saved as .png files in the project directory for review.
