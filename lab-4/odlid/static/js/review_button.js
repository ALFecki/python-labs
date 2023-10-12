const reviewDescription = document.getElementById('review-description');
const reviewRating = document.getElementById('rating');
const submitButton = document.getElementById('submit-button');

reviewDescription.addEventListener('input', toggleSubmitButton);
reviewRating.addEventListener('input', toggleSubmitButton);

function toggleSubmitButton() {
  if (reviewDescription.value.trim() !== '' && reviewRating.value !== '') {
    submitButton.disabled = false;
  } else {
    submitButton.disabled = true;
  }
}