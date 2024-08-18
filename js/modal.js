function main() {
  const photos = document.querySelectorAll('.gallery__frame--picture')
  const videos = document.querySelectorAll('.gallery__frame--video')
  photos.forEach((photo) => {
    photo.addEventListener('click', (e) => modalePhoto(e))
  })
  videos.forEach((video) => {
    video.addEventListener('click', (e) => modaleVideo(e))
  })
}

function modalePhoto(e) {
  let modal = document.createElement('section')
  modal.className = 'modal'
  let frame = document.createElement('div')
  frame.className = 'modal__frame'
  let close = document.createElement('p')
  close.innerText = 'X'
  close.className = 'modal__frame--close'
  let video = document.createElement('img')
  video.src = e.target.src
  video.alt = e.target.alt
  video.className = 'modal__frame--picture'

  frame.appendChild(close)
  frame.appendChild(video)
  modal.appendChild(frame)

  document
    .querySelector('body')
    .insertBefore(modal, document.querySelector('.footer'))

  modal.addEventListener('click', (e) => deleteModal(e))
  close.addEventListener('click', (e) => deleteModal(e))

  function deleteModal(e) {
    if (e.target !== video && e.target !== frame) {
      modal.removeEventListener('click', deleteModal)
      close.removeEventListener('click', deleteModal)
      modal.remove()
    }
  }
}

function modaleVideo(e) {
  let modal = document.createElement('section')
  modal.className = 'modal'
  let frame = document.createElement('div')
  frame.className = 'modal__frame'
  let close = document.createElement('p')
  close.innerText = 'X'
  close.className = 'modal__frame--close'
  let video = document.createElement('video')
  video.controls = true
  video.className = 'modal__frame--picture'
  const sources = e.target.querySelectorAll('source')
  console.log(sources)
  const sourcesClone = []
  sourcesClone[0] = sources[0].cloneNode(true)
  sourcesClone[1] = sources[1].cloneNode(true)
  console.log(sourcesClone)

  frame.appendChild(close)
  frame.appendChild(video)
  modal.appendChild(frame)
  sourcesClone.forEach((source) => {
    video.appendChild(source)
  })

  document
    .querySelector('body')
    .insertBefore(modal, document.querySelector('.footer'))

  modal.addEventListener('click', (e) => deleteModal(e))
  close.addEventListener('click', (e) => deleteModal(e))

  function deleteModal(e) {
    if (e.target !== video && e.target !== frame) {
      modal.removeEventListener('click', deleteModal)
      close.removeEventListener('click', deleteModal)
      modal.remove()
    }
  }
}

main()
