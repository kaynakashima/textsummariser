import pdfplumber
from transformers import pipeline
from huggingface_hub import login

# Authenticate with hugging face token
login(token="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")

# Load a summarization model using Hugging Face's Inference API
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """
TOKYO (Dec 19): The Bank of Japan (BOJ) kept interest rates unchanged on Thursday and its governor offered few clues on how soon it could push up borrowing costs, sending the yen and bond yields tumbling on fresh doubts over the near-term chances of a rate hike.

As widely expected, the nine-member board maintained its short-term policy rate at 0.25% in a sign policymakers preferred to tread cautiously amid uncertainty over US president-elect Donald Trump's economic plans.

But hawkish board member Naoki Tamura dissented and proposed, unsuccessfully, to raise interest rates to 0.5% on the view that inflationary risks were building.

The BOJ's meeting concluded hours after the US Federal Reserve cut interest rates but signalled a more cautious path of easing next year, sending global stocks sharply lower.

BOJ Governor Kazuo Ueda reiterated the central bank's resolve to keep raising rates from their current very low levels if the economy and prices move in line with its forecasts.

Asked why the BOJ stood pat, Ueda told a news conference that the bank preferred to await data on whether wages would retain their upward momentum next year, and to gain more clarity on Trump's economic policies.

"Taken together, the likelihood of Japan's economy moving in line with our forecast is heightening. But we'd like one notch more information to believe we can raise interest rates. That includes the sustainability of wage increases," he said.

Investors widely interpreted his remarks as diminishing the chance of a rate hike at the BOJ's next meeting in January. The dollar rose to ¥157.075, up 1.4% on the day and its highest since July.

"There's a chance the BOJ might wait until March, given he stressed the need to scrutinise next year's wage negotiations," said Junki Iwahashi, senior economist at Sumitomo Mitsui Trust Bank.

Ueda said the BOJ would not necessarily need to wait for a particular event or piece of data to hike rates, although it could take its time as Japan's underlying inflation remained moderate. The rise in import prices, a key contributor to inflation that has been blamed in part on the weak yen, was slowing, he added.

The yen has been languishing in recent months near its lowest in 30 years as Japanese interest rates lag other major economies. Market players have pointed to yen weakness as a key reason for the BOJ to hike rates or get more hawkish in its communications.

Steady recovery
The BOJ holds it next policy meeting on Jan 23-24. The central bank's report on regional economies, due on Jan 9, will offer clues on whether wage hikes are broadening out and taking root among smaller firms.

BOJ Deputy Governor Ryozo Himino will deliver a speech and hold a news conference on Jan 14, which may offer further hints on whether the bank will raise rates in January.

The next window for a move after January will come two months later, on March 18-19.

The BOJ on Thursday also released its review of the pros and cons of monetary easing tools, including negative interest rates, deployed during its 25-year battle with deflation.

The review warned of various side effects from unconventional monetary easing measures, rendering them unsuitable as a substitute for traditional tools like interest rate cuts.

The BOJ ended negative interest rates in March and raised its short-term policy target to 0.25% in July. It has signalled a readiness to hike again if wages and prices move as projected.

All respondents in a Reuters poll taken earlier this month expected the BOJ to raise rates to 0.50% by end-March, although they had been divided on whether the move would come in December, January or March.

Japan's economy expanded an annualised 1.2% in the three months to September, slowing from the previous quarter's 2.2% increase, with consumption up a feeble 0.7%.

BOJ policymakers hope that workers' regular pay, which recently has been rising at an annual pace of 2.5% to 3%, keeps increasing and supports consumption.

There are growing signs that companies are keen to continue hiking pay due to intensifying labour shortages, boding well for the BOJ's plan to keep raising interest rates gradually.

But slowing demand in China and uncertainty over the fallout from Trump's policies could weigh on corporate profits and discourage some of them from boosting pay.

Uploaded by Chng Shear Lane
"""

#using the summariser to generate a summary and print it out

print(summarizer(ARTICLE, max_length=100, min_length=30, do_sample=False))










