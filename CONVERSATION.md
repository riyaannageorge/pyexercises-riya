# Campaign Audit Project – AI Conversation Log

## 1. Project Overview
The objective was to develop a Python program to analyse advertising campaign data from a CSV file, calculate performance metrics and conduct a five-question campaign audit quiz.

## 2. Planning the Program
I structured the program using separate functions:
- `read_campaigns()` – Reads campaign data from the CSV file.
- `calculate_metrics()` – Calculates CTR, CPA and ROAS.
- `get_player_name()` – Collects the player's name.
- `run_quiz()` – Asks five questions and checks answers.
- `save_result()` – Saves the player's score and date in result.csv.

## 3. Data Processing and Calculations
The program processes campaign data and calculates:
- CTR = Clicks / Impressions
- CPA = Cost / Conversions
- ROAS = Revenue / Cost

I also handled European decimal commas and campaigns with empty impressions or zero conversions.

## 4. Testing and Debugging
I ran the Python program using the terminal and checked the campaign calculations.

The program successfully displayed campaign performance metrics, identified the best campaign and launched the quiz.

I also tested the five quiz questions and checked that the answers were evaluated correctly.

## 5. Quiz Results
The five correct answers were:

1. Best CTR: Aurora Launch
2. Highest CPA: Blog Traffic
3. Campaigns with ROAS above 3: 7
4. Channel with the most conversions: YouTube Ads
5. Average CTR: 2.60%

Final quiz score: 5/5.

## 6. Saving Results
The program successfully created result.csv containing:
- Player Name
- Score
- Date

The program was tested successfully and completed the campaign audit project.

## 7. AI Tutor Setup and Troubleshooting

I also attempted to configure the course AI tutor using an API provider.

- I first tried configuring the tutor with different model providers.
- I encountered a model availability error when using Gemini.
- I then tried Groq and created an API key.
- The tutor returned an authentication error (error code 1010).
- I checked the API endpoint and model configuration in the `.env` file.
- A direct test of the Groq models endpoint returned HTTP 200.
- A direct test of the Groq chat endpoint also returned HTTP 200.
- However, running `python tutor.py --check` continued to return the key refusal error.
- I inspected the tutor's `ask_model()` function but did not resolve the issue.

The AI tutor setup remained unsuccessful. I decided not to make further changes because the main campaign audit program was already working correctly.

The campaign audit program was tested successfully and achieved a quiz score of 5/5.