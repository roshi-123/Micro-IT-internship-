// JavaScript for typed text effect in search input

// Swiper initialization

// help center
// Function to show the selected section
function showSection(sectionId) {
  // Get all the content sections
  const sections = document.querySelectorAll('.content');

  // Loop through all sections and hide them
  sections.forEach(section => {
      section.style.display = 'none'; // Hide all sections
  });

  // Show the selected section
  const sectionToDisplay = document.getElementById(sectionId);
  if (sectionToDisplay) {
      sectionToDisplay.style.display = 'block'; // Display the clicked section
  }
}

// Function to toggle FAQ answers
function toggleFAQ(question) {
  let answer = question.nextElementSibling;
  answer.style.display = answer.style.display === "block" ? "none" : "block";
}

// Default: Show FAQ section on page load
window.onload = function() {
  showSection('faq'); // Display FAQ section initially
};
// msgs


