# Submitted to New Hacks 2023

# A Comprehensive Guide on prozon.ai

>  Have you ever struggled to choose between products? prozon.ai will make your decision for you, while taking into consideration your preferences, helping you make the best purchasing choice!

## Project Statistics

<p align="center">
    <a href="https://github.com/simple-icons/simple-icons/actions?query=workflow%3AVerify+branch%3Adevelop">
        <img src="https://img.shields.io/github/actions/workflow/status/simple-icons/simple-icons/verify.yml?branch=develop&logo=github&label=tests" alt="Build status"/>
    </a>
</p>

<p align="center">
    <a href="https://www.npmjs.com/package/simple-icons"><img src="https://img.shields.io/npm/v/simple-icons.svg?logo=npm" alt="NPM version"/></a>
    <a href="https://github.com/{owner}/{repo}/pulls">
    <img src="https://img.shields.io/badge/pull%20requests%20merged-4-blue" alt="Pull Requests Merged">
    </a>
    <a href="https://github.com/{owner}/{repo}/commits">
    <img src="https://img.shields.io/badge/commits-100+-blue" alt="GitHub Commits"> <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/lucyqqi/newhacks">
<br/><br/>
    <img src="https://raw.githubusercontent.com/BraveUX/for-the-badge/master/src/images/badges/0-percent-optimized.svg" />
                <img src="https://raw.githubusercontent.com/BraveUX/for-the-badge/master/src/images/badges/60-percent-of-the-time-works-every-time.svg" />
</a>

</p>

## Inspiration

The inspiration behind our project, Prozon.ai, stemmed from the common issue of indecisiveness that many people face when shopping online. We recognized that the abundance of choices and information available can overwhelm consumers, leading to extended decision-making processes. This inspired us to create a solution that simplifies and streamlines the decision-making process for online shoppers.

## What it does

Prozon.ai is a website designed to assist users in making informed purchasing decisions. It accomplishes this by taking two Amazon product links provided by the user and generating a comparative chart that details the features of each item. The platform then suggests the optimal choice based on the user's unique requirements and preferences.

## How we built it

Our project was developed using a combination of technologies and tools. We distributed tasks between the frontend and backend development teams, using GitHub for collaboration. The process involved:

- Developing the initial algorithm for determining the most optimal product.
- Exploring various web scraping methods to extract data from Amazon.
- Finalizing the web scraping approach, including using Selectorlib for non-recurring data and BeautifulSoup for elements like reviews.
- Integrating the frontend and backend using Flask to create a full-stack application.

Technologies and tools used in the project include:
- Tailwind CSS
- CSS
- HTML
- JavaScript
- Python
- OpenAI API
- Python Selectorlib
- Python BeautifulSoup

## Challenges we ran into

We encountered several challenges during the development of Prozon.ai:

1. **Web Scraping Amazon**: Initially, we attempted to use BeautifulSoup and Selenium for web scraping. However, we faced issues with Captchas produced by Amazon, hindering data retrieval. To overcome this, we adopted a more primitive web scraper called Selectorlib, which had limitations in isolating specific CSS chunks and extracting text.

2. **Connecting Frontend and Backend**: Integrating the frontend and backend components to create a cohesive full-stack application was a challenging task. We needed to find an efficient solution for this, and we successfully accomplished it by using Flask.

## Accomplishments that we're proud of

We are proud of several accomplishments in developing Prozon.ai:

- Successfully overcoming the challenges of web scraping by adapting to the limitations of web scraping tools.
- Creating a user-friendly and efficient platform for comparing and selecting products, helping users make better decisions.

## What we learned

Through the development of Prozon.ai, we learned valuable lessons about web scraping, backend/frontend integration, and the importance of adapting to challenges. We gained a deeper understanding of technology and tools used in the project, enhancing our skills in these areas.

## What's next for Prozon.ai

In the future, we aim to expand the capabilities of Prozon.ai. Some of the potential improvements include:

- Implementing a rating system for all items, allowing users to rate products they have used.
- Further enhancing the user experience with additional features and improvements.
- Continuously improving our web scraping methods for more accurate and comprehensive data retrieval.

Stay tuned for updates and enhancements to make Prozon.ai an even more valuable tool for online shoppers.

