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

## How to Run the Project

# Setting Up the Project

## Step 1: Set Up a Virtual Environment 1. **Create the Environment**: ```bash python -m venv .venv ``` 2. **Activate the Environment**: - For Git Bash: ```bash source .venv/Scripts/activate ``` - For Command Prompt: ```bash .venv\Scripts\activate ```

## Step 2: Install Dependencies 1. Install required Python libraries: ```bash pip install -r requirements.txt ```

## Step 3: Add API Key 1. **Create a `.env` File**: - In the project folder, create a file named `.env`. 2. **Add the API Key**: ```makefile TMDB_API_KEY=your_api_key_here ``` Replace `your_api_key_here` with your actual API key.

## Step 4: Run the Analysis 1. **Execute the Script**: ```bash python analyze_data.py ``` 2. **Review Outputs**: - **Graphs**: Visualizations showing the number of horror movies per year and political events categorized by crisis type. - **Debug Outputs**: Preview datasets and detect any issues in the terminal.

## Step 5: Test the Project 1. **Run Unit Tests**: ```bash pytest tests/ ``` 2. **Verify Outputs**: - Ensure the script processes data correctly (e.g., movie release years, political categorizations). - Manually review debug outputs for errors or missing data.

## Step 6: Wrap Up 1. **Deactivate the Virtual Environment**: ```bash deactivate ``` 2. **Explore and Share**: - Use the generated graphs for discussions or assignments. - Provide feedback or suggestions via the GitHub repository.

---

# Key Insights 1. **Horror Movie Trends**: Peaks in horror movie production often align with societal crises, suggesting that cultural anxieties influence creative narratives. 2. **Crisis Types**: Categories such as "Cultural," "Cold War," and "Civil Rights" prominently appear in certain years, reflecting their potential impact on horror movie themes. 3. **Evolving Genre**: Trends highlight the horror genre’s role in reflecting societal fears and political challenges.

---

# Challenges and Improvements 1. **Legend Complexity**: Simplify by grouping similar crisis types into broader categories for clarity. 2. **Readability**: Improve x-axis label presentation by rotating or filtering by decades. 3. **Focused Analysis**: Deepen insights by filtering data by specific decades or crisis types.

---

# Conclusion This project demonstrates the intersection of horror films and political climates, showcasing the horror genre as a lens for examining societal fears and political anxieties. By analyzing films across decades, this work emphasizes the genre's cultural significance and evolution in response to societal changes.
