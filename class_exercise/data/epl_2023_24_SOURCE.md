# Data source — English Premier League 2023/24

**File:** `epl_2023_24.csv` (380 matches — one full real season)

## Where it comes from
Free historical results from **football-data.co.uk**:

- Landing page (all England divisions): https://www.football-data.co.uk/englandm.php
- Direct file used here (Premier League, season 2023/24): https://www.football-data.co.uk/mmz4281/2324/E0.csv

The data is **real** — actual Premier League results — and is included here already downloaded so the
notebook runs fully offline. You do not need to download anything; the CSV is in this `data/` folder.

## Usage
football-data.co.uk provides this data **free for personal and educational use** and asks only for a link
back to the site. This course uses it for teaching and credits the source above.

## How it was prepared
Downloaded once, then trimmed to a clean teaching subset and renamed to readable column names. To refresh
to another season, change the season code in the URL (e.g. `2324` → `2223`) and re-run the same trim.

## Columns
| column | meaning |
|---|---|
| `date` | match date (dd/mm/yyyy) |
| `home_team`, `away_team` | the two clubs |
| `home_goals`, `away_goals` | full-time goals |
| `result` | `H` home win · `D` draw · `A` away win |
| `ht_home_goals`, `ht_away_goals` | half-time goals |
| `home_shots`, `away_shots` | shots |
| `home_shots_on_target`, `away_shots_on_target` | shots on target |
| `home_corners`, `away_corners` | corners |
| `home_yellows`, `away_yellows` | yellow cards |
| `home_reds`, `away_reds` | red cards |
| `referee` | match referee |

## Note on the course's other data
The rest of this course uses a **fictional** universe (Lagos FC, Accra United, players like Okocha…) so the
teaching examples stay simple and consistent. This bonus lab is the exception: it is **real-world data**, so
you can feel what messy, genuine sports data is like and cite where you got it — exactly what you'll do on the job.
