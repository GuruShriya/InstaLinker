Insta Linker — High-Level Design

Goal

Insta Linker is a terminal app that finds the top 5 #gym videos from the last hour or last 24 hours.

Trending means: highest number of views. If 100 #gym videos were posted in the last hour, sort those 100 by views (highest first) and display the first 5.

User flow

flowchart TD
    A[Open app] --> B[Welcome screen]
    B --> C[Choose time: last hour or last 24 hours]
    C --> D[Get #gym videos]
    D --> E[Keep videos in selected time]
    E --> F[Sort by views and choose top 5]
    F --> G[Show result table]
    G -->|Press R| B
    G -->|Press Q| H[Close app]

Simple explanation: you choose a time; the app gets #gym videos, removes older ones, keeps the five with most views, and shows them. Pressing R starts again without closing the program.

Screens

1. Welcome screen

Welcome to InstaLinker
Choose a time range:
1. Last hour
2. Last 24 hours

2. Results screen

Top 5 #gym videos — Last hour
| Link | Username | Shares |
|------|----------|--------|
| ...  | ...      | ...    |

Happy to help. Press R to reset or Q to quit.

The app uses views to choose the top 5. Views can be shown later; the required columns remain Link, Username, and Shares.

System flow

flowchart LR
    U[User] --> T[TUI]
    T --> S[Insta Linker service]
    S --> I[Instaloader]
    I --> G[Instagram]
    G --> I --> S --> T

Part Job

TUI - Shows screens and reads R / Q.

Service - Filters by time, sorts by views, and returns five.

Instaloader - Gets Instagram hashtag-post data.

Instagram - Source of #gym posts.

Data needed per video
- Link
- Username
- Post timestamp
- View count — used for ranking
- Share count — shown in the table when available

If share count is not available from Instaloader, show N/A, not 0.

Main behaviour

stateDiagram-v2
    [*] --> Welcome
    Welcome --> Loading: User selects time
    Loading --> Results: Top 5 found
    Loading --> Error: Fetch fails or no data
    Results --> Welcome: R
    Error --> Welcome: R
    Welcome --> [*]: Q
    Results --> [*]: Q

The program keeps running until Q or Ctrl+C.

Assumptions and constraints

Instaloader is the first data-source choice; the ADR explains why.

The app makes read-only requests; it does not post or modify content.

Instagram may limit requests or change available data.

A result is based on posts returned to the configured account/session, not necessarily every video on Instagram.

Next documents

LLD: Python modules, TUI library, retries, and tests.

Open questions: Are views and shares reliably available? How will login/session work?

ADR: Record Instaloader vs Meta Graph API and their trade-offs.