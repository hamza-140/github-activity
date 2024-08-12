<div align="center">
    
  # GitHub Activity Tracker
  
  [Overview](#🎯-overview) •
  [Features](#✨-features) •
  [Getting Started](#🚀-getting-started) •
  [Usage](#📘-usage) •
  [API](#📚-api)
  
</div>
  
---

## 🎯 Overview

This project is a Python script that fetches and displays GitHub activity for a given user. It categorizes activities into different types, such as pushes, issues, pull requests, etc., and displays the number of commits or interactions per repository.

## ✨ Features

- **Fetch GitHub Activity**: Retrieves recent activities of a user from GitHub.
- **Categorize Events**: Organizes events into categories like Pushes, Issues, Pull Requests, etc.
- **Count Events**: Counts the number of activities per repository.
- **Display Results**: Outputs the count of activities in a readable format.

## 🚀 Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Requests library (can be installed via `pip install requests`)

### Installation

Clone the repository:

   ```bash
   git clone https://github.com/hamza-140/github-activity.git
   cd github-activity
   ```
Install the required dependencies:

```bash
pip install requests
```
### Usage

Run the script by providing a GitHub username as an argument:

```bash

python github-activity.py <username>
```
For example:

```bash
python github-activity.py forem
```
This will fetch and display GitHub activity for the user forem.

### 📚 API
This section documents the main functions and classes of the script.

### display(type, dict)
Displays the number of commits or interactions for each repository based on the event type.
 | Parameter  | Type   | Description                                   |
  | ---------- | ------ | --------------------------------------------- |
  | `type`    | String | The type of event (e.g., Push, Issues).                        |
  | `dict` | dict | A dictionary containing repository names and counts.      |
  | `dict` | dict | A dictionary containing repository names and counts.      |