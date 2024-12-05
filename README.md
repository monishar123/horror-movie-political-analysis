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

1. **Activate Virtual Environment**:
   - Navigate to your project directory:
     ```bash
     cd ~/Documents/Projects/horror-movie-analysis-main/horror-movie-political-analysis
     ```
   - Activate the virtual environment:
     - For **Git Bash**:
       ```bash
       source .venv/Scripts/activate
       ```
     - For **Command Prompt**:
       ```cmd
       .venv\Scripts\activate
       ```

2. **Install Dependencies**:
   - Ensure all required packages are installed:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Environment Variables**:
   - If your project uses an API key (like TMDB API key), create a `.env` file in your project’s root directory with the following content:
     ```text
     TMDB_API_KEY=your_api_key_here
     ```
   - Make sure to replace `your_api_key_here` with your actual API key.

4. **Run the Data Analysis Script**:
   - Execute the script to load, process, and analyze the movie and political events data:
     ```bash
     python analyze_data.py
     ```

5. **Review Output**:
   - The script will generate:
     - A graph of the number of movies released per year.
     - A graph showing political events categorized by crisis type.
   - Check the terminal for any debug output, such as:
     - Column names in the datasets (`movies_df`, `political_df`).
     - Previews of the datasets using `.head()`.

6. **Update the Script (if needed)**:
   - Based on the debug output, ensure the script is using the correct column names. For example:
     ```python
     movies_df["release_date"] = pd.to_datetime(movies_df["<actual_column_name>"])
     ```

7. **Deactivate the Virtual Environment**:
   - After running the project, deactivate the virtual environment:
     ```bash
     deactivate
     ```

### Steps to Test the Project

1. **Verify Virtual Environment Activation**:
   - Ensure the virtual environment is active before running tests:
     ```bash
     source .venv/Scripts/activate  # Git Bash
     .venv\Scripts\activate         # Command Prompt
     ```

2. **Check Data Integrity**:
   - Run the analysis script to ensure data loads correctly:
     ```bash
     python analyze_data.py
     ```
   - Confirm the script outputs column names and previews for:
     - `movies_df` (Movies DataFrame)
     - `political_df` (Political Events DataFrame)

3. **Test Individual Functions**:
   - Use `pytest` to test individual components:
     ```bash
     pytest tests/
     ```
   - Ensure the following are tested:
     - Data loading functions for `movies.json` and `political_events.csv`.
     - Preprocessing logic, such as handling missing `release_date`.

4. **Integration Testing**:
   - Test how different modules work together:
     ```bash
     python analyze_data.py
     ```
   - Confirm the outputs match expectations:
     - Number of movies counted correctly.
     - Political events grouped and summarized by type.

5. **Manual User Testing**:
   - Manually review the debug outputs for errors or inconsistencies:
     - Are all required columns present (e.g., `release_date`)?
     - Are DataFrame previews showing expected data?

6. **Performance Testing**:
   - Check the runtime of the analysis script:
     ```bash
     time python analyze_data.py
     ```
   - Ensure the runtime is reasonable based on the dataset size.

7. **Log and Fix Errors**:
   - If issues are found:
     - Note the error in the debug output.
     - Update the script (e.g., correct column names or missing fields).
     - Re-run the tests.

8. **Deactivate the Virtual Environment**:
   - After completing tests, deactivate the environment:
     ```bash
     deactivate
     ```     ```
## Example Visualization: Movies by Crisis and Year

This project generates visualizations to explore the relationship between horror movie production and global political climates. Below is an example of a key visualization created during the analysis:

### Movies by Crisis and Year
![Movies by Crisis and Year](path/to/your/image.jpg)

### Description
This stacked bar chart shows the number of horror movies released each year and their correlation with various crisis types. Each bar represents a year, while the segments within each bar correspond to different types of crises (e.g., Cold War, Civil Rights, Technology).

### Key Insights
- The chart highlights peaks in horror movie production during certain crises, suggesting that societal anxieties may drive creative narratives within the genre.
- Crisis types like "Cultural," "Cold War," and "Civil Rights" appear prominently in some years, reflecting their potential influence on horror movie themes.

### Challenges and Improvements
- **Legend Complexity**: With a large number of crisis types, the legend can be overwhelming. Future iterations could group similar crises into broader categories for clarity.
- **Readability**: The x-axis labels are crowded and difficult to read. Adjustments like label rotation or filtering by decades may improve presentation.
- **Focused Analysis**: Filtering the data by specific decades or crisis categories can provide deeper insights into trends.

This visualization demonstrates the project’s ability to identify and analyze patterns between horror movie themes and global political climates, aligning with the overall goal of showcasing the genre as cultural commentary.

### Conclusion

This project highlights the intersection of horror films and political climates, showcasing the horror genre as a lens through which societal fears and political anxieties are reflected. By analyzing horror movies across decades and comparing them to major political events, this project demonstrates the role of the genre as a form of cultural commentary.

Through data collection, analysis, visualization, and an interactive user interface, this project provides insights into how the horror genre evolves in response to societal changes and challenges. It invites audiences to explore the connections between film and political history, fostering a deeper understanding of the cultural significance of horror movies.

The findings from this project can serve as a foundation for further exploration of popular culture as a response to societal issues, encouraging discussion about how media reflects and influences our perceptions of the world.

