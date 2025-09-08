import pandas as pd

# Load the CSV file
df = pd.read_csv("id_grade.csv")

num_people_per_grade = int(
    input("Enter number of people to select from each grade: "))
student_id = int(input("Enter your Student ID: "))

# Remove the student with the given ID from the DataFrame
df = df[df['Perm ID'] != student_id]

# Select the specified number of people from each grade
sampled_df = df.groupby('Grade').apply(lambda x: x.sample(
    n=num_people_per_grade)).reset_index(drop=True)

# generate email list
email_list = sampled_df['Perm ID'].apply(lambda x: f"{x}@lcps.org")

# separate emails into groups of 75
email_groups = [email_list[i:i + 75] for i in range(0, len(email_list), 75)]

# store email list as text file with
with open("email_list.txt", "w") as f:
    for group in email_groups:
        f.write("\n".join(group) + "\n\n---------------------\n\n")
