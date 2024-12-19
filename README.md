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

Step 1: Setting Up the Project
Download the Project

Clone the repository or download it as a ZIP file from GitHub.
If downloading as ZIP, extract the files to a folder on your computer.
Install Python
Ensure Python (version 3.8 or higher) is installed on your computer. You can download it from python.org.

Navigate to the Project Folder
Open a terminal (Command Prompt, Git Bash, etc.) and go to the project directory:

bash
Copy code
cd ~/path/to/horror-movie-political-analysis
Activate the Virtual Environment

For Git Bash:
bash
Copy code
source .venv/Scripts/activate
For Command Prompt:
bash
Copy code
.venv\Scripts\activate
Install Required Libraries
Install the necessary Python packages:

bash
Copy code
pip install -r requirements.txt
Step 2: Preparing the Project
Add Your API Key
If the project uses an API (like TMDB), you need an API key:

Create a file named .env in the project folder.
Add this line:
makefile
Copy code
TMDB_API_KEY=your_api_key_here
Replace your_api_key_here with your actual API key.
Verify the Setup
Ensure the virtual environment is active, and all dependencies are installed.

Step 3: Running the Project
Analyze the Data
Run the analysis script to process the data and generate outputs:

bash
Copy code
python analyze_data.py
Review the Outputs
The script will generate:

Graphs showing the number of movies released per year and political events categorized by type.
Debug information in the terminal, such as dataset previews (movies_df and political_df).
Adjust If Needed
If any errors appear (e.g., missing columns or data issues), update the script to match the dataset structure.

Step 4: Testing the Project
Unit Testing
Test specific parts of the project with:

bash
Copy code
pytest tests/
Integration Testing
Run the main script again to ensure all parts work together:

bash
Copy code
python analyze_data.py
Performance Check
Check how long the script takes to run:

bash
Copy code
time python analyze_data.py
Step 5: Wrap Up
Deactivate the Virtual Environment
When finished, deactivate the environment:

bash
Copy code
deactivate
Explore and Share
Use the graphs and analysis as teaching tools. Feel free to share feedback or suggestions to improve the project.

### Movies by Crisis and Year

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

