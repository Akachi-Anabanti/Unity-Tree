export default function adjustHeight(container) {
    const cards = container.value.querySelectorAll('.children-card');
    const lastCard = cards[cards.length -1];
    const rectContainer = container.value.getBoundingClientRect();
    const rectLastCard = lastCard.getBoundingClientRect();
    const height = rectContainer.height - (rectLastCard.height / 2);
    container.value.style.setProperty('--dynamic-height', `${height}px`);
  }
