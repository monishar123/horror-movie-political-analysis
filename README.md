# Horror Movies and Political Climate Analysis

## Project Overview
This project analyzes popular horror movies across various decades to explore how their themes, narratives, and societal anxieties reflect and respond to the political environments of their times. By identifying key films, examining political contexts, and creating visualizations, this project demonstrates the role of the horror genre as a form of cultural commentary.

---

## Goals

### Primary Goal
- **Analyze popular horror movies from various decades** to understand how their themes, narratives, and societal anxieties reflect and respond to the political environment of their respective times.

### Additional Goals
1. **Identify Patterns**: Examine recurring themes and motifs within horror films across different decades, linking them to significant political events and societal changes.
2. **Cultural Analysis**: Investigate how horror films portray marginalized groups and address social justice issues, highlighting the genre's evolution in response to shifting societal attitudes.
3. **Create a Visual Representation**: Develop a timeline or visual aid that maps the release of notable horror films against major political events.
4. **Engage with Audiences**: Present findings through a well-structured report or presentation that invites discussion about the implications of horror films in reflecting societal fears and the political landscape.

---

## Features
- **Data Collection**: Includes horror movies by decade (titles, release years, box office performance).
- **Political Context**: Analysis of political events or movements coinciding with each film’s release decade.
- **Visualization**: Illustrates correlations between horror film themes and political climates.

---

## Tools and Technologies
- **Programming Languages**: Python (for data analysis and visualization)
- **Libraries**:
  - Pandas (data manipulation and analysis)
  - NumPy (numerical computations)
- **APIs**:
  - IMDb API (for movie data: genre, ratings)
  - Political event databases (e.g., US government archives, Wikipedia)
- **Web Development**: HTML/CSS/JavaScript for a user-friendly interface
- **Data Sources**:
  - IMDb and Rotten Tomatoes (movie data)
  - News APIs (political context and articles)

---

## How to Run the Project

### Step 1: Access the Repository
1. Visit the [GitHub Repository](https://github.com/monishar123/horror-movie-political-analysis).
2. **Download the Project**:
   - Clone with HTTPS: `git clone <repository_url>`
   - Download ZIP: Extract the project to a folder on your computer.

### Step 2: Set Up the Environment
1. **Install Python**: Ensure Python 3.8 or higher is installed.
2. **Navigate to the Project Folder**:  
   ```bash
   cd /path/to/your/project
Setting Up the Project
Step 1: Set Up a Virtual Environment
Create the Environment:
bash
Copy code
python -m venv .venv
Activate the Environment:
For Git Bash:
bash
Copy code
source .venv/Scripts/activate
For Command Prompt:
bash
Copy code
.venv\Scripts\activate
Step 2: Install Dependencies
Install required Python libraries:
bash
Copy code
pip install -r requirements.txt
Step 3: Add API Key
Create a .env File:
In the project folder, create a file named .env.
Add the API Key:
makefile
Copy code
TMDB_API_KEY=your_api_key_here
Replace your_api_key_here with your actual API key.
Step 4: Run the Analysis
Execute the Script:
bash
Copy code
python analyze_data.py
Review Outputs:
Graphs: Visualizations showing the number of horror movies per year and political events categorized by crisis type.
Debug Outputs: Preview datasets and detect any issues in the terminal.
Step 5: Test the Project
Run Unit Tests:
bash
Copy code
pytest tests/
Verify Outputs:
Ensure the script processes data correctly (e.g., movie release years, political categorizations).
Manually review debug outputs for errors or missing data.
Step 6: Wrap Up
Deactivate the Virtual Environment:
bash
Copy code
deactivate
Explore and Share:
Use the generated graphs for discussions or assignments.
Provide feedback or suggestions via the GitHub repository.
Key Insights
Horror Movie Trends: Peaks in horror movie production often align with societal crises, suggesting that cultural anxieties influence creative narratives.
Crisis Types: Categories such as "Cultural," "Cold War," and "Civil Rights" prominently appear in certain years, reflecting their potential impact on horror movie themes.
Evolving Genre: Trends highlight the horror genre’s role in reflecting societal fears and political challenges.
Challenges and Improvements
Legend Complexity: Simplify by grouping similar crisis types into broader categories for clarity.
Readability: Improve x-axis label presentation by rotating or filtering by decades.
Focused Analysis: Deepen insights by filtering data by specific decades or crisis types.
Conclusion
This project demonstrates the intersection of horror films and political climates, showcasing the horror genre as a lens for examining societal fears and political anxieties. By analyzing films across decades, this work emphasizes the genre's cultural significance and evolution in response to societal changes.