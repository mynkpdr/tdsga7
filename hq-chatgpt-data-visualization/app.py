# Email for verification: 23f3004197@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

# 1. Load the employee data
data = """
employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,IT,Asia Pacific,72.66,9,3.6
EMP002,R&D,Asia Pacific,66.47,3,4.7
EMP003,Marketing,Europe,67.93,7,4.6
EMP004,Finance,Latin America,93.33,2,3.5
EMP005,Sales,Africa,73.27,7,4.7
"""

from io import StringIO
df = pd.read_csv(StringIO(data))

# 2. Calculate the frequency count for the "Marketing" department
marketing_count = df['department'].value_counts().get('Marketing', 0)
print(f"Number of employees in Marketing department: {marketing_count}")

# 3. Create a histogram showing the distribution of departments
plt.figure(figsize=(8, 6))
sns.countplot(x='department', data=df, palette='Set2')
plt.title('Employee Count by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as a PNG image
plt.savefig('department_distribution.png')
plt.show()

# 4. Save results and visualization as HTML
html_content = f"""
<html>
<head><title>Employee Performance Analysis</title></head>
<body>
<h1>Employee Performance Analysis</h1>
<p>Email for verification: 23f3004197@ds.study.iitm.ac.in</p>
<p>Number of employees in Marketing department: {marketing_count}</p>
<h2>Department Distribution</h2>
<img src='department_distribution.png' alt='Department Distribution Histogram'>
</body>
</html>
"""

with open("employee_analysis.html", "w") as file:
    file.write(html_content)

print("HTML file 'employee_analysis.html' has been generated.")
