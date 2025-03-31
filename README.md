## 📌 Project Objective  
The goal of this project was to **implement a public transport route search system for the city of Wrocław**, utilizing two popular shortest path algorithms: **Dijkstra's algorithm** and the **A\* algorithm**, as well as data provided by the city of Wrocław.  

---

## 📂 Data  
The program is based on the **`connection_graph.csv`** file, located in **`data_sources`** directory, which was created by merging datasets available from [**"Open Data Wrocław"**](https://opendata.cui.wroclaw.pl/dataset/rozkladjazdytransportupublicznegoplik_data).  
The dataset includes:  
✅ **Stops and their geographical locations**  
✅ **Connections between stops**  
✅ **Departure and arrival times**  
✅ **Transit lines operating on these routes**  

📅 The data used in this project is from **March 1, 2023**.  

### 🔍 Simplifications  
🚫 The program assumes that users travel **exclusively by public transport**, as the dataset only includes public transport stops. Therefore, **nearby stops that could be reached on foot to further minimize travel time are not considered unless they are directly connected to the current stop**.  
📍 **Stop Merging:** All stops with the same name were merged, and their geographic coordinates were averaged to avoid inefficient routing, e.g. at "Plac Grunwaldzki" multiple stops.  

---

## ⚙️ Application Features  
The application is primarily designed to search for **public transport connections within Wrocław**. However, several customization options are available to modify the search criteria:  

### 🔢 Algorithm Selection  

#### 🟢 **Dijkstra's Algorithm**  
✔️ A **classical, optimal**, but **slower** algorithm for finding the shortest path.  
✔️ **Always optimizes routes based on travel time.**  

#### 🔵 **A* Algorithm**  
✔️ A **heuristic-based, faster** algorithm for finding the shortest path.  
✔️ Uses heuristics to estimate path costs.  
✔️ **Euclidean distance** is used as an effective heuristic.  
✔️ Can optimize based on **travel time** or **number of transfers**.  

### 🎯 Optimization Criteria  

#### ⏳ **Optimization by Travel Time**  
✅ Minimizes the **total travel time** without considering the number of transfers.  
⚠️ May lead to **excessive transfers** as comfort is not a factor.  

#### 🔄 **Optimization by Number of Transfers**  
✅ Minimizes the **travel time and number of transfers**.  
✅ Prioritizes staying on the same bus/tram if it doesn't significantly increase travel time.  
🔬 **Experimental approach** (described in project documentation).  

### ⏰ Departure Time Selection  
🕒 By default, the program uses **local time**.  
📆 Users can **select a departure time** to plan future trips or review past departures.  

### 🔎 Step-by-Step Route Breakdown  
📊 After execution, the algorithm presents travel data as **route segments**, where each segment represents a single transit line.  
📜 If a line passes through multiple stops, users can **expand details** to view intermediate stops.  

---

## 🚀 Application Setup Instructions  
The application was developed using **Python 3.10.9**. If execution fails, using this version is recommended.  

### 📥 Installation  
Navigate to the project's main folder (where `main.py` is located) and run the following commands:  
```bash
pip install -r requirements.txt
python main.py
```

### ⚡ Running the Application  
The application can be launched with an optional **`--mode`** argument:  
```bash
python main.py --mode console
```
🖥️ This starts the **console mode**, which is more difficult to operate than the default **graphical interface**.  

---

## 📑 Detailed Description of Libraries, Scripts, and Algorithms  
📄 A document containing a **detailed problem analysis** and **explanation of the implemented solutions** is included with the project:  
- 📘 [**Documentation**](documentation/SPDocumentation.pdf)  
- 📙 [**Documentation (Polish)**](documentation/SPDocumentation_PL.pdf)  

---
