const students = [];

// Add student
function addStudent (name, score) {
score = Number(score);
score = score ?? 0;
name = name.trim().toUpperCase();
students.push({ name, score})
}

// Get Grades
function getGrades() {
    return students.map((student) =>{
        let grade = "F";
        
        if(student.score >= 90) grade = "A";
        else if(student.score >= 75) grade = "B";
        else if(student.score >= 50) grade = "C";
        else if(student.score >= 50) grade = "C";
        return{...student,grade}
    })
}

// Top Scores
function getTopScores() {
return students.filter((student) => student.score >= 75)
}

// Find Student
function findStudent (name) {
return students.find((student) => student.name == name)
}

// Check Failures
function hasFailures() {
    return students.some((student) => student.score < 35)
}

// Display data
function displayAll() {
    const graded = getGrades();
    console.log("Student Data");
    console.log("All Student with Grades");
    console.log("Name | Score | Grade")
    graded.forEach((student) => {
        console.log(`${student.name} | ${student.score} | ${student.grade}`)
})
}

// Adding Students
addStudent("John", "91");
addStudent("Ravi", "82");
addStudent("Sneha", "44");
addStudent("Aarti", "29");

// Display Students Data
displayAll();

// Top Scores
console.log("\n Top Scores: ")
console.log(getTopScores())

// Find Student
console.log("\n Searching for Ravi:")
console.log(findStudent ("RAVI"))

// Check Failures
console.log("\n Any Failures?")
console.log(hasFailures() ? "Yes some students failed": "No Failures")

// node ./student-score.js
