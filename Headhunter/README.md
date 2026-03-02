
---

## 📁 Projeto 3: Candidate-Ranking-Automation

# Candidate Ranking Automation – Resume Screening with Python

## Project Overview
A practical automation tool built to solve a real HR problem: the time wasted manually filtering candidates who don't match job requirements.

Instead of opening spreadsheets one by one, this script processes hundreds of candidates in seconds and delivers a ranked list of the best fits based on skill relevance.

## The Problem It Solves
- HR teams spend hours screening resumes
- Inconsistent criteria lead to missed talent
- Manual filtering is error-prone and slow

## The Solution
This script automates the entire screening process:
- **Data Cleaning:** Standardizes names and skills using Pandas
- **Smart Ranking:** Assigns higher weights to key skills (Python, SQL) to push top candidates to the top
- **Instant Output:** Generates a clean, ready-to-use CSV file sorted by candidate score

## How It Works
1. Reads a CSV file with candidate data (name, skills, experience)
2. Cleans and standardizes the data
3. Applies a scoring system based on skill relevance
4. Ranks candidates from best to worst fit
5. Exports a new CSV with rankings ready for recruiters
