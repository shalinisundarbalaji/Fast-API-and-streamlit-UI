import streamlit as st

st.title("Student Grade Manager")

# Store students
if "students" not in st.session_state:
    st.session_state.students = [
        {"Name": "Priya", "Mark": 92},
        {"Name": "Arun", "Mark": 78}
    ]

# Input
name = st.text_input("Name", "Divya")
mark = st.number_input("Mark", min_value=0, max_value=100, value=83)

# Add button
if st.button("Add"):
    st.session_state.students.append({
        "Name": name,
        "Mark": mark
    })

# Calculate grade
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# Display table
st.write("### Student Details")

for student in st.session_state.students:
    student["Grade"] = get_grade(student["Mark"])

# Calculate statistics
marks = [student["Mark"] for student in st.session_state.students]

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

# Show table
st.table(st.session_state.students)

# Show statistics
st.write(f"**Average:** {average:.1f}")
st.write(f"**Highest:** {highest}")
st.write(f"**Lowest:** {lowest}")