<p align="center">
    <a href="https://sulu.io/" target="_blank">
        <img width="75%" src="img/01_ISEL-Logotipo-RGB_Horizontal.png" alt="ISEL logo">
    </a>


[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)](https://pandas.pydata.org)
[![Numpy](https://img.shields.io/badge/-Numpy-013243?&logo=NumPy)](https://numpy.org)
[![MatPlotLib](https://img.shields.io/badge/-Matplotlib-000000?style=flat&logo=python)](https://matplotlib.org)
[![Google Colab](https://img.shields.io/badge/google_colab-F9AB00?style=&logo=google-colab&logoColor=white)](https://colab.google)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![KG](https://img.shields.io/badge/tags-Knowledge%20Graph%2C%20LLM%2C%20Neo4j%2C%20University%20Data%2C%20Open%20Data-blue)
</p>

# PALEOBIOLOGY DATABASE ANALYSIS FOR STUDENTS
## A Beginner-Friendly Guide to Data Science in Paleontology

---

## 📚 COURSE OVERVIEW

### What You'll Learn:
1. How to download data from the Paleobiology Database
2. Basic exploratory data analysis (EDA) techniques
3. Data cleaning and preparation
4. Creating visualizations
5. Building a knowledge graph to show relationships

### Prerequisites:
- **NO programming experience required!**
- Basic understanding of paleontology (what you already know!)
- Python installed on your computer (we'll guide you)

### Slides Material:
- Open file named **DataScience-Paleontology.pdf**

---

## 🔧 SETUP INSTRUCTIONS

### Step 1: Install Python
- Download Python from: https://www.python.org/downloads/
- Choose version 3.8 or higher
- During installation, check "Add Python to PATH"

### Step 2: Install Required Libraries
Open your command line (Terminal on Mac/Linux, Command Prompt on Windows) and type:

```bash
pip install requests pandas matplotlib seaborn numpy networkx
```

**What each library does:**
- `requests`: Downloads data from websites
- `pandas`: Works with data tables (like Excel)
- `matplotlib`: Creates charts and graphs
- `seaborn`: Makes prettier visualizations
- `numpy`: Does mathematical calculations
- `networkx`: Creates network/graph visualizations

---

## 📖 UNDERSTANDING THE PALEOBIOLOGY DATABASE

### What is it?
The Paleobiology Database (PBDB) is a public database containing information about fossil occurrences from around the world. It includes:
- Taxonomic information (class, order, family, genus, species)
- Geographic locations (where fossils were found)
- Temporal information (when the organisms lived)
- Environmental context (what environment they lived in)

### The API URL Explained

Let's break down the URL we're using:

```
https://paleobiodb.org/data1.2/occs/list.json?
```
This is the base address for fossil occurrence data in JSON format.

**Parameters (what we're asking for):**

1. `base_name=Vertebrata` - We want all vertebrate fossils
2. `interval=Phanerozoic` - Time period: last ~541 million years
3. `pgm=gplates,scotese,seton` - Paleogeographic models for coordinates
4. `show=attr,class,classext,genus...` - All the types of information we want

---

## 🔍 STEP-BY-STEP CODE EXPLANATION

### STEP 1: Import Libraries

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter
```

**Think of this as:** Opening your toolbox and taking out the tools you need.

---

### STEP 2: Download the Data

```python
url = "https://paleobiodb.org/data1.2/occs/list.json?..."
response = requests.get(url, timeout=120)
data_json = response.json()
records = data_json.get('records', [])
df = pd.DataFrame(records)
```

**What's happening:**
1. We send a request to the database server
2. The server sends back data in JSON format (like a structured text file)
3. We convert this JSON to a DataFrame (a table structure)

**Real-world analogy:** You're asking a librarian (the server) for information about books (fossil data), and they give you a catalog (DataFrame) you can easily read.

---

### STEP 3: Explore the Data

```python
print(f"Dataset dimensions: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(df.head(3))
print(df.dtypes)
```

**What we're checking:**
- How many fossils (rows) do we have?
- How many pieces of information (columns) per fossil?
- What does the data look like?
- What type of data is in each column? (numbers, text, dates, etc.)

**Why this matters:** Before analyzing data, you need to understand what you have!

---

### STEP 4: Check Data Quality

```python
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100
```

**What we're checking:**
- Which columns have missing information?
- How much data is missing?

**Why this matters:** Missing data can affect our analysis. If a column is 90% empty, it might not be useful!

**Real-world example:** Imagine trying to study dinosaur diets, but only 10% of your specimens have preserved stomach contents. You need to know this limitation!

---

### STEP 5: Taxonomic Analysis

```python
n_classes = df['class'].nunique()
n_genera = df['genus'].nunique()
class_counts = df['class'].value_counts()
```

**What we're finding:**
- How many different classes are represented?
- How many genera?
- Which classes are most common?

**Scientific value:** This tells us about the diversity and sampling bias in our dataset.

---

### STEP 6: Temporal Distribution

```python
df['max_ma'] = pd.to_numeric(df['max_ma'], errors='coerce')
print(f"Oldest fossil: {df['max_ma'].max():.2f} Ma")
print(f"Youngest fossil: {df['min_ma'].min():.2f} Ma")
```

**What 'Ma' means:** Million years ago

**What we're finding:**
- The age range of our fossils
- Which time periods have the most fossils

**Scientific insight:** Are certain periods over-represented? This could indicate:
- Better preservation conditions
- More research effort
- Actual diversity peaks (like after mass extinctions)

---

### STEP 7: Geographic Distribution

```python
df['paleolng'] = pd.to_numeric(df['paleolng'], errors='coerce')
df['paleolat'] = pd.to_numeric(df['paleolat'], errors='coerce')
coords_available = df[['paleolng', 'paleolat']].notna().all(axis=1).sum()
```

**What we're checking:**
- How many fossils have location information?
- Where in the world are they distributed?

**Why paleocoordinates:** The Earth's continents have moved! Paleocoordinates show where that location was in the past.

**Example:** A Jurassic fossil from England might have paleocoordinates showing it was at a different latitude when the dinosaurs were alive!

---

### STEP 8: Create Visualizations

#### Bar Chart - Top Classes
```python
top_classes = df['class'].value_counts().head(10)
top_classes.plot(kind='barh')
```

**What it shows:** Which vertebrate classes dominate our dataset

**Questions to ask:**
- Why are some classes more common?
- Is this real diversity or sampling bias?

#### Histogram - Temporal Distribution
```python
df['max_ma'].hist(bins=50)
```

**What it shows:** How fossils are distributed across time

**Look for:**
- Gaps (mass extinctions?)
- Peaks (diversity increases?)
- Sampling biases

#### Scatter Plot - Geographic Distribution
```python
plt.scatter(df['paleolng'], df['paleolat'])
```

**What it shows:** Where (geographically) fossils have been found

**Questions to ask:**
- Are certain continents over-studied?
- Do we see patterns related to ancient geography?

---

## 🕸️ KNOWLEDGE GRAPHS: CONNECTING THE DOTS

### What is a Knowledge Graph?

A knowledge graph shows **relationships** between different pieces of information.

**Simple example:**
```
Tyrannosaurus rex (genus) 
    ↓ belongs to
Tyrannosauridae (family)
    ↓ belongs to
Theropoda (order)
    ↓ belongs to
Dinosauria (class)
```

### Types of Relationships We Can Show:

1. **Taxonomic Hierarchy:**
   - Class → Order → Family → Genus

2. **Temporal:**
   - Genus → "lived in" → Time Period

3. **Environmental:**
   - Genus → "found in" → Environment (marine, terrestrial, etc.)

4. **Geographic:**
   - Genus → "distributed in" → Geographic Region

### Building the Knowledge Graph

```python
relationships = []

# Create Class -> Order relationships
class_order = df[['class', 'order']].dropna().drop_duplicates()
for _, row in class_order.iterrows():
    relationships.append({
        'source': row['class'],
        'target': row['order'],
        'relationship': 'HAS_ORDER'
    })
```

**What this code does:**
1. Takes all unique Class-Order pairs
2. Creates a "relationship" showing Class has Order
3. Stores this in a list

**Why it's useful:** You can now query:
- "What orders belong to Mammalia?"
- "What genus lived during the Cretaceous?"
- "What environments did Theropods inhabit?"

---

## 🎯 RESEARCH QUESTIONS YOU CAN ANSWER

After completing this analysis, you can investigate:

### 1. Diversity Questions
- Which vertebrate class has the most genera?
- How has vertebrate diversity changed over time?
- Are there diversity hotspots in certain time periods?

### 2. Sampling Bias Questions
- Which continents are over-represented?
- Which time periods have the best fossil record?
- Are marine or terrestrial vertebrates better represented?

### 3. Evolutionary Questions
- What orders appeared after mass extinctions?
- How did geographic distribution change over time?
- What environmental transitions occurred?

### 4. Methodological Questions
- How complete is our data?
- Where should future fieldwork focus?
- What are the limitations of this dataset?

---

## 🚀 EXTENDING THE ANALYSIS

### Easy Extensions:
1. **Filter by specific group:** Change `base_name=Vertebrata` to `base_name=Mammalia`
2. **Focus on time period:** Change interval to `Mesozoic` or `Cenozoic`
3. **Add more visualizations:** Create pie charts, box plots, etc.

### Advanced Extensions:
1. **Statistical analysis:** Test for diversity trends over time
2. **Machine learning:** Predict environments from taxonomic data
3. **Interactive visualizations:** Use Plotly for interactive graphs
4. **Database queries:** Compare multiple taxonomic groups

---

## 🔍 COMMON ISSUES AND SOLUTIONS

### Problem 1: "ModuleNotFoundError"
**Solution:** Install the missing library
```bash
pip install [library_name]
```

### Problem 2: "Connection timeout"
**Solution:** 
- Check your internet connection
- Increase timeout value: `timeout=300`
- Try downloading smaller datasets first

### Problem 3: "KeyError" - Column doesn't exist
**Solution:** 
- Check if the column name is spelled correctly
- Check if that data is available in your query
- Use `if 'column_name' in df.columns:` to check first

### Problem 4: Too much missing data
**Solution:**
- Filter out rows with missing critical data
- Request different fields in your API query
- Focus analysis on available fields

---

## 📊 INTERPRETING YOUR RESULTS

### Good Scientific Practice:

1. **Be skeptical of your data:**
   - Is this pattern real or sampling bias?
   - What are the limitations?

2. **Consider alternatives:**
   - Could there be other explanations?
   - What additional data would help?

3. **Document everything:**
   - Keep notes on your decisions
   - Record why you filtered certain data
   - Note any unusual findings

4. **Visualize uncertainty:**
   - Show error bars when appropriate
   - Discuss data quality issues
   - Be honest about limitations

---

## 🎓 LEARNING OBJECTIVES CHECKLIST

By the end of this lecture, you should be able to:

- ✅ Download data from the Paleobiology Database API
- ✅ Load and explore data using pandas
- ✅ Assess data quality and completeness
- ✅ Create basic visualizations
- ✅ Understand taxonomic, temporal, and geographic patterns
- ✅ Build a simple knowledge graph
- ✅ Formulate research questions based on your data
- ✅ Identify limitations and biases in paleontological datasets

---

## 📚 ADDITIONAL RESOURCES

### Paleobiology Database:
- Main site: https://paleobiodb.org
- API documentation: https://paleobiodb.org/data1.2/
- Navigator (interactive): https://paleobiodb.org/navigator/

### Python Learning:
- Python for Data Analysis (book by Wes McKinney)
- Pandas documentation: https://pandas.pydata.org/docs/
- Matplotlib gallery: https://matplotlib.org/stable/gallery/

### Paleontology Data Science:
- PyRate (Bayesian analysis): https://github.com/dsilvestro/PyRate
- paleobioDB R package: https://cran.r-project.org/package=paleobioDB

---

## 🤔 DISCUSSION QUESTIONS FOR CLASS

1. Why might Actinopterygii (ray-finned fish) dominate the fossil record?

2. What does a gap in the temporal distribution tell us? Mass extinction, sampling bias, or preservation issues?

3. How can we distinguish between "true" diversity and "sampling" diversity?

4. Why are paleocoordinates important for understanding ancient biogeography?

5. What ethical considerations exist when working with fossil data?

6. How might climate change affect the fossil record we're creating today?

---

## 🎯 ASSIGNMENT IDEAS

### Beginner Level:
1. Modify the code to analyze a different vertebrate class
2. Create a poster showing the 5 most interesting findings
3. Write a 1-page summary of data limitations

### Intermediate Level:
1. Compare two different time periods statistically
2. Create an interactive visualization using Plotly
3. Build a more complex knowledge graph with 5+ relationship types

### Advanced Level:
1. Analyze diversity dynamics across mass extinction boundaries
2. Create a predictive model for fossil preservation
3. Combine PBDB data with modern biodiversity databases

---

## ✨ FINAL THOUGHTS

Data science is not just for computer scientists - it's a powerful tool for **all scientists**! 

The skills you learn here apply to:
- Literature reviews (text mining)
- Field data collection (databases)
- Lab results (statistical analysis)
- Grant writing (data visualization)

**Remember:** Every expert was once a beginner. Don't be afraid to:
- Make mistakes (that's how you learn!)
- Ask questions (there are no stupid questions!)
- Experiment (try changing the code!)
- Collaborate (work with your classmates!)

**The fossil record is incomplete, but with good data science practices, we can extract maximum insight from what we have.**

---

## 📞 GETTING HELP

### During Class:
- Raise your hand
- Ask your neighbor
- Post in the class forum

### Outside Class:
- Stack Overflow (for coding questions)
- PBDB mailing list (for database questions)
- Professor's office hours

**Good luck with your paleontological data adventures! 🦕🦖🐟**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
Developed by Matilde Pato & André Baptista as part of the Master Dissertation in Computer Science and Engineering.

- GitHub: [https://github.com/matpato/Paleo_DataScience](https://github.com/matpato/Paleo_DataScience)
- Email: [andrefbaptista2@gmail.com](mailto:andrefbaptista2@gmail.com) &
         [matilde.pato@isel.pt](mailto:matilde.pato@isel.pt)

---

*Document created for educational purposes*
*Feel free to share and modify for your students*
