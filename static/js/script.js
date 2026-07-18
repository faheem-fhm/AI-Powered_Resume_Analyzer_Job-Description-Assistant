// ==============================
// Elements
// ==============================

const resumeInput = document.getElementById("resume_file");
const resumeName = document.getElementById("resume-name");

const jobInput = document.getElementById("job_file");
const jobName = document.getElementById("job-name");

const loader = document.getElementById("loader");
const extractBtn = document.getElementById("extract-btn");

const errorAlert = document.getElementById("error-alert");
const themeBtn = document.getElementById("theme-btn");

// ==============================
// Resume Preview
// ==============================

resumeInput.addEventListener("change", function () {

    if (this.files.length > 0) {
        resumeName.innerHTML = "📄 " + this.files[0].name;
    } else {
        resumeName.innerHTML = "No Resume Selected";
    }

});

// ==============================
// Job Preview
// ==============================

jobInput.addEventListener("change", function () {

    if (this.files.length > 0) {
        jobName.innerHTML = "📄 " + this.files[0].name;
    } else {
        jobName.innerHTML = "No Job Description Selected";
    }

});

// ==============================
// Form Submit
// ==============================

document.getElementById("upload-form").addEventListener("submit", function (e) {

    if (resumeInput.files.length === 0) {

        e.preventDefault();
        errorAlert.innerHTML = "❌ Please select a Resume.";
        errorAlert.style.display = "block";
        return;
    }

    if (jobInput.files.length === 0) {

        e.preventDefault();
        errorAlert.innerHTML = "❌ Please select a Job Description.";
        errorAlert.style.display = "block";
        return;
    }

    errorAlert.style.display = "none";

    loader.style.display = "block";
    extractBtn.disabled = true;
    extractBtn.innerHTML = "Extracting...";

});

// ==============================
// Page Load
// ==============================

window.onload = function () {

    loader.style.display = "none";

};

// ==============================
// Theme
// ==============================

if (localStorage.getItem("theme") === "light") {

    document.body.classList.add("light");
    themeBtn.innerHTML = "☀️";

}

themeBtn.addEventListener("click", function () {

    document.body.classList.toggle("light");

    if (document.body.classList.contains("light")) {

        localStorage.setItem("theme", "light");
        themeBtn.innerHTML = "☀️";

    } else {

        localStorage.setItem("theme", "dark");
        themeBtn.innerHTML = "🌙";

    }

});