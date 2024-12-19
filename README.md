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
Step 1: Access the Repository
Visit the Repository
Open the project on GitHub at this link:
Horror Movie and Political Analysis

Download the Project

Click the green Code button on the repository page.
Choose one of the following:
Clone with HTTPS: Copy the URL and use git clone in your terminal.
Download ZIP: Download the project as a ZIP file and extract it to a folder on your computer.
Step 2: Set Up the Environment
Install Python
Make sure Python (version 3.8 or higher) is installed. Download it from python.org.

Navigate to the Project Folder
Open a terminal and change to the project directory. Replace /path/to/your/project with the actual path to the folder:

bash
Copy code
cd /path/to/your/project
Set Up a Virtual Environment
Create and activate a virtual environment:

Create the environment:
bash
Copy code
python -m venv .venv
Activate the environment:
For Git Bash:
bash
Copy code
source .venv/Scripts/activate
For Command Prompt:
bash
Copy code
.venv\Scripts\activate
Install Dependencies
Install the required Python libraries:

bash
Copy code
pip install -r requirements.txt
Step 3: Add API Key
If the project requires an API key (e.g., TMDB API), you’ll need to set it up:

Create a file named .env in the project folder.
Add the following line to the file:
makefile
Copy code
TMDB_API_KEY=your_api_key_here
Replace your_api_key_here with your actual API key.
Step 4: Run the Analysis
Execute the Script
Run the main analysis script:

bash
Copy code
python analyze_data.py
Review the Outputs

Graphs will be generated showing:
The number of horror movies released per year.
Political events categorized by crisis type.
Debug outputs in the terminal will show previews of the datasets and any issues detected.
Step 5: Test the Project
Run Unit Tests
Test individual components using:

bash
Copy code
pytest tests/
Verify Outputs
Check that the script processes data correctly, including movie release years and political event categorizations.

Manually Review
Review debug outputs for any missing data or errors.

Step 6: Wrap Up
Deactivate the Environment
When finished, deactivate the virtual environment:

bash
Copy code
deactivate
Explore and Share
Use the graphs and insights for class discussions or assignments. Feel free to provide feedback or suggestions for improvements via the GitHub repository.

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

