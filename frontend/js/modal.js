function main() {
  const photos = document.querySelectorAll('.gallery__frame--picture')
  photos.forEach((photo) => {
    photo.addEventListener('click', (e) => modale(e))
  })
}

function modale(e) {
  let modal = document.createElement('section')
  modal.className = 'modal'
  let frame = document.createElement('div')
  frame.className = 'modal__frame'
  let close = document.createElement('p')
  close.innerText = 'X'
  close.className = 'modal__frame--close'
  let picture = document.createElement('img')
  picture.src = e.target.src
  picture.alt = e.target.alt
  picture.className = 'modal__frame--picture'

  frame.appendChild(close)
  frame.appendChild(picture)
  modal.appendChild(frame)

  document
    .querySelector('body')
    .insertBefore(modal, document.querySelector('.footer'))

  modal.addEventListener('click', (e) => deleteModal(e))
  close.addEventListener('click', (e) => deleteModal(e))

  function deleteModal(e) {
    if (e.target !== picture && e.target !== frame) {
      modal.removeEventListener('click', deleteModal)
      close.removeEventListener('click', deleteModal)
      modal.remove()
    }
  }
}

main()
