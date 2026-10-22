print("Hello, this is python")

"""
home_goals = 2
away_goals = 1
team_name = "Arsenal"
print(f"{team_name} scored {home_goals} goals and the away team scored {away_goals} goals.")

print("This shows home and away goals:",home_goals + away_goals)

print("Home goals:",home_goals)
print("Away goals:",away_goals)
print("Team name: ",team_name)

#kindly print a statement that shows number of players in a team and number of goals scored
#Output should look like this:
#Number of players in a team: 11
#Number of goals scored: 30


a=input("Enter number of players in a team: ")
b=input("Enter number of goals scored: ")
print("Number of players in a team: ",a)
print("Number of goals scored: ",b)
"""


team = "Esperence of Tunisia"
print(team)
goals_scored=[2,1,3,0,4,2,1,1,0,3,2,1,0,2,5]
goals_conceded=[1,1,2,0,2,0,1,2,3,2,2,1,1,2,1]

matches_played = len(goals_scored)
total_goals_scored = sum(goals_scored)
total_goals_conceded = sum(goals_conceded)

print("Matches played:",matches_played)
print("Total goals scored:",total_goals_scored)
print("Total goals conceded:",total_goals_conceded)
#print(f"{team} played {matches_played} matches, scored {total_goals_scored} goals and conceded {total_goals_conceded} goals.")

goal_difference = total_goals_scored - total_goals_conceded
print("Goal difference:",goal_difference)

avg_goals_scored = total_goals_scored / matches_played
avg_goals_conceded = total_goals_conceded / matches_played

print("Average goals scored per match:", avg_goals_scored)
print("Average goals conceded per match:", avg_goals_conceded)

wins=0
draws=0
losses=0

for i in range(matches_played):
    if goals_scored[i] > goals_conceded[i]:
        wins += 1
    elif goals_scored[i] == goals_conceded[i]:
        draws += 1
    else:
        losses += 1

print("Wins:", wins)
print("Draws:", draws)
print("Losses:", losses)

total_points = (wins * 3) + (draws * 1) +(losses * 0)
points_per_match = total_points / matches_played


print("=" * 60)
print("=" * 60)
print("=" * 60)
print("=" * 60)
print("Matches played:",matches_played)
print("Total goals scored:",total_goals_scored)
print("Total goals conceded:",total_goals_conceded)
print("Total points:", total_points)
print("Points per match:", points_per_match)
print("Wins:", wins)
print("Draws:", draws)
print("Losses:", losses)
print("Average goals scored per match:", avg_goals_scored)
print("Average goals conceded per match:", avg_goals_conceded)


