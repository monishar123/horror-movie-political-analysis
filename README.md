# Horror Movies and Political Climate Analysis

## Project Overview
This project aims to analyze popular horror movies across various decades to explore how their themes, narratives, and societal anxieties reflect and respond to the political environment of their respective times. By identifying key films, examining political contexts, and creating visualizations, this project seeks to demonstrate the role of the horror genre as a cultural commentary.

---

## Goals

### Primary Goal
To analyze popular horror movies from various decades to understand how their themes, narratives, and societal anxieties reflect and respond to the political environment of their respective times.

### Additional Goals/Objectives
1. **Identify Patterns**: Examine recurring themes and motifs within horror films across different decades, linking them to significant political events and societal changes.
2. **Cultural Analysis**: Investigate how horror films portray marginalized groups and address social justice issues, highlighting the genre's evolution in response to shifting societal attitudes.
3. **Create a Visual Representation**: Develop a timeline or visual aid that maps the release of notable horror films against major political events to illustrate correlations between film and political climate.
4. **Engage with Audiences**: Present findings through a well-structured report or presentation that invites discussion about the implications of horror films in reflecting societal fears and the political landscape.

---

## Features
- Data collection of horror movies by decade, including titles, release years, and box office performance.
- Analysis of political events or movements occurring during the decade of each film’s release.
- Visualization of trends showing correlations between horror film themes and political climates.

---

## Tools and Technologies
- **Programming Languages**: Python (for data analysis and visualization)
- **Libraries**:
  - Pandas: For data manipulation and analysis
  - NumPy: For numerical computations
- **APIs**:
  - IMDb API: To gather movie-related data (e.g., genre, ratings)
  - Political Event Databases: APIs or datasets that document political events (e.g., US government archives, Wikipedia)
- **Web Development**:
  - HTML/CSS/JavaScript: For developing a user-friendly interface
- **Data Sources**:
  - IMDb, Rotten Tomatoes: For movie data
  - News APIs: For political context and related articles

---

## How to Run the Project

### Prerequisites
- Install Python 3.7 or higher.
- Install required libraries:
  ```bash
  pip install -r requirements.txt

### Steps to Run the Project

1. **Collect Data**:
   - Run the data collection script to fetch horror movie data:
     ```bash
     python collect_movies.py
     ```
   - Retrieve political event data using the API integration script:
     ```bash
     python collect_political_data.py
     ```

2. **Process Data**:
   - Clean and preprocess the collected data:
     ```bash
     python preprocess_data.py
     ```

3. **Analyze Data**:
   - Perform analysis to identify patterns and trends:
     ```bash
     python analyze_data.py
     ```

4. **Visualize Results**:
   - Generate visualizations such as timelines or trend graphs:
     ```bash
     python generate_visualizations.py
     ```

5. **Run the User Interface**:
   - Launch the UI for interactive exploration:
     ```bash
     python app.py
     ```
   - Access the interface at `http://localhost:5000`.
### How to Test the Project

1. **Unit Testing**:
   - Test individual scripts (e.g., data collection, analysis) using:
     ```bash
     pytest tests/
     ```

2. **Integration Testing**:
   - Ensure modules like data processing and visualization work together:
     ```bash
     python integration_test.py
     ```

3. **User Testing**:
   - Open the user interface and test the following functionalities:
     - Search for specific movies or political events.
     - Filter results by decade, movie title, or political event.

4. **Performance Metrics**:
   - Evaluate system performance by tracking:
     - Response time for queries.
     - Accuracy of data retrieval.

### Conclusion

This project highlights the intersection of horror films and political climates, showcasing the horror genre as a lens through which societal fears and political anxieties are reflected. By analyzing horror movies across decades and comparing them to major political events, this project demonstrates the role of the genre as a form of cultural commentary.

Through data collection, analysis, visualization, and an interactive user interface, this project provides insights into how the horror genre evolves in response to societal changes and challenges. It invites audiences to explore the connections between film and political history, fostering a deeper understanding of the cultural significance of horror movies.

The findings from this project can serve as a foundation for further exploration of popular culture as a response to societal issues, encouraging discussion about how media reflects and influences our perceptions of the world.

