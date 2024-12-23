const container = document.querySelector('.container');

// Dynamically add hearts at random positions, angles, sizes, and animate them
function createHeart() {
  const heart = document.createElement('div');
  heart.className = 'heart';

  // Random position
  heart.style.top = Math.random() * 90 + '%';
  heart.style.left = Math.random() * 90 + '%';

  // Random size and rotation
  const randomSize = Math.random() * 0.5 + 0.5; // Scale between 0.5 and 1
  const randomAngle = Math.random() * 180; // Rotation between 0 and 360 degrees
  heart.style.transform = `scale(${randomSize}) rotate(${randomAngle}deg)`;

  // Add heart to container
  container.appendChild(heart);

  // Animate the heart (floating upwards)
  const animationDuration = 5000; // 5 seconds
  const startY = parseFloat(heart.style.top);
  const endY = startY - 10; // Move 10% upwards

  let startTime = null;
  function animateHeart(timestamp) {
    if (!startTime) startTime = timestamp;
    const elapsed = timestamp - startTime;
    const progress = Math.min(elapsed / animationDuration, 1); // Clamp between 0 and 1

    // Update heart's position
    const currentY = startY - progress * 10;
    heart.style.top = `${currentY}%`;
    heart.style.opacity = 1 - progress; // Fade out over time

    if (progress < 1) {
      requestAnimationFrame(animateHeart);
    } else {
      heart.remove(); // Remove heart after animation
    }
  }

  requestAnimationFrame(animateHeart);
}

// Generate a new heart every second
setInterval(createHeart, 1000);


// step2 페이지에서 부적 예시 이미지에 텍스트 동적으로 넣기
