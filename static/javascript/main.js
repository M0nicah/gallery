const img = document.querySelector('img');
const modal = document.getElementById('modal');

img.onclick = () => {
    alert('Image has been clicked')
//   console.log('clicked')
  modal.style.display = 'block';
}

